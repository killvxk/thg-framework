########################################################################################################################
# The   THG RESTful API.
# Adapted from http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
# example code at https://gist.github.com/miguelgrinberg/5614326
########################################################################################################################
#    Verb     URI                                            Action
#    ----     ---                                            ------
########################################################################################################################
#################################################-API-THG-CONFIG-#######################################################
########################################################################################################################
#    GET      http://localhost:1999/api/version              return the current THG version
#    GET      http://localhost:1999/api/config               return the current default config
#    GET      http://localhost:1999/api/shells               return all current shells
#    GET      http://localhost:1999/api/shells/X             return the shell with name X
#    POST     http://localhost:1999/api/base_shell           generate a shell given supplied options (need to implement)
########################################################################################################################
###################################################-API-THG-MODS-#######################################################
########################################################################################################################
#    GET      http://localhost:1999/api/modules                     return all current modules
#    GET      http://localhost:1999/api/modules/<name>              return the module with the specified name
#    POST     http://localhost:1999/api/modules/<name>              execute the given module with the specified options
#    POST     http://localhost:1999/api/modules/search              searches modulesfor a passed term
#    POST     http://localhost:1999/api/modules/search/modulename   searches module names for a specific term
#    POST     http://localhost:1999/api/modules/search/description  searches module descriptions for a specific term
#    POST     http://localhost:1999/api/modules/search/description  searches module comments for a specific term
#    POST     http://localhost:1999/api/modules/search/author       searches module authors for a specific term
#    POST     http://localhost:1999/api/modules/search/cve_id       searches module cve_id for a specific term
########################################################################################################################
#################################################-API-THG-listeners-####################################################
########################################################################################################################
#    GET      http://localhost:1999/api/listeners            return all current listeners
#    GET      http://localhost:1999/api/listeners/Y          return the listener with id Y
#    GET      http://localhost:1999/api/listeners/options    return all listener options
#    POST     http://localhost:1999/api/listeners            starts a new listener with the specified options
#    DELETE   http://localhost:1999/api/listeners/Y          kills listener Y
########################################################################################################################
#################################################-API-THG-cybersX-######################################################
########################################################################################################################
#    GET      http://localhost:1999/api/cybersX               return all current cybersX
#    GET      http://localhost:1999/api/cybersX/stale         return all stale cybersX
#    DELETE   http://localhost:1999/api/cybersX/stale         removes stale cybersX from the database
#    DELETE   http://localhost:1999/api/cybersX/Y             removes agent Y from the database
#    GET      http://localhost:1999/api/cybersX/Y             return the agent with name Y
#    GET      http://localhost:1999/api/cybersX/Y/results     return tasking results for the agent with name Y
#    DELETE   http://localhost:1999/api/cybersX/Y/results     deletes the result buffer for agent Y
#    POST     http://localhost:1999/api/cybersX/Y/shell       task agent Y to execute a shell command
#    POST     http://localhost:1999/api/cybersX/Y/rename      rename agent Y
#    GET/POST http://localhost:1999/api/cybersX/Y/clear       clears the result buffer for agent Y
#    GET/POST http://localhost:1999/api/cybersX/Y/kill        kill agent Y
#    GET      http://localhost:1999/api/creds                return stored credentials
#    POST     http://localhost:1999/api/creds                add creds to the database
########################################################################################################################
#################################################-API-THG-RPORT-########################################################
########################################################################################################################
#    GET      http://localhost:1999/api/reporting            return all logged events
#    GET      http://localhost:1999/api/reporting/agent/X    return all logged events for the given agent name X
#    GET      http://localhost:1999/api/reporting/type/Y     return all logged events of type Y (checkin, task, result, rename)
#    GET      http://localhost:1999/api/reporting/msg/Z      return all logged events matching message Z, wildcards accepted
#    GET      http://localhost:1999/api/creds                return stored credentials
#    POST     http://localhost:1999/api/creds                add creds to the database
########################################################################################################################
#################################################-API-THG-ADM-##########################################################
########################################################################################################################
#    GET      http://localhost:1999/api/admin/login          retrieve the API token given the correct username and password
#    POST     http://localhost:1999/api/admin/login          add retrieve the API token given the correct username and password
#    GET      http://localhost:1999/api/admin/permanenttoken retrieve the permanent API token, generating/storing one if it doesn't already exist
#    GET      http://localhost:1999/api/admin/shutdown       shutdown the RESTful API
#    GET      http://localhost:1999/api/admin/restart        restart the RESTful API
#
####################################################################
from flask import Flask
from flask_restful import Api
from lib.thg.api.resources.modules import Hoteis, Hotel

app = Flask(__name__)
api = Api(app)

api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')

if __name__ == '__main__':
    app.run(debug=True)
