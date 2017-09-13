""" Provides memory info """

def get_memoryinfo():
    """Returns system memory informations """
    with open('/proc/meminfo') as f:
        meminfo = {}
        for line in f:
            if len(line.split(':')) == 2:
                meminfo[line.split(':')[0].strip()] = line.split(':')[1].strip()
            else:
                meminfo[line.split(':')] = ''

        return meminfo

if __name__ == '__main__':
    print(get_memoryinfo())