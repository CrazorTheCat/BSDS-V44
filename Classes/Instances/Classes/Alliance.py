class Alliance:
    ID = [0, 1]
    Name = "Club Name"
    Members = {}
    Description = "Club Description"
    BadgeID = 0
    RegionID = 0
    Type = 0
    TrophiesRequired = 0
    FamilyFriendly = False
    ChatData = []

    def createClubData(calling_instance, fields):
        DBData = {
            'HighID': fields["ClubID"][0],
            'LowID': fields["ClubID"][1],
            'Name': fields['Name'],
            'Members': {str(calling_instance.player.ID[1]): {'HighID': calling_instance.player.ID[0], 'LowID': calling_instance.player.ID[1], 'Name': calling_instance.player.Name, 'Role': 2, 'Trophies': calling_instance.player.Trophies, 'NameColor': calling_instance.player.Namecolor, 'Thumbnail': calling_instance.player.Thumbnail}},
            'Description': fields['Description'],
            'BadgeID': fields['Badge'][1],
            'RegionID': fields['Region'][1],
            'Type': fields['Type'],
            'TrophiesRequired': fields['RequiredTrophies'],
            'FamilyFriendly': fields['FamilyFriendly'],
            'ChatData': []
        }
        return DBData