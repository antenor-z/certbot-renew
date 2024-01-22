#!/usr/bin/env python3

import requests
import os
import json
import time

with open(".env") as fp:
    secrets = json.load(fp)

DOMAIN_ID = secrets["DOMAIN_ID"]
TOKEN = secrets["TOKEN"]
CERTBOT_VALIDATION = os.environ["CERTBOT_VALIDATION"]
WAIT_TIME = secrets["WAIT_TIME"]


res = requests.post(
    url=f"https://api.linode.com/v4/domains/{DOMAIN_ID}/records",
    headers= {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"},
    json= {
        "type": "TXT",
        "name": "_acme-challenge",
        "target": CERTBOT_VALIDATION,
        "ttl_sec": 120
    })

if res.status_code != 200:
    print(res.text)
    exit(1)

TXT_RECORD_ID = str(res.json()["id"])

with open("/tmp/TXT_RECORD_ID", "a") as fp:
    fp.write(f"{TXT_RECORD_ID},")

time.sleep(WAIT_TIME)
