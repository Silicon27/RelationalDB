import argparse
import ctypes
import os
from helper.lightmodehelper import lightmode


# command to make shared library from c code and store it in src/clibs/sharedlibs
# gcc -shared -o src/clibs/sharedlibs/libexample.so src/clibs/example.c

sortfunc = ctypes.CDLL(os.path.join(os.path.dirname(__file__), '../clibs/sharedlibs/sort.so'))

sortfunc.sort.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]

def main():
    parser = argparse.ArgumentParser(description='Sort some integers.')

    parser.add_argument('integers', metavar='N', type=int, nargs='*',
                        help='an integer to sort')
    parser.add_argument('--light', '-l', type=str, 
                        help='light mode', nargs='+')

    args = parser.parse_args()
    if args.integers:
        print(args.integers)
        array = (ctypes.c_int * len(args.integers))(*args.integers)
        sortfunc.sort(array, len(args.integers))
        print(list(array))
    
    elif args.light and len(args.light) > 0:
        lightmode(args.light)

if __name__ == '__main__':
    main()
