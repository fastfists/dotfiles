from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.lazy import lazy
from libqtile import layout, bar, widget, hook
from os import getenv

from typing import List  # noqa: F401

mod = "mod4"
alt = "mod1"

terminal = getenv("TERMINAL")
fileManager = getenv("FILE")
browser = getenv("BROWSER")
lazy.spawn("startup &")

keys = [
    ## Settigs up movement 
    Key([mod], "k", lazy.layout.up(), desc="Switch focus up"),
    Key([mod], "j", lazy.layout.down(), desc="Switch focus down"),

    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),

    Key([mod], "space", lazy.spawn("rofi -show drun"), desc="Run rofi"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle split"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Run terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc=""),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Close a window"),

    Key([mod, alt], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, alt], "q", lazy.shutdown(), desc="Quit Qtile"),
    
    # Media 
    Key([], "XF86AudioRaiseVolume", lazy.spawn("lmc up 5"), desc="Increase Volume by 5"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("lmc down 5"), desc="Decrease Volume by 5"),
    Key([], "XF86AudioMute", lazy.spawn("lmc toggle"), desc="Toggle mute"),
    
    # Screencapture

    
    Key([], "Print", lazy.spawn("maimpick"), desc="Screenshot"), 
    # Key(["shift" ], "Print", lazy.spawn("maimpick"), desc="pick screenshot type"), 
    # Key(["super"], "Print", lazy.spawn("dmenurecord"), desc="record audio or video; del: kill recording"), 
    # Key(["super"], "Delete", lazy.spawn("dmenurecord kill && notify-send \"recording ended\" "), desc="kill audio recording"), 



    # Applications
    Key([mod], "r", lazy.spawn(fileManager), desc="File Manager"),
    Key([mod], "w", lazy.spawn(browser), desc="File Manager"),
]

group_names = [
        "main",
        "side",
        "d",
        "f",
        "thrash",
        "i",
        "o",
        "p",
        ]

groups = [
  Group(i) for i in group_names
]

for group, letter in zip(groups, "asdfuiop"):
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], letter, lazy.group[group.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], letter, lazy.window.togroup(group.name, switch_group=True)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

layouts = [
    layout.MonadTall(),
    layout.TreeTab(),
    layout.Max(),
    # layout.Stack(num_stacks=2),
    # Try more layouts by unleashing below layouts.
    # layout.Tile(),
    # layout.VerticalTile(),
    # layout.Matrix(),
    # layout.Bsp(),
    # layout.Columns(),
    # layout.MonadWide(),
    # layout.RatioTile(),
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=0,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.TextBox("default config", name="default"),
                widget.Systray(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
                widget.QuickExit(),
            ],
            24,
        ),
    ),
    Screen(
        bottom=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.TextBox("default config", name="default"),
                widget.Systray(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
                widget.QuickExit(),
            ],
            24,
        ),
    )
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call(["/home/samarth/.config/qtile/autostart.sh"])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
