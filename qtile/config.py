from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from datetime import datetime
from typing import Optional
from libqtile.widget.textbox import TextBox
import fontawesome
import os
import psutil

mod = "mod4"

terminal = "alacritty" 

colors = {
        "red":["#eb1b1b"],
        "lightred":["#D78A8A"], 
        "white":["#FFFFFF" ],
        "dark grey":["#212121"],
        "blue":["#3E3ED1"],
        "ligth blue":["#4A4AEE"],
        "cascade0":["#581845"],
        "cascade1":["#900C3F"],
        "cascade2":["#C70039"],
        "cascade3":["#FF5733"],
        "cascade4":["#c6a309"],
        "cascade5":["#DAF7A6"],
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
    Key([mod], "f", lazy.spawn("firefox"), desc="navegador wtf"),
    Key([mod], "d", lazy.spawn("discord"), desc="discord"),
    Key([mod], "a", lazy.spawn("android-studio"), desc="android studio"),
    Key([mod], "v", lazy.spawn("code"), desc="vscode"),
    Key([mod], "s", lazy.spawn("spotify"), desc="spotify"), 
    Key([mod], "g", lazy.spawn("github-desktop"), desc="github"),
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
    layout.Columns(border_focus="#D82258",
        border_width=2,
        margin=6,
        ),
    layout.Max(
        border_focus="#D82258",
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

screens = [
    Screen(
        top=bar.Bar(
            [
               widget.GroupBox(
                   borderwidth = 8,
                   fontsize = 15,
                    padding_y = 5,
                    disable_drag = True,
                    highlight_method='block',
                    active="#CD4B4B",inactive="#FFFFFF",
                    this_current_screen_border="#A11212"),
                widget.Spacer(length=300),
                widget.WindowName(parse_text=None),
                widget.TextBox("\uf0d9",
                    fontsize = 55,
                    padding = -8,
                    foreground = colors["cascade4"]),

                widget.TextBox(
                    text='󱌢',
                    background = colors["cascade4"],
                    foreground=colors['white'],
                    fontsize=35,
                    padding=1,
                ),
                widget.TextBox("Time left to work: ",background = colors["cascade4"],padding=3),
                widget.Countdown(
                    date = datetime(2023,today.month,today.day,23,59, 20, 124297),
                    background = colors["cascade4"],
                    format = '{H}h {M}m {S}s',
                    padding=2),
                widget.TextBox("\uf0d9",
                    fontsize = 55,
                    padding = -8,
                    background = colors["cascade4"],
                    foreground = colors["cascade3"]),
                widget.TextBox(
                    text='󰻠',
                    foreground=colors['white'],
                    fontsize=40,
                    padding=3,
                    background = colors["cascade3"],
                ),
                widget.CPU(background=colors["cascade3"],format='{load_percent}%',padding=3),
                widget.TextBox("\uf0d9",
                   fontsize = 55,
                   padding = -8,
                   background = colors["cascade3"],
                    foreground = colors["cascade2"]),
                widget.TextBox(
                    text='󰍛',
                    foreground=colors['white'],
                    fontsize=40,
                    padding=1,
                    background = colors["cascade2"],
                ),
                widget.Memory(background=colors["cascade2"],padding=3),
                widget.TextBox("\uf0d9",
                               fontsize = 55,
                               padding = -8,
                               background = colors["cascade2"],
                               foreground = colors["cascade1"]),
                widget.TextBox(
                    text='',
                    foreground=colors['white'],
                    fontsize=32,
                    padding=3,
                    background = colors["cascade1"]
                ),
                widget.Clock(format="%I:%M %p",background = colors["cascade1"]),
                widget.TextBox(background = colors["cascade1"],
                    foreground = colors["cascade0"],
                    fontsize = 55,
                    text = '\uf0d9',
                    markup = True,
                    padding = -8),
                widget.TextBox(
                    background = colors["cascade0"],
                    text='',
                    foreground=colors['white'],
                    fontsize=18,
                    padding=-1,
                ),
                widget.Clock(format="%Y-%m-%d %a",background = colors["cascade0"]),
            ],
            26,
            margin = 6,
            background = "#212121",
            border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
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
            "picom --experimental-backends -b",
            "setxkbmap latam",
            "feh --bg-fill /home/yulian/.config/qtile/jwejw0cwmjca1.png",
            ] 

for i in start_up_comands:
    os.system(i)
