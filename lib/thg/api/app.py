########################################################################################################################
# The   THG RESTful API.
# Adapted from http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
# example code at https://gist.github.com/miguelgrinberg/5614326
########################################################################################################################
#    Verb     URI                                            Action
#    ----     ---                                            ------

#################################################-API-THG-CONFIG-#######################################################

#
#    GET      http://localhost:1999/api/v1/version              return the current THG version
#    GET      http://localhost:1999/api/v1/config               return the current default config
#    GET      http://localhost:1999/api/v1/shells               return all current shells
#    GET      http://localhost:1999/api/v1/shells/X             return the shell with name X
#    POST     http://localhost:1999/api/v1/base_shells          generate a shell given supplied options (need to implement)
#

###################################################-API-THG-MODS-#######################################################

#
#    GET      http://localhost:1999/api/v1/modules                     return all current modules
#    GET      http://localhost:1999/api/v1/modules/<name>              return the module with the specified name
#    POST     http://localhost:1999/api/v1/modules/<name>              execute the given module with the specified options
#    POST     http://localhost:1999/api/v1/modules/search              searches modulesfor a passed term
#    POST     http://localhost:1999/api/v1/modules/search/modulename   searches module names for a specific term
#    POST     http://localhost:1999/api/v1/modules/search/description  searches module descriptions for a specific term
#    POST     http://localhost:1999/api/v1/modules/search/description  searches module comments for a specific term
#    POST     http://localhost:1999/api/v1/modules/search/author       searches module authors for a specific term
#    POST     http://localhost:1999/api/v1/modules/search/cve_id       searches module cve_id for a specific term
#

#################################################-API-THG-listeners-####################################################

#
#    GET      http://localhost:1999/api/v1/listeners            return all current listeners
#    GET      http://localhost:1999/api/v1/listeners/Y          return the listener with id Y
#    GET      http://localhost:1999/api/v1/listeners/options    return all listener options
#    POST     http://localhost:1999/api/v1/listeners            starts a new listener with the specified options
#    DELETE   http://localhost:1999/api/v1/listeners/Y          kills listener Y
#

#################################################-API-THG-cybersX-######################################################

#
#    GET      http://localhost:1999/api/v1/cybersX               return all current cybersX
#    GET      http://localhost:1999/api/v1/cybersX/stale         return all stale cybersX
#    DELETE   http://localhost:1999/api/v1/cybersX/stale         removes stale cybersX from the database
#    DELETE   http://localhost:1999/api/v1/cybersX/Y             removes agent Y from the database
#    GET      http://localhost:1999/api/v1/cybersX/Y             return the agent with name Y
#    GET      http://localhost:1999/api/v1/cybersX/Y/results     return tasking results for the agent with name Y
#    DELETE   http://localhost:1999/api/v1/cybersX/Y/results     deletes the result buffer for agent Y
#    POST     http://localhost:1999/api/v1/cybersX/Y/shell       task agent Y to execute a shell command
#    POST     http://localhost:1999/api/v1/cybersX/Y/rename      rename agent Y
#    GET/POST http://localhost:1999/api/v1/cybersX/Y/clear       clears the result buffer for agent Y
#    GET/POST http://localhost:1999/api/v1/cybersX/Y/kill        kill agent Y
#    GET      http://localhost:1999/api/v1/creds                return stored credentials
#    POST     http://localhost:1999/api/v1/creds                add creds to the database
#

#################################################-API-THG-RPORT-########################################################

#
#    GET      http://localhost:1999/api/v1/reporting            return all logged events
#    GET      http://localhost:1999/api/v1/reporting/agent/X    return all logged events for the given agent name X
#    GET      http://localhost:1999/api/v1/reporting/type/Y     return all logged events of type Y (checkin, task, result, rename)
#    GET      http://localhost:1999/api/v1/reporting/msg/Z      return all logged events matching message Z, wildcards accepted
#    GET      http://localhost:1999/api/v1/creds                return stored credentials
#    POST     http://localhost:1999/api/v1/creds                add creds to the database
#

#################################################-API-THG-ADM-##########################################################

#    GET      http://localhost:1999/api/v1/admin/login          retrieve the API token given the correct username and password
#    POST     http://localhost:1999/api/v1/admin/login          add retrieve the API token given the correct username and password
#    GET      http://localhost:1999/api/v1/admin/permanenttoken retrieve the permanent API token, generating/storing one if it doesn't already exist
#    GET      http://localhost:1999/api/v1/admin/shutdown       shutdown the RESTful API
#    GET      http://localhost:1999/api/v1/admin/restart        restart the RESTful API
#
########################################################################################################################

from flask import Flask
from flask_restful import Api
from lib.thg.api.resources.modules import Hoteis

app = Flask(__name__)
api = Api(app)

#################################################-API-THG-CONFIG-#######################################################
#
#    GET      http://localhost:1999/api/v1/version              return the current THG version
#    GET      http://localhost:1999/api/v1/config               return the current default config
#    GET      http://localhost:1999/api/v1/shells               return all current shells
#    GET      http://localhost:1999/api/v1/shells/X             return the shell with name X
#    POST     http://localhost:1999/api/v1/base_shells          generate a shell given supplied options (need to implement)
#
########################################################################################################################
api.add_resource(Hoteis,"/api/v1/version")#[http://localhost:1999/api/v1/version]-[return the current THG version-[GET]]
api.add_resource(Hoteis,"/api/v1/config")#[http://localhost:1999/api/v1/config]-[return the current default config-[GET]]
api.add_resource(Hoteis,"/api/v1/shells")#[http://localhost:1999/api/v1/shells]-[return all current shells-[GET]]
api.add_resource(Hoteis,"/api/v1/shells/<string:shell_id>")#[http://localhost:1999/api/v1/shells/X]-[return the shell with name X-[GET]]
api.add_resource(Hoteis,"/api/v1/base_shells")#[http://localhost:1999/api/v1/base_shells]-[generate a shell given supplied options (need to implement)-[POST]]



'''
###################################################-API-THG-MODS-#######################################################
#
#    GET      http://localhost:1999/api/v1/modules                     return all current modules
#    GET      http://localhost:1999/api/v1/modules/<name>              return the module with the specified name
#    POST     http://localhost:1999/api/v1/modules/<name>              execute the given module with the specified options
#    POST     http://localhost:1999/api/v1/modules/search              searches modulesfor a passed term
#    POST     http://localhost:1999/api/v1/modules/search/modulename   searches module names for a specific term
#    POST     http://localhost:1999/api/v1/modules/search/description  searches module descriptions for a specific term
#    POST     http://localhost:1999/api/v1/modules/search/description  searches module comments for a specific term
#    POST     http://localhost:1999/api/v1/modules/search/author       searches module authors for a specific term
#    POST     http://localhost:1999/api/v1/modules/search/cve_id       searches module cve_id for a specific term
#
########################################################################################################################
api.add_resource(Hoteis,"/api/v1/modules")#[http://localhost:1999/api/v1/modules]-[return all current modules-[GET]]
api.add_resource(Hoteis,"/v1/modules/<string:nome>")#[http://localhost:1999/api/v1/modules/<name>]-[return all current modules-[GET-POST]]
api.add_resource(Hoteis,"/api/v1/modules/search")#[http://localhost:1999/api/v1/modules/search]-[searches modulesfor a passed term-[POST]]
api.add_resource(Hoteis,"/api/v1/modules/search/<string:modulename>")#[http://localhost:1999/api/v1/modules/search/modulename]-[searches module names for a specific term-[POST]]
api.add_resource(Hoteis,"/api/v1/modules/search/<string:description>")#[http://localhost:1999/api/v1/modules/search/description]-[searches module descriptions for a specific term-[POST]]
api.add_resource(Hoteis,"/api/v1/modules/search/<string:author>")#[http://localhost:1999/api/v1/modules/search/author]-[searches module authors for a specific term-[POST]]
api.add_resource(Hoteis,"/api/v1/modules/search/<string:cve_id>")#[http://localhost:1999/api/v1/modules/search/cve_id]-[searches module cve_id for a specific term-[POST]]
#################################################-API-THG-listeners-####################################################
#
#    GET      http://localhost:1999/api/v1/listeners            return all current listeners
#    GET      http://localhost:1999/api/v1/listeners/Y          return the listener with id Y
#    GET      http://localhost:1999/api/v1/listeners/options    return all listener options
#    POST     http://localhost:1999/api/v1/listeners            starts a new listener with the specified options
#    DELETE   http://localhost:1999/api/v1/listeners/Y          kills listener Y
#
########################################################################################################################
api.add_resource(Hoteis,"/api/v1/listeners")  #[http://localhost:1999/api/v1/listeners]-[return all current listeners[GET]]
api.add_resource(Hoteis,"/api/v1/listeners/<string:listeners_id>")#[http://localhost:1999/api/v1/listeners/Y]-[return the listener with id Y-[GET]]
api.add_resource(Hoteis,"/api/v1/listeners/<string:options>")#[http://localhost:1999/api/v1/listeners/options]-[return all listener options-[GET]]
api.add_resource(Hoteis,"/api/v1/listeners")#[http://localhost:1999/api/v1/listeners]-[starts a new listener with the specified options-[POST]]
api.add_resource(Hoteis,"/api/v1/listeners/<string:listeners_id>")#[http://localhost:1999/api/v1/listeners/Y]-[kills listener Y-[DELETE]]
#################################################-API-THG-cybersX-######################################################
#
#    GET      http://localhost:1999/api/v1/cybersX               return all current cybersX
#    GET      http://localhost:1999/api/v1/cybersX/stale         return all stale cybersX
#    DELETE   http://localhost:1999/api/v1/cybersX/stale         removes stale cybersX from the database
#    DELETE   http://localhost:1999/api/v1/cybersX/Y             removes agent Y from the database
#    GET      http://localhost:1999/api/v1/cybersX/Y             return the agent with name Y
#    GET      http://localhost:1999/api/v1/cybersX/Y/results     return tasking results for the agent with name Y
#    DELETE   http://localhost:1999/api/v1/cybersX/Y/results     deletes the result buffer for agent Y
#    POST     http://localhost:1999/api/v1/cybersX/Y/shell       task agent Y to execute a shell command
#    POST     http://localhost:1999/api/v1/cybersX/Y/rename      rename agent Y
#    GET/POST http://localhost:1999/api/v1/cybersX/Y/clear       clears the result buffer for agent Y
#    GET/POST http://localhost:1999/api/v1/cybersX/Y/kill        kill agent Y
#    GET      http://localhost:1999/api/v1/creds                 return stored credentials
#    POST     http://localhost:1999/api/v1/creds                add creds to the database
#
########################################################################################################################
api.add_resource(Hoteis,"/api/v1/cybersX")#[http://localhost:1999/api/v1/cybersX]-[return all current cybersX-[GET]]
api.add_resource(Hoteis,"/api/v1/cybersX/<string:stale>")#[http://localhost:1999/api/v1/cybersX/stale]-[return all stale cybersX-[GET]-[removes stale cybersX from the database-[DELETE]]
api.add_resource(Hoteis,"/api/v1/cybersX/<string:Y>")#[http://localhost:1999/api/v1/cybersX/Y]-[removes agent Y from the database-[DELETE]-[return the agent with name Y-[GET]]
api.add_resource(Hoteis,"/api/v1/cybersX/Y/results")#[http://localhost:1999/api/v1/cybersX/Y/results]-[return tasking results for the agent with name Y-[GET]-[deletes the result buffer for agent Y-[DELETE]]
api.add_resource(Hoteis,"/api/v1/cybersX/Y/shell")#[http://localhost:1999/api/v1/cybersX/Y/shell]-[task agent Y to execute a shell command-[POST]]
api.add_resource(Hoteis,"/api/v1/cybersX/Y/rename")#[http://localhost:1999/api/v1/cybersX/Y/rename]-[rename agent Y-[POST]]
api.add_resource(Hoteis,"/api/v1/cybersX/Y/clear")#[http://localhost:1999/api/v1/cybersX/Y/clear]-[clears the result buffer for agent Y-[GET/POST]]
api.add_resource(Hoteis,"/api/v1/cybersX/Y/kill")#[http://localhost:1999/api/v1/cybersX/Y/kill]-[kill agent Y-[GET/POST]]
api.add_resource(Hoteis,"/api/v1/creds")#[http://localhost:1999/api/v1/creds]-[return stored credentials-[GET/POST]]
#################################################-API-THG-RPORT-########################################################
#
#    GET      http://localhost:1999/api/v1/reporting            return all logged events
#    GET      http://localhost:1999/api/v1/reporting/agent/X    return all logged events for the given agent name X
#    GET      http://localhost:1999/api/v1/reporting/type/Y     return all logged events of type Y (checkin, task, result, rename)
#    GET      http://localhost:1999/api/v1/reporting/msg/Z      return all logged events matching message Z, wildcards accepted
#
########################################################################################################################
api.add_resource(Hoteis,"/api/v1/reporting")#[http://localhost:1999/api/v1/reporting]-[return all logged events-[GET]]]
api.add_resource(Hoteis,"/api/v1/reporting/agent/X")#[http://localhost:1999/api/v1/reporting/agent/X]-[return all logged events for the given agent name X-[GET]]]
api.add_resource(Hoteis,"/api/v1/reporting/type/Y")#[http://localhost:1999/api/v1/reporting/type/Y]-[return all logged events of type Y (checkin, task, result, rename)-[GET]]]
api.add_resource(Hoteis,"/api/v1/reporting/msg/Z")#[http://localhost:1999/api/v1/reporting/msg/Z]-[return all logged events matching message Z, wildcards accepted-[GET]]]
#################################################-API-THG-ADM-##########################################################
#
#    GET      http://localhost:1999/api/v1/admin/login          retrieve the API token given the correct username and password
#    POST     http://localhost:1999/api/v1/admin/login          add retrieve the API token given the correct username and password
#    GET      http://localhost:1999/api/v1/admin/permanenttoken retrieve the permanent API token, generating/storing one if it doesn't already exist
#    GET      http://localhost:1999/api/v1/admin/shutdown       shutdown the RESTful API
#    GET      http://localhost:1999/api/v1/admin/restart        restart the RESTful API
#
########################################################################################################################
api.add_resource(Hoteis,"")#[http://localhost:1999/api/v1/admin/login]-[retrieve the API token given the correct username and password/add retrieve the API token given the correct username and passwordadd retrieve the API token given the correct username and password-[GET/POST]]
api.add_resource(Hoteis,"")#[http://localhost:1999/api/v1/admin/permanenttoken]-[retrieve the permanent API token, generating/storing one if it doesn't already exist-[GET]]
api.add_resource(Hoteis,"")#[http://localhost:1999/api/v1/admin/shutdown]-[shutdown the RESTful API-[GET]]
api.add_resource(Hoteis,"")#[http://localhost:1999/api/v1/admin/restart]-[restart the RESTful API-[GET]]
'''

if __name__ == '__main__':
    app.run(debug=True)