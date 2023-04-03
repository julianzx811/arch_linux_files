from libqtile.config import Key
from libqtile.lazy import lazy

def keys():
    mod = "mod4"
    terminal = "alacritty"
    keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.reset(), desc="Reset all window sizes"),
    Key([mod, "control"], "f", lazy.window.toggle_floating()),
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
    # keybinds for the programs i usualy use
    Key([mod, "control"], "f", lazy.spawn("firefox"), desc="navegador wtf"),
    Key([mod, "control"], "b", lazy.spawn("blueman-manager"), desc="bluetooth"),
    Key([mod, "control"], "a", lazy.spawn("android-studio"), desc="android studio"),
    Key([mod, "control"], "v", lazy.spawn("code"), desc="vscode"),
    Key([mod, "control"], "s", lazy.spawn("spotify"), desc="spotify"),
    Key([mod, "control"], "g", lazy.spawn("github-desktop"), desc="github"),
    Key([mod, "control"], "s", lazy.spawn("gnome-control-center "), desc="volume control"),
    Key([mod, "control"], "p", lazy.spawn("postman"), desc="postman"),
    Key(
        [mod, "shift"],
        "i",
        lazy.spawn("intellij-idea-ultimate-edition"),
        desc="everton",
    ),
    # keybinds for my work flow
]

    return keys
