from pypkgtemp.hello import HelloWorld, fizzbuzz


def test_example():
    assert 1 == 1


def test_helloworld_hello():
    helloworld = HelloWorld('Chris', 'Ostrouchov')
    assert helloworld.hello == 'Hello Chris Ostrouchov'


def test_helloworld_helloworld():
    assert HelloWorld.helloworld('Chris') == 'Hello World Chris!'


def test_fizzbuzz(capsys):
    fizzbuzz(9)
    captured = capsys.readouterr()
    assert captured.out == '1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\n'
