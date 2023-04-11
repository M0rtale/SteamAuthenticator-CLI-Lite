# SteamAuthenticator-CLI-Lite
An Extremely Lightweight CLI steam authenticator generator (Literally just one file)

# Why did you make this
procrastinating at work, wanted to check acc but don't have windows instance, and now I can do this on my work PC (Do not try on your own work pc)

# How do I know the code is not malicious
Read app.py, no internet connection is made and all operations are offline

# How to use
If you just want simple one-time use, use CLI Install, if you need 
A lot of code constantly, use Docker. NOTE: PLEASE BLOCK port 6789
OR MODIFY YOUR CODE WITH BASIC AUTHENTICATION OTHERWISE YOU WILL LOSE 
YOUR STEAM AUTH (run the iptable command)

## Install
First, get your shared secret from the maFile or whereever
Then
```
git clone https://github.com/M0rtale/SteamAuthenticator-CLI-Lite.git
cd SteamAuthenticator-CLI-Lite
```

Then replace ```YOUR_SECRET_HERE`` with your shared secret and 

```
echo SHARED_SECRET=YOUR_SECRET_HERE >> .env
```

## CLI run - how to start getting codes
```
python3 app.py
```

## Docker Install - Please follow Install Steps above first
```
sudo apt-get update
sudo apt-get install docker.io -y

iptables -A INPUT -p tcp --destination-port 6789 -j DROP
docker build .
docker images ls
```

## Docker Start
```
docker run -d -p 6789:6789 DOCKER_IMAGE_ID_HERE
```

## Docker stop
```
docker stop CONTAINER_ID -f
```

## Docker get codes
```
nc 127.0.0.1 6789
```

# CREDITS
geel9 - https://github.com/geel9/SteamAuth

# TODO
* Add Confirmation Support
* Add multi-account support
* idk cookies?
