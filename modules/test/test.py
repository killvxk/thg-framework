# 请求redis需要socket 故引入socket
import socket
from lib.BaseMode.BaseMods import BaseExploit

class Exploit(BaseExploit):
    def __init__(self):
        super(Exploit, self).__init__()
        self.update_info({
            "name": "redis unauthorized",
            "description": "redis unauthorized",
            "author": ["unknown"],
            "references": [
                "https://www.freebuf.com/column/158065.html",
            ],
            "disclosure_date": "2019-02-28",
            "service_name": "redis",
            "service_version": "*",
        })
        # 因为redis只需要提供ip和端口，所以这里注册tcp的目标。
        self.register_tcp_target(port_value=6379)

    def check(self):
        # 这三个参数都是self.register_tcp_target方法注册的，这里可以直接调用
        host = self.options.get_option("HOST")
        port = int(self.options.get_option("PORT"))
        timeout = int(self.options.get_option("TIMEOUT"))

        # 执行测试的整个过程最好放进try里面，然后在except里面捕获错误直接调用self.results.failure打印出报错。
        try:
            socket.setdefaulttimeout(timeout)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            s.send(bytes("INFO\r\n", encoding="utf-8"))
            result = s.recv(1024)
            if bytes("redis_version", encoding="utf-8") in result:
                # 存在漏洞 调用该方法  data可传入一个字典，目前没有什么用，也可以不传。
                self.results.success(
                    data={
                        "host": host,
                        "port": port,
                    },
                    # 由于可能会执行多个目标，所以结果里面最好写上目标和端口，方便辨认。
                    message="Host {host}:{port} exists redis unauthorized vulnerability".format(host=host, port=port)
                )
            else:
                # 不存在漏洞 调用self.results.failure方法传入错误信息。
                self.results.failure(
                    error_message="Host {host}:{port} does not exists redis unauthorized vulnerability".format(
                        host=host,
                        port=port
                    )
                )
        except Exception as e:
            # 执行错误，使用self.results.failure传入错误信息。
            self.results.failure(error_message="Host {host}:{port}: {error}".format(host=host, port=port, error=e))
        return self.results

    def exploit(self):
        return self.check()