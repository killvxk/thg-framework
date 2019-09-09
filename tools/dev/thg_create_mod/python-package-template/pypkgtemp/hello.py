class HelloWorld:
    """ HelloWorld class will tell you hello!

    """
    def __init__(self, firstname, lastname):
        """ initialize HelloWorld class

        Args:
           firstname (str): first name of user
           lastname (str): last name of user
        """
        self.firstname = firstname
        self.lastname = lastname

    @property
    def hello(self):
        """ say hello to user

        a longer message about what this function does

        Returns:
            str: special hello message to user
        """
        return f'Hello {self.firstname} {self.lastname}'

    @staticmethod
    def helloworld(name):
        """string with special hello message to name

        Args:
            name (str): the person to say hello to

        Returns:
            str: special hello world message
        """
        return f'Hello World {name}!'


def fizzbuzz(n):
    """A super advanced fizzbuzz function

    Write a program that prints the numbers from 1 to 100. But for
    multiples of three print “Fizz” instead of the number and for the
    multiples of five print “Buzz”. For numbers which are multiples of
    both three and five print “FizzBuzz” Prints out fizz and buzz

    Args:
        n (int): number for fizzbuzz to count to

    Returns:
       None: prints to stdout fizzbuzz
    """
    def _fizzbuzz(i):
        if i % 3 == 0 and i % 5 == 0:
            return 'FizzBuzz'
        elif i % 3 == 0:
            return 'Fizz'
        elif i % 5 == 0:
            return 'Buzz'
        else:
            return str(i)
    print("\n".join(_fizzbuzz(i+1) for i in range(n)))
