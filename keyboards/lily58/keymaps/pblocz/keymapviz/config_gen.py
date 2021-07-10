#%%

from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS


kbd = KeyboardLayoutUS(None)


# %%

from enum import Enum, auto

class KCEnums(Enum):
    # def _generate_next_value_(name, start, count, last):
    #     return last + 1

    KC_NO = 0
    KC_ROLL_OVER = auto()
    KC_POST_FAIL = auto()
    KC_UNDEFINED = auto()
    KC_A = auto()
    KC_B = auto()
    KC_C = auto()
    KC_D = auto()
    KC_E = auto()
    KC_F = auto()
    KC_G = auto()
    KC_H = auto()
    KC_I = auto()
    KC_J = auto()
    KC_K = auto()
    KC_L = auto()
    KC_M = auto()
    KC_N = auto()
    KC_O = auto()
    KC_P = auto()
    KC_Q = auto()
    KC_R = auto()
    KC_S = auto()
    KC_T = auto()
    KC_U = auto()
    KC_V = auto()
    KC_W = auto()
    KC_X = auto()
    KC_Y = auto()
    KC_Z = auto()
    KC_1 = auto()
    KC_2 = auto()
    KC_3 = auto()
    KC_4 = auto()
    KC_5 = auto()
    KC_6 = auto()
    KC_7 = auto()
    KC_8 = auto()
    KC_9 = auto()
    KC_0 = auto()
    KC_ENTER = auto()
    KC_ESCAPE = auto()
    KC_BSPACE = auto()
    KC_TAB = auto()
    KC_SPACE = auto()
    KC_MINUS = auto()
    KC_EQUAL = auto()
    KC_LBRACKET = auto()
    KC_RBRACKET  = auto()
    KC_BSLASH = auto()
    KC_NONUS_HASH = auto()
    KC_SCOLON = auto()
    KC_QUOTE = auto()
    KC_GRAVE = auto()
    KC_COMMA = auto()
    KC_DOT = auto()
    KC_SLASH = auto()
    KC_CAPSLOCK = auto()
    KC_F1 = auto()
    KC_F2 = auto()
    KC_F3 = auto()
    KC_F4 = auto()
    KC_F5 = auto()
    KC_F6 = auto()
    KC_F7  = auto()
    KC_F8 = auto()
    KC_F9 = auto()
    KC_F10 = auto()
    KC_F11 = auto()
    KC_F12 = auto()
    KC_PSCREEN = auto()
    KC_SCROLLLOCK = auto()
    KC_PAUSE = auto()
    KC_INSERT = auto()
    KC_HOME = auto()
    KC_PGUP = auto()
    KC_DELETE = auto()
    KC_END = auto()
    KC_PGDOWN = auto()
    KC_RIGHT = auto()
    KC_LEFT  = auto()
    KC_DOWN = auto()
    KC_UP = auto()
    KC_NUMLOCK = auto()
    KC_KP_SLASH = auto()
    KC_KP_ASTERISK = auto()
    KC_KP_MINUS = auto()
    KC_KP_PLUS = auto()
    KC_KP_ENTER = auto()
    KC_KP_1 = auto()
    KC_KP_2 = auto()
    KC_KP_3 = auto()
    KC_KP_4 = auto()
    KC_KP_5 = auto()
    KC_KP_6 = auto()
    KC_KP_7 = auto()
    KC_KP_8  = auto()
    KC_KP_9 = auto()
    KC_KP_0 = auto()
    KC_KP_DOT = auto()
    KC_NONUS_BSLASH = auto()
    KC_APPLICATION = auto()
    KC_POWER = auto()
    KC_KP_EQUAL = auto()
    KC_F13 = auto()
    KC_F14 = auto()
    KC_F15 = auto()
    KC_F16 = auto()
    KC_F17 = auto()
    KC_F18 = auto()
    KC_F19 = auto()
    KC_F20 = auto()
    KC_F21  = auto()
    KC_F22 = auto()
    KC_F23 = auto()
    KC_F24 = auto()
    KC_EXECUTE = auto()
    KC_HELP = auto()
    KC_MENU = auto()
    KC_SELECT = auto()
    KC_STOP = auto()
    KC_AGAIN = auto()
    KC_UNDO = auto()
    KC_CUT = auto()
    KC_COPY = auto()
    KC_PASTE = auto()
    KC_FIND = auto()
    KC__MUTE = auto()
    KC__VOLUP  = auto()
    KC__VOLDOWN = auto()
    KC_LOCKING_CAPS = auto()
    KC_LOCKING_NUM = auto()
    KC_LOCKING_SCROLL = auto()
    KC_KP_COMMA = auto()
    KC_KP_EQUAL_AS400 = auto()
    KC_INT1 = auto()
    KC_INT2 = auto()
    KC_INT3 = auto()
    KC_INT4 = auto()
    KC_INT5 = auto()
    KC_INT6 = auto()
    KC_INT7 = auto()
    KC_INT8 = auto()
    KC_INT9 = auto()
    KC_LANG1 = auto()
    KC_LANG2 = auto()
    KC_LANG3 = auto()
    KC_LANG4 = auto()
    KC_LANG5 = auto()
    KC_LANG6 = auto()
    KC_LANG7 = auto()
    KC_LANG8 = auto()
    KC_LANG9 = auto()
    KC_ALT_ERASE = auto()
    KC_SYSREQ = auto()
    KC_CANCEL = auto()
    KC_CLEAR = auto()
    KC_PRIOR = auto()
    KC_RETURN = auto()
    KC_SEPARATOR = auto()
    KC_OUT = auto()
    KC_OPER = auto()
    KC_CLEAR_AGAIN = auto()
    KC_CRSEL = auto()
    KC_EXSEL = auto()

    # /* Modifiers */
    KC_LCTRL = 0xE0
    KC_LSHIFT = auto()
    KC_LALT = auto()
    KC_LGUI = auto()
    KC_RCTRL = auto()
    KC_RSHIFT = auto()
    KC_RALT = auto()
    KC_RGUI = auto()
# %%

synonims = {
# /* Transparent */
# "KC_TRANSPARENT": 0x01,
"KC_TRANSPARENT": "KC_TRNS",

# /* Punctuation */
"KC_ENTER": "KC_ENT",
"KC_ESCAPE": "KC_ESC",
"KC_BSPACE": "KC_BSPC",
"KC_SPACE": "KC_SPC",
"KC_MINUS": "KC_MINS",
"KC_EQUAL": "KC_EQL",
"KC_LBRACKET": "KC_LBRC",
"KC_RBRACKET": "KC_RBRC",
"KC_BSLASH": "KC_BSLS",
"KC_NONUS_HASH": "KC_NUHS",
"KC_SCOLON": "KC_SCLN",
"KC_QUOTE": "KC_QUOT",
"KC_GRAVE": "KC_GRV",
"KC_COMMA": "KC_COMM",
"KC_SLASH": "KC_SLSH",
"KC_NONUS_BSLASH": "KC_NUBS",

# /* Lock Keys */
# "KC_CAPSLOCK": "KC_CLCK",
"KC_CAPSLOCK": "KC_CAPS",
"KC_SCROLLLOCK": "KC_SLCK",
"KC_NUMLOCK": "KC_NLCK",
"KC_LOCKING_CAPS": "KC_LCAP",
"KC_LOCKING_NUM": "KC_LNUM",
"KC_LOCKING_SCROLL": "KC_LSCR",

# /* Commands */
"KC_PSCREEN": "KC_PSCR",
"KC_PAUSE": "KC_PAUS",
"KC_PAUSE": "KC_BRK",
"KC_INSERT": "KC_INS",
"KC_DELETE": "KC_DEL",
"KC_PGDOWN": "KC_PGDN",
"KC_RIGHT": "KC_RGHT",
"KC_APPLICATION": "KC_APP",
"KC_EXECUTE": "KC_EXEC",
"KC_SELECT": "KC_SLCT",
"KC_AGAIN": "KC_AGIN",
"KC_PASTE": "KC_PSTE",
"KC_ALT_ERASE": "KC_ERAS",
"KC_CLEAR": "KC_CLR",
"*/": "Keypad",
"KC_KP_SLASH": "KC_PSLS",
"KC_KP_ASTERISK": "KC_PAST",
"KC_KP_MINUS": "KC_PMNS",
"KC_KP_PLUS": "KC_PPLS",
"KC_KP_ENTER": "KC_PENT",
"KC_KP_1": "KC_P1",
"KC_KP_2": "KC_P2",
"KC_KP_3": "KC_P3",
"KC_KP_4": "KC_P4",
"KC_KP_5": "KC_P5",
"KC_KP_6": "KC_P6",
"KC_KP_7": "KC_P7",
"KC_KP_8": "KC_P8",
"KC_KP_9": "KC_P9",
"KC_KP_0": "KC_P0",
"KC_KP_DOT": "KC_PDOT",
"KC_KP_EQUAL": "KC_PEQL",
"KC_KP_COMMA": "KC_PCMM",

# /* Japanese specific */
# "KC_GRAVE": "KC_ZKHK",
# "KC_INT1": "KC_RO",
# "KC_INT2": "KC_KANA",
# "KC_INT3": "KC_JYEN",
# "KC_INT4": "KC_HENK",
# "KC_INT5": "KC_MHEN",

# # /* Korean specific */
# "KC_LANG1": "KC_HAEN",
# "KC_LANG2": "KC_HANJ",

# /* Modifiers */
"KC_LCTRL": "KC_LCTL",
"KC_LSHIFT": "KC_LSFT",
"KC_LALT": "KC_LOPT",
# "KC_LGUI": "KC_LCMD",
"KC_LGUI": "KC_LWIN",
"KC_RCTRL": "KC_RCTL",
"KC_RSHIFT": "KC_RSFT",
"KC_RALT": "KC_ALGR",
# "KC_RALT": "KC_ROPT",
# "KC_RGUI": "KC_RCMD",
"KC_RGUI": "KC_RWIN",

# /* Generic Desktop Page (0x01) */
"KC_SYSTEM_POWER": "KC_PWR",
"KC_SYSTEM_SLEEP": "KC_SLEP",
"KC_SYSTEM_WAKE": "KC_WAKE",

# /* Consumer Page (0x0C) */
"KC_AUDIO_MUTE": "KC_MUTE",
"KC_AUDIO_VOL_UP": "KC_VOLU",
"KC_AUDIO_VOL_DOWN": "KC_VOLD",
"KC_MEDIA_NEXT_TRACK": "KC_MNXT",
"KC_MEDIA_PREV_TRACK": "KC_MPRV",
"KC_MEDIA_STOP": "KC_MSTP",
"KC_MEDIA_PLAY_PAUSE": "KC_MPLY",
"KC_MEDIA_SELECT": "KC_MSEL",
"KC_MEDIA_EJECT": "KC_EJCT",
"KC_CALCULATOR": "KC_CALC",
"KC_MY_COMPUTER": "KC_MYCM",
"KC_WWW_SEARCH": "KC_WSCH",
"KC_WWW_HOME": "KC_WHOM",
"KC_WWW_BACK": "KC_WBAK",
"KC_WWW_FORWARD": "KC_WFWD",
"KC_WWW_STOP": "KC_WSTP",
"KC_WWW_REFRESH": "KC_WREF",
"KC_WWW_FAVORITES": "KC_WFAV",
"KC_MEDIA_FAST_FORWARD": "KC_MFFD",
"KC_MEDIA_REWIND": "KC_MRWD",
"KC_BRIGHTNESS_UP": "KC_BRIU",
"KC_BRIGHTNESS_DOWN": "KC_BRID",

# /* System Specific */
"KC_PAUSE": "KC_BRMU",
"KC_SCROLLLOCK": "KC_BRMD",

# /* Mouse Keys */
"KC_MS_UP": "KC_MS_U",
"KC_MS_DOWN": "KC_MS_D",
"KC_MS_LEFT": "KC_MS_L",
"KC_MS_RIGHT": "KC_MS_R",
"KC_MS_BTN1": "KC_BTN1",
"KC_MS_BTN2": "KC_BTN2",
"KC_MS_BTN3": "KC_BTN3",
"KC_MS_BTN4": "KC_BTN4",
"KC_MS_BTN5": "KC_BTN5",
"KC_MS_BTN6": "KC_BTN6",
"KC_MS_BTN7": "KC_BTN7",
"KC_MS_BTN8": "KC_BTN8",
"KC_MS_WH_UP": "KC_WH_U",
"KC_MS_WH_DOWN": "KC_WH_D",
"KC_MS_WH_LEFT": "KC_WH_L",
"KC_MS_WH_RIGHT": "KC_WH_R",
"KC_MS_ACCEL0": "KC_ACL0",
"KC_MS_ACCEL1": "KC_ACL1",
"KC_MS_ACCEL2": "KC_ACL2",
}

#%%

import string

def to_keycode(c):
    try:
        return KCEnums(kbd._char_to_keycode(c)).name
    except: pass

kctosym = {to_keycode(c): c for c in string.printable if to_keycode(c)}
# {c: KCEnums(to_keycode(c)) for c in string.printable if to_keycode(c)}

for k in list(kctosym.keys()):
    if k in synonims:
        kctosym[synonims[k]] = kctosym[k]
    
# %%
extra_mapping = {
    "KC_TILDE": '~',
    "KC_TILD": '~',
    "KC_EXCLAIM": '!',
    "KC_EXLM": '!',
    "KC_AT ": '@',
    "KC_HASH ": '#',
    "KC_DOLLAR": '$',
    "KC_DLR": '$',
    "KC_PERCENT": '%',
    "KC_PERC": '%',
    "KC_CIRCUMFLEX": '^',
    "KC_CIRC": '^',
    "KC_AMPERSAND": '&',
    "KC_AMPR": '&',
    "KC_ASTERISK": '*',
    "KC_ASTR": '*',
    "KC_LEFT_PAREN": '(',
    "KC_LPRN": '(',
    "KC_RIGHT_PAREN": ')',
    "KC_RPRN": ')',
    "KC_UNDERSCORE": '_',
    "KC_UNDS": '_',
    "KC_PLUS ": '+',
    "KC_LEFT_CURLY_BRACE": '{',
    "KC_LCBR": '{',
    "KC_RIGHT_CURLY_BRACE": '}',
    "KC_RCBR": '}',
    "KC_PIPE ": '|',
    "KC_COLON": ':',
    "KC_COLN": ':',
    "KC_DOUBLE_QUOTE": '"',
    "KC_DQUO": '"',
    "KC_DQT": '"',
    "KC_LEFT_ANGLE_BRACKET": '<',
    "KC_LABK": '<',
    "KC_LT": '<',
    "KC_RIGHT_ANGLE_BRACKET": '>',
    "KC_RABK": '>',
    "KC_GT": '>',
    "KC_QUESTION": '?', 
    "KC_QUES": '?', 
}

kctosym.update(extra_mapping)
#%%

with open("config-gen.properties", "w") as f:
    print("[legends]", file=f)
    for k, v in kctosym.items():
        print(f"{k}={v}", file=f)
# %%
