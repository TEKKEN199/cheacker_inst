import requests
import time

def cheacker():
    url = "https://www.instagram.com/accounts/web_create_ajax/attempt/"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
        "x-csrftoken": "missing",
        #"mid": "YC4O0gALAAHz26FFAmBWJzSv0A"
    }
    file = str(input("name list :"))
    list = open(file, "r")
    n = 0
    while True:
        n += 1
        username = list.readline().split("\n")[0]
        data = {
            "email": "",
            "username": username,
            "first_name": "",
            "client_id": "YC4O0gALAAHz26FFAmBWJzSv0A-4",
            "seamless_login_enabled": "1",
            "opt_into_one_tap": "false"
        }
        x = requests.post(url, headers=headers, data=data)
        time.sleep(1)
        if ('"spam":true') in x.text:
            exit()
        xx = str(x.text).split()
        xxx = str(xx[25] + " " + xx[26]).split(",")
        xxxx = xxx[0]
        if xxxx == '"username_suggestions": []':
            print("\033[0;96m" + str(n) + "[+] Found -->> " + username + "\033[0m")
            with open('accountfound.txt', 'a') as x:
                x.write(username + '\n')
        else:
            print("\033[0;91m" + str(n) + "[+] not found -->> " + username + "\033[0m")

cheacker()
