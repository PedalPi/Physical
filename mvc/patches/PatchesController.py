# -*- coding: utf-8 -*-
from base.Controller import Controller
from mvc.patches.PatchesView import PatchesView


class PatchesController(Controller):
    indexEffectFocused = 0
    currentPatch = None

    def __init__(self, components, actions):
        super().__init__(components, actions, PatchesView)

    def init(self, currentPatch):
        self.currentPatch = currentPatch
        self.view.showPatch(currentPatch)

    def toNextPatch(self):
        nextPatch = self.actions.toNextPatch()
        self.init(nextPatch)

    def toBeforePatch(self):
        beforePatch = self.actions.toBeforePatch()
        self.init(beforePatch)

    def toggleStatusEffect(self):
        beforePatch = self.actions.toBeforePatch()
        self.init(beforePatch)

    @property
    def currentEffect(self):
        return self.currentPatch.effects[self.indexEffectFocused]

    def toNextEffect(self):
        self.indexEffectFocused += 1
        if self.indexEffectFocused == self.currentPatch.effects.size:
            self.indexEffectFocused = 0

        self.view.showEffect(self.currentEffect)

    def toBeforeEffect(self):
        self.indexEffectFocused -= 1

        if self.indexEffectFocused == -1:
            self.indexEffectFocused = self.currentPatch.effects.size-1

        self.view.showEffect(self.currentEffect)
