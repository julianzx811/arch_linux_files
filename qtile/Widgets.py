from Colors import GetColors
from libqtile import  widget

def my_func(text): 
    for string in ["Chromium", "Firefox","alacritty"]: #Add any other apps that have long names here
        if string in text:
            text = string
        else:
            text = text
    return text

def GetWidgets():
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
                widget.WindowName(parse_text=my_func),
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
                                background=colors["cascade6"],
                                foreground = colors["cascade2"]
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
                    text="󰍛",
                    foreground=colors["white"],
                    fontsize=40,
                    padding=1,
                    background=colors["cascade4"],
                ),
                widget.Memory(background=colors["cascade4"], padding=3),
                widget.TextBox(
                    text="",
                    foreground=colors["white"],
                    fontsize=18,
                    padding=3,
                    background=colors["cascade3"],
                ),
                widget.Clock(format="%I:%M %p", background=colors["cascade3"]),
                widget.TextBox(
                    background=colors["cascade2"],
                    text="",
                    foreground=colors["white"],
                    fontsize=21,
                    padding=5,
                ),
                widget.Clock(format="%Y-%m-%d %a", background=colors["cascade2"]),
                widget.TextBox(
                    background=colors["cascade1"],
                    text="",
                    foreground=colors["white"],
                    fontsize=26,
                ),
            ]
    return widgets
