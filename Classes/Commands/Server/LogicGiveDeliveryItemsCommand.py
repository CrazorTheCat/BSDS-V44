from Classes.Commands.LogicServerCommand import LogicServerCommand


class LogicGiveDeliveryItemsCommand(LogicServerCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        self.writeVInt(0)

        self.writeVInt(1)

        self.writeVInt(12)

        self.writeVInt(2)

        self.writeVInt(116)
        self.writeVInt(0)
        self.writeVInt(7)
        self.writeHexa('00 00 00', 3)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(29)
        self.writeVInt(218)
        self.writeVInt(5)
        self.writeHexa('00 00 00', 3)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(3)
        LogicServerCommand.encode(self, fields)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        return LogicServerCommand.decode(calling_instance, fields)

    def getCommandType(self):
        return 201