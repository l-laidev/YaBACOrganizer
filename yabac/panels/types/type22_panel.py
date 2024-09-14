from yabac.panels.types import BasePanel
from yabac.my_helpers import convert_to_px


class Type22Panel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        self.u_08 = self.add_hex_entry(self.unknown_page, 'U_08')
        self.f_0c = self.add_float_entry(self.unknown_page, 'F_0C')
        self.name = self.add_text_entry(self.entry_page, 'Name', size=(convert_to_px(300), -1))
