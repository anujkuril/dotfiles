from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import subprocess
import os
from libqtile import hook
# import dbus


#colours
colors = []
# cache='/home/ak/.cache/wal/colors'
cache='/home/ak/.config/qtile/colors/catppuccinMocha'
# cache='/home/ak/.config/qtile/colors/tokyonight'
# cache='/home/ak/.config/qtile/colors/dracula'
def load_colors(cache):
    with open(cache, 'r') as file:
        for i in range(15):
            colors.append(file.readline().strip())
    colors.append('#ffffff')
    lazy.reload()
load_colors(cache)


# widget_defaults = dict(
#     font="JetBrainsMono Nerd Font Bold",
#     fontsize=10,
#     padding=3,
#     background=colors[0],
# )
# extension_defaults = widget_defaults.copy()


main_bar=bar.Bar(
    [
        widget.TextBox(
            fmt = "",
            foreground = colors[8],
            padding = 10,
            fontsize = 14,
        ),

        widget.Spacer(length=10),
        widget.GroupBox(
            # font = 'Symbols Nerd Font Mono',
            fontsize = 14,
            highlight_method = "text",
            urgent_alert_method = "text",
            block_highlight_text_color = colors[1],
            this_current_screen_border = colors[1], 
            inactive = colors[0],
            active = colors[4],
            hide_unused = True,
            spacing = 12,

            ),

        widget.Spacer(length=10),

        widget.CurrentLayout(),
        widget.CurrentLayoutIcon(),
        widget.Spacer(length=10),

        widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            ),
        widget.AGroupBox(
            padding=12,
            border=colors[0],
            ),

        widget.WindowName(
            ),
        

        widget.WidgetBox(
            text_closed = "",
            text_open = "",
            close_button_location="right",
            fontsize = 25,
            foreground = colors[8],
            widgets=[
            widget.TextBox(text="",fontsize=30,),
            widget.Memory(),
        ]
        ),

        # widget.Mpd2(
        #         status_format='{play_status}/{title}',
        #         max_chars=10,
        #         ),

        # widget.GenPollText(
        #         update_interval = 60,
        #         padding_x = 5,
        #         func = lambda : subprocess.check_output("/home/ak/.config/qtile/autostart/uptime").decode("utf-8"),
        #         ),

        widget.Spacer(length=20),


        widget.Wlan(
            format=' {essid}',
            disconnected_message = "󰖪",
            foreground=colors[6],
        ),
        widget.Net(
            format='{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}',
            foreground=colors[6],
        ),

        widget.Spacer(length=20),


        widget.Volume(
            fmt="  {}",
            foreground=colors[3],
            ),

        widget.Spacer(length=20),

        
        widget.Clock(
            format="  %a %I:%M %p",
            foreground=colors[4],
        ),

        widget.Spacer(length=20),
 
        widget.Battery(
            foreground=colors[5],
            charge_char = "󰢞",
            discharge_char=" ",
            empty_char = "󰢟",
            full_char = "󰁹",
            format="{char} {percent:2.0%}",
            low_background=colors[1],
            low_foreground=colors[0],
            notify_below = 20,
            margin=5,
            update_interval = 1,
            ),

        widget.Spacer(length=20),

        widget.ThermalSensor(
            fmt=" {}",
            foreground=colors[2],
        ),

        widget.Spacer(length=20),
        widget.Sep(),
        # widget.StatusNotifier(),
        widget.Systray(),
        widget.Sep(),
        widget.Spacer(length=20),

        widget.TextBox(
            fmt="",
        ),
        widget.Spacer(length=20),
    ],
    28,
    margin = (5,5,0,5),
)
