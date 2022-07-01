from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import ClubDatabaseHandler
from Classes.Stream.StreamEntryFactory import StreamEntryFactory
import json

class AllianceStreamMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        clubdb_instance = ClubDatabaseHandler()
        clubData = json.loads(clubdb_instance.getClubWithLowID(player.AllianceID[1])[0][1])

        self.writeVInt(len(clubData["ChatData"]))
        for i in clubData['ChatData']:
            self.writeVint(i['StreamType'])
            StreamEntryFactory.encode(self, fields, i)

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24311

    def getMessageVersion(self):
        return self.messageVersion