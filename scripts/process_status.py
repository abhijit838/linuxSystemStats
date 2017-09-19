"""Provides process status"""

def get_process_status(pid):
    """Returns process status/details for a perticular pid"""
    process_status = {}
    with open('/proc/' + str(pid) + '/status') as f:
        for line in f:
            line = line.split(':')
            process_status[line[0].strip()] = line[1].strip()

    return process_status

if __name__ == '__main__':
    print(get_process_status(1))