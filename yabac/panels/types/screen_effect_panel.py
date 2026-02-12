import wx
from yabac.panels.types import BasePanel, BONE_TYPES
from pyxenoverse.bac.types.screen_effect import ScreenEffect


class ScreenEffectPanel(BasePanel):
    def __init__(self, *args):
        BasePanel.__init__(self, *args)
        self.bpe_effect_id = self.add_unknown_num_entry(self.entry_page, 'BPE Effect Id',
                                                        knownValues=ScreenEffect.description)
        self.bone_link = self.add_single_selection_entry(self.entry_page, 'Bone Link', majorDimension=5,
                                                         choices=BONE_TYPES)
        self.screen_effect_flags = self.add_multiple_selection_entry(
            self.entry_page,
            'ScreenEffect Flags',
            majorDimension=2,
            choices=[
                ('ScreenEffect Options #1', [
                    None,
                    None,
                    None,
                    None
                ], True),
                ('ScreenEffect Options #2', [
                    None,
                    None,
                    None,
                    None
                ], True),
                ('ScreenEffect Options #3', [
                    None,
                    None,
                    None,
                    None
                ], True),
                ('ScreenEffect Options #4', [
                    'Visible For All',
                    'Disable Effect',
                    'Unknown (0x4)',
                    'Loop with Action',
                ], True)
                # ('Activation Options', {
                #     'On': 0x0,
                #     'Unknown (0x1)': 0x1,
                #     "Off? (0x2)": 0x2,
                #     'Off? (0x3)': 0x3
                # }, False)
            ]
        )

        self.u_10 = self.add_hex_entry(self.unknown_page, 'U_10')
        self.u_14 = self.add_float_entry(self.entry_page, 'X Position Offset')
        self.u_18 = self.add_float_entry(self.entry_page, 'Y Position Offset')
        self.u_1c = self.add_float_entry(self.entry_page, 'Z Position Offset')

        self.bpe_effect_id_dropdown = wx.ComboBox(self.bpe_effect_id, -1, choices=[f'[{k}] {v}' for k,v in ScreenEffect.description.items()])
        self.bpe_effect_id.GetSizer().Add(self.bpe_effect_id_dropdown, 0, wx.ALL, 10)
        self.bpe_effect_id_dropdown.Bind(wx.EVT_COMBOBOX, self.on_select)
        self.bpe_effect_id.hex_ctrl.Bind(wx.EVT_SPINCTRL, self.on_change_modif)
    
    def on_select(self, _):
        val = self.bpe_effect_id_dropdown.GetValue()
        key = val.split(' ')[0]
        key = key.split(']')[0]
        key = key[1:]
        self.bpe_effect_id.SetValue(int(key))
    
    def on_change_modif(self, value):
        self.bpe_effect_id.on_change(value)
        
        key = self.bpe_effect_id.hex_ctrl.GetValue()
        val = self.bpe_effect_id.known_values.get(key, 'Unknown')
        
        self.bpe_effect_id_dropdown.SetValue(f'[{key}] {val}')