from replbot.__init__ import *


clients      = []
clients_     = []

for client in clients:
    bot = replbot(
          connect_sid = client
    ).login()
