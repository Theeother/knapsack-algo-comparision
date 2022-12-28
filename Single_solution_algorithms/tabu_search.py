import numpy as np
import re
from operator import itemgetter

def greedy_knapsack(numberOfElements,listOfElements, capacity):
    solution = []

    capacite_restante = capacity
    current_weight = 0
    listOfElements = sorted(listOfElements,key=itemgetter(1), reverse=True)
    max_value = 0
    for i in range(numberOfElements):
        if listOfElements[i][1] <= capacite_restante:
            capacite_restante -= listOfElements[i][1]
            current_weight += listOfElements[i][1]
            solution.append(i)
            max_value += listOfElements[i][0]

    begin_solution = [0 for i in range(numberOfElements)]
    for i in solution:
        begin_solution[i] = 1

    return begin_solution, current_weight


def f(begin_solution, item, capacity):
    max_value = 0
    for i in range(len(item)):
        if begin_solution[i] == 1 and capacity >= 0:
            max_value += item[i][0]
            capacity -= item[i][1]

    if capacity < 0:
        max_value = -1
    return max_value


def tabu_search_method(numberOfElements, listOfElements , backPackSize):
    begin_solution, current_weight = greedy_knapsack(numberOfElements,listOfElements, backPackSize)
    T = []
    It = 0
    BestIt = 0
    best_solution = begin_solution[:]  # Best solution until then.
    capacity_rest = backPackSize
    temp = best_solution[:]
    solution_partial = []
    while It - BestIt <= 100:
        It += 1
        save_solution = temp[:]
        solution_tabu = list()
        valor = -1
        valorTabu = -1
        mov = -1
        movTabu = -1
        for i in range(numberOfElements):
            if temp[i] == 1:
                temp[i] = 0
            else:
                temp[i] = 1


            solution_partial = temp[:]
            if f(solution_partial, listOfElements, capacity_rest) > valor and not (i in T):
                save_solution = solution_partial[:]
                valor = f(save_solution, listOfElements, backPackSize)
                mov = i
                if f(solution_partial, listOfElements, backPackSize) > f(best_solution, listOfElements, capacity_rest):
                    best_solution = solution_partial[:]
                    BestIt = It
            elif f(solution_partial, listOfElements, capacity_rest) > f(best_solution, listOfElements, capacity_rest):
                save_solution = solution_partial[:]
                valor = f(save_solution, listOfElements, capacity_rest)
                best_solution = solution_partial[:]
                BestIt = It
                mov = i
            elif i in T and f(solution_partial, listOfElements, capacity_rest) > valorTabu:
                solution_tabu = solution_partial[:]
                valorTabu = f(solution_tabu, listOfElements, backPackSize)
                movTabu = i

            if temp[i] == 1:
                temp[i] = 0
            else:
                temp[i] = 1

        if mov == -1 and movTabu == -1:
            break
        if mov != -1:
            if not(mov in T):
                if len(T) == 3:
                    del T[0]
                T.append(mov)
            temp = save_solution[:]
        else:
            temp = solution_tabu[:]

    result = list()
    result.append(f(best_solution, listOfElements, backPackSize))
    result.append("".join(str(i) for i in temp))
    return result