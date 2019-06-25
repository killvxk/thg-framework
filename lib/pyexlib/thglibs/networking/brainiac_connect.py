import socket
from thglibs.auxiliares.debug.debug import Debug


class Connect:
    def __init__(self, host, port, timeout):
        self.host = host
        self.port = port
        self.timeout = timeout

    def connect_TCP(host, port, timeout):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)
            s.connect((host, port))
            hp = str(host) + ":" + str(port)
            Debug.CRITICAL(f"conectado TCP => [{hp}]")
        except socket.error:
            hp = str(host) + ":" + str(port)
            Debug.AVISO(f"falha ao conectar => [{hp}]")

    def connect_UDP(host, port, timeout):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.settimeout(timeout)
            s.connect((host, port))
            hp = str(host) + ":" + str(port)
            Debug.CRITICAL(f"conectado UDP => [{hp}]")
        except socket.error:
            hp = str(host) + ":" + str(port)
            Debug.AVISO(f"falha ao conectar => [{hp}]")

    def connect_recv(host, port, timeout):

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            s.settimeout(5)
            try:
                print("[+] Connected to bind shell!\n")
                while 1:
                    cmd = input("(py-shell) $ ");
                    s.send(b'cmd');
                    result = s.recv(1024).strip();
                    if not len(result):
                        print("[+] Empty response. Dead shell / exited?")
                        s.close();
                        break;
                    print(result);

            except KeyboardInterrupt:
                print("\n[+] ^C Received, closing connection")
                s.close();
            except EOFError:
                print("\n[+] ^D Received, closing connection")
                s.close();

        except socket.error:
            print("[+] Unable to connect to bind shell.")


Connect.connect_recv("localhost", 90, 10)
