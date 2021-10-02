#! /usr/bin/env nix-shell
#! nix-shell -i python3 -p "[python3] ++ (with pkgs.python37Packages; [ requests future ws4py pytest pylint coveralls twine wheel ])"
# <<END Extended Shebang>>

import json
from pywebostv.discovery import *
from pywebostv.connection import *
from pywebostv.controls import *

with open('/home/camus/.lgtv.json') as f:
    store = json.load(f)

client = WebOSClient(store['hostname'])
client.connect()
for status in client.register(store):
    if status == WebOSClient.PROMPTED:
        print("Please accept the connect on the TV!")
    elif status == WebOSClient.REGISTERED:
        print("Registration successful!")

ctrl = InputControl(client)
system = SystemControl(client)
media = MediaControl(client)
app = ApplicationControl(client)
inp = InputControl(client)
inp.connect_input()


# vim: set filetype=python :
