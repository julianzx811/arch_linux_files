from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from datetime import datetime
from typing import Optional
from libqtile.widget.textbox import TextBox
import re
import fontawesome
import os
import psutil

mod = "mod4"

terminal = "alacritty" 

colors = {
        "background":["#222831"],
        "white":["#FFFFFF"],
        "cascade1":["#36574C"],
        "cascade2":["#416B5D"],
        "cascade3":["#61876E"],
        "cascade4":["#6C957B"],
        "cascade5":["#A0B587"],
        "cascade6":["#ADC493"],
        }

groups = [
    Group("1", label=""),
    Group("2", label=""),
    Group("3", label=""),
    Group("4", label="󰓇"),
    Group("5", label="󰙯"),
]

today = datetime.today()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod,"control"], "f", lazy.window.toggle_floating()),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    #keybinds for the programs i usualy use 
    Key([mod ,"shift"], "f", lazy.spawn("firefox"), desc="navegador wtf"),
    Key([mod,"shift"], "d", lazy.spawn("discord"), desc="discord"),
    Key([mod,"shift"], "a", lazy.spawn("android-studio"), desc="android studio"),
    Key([mod,"shift"], "v", lazy.spawn("code"), desc="vscode"),
    Key([mod,"shift"], "s", lazy.spawn("spotify"), desc="spotify"), 
    Key([mod,"shift"], "g", lazy.spawn("github-desktop"), desc="github"),
    Key([mod,"shift"], "e", lazy.spawn("Evernote"), desc="everton"),
    #keybinds for my work flow 
    Key([mod, "control"], "f", lazy.spawn("xd"), desc="my workflow"),
]



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
    layout.Columns(border_focus=colors["cascade3"],
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
    font="sans",
    fontsize=12,
    padding=10,
)

extension_defaults = widget_defaults.copy()

def my_func(text):
    text = text.rpartition('/')
    if(text):
        text = text[-1]
    elif not text: 
        text = text.rpartition('-')[-1]
    return text 

screens = [
    Screen(
        top=bar.Bar(
            [
               widget.GroupBox(
                    borderwidth = 8,
                    fontsize = 15,
                    padding_y = 5,
                    padding_x= 7,
                    disable_drag = True,
                    highlight_method='block',
                    active=colors["cascade2"],
                    inactive=colors["white"],
                    this_current_screen_border=colors["cascade3"]),
                widget.Spacer(length=350),
                widget.WindowName(parse_text=my_func),
                widget.TextBox("\uf0d9",
                    fontsize = 55,
                    padding = -8,
                    foreground = colors["cascade6"]),

                widget.TextBox(
                    text='󱌢',
                    background = colors["cascade6"],
                    foreground=colors['white'],
                    fontsize=35,
                    padding=1,
                ),
                widget.TextBox("Time left to work: ",background = colors["cascade6"],padding=3),
                widget.Countdown(
                    date = datetime(2023,today.month,today.day,23,59, 20, 124297),
                    background = colors["cascade6"],
                    format = '{H}h {M}m {S}s',
                    padding=2),
                widget.TextBox("\uf0d9",
                    fontsize = 55,
                    padding = -8,
                    background = colors["cascade6"],
                    foreground = colors["cascade5"]),
                widget.TextBox(
                    text='󰻠',
                    foreground=colors['white'],
                    fontsize=40,
                    padding=3,
                    background = colors["cascade5"],
                ),
                widget.CPU(background=colors["cascade5"],format='{load_percent}%',padding=3),
                widget.TextBox("\uf0d9",
                   fontsize = 55,
                   padding = -8,
                   background = colors["cascade5"],
                    foreground = colors["cascade4"]),
                widget.TextBox(
                    text='󰍛',
                    foreground=colors['white'],
                    fontsize=40,
                    padding=1,
                    background = colors["cascade4"],
                ),
                widget.Memory(background=colors["cascade4"],padding=3),
                widget.TextBox("\uf0d9",
                               fontsize = 55,
                               padding = -8,
                               background = colors["cascade4"],
                               foreground = colors["cascade3"]),
                widget.TextBox(
                    text='',
                    foreground=colors['white'],
                    fontsize=18,
                    padding=3,
                    background = colors["cascade3"]
                ),
            widget.Clock(format="%I:%M %p",background = colors["cascade3"]),
            widget.TextBox(background = colors["cascade3"],
                foreground = colors["cascade2"],
                fontsize = 55,
                text = '\uf0d9',
                markup = True,
                padding = -8),
            widget.TextBox(
                background = colors["cascade2"],
                text='',
                foreground=colors['white'],
                fontsize=17,
                padding=-1,
            ),
            widget.Clock(format="%Y-%m-%d %a",background = colors["cascade2"]),
            widget.TextBox(background = colors["cascade2"],
                foreground = colors["cascade1"],
                fontsize = 55,
                text = '\uf0d9',
                markup = True,
                padding = -8),

            widget.TextBox(
                background = colors["cascade1"],
                    text='',
                    foreground=colors['white'],
                    fontsize=26,
                ),
            ],
            26,
            margin = 10,
            background = colors["background"],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
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
            "setxkbmap latam",
            "feh --bg-fill /home/yulian/.config/qtile/s3p0kt49w0ga1.jpg",
            "picom --experimental-backends -b",
            ] 

for i in start_up_comands:
    os.system(i)
