import sys, platform
import docker
from os import system
from colorama import Fore

try:
    distro = platform.node()
    if distro == 'debian' or distro == 'ubuntu':
        import apt
    elif distro == 'arch':
        import pacman
except ImportError:
    pass

'''
Instala os pacotes para o debian
'''


def arch_linux():
    import pacman
    # lista de programas
    listt = ['docker', "nmap"]
    # procura no cache
    pacman.refresh()
    banner = '''
████████╗██╗  ██╗ ██████╗        █████╗ ██████╗  ██████╗██╗  ██╗      ██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗     
╚══██╔══╝██║  ██║██╔════╝       ██╔══██╗██╔══██╗██╔════╝██║  ██║      ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║     
   ██║   ███████║██║  ███╗█████╗███████║██████╔╝██║     ███████║█████╗██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║     
   ██║   ██╔══██║██║   ██║╚════╝██╔══██║██╔══██╗██║     ██╔══██║╚════╝██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║     
   ██║   ██║  ██║╚██████╔╝      ██║  ██║██║  ██║╚██████╗██║  ██║      ██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗
   ╚═╝   ╚═╝  ╚═╝ ╚═════╝       ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝      ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝
                                                                                                                          
    '''
    print(Fore.BLUE + banner)
    # faz o check dos programas
    for i in listt:
        if i in pacman.get_installed():
            print("{colorp}{i} =>{color} already installed".format(colorp=Fore.RED, color=Fore.CYAN, i=i))
        else:
            # instala
            try:
                pacman.install(i)
            except Exception as arg:
                print("Sorry, package installation failed [{err}]".format(err=str(arg)))


'''
Instala os pacotes para o debian
'''


def deb_ubu():
    # lista de programas
    listt = ['docker.io', "nmap"]
    # procura no cache
    cache = apt.cache.Cache()
    # atualiza o cache
    cache.update()
    cache.open()
    banner = '''
████████╗██╗  ██╗ ██████╗       ██╗   ██╗██████╗ ██╗   ██╗███╗   ██╗████████╗██╗   ██╗      ██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗     
╚══██╔══╝██║  ██║██╔════╝       ██║   ██║██╔══██╗██║   ██║████╗  ██║╚══██╔══╝██║   ██║      ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║     
   ██║   ███████║██║  ███╗█████╗██║   ██║██████╔╝██║   ██║██╔██╗ ██║   ██║   ██║   ██║█████╗██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║     
   ██║   ██╔══██║██║   ██║╚════╝██║   ██║██╔══██╗██║   ██║██║╚██╗██║   ██║   ██║   ██║╚════╝██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║     
   ██║   ██║  ██║╚██████╔╝      ╚██████╔╝██████╔╝╚██████╔╝██║ ╚████║   ██║   ╚██████╔╝      ██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗
   ╚═╝   ╚═╝  ╚═╝ ╚═════╝        ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝    ╚═════╝       ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝
                                                                                                                                                  
    '''
    print(Fore.BLUE + banner)
    # faz o check dos programas
    for i in listt:
        pass
        pkg = cache[i]
        if pkg.is_installed:
            print("{colorp}{i} =>{color} already installed".format(colorp=Fore.RED, color=Fore.CYAN, i=i))
        else:
            # instala
            print(pkg.mark_install())
        try:
            cache.commit()
        except Exception as  arg:
            print("Sorry, package installation failed [{err}]".format(err=str(arg)))


'''
cria  e configura banco de dados
'''


def confpostgre():
    client = docker.from_env()
    if client.images.get("postgres") != None:
        if client.containers.get("thgdb") != None:
            print("Database already exist!")
        else:
            client.api.create_container("postgres", "POSTGRES_DB=thgdb", "POSTGRES_USER=thgdb",
                                        "POSTGRES_PASSWORD=thgdb", "port=5432")
    else:
        client.image.pull("postgres")



'''
Verifica a distro e configura o banco de dados
'''


def check():
    linux = platform.node()
    if linux == "ubuntu" or linux == "debian":
        deb_ubu()
        confpostgre()
    elif linux == "arch":
        arch_linux()
        confpostgre()
    else:
        print("Sorry, distro not found")
        pass
    print(Fore.RESET)


check()
