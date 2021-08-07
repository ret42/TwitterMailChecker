#!/usr/bin/python3

#pip3 install requests

import requests
import json

mail = input("Enter the mail or a file text: ")
if mail.endswith(".txt"):
    with open(mail, "r") as f:
        for i in f:
            rs = requests.get(f"https://twitter.com/users/email_available?email={i}")
            resulti = json.loads(rs.text)
            if (resulti["taken"]) == True:
                print("\033[1;31;40m[X]\033[0m Mail already taken -", i)
            else:
                print("\033[1;32;40m[+]\033[0m Mail not taken -", i)
else:
    r = requests.get("https://twitter.com/users/email_available?email=" + mail)
    result = json.loads(r.text)
    if (result["taken"]) == True:
        print("\033[1;31;40m[X]\033[0m", mail, "- Mail already taken")
        print("\033[1;36;40m[!]\033[0m The JSON response: ", result)
    else:
        print("\033[1;32;40m[+]\033[0m", mail, "- Mail not taken")
        print("\033[1;36;40m[!]\033[0m The JSON response: ", result)
