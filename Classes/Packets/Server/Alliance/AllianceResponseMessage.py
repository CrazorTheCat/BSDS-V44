from Classes.Packets.PiranhaMessage import PiranhaMessage


class AllianceResponseMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        self.writeVInt(fields["ResponseID"])
        self.writeVInt(0)

    def decode(self):
        fields = {}
        fields["ResponseID"] = self.readVInt()
        fields["Unk1"] = self.readVInt()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24333

    def getMessageVersion(self):
        return self.messageVersion