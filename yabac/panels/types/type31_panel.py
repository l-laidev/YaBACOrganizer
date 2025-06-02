from yabac.panels.types import BasePanel


class Type31Panel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)

        self.u_12 = self.add_hex_entry(self.unknown_page, 'U_12')
        self.u_16 = self.add_hex_entry(self.unknown_page, 'U_16')
        self.u_18 = self.add_hex_entry(self.unknown_page, 'U_18')
        self.u_20 = self.add_hex_entry(self.unknown_page, 'U_20')
        self.u_08 = self.add_hex_entry(self.unknown_page, 'U_08')
        self.u_22 = self.add_hex_entry(self.unknown_page, 'U_22')
        self.f_24 = self.add_float_entry(self.unknown_page, 'F_24')
        self.f_28 = self.add_float_entry(self.unknown_page, 'F_28')
        self.u_32 = self.add_hex_entry(self.unknown_page, 'U_32')
        self.u_36 = self.add_hex_entry(self.unknown_page, 'U_36')
        self.u_40 = self.add_hex_entry(self.unknown_page, 'U_40')
        self.u_44 = self.add_hex_entry(self.unknown_page, 'U_44')
        self.u_48 = self.add_hex_entry(self.unknown_page, 'U_48')
        self.u_52 = self.add_hex_entry(self.unknown_page, 'U_52')
        self.u_56 = self.add_hex_entry(self.unknown_page, 'U_56')
        self.u_60 = self.add_hex_entry(self.unknown_page, 'U_60')




