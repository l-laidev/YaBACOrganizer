from yabac.panels.types import BasePanel
from pyxenoverse.bac.types.physics import Physics


class PhysicsPanel(BasePanel):
    def __init__(self, *args):
        BasePanel.__init__(self, *args)
        
        self.function_type_A = self.add_multiple_selection_entry(self.entry_page, 'Function Type A', majorDimension=3, choices=[
                                                                   ("Options #1", [
                                                                       'Unk1',
                                                                       'Unk2',
                                                                       'Unk3',
                                                                       'Unk4'
                                                                   ], True),
                                                                   ("Options #2", [
                                                                       'Unk1',
                                                                       'Unk2',
                                                                       'Unk3',
                                                                       'Unk4'
                                                                   ], True),
                                                                   ("Options #3", [
                                                                       'Unk1',
                                                                       'Unk2',
                                                                       'Unk3',
                                                                       'Unk4'
                                                                   ], True),
                                                                   ("Options #4", {
                                                                       'Unk1': 0x0,
                                                                       'Simulate Physics': 0x1,
                                                                       'Unk2': 0x2,
                                                                       'Play SCD Animations': 0x3,
                                                                       'Unk3': 0x4,
                                                                       'Unk4': 0x5,
                                                                       'Unk5': 0x6,
                                                                       'Unk6': 0x7,
                                                                       'Unk7': 0x8,
                                                                       'Unk8': 0x9,
                                                                       'Unk9': 0xa,
                                                                       'Unk10': 0xb,
                                                                       'Unk11': 0xc,
                                                                       'Unk12': 0xd,
                                                                       'Unk13': 0xe,
                                                                       'Unk14': 0xf,
                                                                   },
                                                                   False),
                                                               ]
                                                               )
        self.function_type_B = self.add_multiple_selection_entry(self.entry_page, 'Funtion Type B', choices=[
            ('', [], True),
            ('', [], True),
            ('', [], True),
            ('', [], True),
        ])
        
        self.ean_index = self.add_num_entry(self.entry_page, 'EAN Index For "Play SCD Animations"')
        self.u_10 = self.add_hex_entry(self.unknown_page, 'U_10')
        self.f_14 = self.add_float_entry(self.unknown_page, 'F_14')
        self.f_18 = self.add_float_entry(self.unknown_page, 'F_18')
        self.u_1c = self.add_hex_entry(self.unknown_page, 'U_1C')
