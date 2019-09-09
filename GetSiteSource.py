"""
Our Channel: https://t.me/APPSHACKING
Me : Https://t.me/Mr_Meta
"""
#-----------------------------------------






from requests import get as reqg
from time import sleep
from fake_useragent import UserAgent
from os import startfile
ua = UserAgent()
headers = {"User-agent":f'{ua.random}'}
BAN="""
Our Channel: https://t.me/APPSHACKING
Me : Https://t.me/Mr_Meta
"""
print(BAN)



def main():
    while True:
        site = str(input("Please Enter Site Url (ex: https://google.com) >>"))
        if site.startswith("http"):
            print(f"[+]Sending Request To Site {site}")
            try:
                res = reqg(site,headers=headers)
                print("[+]Request Send To {site} Successfuly!")
                sleep(2)
                with open("index.html","w",encoding='utf8') as file:
                    file.write(f"<!--{BAN}-->")
                    file.write(res.text)
                    file.write(f"<!--{BAN}-->")
                    file.close()
                print(f"Source Site {site} Extracet Successful")
                sleep(1)
                print("Opening File....")
                startfile("index.html")
                print(BAN)
                sleep(5)
                break

            except Exception as exx:
                print(f"[-]{exx}")
                sleep(3)
                continue
        else:
            print()
            print("Please Enter Http Or Https In Start (ex:https://google.com)")
            sleep(3)
            print()
            continue



main()




#-------------------------------
"""
Our Channel: https://t.me/APPSHACKING
Me : Https://t.me/Mr_Meta
"""