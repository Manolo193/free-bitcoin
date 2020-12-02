# What is FreeBitCoin ?
This is a free script for automatic playing in freebitco.in website and earn Free BitCoin. you can play multiple BTC with this script.

# How to Use ?
You need to extract your cooke, client seed and csrf token from playing packet. you can use BurpSuite or any other interception application for extracting this information.

I'll show you how you can extract this information from your request packet. see below image for more information.
![Create Request/Response File](https://raw.githubusercontent.com/Miladkhoshdel/free-bitcoin/master/Help.PNG)



# FreeBitCoin version 1.1

- All patterns will save automaticly in patter.txt file.
note that if you win your pattern is 1 and if you lose your pattern is 0.

- Script bet all of your balance if detect that you lost 6 set Continuously.

Usage:

```sh
$ python.exe script.py -c "Cookie" -s "ClientSeed" -t "Token(for bypassing cloudflare)"
```

# FreeBitCoin version 1.0

You can use this script for bet automatically on freebitco [dot] in in HI LO game.

Usage:

```sh
$ python.exe script.py -c "Cookie" -s "ClientSeed" -t "Token(for bypassing cloudflare)"
```
