import numpy as np
import random
import math
from pandas import *
import time

class Dice:
    def __init__(self):
        self.game_state()

    def game_state(self):  # returns three dictionaries
        dict1 = {1: 0.01, 2: 0.015, 3: 0.025, 4: 0.05, 5: 0.4, 6: 0.5}
        dict2 = {1: 0.01, 2: 0.4, 3: 0.05, 4: 0.025, 5: 0.015, 6: 0.5}
        dict3 = {1: 0.05, 2: 0.015, 3: 0.01, 4: 0.025, 5: 0.4, 6: 0.5}
        return dict1, dict2, dict3

    def fac(self, x, y, z):
        return np.absolute((x + y + z) / 3 - (3.01))

    def dicevalue(self, n):  # returns a list
        keys = list(self.game_state()[n - 1].keys())
        values = list(self.game_state()[n - 1].values())
        res = []
        for i in keys:
            res.append(values[i - 1])
        return res

    def minimax_app(self, n):
        dv1 = self.dicevalue(1)  # values of dice 1
        dv2 = self.dicevalue(2)  # values of dice 2
        dv3 = self.dicevalue(3)  # values of dice 3
        dictvalue = [[0 for j in range(6)] for i in range(6)]
        dictkey = [[0 for j in range(6)] for i in range(6)]
        dv2_backprog = [[0 for j in range(6)] for i in range(6)]
        for i in range(len(dv1)):
            for j in range(len(dv1)):
                listl = []
                for k in range(len(dv1)):
                    value = dv3[k] / self.fac(i + 1, j + 1, k + 1)  # calcualtes values of dice 3 based on normalization
                    listl.append(value)  # puts the calculated values into a list
                dictvalue[i][j] = max(listl)  # selects the maximum values of dice 3
                dictkey[i][j] = listl.index(max(listl)) + 1  # gets the indices of dice3 with maximum values
                dv2_backprog[i][j] = dv1[listl.index(max(listl))]  # updates the values of dice2 for each index of dice1

        dictvalue2 = []
        dictkey2 = []
        dv1_backprog = []
        for i in range(len(dv1)):
            listm = []
            for j in range(len(dv1)):
                value = dv2_backprog[i][j] / self.fac(i + 1, j + 1, dictkey[i][
                    j])  # calculates the updated values of dice 2 based on normalization
                listm.append(value)  # puts the calculated values into a list
            dictvalue2.append(max(listm))  # puts the maximum values into a list
            dictkey2.append([listm.index(max(listm)) + 1, dictkey[i][j]])
            dv1_backprog.append(dv2_backprog[i][listm.index(max(listm))])

        fvalues = []
        fvaluesind = []
        for i in range(len(dv1)):
            fvalues.append(dv1_backprog[i] / self.fac(i + 1, dictkey2[i][0], dictkey2[i][1]))
            fvaluesind.append([i + 1, dictkey2[i][0], dictkey2[i][1]])
        fres = fvalues.index(max(fvalues))
        # fres_ind = fvaluesind.index(max(fvalues))
        if n == 1:
            return (fres, fvaluesind)
        if n == 0:
            return (dictkey)

def main():
    g = Dice()
    print(g.minimax_app(0))

if __name__ == "__main__":
    main()