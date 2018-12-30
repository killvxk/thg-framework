from os import system
import os
import socket
import base64
import pip
import shutil
import distro
from thgconsole.core.CoreUtils.printer import print_success,print_info
class THG_INSTALL():
    def __init__(self):
        print("start...")
    def install():
        exitfile = "~/"
        infile = system("cp -rv extra_thg_package {}".format(exitfile))
        print_success(infile)
        with open("requirements.txt") as fl:
            check_os = distro.linux_distribution()[0]
            if check_os == "Ubuntu":
                os.system("apt install python3-pip")
                for libs in fl.readlines():
                    print_success(libs)
                    os.system("pip3 install {}".format(libs))
            elif check_os == "Debian":
                os.system("apt install python3-pip")
                for libs in fl.readlines():
                    print_success(libs)
                    os.system("pip3 install {}".format(libs))
                print("fish instalation...[{}]".format(check_os))
            elif check_os == "Manjaro Linux":
                os.system("pacman -Syy python3-pip")
                for libs in fl.readlines():
                    print_success(libs)
                    os.system("pip3 install {}".format(libs))
                print("fish instalation...[{}]".format(check_os))

            else:
                for libs in fl.readlines():
                    print(libs)
                    os.system("pip3 install {}".format(libs))


THG_INSTALL.install()