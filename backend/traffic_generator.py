import requests
import random
import time
import argparse

URL = "http://127.0.0.1:5000/traffic"

def generate_traffic(mode="normal"):
    while True:
        ip = f"192.168.1.{random.randint(1, 50)}"
        if mode == "attack":
            ip = "10.0.0.99"  # attacker IP

        try:
            res = requests.post(URL, json={"ip": ip})
            print(ip, res.json())
        except Exception as e:
            print("Error:", e)

        time.sleep(0.1 if mode=="normal" else 0.01)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--attack", action="store_true")
    args = parser.parse_args()

    if args.attack:
        generate_traffic("attack")
    else:
        generate_traffic("normal")
