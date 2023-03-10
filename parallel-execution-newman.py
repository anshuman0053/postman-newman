import subprocess
import json
import random
import sys

collection_url = sys.argv[1]

with open('CVC_Apis.postman_collection.json', 'r') as f:
    collection = json.load(f)

random.shuffle(collection['item'])

chunks = [collection['item'][i:i+10] for i in range(0, len(collection['item']), 20)]

for i, chunk in enumerate(chunks):
    command = f"newman run {collection_url} --env-var concurrency={len(chunk)} --reporters cli,junit --reporter-junit-export report.xml"
    proc = subprocess.Popen(command, shell=True)
    proc.wait()

print(f"Started {len(chunks)} parallel processes for {len(collection['item'])} requests.")
