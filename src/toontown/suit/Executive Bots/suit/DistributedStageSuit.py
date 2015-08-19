from src.toontown.suit import DistributedFactorySuit
from src.toontown.suit.Suit import *
from direct.directnotify import DirectNotifyGlobal
from direct.actor import Actor
from src.otp.avatar import Avatar
import SuitDNA
from src.toontown.toonbase import ToontownGlobals
from pandac.PandaModules import *
from src.toontown.battle import SuitBattleGlobals
from direct.task import Task
from src.toontown.battle import BattleProps
from src.toontown.toonbase import TTLocalizer
import string

class DistributedStageSuit(DistributedFactorySuit.DistributedFactorySuit):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedStageSuit')

    def setCogSpec(self, spec):
        self.spec = spec
        self.setPos(spec['pos'])
        self.setH(spec['h'])
        self.originalPos = spec['pos']
        self.escapePos = spec['pos']
        self.pathEntId = spec['path']
        self.behavior = spec['behavior']
        self.skeleton = spec['skeleton']
        self.boss = spec['boss']
        self.revives = spec.get('revives')
        if self.reserve:
            self.reparentTo(hidden)
        else:
            self.doReparent()
