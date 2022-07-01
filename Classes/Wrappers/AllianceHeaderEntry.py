from Classes.Files.Classes.Regions import Regions

class AllianceHeaderEntry:
    def encode(calling_instance, clubdb, clubData):
        calling_instance.writeLong(clubData["HighID"], clubData["LowID"])
        calling_instance.writeString(clubData["Name"])
        calling_instance.writeDataReference(8, clubData["BadgeID"])
        calling_instance.writeVInt(clubData["Type"])
        calling_instance.writeVInt(len(clubData["Members"]))
        calling_instance.writeVInt(clubdb.getTotalTrophies(clubData))
        calling_instance.writeVInt(clubData["TrophiesRequired"])
        calling_instance.writeDataReference(0)
        calling_instance.writeString(Regions.getRegionByID(calling_instance, clubData["RegionID"]))
        calling_instance.writeVInt(0)
        calling_instance.writeBoolean(clubData["FamilyFriendly"])
        calling_instance.writeVInt(0)

    def decode(calling_instance, fields):
        fields["AllianceHeaderEntry"] = {} # TODO: this thing
        return fields