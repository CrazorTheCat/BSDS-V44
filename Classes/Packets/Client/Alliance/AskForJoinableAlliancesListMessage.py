from Classes.Instances.Classes.Alliance import Alliance
from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Utility import Utility
from Database.DatabaseHandler import DatabaseHandler, ClubDatabaseHandler
import json


class AskForJoinableAlliancesListMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        fields["Socket"] = calling_instance.client
        Messaging.sendMessage(24304, fields, calling_instance.player)

    def getMessageType(self):
        return 14303

    def getMessageVersion(self):
        return self.messageVersion