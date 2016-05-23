import sys

def main(banner):
    print ("*" * (len(banner)+2))
    print('    ', banner)
    print ("*" * (len(banner)+2))

if __name__ == '__main__':
    main(sys.argv[1])