from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage


class PlayerStatusMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields["Unknown1"] = self.readVInt()
        fields["Unknown2"] = self.readVInt()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 14366

    def getMessageVersion(self):
        return self.messageVersion