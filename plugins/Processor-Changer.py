import subprocess
import idaapi
import idc
from idc import *
from idaapi import *



class Gullasch(idaapi.plugin_t):
    flags = idaapi.PLUGIN_UNL
    comment = "This is a comment"

    help = "Windbg helper"
    wanted_name = "Windbg helper"
    wanted_hotkey = "Alt-F6"

    def init(self):
        idaapi.msg("windbg helper is found Plugin is found. \n")
        return idaapi.PLUGIN_OK

    def run(self, arg):
        idaapi.msg("run() called with %d!\n" % arg)

    def term(self):
        idaapi.msg("")

    def AddMenuElements(self):
        idaapi.add_menu_item("Help/", "WinDbg helper", "", 0, self.Chop, ())
        idaapi.add_menu_item("Help/", "OpCodes", "", 0, self.Onion, ())

    def run(self, arg = 0):
        idaapi.msg("helper found.\n")

        self.AddMenuElements()

    def Chop(self):
        import os
        import subprocess
        import sys
        subprocess.Popen(os.path.join(os.path.expanduser('~'), os.path.expandvars('%IDADIR%'),
    'debugger.chm'), shell=True)

    def Onion(self):
        subprocess.Popen(os.path.join(os.path.expanduser('~'), os.path.expandvars('%IDADIR%'),
    'opcodes.chm'), shell=True)


def PLUGIN_ENTRY():
    return Gullasch()
