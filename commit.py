from os import system
men = input("mensagem do commit =>")
a = system("git add -A & git commit -am {}".format(men))
pussh = input("push ? =>")
if pussh == "":
	system("git push origin master")
else:
	system("git push origin {}".format(pussh))
