from Classes.Stream.AllianceEventStreamEntry import AllianceEventStreamEntry
from Classes.Stream.ChatStreamEntry import ChatStreamEntry
from Classes.Stream.JoinRequestAllianceStreamEntry import JoinRequestAllianceStreamEntry
from Classes.Stream.MessageDataStreamEntry import MessageDataStreamEntry
from Classes.Stream.QuickChatStreamEntry import QuickChatStreamEntry
from Classes.Stream.ReplayStreamEntry import ReplayStreamEntry
from Classes.Stream.StreamEntry import StreamEntry
from Classes.Stream.TeamCreatedStreamEntry import TeamCreatedStreamEntry

StreamIDs = {
    2: ChatStreamEntry,
    3: JoinRequestAllianceStreamEntry,
    4: AllianceEventStreamEntry,
    5: ReplayStreamEntry,
    6: MessageDataStreamEntry,
    7: 'Unknown',
    8: QuickChatStreamEntry,
    77: TeamCreatedStreamEntry,
}

class StreamEntryFactory:
    def encode(self, fields, info):
        streamID = info['StreamType']
        if streamID not in StreamIDs:
            StreamEntry.encode(self, info)
            raise NotImplementedError(f"Stream with id {streamID} is not implemented.")
        elif type(StreamIDs[streamID]) != str:
            StreamIDs[streamID].encode(self, info)
        else:
            raise NotImplementedError(f"{StreamIDs[streamID]} is not implemented.")