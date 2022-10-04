import requests
import random
import subprocess

resources = requests.get("https://sekai-world.github.io/sekai-master-db-diff/musicVocals.json").json()

def get_resource(mid):
    print("here:", random.choice([i for i in resources if i["musicId"] == mid])["assetbundleName"])
    return random.choice([i for i in resources if i["musicId"] == mid])["assetbundleName"]

def download(mid):
    resource = get_resource(mid)
    r = requests.get(f"https://storage.sekai.best/sekai-assets/music/short/{resource}_rip/{resource}_short.mp3")

    filename = f"{mid}.mp3"
    print(chr(mid))
    with open(filename, "wb") as f:
        f.write(r.content)
    return mid

with open("flag.txt") as f:
    flag = f.read().strip()

assert flag.startswith("SEKAI{") and flag.endswith("}")
flag = flag[6:-1]
tracks = [download(ord(i)) for i in flag]


