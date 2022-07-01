from Classes.ByteStream import ByteStream
from Classes.Stream.StreamEntry import StreamEntry

class MessageDataStreamEntry:
    def encode(self: ByteStream, info):
        StreamEntry.encode(self, info)
        self.writeDataReference(0, info['MessageID'])

