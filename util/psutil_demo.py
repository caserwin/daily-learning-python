import os
pid = os.getpid()
print(pid)


import psutil
print(psutil.pids())