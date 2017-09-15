#!/usr/local/bin/python3

import requests
import time
import random

def set_lights(r, g, b):
    r = requests.get("http://10.1.248.40/setlight", params={"red":r, "green":g, "blue": b})

for i in range(0, 255):
    set_lights(i, i, i)



