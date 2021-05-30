# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# Hell is other people's code.

import bpy

class View3dPanel:
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Item"


    @classmethod
    def poll(cls, context):
        if context.view_layer.objects.active:
            return True


class CUSTOM_UL_NoteList(bpy.types.UIList):
    EMPTY = 1 << 0


    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        split = layout.split(factor=0.2, align=True)
        split.prop(item, "title", text="")
        row = split.row(align=True)
        row.prop(item, "text", text="")
        op = row.operator("nk.remove_note", text="", icon='CANCEL')
        op.index = index

        row.separator()

        op = row.operator("nk.select_by_note_title", text="", icon='VIEWZOOM')
        op.query = item.title
        op.ui = True


    def draw_filter(self, context, layout):
        # Nothing much to say here, it's usual UI code...
        row = layout.row()
        row.alignment = 'RIGHT'


    def filter_items(self, context, data, propname):
        notes = getattr(data, propname)
        flt_flags = []
        flt_neworder = []

        helper_funcs = bpy.types.UI_UL_list

        cams = []
        for obj in bpy.data.objects:
            for cam in notes:
                if obj.data == cam:
                    cams.append(obj)
                    # break

        if self.filter_name:
            flt_flags = helper_funcs.filter_items_by_name(self.filter_name, self.bitflag_filter_item, notes, "title",
                                                          reverse=self.use_filter_name_reverse)
        if not flt_flags:
            flt_flags = [self.bitflag_filter_item] * len(notes)

        if not flt_flags:
            flt_flags = [self.bitflag_filter_item] * len(notes)

        return flt_flags, flt_neworder


class NK_PT_MainPanel(View3dPanel, bpy.types.Panel):
    bl_idname = "NK_PT_MainPanel"
    bl_label = "Notes"

    def draw(self, context):
        layout = self.layout
        root = layout.column(align=True)
        obj = context.view_layer.objects.active

        root.operator(
            "nk.add_note"
        )

        root.separator()
        root.template_list(
            "CUSTOM_UL_NoteList",
            "",
            obj.notes,
            "notes",
            obj.notes,
            "active_index",
            rows=1,
            maxrows=4
        )

        box = root.box()
        box = box.column(align=True)
        note = obj.notes.notes[obj.notes.active_index]

        box.prop(note, 'tags')