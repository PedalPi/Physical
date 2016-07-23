# -*- coding: utf-8 -*-
from configurations import Configurations

from action.ActionsFacade import ActionsFacade
from component.Components import Components

from mvc.params.ParamsController import ParamsController
from mvc.patches.PatchesController import PatchesController


class Physical(object):
    app = None
    config = None
    components = None
    controllers = None
    actions = None

    def __init__(self, application):
        self.app = application
        self.config = Configurations()

        self.components = self.initComponents(self.config)

        self.actions = ActionsFacade(application)
        self.controllers = self.initControllers(self.components, self.actions)

        controller = self.controllers[PatchesController]
        controller.init(self.actions.currentPatch)

    def initComponents(self, configurations):
        components = dict()

        components[Components.DISPLAY] = configurations.display
        components[Components.NEXT_PATCH] = configurations.nextPatchButton
        components[Components.BEFORE_PATCH] = configurations.beforePatchButton
        components[Components.EFFECT] = configurations.effectButton
        components[Components.DIGITAL_ENCODER] = configurations.digitalEncoder

        return components

    def initControllers(self, components, actions):
        controllers = {}

        controllers[PatchesController] = PatchesController(controllers, components, actions)
        controllers[ParamsController] = ParamsController(controllers, components, actions)

        return controllers

    def setController(self, controller):
        manager = self.config.manager

        manager.onNext = controller.onNext
        manager.onBefore = controller.onBefore
        manager.onClick = controller.onClick
