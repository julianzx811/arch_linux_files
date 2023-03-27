import os
import re
from datetime import datetime
from typing import Optional
from libqtile import bar, layout, widget
from libqtile.config import Click,Drag,Key, Match,Screen
from libqtile.lazy import lazy
from libqtile.widget.textbox import TextBox
#import own modules
from Colors import GetColors 
from Groups import groups
from Keys import keys
colors = GetColors()
groups = groups()
kkeys = keys() 
mod = "mod4"

today = datetime.today()

keys = kkeys 

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
        border_focus=colors["cascade3"],
        border_width=2,
        margin=11,
    ),
    layout.Max(
        border_focus=colors["cascade3"],
        border_width=2,
        margin=6,
    ),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="scientifica",
    fontsize=18,
    padding=12,
)

extension_defaults = widget_defaults.copy()


def my_func(text):
    text = text.rpartition("/")
    if text:
        text = text[-1]
    elif not text:
        text = text.rpartition("-")[-1]
    return text


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    borderwidth=8,
                    fontsize=15,
                    padding_y=5,
                    padding_x=7,
                    disable_drag=True,
                    highlight_method="block",
                    active=colors["cascade2"],
                    inactive=colors["white"],
                    this_current_screen_border=colors["cascade3"],
                ),
                widget.Spacer(length=110),
                widget.WindowName(parse_text=my_func),
                widget.TextBox(
                    "\uf0d9", fontsize=55, padding=-8, foreground=colors["cascade6"]
                ),
                widget.TextBox(
                    text="󰂅",
                    background=colors["cascade6"],
                    foreground=colors["green"],
                    fontsize=35,
                    padding=1,
                ),
                widget.Battery(battery = 0 ,
                               format = '{percent:2.0%} {hour:d}:{min:02d}',
                               update_interval=20,
                                discharge_char = 'v',
                               charge_char = '^',
                                empty_char = '',
                               full_char = '',
                                background=colors["cascade6"],
                               foreground = colors["cascade2"]
                               ),
                widget.TextBox(
                    text="󰂅",
                    background=colors["cascade6"],
                    foreground=colors["green"],
                    fontsize=35,
                    padding=1,
                ),
                widget.Battery(battery = 1 ,
                               format = '{percent:2.0%} {hour:d}:{min:02d}',
                               empty_char = '',
                               full_char = '',
                                background=colors["cascade6"],
                                foreground = colors["cascade2"]
                               ),
                widget.TextBox(
                    "\uf0d9",
                    fontsize=55,
                    padding=-8,
                    background=colors["cascade6"],
                    foreground=colors["cascade5"],
                ),
                widget.TextBox(
                    text="󰻠",
                    foreground=colors["gold"],
                    fontsize=40,
                    padding=3,
                    background=colors["cascade5"],
                ),
                widget.CPU(
                    background=colors["cascade5"], 
                    format="{load_percent}%", 
                    padding=3,
                    foreground = colors["cascade2"]
                ),
                widget.TextBox(
                    "\uf0d9",
                    fontsize=55,
                    padding=-8,
                    background=colors["cascade5"],
                    foreground=colors["cascade4"],
                ),
                widget.TextBox(
                    text="󰍛",
                    foreground=colors["white"],
                    fontsize=40,
                    padding=1,
                    background=colors["cascade4"],
                ),
                widget.Memory(background=colors["cascade4"], padding=3),
                widget.TextBox(
                    "\uf0d9",
                    fontsize=55,
                    padding=-8,
                    background=colors["cascade4"],
                    foreground=colors["cascade3"],
                ),
                widget.TextBox(
                    text="",
                    foreground=colors["white"],
                    fontsize=18,
                    padding=3,
                    background=colors["cascade3"],
                ),
                widget.Clock(format="%I:%M %p", background=colors["cascade3"]),
                widget.TextBox(
                    background=colors["cascade3"],
                    foreground=colors["cascade2"],
                    fontsize=55,
                    text="\uf0d9",
                    markup=True,
                    padding=-8,
                ),
                widget.TextBox(
                    background=colors["cascade2"],
                    text="",
                    foreground=colors["white"],
                    fontsize=17,
                    padding=-1,
                ),
                widget.Clock(format="%Y-%m-%d %a", background=colors["cascade2"]),
                widget.TextBox(
                    background=colors["cascade2"],
                    foreground=colors["cascade1"],
                    fontsize=55,
                    text="\uf0d9",
                    markup=True,
                    padding=-8,
                ),
                widget.TextBox(
                    background=colors["cascade1"],
                    text="",
                    foreground=colors["white"],
                    fontsize=26,
                ),
            ],
            26,
            margin=10,
            background=colors["background"],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

start_up_comands = [
    "picom --experimental-backends -b",
    "setxkbmap latam",
    "feh --bg-fill /home/yulian/.config/qtile/6zsqbsxu5nka1.jpg",
]

for i in start_up_comands:
    os.system(i)
