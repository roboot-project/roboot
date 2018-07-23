# By Zack Pace @ Roboot Team.  @RevelMind
# Any edits made, list here:
""" Edits;
001, Add custom.sh, changes text color.
002, Add edits section.
003, Add welcome message.
004, Returns subprocess output instead of ignoring it.
005, Add error system.
006, Import json system.
007, Add first boot system.
008, Add system configuration.
009, Ignore if not first boot.
"""
import subprocess
import os
import json

def cmd(c="cls"):
  os.system(c)
  
def exe(f):
 return subprocess.call(f)

exe(["custom.sh"]) # Customize Color
cmd("echo 'Welcome to Roboot.'")

# Idk what now.
_error = None

while True:
  if not _error == None:
    cmd("echo 'Error," + _error + "'")

with open("sys.json") as f:
  data = json.load(f)
  if data["first-run"] == "false":
    data["first-run"] = "true"
    cmd("install_dependencies.sh")
  else:
    pass
