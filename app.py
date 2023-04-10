# Author: nikobelic29
#
# Purpose: Intakes one argument shared_secret and whether to align with steam time
# and spits out a one-time 5 character code
#
###################################################################################


import sys
from base64 import b64decode
from time import time
from hashlib import sha1
import hmac
from math import floor
import os

steamGuardCodeTranslations = [ 50, 51, 52, 53, 54, 55, 56, 57, 66, 67, 68, 70, 71, 72, 74, 75, 77, 78, 80, 81, 82, 84, 86, 87, 88, 89 ]


def Gen_Code(share):
    global time
    share = share.strip()
    share = b64decode(share)

    timeArr = [0] * 8

    timestamp = floor((time() // 1) // 30)

    for i in reversed(range(len(timeArr))):
        timeArr[i] = timestamp & 0xff
        timestamp >>= 8

    hmacGen = hmac.new(share, b''.join(i.to_bytes(1, "little") for i in timeArr), sha1)
    hashedData = hmacGen.digest().rstrip(b"\n")

    codeArray = [0] * 5

    b = hashedData[19] & 0xF
    codePoint = (hashedData[b] & 0x7F) << 24 | \
        (hashedData[b + 1] & 0xFF) << 16 | \
        (hashedData[b + 2] & 0xFF) << 8 | \
        (hashedData[b + 3] & 0xFF);

    for i in range(5):
        codeArray[i] = steamGuardCodeTranslations[floor(codePoint % len(steamGuardCodeTranslations))];
        codePoint /= len(steamGuardCodeTranslations)

    return ''.join(chr(i) for i in codeArray)

if __name__ == "__main__":
    #shr = os.getenv('SHARED_SECRET')
    #print(shr)
    shr = sys.argv[1]
    print(Gen_Code(shr))


