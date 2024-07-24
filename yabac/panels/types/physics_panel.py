from yabac.panels.types import BasePanel
from pyxenoverse.bac.types.physics import Physics


class PhysicsPanel(BasePanel):
    def __init__(self, *args):
        BasePanel.__init__(self, *args)
        
        self.function_type = self.add_multiple_selection_entry(self.entry_page, 'Function Type', choices=[
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
                                                                   ("Options #4", [
                                                                       'Unk1',
                                                                       'Simulate Physics',
                                                                       'Play SCD Animations',
                                                                       'Unk4'
                                                                   ], True),
                                                               ]
                                                               )
        
        self.ean_index = self.add_num_entry(self.entry_page, 'EAN Index')
        self.u_10 = self.add_hex_entry(self.unknown_page, 'U_10')
        self.f_14 = self.add_float_entry(self.unknown_page, 'F_14')
        self.f_18 = self.add_float_entry(self.unknown_page, 'F_18')
        self.u_1c = self.add_hex_entry(self.unknown_page, 'U_1C')
