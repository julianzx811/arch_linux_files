from Colors import GetColors
from libqtile import  widget

def widgets():
    colors = GetColors()
    widgets = [
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
                widget.Spacer(length=120),
                widget.WindowName(),
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
            ]
    return widgets
