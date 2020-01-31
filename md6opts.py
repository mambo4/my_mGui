__author__ = "logan.bender@idsoftware.com"

"""
optionbox for idMenuItem export md6Mesh
"""

import sys;

sys.path.append("W:/animation-pipeline/python27/idanim/maya/mGui")

import pymel.core as pm

from idanim.maya.mGui.gui import *
from idanim.maya.mGui.forms import *
from idanim.maya.mGui.bindings import BindingContext as bind

TEST = True
ID_MD6MASK = "W:/ghost/base/md6/characters/monsters/imp/assets/mesh/imp.md6mask"
ID_MD6SKL = "W:/ghost/base/md6/characters/monsters/imp/assets/mesh/imp.md6skl"
ID_MD6MESH = "W:/ghost/base/md6/characters/monsters/imp/assets/mesh/imp.md6mesh"
ID_MD6DEFPATH = "W:/ghost/base/declTree/md6Def/md6def/characters/monsters/imp/imp.md6def"


def create_export_set():
    export_set = pm.createNode("network", name="ExportSet")
    pm.addAttr(longName="id_Md6Mask", dataType="string")
    pm.addAttr(longName="id_Md6Skl", dataType="string")
    pm.addAttr(longName="id_Md6Mesh", dataType="string")
    pm.addAttr(longName="id_Md6DefPath", dataType="string")
    export_set.id_Md6Mask.set(ID_MD6MASK)
    export_set.id_Md6Skl.set(ID_MD6SKL)
    export_set.id_Md6Mesh.set(ID_MD6MESH)
    export_set.id_Md6DefPath.set(ID_MD6DEFPATH)
    return export_set


def get_export_set():
    if pm.uniqueObjExists("ExportSet"):
        return pm.PyNode("ExportSet")
    else:
        return create_export_set()


class ExportMd6OptionsUI(object):
    def __init__(self, export_set=None):
        self.md6mask = ""
        self.md6skl = ""
        self.md6mesh = ""
        self.md6def = ""
        self.export_set_loaded = False
        self.is_overrides = False
        self.normals = True
        self.test = False
        if export_set:
            self._load_export_set(export_set)

        self.window = self.create_window()

    def __str__(self):
        return ("ExportMd6OptionsUI()")

    def _load_export_set(self, export_set):
        self.md6mask = export_set.id_Md6Mask.get()
        self.md6skl = export_set.id_Md6Skl.get()
        self.md6mesh = export_set.id_Md6Mesh.get()
        self.md6def = export_set.id_Md6DefPath.get()
        self.export_set_loaded = True

    def on_command_clicked(self, *args, **kwargs):
        # print("on_command_clicked({},{})...".format(args,kwargs))
        pm.deleteUI(self.id, window=True)
        normals = kwargs.get("normals", True)

        if self.is_overrides:
            print("export_md6mesh.export_md6mask(md6mask_override={},test={})".format(self.md6mask, TEST))
            print("export_md6mesh.export_md6skl(md6mask_override={},md6skl_override={},test={})".format(self.md6mask,
                                                                                                        self.md6skl,
                                                                                                        TEST))
            print("export_md6mesh.export_md6mesh(md6skl_override={},md6mesh_override={},normals={},test={})".format(
                self.md6skl, self.md6mesh, normals, TEST))
            print("export_md6mesh.export_md6def(md6mesh_override={},md6def_override={},test={})".format(self.md6mesh,
                                                                                                        self.md6def,
                                                                                                        TEST))
        else:
            print("export_md6mesh.idMD6_ExportPlus(normals={}, test={})".format(normals, TEST))
            # export_md6mesh.idMD6_ExportPlus(normals=normals, test=TEST)

    def info(self):
        print("{}.md6mask:{}".format(self, self.md6mask) )
        print("{}.md6skl:{}".format(self, self.md6skl) )
        print("{}.md6mesh:{}".format(self, self.md6mesh) )
        print("{}.md6def:{}".format(self, self.md6def) )
        print("{}.export_set_loaded:{}".format(self, self.export_set_loaded) )
        print("{}.is_overrides:{}".format(self, self.is_overrides) )
        print("{}.normals:{}".format(self, self.normals) )
        print("{}.test:{}".format(self, self.test) )

    def create_window(self):
        with Window() as window:
            with FooterForm() as form:
                with VerticalForm() as options:
                    cb_normals = CheckBox(label="normals", value=True)
                    cb_normals.value > bind() > self.normals
                    cb_normals.changeCommand += self.info
                    cb_test = CheckBox(label="test", value=True)
                    cb_override = CheckBox(label="override")
                    with RowColumnLayout('overrides', numberOfColumns=2, visible=False) as overrides:
                        cb_md6mask = CheckBox(label="")
                        tf_md6mask = TextField(text=self.md6mask, width=500, editable=False)
                        cb_md6skl = CheckBox(label="")
                        tf_md6skl = TextField(text=self.md6skl, width=500, editable=False)
                        cb_md6mesh = CheckBox(label="")
                        tf_md6mesh = TextField(text=self.md6mesh, width=500, editable=False)
                        cb_md6def = CheckBox(label="")
                        tf_md6def = TextField(text=self.md6def, width=500, editable=False)
                with HorizontalStretchForm() as buttons:
                    btn_all = Button(label="export md6 all")
                    btn_mesh = Button(label="export md6 mesh")
        return window

    def show(self):
        self.window.show()

    def set_commands(self):
        print "set_commands()..."
        print self.window.named_children
        self.window.form.options.cb_mormals.value > bind() > self.normals
        # self.window.main.options.cb_test.value > bind() > self.normals
        # self.window.main.options.cb_overrides.value > bind() > self.window.main.options.overrides.visible

    def update_ui(self):
        print"{}.update".format(self)
        self.normals = pm.checkBox(self.checkbox_normals, q=True, value=True)
        self.test = pm.checkBox(self.checkbox_test, q=True, value=True)
        # are the override boxes checked?
        show_md6mask = pm.checkBox(self.checkbox_md6mask, q=True, value=True)
        show_md6skl = pm.checkBox(self.checkbox_md6skl, q=True, value=True)
        show_md6mesh = pm.checkBox(self.checkbox_md6mesh, q=True, value=True)
        show_md6def = pm.checkBox(self.checkbox_md6def, q=True, value=True)

        pm.textField(self.textfield_md6mask, edit=True, text=self.md6mask, visible=show_md6mask)
        pm.textField(self.textfield_md6skl, edit=True, text=self.md6skl, visible=show_md6skl)
        pm.textField(self.textfield_md6mesh, edit=True, text=self.md6mesh, visible=show_md6mesh)
        pm.textField(self.textfield_md6def, edit=True, text=self.md6def, visible=show_md6def)

    def update_md6data(self):
        self.is_overrides = True
        self.md6mask = pm.textField(self.textfield_md6mask, query=True, text=True)
        self.md6skl = pm.textField(self.textfield_md6skl, query=True, text=True)
        self.md6mesh = pm.textField(self.textfield_md6mesh, query=True, text=True)
        self.md6def = pm.textField(self.textfield_md6def, query=True, text=True)
        self.update_ui()


def run():
    export_set = get_export_set()
    ui = ExportMd6OptionsUI(export_set=export_set)
    ui.show()
    # ui.export_set = get_export_set()
    # ui.update_ui()
    # todo: populate md6 values from exportset


if __name__ == '__main__':
    run()
