# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy
from bpy.props import PointerProperty

from . properties import Note
from . properties import NoteCollection

from . operators import NK_OT_AddNote
from . operators import NK_OT_RemoveNote
from . operators import NK_OT_SelectByNoteTitle

from . interface import CUSTOM_UL_NoteList
from . interface import NK_PT_MainPanel


bl_info = {
    "name" : "NoteKeeper",
    "author" : "ThatAsherGuy",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

classes = [
    # Props
    Note,
    NoteCollection,
    # Ops
    NK_OT_AddNote,
    NK_OT_RemoveNote,
    NK_OT_SelectByNoteTitle,
    # UI
    CUSTOM_UL_NoteList,
    NK_PT_MainPanel,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Object.notes = PointerProperty(type=NoteCollection)


def unregister():

    del bpy.types.object.notes

    for cls in classes:
        bpy.utils.unregister_class(cls)


    
