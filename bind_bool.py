__author__ = "logan.bender@idsoftware.com"

import pymel.core as pm
from idanim.maya.mGui.gui import *
from idanim.maya.mGui.forms import *
from idanim.maya.mGui.bindings import * # need for bind() expression


class Data(object):
    def __init__(self):
        self.bool = False

    def __str__(self):
        return "Data()"

    def info(self):
        return "{}.bool: {}".format(self, self.bool)


class UI(object):
    def __init__(self, data=None):
        self.data = data
        self.window = self.create_window()

    def __str__(self):
        return "UI()"

    def create_window(self):
        # create
        with Window(title="class instance") as window:
            with FooterForm() as main:
                with VerticalForm() as form:
                    cb_1 = CheckBox(label='bool',value=False)
                with HorizontalStretchForm() as footer:
                    btn_1 = Button('print data')

        window.main.form.cb_1.bind.value > bind() > (self.data,'bool') # must be "object.attribute" or (object,attr)

        # add comands
        window.main.footer.btn_1.command += self.test_event

        return window

    def test_event(self, *args, **kwargs):
        print self.data.info()

    def show(self):
        if not self.window:
            self.window = self.create_window()
        self.window.show()


if not pm.uniqueObjExists("my_sphere"):
    pm.polySphere(name="my_sphere")

ui=None
ui = UI(data=Data())
ui.show()
