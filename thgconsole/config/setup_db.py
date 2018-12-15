import sqlite3, os, string, hashlib, random
from datetime import date,datetime

###################################################
#
# Default values for the config
#
###################################################

# Staging Key is set up via environmental variable
# or via command line. By setting RANDOM a randomly
# selected password will automatically be selected
# or it can be set to any bash acceptable character
# set for a password.

STAGING_KEY = os.getenv('STAGING_KEY', "BLANK")
punctuation = '!#%&()*+,-./:;<=>?@[]^_{|}~'

# otherwise prompt the user for a set value to hash for the negotiation password
if STAGING_KEY == "BLANK":
    choice = input("\n [>] Enter server negotiation password, enter for random generation: ")
    if choice == "":
        # if no password is entered, generation something random
        STAGING_KEY = ''.join(random.sample(string.ascii_letters + string.digits + punctuation, 32))
    else:
        STAGING_KEY = hashlib.md5(choice).hexdigest()
elif STAGING_KEY == "RANDOM":
    STAGING_KEY = ''.join(random.sample(string.ascii_letters + string.digits + punctuation, 32))

# Calculate the install path. We know the project directory will always be the parent of the current directory. Any modifications of the folder structure will
# need to be applied here.
INSTALL_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/"

# an IP white list to ONLY accept clients from
#   format is "192.168.1.1,192.168.1.10-192.168.1.100,10.0.0.0/8"
IP_WHITELIST = ""

# an IP black list to reject accept clients from
#   format is "192.168.1.1,192.168.1.10-192.168.1.100,10.0.0.0/8"
IP_BLACKLIST = ""

# default credentials used to log into the RESTful API
API_USERNAME = "empireadmin"
API_PASSWORD = ''.join(random.sample(string.ascii_letters + string.digits + punctuation, 32))

# the 'permanent' API token (doesn't change)
API_PERMANENT_TOKEN = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(40))

# default obfuscation setting
OBFUSCATE = 0

# default obfuscation command
OBFUSCATE_COMMAND = r'Token\All\1'
###################################################
#
# Database setup.
#
###################################################

conn = sqlite3.connect('%s/thg.db'%INSTALL_PATH)

c = conn.cursor()

# try to prevent some of the weird sqlite I/O errors
c.execute('PRAGMA journal_mode = OFF')

c.execute('DROP TABLE IF EXISTS config')

c.execute('''CREATE TABLE config (
    "staging_key" text,
    "install_path" text,
    "ip_whitelist" text,
    "ip_blacklist" text,
    "autorun_command" text,
    "autorun_data" text,
    "rootuser" boolean,
    "api_username" text,
    "api_password" text,
    "api_current_token" text,
    "api_permanent_token" text,
    "obfuscate" integer,
    "obfuscate_command" text
    )''')

#lembra de criar metodo para add datetime na hora da inicializacao da restapi

#database api_keys
c.execute('''CREATE TABLE "api_keys"(
    "token" text,
    "created_at" text, 
    "updated_at" text    
)''')


"""
"created_at" text,
"updated_at" text)
"""

#add_index "automatic_exploitation_match_results", ["match_id"], name: "index_automatic_exploitation_match_results_on_match_id", using: :
#add_index "automatic_exploitation_match_results", ["run_id"], name: "index_automatic_exploitation_match_results_on_run_id", using: :btree
c.execute('''CREATE TABLE "automatic_exploitation_match_results"(
    "match_id" integer,
    "run_id"   integer,
    "created_at" text,
    "updated_at" text)''')

#add_index"automatic_exploitation_match_results", ["match_id"], name: "index_automatic_exploitation_match_results_on_match_id", using::btree
#add_index"automatic_exploitation_match_results", ["run_id"], name: "index_automatic_exploitation_match_results_on_run_id", using::btree
c.execute('''CREATE TABLE "automatic_exploitation_match_sets" (
    "workspace_id" integer ,
    "user_id" integer,
    "created_at" text,
    "updated_at" text)''')

#add_index"automatic_exploitation_match_sets", ["user_id"], name: "index_automatic_exploitation_match_sets_on_user_id", using::btree
#add_index"automatic_exploitation_match_sets", ["workspace_id"], name: "index_automatic_exploitation_match_sets_on_workspace_id", using::btree
c.execute('''CREATE TABLE "automatic_exploitation_matches" (
    "module_detail_id" integer ,
    "state" texto,
    "nexpose_data_vulnerability_definition_id" texto,
    "match_set_id" integer,   
    "matchable_type" text,
    "matchable_id" integer,   
    "module_fullname" text,
    "created_at" text,
    "updated_at" text)''')

#add_index "automatic_exploitation_matches", ["module_detail_id"], name: "index_automatic_exploitation_matches_on_module_detail_id", using: :btree
#add_index "automatic_exploitation_matches", ["module_fullname"], name: "index_automatic_exploitation_matches_on_module_fullname", using: :btree
c.execute('''CREATE TABLE "automatic_exploitation_runs" (
    "workspace_id" integer,
    "user_id" integer,
    "match_set_id" integer,
    "created_at" text,
    "updated_at" text)''')

# add_index"automatic_exploitation_runs", ["match_set_id"], name: "index_automatic_exploitation_runs_on_match_set_id", using::btree
# add_index"automatic_exploitation_runs", ["user_id"], name: "index_automatic_exploitation_runs_on_user_id", using::btree
# add_index"automatic_exploitation_runs", ["workspace_id"], name: "index_automatic_exploitation_runs_on_workspace_id", using::btree
c.execute('''CREATE TABLE "clients" (
    "host_id" integer,
    "ua_string" text,
    "ua_name" text,
    "ua_ver" 
    "created_at" text,
    "updated_at" text)''')

c.execute('''CREATE TABLE "credential_cores_tasks" (
    "core_id" integer,
    "task_id" integer )''')

c.execute('''CREATE TABLE "credential_logins_tasks"(
    "login_id" integer,
    "task_id" integer
)''')

c.execute('''CREATE TABLE "creds" (
    "service_id" integer ,
    "user" text,
    "pass" text,
    "proof" text,
    "ptype" text,
    "source_id" integer,
    "source_type" text
    "created_at" text,
    "updated_at" text
    )''')

c.execute('''CREATE TABLE "events" (
    "workspace_id" integer,
    "host_id" integer ,
    "name"  text,
    "username" text,
    "info" text,
    "seen" boolean,
    "critical" boolean,
    "created_at" text,
    "updated_at" text
)''')

c.execute('''CREATE TABLE "exploit_attempts"(
    "host_id" integer, 
    "service_id" integer,
    "vuln_id" integer,
    "attempted_at" text,
    "exploited" boolean,
    "fail_reason" text,
    "username" text,
    "module" text,
    "session_id" integer,
    "loot_id" integer,
    "port" integer,
    "proto" text,
    "fail_detail" text 
)''')

c.execute('''CREATE TABLE "exploited_hosts" (

    "host_id integer",
    "service_id" integer,
    "session_uuid" text,
    "name" text,
    "payload" text
    "created_at" text,
    "updated_at" text 
    )''')

c.execute('''CREATE TABLE "host_details" (
    "host_id" integer,
    "nx_console_id" integer,
    "nx_device_id" integer,
    "src" text,
    "nx_site_name" text
    "nx_site_importance" text
    "nx_scan_template" text
    "nx_risk_score" flout
)''')

c.execute('''CREATE TABLE "hosts" (
    "address" text ,
    "mac" text,
    "comm" text,
    "name" text,
    "state" text,
    "os_name" text,
    "os_flavor" text,
    "os_sp" text,
    "os_lang" text,
    "arch" text,
    "workspace_id" integer,
    "purpose" text
    "info" text,
    "comments" text,
    "scope" text
    "virtual_host" text
    "note_count" integer
    "vuln_count" integer
    "service_count" integer
    "host_detail_count" integer
    "exploit_attempt_count" integer
    "cred_count" interger
    "detected_arch" text
    "os_family" text
)''')


#add_index"hosts", ["name"], name: "index_hosts_on_name", using::btree
#add_index"hosts", ["os_flavor"], name: "index_hosts_on_os_flavor", using::btree
#add_index"hosts", ["os_name"], name: "index_hosts_on_os_name", using::btree
#add_index"hosts", ["purpose"], name: "index_hosts_on_purpose", using::btree
#add_index"hosts", ["state"], name: "index_hosts_on_state", using::btree
#add_index"hosts", ["workspace_id", "address"], name: "index_hosts_on_workspace_id_and_address", unique: true, using::btree
c.execute('''CREATE TABLE "hosts_tags" (
    "host_id" integer,
    "tag_id" integer  
)''')

c.execute('''CREATE TABLE "listeners"(
    "workspace_id" text,
    "enabled" boolean,
    "owner" text,
    "payload" text,   
    "address" text,
    "port" text,
    "options" text,
    "macro" text,
    "created_at" text,
    "updated_at" text 
)''')

c.execute('''CREATE TABLE "loots" (
    "workspace_id" interger,
    "host_id" interger,
    "service_id" interger
    "ltype" text,
    "path" text,   
    "data" text,
    "content_type" text,
    "name" text,
    "info" text
    "module_run_id" text
    "created_at" text,
    "updated_at" text
)''')

#add_index"loots", ["module_run_id"], name: "index_loots_on_module_run_id", using::btree
c.execute('''CREATE TABLE "macros"(
    "owner" text,
    "name" text,
    "description" text,
    "actions" text,
    "prefs" text
)''')

c.execute('''CREATE TABLE "thg_credential_cores" (
    "origin_id" interger,
    "origin_type" texto
    "private_id" interger
    "public_id" interger
    "realm_id" interger
    "workspace_id" interger
    "logins_count" interger
    "created_at" text,
    "updated_at" text
)''')

#add_index"metasploit_credential_cores", ["origin_type","origin_id"], name: "index_metasploit_credential_cores_on_origin_type_and_origin_id", using::btree
#add_index"metasploit_credential_cores", ["private_id"], name: "index_metasploit_credential_cores_on_private_id", using::btree
#add_index"metasploit_credential_cores", ["public_id"], name: "index_metasploit_credential_cores_on_public_id", using::btree
#add_index"metasploit_credential_cores", ["realm_id"], name: "index_metasploit_credential_cores_on_realm_id", using::btree
#add_index"metasploit_credential_cores", ["workspace_id","private_id"], name: "unique_private_metasploit_credential_cores", unique: true, where: "((realm_id IS NULL) AND (public_id IS NULL) AND (private_id IS NOT NULL))", using::btree
#add_index"metasploit_credential_cores", ["workspace_id", "public_id","private_id"], name: "unique_realmless_metasploit_credential_cores", unique: true, where: "((realm_id IS NULL) AND (public_id IS NOT NULL) AND (private_id IS NOT NULL))", using::btree
#add_index"metasploit_credential_cores", ["workspace_id","public_id"], name: "unique_public_metasploit_credential_cores", unique: true, where: "((realm_id IS NULL) AND (public_id IS NOT NULL) AND (private_id IS NULL))", using::btree
#add_index"metasploit_credential_cores", ["workspace_id", "realm_id","private_id"], name: "unique_publicless_metasploit_credential_cores", unique: true, where: "((realm_id IS NOT NULL) AND (public_id IS NULL) AND (private_id IS NOT NULL))", using::btree
#add_index"metasploit_credential_cores", ["workspace_id", "realm_id", "public_id","private_id"], name: "unique_complete_metasploit_credential_cores", unique: true, where: "((realm_id IS NOT NULL) AND (public_id IS NOT NULL) AND (private_id IS NOT NULL))", using::btree
#add_index"metasploit_credential_cores", ["workspace_id", "realm_id","public_id"], name: "unique_privateless_metasploit_credential_cores", unique: true, where: "((realm_id IS NOT NULL) AND (public_id IS NOT NULL) AND (private_id IS NULL))", using::btree
#add_index"metasploit_credential_cores", ["workspace_id"], name: "index_metasploit_credential_cores_on_workspace_id", using::btree
c.execute('''CREATE TABLE "metasploit_credential_logins" (
    "core_id" integer,
    "service_id" interger,
    "access_level" text,
    "status" text,
    "last_attempted_at" text
    "created_at" text,
    "updated_at" text
)''')

#add_index"metasploit_credential_logins", ["core_id","service_id"], name: "index_metasploit_credential_logins_on_core_id_and_service_id", unique: true, using::btree
#add_index"metasploit_credential_logins", ["service_id","core_id"], name: "index_metasploit_credential_logins_on_service_id_and_core_id", unique: true, using::btree


c.execute('''CREATE TABLE "metasploit_credential_origin_cracked_passwords" (
    "metasploit_credential_core_id" integer,
    "created_at" text,
    "updated_at" text
    
    )''')

#add_index"metasploit_credential_origin_cracked_passwords", ["metasploit_credential_core_id"], name: "originating_credential_cores", using::btree
c.execute('''CREATE TABLE "metasploit_credential_origin_imports" (
    "filename" text,
    "task_id" integer
    "created_at" text,
    "updated_at" text
)''')

#add_index"metasploit_credential_origin_imports", ["task_id"], name: "index_metasploit_credential_origin_imports_on_task_id", using::btree
c.execute('''CREATE TABLE "metasploit_credential_origin_manuals" (
    "user_id" integer,
    "created_at" text,
    "updated_at" text
)''')

#add_index"metasploit_credential_origin_services", ["service_id","module_full_name"], name: "unique_metasploit_credential_origin_services", unique: true, using::btree
c.execute('''CREATE TABLE "metasploit_credential_origin_sessions" (
    "post_reference_name" text,
    "session_id" integer
    "created_at" text,
    "updated_at" text
)''')

#add_index"metasploit_credential_privates", ["type","data"], name: "index_metasploit_credential_privates_on_type_and_data", unique: true, where: "(NOT ((type)::text = 'Metasploit::Credential::SSHKey'::text))", using::btree
#add_index"metasploit_credential_privates", ["type"], name: "index_metasploit_credential_privates_on_type_and_data_sshkey", unique: true, where: "((type)::text = 'Metasploit::Credential::SSHKey'::text)", using::btree
c.execute('''CREATE TABLE "metasploit_credential_publics" (
    "username" text,
    "type" text
    "created_at" text,
    "updated_at" text
)''')
#add_index"metasploit_credential_publics", ["username"], name: "index_metasploit_credential_publics_on_username", unique: true, using::btree
c.execute('''CREATE TABLE "metasploit_credential_realms" (
    "key" text,
    "value" text
    "created_at" text,
    "updated_at" text
)''')
#add_index"metasploit_credential_realms", ["key","value"], name: "index_metasploit_credential_realms_on_key_and_value", unique: true, using::btree
c.execute('''CREATE TABLE "mod_refs" (
    "module" text,
    "mtype" text,
    "ref" text
)''')

c.execute('''CREATE TABLE "module_actions" (
    "detail_id" integer,
    "name" text
)''')

#add_index"module_actions", ["detail_id"], name: "index_module_actions_on_detail_id", using::btree
c.execute('''CREATE TABLE "module_archs" (
    "detail_id" integer,
    "name" text
)''')

#add_index"module_archs", ["detail_id"], name: "index_module_archs_on_detail_id", using::btree
c.execute('''CREATE TABLE "module_authors" (
    "detail_id" integer,
    "name" text
    "email" text
)''')


# kick off the config component of the database
c.execute("INSERT INTO config VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", (STAGING_KEY, INSTALL_PATH, IP_WHITELIST, IP_BLACKLIST, '', '', False, API_USERNAME, API_PASSWORD, '', API_PERMANENT_TOKEN, OBFUSCATE, OBFUSCATE_COMMAND))

c.execute('''CREATE TABLE "agents" (
    "id" integer PRIMARY KEY,
    "session_id" text,
    "listener" text,
    "name" text,
    "language" text,
    "language_version" text,
    "delay" integer,
    "jitter" real,
    "external_ip" text,
    "internal_ip" text,
    "username" text,
    "high_integrity" integer,
    "process_name" text,
    "process_id" text,
    "hostname" text,
    "os_details" text,
    "session_key" text,
    "nonce" text,
    "checkin_time" text,
    "lastseen_time" text,
    "parent" text,
    "children" text,
    "servers" text,
    "profile" text,
    "functions" text,
    "kill_date" text,
    "working_hours" text,
    "lost_limit" integer,
    "taskings" text,
    "results" text
    )''')

# the 'options' field contains a pickled version of all
#   currently set listener options

# type = hash, plaintext, token
#   for krbtgt, the domain SID is stored in misc
#   for tokens, the data is base64'ed and stored in pass
c.execute('''CREATE TABLE "credentials" (
    "id" integer PRIMARY KEY,
    "credtype" text,
    "domain" text,
    "username" text,
    "password" text,
    "host" text,
    "os" text,
    "sid" text,
    "notes" text
    )''')

c.execute( '''CREATE TABLE "taskings" (
    "id" integer,
    "data" text,
    "agent" text,
    PRIMARY KEY(id, agent)
)''')

c.execute( '''CREATE TABLE "results" (
    "id" integer,
    "data" text,
    "agent" text,
    PRIMARY KEY(id, agent)
)''')

# event_types -> checkin, task, result, rename
c.execute('''CREATE TABLE "reporting" (
    "id" integer PRIMARY KEY,
    "name" text,
    "event_type" text,
    "message" text,
    "time_stamp" text,
    "taskID" integer,
    FOREIGN KEY(taskID) REFERENCES results(id)
)''')

# commit the changes and close everything off
conn.commit()
conn.close()

print ("\n [*] Database setup completed!\n")