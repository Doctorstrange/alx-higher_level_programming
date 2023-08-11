#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = 0
    targ = (len(sys.argv))
    for ac in range(targ - 1):
        count += int(sys.argv[ac + 1])
    print("{}".format(count))
