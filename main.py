# -*- coding:utf8 -*-
import os
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket


class SimpleEcho(WebSocket):
    def handleMessage(self):
        print(self.data)
        command = os.popen(self.data)
        self.sendMessage(command.read())

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')


if __name__ == '__main__':
    server = SimpleWebSocketServer('', 8991, SimpleEcho)
    server.serveforever()
