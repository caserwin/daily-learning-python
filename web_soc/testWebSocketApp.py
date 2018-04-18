from websocket import WebSocketApp
import time
import thread

wss_address = "wss://10.29.42.18:4747/app/adef91fb-134e-47ed-bfbb-4eb8d1ceffbb"

ssl_opt = {
    'certfile': "./key/client.pem",
    "keyfile": "./key/client_key.pem",
    "ca_certs": "./key/root.pem"
}


def on_message(ws, message):
    print(message)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    def run(*args):
        for i in range(3):
            time.sleep(1)
            ws.send("Hello %d" % i)
        time.sleep(1)
        ws.close()
        print("thread terminating...")

    thread.start_new_thread(run, ())

ws = WebSocketApp(wss_address, on_open=on_open, on_message= on_message, on_error=on_error, on_close=on_close)

if __name__ == "__main__":
    ws.run_forever(sslopt= ssl_opt)
    ws.send("Hello")
