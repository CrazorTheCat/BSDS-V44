from Classes.ByteStream import ByteStream
from Classes.Stream.StreamEntry import StreamEntry


class TeamCreatedStreamEntry:
    def encode(self: ByteStream, info):
        StreamEntry.encode(self, info)
        self.writeLong(info['TargetID'][0], info['TargetID'][1])
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
