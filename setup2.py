from os import system
import os
import socket
import base64
import pip
import shutil
import distro
from thgconsole.core.CoreUtils.printer import print_success,print_info
class THG_INSTALL():
    def __init__(self,check_os):
        print("start...")
        self.check_os =""
    def install(self):
        exitfile = "~/"
        infile = system("cp -rv extra_thg_package {}".format(exitfile))
        print_success(infile)
        with open("requirements.txt") as fl:
            if self.check_os == "Ubuntu":
                os.system("apt install python3-pip vagrant")
                for libs in fl.readlines():
                    print_success(libs)
                    os.system("pip3 install {}".format(libs))
            elif self.check_os == "Debian":
                os.system("apt install python3-pip vagrant ")
                for libs in fl.readlines():
                    print_success(libs)
                    os.system("pip3 install {}".format(libs))
                print("fish instalation...[{}]".format(self.check_os))
            elif self.check_os == "Manjaro Linux":
                os.system("pacman -Syy python3-pip vagrant")
                for libs in fl.readlines():
                    print_success(libs)
                    os.system("pip3 install {}".format(libs))
                print("fish instalation...[{}]".format(self.check_os))

            else:
                for libs in fl.readlines():
                    print(libs)
                    os.system("pip3 install {}".format(libs))


a = THG_INSTALL(check_os=distro.linux_distribution()[0]).install()



from abc import ABCMeta,abstractmethod
