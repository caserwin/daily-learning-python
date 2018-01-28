# coding: utf-8

from websocket import create_connection
import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

# qlik_ws_url = "ws://127.0.0.1:4848/app/C%3A%5CUsers%5Cvirilo.tejedor%5CDocuments%5CQlik%5CSense%5CApps%5CPOC.qvf"
# qlik_wss_url = "wss://10.29.42.18/app/adef91fb-134e-47ed-bfbb-4eb8d1ceffbb?reloadUri=https://10.29.42.18/dev-hub/engine-api-explorer"

qlik_wss_url = "wss://10.29.42.18:4747/app/adef91fb-134e-47ed-bfbb-4eb8d1ceffbb"
ws = create_connection(qlik_wss_url, sslopt={"cert_reqs": ssl.CERT_NONE})

params = '''{
    "jsonrpc": "2.0",
    "id": 2,
    "method": "DoReload",
    "handle": 1,
    "params": {
	   "qMode": 0,
	   "qPartial": false,
	   "qDebug": false
	}
}
'''
ws.send(params)
result = ws.recv()
print ("Received '%s'" % result)
# ws.close()
