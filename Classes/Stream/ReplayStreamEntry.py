from Classes.ByteStream import ByteStream
from Classes.Stream.StreamEntry import StreamEntry


class ReplayStreamEntry:
    def encode(self: ByteStream, info):
        StreamEntry.encode(self, info)
        self.writeVInt(0)
        self.writeLong(info['ReplayID'][0], info['ReplayID'][1])
        self.writeBoolean(False)
        self.writeString("String1")
        self.writeString("String2")
        self.writeString("String3")
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

