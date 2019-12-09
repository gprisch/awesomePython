import sys


if __name__ == '__main__':
    arguments = sys.argv()
    if arguments == 3:
        a, b, c = (arguments)
        for i in arguments: (
            print('%s %s %s' % (a, b, c)))
    else:
        print('iLLegal number of arguments: must be 3')


