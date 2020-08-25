from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.lazy import lazy

from libqtile import layout, bar, widget, hook
from os import getenv
import os

from typing import List  # noqa: F401

mod = "mod4"
alt = "mod1"

terminal = getenv("TERMINAL")
fileManager = getenv("FILE")
browser = getenv("BROWSER")
lazy.spawn("startup &")

keys = [
    ## Settigs up movement 
    Key([mod], "h", lazy.layout.shrink(), desc="Shrink size of window"),
    Key([mod], "k", lazy.layout.up(), desc="Switch focus up"),
    Key([mod], "j", lazy.layout.down(), desc="Switch focus down"),
    Key([mod], "l", lazy.layout.grow(), desc="Grow size of window"),

    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),

    # Key([mod], "leftanglebracket", window_to_next_screen(), desc="Move window down"),
    # Key([mod], "rightanglebracket", window_to_prev_screen(), desc="Move window down"),

    Key([mod], "space", lazy.spawn("rofi -show drun"), desc="Run rofi"),

    Key([mod], "period", lazy.next_screen(), desc='Move focus to next monitor'),
    Key([mod], "comma", lazy.prev_screen(), desc='Move focus to prev monitor'),

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
    Key([mod], "r", lazy.spawn(f"{terminal} -e {fileManager}"), desc="File Manager"),
    Key([mod], "w", lazy.spawn(browser), desc="Browser"),
]


############ Special Functions ############


def window_to_prev_screen():
    @lazy.function
    def __inner(qtile):
        i = qtile.screens.index(qtile.current_screen)

        if qtile.current_window and i != 0:
            group = qtile.screens[i - 1].group.name
            qtile.current_window.togroup(group)
    return __inner

def window_to_next_screen():
    @lazy.function
    def __inner(qtile):
        i = qtile.screens.index(qtile.current_screen)

        if qtile.current_window and i + 1 != len(qtile.screens):
            group = qtile.screens[i + 1].group.name
            qtile.current_window.togroup(group)
    return __inner

############
 
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
        Key([mod, "shift"], letter, lazy.window.togroup(group.name)),
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
    font='Ubantu',
    fontsize=12,
    padding=0,
)

extension_defaults = widget_defaults.copy()

# Colors
# 	"#282828", /* hard contrast: #1d2021 / soft contrast: #32302f */
# 	"#cc241d",
# 	"#98971a",
# 	"#d79921",
# 	"#458588",
# 	"#b16286",
# 	"#689d6a",
# 	"#a89984",
# 	"#928374",
# 	"#fb4934",
# 	"#b8bb26",
# 	"#fabd2f",
# 	"#83a598",
# 	"#d3869b",
# 	"#8ec07c",
# 	"#ebdbb2",

colors = [["#282828", "#282828"], # panel background
          ["#4e4e4e", "#4e4e4e"], # background for current screen tab
          ["#ebdbb2", "#ebdbb2"], # font color for group names
          ["#cc241d", "#cc241d"], # border line color for current tab
          ["#ff8700", "#ff8700"], # border line color for other tab and odd widgets
          ["#cc241d", "#cc241d"], # color for the even widgets
          ["#689d6a", "#689d6a"]] # window name

def init_widgets_list():
    widgets_list = [
              widget.Sep(
                       linewidth = 0,
                       padding = 4,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.CurrentLayoutIcon(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                       foreground = colors[0],
                       background = colors[6],
                       padding = 0,
                       scale = 0.7
                       ),
              widget.CurrentLayout(
                       foreground = colors[2],
                       background = colors[6],
                       padding = 5
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 5,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.GroupBox(
                       font = "monospace",
                       fontsize = 9,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,

                       active = colors[2],
                       inactive = colors[6],

                       rounded = False,
                       highlight_color = colors[1],
                       highlight_method = "line",

                       this_current_screen_border = colors[3],
                       other_current_screen_border = colors[4],
                       inactive_current_screen_border = colors[6],


                       this_screen_border = colors[6],
                       other_screen_border = colors[4],
                       inactive_screen_border = colors[6],

                       foreground = colors[2],
                       background = colors[0],

                       disable_drag = True,
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 20,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.WindowName(
                       foreground = colors[2],
                       background = colors[0],
                       padding = 0
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[0],
                       foreground = colors[5],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.TextBox(
                       text = " 🌡",
                       padding = 2,
                       foreground = colors[2],
                       background = colors[5],
                       fontsize = 11
                       ),
              widget.ThermalSensor(
                       foreground = colors[2],
                       background = colors[5],
                       threshold = 90,
                       padding = 5
                       ),
              widget.TextBox(
                       text='',
                       background = colors[5],
                       foreground = colors[4],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.TextBox(
                       text = " ⟳",
                       padding = 2,
                       foreground = colors[2],
                       background = colors[4],
                       fontsize = 14
                       ),
              widget.Pacman(
                       update_interval = 1800,
                       foreground = colors[2],
                       mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(terminal + ' -e sudo pacman -Syu')},
                       background = colors[4]
                       ),
              widget.TextBox(
                       text = "Updates",
                       padding = 5,
                       mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(terminal + ' -e sudo pacman -Syu')},
                       foreground = colors[2],
                       background = colors[4]
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[5],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.TextBox(
                       text = " 🖬",
                       foreground = colors[2],
                       background = colors[5],
                       padding = 0,
                       fontsize = 14
                       ),
              widget.Memory(
                       foreground = colors[2],
                       background = colors[5],
                       mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(terminal + ' -e htop')},
                       padding = 5
                       ),
              widget.TextBox(
                       text='',
                       background = colors[5],
                       foreground = colors[4],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.Net(
                       interface = "enp6s0",
                       format = '{down} ↓↑ {up}',
                       foreground = colors[2],
                       background = colors[4],
                       padding = 5
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[5],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.TextBox(
                      text = " Vol:",
                       foreground = colors[2],
                       background = colors[5],
                       padding = 0
                       ),
              widget.Volume(
                       foreground = colors[2],
                       background = colors[5],
                       padding = 5
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[5],
                       foreground = colors[4],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.Clock(
                       foreground = colors[2],
                       background = colors[4],
                       format = "%A, %B %d  [ %I:%M%p ]"
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 10,
                       foreground = colors[0],
                       background = colors[4]
                       ),
              widget.Systray(
                       background = colors[4],
                       padding = 5
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 10,
                       foreground = colors[0],
                       background = colors[4]
                       ),
              ]
    return widgets_list


screens = [
    Screen(bottom=bar.Bar(
        widgets=init_widgets_list(),
        size=24,
        opacity=0.92)
        ),
    Screen(bottom=bar.Bar(
        widgets=init_widgets_list(),
        size=24,
        opacity=0.92)
        ),
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
    subprocess.call(["/home/fastfist/.scripts/wmcmds/startup"])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
