#! /home/mf/anaconda3/envs/venv-python-3-7-5/bin/python

import fileinput

if __name__ == '__main__':
    for line in fileinput.input():
        if fileinput.isfirstline():
            print("<Start of file {0}>".format(fileinput.filename()))
        print(line, sep=' ')
