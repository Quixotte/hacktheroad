import requests
from pprint import pprint

import json
import pandas as pd

def request_hack_the_road():
    #r = requests.get("https://hacktheroad.mqd.me/api/instruments/")

    #response_dict = json.loads(r.text)
    #collected_results = response_dict["results"]
    #while "next" in response_dict and response_dict["next"] is not None:
    #    response_dict = json.loads(requests.get(response_dict["next"]).text)
    #    collected_results += response_dict["results"]

    df = pd.DataFrame.from_csv("hacktheroad_instruments.csv")

    df["lat"] = [eval(loc)["lat"] for loc in df["location"]]
    df["lng"] = [eval(loc)["lng"] for loc in df["location"]]
    del df["location"]
    df.to_csv("hacktheroad_instruments.csv")

if __name__ == "__main__":
    request_hack_the_road()

    #wop = '{"lat":45}'
    #print(json.loads(wop))
    #print(json.loads(json.dumps(wop)))
