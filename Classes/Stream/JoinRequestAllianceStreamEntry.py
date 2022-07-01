from Classes.ByteStream import ByteStream
from Classes.Stream.StreamEntry import StreamEntry
from Classes.Wrappers.PlayerDisplayData import PlayerDisplayData


class JoinRequestAllianceStreamEntry:
    def encode(self: ByteStream, info):
        StreamEntry.encode(self, info)
        self.writeString()
        self.writeString()
        self.writeVInt(0)
        PlayerDisplayData.encode(self, info['Target'])

