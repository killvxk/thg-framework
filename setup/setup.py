import distro,sys
from os import system
from colorama import Fore
try:
    if distro.linux_distribution()[0] == 'debian' or 'ubuntu':
        import apt
    elif distro.linux_distribution()[0] == 'Arch Linux':
        import pacman
except ImportError:
    pass
def arch_linux():
    #lista de programas
    listt = ['docker.io', "nmap"]
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
    print(Fore.BLUE+banner)
    #faz o check dos programas
    for i in listt:
        if i in pacman.get_installed():
            print("{colorp}{i} =>{color} already installed".format(colorp=Fore.RED, color=Fore.CYAN, i=i))
        else:
            #instala
            pacman.install(i)
        #try:
        #except Exception as arg:
        #   print("Sorry, package installation failed [{err}]".format(err=str(arg)))

def deb_ubu():
    #lista de programas
    listt= ['docker.io',"nmap"]
    #procura no cache
    cache = apt.cache.Cache()
    #atualiza o cache
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
    print(Fore.BLUE+banner)
    #faz o check dos programas
    for i in listt:
        pkg = cache[i]
        if pkg.is_installed:
            print("{colorp}{i} =>{color} already installed".format(colorp=Fore.RED,color=Fore.CYAN,i=i))
        else:
            #instala
            print(pkg.mark_install())
        try:
            cache.commit()
        except Exception as  arg:
            print("Sorry, package installation failed [{err}]".format(err=str(arg)))

def confpostgre():
        system("""docker run --name thgdb \
    -e POSTGRES_PASSWORD=thgdb \
    -e POSTGRES_USER=thgdb \
    -e POSTGRES_DB=thgdb \
    -p 5432:5432 \
    -d postgres""")
def check():
    linux = distro.linux_distribution()[0]
    if linux == "ubuntu" or "debian":
        deb_ubu()
        confpostgre()
    elif linux == "Arch Linux":
        arch_linux()
        confpostgre()
check()