#!/usr/bin/env python
import sys

if __name__ == "__main__":

    names = {}
    # sys.stdin is a file object. All the same functions that
    # can be applied to a file object can be applied to sys.stdin.
    #sys.stdout.write("output---->")
    
    for name in sys.stdin.readlines():
            # Each line will have a newline on the end or empty '' input
            # that should be removed. 
            name = name.strip()            
            if name == '': continue 
                       
            if name in names:
                    names[name] += 1
            else:
                    names[name] = 1

    # Iterating over the dictionary,
    # print name followed by a space followed by the
    # number of times it appeared.
    #print(names)
    for name, count in names.items():
            sys.stdout.write("%d\t%s\n" % (count, name))
