""" Provides block device info"""
import re
import glob
import os

# Add any other device pattern to read from
dev_pattern = ['sd.*','mmcblk*']

def size(device):
    nr_sectors = open(device+'/size').read().rstrip('\n')
    sect_size = open(device+'/queue/hw_sector_size').read().rstrip('\n')

    # The sect_size is in bytes, so we convert it to GiB and then send it back
    return (float(nr_sectors)*float(sect_size))/(1024.0*1024.0*1024.0)


def get_blockdeviceinfo():
    """ Returns basic block device info like:
    Size of the block device
    """
    info = {}
    devices = []
    for device in glob.glob('/sys/block/*'):
        for pattern in dev_pattern:
            if re.compile(pattern).match(os.path.basename(device)):
                info['device'] = device
                info['size'] = size(device)
        list.append(info)
    return devices

if __name__ == '__main__':
    print(get_blockdeviceinfo())