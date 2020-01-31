__author__ = "logan.bender@idsoftware.com"

from idanim.maya.mGui.gui import *
from idanim.maya.mGui.forms import *
from idanim.maya.mGui.lists import *
from idanim.maya.mGui.core import BindingContext as bind


class Data(object):
    def __init__(self):
        self.bool = True
        self.text = "my_text"
        self.list = ["spam", "eggs", "sausage", "spam"]
        self.dict = {"Swallows": ["african", "european"], "teeth": {"nasty", "huge", "sharp", "pointy"}}

    def __str__(self):
        return "Data()"

    def info(self):
        for k, v in vars(self).iteritems():
            print "{}.{}:{}".format(self, k, v)


class UI(object):
    def __init__(self, data=None):
        self.data = data

        self.window = self.create_window()

    def create_window(self):
        # create
        with Window(title="class instance") as window:
            with FooterForm() as main:
                with VerticalForm() as form:
                    cb_1 = CheckBox(label='bool')
                    # lb_1 = VerticalList()
                with HorizontalStretchForm() as footer:
                    btn_beans = Button('add baked beans', width=60)
                    btn_ham = Button('add ham', width=60)

        # bind controls to data
        window.main.form.cb_1.bind.value > bind() > self.data.bool
        window.main.form.cb_1.changeCommand += self.test_event
        # window.main.form.lb_1.collection.set_collection(self.data.list)
        window.main.footer.btn_beans.command += self.test_event
        window.main.footer.btn_ham.command += self.test_event_alt


        return window

    def test_event(self, *args, **kwargs):
        print "test_event({},{})".format(args, kwargs)
        self.data.info()

    def test_event_alt(self, *args, **kwargs):
        print "test_event_alt({},{})".format(args, kwargs)
        print "{} was pressed".format(kwargs["sender"])
        self.data.info()

    def show(self):
        self.window.show()

    def info(self):
        for k, v in vars(self).iteritems():
            print "{}.{}:{}".format(self, k, v)


ui = UI(data=Data())
ui.show()
ui.info()
