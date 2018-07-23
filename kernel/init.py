# By Zack Pace @ Roboot Team.  @RevelMind
# Any edits made, list here:
""" Edits;
001, Add custom.sh, changes text color.
002, Add edits section.
003, Add welcome message.
004, Returns subprocess output instead of ignoring it.
005, Add error system.
"""
import subprocess
import os

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
