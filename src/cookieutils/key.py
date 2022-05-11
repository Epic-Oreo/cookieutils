import enum
class CKey():
    """A class representing various buttons that may not correspond to
    letters. This includes modifier keys and function keys.

    The actual values for these items differ between platforms. Some platforms
    may have additional buttons, but these are guaranteed to be present
    everywhere.
    """
    #: A generic Alt key. This is a modifier.
    class alt():
        name = "alt"

    #: The left Alt key. This is a modifier.
    class alt_l():
        name = "alt_l"

    #: The right Alt key. This is a modifier.
    class alt_r():
        name = "alt_r"

    #: The AltGr key. This is a modifier.
    class alt_gr():
        name = "alt_gr"

    #: The Backspace key.
    class backspace():
        name = "backspace"

    #: The CapsLock key.
    class caps_lock():
        name = "caps_lock"

    #: A generic command button. On *PC* platforms, this corresponds to the
    #: Super key or Windows key, and on *Mac* it corresponds to the Command
    #: key. This may be a modifier.
    class cmd():
        name = "cmd"

    #: The left command button. On *PC* platforms, this corresponds to the
    #: Super key or Windows key, and on *Mac* it corresponds to the Command
    #: key. This may be a modifier.
    class cmd_l():
        name = "cmd_l"

    #: The right command button. On *PC* platforms, this corresponds to the
    #: Super key or Windows key, and on *Mac* it corresponds to the Command
    #: key. This may be a modifier.
    class cmd_r():
        name = "cmd_r"

    #: A generic Ctrl key. This is a modifier.
    class ctrl():
        name = "ctrl"

    #: The left Ctrl key. This is a modifier.
    class ctrl_l():
        name = "ctrl_l"

    #: The right Ctrl key. This is a modifier.
    class ctrl_r():
        name = "ctrl_r"

    #: The Delete key.
    class delete():
        name = "delete"

    #: A down arrow key.
    class down():
        name = "down"

    #: The End key.
    class end():
        name = "end"

    #: The Enter or Return key.
    class enter():
        name = "enter"

    #: The Esc key.
    class esc():
        name = "esc"

    #: The function keys. F1 to F20 are defined.
    class f1():
        name = "f1"
    class f2():
        name = "f2"
    class f3():
        name = "f3"
    class f4():
        name = "f4"
    class f5():
        name = "f5"
    class f6():
        name = "f6"
    class f7():
        name = "f7"
    class f8():
        name = "f8"
    class f9():
        name = "f9"
    class f10():
        name = "f10"
    class f11():
        name = "f11"
    class f12():
        name = "f12"
    class f13():
        name = "f13"
    class f14():
        name = "f14"
    class f15():
        name = "f15"
    class f16():
        name = "f16"
    class f17():
        name = "f17"
    class f18():
        name = "f18"
    class f19():
        name = "f19"
    class f20():
        name = "f20"

    #: The Home key.
    class home():
        name = "home"

    #: A left arrow key.
    class left():
        name = "left"

    #: The PageDown key.
    class page_down():
        name = "page_down"

    #: The PageUp key.
    class page_up():
        name = "page_up"

    #: A right arrow key.
    class right():
        name = "right"

    #: A generic Shift key. This is a modifier.
    class shift():
        name = "shift"

    #: The left Shift key. This is a modifier.
    class shift_l():
        name = "shift_l"

    #: The right Shift key. This is a modifier.
    class shift_r():
        name = "shift_r"

    #: The Space key.
    class space():
        name = "space"

    #: The Tab key.
    class tab():
        name = "tab"

    #: An up arrow key.
    class up():
        name = "up"

    #: The play/pause toggle.
    class media_play_pause():
        name = "media_play_pause"

    #: The volume mute button.
    class media_volume_mute():
        name = "media_volume_mute"

    #: The volume down button.
    class media_volume_down():
        name = "media_volume_down"

    #: The volume up button.
    class media_volume_up():
        name = "media_volume_up"

    #: The previous track button.
    class media_previous():
        name = "media_previous"

    #: The next track button.
    class media_next():
        name = "media_next"

    #: The Insert key. This may be undefined for some platforms.
    class insert():
        name = "insert"

    #: The Menu key. This may be undefined for some platforms.
    class menu():
        name = "menu"

    #: The NumLock key. This may be undefined for some platforms.
    class num_lock():
        name = "num_lock"

    #: The Pause/Break key. This may be undefined for some platforms.
    class pause():
        name = "pause"

    #: The PrintScreen key. This may be undefined for some platforms.
    class print_screen():
        name = "print_screen"

    #: The ScrollLock key. This may be undefined for some platforms.
    class scroll_lock():
        name = "scroll_lock"