import requests
import time
import random
import argparse
import sys

def banner():
        print("")
        print(" ###############################################################")
        print(" #                                                             #")
        print(" #    ______               ____  _ _            _              #")
        print(" #   |  ____|             |  _ \(_) |          (_)             #")
        print(" #   | |__ _ __ ___  ___  | |_) |_| |_ ___ ___  _ _ __         #")
        print(" #   |  __| '__/ _ \/ _ \ |  _ <| | __/ __/ _ \| | '_ \\        #")
        print(" #   | |  | | |  __/  __/ | |_) | | || (_| (_) | | | | |       #")
        print(" #   |_|  |_|  \___|\___| |____/|_|\__\___\___/|_|_| |_|       #")
        print(" #                                                             #")
        print(" #   By: Milad Khoshdel                                        #")
        print(" #   Blog: https://blog.regux.com                              #")
        print(" #   Email: miladkhoshdel@gmail.com                            #")
        print(" #                                                             #")
        print(" ###############################################################")
        print("")


try:
        banner()

        parser = argparse.ArgumentParser()
        parser.add_argument("-c", "--cookie")
        parser.add_argument("-s", "--seed")
        parser.add_argument("-t", "--token")
        args = parser.parse_args()

        if not args.cookie or not args.seed or not args.token:
                print(" You must enter your cookie and client seed for continue.")
                print(" Exiting ...")
                print("")
                sys.exit(0)

        cookie = args.cookie
        seed = args.seed
        token = args.token

        pattern = ""
        step = 1
        while 1:
                if step == 1:
                        seconds = 1
                else:
                        seconds = random.randint(5,120)
                print("Step {} will start in {} Seconds".format(step, seconds))
                print(" ")
                time.sleep(seconds)
                stake = 0.00000001
                print(" [-] Checking ...")
                headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
                        'Cookie': cookie,
                        'x-csrf-token': token
                }
                host = "https://freebitco.in"
                randomseed = random.randint(0000000000000000, 99999999999999999)
                url = "/cgi-bin/bet.pl?m=lo&client_seed=" + seed + "&jackpot=0&stake=" + str(stake) + "&multiplier=2.00&rand=0." + str(randomseed) + "&csrf_token=uVxCzpJF320Y"
                try:
                        r = requests.get(host + url, headers=headers)
                except requests.exceptions.RequestException as e:
                        print(" Some Errors Happened:")
                        print(e)

                print(" [+] Status:", r.status_code, r.reason)
                try:
                        h1 = float(str(r.content).split(":")[3])
                except:
                        print("")
                        print("It's not in correct format, it seems your balance is too low.")
                        print("")
                        sys.exit(0)
                start = h1
                end = 0
                print(" [+] Balance:", "%.8f" % h1)
                print(" ")
                print(" [-] starting ...")
                print(" ")


                for x in range(0, 10):
                        if start < end:
                                f = open("pattern.txt", "a+")
                                f.write(pattern + "\r\n")
                                f.close()
                                pattern = ""
                                break
                        else:
                                print("----------------------------------------")
                                print(" [-] round", x ,"Started")
                                print(" ")
                                for x in range(0, 4):
                                        print(" [+] Amount:", "%.8f" % stake)
                                        headers = {
                                                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0',
                                                'Cookie': cookie,
                                                'x-csrf-token': token
                                        }
                                        randomseed = random.randint(0000000000000000, 99999999999999999)
                                        print(" [+] Random: ", randomseed)
                                        host = "https://freebitco.in"
                                        if x == 3:
                                                print(" [+] Type: High")
                                                url = "/cgi-bin/bet.pl?m=hi&client_seed=" + seed + "&jackpot=0&stake=" + str(stake) + "&multiplier=2.00&rand=0." + str(randomseed) + "&csrf_token=uVxCzpJF320Y"
                                        else:
                                                print(" [+] Type: Low")
                                                url = "/cgi-bin/bet.pl?m=lo&client_seed=" + seed + "&jackpot=0&stake=" + str(stake) + "&multiplier=2.00&rand=0." + str(randomseed) + "&csrf_token=uVxCzpJF320Y"
                                        try:
                                                r = requests.get(host + url, headers=headers)
                                        except requests.exceptions.RequestException as e:
                                                print(" Some Errors Happened:")
                                                print(e)
                                        print(" [+] Status:", r.status_code, r.reason)
                                        try:
                                                h2 = float(str(r.content).split(":")[3])
                                        except:
                                                print("")
                                                print("It's not in correct format, it seems your balance is too low.")
                                                print("")
                                                sys.exit(0)
                                        if h1 > h2:
                                                print(" [+] You Lose", "%.8f" % stake)
                                                stake = (h1 - h2) * 2
                                                pattern = pattern + "0"
                                        else:
                                                print(" [+] You Win", "%.8f" % stake)
                                                stake = 0.00000001
                                                pattern = pattern + "1"
                                        if pattern.count("000000") == 1 and pattern.count("0000001") == 0:
                                                stake = h2
                                        print(" [+] Now You Have:", "%.8f" % h2)
                                        print(" [+] Pattern: {}".format(pattern))
                                        h1 = h2
                                        end = h2
                                        print(" ")
                                        time.sleep(5)
                                print(" [-] round Ended")
                                print("----------------------------------------")
                                print(" ")
                step = step + 1
except KeyboardInterrupt:
        print("")
        print("Exiting ...")
        sys.exit(0)
