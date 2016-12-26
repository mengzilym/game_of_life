# -*- coding:utf-8 -*-

import json
import tkinter as tk
from operator import itemgetter


class GameofLife():
    def __init__(self, row=0, colum=0):
        self.row, self.colum = row, colum
