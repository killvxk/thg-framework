"""
Create the structure of the python project and
Redirect the files and folders to the proper function.

Also write the AUTHORS.rst, LICENSE, .gitignore and
setup.py files with the users inputs.
"""
import os
import sys
import json
import click


def make_skeleton(project_name, authors, choosen_license, setup, gitignore):
    """
    Creates the structure of the python project and
    redirect the files and folders to the proper function.
    """
    loaded_template = load_template()
    for folder in loaded_template.keys():  # make the folders
        makedir(folder, project_name)
        for files in loaded_template[folder]:  # make the files
            makefile(files, project_name, authors,
                     choosen_license, setup, gitignore)


def load_template():
    """
    Load the default template for the python package
    """
    skeleton = os.path.join(os.path.dirname(__file__),
                            'templates', 'default_structure.json')
    try:
        with open(skeleton, 'r') as template:
            return json.load(template)
    except FileNotFoundError:
        click.echo('Template file not found. Aborted!')
        sys.exit(1)


def makedir(directory, project_name):
    """
    Make the folders tree.
    """
    # change the name of base and bin for the name of the project
    if (directory == 'base') or (directory == 'bin'):
        directory = project_name
    try:  # write the folders
        os.makedirs(directory)
        os.chdir(directory)
    except FileExistsError:
        click.echo('Folder {} alredy exists. Aborted!'.format(directory))
        sys.exit(1)


def makefile(file, project_name, authors, choosen_license, setup, gitignore):
    """
    Make the files for the project and write the content
    of AUTHORS.rst, LICENSE, .gitignore and setup.py in
    assistant mode
    """
    # change the names project.py and test_project.py
    if file == 'project.py':
        file = project_name + '.py'
    elif file == 'test_project.py':
        file = 'test_' + project_name + '.py'

    template_files = {
        'LICENSE': lambda: writefile(file, choosen_license),
        'AUTHORS.rst': lambda: writefile(file, authors),
        'setup.py': lambda: writefile(file, setup),
        '.gitignore': lambda: writefile(file, gitignore)
    }  # if the file is found, template it, else, None
    template_files.get(file, lambda: writefile(file))()


def writefile(file, content=''):
    """
    Function that write the files and go back one folder
    for the sake of the stucture.
    """
    if file == '<--':  # go back one directory
        os.chdir('..')
    else:
        # try:
        with open(file, 'w') as f:
            f.write(content)
        # except Exception as e:
        #     click.echo('Error wrinting {}. Aborted!'.format(file))
        #     sys.exit(1)


if __name__ == '__main__':
    pass
