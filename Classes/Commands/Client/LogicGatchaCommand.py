import json

from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Database.DatabaseHandler import DatabaseHandler

class LogicGatchaCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        LogicCommand.encode(self, fields)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields):
        fields["Socket"] = calling_instance.client
        fields["Command"] = {"ID": 203}
        Messaging.sendMessage(24111, fields)

    def getCommandType(self):
        return 500