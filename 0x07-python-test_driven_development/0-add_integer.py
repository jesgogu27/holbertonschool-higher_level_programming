#!/usr/bin/python3
def add_integer(a, b=98):
    """
        add_integer plus two number integer

        Arguments:
            a {int} -- integer one
            b {int} -- integer two

        Returns:
            int -- plus of integers

        Raises:
            TypeError: if any arguments is not a integer
    """
    try:
        x = int(a)
        y = int(b)
        return x + y
    except ValueError:
        if a is not int:
            raise TypeError("a must be an integer")

    except Exception as e:
        if b is not int:
            raise TypeError("b must be an integer")
