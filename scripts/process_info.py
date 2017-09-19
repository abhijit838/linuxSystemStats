"""Provides process details"""
import os

def get_processinfo():
    """Returns list of processes running"""
    pids = []
    for subdir in os.listdir('/proc'):
        if subdir.isdigit():
            pids.append(subdir)
    # TODO: Return process status from /proc/<pid>/status
    # Note: Use generics for lazy loading
    return pids

if __name__ == '__main__':
    print(get_processinfo())