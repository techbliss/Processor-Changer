import re
import idaapi
import idc
from idc import *
from idaapi import *
import PyQt4
from PyQt4 import QtCore, QtGui
import idautils

class Zadow(idaapi.plugin_t):
    flags = idaapi.PLUGIN_UNL
    comment = "This is a comment"

    help = "Processor Changer"
    wanted_name = "Processor Changer"
    wanted_hotkey = "Alt-F7"

    def init(self):
        idaapi.msg("Process Plugin is found. \n")
        return idaapi.PLUGIN_OK

    def run(self, arg):
        idaapi.msg("run() called with %d!\n" % arg)

    def term(self):
        idaapi.msg("")
    
    def AddMenuElements(self):
        '''Menus are better than no GUI at all *sigh*'''

        idaapi.add_menu_item("Debugger/", "Change Processor to SPU", "", 0, self.ZadowSpu, ())
        idaapi.add_menu_item("Debugger/", "Change Processor to PPC", "", 0, self.ZadowPpc, ())
        idaapi.add_menu_item("Debugger/", "Change Processor to PPC64", "", 0, self.ZadowPpc64, ())
        idaapi.add_menu_item("Debugger/", "Change Processor to Arm", "", 0, self.ZadowArm, ())
        idaapi.add_menu_item("Debugger/", "Change Processor to PC", "", 0, self.ZadowPc, ())
        idaapi.add_menu_item("Debugger/", "Change Processor to java", "", 0, self.ZadowJava, ())
        idaapi.add_menu_item("Debugger/", "Change Processor to Mips", "", 0, self.ZadowMips, ())
        idaapi.add_menu_item("Debugger/", "Change Processor to Net", "", 0, self.ZadowNet, ())
        idaapi.add_menu_item("Debugger/", "Change Processor to Dalvik", "", 0, self.ZadowDalvik, ())
        idaapi.add_menu_item("Debugger/", "HighLight Calls", "", 0, self.ZadowHigh, ())



    def run(self, arg = 0):
        idaapi.msg("Hombre you are runnig good.\n")

        self.AddMenuElements()

    def ZadowSpu(self):
        idc.SetProcessorType('spu', SETPROC_USER)

    def ZadowPpc(self):
        idc.SetProcessorType('ppc', SETPROC_USER)

    def ZadowPpc64(self):
        idc.SetProcessorType('ppc64', SETPROC_USER)

    def ZadowArm(self):
        idc.SetProcessorType('arm', SETPROC_USER)

    def ZadowPc(self):
        idc.SetProcessorType('pc', SETPROC_USER)

    def ZadowJava(self):
        idc.SetProcessorType('java', SETPROC_USER)

    def ZadowMips(self):
        idc.SetProcessorType('mips', SETPROC_USER)

    def ZadowNet(self):
        idc.SetProcessorType('cli', SETPROC_USER)

    def ZadowDalvik(self):
        idc.SetProcessorType('dalvik', SETPROC_USER)

    def ZadowHigh(self):
        from idautils import XrefsFrom
        from idaapi import fl_CN as call_near, fl_CF as call_far
        from providers import ida

        provider = ida.IDA()

        startEA = provider.funcStart(provider.currentEA())
        endEA = provider.funcEnd(provider.currentEA())

        all_addresses = list(provider.iterInstructions(startEA, endEA))
        all_addresses.extend(provider.iterFuncChunks(startEA))
        all_addresses = list(set(all_addresses))

        for head in all_addresses:
            for xref in XrefsFrom(head):
                if xref.type == call_near or xref.type == call_far:
                    provider.setColor(head, 0x0000FF)

                provider.refreshView()


def PLUGIN_ENTRY():
    return Zadow()
