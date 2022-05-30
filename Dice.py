import numpy as np
import random
import math
from pandas import *
import time

class Dice:
    def __init__(self):
        self.game_state()

    def game_state(self):  # returns three dictionaries
        dict1 = {1: 0.5, 2: 0.015, 3: 0.025, 4: 0.05, 5: 0.4, 6: 0.01}
        dict2 = {1: 0.5, 2: 0.4, 3: 0.05, 4: 0.01, 5: 0.015, 6: 0.025}
        dict3 = {1: 0.05, 2: 0.015, 3: 0.01, 4: 0.4, 5: 0.5, 6: 0.025}
        return dict1, dict2, dict3

    def fac(self, x, y, z):
        return np.absolute((x + y + z) / 3 - (3.01))

    def fac_(self, x):
        return np.absolute((x + 1 / 3 - (1.01)))

    def minimax_app(self, n):
        dv1 = self.fvalue(0)  # values of dice 1
        dv2 = self.fvalue(1)  # values of dice 2
        dv3 = self.fvalue(2)  # values of dice 3
        dictvalue = [[0 for j in range(6)] for i in range(6)]
        dictkey = [[0 for j in range(6)] for i in range(6)]
        dv2_backprog = [[0 for j in range(6)] for i in range(6)]
        for i in range(len(dv1)):
            for j in range(len(dv1)):
                listl = []
                for k in range(len(dv1)):
                    value = dv3[k]  # calcualtes values of dice 3 based on normalization
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
                value = dv2_backprog[i][j] # calculates the updated values of dice 2 based on normalization
                listm.append(value)  # puts the calculated values into a list
            dictvalue2.append(max(listm))  # puts the maximum values into a list
            dictkey2.append([listm.index(max(listm)) + 1, dictkey[i][j]])
            dv1_backprog.append(dv2_backprog[i][listm.index(max(listm))])

        fvalues = []
        fvaluesind = []
        for i in range(len(dv1)):
            fvalues.append(dv1_backprog[i])
            fvaluesind.append([i + 1, dictkey2[i][0] + 1, dictkey2[i][1]])
        fres = fvalues.index(max(fvalues))
        #fres_ind = fvaluesind.index(max(fvalues))
        if n == 1:
            return fvaluesind[fres]
        if n == 0:
            return (dictkey)

    def fvalue(self, n):
        gs0 = list(self.game_state()[0].values())
        gs1 = list(self.game_state()[1].values())
        gs2 = list(self.game_state()[2].values())
        game_state_values = []
        game_state_keys = []
        if n == 0:
            for i in range(0, 6):
                game_state_values.append(gs0[i] / self.fac_(i))
        if n == 1:
            for i in range(0, 6):
                game_state_values.append(gs1[i] / self.fac_(i))
        if n == 2:
            for i in range(0, 6):
                game_state_values.append(gs2[i] / self.fac_(i))
        return game_state_values

    def gamestate_value(self):
        listv =[]
        listi = []
        for i in range(0, 6):
            for j in range(0, 6):
                for k in range(0, 6):
                    listv.append(self.fvalue(i, j, k))
                    listi.append([i + 1, j + 1, k + 1])
        return listv, listi

    def get_best_1st_node(self):
        gsv0 = self.fvalue(0)
        gsv1 = self.fvalue(1)
        gsv2 = self.fvalue(2)
        parent_visit = 1
        for j in range(0, 6):
            listl = []
            for k in range(0, 6):
                listl.append(gsv2[k] + np.sqrt(2) * np.sqrt(np.absolute(np.log(parent_visit))))
            gsv1[j] = gsv1[j] + max(listl)
            parent_visit = parent_visit + 1
        parent_visit = 6
        for i in range(0, 6):
            listl = []
            for j in range(0, 6):
                listl.append(gsv1[j] + np.sqrt(2) * np.sqrt(np.absolute(np.log(parent_visit) / (j + 7))))
            gsv0[i] = gsv0[i] + max(listl)
            parent_visit = parent_visit + 1
        return gsv0.index(max(gsv0)) + 1

    def get_best_node(self):
        i = self.get_best_1st_node()
        gsv1 = self.fvalue(1)
        gsv2 = self.fvalue(2)
        parent_visit = 12
        for j in range(0, 6):
            listl = []
            for k in range(0, 6):
                listl.append(gsv2[k] + np.sqrt(2) * np.sqrt(np.absolute(np.log(parent_visit) / (k + 1))))
            gsv1[j] = gsv1[j] + max(listl)
            parent_visit = parent_visit + 1
        return (i, gsv1.index(max(gsv1)) + 1, gsv2.index(max(gsv2)) + 1)

def main():
    g = Dice()
    print(g.get_best_node())
    print(g.minimax_app(1))

if __name__ == "__main__":
    main()
