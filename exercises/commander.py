__author__ = 'PWXG8293'

from subprocess import PIPE, Popen

# This method takes 3 arguments builds an UNIX POSIX  command  ann execute it
# The result of the execution is returned
def executeCmd(command, args={}, greplist={}):
    print args, greplist
    cmd = command
    if len(args):
        i = 0
        while i < len(args):
            cmd = cmd + ' ' + str(args[i])
            i = i + 1
    if len(greplist):
        i = 0
        while i < len(greplist):
            cmd = cmd + ' |grep ' + str(greplist[i])
            i = i + 1
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    outdata, errdata = p.communicate()
    if len(outdata) <= 0:
        raise RuntimeError(
            'unable to execute the command[ %s ] for args= %s and grelist= %s: %s' % (cmd, args, greplist, errdata))
    return outdata
