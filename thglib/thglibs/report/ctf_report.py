from thglibs.auxiliares.debug.debug import Debug
import os
import datetime

today = datetime.date.today()


class CTF_REPORT:
    def __init__(self, team, nome, desafio, pasta_name, file_name):
        self.team = team
        self.nome = nome
        self.desafio = desafio
        self.pasta_name = pasta_name
        self.file_name = file_name

    def report(CTF_NOME, CTF_team, CTF_USER, CTF_challenges, CTF_challenges_PASTA, file_name, evento_nome, flag_pontos):
        Debug.CRITICAL("[+]criando relatorio")
        Debug.AVISO(f"CTF_NOME: {CTF_NOME} ")
        Debug.AVISO(f"CTF_TIME: {CTF_team} ")
        Debug.AVISO(f"CTF_USER: {CTF_USER} ")
        Debug.AVISO(f"CTF_TIPO: {CTF_challenges} ")
        Debug.AVISO(f"CTF_PASTA: {CTF_challenges_PASTA} ")
        Debug.AVISO(f"EVENTO_NOME: {evento_nome} ")
        Debug.AVISO(f"FLAG_PONTOS {flag_pontos} ")
        try:  # Ele vai tentar criar a pasta brainiac_ctf_report, pasta CTF_challenges_PASTA e o nome do arquivo
            os.mkdir("../brainiac_ctf_report")  # Cria pasta brainiac_ctf_report
            Debug.CRITICAL("[+] criando pasta => [brainiac_ctf_report]")
            os.mkdir(CTF_challenges_PASTA)  # Cria pasta CTF_challenges_PASTA
            os.chdir(CTF_challenges_PASTA)  # Entra na pasta CTF_challenges_PASTA
            Debug.CRITICAL(f"[+] CTF_challenges  => [{CTF_challenges_PASTA}]")
            Debug.CRITICAL(f"[+] file_challenges  => [{file_name}]")

        except FileExistsError:  # Se a pasta brainiac_ctf_report existir ele entra na pasta
            os.chdir("../brainiac_ctf_report")  # Entra na pasta brainiac_ctf_report
            try:  # Tenta criar a pasta CTF_challenges_PASTA
                os.mkdir(CTF_challenges_PASTA)  # Cria CTF_challenges_PASTA
                os.chdir(CTF_challenges_PASTA)  # Entra CTF_challenges_PASTA
                Debug.CRITICAL(f"[+] CTF_challenges  => [{CTF_challenges_PASTA}]")
                Debug.CRITICAL(f"[+] file_challenges  => [{file_name}]")

            except FileExistsError:  # Se a pasta CTF_challenges_PASTA existir
                os.chdir(CTF_challenges_PASTA)  # Entra na pasta CTF_challenges_PASTA
                Debug.CRITICAL(f"[+] CTF_challenges  => [{CTF_challenges_PASTA}]")
                Debug.CRITICAL(f"[+] file_challenges  => [{file_name}]")

        with open(file_name, "w") as fl:  ###Escreve logs no file_name
            fl.write("#" * 35)
            fl.write("\n" + "#" * 10 + "report" + "#" * 10)
            fl.write("\n" + "#" * 5 + "brainiac_report_info_ctf" + "#" * 6)
            fl.write("\n" + "#" * 35)
            fl.write("\n" + f"CTF_EVENTO: {evento_nome} ")
            fl.write("\n" + f"CTF_DATE: {today}")

            fl.write("\n" + f"CTF_PONTOS: {flag_pontos} ")
            fl.write("\n" + f"CTF_NOME: {CTF_NOME} ")
            fl.write("\n" + f"CTF_TIME: {CTF_team} ")
            fl.write("\n" + f"CTF_USER: {CTF_USER} ")
            fl.write("\n" + f"CTF_TIPO: {CTF_challenges} ")
            fl.write("\n" + f"CTF_PASTA: {CTF_challenges_PASTA} ")
            fl.close()
            os.system("nano " + file_name)
