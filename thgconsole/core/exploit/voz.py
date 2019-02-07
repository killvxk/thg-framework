
# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os
import subprocess
import sqlite3
class thgvoz():
    def __init__(self):
        pass
    def load():
        conexoes = sqlite3.connect("thgconsole/thg.db")
        cursor = conexoes.cursor()
        res = conexoes.execute("SELECT name FROM sqlite_master WHERE type='table';")
        conexoes = sqlite3.connect("thgconsole/thg.db")
        cursor = conexoes.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        res = conexoes.execute("SELECT name FROM sqlite_master WHERE type='table';")
        conexoes = sqlite3.connect("thgconsole/thg.db")
        cursor = conexoes.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        total = len(cursor.fetchall())
        # The text that you want to convert to audio
        text = "wellcome darkcode"
        text2 = "you are root!"
        text3 = 'now! start the hacker group aplication!'
        text4 = "initiating loading of the base modules [ok]"
        text5 = "starting base system [ok]"
        text51 = "{} tables created ".format(total)
        text6 = "start security mod"
        text7 = "start iptables, if you want to change the default iptables settings, edit /etc/kull/config file "
        text8 = "collecting system information [ok]"
        text9 = "let's go to happy hacking and hacking the all things"
        total = text+text2+text3+text4+text5+text51+text6+text7+text8+text9
        # Language in which you want to convert
        language = 'en'

        # Passing the text and language to the engine,
        # here we have marked slow=False. Which tells
        # the module that the converted audio should
        # have a high speed
        myobj = gTTS(text=total, lang=language, slow=False)

        # Saving the converted audio in a mp3 file named
        # welcome
        myobj.save("welcome")
        FNULL = open(os.devnull, 'w')
        retcode = subprocess.call(['mpg123','welcome'], stdout=FNULL, stderr=subprocess.STDOUT)


