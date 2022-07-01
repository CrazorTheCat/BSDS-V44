from Classes.ByteStream import ByteStream
from Classes.Stream.StreamEntry import StreamEntry


class AllianceEventStreamEntry:
    def encode(self: ByteStream, info):
        StreamEntry.encode(self, info)
        self.writeVInt(info['EventType'])
        self.writeBoolean(info['Target'] != {})
        if info['Target'] != {}:
            self.writeLogicLong(info['Target']['ID'][0], info['Target']['ID'][1])
            self.writeString(info['Target']['Name'])

