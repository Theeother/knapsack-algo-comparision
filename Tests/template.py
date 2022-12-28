import time
import timeit
import os
import sys
import matplotlib.pyplot as plt
import numpy as np


# setting path 
sys.path.insert(0, 'C:/Users/aksed/OneDrive/Bureau/softComputing/Single_solution_algorithms')

# import ../Single_solution_algorithms/simulated_annealing.py
import simulated_annealing 

class Team1:
    def __init__(self):
        self.name = "Team 1"
        self.solvingMethods = ["simulated_annealing"] # List of methods that are exactly the name of the methods used

    def simulated_annealing(self, numberOfElements, listOfElements , backPackSize):
        return simulated_annealing.simulated_annealing_method(numberOfElements, listOfElements , backPackSize)
    
    # Don't forget to add any new methods name to the solvingMethods list above
    # Edit only team 1, and the program will automatically compare the results of both teams and all the methods used by each team

class Team2:
    def __init__(self):
        self.name = "Team 2"
        self.solvingMethods = ["bruteForce"] 
    
    def bruteForce(self, numberOfElements, listOfElements , backPackSize):
      # brute force knapsack 0/1
      if numberOfElements >10:
        return [0, '']
      maxi = 0
      answer = ''
      for i in range(2**numberOfElements):
        weight = 0
        value = 0
        for j in range(numberOfElements):
          if i & (1 << j):
            weight += listOfElements[j][1]
            value += listOfElements[j][0]
        if weight <= backPackSize:
          if value > maxi:
            maxi = value
            answer = i 
      answer = bin(answer)[2:].zfill(numberOfElements)

      return [maxi, answer]

def check_solution(solution, item_list):
    value = 0
    weight = 0
    for i in range(len(solution[1])):
        if solution[1][i] == '1':
            value += item_list[i][0]
            weight += item_list[i][1]

    return solution[0]==value

# Don't change anything below this line unless you know what you are doing
# This is the main function that will run the program

if __name__ == "__main__":
    # get all file names from ../testsFC
    fileScales=["large_scale","low-dimensional"]
    # data structure
    # data = {team:{method:{averageTime:{smallTest:float,largeTest:float},accuracy:{smallTest:percentage,largeTest:percentage}}}}
    data = {}
    for fileScale in fileScales:
        data[fileScale]={}
        for file in os.listdir("../testsFC/"+fileScale):
            # get the file name
            fileName = os.path.splitext(file)[0]
            # get the file content
            fileContent = open("../testsFC/"+fileScale+"/"+file, "r")
            # get the number of elements and the backpack size
            numberOfElements, backPackSize = [int(x) for x in fileContent.readline().split()]
            # get the list of elements
            listOfElements = []
            for i in range(numberOfElements):
                try:
                    listOfElements.append([float(x) for x in fileContent.readline().split()])
                except:
                    print("Error in file "+file)
                    print("Line "+str(i+2))
                    print("Number of elements: "+str(numberOfElements))
                    print("Number of elements read: "+str(i))
                    print("Line content: "+fileContent.readline())
                    print("List of elements: "+str(listOfElements))
                    exit()
            # close the file
            fileContent.close()
            #get the solution
            solutionFile = open("../testsFC/"+fileScale+"-optimum/"+file, "r")
            realSolution = float(solutionFile.readline())
            # create the teams
            team1 = Team1()
            team2 = Team2()
            # create the data structure for the file
            data[fileScale][fileName] = {}
            # run the methods of team 1
            for method in team1.solvingMethods:
                # get the function
                function = getattr(team1, method)
                # run the function 100 times and get the average time
                averageTime = timeit.timeit(lambda: function(numberOfElements, listOfElements, backPackSize), number=100)/100
                # get the solution
                solution = function(numberOfElements, listOfElements, backPackSize)
                # check the solution
                accuracy = check_solution(solution, listOfElements)
                # add the data to the data structure
                data[fileScale][fileName][method] = {"averageTime":averageTime, "accuracy":accuracy}
            # run the methods of team 2
            for method in team2.solvingMethods:
                # get the function
                function = getattr(team2, method)
                # run the function 100 times and get the average time
                averageTime = timeit.timeit(lambda: function(numberOfElements, listOfElements, backPackSize), number=100)
                # get the solution
                solution = function(numberOfElements, listOfElements, backPackSize)
                # check if the solution is valid
                valid = check_solution(solution, listOfElements)
                # check accuracy
                accuracy = 0
                if valid:
                    accuracy = 100*solution[0]/realSolution 
                # add the data to the data structure
                data[fileScale][fileName][method] = {"averageTime":averageTime, "accuracy":accuracy}
    # print the data
    print(data)
    # plot the data comparing the methods of team 1 and team 2 average time and accuracy over the small and large tests 
    # create the data structure for the plot
    plotData = {}
    for fileScale in fileScales:
        plotData[fileScale] = {}
        for method in team1.solvingMethods+team2.solvingMethods:
            plotData[fileScale][method] = {"averageTime":{"smallTest":[], "largeTest":[]}, "accuracy":{"smallTest":[], "largeTest":[]}}
    # fill the data structure
    for fileScale in fileScales:
        for fileName in data[fileScale]:
            for method in data[fileScale][fileName]:
                if fileName[0]=="s":
                    plotData[fileScale][method]["averageTime"]["smallTest"].append(data[fileScale][fileName][method]["averageTime"])
                    plotData[fileScale][method]["accuracy"]["smallTest"].append(data[fileScale][fileName][method]["accuracy"])
                else:
                    plotData[fileScale][method]["averageTime"]["largeTest"].append(data[fileScale][fileName][method]["averageTime"])
                    plotData[fileScale][method]["accuracy"]["largeTest"].append(data[fileScale][fileName][method]["accuracy"])
    # plot the data
    for fileScale in fileScales:
        for method in team1.solvingMethods+team2.solvingMethods:
            # create a figure and two subplots
            fig = plt.figure()
            ax1 = plt.subplot(2, 1, 1)
            ax2 = plt.subplot(2, 1, 2)

            # remove the first subplot
           

            plt.title(method + " " + fileScale)

            # do some plotting on the second subplot
            ax1.boxplot([plotData[fileScale][method]["averageTime"]["smallTest"], plotData[fileScale][method]["averageTime"]["largeTest"]])
            ax1.set_xticks([1, 2])
            ax1.set_xticklabels(["smallTest", "largeTest"], rotation=45)
            ax1.set_ylabel("averageTime")

            # do some plotting on the second subplot
            ax2.boxplot([plotData[fileScale][method]["accuracy"]["smallTest"], plotData[fileScale][method]["accuracy"]["largeTest"]])
            ax2.set_xticks([1, 2])
            ax2.set_xticklabels(["smallTest", "largeTest"], rotation=45)
            ax2.set_ylabel("accuracy")

            # save the figure
            plt.savefig("plots/" + fileScale + ".png")

            # close the figure
            plt.close()


# Don't change anything above this line unless you know what you are doing