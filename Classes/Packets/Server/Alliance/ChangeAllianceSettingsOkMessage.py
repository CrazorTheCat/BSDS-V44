from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Wrappers.AllianceHeaderEntry import AllianceHeaderEntry
from Database.DatabaseHandler import ClubDatabaseHandler, DatabaseHandler
import json

class ChangeAllianceSettingsOkMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        clubdb_instance = ClubDatabaseHandler()
        db_instance = DatabaseHandler()
        clubData = json.loads(clubdb_instance.getClubWithLowID(player.AllianceID[1])[0][1])
        db_instance.loadAccount(player, player.ID)
        
        AllianceHeaderEntry.encode(self, clubdb_instance, clubData)

        self.writeString(clubData["Description"])

        self.writeVInt(len(clubData["Members"]))

        for i in clubdb_instance.getMembersSorted(clubData):
            memberData = i[1]
            playerData = json.loads(db_instance.getPlayerEntry([memberData['HighID'], memberData['LowID']])[2])
            self.writeLong(memberData['HighID'], memberData['LowID'])
            self.writeVInt(memberData['Role']) # Role
            self.writeVInt(playerData['Trophies']) # Trophies
            self.writeVInt(0) # Player State TODO: Members state
            self.writeVInt(0) # State Timer

            # whatIsThat = 5
            whatIsThat = 0
            self.writeVInt(whatIsThat)
            # if whatIsThat >= 1:
            #     self.writeVint(1) # idk
            #     self.writeVint(3) # Power League Rank

            self.writeBoolean(False) # DoNotDisturb TODO: Do not disturb sync

            self.writeString(playerData['Name']) # Player Name
            self.writeVInt(100)
            self.writeVInt(28000000 + playerData['Thumbnail']) # Player Thumbnail
            self.writeVInt(43000000 + playerData['Namecolor']) # Player Name Color
            self.writeVInt(46000000) # Color Gradients

            self.writeVInt(-1)
            self.writeBoolean(False)

            thisThing = 0
            self.writeVInt(thisThing) # Club Leauge?

            if thisThing > 1:
                self.writeVInt(0)
                self.writeVInt(0)
                self.writeVInt(0)
                self.writeVInt(0)
                self.writeVInt(0)
                self.writeVInt(0)
                self.writeVInt(0)
                self.writeBoolean(False)

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24313

    def getMessageVersion(self):
        return self.messageVersion