import numpy


def fct_1():
    return 10


def fct_2():
    pass


def main():
    a = numpy.array([1, 2, 3])
    print(a ** 5)
    fct_1()
    fct_2()


if __name__ == "__main__":
    main()
