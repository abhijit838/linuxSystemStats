# provides system/platform info
import platform as pf

def get_system_info():
    info = dict()
    info['sys_type'] = pf.system()
    info['node_name'] = pf.node()
    info['release'] = pf.release()
    info['version'] = pf.version()
    info['machine'] = pf.machine()
    info['processro_type'] = pf.processor()
    info['dist'] = pf.linux_distribution()
    info['architecture'] = pf.architecture()
    return info

if __name__ == '__main__':
    print(get_system_info())