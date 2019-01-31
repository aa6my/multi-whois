import sys
from cx_Freeze import setup, Executable
import _version as mwhois_info

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None

#IMPORTANT: Make sure the target_name has the .exe at end of name .e.g example.exe
target_name = 'mwhois.exe'

if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = mwhois_info.__name__,
        version = mwhois_info.__version__,
        author = mwhois_info.__author__,
        description = mwhois_info.__description__,
        license = mwhois_info.__license__,
        options = {"build_exe": build_exe_options},
        executables = [Executable("__init__.py", base=base, targetName=target_name)])