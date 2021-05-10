import os, platform

### Modul os
uname = os.uname()
print("<<< OS module >>>")
print("system name:", uname.sysname)
print("OS release:", uname.release)
print("version:", uname.version)
print("architecture 32/64bit/ARM atd:", uname.machine)
print("network name:", uname.nodename)

print("username:", os.getlogin())

### Modul platform je doporucovany zpusob, jak zjistovat info o systemu
print("\n<<< PLATFORM module >>>")
print("architecture:", platform.architecture())
print("platform:", platform.machine())
print("processor:", platform.processor())
print("python version:", platform.python_version())
print("uname:", platform.uname())
