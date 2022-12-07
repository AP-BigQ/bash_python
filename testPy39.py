#!/usr/bin/env python3
import sys

if __name__ == "__main__":

    sys.stdout.write("output---->\n")
    
    for name in sys.stdin.readlines():
        print(name)

