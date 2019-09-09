import sys, distro, string, random, hashlib
import dotenv, base64
from os import system
from colorama import Fore
from pathlib import Path
from lib.thg.rootpath import ROOT_PATH

### Verifica o arquivo  .env
dotenv_path = Path(str(ROOT_PATH) + "/.env")
if dotenv_path.exists() == False:
    Path(str(ROOT_PATH) + "/.env").touch()
try:
    dotenv_file = dotenv.find_dotenv()
    dotenv.load_dotenv(dotenv_file)
except e:
    print("Error occurred loading .env file: ")
    print("Error detail: \n {}".format(e))

#### verificacao da python-pip
try:
    import pip
except ImportError:
   if distro.name() == 'Debian' or distro.name() == 'Ubuntu':
       system("apt install python3-pip")
       import pip
   elif distro.name() == 'Arch':
       system("pacman -S python-pip")
       import pip
   else:
       print("instalar manual o pip... thg finalizado")
       exit(1)

### instala o docker
try:
    import docker
except ImportError:
   if distro.name() == 'Debian' or distro.name() == 'Ubuntu':
       system("apt install docker.io")
       import docker
   elif distro.name() == 'Arch':
       system("pacman -S docker")
       import docker
   elif distro.name() == 'Fedora':
       system("dnf install python3-docker")
       import docker
   else:
       print("instalar manual o pip... thg finalizado")
       exit(1)

### instala o apt
try:
    import apt
except ImportError:
    if distro == 'Debian' or distro == 'Ubuntu':
       system("apt install python3-apt")
       import apt

### instala o pacman
try:
    import pacman
except ImportError:
   if distro.name() == 'Arch':
       system("pip install python-pacman ")
       try:
          import pacman
       except ImportError:
          print("instalacao manual do python-pacman\nlink:https://pypi.org/project/python-pacman/")

### instala o dnf
try:
    import dnf
except ImportError:
    if distro.name() == 'Fedora':
        system("pip install python3-dnf")
        import dnf

### install dev packages
try:
    from pystemd.systemd1 import Unit
except ImportError:
    if distro.name() == 'Fedora':
        system("dnf install python3-devel")
        system("dnf install systemd-libs")
        system("dnf install python3-pystemd")
        from pystemd.systemd1 import Unit

docker_service = Unit(b'docker.service')
docker_service.load()
if docker_service.ActiveState == b'inactive':
    docker_service.Start(b'docker.service')


### variavel global para usar o docker
client = docker.from_env()

### Gera o hash que será usado como senha no db
def HashGen():
    STAGING_KEY = "RANDOM"
    set_chars = string.ascii_letters + string.digits + string.punctuation
    STAGING_KEY = ''.join([ random.SystemRandom().choice( set_chars) for _ in range( 128) ])
    hash = hashlib.md5(STAGING_KEY.encode("UTF-8")).hexdigest()
    b64 = base64.b64encode(hash.encode('UTF-8'))
    b64str = b64.decode("UTF-8")
    dotenv.set_key(dotenv_file,"MONGODB_PASSWORD", b64str)
    return b64str

#configura o arquivo .env
def GenerateDotEnv():
    db_name = dotenv.set_key(dotenv_file, "MONGODB_DATABASE", "thgdb")
    db_user = dotenv.set_key(dotenv_file, "MONGODB_USERNAME", "thguser")
    db_pass = HashGen()
    return [db_name, db_user, db_pass]

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
        if pacman.is_installed(i):
            print("{colorp}{i} =>{color} already installed.".format(colorp=Fore.RED, color=Fore.CYAN, i=i))
        else:
            # instala
            try:
                print("Installing {}...".format(i))
                pacman.install(i)
                print("{} installed.".format(i))
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
        pkg = cache[i]
        if pkg.is_installed:
            print("{colorp}{i} =>{color} already installed".format(colorp=Fore.RED, color=Fore.CYAN, i=i))
        else:
            # instala
            pkg.mark_install()
        try:
            cache.commit()
        except Exception as  arg:
            print("Sorry, package installation failed [{err}]".format(err=str(arg)))

'''
Instala os pacotes para o fedora
'''

def fedora():
    # List the packages
    listt = ['docker', "nmap"]
    banner = '''
    ████████╗██╗  ██╗ ██████╗       ███████╗███████╗██████╗  ██████╗ ██████╗  █████╗       ██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗
    ╚══██╔══╝██║  ██║██╔════╝       ██╔════╝██╔════╝██╔══██╗██╔═══██╗██╔══██╗██╔══██╗      ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║
       ██║   ███████║██║  ███╗█████╗█████╗  █████╗  ██║  ██║██║   ██║██████╔╝███████║█████╗██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║
       ██║   ██╔══██║██║   ██║╚════╝██╔══╝  ██╔══╝  ██║  ██║██║   ██║██╔══██╗██╔══██║╚════╝██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║
       ██║   ██║  ██║╚██████╔╝      ██║     ███████╗██████╔╝╚██████╔╝██║  ██║██║  ██║      ██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗
       ╚═╝   ╚═╝  ╚═╝ ╚═════╝       ╚═╝     ╚══════╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝      ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝

    '''
    print(Fore.BLUE + banner)
    with dnf.Base() as base:
        RELEASEVER = dnf.rpm.detect_releasever(base.conf.installroot)
        base.conf.substitutions['releasever'] = RELEASEVER
        base.conf.best = True
        base.conf.assumeyes = True
        base.read_all_repos()
        base.fill_sack()
        query = base.sack.query()
        # faz o check dos programas
        installed = query.installed()
        available = query.available()
        for i in listt:
            pkg = available.filter(name=i).run()
            if installed.filter(name=i).run() != []:
                print("{colorp}{i} =>{color} already installed".format(colorp=Fore.RED, color=Fore.CYAN, i=i))
            else:
                # instala
                try:
                    print("{color}Installing =>{colorp} {i}".format(colorp=Fore.RED, color=Fore.CYAN, i=i))
                    base.install(pkg[0].name)
                except dnf.exceptions.MarkingError:
                    print('Feature(s) cannot be found: ' + pkg[0].name)
                except Exception as  arg:
                    print("Sorry, package installation failed [{err}]".format(err=str(arg)))
        # Check dependencies
        try:
            base.resolve()
        except:
            print('Dependencies cannot be resolved.')
        # except dnf.exceptions.DepsolveError:
        #     print('Dependencies cannot be resolved.')

        # Download the packages
        try:
            base.download_packages(base.transaction.install_set)
        except dnf.exceptions.DownloadError:
            print('Required package cannot be downloaded.')
        # Finally do the installation
        try:
            base.do_transaction()
        except Exception as  arg:
            print("Sorry, package installation failed [{err}]".format(err=str(arg)))



'''
cria  e configura banco de dados
'''


def conf_db():
    client = docker.from_env()
    try:
        print("Getting mongodb image for docker.")
        img = client.images.get("bitnami/mongodb")
    except docker.errors.ImageNotFound:
        print("Downloading image from dockerhub...")
        img = client.images.pull("bitnami/mongodb:latest")

    try:
        print("Trying to get thgdb container.")
        container = client.containers.get("thgdb-mongodb")
    except docker.errors.NotFound:
        container = None


    if img != None:
        if container != None:
            print("Database already exist!")
            remove_container(container)
            create_container().start()
            print("Database container recreated.")
        else:
            create_container().start()
            print("Database container created.")

### remove o docker container
def remove_container(container):
    client = docker.from_env()
    container.stop()
    print("Database container stopped.")
    container.remove()
    print("Database container removed.")

### cria o docker container
def create_container():
    client = docker.from_env()
    print("Creating container...")
    GenerateDotEnv()
    db_name = dotenv.get_key(dotenv_file, "MONGODB_DATABASE")
    db_user = dotenv.get_key(dotenv_file, "MONGODB_USERNAME")
    db_pass = dotenv.get_key(dotenv_file, "MONGODB_PASSWORD")
    container = client.containers.run("bitnami/mongodb", name="thgdb-mongodb", environment={
            "MONGODB_DATABASE": db_name,
            "MONGODB_USERNAME": db_user,
            "MONGODB_PASSWORD": db_pass
            }, ports={'27017/tcp': 27017}, detach=True)
    return container


'''
Verifica a distro e configura o banco de dados
'''


def check():
    linux = distro.id()
    if linux == "ubuntu" or linux == "debian":
        deb_ubu()
        conf_db()
    elif linux == "arch":
        arch_linux()
        conf_db()
    elif linux == "fedora":
        fedora()
        conf_db()
    else:
        print("Sorry, distro not found")
        pass
    print(Fore.RESET)
