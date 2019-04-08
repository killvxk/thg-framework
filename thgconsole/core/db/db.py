import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,Index,Boolean,Binary,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine,TIMESTAMP
Base = declarative_base()
class api_keys(Base):
    __tablename__ ="api_keys"
    id = Column(Integer,primary_key=True)
    token = Column(String(255))
    created_at = Column(TIMESTAMP,nullable=False)
    updated_at = Column(TIMESTAMP,nullable=False)
class automatic_exploitation_match_results(Base):
    __tablename__ = "automatic_exploitation_match_results"
    match_id = Column(Integer,primary_key=True)
    run_id = Column(Integer,primary_key=True)
    state = Column(String(255))
    created_at = Column(TIMESTAMP,nullable=False)
    updated_at = Column(TIMESTAMP,nullable=False)
    __table_args__ = (
        Index('index_automatic_exploitation_match_results_on_match_id', 'match_id'),
        Index('index_automatic_exploitation_match_results_on_run_id', 'run_id'),
    )
class automatic_exploitation_match_sets (Base):
    __tablename__="automatic_exploitation_match_sets"
    workspace_id = Column(Integer,primary_key=True)
    user_id = Column(Integer,primary_key=True)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
    __table_args__ = (
        Index('index_automatic_exploitation_match_sets_on_user_id', 'user_id'),
        Index('index_automatic_exploitation_match_sets_on_workspace_id', 'workspace_id'),
    )
class automatic_exploitation_matches(Base):
    __tablename__="automatic_exploitation_matches"
    module_detail_id = Column(Integer,primary_key=True)
    state = Column(String(255))
    nexpose_data_vulnerability_definition_id = Column(Integer,primary_key=True)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
    match_set_id = Column(Integer,primary_key=True)
    matchable_type= Column(String(255))
    matchable_id= Column(Integer,primary_key=True)
    module_fullname= Column(String(255))
    __table_args__ = (
        Index('index_automatic_exploitation_matches_on_module_detail_id', 'module_detail_id'),
        Index('index_automatic_exploitation_matches_on_module_fullname', 'module_fullname'),
    )
class automatic_exploitation_runs(Base):
    __tablename__ ="automatic_exploitation_runs"
    workspace_id=Column(Integer,primary_key=True)
    user_id=Column(Integer,primary_key=True)
    match_set_id =Column(Integer,primary_key=True)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
    __table_args__ = (
        Index('index_automatic_exploitation_runs_on_match_set_id', 'match_set_id'),
        Index('index_automatic_exploitation_runs_on_user_id', 'user_id'),
        Index('index_automatic_exploitation_runs_on_workspace_id', 'workspace_id'),

    )
class clients(Base):
    __tablename__ = "clients"
    host_id=Column(Integer,primary_key=True)
    created_at = Column(TIMESTAMP, nullable=False)
    ua_string=Column(String(255))
    ua_name=Column(String(255))
    ua_ver=Column(String(255))
    updated_at=Column(TIMESTAMP, nullable=False)
class credential_cores_tasks(Base):
    __tablename__ = "credential_cores_tasks"
    core_id=Column(Integer,primary_key=True)
    task_id=Column(Integer,primary_key=True)
class credential_logins_tasks(Base):
    __tablename__ = "credential_logins_tasks"
    login_id=Column(Integer,primary_key=True)
    task_id=Column(Integer,primary_key=True)
class creds(Base):
    __tablename__ ="creds"
    service_id=Column(Integer,primary_key=True,nullable=False)
    user= Column(String(255))
    passw = Column(String(255))
    active=Column(Boolean, unique=False, default=True)
    proof=Column(String(255))
    ptype=Column(String(255))
    source_id=Column(Integer,primary_key=True)
    source_type=Column(String(255))
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
class events(Base):
    __tablename__="events"
    workspace_id=Column(Integer,primary_key=True)
    host_id=Column(Integer,primary_key=True)
    name=Column(String(255))
    critical=Column(Boolean, unique=False, default=False)
    seen=Column(Boolean, unique=False, default=False)
    username=Column(String(255))
    info=Column(String(255))
class exploit_attempts(Base):
    __tablename__= "exploit_attempts"
    host_id=Column(Integer,primary_key=True)
    service_id=Column(Integer,primary_key=True)
    session_id=Column(Integer,primary_key=True)
    vuln_id=Column(Integer,primary_key=True)
    loot_id=Column(Integer,primary_key=True)
    exploited=Column(Boolean, unique=False, default=False)
    attempted_at=Column(String(255))
    fail_reason=Column(String(255))
    username=Column(String(255))
    module=Column(String(255))
    port=Column(Integer)
    proto=Column(String(255))
    fail_detail=Column(String(255))
class exploited_hosts(Base):
    __tablename__="exploited_hosts"
    host_id=Column(Integer,nullable=False,primary_key=True)
    service_id=Column(Integer,primary_key=True)
    session_uuid=Column(Integer)
    name=Column(Integer)
    payload=Column(Integer)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
class host_details(Base):
    __tablename__="host_details"
    host_id=Column(Integer,primary_key=True)
    nx_console_id=Column(Integer,primary_key=True)
    nx_device_id=Column(Integer,primary_key=True)
    src=Column(String(255))
    nx_site_name=Column(String(255))
    nx_site_importance=Column(String(255))
    nx_scan_template=Column(String(255))
    nx_risk_score=Column(String(255))
class hosts(Base):
    __tablename__ = "hosts"
    address=Column(String(255))
    mac=Column(String(255))
    comm=Column(String(255))
    name=Column(String(255))
    state=Column(String(255))
    os_name=Column(String(255))
    os_flavor=Column(String(255))
    os_sp=Column(String(255))
    os_lang=Column(String(255))
    arch=Column(String(255))
    workspace_id=Column(Integer,primary_key=True)
    purpose=Column(String(255))
    info=Column(String(255))
    comments=Column(String(255))
    scope=Column(String(255))
    virtual_host=Column(String(255))
    note_count=Column(Integer,default=0)
    vuln_count=Column(Integer,default=0)
    service_count=Column(Integer,default=0)
    host_detail_count=Column(Integer,default=0)
    xploit_attempt_count=Column(Integer,default=0)
    cred_count=Column(Integer,default=0)
    detected_arch=Column(String(255))
    os_family=Column(String(255))
    __table_args__ = (
        Index('index_hosts_on_name', 'name'),
        Index('index_hosts_on_os_flavor', 'os_flavor'),
        Index('index_hosts_on_os_name', 'os_name'),
        Index('index_hosts_on_purpose','purpose'),
        Index('index_hosts_on_state','state'),
        Index('index_hosts_on_workspace_id_and_address','workspace_id','address'),
    )
class hosts_tags(Base):
    __tablename__ = "hosts_tags"
    host_id=Column(Integer,primary_key=True)
    tag_id=Column(Integer,primary_key=True)
class listeners(Base):
    __tablename__="listeners"
    workspace_id = Column(Integer,nullable=False,default=1)
    task_id=Column(Integer,primary_key=True)
    enabled=Column(Boolean,default=True)
    owner=Column(String(255))
    payload=Column(String(255))
    address=Column(String(255))
    port=Column(Integer)
    options=Column(Binary)
    macro=Column(String(255))
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
class loots(Base):
    __tablename__="loots"
    workspace_id = Column(Integer,default=1,nullable=False,primary_key=True)
    host_id = Column(Integer,primary_key=True)
    service_id = Column(Integer,primary_key=True)
    ltype=Column(String(255))
    path=Column(String(255))
    data=Column(String(255))
    content_type=Column(String(255))
    name=Column(String(255))
    info=Column(String(255))
    module_run_id=Column(Integer,primary_key=True)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
    __table_args__ = (
        Index('index_loots_on_module_run_id', 'module_run_id'),

    )
class Macros(Base):
    __tablename__="Macros"
    id=Column(Integer,primary_key=True)
    owner=Column(String(255))
    name=Column(String(255))
    description=Column(String(255))
    actions=Column(Binary)
    prefs=Column(Binary)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
class thg_credential_cores(Base):
    __tablename__="thg_credential_cores"
    origin_id=Column(Integer,primary_key=True,default=0)
    origin_type=Column(String(255),nullable=False)
    private_id=Column(Integer,primary_key=True)
    public_id=Column(Integer,primary_key=True)
    realm_id=Column(Integer,primary_key=True)
    workspace_id=Column(Integer,primary_key=True)
    logins_count=Column(Integer,primary_key=True,default=0)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
    __table_args__ = (
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
    )
class thg_credential_logins(Base):
    __tablename__="thg_credential_logins"
    core_id=Column(Integer,primary_key=True,nullable=False)
    service_id=Column(Integer,primary_key=True,nullable=False)
    access_level=Column(String(255),nullable=False)
    status=Column(String(255),nullable=False)
    last_attempted_at=Column(TIMESTAMP, nullable=False)
    created_at=Column(TIMESTAMP, nullable=False)
    updated_at=Column(TIMESTAMP, nullable=False)
    __table_args__ = (
        Index('index_thg_credential_logins_on_core_id_and_service_id', 'service_id', 'core_id'),
        Index('index_thg_credential_logins_on_service_id_and_core_id', 'service_id','core_id'),
    )
class thg_credential_origin_cracked_passwords(Base):
    __tablename__="thg_credential_origin_cracked_passwords"
    thg_credential_core_id=Column(Integer,primary_key=True,nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
    __table_args__ = (
        Index('originating_credential_cores', 'thg_credential_core_id'),
    )
class thg_credential_origin_imports(Base):
    __tablename__ ="thg_credential_origin_imports"
    filename=Column(String(255))
    task_id=Column(Integer,primary_key=True,nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
    __table_args__ = (
        Index('index_thg_credential_origin_imports_on_task_id', 'task_id'),
    )
class thg_credential_origin_manuals(Base):
    __tablename__ ="thg_credential_origin_manuals"
    user_id=Column(Integer,primary_key=True,nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
    __table_args__ = (
        Index('index_thg_credential_origin_manuals_on_user_id', 'user_id'),
    )
class thg_credential_origin_services(Base):
    __tablename__ ="thg_credential_origin_services"
    service_id=Column(Integer,primary_key=True,nullable=False)
    module_full_name=Column(String(255))
    __table_args__ = (
        Index('unique_thg_credential_origin_services', 'service_id','module_full_name'),
    )
class thg_credential_origin_sessions(Base):
    __tablename__ = "thg_credential_origin_sessions"
    post_reference_name=Column(String(255),nullable=False)
    session_id=Column(Integer,primary_key=True,nullable=False)
    __table_args__ = (
        Index('unique_thg_credential_origin_sessions', 'session_id', 'post_reference_name'),
    )
class thg_credential_privates(Base):
    __tablename__="thg_credential_privates"
    id = Column(Integer,nullable=False,primary_key=True)
    types=Column(String(255),nullable=False)
    data=Column(String(255),nullable=False)
    jtr_format=Column(String(255),nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
    __table_args__ = (
        Index('index_thg_credential_privates_on_type_and_data', 'types', 'data'),
        Index('index_thg_credential_privates_on_type_and_data_sshkey','types')
    )
class thg_credential_publics(Base):
    __tablename__="thg_credential_publics"
    id = Column(Integer, nullable=False, primary_key=True)
    username=Column(String(255),nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
    __table_args__ = (
        Index('index_thg_credential_publics_on_username', 'username'),
    )
class thg_credential_realms(Base):
    __tablename__="thg_credential_realms"
    id = Column(Integer, nullable=False, primary_key=True)
    key=Column(String(255),nullable=False)
    value=Column(String(255),nullable=False)
    __table_args__ = (
        Index('index_thg_credential_realms_on_key_and_value', 'key','value'),
    )
class mod_refs(Base):
    __tablename__ = "mod_refs"
    id = Column(Integer, nullable=False, primary_key=True)
    module=Column(String(255),nullable=False)
    mtype=Column(String(255),nullable=False)
    ref=Column(String(255),nullable=False)
class module_actions(Base):
    __tablename__ = "module_actions"
    detail_id=Column(Integer, nullable=False, primary_key=True)
    name=Column(String(255),nullable=False)
    __table_args__ = (
        Index('index_module_actions_on_detail_id', 'detail_id'),
    )
class module_archs(Base):
    __tablename__= "module_archs"
    detail_id=Column(Integer, nullable=False, primary_key=True)
    name=Column(String(255),nullable=False)
    __table_args__ = (
        Index('index_module_archs_on_detail_id', 'detail_id'),
    )
class module_authors(Base):
    __tablename__ = "module_authors"
    detail_id=Column(Integer, nullable=False, primary_key=True)
    name=Column(String(255),nullable=False)
    email=Column(String(255),nullable=False)
    __table_args__ = (
        Index('index_module_authors_on_detail_id', 'detail_id'),
    )
class module_details(Base):
    __tablename__="module_details"
    id=Column(Integer,primary_key=True)
    mtime=Column(TIMESTAMP, nullable=False)
    file=Column(String(255),nullable=False)
    mtype=Column(String(255),nullable=False)
    refname=Column(String(255),nullable=False)
    fullname=Column(String(255),nullable=False)
    name=Column(String(255),nullable=False)
    rank=Column(Integer,nullable=False)
    description=Column(String(255),nullable=False)
    license=Column(String(255),nullable=False)
    privileged=Column(Boolean,nullable=False)
    disclosure_date=Column(TIMESTAMP,nullable=False)
    default_target=Column(Integer,nullable=False)
    default_action=Column(String(255),nullable=False)
    stance=Column(String(255),nullable=False)
    ready=Column(Boolean,nullable=False)
    __table_args__ = (
        Index('index_module_details_on_description', 'description'),
        Index('index_module_details_on_mtype','mtype'),
        Index('index_module_details_on_name', 'name'),
        Index('index_module_details_on_refname', 'refname'),
    )
class module_mixins(Base):
    __tablename__="module_mixins"
    detail_id=Column(Integer,primary_key=True)
    name=Column(String(255),nullable=False)
    __table_args__ = (
        Index('index_module_mixins_on_detail_id', 'detail_id'),
    )
class module_platforms(Base):
    __tablename__="module_platforms"
    detail_id=Column(Integer,primary_key=True)
    name=Column(String(255),nullable=False)
    __table_args__ = (
        Index('index_module_platforms_on_detail_id', 'detail_id'),
    )
class module_refs(Base):
    __tablename__="module_refs"
    detail_id=Column(Integer,primary_key=True)
    name=Column(String(255),nullable=False)
    __table_args__ = (
        Index('index_module_refs_on_detail_id', 'detail_id'),
        Index('index_module_refs_on_name','name'),
    )
class module_runs(Base):
    __tablename__="module_runs"
    id = Column(Integer,primary_key=True,nullable=False)
    attempted_at=Column(TIMESTAMP,nullable=True)
    fail_detail=Column(String(255),nullable=False)
    fail_reason=Column(String(255),nullable=False)
    module_fullname=Column(String(255),nullable=False)
    port=Column(Integer,nullable=False)
    proto=Column(String(255),nullable=False)
    status = Column(String(255), nullable=False)
    session_id=Column(Integer,nullable=False)
    trackable_id=Column(Integer,nullable=False)
    trackable_type=Column(String(255),nullable=False)
    user_id=Column(String(255),nullable=False)
    username=Column(String(255),nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
    __table_args__ = (
        Index('index_module_runs_on_session_id', 'session_id'),
        Index('index_module_runs_on_user_id','user_id'),
    )
class module_targets(Base):
    __tablename__="module_targets"

    detail_id=Column(Integer,nullable=False,primary_key=True)
    index=Column(Integer,nullable=False)
    name=Column(String(255),nullable=False)
    __table_args__ = (
        Index('index_module_targets_on_detail_id', 'detail_id'),
    )
class nexpose_consoles(Base):
    __tablename__="nexpose_consoles"
    id= Column(Integer,primary_key=True)
    enabled= Column(Boolean,default=True)
    owner=Column(String(255),nullable=False)
    address=Column(String(255),nullable=False)
    port=Column(Integer,nullable=False,default=3780)
    username=Column(String(255),nullable=False)
    password=Column(String(255),nullable=False)
    status=Column(String(255),nullable=False)
    version=Column(String(255),nullable=False)
    cert=Column(String(255),nullable=False)
    cached_sites=Column(Binary)
    name=Column(String(255),nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
class notes(Base):
    __tablename__ ="notes"
    id = Column(Integer,primary_key=True)
    ntype=Column(String(255),nullable=False)
    workspace_id=Column(Integer,nullable=False,default=1)
    service_id=Column(Integer,nullable=False)
    host_id=Column(Integer,nullable=False)
    data=Column(String(255),nullable=False)
    critical= Column(Boolean,default=True)
    seen= Column(Boolean,default=True)
    vuln_id= Column(Integer)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
    __table_args__ = (
        Index('index_notes_on_ntype', 'ntype'),
        Index('index_notes_on_vuln_id', 'vuln_id'),
    )
class payloads(Base):
    __tablename__ ="payloads"
    id = Column(Integer, primary_key=True)
    name=Column(String(255),nullable=False)
    uuid=Column(String(255),nullable=False)
    arch=Column(String(255),nullable=False)
    platform=Column(String(255),nullable=False)
    urls=Column(String(255),nullable=False)
    description=Column(String(255),nullable=False)
    raw_payload=Column(String(255),nullable=False)
    build_status=Column(String(255),nullable=False)
    raw_payload_hash=Column(String(255),nullable=False)
    build_opts=Column(String(255),nullable=False)
    uuid_mask= Column(Integer)
    timestamp= Column(Integer)
    workspace_id= Column(Integer,nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
class profiles(Base):
    __tablename__= "profiles"
    id = Column(Integer, primary_key=True)
    active =Column(Boolean,default=True)
    name=Column(String(255),nullable=False)
    owner=Column(String(255),nullable=False)
    settings =Column(Binary)
class refs(Base):
    __tablename__ = "refs"
    id = Column(Integer, primary_key=True)
    ref_id=Column(Integer,nullable=False)
    name= Column(String(255),nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
    __table_args__ = (
        Index('index_refs_on_name', 'name'),
    )
class report_templates(Base):
    __tablename__="report_templates"
    workspace_id = Column(Integer, primary_key=True,nullable=False)
    created_by= Column(String(255),nullable=False)
    path= Column(String(255),nullable=False)
    name= Column(String(255),nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
class reports(Base):
    __tablename__= "reports"
    workspace_id = Column(Integer, primary_key=True, nullable=False)
    created_by = Column(String(255), nullable=False)
    path = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    options=Column(String(255), nullable=False)
    downloaded_at=Column(String(255), nullable=False)
    task_id= Column(Integer, primary_key=True, nullable=False)
class routes(Base):
    __tablename__ = "routes"
    session_id=Column(String(255), nullable=False,primary_key=True)
    subnet=Column(String(255), nullable=False)
    netmask=Column(String(255), nullable=False)
class services(Base):
    __tablename__= "services"

    host_id=Column(Integer, nullable=False,primary_key=True)
    port=Column(String(255), nullable=False)
    proto=Column(String(255), nullable=False)
    state=Column(String(255), nullable=False)
    name=Column(String(255), nullable=False)
    info=Column(String(255), nullable=False)
    __table_args__ = (
        Index('index_services_on_host_id_and_port_and_proto', 'host_id','port','proto'),
        Index('index_services_on_name', 'name'),
        Index('index_services_on_port', 'port'),
        Index('index_services_on_proto', 'name'),
        Index('index_services_on_state', 'state'),
    )
class session_events(Base):
    __tablename__ = "session_events"
    session_id =Column(Integer,primary_key=True,nullable=True)
    etype =Column(String(255), nullable=False)
    command = Column(Binary,nullable=True)
    output= Column(Binary,nullable=True)
    remote_path=Column(String(255), nullable=False)
    local_path =Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
class sessions(Base):
    __tablename__ = "sessions"
    host_id=Column(Integer,primary_key=True,nullable=True)
    stype=Column(String(255), nullable=False)
    via_exploit=Column(String(255), nullable=False)
    via_payload=Column(String(255), nullable=False)
    desc=Column(String(255), nullable=False)
    port = Column(Integer,nullable=False)
    platform=Column(String(255), nullable=False)
    datastore=Column(String(255), nullable=False)
    closed_at = Column(TIMESTAMP,nullable=False)
    close_reason=Column(String(255), nullable=False)
    local_id= Column(Integer,nullable=False,primary_key=True)
    last_seen= Column(TIMESTAMP,nullable=False)
    module_run_id= Column(Integer,nullable=False,primary_key=True)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)

    __table_args__ = (Index('index_sessions_on_module_run_id','module_run_id'),)
class tags(Base):
    __tablename__ = "tags"
    user_id= Column(Integer,nullable=False,primary_key=True)
    name=Column(String(255), nullable=False)
    desc=Column(String(255), nullable=False)
    report_summary= Column(Binary,default=False,nullable=False)
    report_detail= Column(Binary,default=False,nullable=False)
    critical= Column(Binary,default=False,nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
class task_creds(Base):
    __tablename__ = "task_creds"
    task_id= Column(Integer,nullable=False,primary_key=True)
    cred_id= Column(Integer,nullable=False,primary_key=True)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
class task_hosts(Base):
    __tablename__ ="task_hosts"
    task_id= Column(Integer,nullable=False,primary_key=True)
    cred_id= Column(Integer,nullable=False,primary_key=True)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
class task_services(Base):
    __tablename__ ="task_services"
    task_id= Column(Integer,nullable=False,primary_key=True)
    cred_id= Column(Integer,nullable=False,primary_key=True)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
class task_sessions(Base):
    __tablename__ ="task_sessions"
    task_id= Column(Integer,nullable=False,primary_key=True)
    cred_id= Column(Integer,nullable=False,primary_key=True)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
class tasks(Base):
    __tablename__ ="tasks"
    workspace_id = Column(Integer,default=1,nullable=False,primary_key=True)
    created_by=Column(String(255), nullable=False)
    module=Column(String(255), nullable=False)
    completed_at=Column(TIMESTAMP, nullable=False)
    path=Column(String(255), nullable=False)
    info=Column(String(255), nullable=False)
    description=Column(String(255), nullable=False)
    progress=Column(Integer,primary_key=True,nullable=False)
    options=Column(String(255), nullable=False)
    error=Column(String(255), nullable=False)
    result =Column(String(255), nullable=False)
    module_uuid =Column(String(255), nullable=False)
    settings = Column(Binary)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
class users(Base):
    __tablename__ ="users"
    id = Column(Integer,primary_key=True)
    username =Column(String(255), nullable=False)
    crypted_password =Column(String(255), nullable=False)
    password_salt =Column(String(255), nullable=False)
    persistence_token =Column(String(255), nullable=False)
    fullname =Column(String(255), nullable=False)
    email =Column(String(255), nullable=False)
    phone =Column(String(255), nullable=False)
    company =Column(String(255), nullable=False)
    prefs =Column(String(255), nullable=False)
    admin = Column(Boolean,default=True,nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
class vuln_attempts(Base):
    __tablename__ ="vuln_attempts"
    vuln_id =Column(Integer,primary_key=True)
    attempted_at= Column(TIMESTAMP, nullable=False)
    exploited =Column(Boolean,default=False,nullable=False)
    fail_reason =Column(String(255), nullable=False)
    username =Column(String(255), nullable=False)
    module =Column(String(255), nullable=False)
    loot_id =Column(Integer,primary_key=True)
    session_id =Column(Integer,primary_key=True)
    fail_detail =Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
class vuln_details(Base):
    __tablename__ ="vuln_details"
    vuln_id=Column(Integer,nullable=False,primary_key=True)
    cvss_score=Column(Float)
    cvss_vector=Column(String(255), nullable=False)
    title=Column(String(255), nullable=False)
    description =Column(String(255), nullable=False)
    solution =Column(String(255), nullable=False)
    proof=Column(Binary)
    nx_console_id =Column(Integer,nullable=False,primary_key=True)
    nx_device_id =Column(Integer,nullable=False,primary_key=True)
    nx_vuln_id =Column(String(255), nullable=False)
    nx_severity=Column(Float)
    nx_pci_severity =Column(Float)
    nx_published=Column(TIMESTAMP, nullable=False)
    nx_added =Column(TIMESTAMP, nullable=False)
    nx_modified =Column(TIMESTAMP, nullable=False)
    nx_tags =Column(String(255), nullable=False)
    nx_vuln_status =Column(String(255), nullable=False)
    nx_proof_key =Column(String(255), nullable=False)
    src =Column(String(255), nullable=False)
    nx_scan_id = Column(Integer,nullable=False,primary_key=True)
    nx_vulnerable_since =Column(TIMESTAMP, nullable=False)
    nx_pci_compliance_status=Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
class vulns(Base):
    __tablename__="vulns"
    host_id= Column(Integer,nullable=False,primary_key=True)
    service_id= Column(Integer,nullable=False,primary_key=True)
    name=Column(String(255), nullable=False)
    info=Column(String(255), nullable=False)
    exploited_at= Column(TIMESTAMP, nullable=False)
    vuln_detail_count= Column(Integer,nullable=False,primary_key=True,default=0)
    vuln_attempt_count= Column(Integer,nullable=False,primary_key=True,default=0)
    origin_id= Column(Integer,nullable=False,primary_key=True,default=0)
    origin_type=Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
    __table_args__ = (Index('index_vulns_on_name','name'),Index('index_vulns_on_origin_id','origin_id'))
class vulns_refs(Base):
    __tablename__ = "vulns_refs"
    ref_id =Column(Integer,nullable=False,primary_key=True)
    vuln_id =Column(Integer,nullable=False,primary_key=True)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
class web_forms(Base):
    __tablename__ ="web_forms"
    web_site_id =Column(Integer,nullable=False,primary_key=True)
    path=Column(String(255), nullable=False)
    method=Column(String(255), nullable=False)
    params=Column(String(255), nullable=False)
    query=Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
    __table_args__ = (Index('index_web_forms_on_path','path'),)
class web_pages(Base):
    __tablename__="web_pages"

    web_site_id=Column(Integer,nullable=False,primary_key=True)
    path=Column(String(255), nullable=False)
    query=Column(String(255), nullable=False)
    code=Column(Integer,nullable=False,primary_key=True)
    cookie=Column(String(255), nullable=False)
    auth=Column(String(255), nullable=False)
    ctype=Column(String(255), nullable=False)
    mtime =Column(TIMESTAMP, nullable=False)
    location=Column(String(255), nullable=False)
    headers =Column(String(255), nullable=False)
    body=Column(Binary)
    request=Column(Binary)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
    __table_args__ = (Index('index_web_pages_on_path', 'path'),Index('index_web_pages_on_query','query'))
class web_sites(Base):
    __tablename__="web_sites"

    service_id=Column(Integer,nullable=False,primary_key=True)
    vhost=Column(String(255), nullable=False)
    comments=Column(String(255), nullable=False)
    options=Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
    __table_args__ = (Index('index_web_sites_on_comments', 'comments'),Index('index_web_sites_on_options','options'),Index('index_web_sites_on_vhost','vhost'))
class web_vulns(Base):
    __tablename__= "web_vulns"
    web_site_id = Column(Integer,nullable=False,primary_key=True)
    path=Column(String(255), nullable=False)
    method=Column(String(255), nullable=False)
    params=Column(String(255), nullable=False)
    pname=Column(String(255), nullable=False)
    risk=Column(Integer,nullable=False,primary_key=True)
    name=Column(String(255), nullable=False)
    query=Column(String(255), nullable=False)
    category=Column(String(255), nullable=False)
    confidence=Column(Integer,nullable=False,primary_key=True)
    description =Column(String(255), nullable=False)
    blame =Column(String(255), nullable=False)
    request=Column(Binary)
    proof =Column(Binary)
    owner=Column(String(255), nullable=False)
    payload=Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
    __table_args__= (Index('index_web_vulns_on_method','method'),
                      Index('index_web_vulns_on_name','name'),
                      Index('index_web_vulns_on_path','path'),)
class wmap_requests(Base):
    __tablename__="wmap_requests"
    host=Column(String(255), nullable=False)
    address=Column(Integer,nullable=False,primary_key=True)
    port=Column(String(255), nullable=False)
    ssl=Column(Integer,nullable=False,primary_key=True)
    meth=Column(String(255), nullable=False)
    path=Column(String(255), nullable=False)
    headers=Column(String(255), nullable=False)
    query=Column(String(255), nullable=False)
    body=Column(String(255), nullable=False)
    respcode=Column(String(255), nullable=False)
    resphead=Column(String(255), nullable=False)
    response=Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
class wmap_targets(Base):
    __tablename__ = "wmap_targets"
    host=Column(String(255), nullable=False)
    address=Column(String(255))
    port=Column(Integer,nullable=False,primary_key=True)
    ssl=Column(Integer,nullable=False,primary_key=True)
    selected=Column(Integer,nullable=False,primary_key=True)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
class workspace_members(Base):
    __tablename__ = "workspace_members"
    workspace_id=Column(Integer,nullable=False,primary_key=True)
    user_id=Column(Integer,nullable=False,primary_key=True)
class workspaces(Base):
    __tablename__="workspaces"
    name=Column(String(255), nullable=False)
    boundary=Column(String(255), nullable=False)
    description=Column(String(255), nullable=False)
    owner_id=Column(Integer,nullable=False,primary_key=True)
    limit_to_network=Column(Boolean,nullable=False,default=False)
    import_fingerprint=Column(Boolean,default=False)

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///THG.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)