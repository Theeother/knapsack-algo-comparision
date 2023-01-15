
#uniform selection (prob=1/len(population)) + single point crossover(rate 0.7) + mutation (rate 0.8) 
#initial population(represented by binary matrix) of solutions(represented by binary lists) generated randomly  
#the graph represents the variation of fitness (gain) through out the generations 
#fitness = sum(index*value) index =0 or 1 if sum(index*weight)<max else fitness=0 

from array import array
import numpy as np
import pandas as pd
import random as rd
from random import randint
import matplotlib.pyplot as plt
from typing import List, Optional, Callable, Tuple

def cal_fitness(weight, value, population, threshold):
    fitness=[]
    for i in range(population.shape[0]):
        S1 = np.sum(population[i] * value)
        S2 = np.sum(population[i] * weight)
        if S2 <= threshold:
            fitness.append(S1)
        else :
            fitness.append(0)
    #print(fitness)        
    return fitness 


def uniform_selection(fitness, num_parents, population):
   
    newPopulation=[]
    # Computes the totallity of the population fitness
    population_fitness = sum([indiv for indiv in fitness])
    indivList=[]
    for i in range(len(population)):
        indivList.append(i)
    # Computes for each chromosome the probability 
    chromosome_probabilities = [1/len(population) for _ in population]
    
    #print(chromosome_probabilities)
    # Selects one chromosome based on the computed probabilities
    while(len(population)!=len(newPopulation)):
        v= np.random.choice(indivList,p=chromosome_probabilities)
        newPopulation.append(population[v])
    return np.array(newPopulation)
      
def single_point_crossover(parents,num_offsprings1,num_offsprings2):
    global cross
 
    crossover_rate = 0.5
    i=0
    x = rd.random()
    parents=parents.tolist()
    if x > crossover_rate:
          
          p=randint(2,len(parents[num_offsprings1])-1)
          A=parents[num_offsprings1][0:p]+parents[num_offsprings2][p:]
          B=parents[num_offsprings2][0:p] + parents[num_offsprings1][p:]
          parents[num_offsprings1]=A 
          parents[num_offsprings2]=B
    return np.array(parents)

def mutation(parents):
    parents=parents.tolist()
    l=randint(0,len(parents)-1)
    mutation_rate = 0.8
    for i in range(len(parents[l])):
        random_value = rd.random()
        if random_value > mutation_rate:
            parents[l][i]=1-parents[l][i]
    return np.array(parents)


def optimize(weight, value, population, pop_size, num_generations, threshold):
    parameters, fitness_history = [], []
    num_parents = int(pop_size[0]/2)
    
    for i in range(num_generations):
        num_offsprings1 = randint(0,pop_size[0]-1)
        num_offsprings2 = randint(0,pop_size[0]-1)
        fitness = cal_fitness(weight, value, population, threshold)
        fitness_history.append(fitness)
        
        #print(population)
        population = uniform_selection(fitness, num_parents, population)
        #print("selection:")
        #print(population)
        population = single_point_crossover(population, num_offsprings1,num_offsprings2)
        #print("crossover")
        #print(population)
        population = mutation(population)
        #print("mutation")
        #print(population)
        
    #print('Last generation: \n{}\n'.format(population)) 
    fitness_last_gen = cal_fitness(weight, value, population, threshold)      
    #print('Fitness of the last generation: \n{}\n'.format(fitness_last_gen))
    max_fitness = np.where(fitness_last_gen == np.max(fitness_last_gen))
    parameters.append(population[max_fitness[0][0],:])
    return parameters, fitness_history


def uniform_selection_and_single_point_crossover(numberOfElements, listOfElements , backPackSize):
    
    num_generations=500
    solutions_per_pop = 8
    pop_size=(solutions_per_pop,numberOfElements)
    weight=[]
    value=[]
    initial_population = np.random.randint(2, size = pop_size)
    initial_population = initial_population.astype(int)
    for elt in listOfElements:
        weight.append(elt[1])
        value.append(elt[0])
    parameters, fitness_history = optimize(weight, value, initial_population, pop_size, num_generations, backPackSize)
    #print('The optimized parameters for the given inputs are: \n{}'.format(parameters))
    selected_items = parameters
    #print('\nSelected items that will maximize the knapsack without breaking it:')
    sumValue=0
    for i in range(len(selected_items[0])):
      if selected_items[0][i] != 0:
         #print('{}'.format(selected_items[0][i]))
         sumValue+=value[selected_items[0][i]-1]
     
    #fitness_history_mean = [np.mean(fitness) for fitness in fitness_history]
    #fitness_history_max = [np.max(fitness) for fitness in fitness_history]
    #list1=range(num_generations)
    #plt.plot(list1, fitness_history_mean, label = 'Mean Fitness')
    #plt.plot(list1, fitness_history_max, label = 'Max Fitness')
    #plt.legend()
    #plt.title('Fitness through the generations')
    #plt.xlabel('Generations')
    #plt.ylabel('Fitness')
    #plt.show()
    #print(np.asarray(fitness_history).shape)
    return [sumValue,"".join(list(map(str, selected_items[0])))]

#print(list)
#print(maxv)
