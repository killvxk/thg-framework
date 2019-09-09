thg_pack
========

A simple and quick command line tool to create python packages.


Install
-------

``$ pip install thgc-pack``

Usage
-----

The config command
~~~~~~~~~~~~~~~~~~

``$ thgc config``

Use it to fill common fields once (if executed twice it
will overwrite the previous configuration).

Create a default python project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``$ thgc create <project-name>``

Create a project using one of the available templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``$ thgc create <project-name> -t <template>``

*-t* is the short for *--template*.

Available templates:

-  *flask*
-  *django*
-  *pymin* (minimal python project)

To use your own template you need to store it in a *.json* file in your current
directory, e.g.:

``my_template.json``

And use it by:

``$ thgc create my_project -t my_template``

A step by step setup for new projects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``$ thgc assistant``

This command help you fill:

-  ``setup.py``
-  ``AUTHORS.rst``
-  ``LICENSE``
-  ``.gitignore`` with rules for *Linux*, *MacOs*,
   *Winthgcws*, *Python*, *Visual Studio*, *VS Code*, *Sublime Text* and
   *Pycharm* (made with https://www.gitignore.io/).

Default Folder Structure and Templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the folder structure created when using
``thgc create <my_project>`` and ``thgc assistant``.

::

    project_folder
    ├── project
    │   ├── __init__.py
    │   └── project.py
    ├── thgccs
    │   └── index.rst
    ├── tests
    │   ├── __init__.py
    │   └── project_test.py
    ├── .gitignore
    ├── LICENSE
    ├── README.rst
    ├── AUTHORS.rst
    ├── setup.py
    ├── requirements.txt
    └── test-requirements.txt

-  The template system use a ``.json`` file in wich the keys are
   folders and the values are files.
-  Every time a folder is created, the program will automatically enter
   it. If you need to exit that folder so the next one is placed in the
   same directory, place a ``<--`` in the files (values) as many times needed.
-  Folders (keys) ``base`` and ``bin`` are replaced with the project name.
-  ``project.py`` is replaced with the project name (e.g.
   ``my_project.py``).
-  In ``test_projet.py``, ``project`` is replaced with the project name
   (e.g. ``test_my_project.py``)

This is the template for the default folder structure:

::

    {
        "base": [
            "LICENSE",
            "setup.py",
            "README.rst",
            "AUTHORS.rst",
            ".gitignore",
            "requirements.txt",
            "test-requirements.txt",
            "MANIFEST.in"
        ],
        "bin": [
            "project.py",
            "__init__.py",
            "<--"
        ],
        "thgccs": [
            "index.rst",
            "<--"
        ],
        "tests": [
            "__init__.py",
            "test_project.py",
            "<--"
        ]
    }

TOthgcs
~~~~~

-  Implement ``--template`` for  the ``assistant`` command (75%).
-  Add github username to the ``config`` command for the project
   url.
-  Generate the thgccumentation (sphinx).
