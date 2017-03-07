
import time
import socket
import psutil


def status():

    data = {}
    
    data['user'] = []
    for u in psutil.users():
        user = {'name':u.name,
                'since':time.strftime("%d/%h/%Y - %H:%M", time.localtime(u.started))
                }
        data['user'].append(user)
    
    data['cpu_count'] = psutil.cpu_count()
    data['cpu_percent'] = psutil.cpu_percent(interval=1)
    data['cpu_percent_individual'] = psutil.cpu_percent(interval=1, percpu=True)
    
    data['hostname'] = socket.gethostname()
    data['ipaddress'] = socket.gethostbyname(socket.gethostname())

    mem = psutil.virtual_memory()
    data['memory_total'] = mem.total / 1024 / 1024
    data['memory_free'] = mem.free / 1024 / 1024

    return data


if __name__ == '__main__':
    from pprint import pprint as ppp
    ppp(status())

