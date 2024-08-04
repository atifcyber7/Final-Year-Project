from twisted.internet import reactor, protocol

class FakeService(protocol.Protocol):
    def connectionMade(self):
        peer = self.transport.getPeer()
        print(f"Incoming connection from: {peer.host}")

    def dataReceived(self, data):
        # Handle incoming data if needed
        pass

class FakeServiceFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return FakeService()

def main():
    ports = [23, 80, 3306]  # Example ports for Telnet, HTTP, MySQL
    for port in ports:
        try:
            reactor.listenTCP(port, FakeServiceFactory())
            print(f"Listening on {port} for fake service")
        except Exception as e:
            print(f"Failed to start fake service on port {port}: {e}")

    reactor.run()

if __name__ == '__main__':
    main()

