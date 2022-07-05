import os
import json

def install_sumo(i):
    _mac_version = ''
    cmd = ' ssh ubuntu@' + str(i) + ' uptime'
    op = str(os.popen(cmd).read())
    print(op)

# ip = '10.160.64.159'
# install_sumo(ip);
