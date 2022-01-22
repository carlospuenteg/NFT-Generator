import shutil
import os
import json

number_of_NFTs = 100  # ( 100 / 8000 )

data = {
  "name": "",  # ( "Degen Ape #0 / Degen Ape #1 / Degen Ape" ) If you put "#0" at the end, they will be numerated starting from 0. If you put "#1", they will start from 1. If you don't put "#", they won't be numerated
  "symbol": "",  # ( "POWR" )
  "description": "",  # ( "100,000 digital snowflakes floating around the metaverse. Learn more at fractal.is/nft" )
  "seller_fee_basis_points": 0,  # Royalties -> 1000 = 10%  ( 700 , 1000 )
  "image": "image.png",  # ( image.png , image.jpg )
  "external_url": "",  # ( "https://www.fractal.is" )
  "edition": 0,  # ( 0 , "2021 Summer Edition" )
  "collection": {
    "name": "",  # ( "Galactic Gecko Space Garage" / "fractals" )
    "family": ""  # ( "Galactic Gecko" / "fractals" )
  },
  "updateAuthority": "53LS1oDAWmCMFaezgYqwprEwM1Ginrxj5SVDK6AaU7gB",  # Public key of the wallet that will have the update authority ( "53LS1oDAWmCMFaezgYqwprEwM1Ginrxj5SVDK6AaU7gB" )
  "properties": {
    "creators": [  # You can add more than 1 to this list
      {
        "address": "HMduKVo3A19U5EpQdEhPjo9hq9zfZXn8aGVYZp7Vc7fX",  # Your public address ( "8fKenUymbNLAiCfiTx6gkBUHgyUCZNcc8yMqcZMFYEyz" )
        "share": 100,  # Your share of the royalties
        "verified": 1  # 1 (address is verified) / 0 (address is not verified)
      },
    ]
  }
}

data["properties"]["files"] = {}
data["properties"]["files"]["uri"] = data["image"]
data["properties"]["files"]["type"] = "/".join(data["image"].split("."))
data["properties"]["category"] = "image"

def create():
    if "builds" not in os.listdir(os.getcwd()): os.mkdir("builds")
    buildNum = str(int(sorted(os.listdir("builds"))[-1])+1) if os.listdir("builds") else "1"
    os.mkdir("builds/" + buildNum)
    os.mkdir("builds/" + buildNum + "/json")
    os.mkdir("builds/" + buildNum + "/images")

    for i in range(number_of_NFTs):
        newData = data.copy()
        name = data["name"]
        if name[-2:] == "#0":
            newData["name"] = name[:-1] + str(i)
        elif name[-2:] == "#1":
            newData["name"] = name[:-1] + str(i+1)

        with open("builds/" + buildNum + "/json/" + str(i) + ".json", 'w') as json_file:
            json.dump(newData, json_file, indent=4)

        imgName = "".join(os.listdir("img"))
        shutil.copy2("img/" + imgName, "builds/" + buildNum + "/images/" + str(i) + "." + data["image"].split(".")[1])

create()