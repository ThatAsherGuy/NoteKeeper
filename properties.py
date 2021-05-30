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
from bpy.types import PropertyGroup
from bpy.props import (
    CollectionProperty,
    EnumProperty,
    FloatVectorProperty,
    BoolProperty,
    BoolVectorProperty,
    IntProperty,
    IntVectorProperty,
    StringProperty,
    PointerProperty,
    FloatProperty,
)

class Note(PropertyGroup):
    title: StringProperty(
        name="Note Title",
        default="",
        subtype='FILE_NAME'
    )

    text: StringProperty(
        name="Note Text",
        default=""
    )

    tags: StringProperty(
        name="Tags",
        default=""
    )


class NoteCollection(PropertyGroup):

    notes: CollectionProperty(
        type=Note,
        name="Object Notes"
    )

    active_index: IntProperty(
        name="Active Index",
        default=0
    )

    tags: StringProperty(
        name="Tags",
        default=""
    )