import thgc.skeleton
import thgc.template_config
import string
import thgc.licenses


def test_load_template():
    test_load = thgc.skeleton.load_template()
    assert isinstance(test_load, dict)


def test_templates():
    test_author = thgc.template_config.authors_template(
        'project', 'carlos', 'carlos@gmail.com')
    test_load = thgc.template_config.load_template('template_authors.txt')
    test_setup = thgc.template_config.setup_template(
        setup_name='setup_name',
        setup_version='setup_version',
        setup_description='setup_description',
        setup_author='setup_author',
        setup_author_email='setup_author_email',
        setup_url='setup_url')

    assert isinstance(test_author, str)
    assert isinstance(test_load, string.Template)
    assert isinstance(test_setup, str)


def test_licenses():
    test_index = thgc.licenses.load_index_json()
    assert isinstance(test_index, dict)
