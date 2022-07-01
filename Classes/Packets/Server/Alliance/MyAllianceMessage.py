from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Wrappers.AllianceHeaderEntry import AllianceHeaderEntry
from Database.DatabaseHandler import ClubDatabaseHandler
import json

class MyAllianceMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        if fields["HasClub"] == True:
            clubdb_instance = ClubDatabaseHandler()
            clubData = json.loads(clubdb_instance.getClubWithLowID(player.AllianceID[1])[0][1])
            localMemberData = clubdb_instance.getMemberWithLowID(clubData, player.ID[1])

            self.writeVInt(1) # Onlines Members TODO: members state
            self.writeBoolean(True)
            self.writeDataReference(25, localMemberData["Role"])
        
            AllianceHeaderEntry.encode(self, clubdb_instance, clubData)

            self.writeBoolean(False)
        else:
            self.writeVInt(0)
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
        return 24399

    def getMessageVersion(self):
        return self.messageVersion