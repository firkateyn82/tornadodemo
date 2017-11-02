import tornado.ioloop
import tornado.web
import tornado.websocket


class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")

def make_app():
    return tornado.web.Application([
        (r'/ws', EchoWebSocket),
    ])


if __name__=="__main__":
    app=make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()