from os import system
import os
import socket
import base64
import pip
import shutil
import distro
#from thgconsole.core.CoreUtils.printer import print_success,print_info
class THG_INSTALL():
    def __init__(self,check_os):
        print("start...")
    def install(self):
        exitfile = "~/.extra_thg_package"
        files = system("cp -rv extra_thg_package {}".format(exitfile))
        os.system("apt install python3-pip && pip3 install -r requirements.txt ")

a = THG_INSTALL(check_os=distro.linux_distribution()[0]).install()



