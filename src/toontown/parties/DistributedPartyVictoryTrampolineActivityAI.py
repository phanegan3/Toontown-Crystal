from direct.directnotify import DirectNotifyGlobal
from src.toontown.parties.DistributedPartyTrampolineActivityAI import DistributedPartyTrampolineActivityAI

class DistributedPartyVictoryTrampolineActivityAI(DistributedPartyTrampolineActivityAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedPartyVictoryTrampolineActivityAI")

