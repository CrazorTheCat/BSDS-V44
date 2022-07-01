import socket

import Configuration
from Classes.ClientsManager import ClientsManager
from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Utility import Utility
from Database.DatabaseHandler import DatabaseHandler, ClubDatabaseHandler
import json


class LoginMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields["AccountID"] = self.readLong()
        fields["PassToken"] = self.readString()
        fields["ClientMajor"] = self.readInt()
        fields["ClientMinor"] = self.readInt()
        fields["ClientBuild"] = self.readInt()
        fields["ResourceSha"] = self.readString()
        fields["Device"] = self.readString()
        fields["PreferredLanguage"] = self.readDataReference()
        fields["PreferredDeviceLanguage"] = self.readString()
        fields["OSVersion"] = self.readString()
        fields["isAndroid"] = self.readBoolean()
        fields["IMEI"] = self.readString()
        fields["AndroidID"] = self.readString()
        fields["isAdvertisingEnabled"] = self.readBoolean()
        fields["AppleIFV"] = self.readString()
        fields["RndKey"] = self.readInt()
        fields["AppStore"] = self.readVInt()
        fields["ClientVersion"] = self.readString()
        fields["TencentOpenId"] = self.readString()
        fields["TencentToken"] = self.readString()
        fields["TencentPlatform"] = self.readVInt()
        fields["DeviceVerifierResponse"] = self.readString()
        fields["AppLicensingSignature"] = self.readString()
        fields["DeviceVerifierResponse"] = self.readString()
        fields["SupercellIdToken"] = self.readCompressedString()
        fields["UpdateMaintenanceMode"] = self.readBoolean()
        fields["YoozooOsdkTicket"] = self.readString()
        fields["YoozooDeviceId"] = self.readString()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        if fields["ClientMajor"] == 44:
            calling_instance.player.ClientVersion = f'{str(fields["ClientMajor"])}.{str(fields["ClientBuild"])}.{str(fields["ClientMinor"])}'
            fields["Socket"] = calling_instance.client
            db_instance = DatabaseHandler()
            if db_instance.playerExist(fields["PassToken"], fields["AccountID"]):
                player_data = json.loads(db_instance.getPlayerEntry(fields["AccountID"])[2])
                try:
                    player_data["AllianceID"] = player_data["AllianceID"]
                except:
                    player_data["AllianceID"] = [0, 0]
                    db_instance.updatePlayerData(player_data, calling_instance)
                db_instance.loadAccount(calling_instance.player, fields["AccountID"])
            else:
                db_instance.createAccount(calling_instance.player.getDataTemplate(fields["AccountID"][0], fields["AccountID"][1], fields["PassToken"]))

            ClientsManager.AddPlayer(calling_instance.player.ID, calling_instance.client)

            contentUpdateInfo = Utility.getContentUpdaterInfo()
            if Configuration.settings["UseContentUpdater"] == True and fields["ResourceSha"] != contentUpdateInfo[1]:
                Messaging.sendMessage(20103, {'Socket': calling_instance.client, 'ErrorID': 7, 'Message': None, 'FingerprintData': Utility.getFingerprintData(contentUpdateInfo[1]), 'ContentURL': f'http://{socket.gethostbyname(socket.gethostname())}:8080'})

            elif fields["ClientMajor"] == 44:
                Messaging.sendMessage(20104, fields, calling_instance.player)
                Messaging.sendMessage(24101, fields, calling_instance.player)

                try:
                    clubdb_instance = ClubDatabaseHandler()
                    json.loads(clubdb_instance.getClubWithLowID(calling_instance.player.AllianceID[1])[0][1])
                    fields["HasClub"] = True

                except IndexError:
                    player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
                    player_data["AllianceID"] = [0, 0]
                    db_instance.updatePlayerData(player_data, calling_instance)
                    fields["HasClub"] = False

                Messaging.sendMessage(24399, fields, calling_instance.player)
                if fields["HasClub"]:
                    Messaging.sendMessage(24311, fields, calling_instance.player)

            db_instance.cursor.close()

    def getMessageType(self):
        return 10101

    def getMessageVersion(self):
        return self.messageVersion