from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import ClubDatabaseHandler
from Classes.Wrappers.AllianceHeaderEntry import AllianceHeaderEntry
import random

class JoinableAllianceListMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        clubdb_instance = ClubDatabaseHandler()
        allClubs = clubdb_instance.getAllClubByRegion(player.Region)

        if len(allClubs) >= 50:
            maxClub = 50
            self.writeVInt(50)
        elif len(allClubs) == 0:
            maxClub = -1
            self.writeVInt(0)
        else:
            maxClub = len(allClubs)
            self.writeVInt(len(allClubs))


        if maxClub > 1:
            found = 0
            randomClubList = []
            while found != maxClub:
                randomEntry = random.choice(allClubs)
                if randomEntry not in randomClubList:
                    randomClubList.append(randomEntry)
                    found += 1

        for clubData in allClubs:
            AllianceHeaderEntry.encode(self, clubdb_instance, clubData)

    def decode(self):
        return { }

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24304

    def getMessageVersion(self):
        return self.messageVersion