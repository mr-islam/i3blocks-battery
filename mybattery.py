#!/usr/bin/env python3
#
# A battery indicator blocklet script for i3blocks

from subprocess import check_output, Popen
import os

# inspiration from https://www.reddit.com/r/i3wm/comments/3tt8xf/i3blocks_new_blocks_for_everyone/cx9c7k9

def image(percent):
    if percent < 20:
        return ""
    elif percent < 40:
        return ""
    elif percent < 60:
        return ""
    elif percent < 85:
        return ""
    else: 
        return ""

status = check_output(['acpi'], universal_newlines=True)
state = status.split(": ")[1].split(", ")[0]
commasplitstatus = status.split(", ")
percentleft = int(commasplitstatus[1].rstrip("%\n"))

FA_CHR = "<span font='FontAwesome'>\uf077</span>"
FA_DIS = "<span font='FontAwesome'>\uf078</span>"
FA_FULL = "<span font='FontAwesome'>\uf139</span>"
FA_LIGHTNING = "<span font='FontAwesome'>\uf0e7</span>"

fulltext = "<span color='yellow'>{}</span>".format(FA_LIGHTNING)
timeleft = state + ", time left:"
time = commasplitstatus[-1].split()[0]
time = ":".join(time.split(":")[0:2])
timeleft += " {}".format(time)

if state == "Discharging":
    form = ' <span color="{}">{}</span>'
    fulltext += form.format(image(percentleft), FA_DIS)
elif state == "Charging":
    fulltext += " " + FA_CHR
else:
    fulltext += " " + FA_FULL

form =  '<span color="{}">{}%</span>'
percent_string = str(percentleft).rjust(3)
fulltext += form.format(image(percentleft), percent_string)

if os.environ.get('BLOCK_BUTTON'):
    Popen(['notify-send', timeleft])

print(fulltext)
print(fulltext)
if percentleft < 5:
    exit(33)
