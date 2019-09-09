"""
Retrieve and load the user inputs for common fields.
config command.
"""
import os
import json

# the absolute path to config.json
path_config = os.path.join(
    os.path.dirname(__file__), 'config.json')


def load_json():
    """
    Load the config.json
    """
    with open(path_config, 'r') as f:
        return json.load(f)


def write_json(author, mail):
    """
    Retrieves the input info form thgc.config()
    and write the confit.json.
    """
    loaded_config = load_json()
    loaded_config['default_author'] = author
    loaded_config['default_mail'] = mail

    with open(path_config, 'w') as f:
        json.dump(loaded_config, f)


def show_common(field):
    """
    return the default data for the assistant command
    """
    loaded_config = load_json()
    return loaded_config[field]


if __name__ == '__main__':
    pass
