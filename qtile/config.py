from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import subprocess
import os
from libqtile import hook
from libqtile.backend.wayland import InputConfig
from libqtile import qtile
from mybar import main_bar


if qtile.core.name == "x11":
    @hook.subscribe.startup_once 
    def autostart():
        home = os.path.expanduser("~/.config/qtile/autostart/x11autostart.sh")
        subprocess.run([home])
elif qtile.core.name == "wayland":
    @hook.subscribe.startup_once
    def autostart():
        home = os.path.expanduser("~/.config/qtile/autostart/waylandautostart.sh")
        subprocess.run([home])

# functions + lazy finctions 
def sc(sc):
    os.system("scrot ~/Pictures/Screenshots/$(date +%F-%H_%M_%S).jpg -e 'copyq write image/jpeg - < $f'"),
    # os.system('scrot ~/Pictures/Screenshots/$(date +%F-%H_%M_%S).jpg'),
    os.system("notify-send 'screenshot taken and copied to clipboard'"),
def ss(ss):
    # os.system('scrot -s ~/Pictures/Screenshots/$(date +%F-%H_%M_%S).jpg'),
    os.system("scrot -s ~/Pictures/Screenshots/$(date +%F-%H_%M_%S).jpg -e 'copyq write image/jpeg - < $f'"),
    os.system("notify-send 'screenshot taken and copied to clipboard'"),
@lazy.function 
def minimize_all(qtile):
    for win in qtile.current_group.windows:
        if hasattr(win, "toggle_minimize"):
            win.toggle_minimize()



mod = "mod4"
mod1 = "control"
terminal = "kitty"

keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Key([mod], "n", lazy.layout.reset(), desc="Reset all window sizes"),

    ######monadtall##########
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "control"], "i", lazy.layout.grow()),
    Key([mod,"control"], "m", lazy.layout.shrink()),
    Key([mod,"control"], "n", lazy.layout.reset()),
    Key([mod,"control"], "o", lazy.layout.maximize()),
    Key([mod, "shift"], "space", lazy.layout.flip()),
    # Key([mod],"m",lazy.layout.maximize()),


    ##########column##################
    # Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    # Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    # Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    # Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    # Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    # Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    # Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    # Key([mod, "shift", "control"], "h", lazy.layout.swap_column_left()),
    # Key([mod, "shift", "control"], "l", lazy.layout.swap_column_right()),
    # Key([mod], "Return", lazy.layout.toggle_split()),
    # Key([mod], "n", lazy.layout.normalize()),

    # Key([mod, "shift"],"Return",lazy.layout.toggle_split(),desc="Toggle between split and unsplit sides of stack",),
    

    #general functions
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod,"shift"],"r",lazy.restart(),desc="Restart Qtile. In X11, it won't close your windows."),

    #groups functions
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "bracketright",lazy.screen.next_group(),desc="Move to the group on the right"),
    Key([mod],"bracketleft",lazy.screen.prev_group(),desc="Move to the group on the left"),
    Key([mod1],"Tab",lazy.screen.toggle_group(),desc="Move to the last visited group"),
    Key([mod],"space",lazy.group.next_window()),
    
    #window functions
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    # Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod], "f",lazy.window.toggle_floating(),desc="Put the focused window to/from floating mode"),
    Key([mod], "m",lazy.window.toggle_fullscreen(),desc="Put the focused window to/from fullscreen mode"),
    Key([mod],"v",lazy.window.bring_to_front(),desc="Bring window above all other windows. Ignores kept_above priority."),
    Key([mod,"shift"], "n", minimize_all(), desc="Toggle minimization on all window"),
    Key([mod], "n",lazy.window.toggle_minimize()),

    #volumecontrol
    Key([], "XF86AudioMute" , lazy.spawn("amixer set Master toggle")),
    Key([], "XF86AudioLowerVolume" , lazy.spawn("amixer set Master 10%-")),
    Key([], "XF86AudioRaiseVolume" , lazy.spawn("amixer set Master 5%+")),

    #brightness
    Key([], "XF86MonBrightnessUp" , lazy.spawn("brightnessctl set +1%")),
    Key([], "XF86MonBrightnessDown" , lazy.spawn("brightnessctl set 1%-")),


    #applicaion launcher + essentials
    KeyChord([mod], "a", [
    Key([], "b", lazy.spawn("firefox")),
    Key([], "o", lazy.spawn("kitty -e yazi")),
    Key([], "t", lazy.spawn("thunar")),
    Key([], "n", lazy.spawn("flatpak run io.appflowy.AppFlowy")),
    Key([], "j", lazy.spawn("flatpak run org.signal.Signal")),
    ]),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Spawn a command using a prompt widget"),
    Key([mod], "d", lazy.spawn("rofi -show run")),
    Key([mod], "w", lazy.spawn("rofi -show window")),

    #screenlock
    Key([mod], "x", lazy.spawn("betterlockscreen -l")),
    Key([mod], "c", lazy.spawn("kitty -e nvim /home/ak/.config/qtile/config.py")),

    # SCREENSHOTS
    # Key([], "Print", lazy.spawn("scrot ~/Pictures/Screenshots/$(date +%F-%H_%M_%S).jpg")),
    Key([], "Print", lazy.function(sc)),
    Key([mod],"Print", lazy.function(ss)),

    
]


#colours

colors = []
cache='/home/ak/.config/qtile/colors/catppuccinMocha'
def load_colors(cache):
    with open(cache, 'r') as file:
        for i in range(8):
            colors.append(file.readline().strip())
    colors.append('#ffffff')
    lazy.reload()
load_colors(cache)


groups = []
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9","0","minus"]
#group_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9",]
group_labels = ["","","","","󰝤","󰭻","","","󰎚","󰞦",""]

# Add group names, labels, and default layouts to the groups object.
for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            # layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))
for i in groups:
    keys.extend(
        [
            # mod1 + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

# Define scratchpads
groups.append(ScratchPad("scratchpad", [
    DropDown("term", "kitty --class=scratch", width=0.8, height=0.8,x=0.1,y=0.1, opacity=1),
    DropDown("yazi", "kitty --class=ranger -e yazi", width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),
    DropDown("ncmpcpp", "kitty -e ncmpcpp", width=0.5,height=0.4,x=0.25),
    DropDown("keepass", "keepassxc",width=0.4,height=0.8,x=0.58,y=0.1),
    DropDown("rightterm", "kitty", width=0.5,height=0.98,y=0.01,x=0.49)

]))
# Scratchpad keybindings
keys.extend([
    Key([mod], "t", lazy.group['scratchpad'].dropdown_toggle('term')),
    Key([mod], "y", lazy.group['scratchpad'].dropdown_toggle('yazi')),
    Key([mod], "p", lazy.group['scratchpad'].dropdown_toggle('ncmpcpp')),
    Key([mod,"shift"], "t", lazy.group['scratchpad'].dropdown_toggle('rightterm')),
    Key([mod], "g", lazy.group['scratchpad'].dropdown_toggle('keepass')),
])

# for key, x, y in [("Left", -10, 0), 
#                   ("Right", 10, 0), 
#                   ("Up", 0, -10),
#                   ("Down", 0, 10)]:
#     keys.append(Key([mod, "control"], key, lazy.window.move_floating(x, y)))
#     keys.append(Key([mod, "shift"], key, lazy.window.resize_floating(x, y)))


# Define layouts and layout themes
layout_theme = {
        "margin":15,
        "border_width": 2,
        "border_focus": colors[4],
        "border_normal": colors[0],
    }

layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    # layout.Columns(**layout_theme),
    layout.Floating(
        border_focus=colors[3],
        ),
    layout.TreeTab(**layout_theme),
]

widget_defaults = dict(
    font="JetBrainsMono Nerd Font ExtraBold",
    fontsize=12,
    padding=3,
    background = colors[0],
    
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=main_bar,
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
bring_front_click = True
cursor_warp = False

# @hook.subscribe.client_new
# def new_clinet(client):
#     if "pavucontrol" in client.get_wm_class():
#         client.set_position_floating(200,200)
# def floating_size_hints(window):
    # hints = window.window.get_wm_normal_hints()
    # if hints and 0 < hints['max_width'] < 1000:
    #     window.floating = True

floating_layout = layout.Floating(border_focus=colors[1],
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="Signal"),
        # Match(wm_class="keepassxc"),
        Match(wm_class="pavucontrol"),
        Match(wm_class="ghidra-Ghidra"),
        Match(wm_class="pinentry-gtk-2"),
    ]
)

##disable float 
@hook.subscribe.client_new
def disable_floating(window):
    rules = [
        Match(wm_class="mpv")
    ]

    if any(window.match(rule) for rule in rules):
        window.togroup(qtile.current_group.name)
        window.cmd_disable_floating()

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = {
        '1267:12637:ELAN0729:00 04F3:315D Touchpad': InputConfig(
            left_handed=True,
            accel_profile="adaptive",
            tap=True,
            pointer_accel=0.5,),
}

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.

##qtile behavior
wmname = "qtile"
