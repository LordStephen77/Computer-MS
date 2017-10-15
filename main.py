#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
* @name        Computer Management Systems
* @copyright   Stefano Peris (c) 2017
* @author      Stefano Peris
* @email       lordstephen77@gmail.com
* @github      https://github.com/LordStephen77/Computer-MS
* @license     GPL-3.0 (https://www.gnu.org/licenses/gpl-3.0.en.html)
* @create      lun 16 ott 2017 00:31:27 CEST
* @update      null
"""

from tkinter import *
import random
import time

root = Tk()
root.geometry("1600x800+0+0")
root.title("Computer Management Systems")

Tops = Frame(root, width = 1600, height = 50, bg = "powder blue", relief = SUNKEN)
Tops.pack(side = TOP)

f1 = Frame(root, width = 800, height = 700, bg = "powder blue", relief = SUNKEN)
f1.pack(side = LEFT)

f2 = Frame(root, width = 300, height = 700, bg = "powder blue", relief = SUNKEN)
f2.pack(side = RIGHT)

######################### TIME #########################
localtime = time.asctime(time.localtime(time.time()))

######################### INFO #########################
lblInfo = Label(Tops, font = ("arial", 50, "bold"), text = "Computer Management Systems", fg = "Steel Blue", bd = 10, anchor = "w")
lblInfo.grid(row = 0, column = 0)
lblInfo = Label(Tops, font = ("arial", 20, "bold"), text = localtime, fg = "Steel Blue", bd = 10, anchor = "w")
lblInfo.grid(row = 1, column = 0)

root.mainloop()
