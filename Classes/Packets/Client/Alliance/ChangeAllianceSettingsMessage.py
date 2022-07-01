from Classes.Instances.Classes.Alliance import Alliance
from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Utility import Utility
from Database.DatabaseHandler import ClubDatabaseHandler
import json


class ChangeAllianceSettingsMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields["Description"] = self.readString()
        fields["Badge"] = self.readDataReference()
        fields["Region"] = self.readDataReference()
        fields["Type"] = self.readVInt()
        fields["RequiredTrophies"] = self.readVInt()
        fields["FamilyFriendly"] = self.readBoolean()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        fields["Socket"] = calling_instance.client
        clubdb_instance = ClubDatabaseHandler()
        clubData = json.loads(clubdb_instance.getClubWithLowID(calling_instance.player.AllianceID[1])[0][1])

        if clubData["Members"][str(calling_instance.player.ID[1])]["Role"] == 2:
            clubData["Description"] = fields["Description"]
            clubData["BadgeID"] = fields["Badge"][1]
            clubData["RegionID"] = fields["Region"][1]
            clubData["Type"] = fields["Type"]
            clubData["TrophiesRequired"] = fields["RequiredTrophies"]
            clubData["FamilyFriendly"] = fields["FamilyFriendly"]
            clubdb_instance.updateClubData(clubData, calling_instance.player.AllianceID[1])
            fields["HasClub"] = True
            Messaging.sendMessage(24399, fields, calling_instance.player)
            Messaging.sendMessage(24313, fields, calling_instance.player)
            fields["ResponseID"] = 10
            Messaging.sendMessage(24333, fields)
        else:
            Messaging.sendMessage(24399, fields, calling_instance.player)
            fields["ResponseID"] = 95
            Messaging.sendMessage(24333, fields)

    def getMessageType(self):
        return 14316

    def getMessageVersion(self):
        return self.messageVersion