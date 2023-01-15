import timeit
import os
import sys
import matplotlib.pyplot as plt
import numpy as np

# setting path

# import ../Single_solution_algorithms/simulated_annealing.py


def importingTeam1():
    sys.path.insert(
        0, 'C:/Users/aksed/OneDrive/Bureau/softComputing/Single_solution_algorithms')
    import simulated_annealing
    import glouton_search
    import tabu_search
    return simulated_annealing, glouton_search, tabu_search


def importingTeam2():
    sys.path.insert(
        0, 'C:/Users/aksed/OneDrive/Bureau/softComputing/genetic_algorithms')
    import genetic_algo_1
    import genetic_algo_2
    import genetic_algo_3
    import genetic_algo_4
    import genetic_algo_5
    import genetic_algo_6
    return genetic_algo_1.determinist_selection_and_single_point_crossover, genetic_algo_2.determinist_selection_and_multipoints_crossover, genetic_algo_3.determinist_selection_and_uniform_crossover, genetic_algo_4.tournament_selection_and_single_point_crossover, genetic_algo_5.roulette_wheel_selection_and_single_point_crossover, genetic_algo_6.uniform_selection_and_single_point_crossover


def importing_plots():
    sys.path.insert(
        0, 'C:/Users/aksed/OneDrive/Bureau/softComputing/Tests/plots')
    import ploting
    return ploting


simulated_annealing, glouton_search, tabu_search = importingTeam1()
determinist_selection_and_single_point_crossover, determinist_selection_and_multipoints_crossover, determinist_selection_and_uniform_crossover, tournament_selection_and_single_point_crossover, roulette_wheel_selection_and_single_point_crossover, uniform_selection_and_single_point_crossover = importingTeam2()


class Team1:
    def __init__(self):
        self.name = "Team 1"
        # List of methods that are exactly the name of the methods used
        self.solvingMethods = ["simulated_annealing",
                               "glouton_search", "tabu_search"]

    def simulated_annealing(self, numberOfElements, listOfElements, backPackSize):
        return simulated_annealing.simulated_annealing_method(numberOfElements, listOfElements, backPackSize)

    def glouton_search(self, numberOfElements, listOfElements, backPackSize):

        return glouton_search.glouton_search_method(numberOfElements, listOfElements, backPackSize)

    def tabu_search(self, numberOfElements, listOfElements, backPackSize):
        if numberOfElements > 10:
            return [1, '0'*numberOfElements]
        return tabu_search.tabu_search_method(numberOfElements, listOfElements, backPackSize)

    # Don't forget to add any new methods name to the solvingMethods list above
    # Edit only team 1, and the program will automatically compare the results of both teams and all the methods used by each team


class Team2:
    def __init__(self):
        self.name = "Team 2"
        self.solvingMethods = ["combination1_determinist_selection_and_single_point_crossover", "combination2_determinist_selection_and_multipoints_crossover", "combination3_determinist_selection_and_uniform_crossover",
                               "combination4_tournament_selection_and_single_point_crossover", "combination5_roulette_wheel_selection_and_single_point_crossover", "combination6_uniform_selection_and_single_point_crossover"]

    def combination1_determinist_selection_and_single_point_crossover(self, numberOfElements, listOfElements, backPackSize):
        try:
            return determinist_selection_and_single_point_crossover(numberOfElements, listOfElements, backPackSize)
        except:
            return [1, '0'*numberOfElements]

    def combination2_determinist_selection_and_multipoints_crossover(self, numberOfElements, listOfElements, backPackSize):
        try:
            return determinist_selection_and_multipoints_crossover(numberOfElements, listOfElements, backPackSize)
        except:
            return [1, '0'*numberOfElements]

    def combination3_determinist_selection_and_uniform_crossover(self, numberOfElements, listOfElements, backPackSize):
        try:
            return determinist_selection_and_uniform_crossover(numberOfElements, listOfElements, backPackSize)
        except:
            return [1, '0'*numberOfElements]

    def combination4_tournament_selection_and_single_point_crossover(self, numberOfElements, listOfElements, backPackSize):
        try:
            return tournament_selection_and_single_point_crossover(numberOfElements, listOfElements, backPackSize)
        except:
            return [1, '0'*numberOfElements]

    def combination5_roulette_wheel_selection_and_single_point_crossover(self, numberOfElements, listOfElements, backPackSize):
        try:
            return roulette_wheel_selection_and_single_point_crossover(numberOfElements, listOfElements, backPackSize)
        except:
            return [1, '0'*numberOfElements]

    def combination6_uniform_selection_and_single_point_crossover(self, numberOfElements, listOfElements, backPackSize):
        try:
            return uniform_selection_and_single_point_crossover(numberOfElements, listOfElements, backPackSize)
        except:
            return [1, '0'*numberOfElements]


def check_solution_validity(solution, item_list, backPackSize):
    value = 0
    weight = 0
    for i in range(len(solution[1])):
        if solution[1][i] == '1':
            value += item_list[i][0]
            weight += item_list[i][1]
    return (round(solution[0], 6) == round(value, 6) and weight <= backPackSize)


def run_method(method, numberOfElements, listOfElements, backPackSize, optimalSolution):
    # This function will run the method and return the time it took to run 100 times, the solution accuracy
    # and the solution itself

    # Run the method 100 times
    time = timeit.timeit(lambda: method(
        numberOfElements, listOfElements, backPackSize), number=1)*100
    # Get the solution
    solution = method(numberOfElements, listOfElements, backPackSize)
    # Check if the solution is valid
    solutionValidity = check_solution_validity(
        solution, listOfElements, backPackSize)
    # Check solution accuracy

    solutionAccuracy = 0
    if solutionValidity:
        solutionAccuracy = 100*(solution[0])/optimalSolution
    # else:
    #     print(method)
    #     print(optimalSolution, solution, solutionValidity)

    return {"time": time, "solutionValidity": solutionValidity, "solutionAccuracy": solutionAccuracy, "solution": solution}


# data structure :
# data = {low-dim:
#   team1:
#       method1:
#           nb_valid: number of valid elements
#           time_list: [valid times from run method]
#           accuracy_list: [solutionAccuracy from run method (0 if none valid)]
#   ...}


if __name__ == "__main__":
    # list of Teams
    teams = [Team1(), Team2()]
    list_of_scales = ["low_scale", "large_scale"]
    data = {}
    for scale in list_of_scales:
        data[scale] = {}
        for team in teams:
            data[scale][team.name] = {}
            for method in team.solvingMethods:
                data[scale][team.name][method] = {}
                data[scale][team.name][method]["nb_valid"] = 0
                data[scale][team.name][method]["time_list"] = []
                data[scale][team.name][method]["accuracy_list"] = []
            # list of test cases for each scale
                list_of_test_cases = os.listdir("Tests/test_data/"+scale)
                for test_case in list_of_test_cases:
                    # get the optimal solution
                    optimalSolution = float(
                        open("Tests/test_data/"+scale+"_optimum/"+test_case).read())
                    # get the test case data
                    with open("Tests/test_data/"+scale+"/"+test_case) as f:
                        numberOfElements, backPackSize = map(
                            int, f.readline().split())
                        listOfElements = []
                        for i in range(numberOfElements):
                            listOfElements.append(
                                list(map(float, f.readline().split())))
                    # run the methods

                    result = run_method(getattr(
                        team, method), numberOfElements, listOfElements, backPackSize, optimalSolution)
                    data[scale][team.name][method]["nb_valid"] += result["solutionValidity"]
                    data[scale][team.name][method]["time_list"].append(
                        result["time"])
                    data[scale][team.name][method]["accuracy_list"].append(
                        result["solutionAccuracy"])

    # print the results
    for scale in list_of_scales:
        print("Scale : ", scale)
        for team in teams:
            print("Team : ", team.name)
            for method in team.solvingMethods:
                print("Method : ", method)
                print("Number of valid solutions : ",
                      data[scale][team.name][method]["nb_valid"])
                print("Average time : ", np.mean(
                    data[scale][team.name][method]["time_list"]))
                print("Average accuracy : ", np.mean(
                    data[scale][team.name][method]["accuracy_list"]))
                print("")
            print("")
        print("")

    print(data)

    # plot the results
    # for scale in list_of_scales:
    #     for team in teams:
    #         for method in team.solvingMethods:
    #             plt.figure()
    #             plt.title("Scale : "+scale+" Team : "+team.name+" Method : "+method)
    #             plt.hist(data[scale][team.name][method]["accuracy_list"], bins=100)
    #             plt.xlabel("Accuracy")
    #             plt.ylabel("Number of solutions")
    #             plt.show()

    # plot the results

    ploting = importing_plots()
    ploting.plot(data)
