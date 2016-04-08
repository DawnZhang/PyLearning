#!/usr/bin/python -tt
"""
Generate uniform python file for coding
"""

import os, sys
import commands


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print 'usage: ./pyinit.py -filename'
        sys.exit(1)
    else:
        filename = args[0]

    f = open(filename, 'wb')
    f.write("#!/usr/bin/python -tt\n")
    f.write("\n"*1)
    f.write("import os, sys\n")
    f.write("import urllib\n")
    f.write("import re\n")
    f.write("\n"*1)
    f.write("filename = '%s'\n" % filename)
    f.write("url = ''\n")
    f.write("\n"*2)
    f.write("def main():\n")
    with open('saveurl', 'r') as saveurl:
        f.write(saveurl.read())
    f.write("\n"*2)
    f.write("if __name__ == '__main__':\n")
    f.write("    main()")
    f.close()
    cmd = 'chmod +x ' + filename
    (status, output) = commands.getstatusoutput(cmd)
    if status:
        sys.stderr.write(output)
        sys.exit(1)


if __name__ == '__main__':
    main()
