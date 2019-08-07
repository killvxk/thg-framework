import mongoengine

class api_keys(mongoengine.Document):
    #__tablename__ ="api_keys"
    #id = mongoengine.IntField(unique=True)
    token = mongoengine.StringField()
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
class automatic_exploitation_match_results(mongoengine.Document):
    #__tablename__ = "automatic_exploitation_match_results"
    match_id = mongoengine.IntField()
    run_id = mongoengine.IntField()
    state = mongoengine.StringField()
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
    #meta = (
    #    Index('index_automatic_exploitation_match_results_on_match_id', 'match_id'),
    #    Index('index_automatic_exploitation_match_results_on_run_id', 'run_id'),
    #)
    #index_automatic_exploitation_match_results_on_match_id = self.match_id
    #index_automatic_exploitation_match_results_on_run_id = self.run_id
    """meta = {
        'indexes': {
            name: '',
            fields: ['']
        }
    }"""
class automatic_exploitation_match_sets (mongoengine.Document):
    #__tablename__="automatic_exploitation_match_sets"
    workspace_id = mongoengine.IntField()
    user_id = mongoengine.IntField()
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
    #meta = (
    #    Index('index_automatic_exploitation_match_sets_on_user_id', 'user_id'),
    #    Index('index_automatic_exploitation_match_sets_on_workspace_id', 'workspace_id'),
    #)
    """index_automatic_exploitation_match_sets_on_user_id = self.user_id
    index_automatic_exploitation_match_sets_on_workspace_id = self.workspace_id"""

class automatic_exploitation_matches(mongoengine.Document):
    #__tablename__="automatic_exploitation_matches"
    module_detail_id = mongoengine.IntField(unique=True)
    state = mongoengine.StringField()
    nexpose_data_vulnerability_definition_id = mongoengine.IntField()
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
    match_set_id = mongoengine.IntField()
    matchable_type= mongoengine.StringField()
    matchable_id= mongoengine.IntField()
    module_fullname= mongoengine.StringField()
    #meta = (
    #    Index('index_automatic_exploitation_matches_on_module_detail_id', 'module_detail_id'),
    #    Index('index_automatic_exploitation_matches_on_module_fullname', 'module_fullname'),
    #)
    """index_automatic_exploitation_matches_on_module_detail_id = self.module_detail_id
    index_automatic_exploitation_matches_on_module_full_name = self.module_full_name"""
class automatic_exploitation_runs(mongoengine.Document):
    #__tablename__ ="automatic_exploitation_runs"
    workspace_id=mongoengine.IntField(unique=True)
    user_id=mongoengine.IntField(unique=True)
    match_set_id =mongoengine.IntField(unique=True)
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
    """meta = (
        index_automatic_exploitation_runs_on_match_set_id = match_set_id
        index_automatic_exploitation_runs_on_user_id = user_id
        index_automatic_exploitation_runs_on_workspace_id = workspace_id

    )"""
class clients(mongoengine.Document):
    #__tablename__ = "clients"
    host_id=mongoengine.IntField(unique=True)
    created_at = mongoengine.DateTimeField(null=False)
    ua_string=mongoengine.StringField()
    ua_name=mongoengine.StringField()
    ua_ver=mongoengine.StringField()
    updated_at=mongoengine.DateTimeField(null=False)
class credential_cores_tasks(mongoengine.Document):
    #__tablename__ = "credential_cores_tasks"
    core_id=mongoengine.IntField(unique=True)
    task_id=mongoengine.IntField(unique=True)
class credential_logins_tasks(mongoengine.Document):
    #__tablename__ = "credential_logins_tasks"
    login_id=mongoengine.IntField(unique=True)
    task_id=mongoengine.IntField(unique=True)
class creds(mongoengine.Document):
    #__tablename__ ="creds"
    service_id=mongoengine.IntField(unique=True, null=False)
    user= mongoengine.StringField()
    passw = mongoengine.StringField()
    active=mongoengine.BooleanField(unique=False, default=True)
    proof=mongoengine.StringField()
    ptype=mongoengine.StringField()
    source_id=mongoengine.IntField(unique=True)
    source_type=mongoengine.StringField()
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
class events(mongoengine.Document):
    #__tablename__="events"
    workspace_id=mongoengine.IntField(unique=True)
    host_id=mongoengine.IntField(unique=True)
    name=mongoengine.StringField()
    critical=mongoengine.BooleanField(unique=False, default=False)
    seen=mongoengine.BooleanField(unique=False, default=False)
    username=mongoengine.StringField()
    info=mongoengine.StringField()
class exploit_attempts(mongoengine.Document):
    #__tablename__= "exploit_attempts"
    host_id=mongoengine.IntField(unique=True)
    service_id=mongoengine.IntField(unique=True)
    session_id=mongoengine.IntField(unique=True)
    vuln_id=mongoengine.IntField(unique=True)
    loot_id=mongoengine.IntField(unique=True)
    exploited=mongoengine.BooleanField(unique=False, default=False)
    attempted_at=mongoengine.StringField()
    fail_reason=mongoengine.StringField()
    username=mongoengine.StringField()
    module=mongoengine.StringField()
    port=mongoengine.IntField()
    proto=mongoengine.StringField()
    fail_detail=mongoengine.StringField()
class exploited_hosts(mongoengine.Document):
    #__tablename__="exploited_hosts"
    host_id=mongoengine.IntField(null=False, unique=True)
    service_id=mongoengine.IntField(unique=True)
    session_uuid=mongoengine.IntField()
    name=mongoengine.IntField()
    payload=mongoengine.IntField()
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
class host_details(mongoengine.Document):
    #__tablename__="host_details"
    host_id=mongoengine.IntField(unique=True)
    nx_console_id=mongoengine.IntField(unique=True)
    nx_device_id=mongoengine.IntField(unique=True)
    src=mongoengine.StringField()
    nx_site_name=mongoengine.StringField()
    nx_site_importance=mongoengine.StringField()
    nx_scan_template=mongoengine.StringField()
    nx_risk_score=mongoengine.StringField()
class hosts(mongoengine.Document):
    #__tablename__ = "hosts"
    address=mongoengine.StringField()
    mac=mongoengine.StringField()
    comm=mongoengine.StringField()
    name=mongoengine.StringField()
    state=mongoengine.StringField()
    os_name=mongoengine.StringField()
    os_flavor=mongoengine.StringField()
    os_sp=mongoengine.StringField()
    os_lang=mongoengine.StringField()
    arch=mongoengine.StringField()
    workspace_id=mongoengine.IntField(unique=True)
    purpose=mongoengine.StringField()
    info=mongoengine.StringField()
    comments=mongoengine.StringField()
    scope=mongoengine.StringField()
    virtual_host=mongoengine.StringField()
    note_count=mongoengine.IntField(default=0)
    vuln_count=mongoengine.IntField(default=0)
    service_count=mongoengine.IntField(default=0)
    host_detail_count=mongoengine.IntField(default=0)
    xploit_attempt_count=mongoengine.IntField(default=0)
    cred_count=mongoengine.IntField(default=0)
    detected_arch=mongoengine.StringField()
    os_family=mongoengine.StringField()
    """meta = (
        Index('index_hosts_on_name', 'name'),
        Index('index_hosts_on_os_flavor', 'os_flavor'),
        Index('index_hosts_on_os_name', 'os_name'),
        Index('index_hosts_on_purpose','purpose'),
        Index('index_hosts_on_state','state'),
        Index('index_hosts_on_workspace_id_and_address','workspace_id','address'),
    )"""
class hosts_tags(mongoengine.Document):
    #__tablename__ = "hosts_tags"
    host_id=mongoengine.IntField(unique=True)
    tag_id=mongoengine.IntField(unique=True)
class listeners(mongoengine.Document):
    #__tablename__="listeners"
    workspace_id = mongoengine.IntField(null=False,default=1)
    task_id=mongoengine.IntField(unique=True)
    enabled=mongoengine.BooleanField(default=True)
    owner=mongoengine.StringField()
    payload=mongoengine.StringField()
    address=mongoengine.StringField()
    port=mongoengine.IntField()
    options=mongoengine.BinaryField()
    macro=mongoengine.StringField()
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
class loots(mongoengine.Document):
    #__tablename__="loots"
    workspace_id = mongoengine.IntField(default=1,null=False,unique=True)
    host_id = mongoengine.IntField(unique=True)
    service_id = mongoengine.IntField(unique=True)
    ltype=mongoengine.StringField()
    path=mongoengine.StringField()
    data=mongoengine.StringField()
    content_type=mongoengine.StringField()
    name=mongoengine.StringField()
    info=mongoengine.StringField()
    module_run_id=mongoengine.IntField(unique=True)
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
    """meta = (
        Index('index_loots_on_module_run_id', 'module_run_id'),

    )"""
class Macros(mongoengine.Document):
    #__tablename__="Macros"
    id=mongoengine.IntField(unique=True)
    owner=mongoengine.StringField()
    name=mongoengine.StringField()
    description=mongoengine.StringField()
    actions=mongoengine.BinaryField()
    prefs=mongoengine.BinaryField()
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
class thg_credential_cores(mongoengine.Document):
    #__tablename__="thg_credential_cores"
    origin_id=mongoengine.IntField(unique=True,default=0)
    origin_type=mongoengine.StringField(null=False)
    private_id=mongoengine.IntField(unique=True)
    public_id=mongoengine.IntField(unique=True)
    realm_id=mongoengine.IntField(unique=True)
    workspace_id=mongoengine.IntField(unique=True)
    logins_count=mongoengine.IntField(unique=True, default=0)
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
    """meta = (
        Index('index_thg_credential_cores_on_origin_type_and_origin_id', 'origin_type','origin_id'),
        Index('index_thg_credential_cores_on_private_id', 'private_id'),
        Index('index_thg_credential_cores_on_public_id', 'public_id'),
        Index('index_thg_credential_cores_on_realm_id', 'realm_id'),
        Index('unique_private_thg_credential_cores', 'workspace_id','private_id'),
        Index('unique_realmless_thg_credential_cores', 'workspace_id','public_id','private_id'),
        Index('unique_public_thg_credential_cores', 'workspace_id','public_id'),
        Index('unique_publicless_thg_credential_cores','workspace_id','realm_id','private_id'),
        Index('unique_complete_thg_credential_cores','workspace_id','realm_id','private_id','public_id'),
        Index('unique_privateless_thg_credential_cores','workspace_id','realm_id','public_id'),
        Index('index_thg_credential_cores_on_workspace_id','workspace_id')
    )"""
class thg_credential_logins(mongoengine.Document):
    #__tablename__="thg_credential_logins"
    core_id=mongoengine.IntField(unique=True,null=False)
    service_id=mongoengine.IntField(unique=True,null=False)
    access_level=mongoengine.StringField(null=False)
    status=mongoengine.StringField(null=False)
    last_attempted_at=mongoengine.DateTimeField(null=False)
    created_at=mongoengine.DateTimeField(null=False)
    updated_at=mongoengine.DateTimeField(null=False)
    """meta = (
        Index('index_thg_credential_logins_on_core_id_and_service_id', 'service_id', 'core_id'),
        Index('index_thg_credential_logins_on_service_id_and_core_id', 'service_id','core_id'),
    )"""
class thg_credential_origin_cracked_passwords(mongoengine.Document):
    #__tablename__="thg_credential_origin_cracked_passwords"
    thg_credential_core_id=mongoengine.IntField(unique=True,null=False)
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
    """meta = (
        Index('originating_credential_cores', 'thg_credential_core_id'),
    )"""
class thg_credential_origin_imports(mongoengine.Document):
    #__tablename__ ="thg_credential_origin_imports"
    filename=mongoengine.StringField()
    task_id=mongoengine.IntField(unique=True,null=False)
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
    """meta = (
        Index('index_thg_credential_origin_imports_on_task_id', 'task_id'),
    )"""
class thg_credential_origin_manuals(mongoengine.Document):
    #__tablename__ ="thg_credential_origin_manuals"
    user_id=mongoengine.IntField(unique=True,null=False)
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
    """meta = (
        Index('index_thg_credential_origin_manuals_on_user_id', 'user_id'),
    )"""
class thg_credential_origin_services(mongoengine.Document):
    #__tablename__ ="thg_credential_origin_services"
    service_id=mongoengine.IntField(unique=True,null=False)
    module_full_name=mongoengine.StringField()
    """meta = (
        Index('unique_thg_credential_origin_services', 'service_id','module_full_name'),
    )"""
class thg_credential_origin_sessions(mongoengine.Document):
    #__tablename__ = "thg_credential_origin_sessions"
    post_reference_name=mongoengine.StringField(null=False)
    session_id=mongoengine.IntField(unique=True,null=False)
    """meta = (
        Index('unique_thg_credential_origin_sessions', 'session_id', 'post_reference_name'),
    )"""
class thg_credential_privates(mongoengine.Document):
    #__tablename__="thg_credential_privates"
    id = mongoengine.IntField(null=False,unique=True)
    types=mongoengine.StringField(null=False)
    data=mongoengine.StringField(null=False)
    jtr_format=mongoengine.StringField(null=False)
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
    """meta = (
        Index('index_thg_credential_privates_on_type_and_data', 'types', 'data'),
        Index('index_thg_credential_privates_on_type_and_data_sshkey','types')
    )"""
class thg_credential_publics(mongoengine.Document):
    #__tablename__="thg_credential_publics"
    id = mongoengine.IntField(null=False,unique=True)
    username=mongoengine.StringField(null=False)
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
    """meta = (
        Index('index_thg_credential_publics_on_username', 'username'),
    )"""
class thg_credential_realms(mongoengine.Document):
    #__tablename__="thg_credential_realms"
    id = mongoengine.IntField(null=False, unique=True)
    key=mongoengine.StringField(null=False)
    value=mongoengine.StringField(null=False)
    """meta = (
        Index('index_thg_credential_realms_on_key_and_value', 'key','value'),
    )"""
class mod_refs(mongoengine.Document):
    #__tablename__ = "mod_refs"
    #id = mongoengine.IntField(null=False, unique=True)
    module=mongoengine.StringField(unique=True,null=False)
    mtype=mongoengine.StringField(null=False)
    ref=mongoengine.StringField(null=False)
class module_actions(mongoengine.Document):
    #__tablename__ = "module_actions"
    detail_id=mongoengine.IntField(null=False, unique=True)
    name=mongoengine.StringField(null=False)
    """meta = (
        Index('index_module_actions_on_detail_id', 'detail_id'),
    )"""
    meta = {
        'indexes': [
            {
                'name': 'index_module_actions_on_detail_id',
                'fields': ['detail_id']
            }
        ]
    }
class module_archs(mongoengine.Document):
    #__tablename__= "module_archs"
    detail_id=mongoengine.IntField(null=False, unique=True)
    name=mongoengine.StringField(null=False)
    """meta = (
        Index('index_module_archs_on_detail_id', 'detail_id'),
    )"""
    meta = {
        'indexes': [
            {
                'name': 'index_module_archs_on_detail_id',
                'fields': ['detail_id']
            }
        ]
    }
class module_authors(mongoengine.Document):
    #__tablename__ = "module_authors"
    detail_id=mongoengine.IntField(null=False, unique=True)
    name=mongoengine.StringField(null=False)
    email=mongoengine.StringField(null=False)
    """meta = (
        Index('index_module_authors_on_detail_id', 'detail_id'),
    )"""
    meta = {
        'indexes': [
            {
                'name': 'index_module_authors_on_detail_id',
                'fields': ['detail_id']
            }
        ]
    }
class module_details(mongoengine.Document):
    #__tablename__="module_details"
    id=mongoengine.IntField(unique=True)
    mtime=mongoengine.DateTimeField(null=False)
    file=mongoengine.StringField(null=False)
    mtype=mongoengine.StringField(null=False)
    refname=mongoengine.StringField(null=False)
    fullname=mongoengine.StringField(null=False)
    name=mongoengine.StringField(null=False)
    rank=mongoengine.IntField(null=False)
    description=mongoengine.StringField(null=False)
    license=mongoengine.StringField(null=False)
    privileged=mongoengine.BooleanField(null=False)
    disclosure_date=mongoengine.DateTimeField(null=False)
    default_target=mongoengine.IntField(null=False)
    default_action=mongoengine.StringField(null=False)
    stance=mongoengine.StringField(null=False)
    ready=mongoengine.BooleanField(null=False)
    """meta = (
        Index('index_module_details_on_description', 'description'),
        Index('index_module_details_on_mtype','mtype'),
        Index('index_module_details_on_name', 'name'),
        Index('index_module_details_on_refname', 'refname'),
    )"""
    """meta = {
        'indexes': {
            name: 'index_module_authors_on_detail_id',
            fields: ['detail_id']
        }
    }"""
class module_mixins(mongoengine.Document):
    #__tablename__="module_mixins"
    detail_id=mongoengine.IntField(unique=True)
    name=mongoengine.StringField(null=False)
    """meta = (
        Index('index_module_mixins_on_detail_id', 'detail_id'),
    )"""
class module_platforms(mongoengine.Document):
    #__tablename__="module_platforms"
    detail_id=mongoengine.IntField(unique=True)
    name=mongoengine.StringField(null=False)
    """meta = (
        Index('index_module_platforms_on_detail_id', 'detail_id'),
    )"""
class module_refs(mongoengine.Document):
    #__tablename__="module_refs"
    detail_id=mongoengine.IntField(unique=True)
    name=mongoengine.StringField(null=True)
    """meta = (
        Index('index_module_refs_on_detail_id', 'detail_id'),
        Index('index_module_refs_on_name','name'),
    )"""
class module_runs(mongoengine.Document):
    #__tablename__="module_runs"
    id = mongoengine.IntField(unique=True,)
    attempted_at=mongoengine.DateTimeField(null=True)
    fail_detail=mongoengine.StringField(null=True)
    fail_reason=mongoengine.StringField(null=True)
    module_fullname=mongoengine.StringField(null=True)
    port=mongoengine.IntField(null=True)
    proto=mongoengine.StringField(null=True)
    status = mongoengine.StringField(null=True)
    session_id=mongoengine.IntField(null=True)
    trackable_id=mongoengine.IntField(null=True)
    trackable_type=mongoengine.StringField(null=True)
    user_id=mongoengine.StringField(null=True)
    username=mongoengine.StringField(null=True)
    created_at = mongoengine.DateTimeField(null=True)
    updated_at = mongoengine.DateTimeField(null=True)
    """meta = (
        Index('index_module_runs_on_session_id', 'session_id'),
        Index('index_module_runs_on_user_id','user_id'),
    )"""
class module_targets(mongoengine.Document):
    #__tablename__="module_targets"

    detail_id=mongoengine.IntField(null=False,unique=True)
    index=mongoengine.IntField(null=False)
    name=mongoengine.StringField(null=False)
    """meta = (
        Index('index_module_targets_on_detail_id', 'detail_id'),
    )"""
class nexpose_consoles(mongoengine.Document):
    #__tablename__="nexpose_consoles"
    id= mongoengine.IntField(unique=True)
    enabled= mongoengine.BooleanField(default=True)
    owner=mongoengine.StringField(null=False)
    address=mongoengine.StringField(null=False)
    port=mongoengine.IntField(null=False,default=3780)
    username=mongoengine.StringField(null=False)
    password=mongoengine.StringField(null=False)
    status=mongoengine.StringField(null=False)
    version=mongoengine.StringField(null=False)
    cert=mongoengine.StringField(null=False)
    cached_sites=mongoengine.BinaryField()
    name=mongoengine.StringField(null=False)
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
class notes(mongoengine.Document):
    #__tablename__ ="notes"
    id = mongoengine.IntField(unique=True)
    ntype=mongoengine.StringField(null=False)
    workspace_id=mongoengine.IntField(null=False,default=1)
    service_id=mongoengine.IntField(null=False)
    host_id=mongoengine.IntField(null=False)
    data=mongoengine.StringField(null=False)
    critical= mongoengine.BooleanField(default=True)
    seen= mongoengine.BooleanField(default=True)
    vuln_id= mongoengine.IntField()
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
    """meta = (
        Index('index_notes_on_ntype', 'ntype'),
        Index('index_notes_on_vuln_id', 'vuln_id'),
    )"""
class payloads(mongoengine.Document):
    #__tablename__ ="payloads"
    id = mongoengine.IntField(unique=True)
    name=mongoengine.StringField(null=False)
    uuid=mongoengine.StringField(null=False)
    arch=mongoengine.StringField(null=False)
    platform=mongoengine.StringField(null=False)
    urls=mongoengine.StringField(null=False)
    description=mongoengine.StringField(null=False)
    raw_payload=mongoengine.StringField(null=False)
    build_status=mongoengine.StringField(null=False)
    raw_payload_hash=mongoengine.StringField(null=False)
    build_opts=mongoengine.StringField(null=False)
    uuid_mask= mongoengine.IntField()
    timestamp= mongoengine.IntField()
    workspace_id= mongoengine.IntField(null=False)
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
class profiles(mongoengine.Document):
    #__tablename__= "profiles"
    id = mongoengine.IntField( unique=True)
    active =mongoengine.BooleanField(default=True)
    name=mongoengine.StringField(null=False)
    owner=mongoengine.StringField(null=False)
    settings =mongoengine.BinaryField()
class refs(mongoengine.Document):
    #__tablename__ = "refs"
    id = mongoengine.IntField( unique=True)
    ref_id=mongoengine.IntField(null=False)
    name= mongoengine.StringField(null=False)
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
    """meta = (
        Index('index_refs_on_name', 'name'),
    )"""
class report_templates(mongoengine.Document):
    #__tablename__="report_templates"
    workspace_id = mongoengine.IntField(unique=True,null=False)
    created_by= mongoengine.StringField(null=False)
    path= mongoengine.StringField(null=False)
    name= mongoengine.StringField(null=False)
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
class reports(mongoengine.Document):
    #__tablename__= "reports"
    workspace_id = mongoengine.IntField( unique=True, null=False)
    created_by = mongoengine.StringField(null=False)
    path = mongoengine.StringField(null=False)
    name = mongoengine.StringField(null=False)
    options=mongoengine.StringField(null=False)
    downloaded_at=mongoengine.StringField()
    task_id= mongoengine.IntField( unique=True, null=False)
class routes(mongoengine.Document):
    #__tablename__ = "routes"
    session_id=mongoengine.StringField(null=False,unique=True)
    subnet=mongoengine.StringField(null=False)
    netmask=mongoengine.StringField(null=False)
class services(mongoengine.Document):
    #__tablename__= "services"

    host_id=mongoengine.IntField( null=False,unique=True)
    port=mongoengine.StringField(null=False)
    proto=mongoengine.StringField(null=False)
    state=mongoengine.StringField(null=False)
    name=mongoengine.StringField(null=False)
    info=mongoengine.StringField(null=False)
    """meta = (
        Index('index_services_on_host_id_and_port_and_proto', 'host_id','port','proto'),
        Index('index_services_on_name', 'name'),
        Index('index_services_on_port', 'port'),
        Index('index_services_on_proto', 'name'),
        Index('index_services_on_state', 'state'),
    )"""
class session_events(mongoengine.Document):
    #__tablename__ = "session_events"
    session_id =mongoengine.IntField(unique=True,null=True)
    etype =mongoengine.StringField(null=False)
    command = mongoengine.BinaryField(null=True)
    output= mongoengine.BinaryField(null=True)
    remote_path=mongoengine.StringField(null=False)
    local_path =mongoengine.StringField(null=False)
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
class sessions(mongoengine.Document):
    #__tablename__ = "sessions"
    host_id=mongoengine.IntField(unique=True,null=True)
    stype=mongoengine.StringField(null=False)
    via_exploit=mongoengine.StringField(null=False)
    via_payload=mongoengine.StringField(null=False)
    desc=mongoengine.StringField(null=False)
    port = mongoengine.IntField(null=False)
    platform=mongoengine.StringField(null=False)
    datastore=mongoengine.StringField(null=False)
    closed_at = mongoengine.DateTimeField(null=False)
    close_reason=mongoengine.StringField(null=False)
    local_id= mongoengine.IntField(null=False, unique=True)
    last_seen= mongoengine.DateTimeField(null=False)
    module_run_id= mongoengine.IntField(null=False,unique=True)
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)

    """meta = (Index('index_sessions_on_module_run_id','module_run_id'),)"""
class tags(mongoengine.Document):
    #__tablename__ = "tags"
    user_id= mongoengine.IntField(unique=True,null=False)
    name=mongoengine.StringField(null=False)
    desc=mongoengine.StringField(null=False)
    report_summary= mongoengine.BinaryField(default=False,null=False)
    report_detail= mongoengine.BinaryField(default=False,null=False)
    critical= mongoengine.BinaryField(default=False,null=False)
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
class task_creds(mongoengine.Document):
    #__tablename__ = "task_creds"
    task_id= mongoengine.IntField(unique=True,null=False)
    cred_id= mongoengine.IntField(unique=True,null=False)
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
class task_hosts(mongoengine.Document):
    #__tablename__ ="task_hosts"
    task_id= mongoengine.IntField(unique=True,null=False)
    cred_id= mongoengine.IntField(unique=True,null=False)
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
class task_services(mongoengine.Document):
    #__tablename__ ="task_services"
    task_id= mongoengine.IntField(unique=True,null=False)
    cred_id= mongoengine.IntField(unique=True,null=False)
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
class task_sessions(mongoengine.Document):
    #__tablename__ ="task_sessions"
    task_id= mongoengine.IntField(unique=True,null=False)
    cred_id= mongoengine.IntField(unique=True,null=False)
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
class tasks(mongoengine.Document):
    #__tablename__ ="tasks"
    workspace_id = mongoengine.IntField(default=1,unique=True,null=False)
    created_by=mongoengine.StringField(null=False)
    module=mongoengine.StringField(null=False)
    completed_at=mongoengine.DateTimeField(null=False)
    path=mongoengine.StringField(null=False)
    info=mongoengine.StringField(null=False)
    description=mongoengine.StringField(null=False)
    progress=mongoengine.IntField(unique=True,null=False)
    options=mongoengine.StringField(null=False)
    error=mongoengine.StringField(null=False)
    result =mongoengine.StringField(null=False)
    module_uuid =mongoengine.StringField(null=False)
    settings = mongoengine.BinaryField()
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
class users(mongoengine.Document):
    #__tablename__ ="users"
    id = mongoengine.IntField(unique=True)
    username =mongoengine.StringField(null=False)
    crypted_password =mongoengine.StringField(null=False)
    password_salt =mongoengine.StringField(null=False)
    persistence_token =mongoengine.StringField(null=False)
    fullname =mongoengine.StringField(null=False)
    email =mongoengine.StringField(null=False)
    phone =mongoengine.StringField(null=False)
    company =mongoengine.StringField(null=False)
    prefs =mongoengine.StringField(null=False)
    admin = mongoengine.BooleanField(default=True,null=False)
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
class vuln_attempts(mongoengine.Document):
    #__tablename__ ="vuln_attempts"
    vuln_id =mongoengine.IntField(unique=True)
    attempted_at= mongoengine.DateTimeField(null=False)
    exploited =mongoengine.BooleanField(default=False,null=False)
    fail_reason =mongoengine.StringField(null=False)
    username =mongoengine.StringField(null=False)
    module =mongoengine.StringField(null=False)
    loot_id =mongoengine.IntField(unique=True)
    session_id =mongoengine.IntField(unique=True)
    fail_detail =mongoengine.StringField(null=False)
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
class vuln_details(mongoengine.Document):
    #__tablename__ ="vuln_details"
    vuln_id=mongoengine.IntField(null=False,unique=True)
    cvss_score=mongoengine.FloatField()
    cvss_vector=mongoengine.StringField(null=False)
    title=mongoengine.StringField(null=False)
    description =mongoengine.StringField(null=False)
    solution =mongoengine.StringField(null=False)
    proof=mongoengine.BinaryField()
    nx_console_id =mongoengine.IntField(null=False,unique=True)
    nx_device_id =mongoengine.IntField(null=False,unique=True)
    nx_vuln_id =mongoengine.StringField(null=False,unique=True)
    nx_severity=mongoengine.FloatField()
    nx_pci_severity =mongoengine.FloatField()
    nx_published=mongoengine.DateTimeField(null=False)
    nx_added =mongoengine.DateTimeField(null=False)
    nx_modified =mongoengine.DateTimeField(null=False)
    nx_tags =mongoengine.StringField(null=False)
    nx_vuln_status =mongoengine.StringField(null=False)
    nx_proof_key =mongoengine.StringField(null=False)
    src =mongoengine.StringField(null=False)
    nx_scan_id = mongoengine.IntField(null=False,unique=True)
    nx_vulnerable_since =mongoengine.DateTimeField(null=False)
    nx_pci_compliance_status=mongoengine.StringField(null=False)
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
class vulns(mongoengine.Document):
    #__tablename__="vulns"
    host_id= mongoengine.IntField(null=False)
    service_id= mongoengine.IntField(null=False)
    name=mongoengine.StringField(null=False)
    info=mongoengine.StringField(null=False)
    exploited_at= mongoengine.DateTimeField(null=False)
    vuln_detail_count= mongoengine.IntField(null=False,unique=True,default=0)
    vuln_attempt_count= mongoengine.IntField(null=False,unique=True,default=0)
    origin_id= mongoengine.IntField(null=False,unique=True,default=0)
    origin_type=mongoengine.StringField(null=False)
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
    """meta = (Index('index_vulns_on_name','name'),Index('index_vulns_on_origin_id','origin_id'))"""
class vulns_refs(mongoengine.Document):
    #__tablename__ = "vulns_refs"
    ref_id =mongoengine.IntField(null=False)
    vuln_id =mongoengine.IntField(null=False)
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
class web_forms(mongoengine.Document):
    #__tablename__ ="web_forms"
    web_site_id =mongoengine.IntField(null=False)
    path=mongoengine.StringField(null=False)
    method=mongoengine.StringField(null=False)
    params=mongoengine.StringField(null=False)
    query=mongoengine.StringField(null=False)
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
    """meta = (Index('index_web_forms_on_path','path'),)"""
class web_pages(mongoengine.Document):
    #__tablename__="web_pages"

    web_site_id=mongoengine.IntField(unique=True,null=False)
    path=mongoengine.StringField(null=False)
    query=mongoengine.StringField(null=False)
    code=mongoengine.IntField(null=False)
    cookie=mongoengine.StringField(null=False)
    auth=mongoengine.StringField(null=False)
    ctype=mongoengine.StringField(null=False)
    mtime =mongoengine.DateTimeField(null=False)
    location=mongoengine.StringField(null=False)
    headers =mongoengine.StringField(null=False)
    body=mongoengine.BinaryField()
    request=mongoengine.BinaryField()
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
    """meta = (Index('index_web_pages_on_path', 'path'),Index('index_web_pages_on_query','query'))"""
class web_sites(mongoengine.Document):
    #__tablename__="web_sites"

    service_id=mongoengine.IntField(unique=True,null=False)
    vhost=mongoengine.StringField(null=False)
    comments=mongoengine.StringField(null=False)
    options=mongoengine.StringField(null=False)
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
    """meta = (Index('index_web_sites_on_comments', 'comments'),Index('index_web_sites_on_options','options'),Index('index_web_sites_on_vhost','vhost'))"""
class web_vulns(mongoengine.Document):
    #__tablename__= "web_vulns"
    web_site_id = mongoengine.IntField(unique=True,null=False)
    path=mongoengine.StringField(null=False)
    method=mongoengine.StringField(null=False)
    params=mongoengine.StringField(null=False)
    pname=mongoengine.StringField(null=False)
    risk=mongoengine.IntField(null=False)
    name=mongoengine.StringField(null=False)
    query=mongoengine.StringField(null=False)
    category=mongoengine.StringField(null=False)
    confidence=mongoengine.IntField(null=False)
    description =mongoengine.StringField(null=False)
    blame =mongoengine.StringField(null=False)
    request=mongoengine.BinaryField()
    proof =mongoengine.BinaryField()
    owner=mongoengine.StringField(null=False)
    payload=mongoengine.StringField(null=False)
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
    """meta= (Index('index_web_vulns_on_method','method'),
                      Index('index_web_vulns_on_name','name'),
                      Index('index_web_vulns_on_path','path'),)"""
class wmap_requests(mongoengine.Document):
    #__tablename__="wmap_requests"
    host=mongoengine.StringField(null=False)
    address=mongoengine.IntField(null=False)
    port=mongoengine.StringField(null=False)
    ssl=mongoengine.IntField(null=False)
    meth=mongoengine.StringField(null=False)
    path=mongoengine.StringField(null=False)
    headers=mongoengine.StringField(null=False)
    query=mongoengine.StringField(null=False)
    body=mongoengine.StringField(null=False)
    respcode=mongoengine.StringField(null=False)
    resphead=mongoengine.StringField(null=False)
    response=mongoengine.StringField(null=False)
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
class wmap_targets(mongoengine.Document):
    #__tablename__ = "wmap_targets"
    host=mongoengine.StringField(null=False)
    address=mongoengine.StringField(null=False)
    port=mongoengine.IntField(null=False)
    ssl=mongoengine.IntField(null=False)
    selected=mongoengine.IntField(null=False)
    created_at = mongoengine.DateTimeField(null=False)
    updated_at = mongoengine.DateTimeField(null=False)
class workspace_members(mongoengine.Document):
    #__tablename__ = "workspace_members"
    workspace_id=mongoengine.IntField(null=False)
    user_id=mongoengine.IntField(null=False)
class workspaces(mongoengine.Document):
    #__tablename__="workspaces"
    name=mongoengine.StringField(null=False)
    boundary=mongoengine.StringField(null=False)
    description=mongoengine.StringField(null=False)
    owner_id=mongoengine.IntField(null=False)
    limit_to_network=mongoengine.BooleanField(null=False,default=False)
    import_fingerprint=mongoengine.BooleanField(default=False)
