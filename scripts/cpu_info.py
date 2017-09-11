# Provides cpu info

from collections import OrderedDict

def get_cpuinfo():
    cpuinfo = {}
    procinfo = {}

    nprocs = 0
    with open('/proc/cpuinfo') as f:
        for line in f:
            if not line.strip():
                cpuinfo['proc%s' % nprocs] = procinfo
                nprocs += 1
                procinfo = {}
            else:
                if len(line.split(':')) == 2:
                    procinfo[line.split(':')[0].strip()] = line.split(':')[1].strip()
                else:
                    procinfo[line.split(':')[0].strip()] = ''

    return cpuinfo
if __name__ == '__main__':
    print(get_cpuinfo())
