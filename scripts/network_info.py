"""Provides network informations"""

def get_networkinfo():
    """Returns receivd and transmitted data amount"""
    with open('/proc/net/dev') as f:
        net_dump = f.readlines()

    device_data = {}
    for line in net_dump[2:]:
        line = line.split(':')
        if line[0].strip() != 'lo':
            device_data[line[0].strip()] = {
                'rx': '{0} {1}'.format(float(line[1].split()[0])/(1024.0*1024.0), 'MiB'),
                'tx': '{0} {1}'.format(float(line[1].split()[8])/(1024.0*1024.0), 'MiB')
            }
    
    return device_data

if __name__ == '__main__':
    print(get_networkinfo())