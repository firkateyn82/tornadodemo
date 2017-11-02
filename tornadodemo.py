import tornado.ioloop
import tornado.web
import tornado.websocket
import threading
import time

live_web_sockets = set()


class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")
        live_web_sockets.add(self)
        printit()

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")

    def check_origin(self, origin):
        return True

def web_socket_send_message(message):
    removable = set()
    for ws in live_web_sockets:
        if not ws.ws_connection or not ws.ws_connection.stream.socket:
            removable.add(ws)
        else:
            ws.write_message(message)
    for ws in removable:
        live_web_sockets.remove(ws)

def SendBatteryStatus():
    threading.Timer(1.0, SendBatteryStatus).start()
    web_socket_send_message(time.ctime())

def UltraSonicInfo():
    web_socket_send_message(time.ctime())

def main():
    app = tornado.web.Application([
        (r'/websocket', EchoWebSocket),
    ])
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()



if __name__=="__main__":
    main();