from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser()
    # add arguments
    parser.add_argument('indent', type=int, help='indent for report')
    parser.add_argument('input_file', help='read data from this file')
    parser.add_argument('-f', '--file', dest='filename',
                        help='write report to FILE', metavar='FILE')
    parser.add_argument('-x', '--xray', help='specify xray strength factor')
    parser.add_argument('-q', '--quiet', action='store_false', dest='verbose', default=True,
                        help='do not print status messages to stdout')
    args = parser.parse_args()

    print('arguments:', args)
