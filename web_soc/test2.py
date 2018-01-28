# coding:utf-8
import requests


payload = {
        "jsonrpc": "2.0",
        "id": 2,
        "method": "DoReload",
        "handle": 1,
        "params": {
            "qMode": 0,
            "qPartial": False,
            "qDebug": False
        }
    }



def send_json(json):
    s = requests.Session()
    s.cert = './key/client.pem'
    r = s.post("wss://10.29.42.18:4747/app/adef91fb-134e-47ed-bfbb-4eb8d1ceffbb", json=json)
    return r.text


if __name__ == "__main__":
    print send_json(payload)