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
from bpy.props import (
    BoolProperty, IntProperty,
    FloatVectorProperty,
    EnumProperty, StringProperty
)


class NK_OT_AddNote(bpy.types.Operator):
    """Standard"""
    bl_idname = "nk.add_note"
    bl_label = "Add Note"

    def execute(self, context):
        obj = context.view_layer.objects.active
        obj.notes.notes.add()

        return {'FINISHED'}


class NK_OT_RemoveNote(bpy.types.Operator):
    """Standard"""
    bl_idname = "nk.remove_note"
    bl_label = "Remove Note"

    index: IntProperty(
        name='Note Index',
        default=-1
    )

    def execute(self, context):
        if not context.active_object:
            return {'CANCELLED'}

        if len(context.active_object.notes.notes) == 0:
            return{'CANCELLED'}

        obj = context.view_layer.objects.active
        obj.notes.notes.remove(self.index)

        return {'FINISHED'}


class NK_OT_SelectByNoteTitle(bpy.types.Operator):
    """Treats note titles like tags"""
    bl_idname= "nk.select_by_note_title"
    bl_label= "Select Objects by Note Title"

    query: StringProperty(
        name="Search Query",
        default=""
    )

    qtype_items = [
        ('TITLE', 'Title', "Note Title", 1),
        ('TEXT', 'Text', "Note Body Text", 2),
        ('TAGS', 'Tags', "Note Tags", 3)
    ]

    query_type: EnumProperty(
        items=qtype_items,
        name='Search Mode',
        description="What part of the note to search",
        default='TITLE'
    )

    ui: BoolProperty(
        name="Called from UI",
        default=False,
        options={'HIDDEN'}
    )

    def invoke(self, context, event):
        wm = context.window_manager
        if self.ui:
            if event.alt:
                return wm.invoke_props_dialog(self)
            return self.execute(context)

        return wm.invoke_props_dialog(self)

    def execute(self, context):
        bpy.ops.object.select_all(action='DESELECT')
        selected = []

        for obj in context.selectable_objects:
            notes = getattr(obj, "notes", None)
            if notes:
                if len(notes.notes) > 0:
                    for note in notes.notes:
                        target = getattr(note, self.query_type.lower(), 'title')
                        if self.query.lower() in target.lower():
                            selected.append(obj)


        for obj in selected:
            obj.select_set(True)

        return {'FINISHED'}
