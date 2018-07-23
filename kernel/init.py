# By Zack Pace @ Roboot Team.  @RevelMind
# Any edits made, list here:
""" Edits:

"""
import subprocess
import os

def cmd(c="cls"):
  os.system(c)
  
def exe(f):
 subprocess.call(f)

exe(["custom.sh"]) # Customize Color
