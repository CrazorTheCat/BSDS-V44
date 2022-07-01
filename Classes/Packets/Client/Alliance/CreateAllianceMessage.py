from Classes.Instances.Classes.Alliance import Alliance
from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Utility import Utility
from Database.DatabaseHandler import DatabaseHandler, ClubDatabaseHandler
import json


class CreateAllianceMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields["Name"] = self.readString()
        fields["Description"] = self.readString()
        fields["Badge"] = self.readDataReference()
        fields["Region"] = self.readDataReference()
        fields["Type"] = self.readVInt()
        fields["RequiredTrophies"] = self.readVInt()
        fields["FamilyFriendly"] = self.readBoolean()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        db_instance = DatabaseHandler()
        clubdb_instance = ClubDatabaseHandler()
        fields["Socket"] = calling_instance.client

        db_instance.loadAccount(calling_instance.player, calling_instance.player.ID)

        fields["ClubID"] = Utility.getRandomID()
        fields["ClubInfo"] = Alliance.createClubData(calling_instance, fields)
        clubdb_instance.createClub(fields["ClubID"][1], fields["ClubInfo"])

        player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
        player_data["AllianceID"] = fields["ClubID"]
        db_instance.updatePlayerData(player_data, calling_instance)

        fields["ResponseID"] = 20
        Messaging.sendMessage(24333, fields)
        Messaging.sendMessage(24311, fields, calling_instance.player)
        fields["HasClub"] = True
        Messaging.sendMessage(24399, fields, calling_instance.player)

    def getMessageType(self):
        return 14301

    def getMessageVersion(self):
        return self.messageVersion