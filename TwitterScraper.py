from seleniumwire import webdriver
import requests
import threading
import json
import random
import time
import ctypes
import re
import sys 
import os





print("""



         [-] TwitterScraper [-]
        [ By : Remax Alghamdi . ]
    ======================================= 
    [+] Twitter : @iR3max .               |
    [+] Instagram: @OQO .                 |
    [+] Discord : Remax#6666 .            |
    [+] Github : Fah4d .                  |
    =======================================



    """)




print("Please wait to bring x-guest-token .")
print("")



Remax = "The best programmer in the world"

Counter = 0 

def gettoken():

        ##  Get the URL
        driver = webdriver.Chrome()
        driver.get("https://twitter.com")

        ##  Print request headers
        for request in driver.requests:
            x = request.headers # <----------- Request headers
            xx = re.findall(r"(x-guest-token: [\d\w\.]+)", str(x))
            for xxx in xx:
                if xxx.find("guest") >= 0:
                    GuestToken = str(xxx.replace("x-guest-token: ", ""))
                    print("x-guest-token: "+GuestToken)
                    print("")
                    driver.quit()
                    Scrape(GuestToken)


def Scrape(GuestToken):


    print("")

    NmofThrads = int(input("Threads : "))
    limit = int(input("How many users: "))

    RandomC = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


    def Goo():

        global Counter
        while True:

            try:

                url = "https://twitter.com/i/api/2/search/adaptive.json"
                params = {

                    "q":random.choice(RandomC),
                    "tweet_search_mode":"live",
                    "count":"100"

                }
                headers = {

                    "Host": "twitter.com",
                    "x-csrf-token": "missing",
                    "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
                    "x-guest-token": GuestToken

                }
                r = requests.get(url,params=params, headers=headers)
                mew = json.loads(r.text)
                mewloadwithinsert = json.dumps(mew, indent=4, sort_keys=True)
                numberofusers = (json.loads(mewloadwithinsert)["globalObjects"]["users"])
                userslist = list(numberofusers.keys())
                for user in userslist:
                    getid = (json.loads(mewloadwithinsert)["globalObjects"]["users"][user])
                    g = json.dumps(getid)
                    y = json.loads(g)
                    idd = (y["id"])
                    username = (y["screen_name"])
                    name = (y["name"]).replace("\n", "")
                    description = (y["description"]).replace("\n", "")
                    following = (y["friends_count"])
                    followers = (y["followers_count"])
                    tweets = (y["statuses_count"])
                    media = (y["media_count"])
                    favourites = (y["favourites_count"])
                    location = (y["location"]).replace("\n", "")
                    created_at = (y["created_at"])
                    verified = (y["verified"])
                    profileimage = (y["default_profile_image"])
                    profilebanner = (y["default_profile"])
                    Counter +=1
                    #print("[+]Counter:{}[+]".format(Counter),end="\r")
                    ctypes.windll.kernel32.SetConsoleTitleW(f"[+]Counter: {Counter}[+]") ## Remove this line if you use OS other than Windows
                    print(f"username : {username}")
                    with open("FullData.txt","a", encoding="utf-8") as wr:
                        wr.write(f"{idd},{username},{name},{description},{following},{followers},{tweets},{media},{favourites},{location},{created_at},{verified},{profileimage},{profilebanner}\n")
                    with open("users.txt","a") as wr:
                        wr.write(username+"\n")
                    if Counter >= limit:
                        print(f"Done! , Users = {Counter} !")
                        os._exit(1)
            except Exception as e:
                print(e)



    threads = []


    for x in range(NmofThrads):
        t = threading.Thread(target=Goo)
        t.start()
        threads.append(t)



if Remax == "The best programmer in the world":
    gettoken()
else:
    print("Remax is the best programmer in the world")
