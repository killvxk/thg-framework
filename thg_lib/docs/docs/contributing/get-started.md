# Contributing

Github has a great guide for contributing to open source projects:

- [Contributing to a project](https://guides.github.com/activities/forking/)
- [Fork the repository](https://guides.github.com/activities/forking/#fork)
- [Clone your fork](https://guides.github.com/activities/forking/#clone)
- [Making and pushing changes](https://guides.github.com/activities/forking/#making-changes)
- [Making a Pull Request](https://guides.github.com/activities/forking/#making-a-pull-request)
- [Huzzah!](https://guides.github.com/activities/forking/#huzzah)

## thg Specifics
In general, we like to keep things documented. You should add documentation to any new functionality, and update it for any changed functionality. Our docstrings use the [Google Style Python Docstrings] (https://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_google.html#example-google).


Finally, it is probably a good idea to run the test suite locally before doing
the pull-request to make sure everything works, however this is not a
requirement.

Once you are ready to pull-request, you should figure out if your changes
or a bugfix in stable or beta. If it is a bugfix in
stable or beta, you should do the pull-request against the branch in question,
and otherwise your pull-request should be against the dev branch.
