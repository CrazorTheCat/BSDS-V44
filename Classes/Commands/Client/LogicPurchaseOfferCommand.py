import json

from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Database.DatabaseHandler import DatabaseHandler

OwnedPinsLatest = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780]
OwnedThumbnailsLatest  = [60, 61, 63, 64, 69, 70, 72, 73, 76, 77, 78, 79, 83, 84, 87, 88, 106, 107]

OwnedBrawlersLatest = {
    0: {'CardID': 0, 'Skins': [29, 52, 122, 159, 195, 196, 320, 321, 322, 359], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    1: {'CardID': 4, 'Skins': [2, 103, 69, 135, 217, 303, 323, 324, 325, 326, 330, 331, 377, 544], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    2: {'CardID': 8, 'Skins': [25, 64, 102, 178, 218, 219, 262, 393, 477, 501], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    3: {'CardID': 12, 'Skins': [5, 58, 72, 91, 201, 242, 400, 401, 541], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    4: {'CardID': 16, 'Skins': [26, 68, 130, 171, 223, 224, 397, 473], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    5: {'CardID': 20, 'Skins': [11, 96, 208, 263, 301, 302, 448, 509], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    6: {'CardID': 24, 'Skins': [27, 59, 90, 92, 116, 220, 221, 357, 436], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    7: {'CardID': 28, 'Skins': [44, 47, 123, 162, 174, 253, 254, 395], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    8: {'CardID': 32, 'Skins': [15, 439, 60, 79, 148, 297, 298, 347], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    9: {'CardID': 36, 'Skins': [56, 57, 97, 160, 236, 276, 314, 315, 316, 398, 430, 431, 462], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    10: {'CardID': 40, 'Skins': [28, 30, 128, 183, 187, 213, 317, 318, 319, 354, 360, 438, 441], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    11: {'CardID': 44, 'Skins': [50, 63, 75, 173, 228, 230, 227, 229, 311], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    12: {'CardID': 48, 'Skins': [20, 49, 95, 100, 101, 248, 249, 390], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    13: {'CardID': 52, 'Skins': [71, 140, 214, 342, 406, 407], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    14: {'CardID': 56, 'Skins': [94, 98, 99, 163, 216, 245, 363, 364, 445, 478], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    15: {'CardID': 60, 'Skins': [108, 120, 147, 197, 198, 234, 382], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    16: {'CardID': 64, 'Skins': [179, 355, 411, 412], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    17: {'CardID': 68, 'Skins': [111, 145, 259, 260, 282, 516], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    18: {'CardID': 72, 'Skins': [70, 158, 250, 251, 264, 351, 511], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    19: {'CardID': 95, 'Skins': [61, 88, 165, 274, 453, 454], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    20: {'CardID': 100, 'Skins': [45, 125, 225, 226, 244], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    21: {'CardID': 105, 'Skins': [117, 172, 304, 305, 389], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    22: {'CardID': 110, 'Skins': [190, 243, 246, 247, 468], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    23: {'CardID': 115, 'Skins': [110, 126, 131, 199, 200, 312], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    24: {'CardID': 120, 'Skins': [215, 309, 446, 455, 456, 483], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    25: {'CardID': 125, 'Skins': [93, 104, 132, 134, 267, 308, 424, 425, 507], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    26: {'CardID': 130, 'Skins': [146, 222, 273, 345, 422, 423, 470], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    27: {'CardID': 177, 'Skins': [109, 143, 283, 402, 403, 409], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    28: {'CardID': 182, 'Skins': [471, 118, 210, 287, 371, 372], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    29: {'CardID': 188, 'Skins': [139, 188, 284, 285, 290, 365, 366], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    30: {'CardID': 194, 'Skins': [167, 185, 186, 209, 542], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    31: {'CardID': 200, 'Skins': [152, 332, 333, 415, 479, 513], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    32: {'CardID': 206, 'Skins': [137, 202, 232, 310, 404, 405], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    34: {'CardID': 218, 'Skins': [176, 189, 307, 444, 449, 450, 505], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    35: {'CardID': 224, 'Skins': [180, 241, 367, 368, 388], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    36: {'CardID': 230, 'Skins': [194, 233, 369, 370], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    37: {'CardID': 236, 'Skins': [177, 211, 379, 383, 488, 492, 493], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    38: {'CardID': 279, 'Skins': [203, 292, 419, 496, 497], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    39: {'CardID': 296, 'Skins': [212, 270, 391, 428, 429], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    40: {'CardID': 303, 'Skins': [280, 426, 427], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    41: {'CardID': 320, 'Skins': [237, 266, 306, 451, 452], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    42: {'CardID': 327, 'Skins': [358, 512], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    43: {'CardID': 334, 'Skins': [472, 281, 437, 506], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    44: {'CardID': 341, 'Skins': [268, 286, 490, 491, 539], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    45: {'CardID': 358, 'Skins': [277, 346, 420, 526, 527], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    46: {'CardID': 365, 'Skins': [294, 489, 524, 525, 547], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    47: {'CardID': 372, 'Skins': [392, 418], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    48: {'CardID': 379, 'Skins': [482, 550, 551], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    49: {'CardID': 386, 'Skins': [343, 386, 494, 495], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    50: {'CardID': 393, 'Skins': [458], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    51: {'CardID': 410, 'Skins': [381, 528, 529], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    52: {'CardID': 417, 'Skins': [475, 517, 532, 533], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    53: {'CardID': 427, 'Skins': [433, 510, 530, 531], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    54: {'CardID': 434, 'Skins': [460, 548, 558, 559], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    56: {'CardID': 448, 'Skins': [484, 552, 553], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    57: {'CardID': 466, 'Skins': [536, 554, 555], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    58: {'CardID': 474, 'Skins': [521, 556, 557], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    59: {'CardID': 491, 'Skins': [546], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
}


class LogicPurchaseOfferCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        LogicCommand.encode(self, fields)
        self.writeVInt(0)
        self.writeDataReference(0)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        fields["Unk1"] = calling_instance.readVInt()
        fields["Unk2"] = calling_instance.readDataReference()
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields):
        if fields["Unk1"] == 0:
            db_instance = DatabaseHandler()
            player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
            for i,v in player_data["OwnedBrawlers"].items():
                v["Skins"] = OwnedBrawlersLatest[int(i)]["Skins"]
            player_data["OwnedPins"] = OwnedPinsLatest
            player_data["OwnedThumbnails"] = OwnedThumbnailsLatest
            db_instance.updatePlayerData(player_data, calling_instance)
            Messaging.sendMessage(24104, {"Socket": calling_instance.client, "ServerChecksum": 0, "ClientChecksum": 0, "Tick": 0})

    def getCommandType(self):
        return 519