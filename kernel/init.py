# By Zack Pace @ Roboot Team.  @RevelMind
# Any edits made, list here:
""" Edits;
001, Add custom.sh, changes text color.
002, Add edits section.
003, Add welcome message.
"""
import subprocess
import os

def cmd(c="cls"):
  os.system(c)
  
def exe(f):
 subprocess.call(f)

exe(["custom.sh"]) # Customize Color
cmd("echo 'Welcome to Roboot.'")
