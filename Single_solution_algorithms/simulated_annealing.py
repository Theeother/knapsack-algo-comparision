import random
import math

# function that select the initial solution of simulated_annealing method randomly
def select_initial_solution_randomly(numberOfElements, listOfElements, backPackSize):
    remaining_items = listOfElements.copy()
    selected_items = []
    remaining_capacity = backPackSize

    items_selection_list = numberOfElements * ['0']
    value = 0
  
    while remaining_capacity > 0 and len(remaining_items) > 0:
        index = random.randint(0, len(remaining_items) - 1)
        if remaining_capacity - remaining_items[index][1] < 0:
            del remaining_items[index]
            continue
        else:
            remaining_capacity = remaining_capacity - remaining_items[index][1]
            selected_items.append(remaining_items[index])
            value = value + remaining_items[index][0]
            initial_index = listOfElements.index(remaining_items[index])
            items_selection_list[initial_index] = '1'
            #Test
            #print("Selected object: ", remaining_items[index],' --> initial index ', initial_index)
            del remaining_items[index]
    #Test  
    #print("Remaining capacity: ", remaining_capacity)
    #print("Selected objects: ", selected_items)
  
    items_selection_string = ''.join(e for e in items_selection_list)
  
    return [value, items_selection_string]

#Test 
#result = random_selection_initial_solution(4, [[9,6],[11,5],[13,9],[15,7]], 20)
#print(result)

# function that create a new solution based on the initial one (perturbation)
def create_new_solution(initial_solution, listOfElements, backPackSize ):
    new_solution = list(initial_solution[1].strip())
    newValue = initial_solution[0]

    total_size = 0
    for i in range(len(initial_solution)-1):
        if initial_solution[i] == '1':
            total_size = total_size + listOfElements[i][1]

    while True:
        index = random.randint(0,len(initial_solution)-1)

        if new_solution[index] == '0':
            if total_size + listOfElements[index][1] > backPackSize:
                continue
            new_solution[index] = '1'
            newValue = newValue + listOfElements[index][0]
            break
        else:
            new_solution[index] = '0'
            newValue = newValue - listOfElements[index][0]
            break

    return [newValue, ''.join(e for e in new_solution)]

#Test 
#print(create_new_solution([33,'1110'], [[9,6],[11,5],[13,9],[15,7]], 20))

    
def simulated_annealing_method(numberOfElements, listOfElements , backPackSize):
    # Initialisation
    T = 100
    Tmin = 85
    K = 0.9
    nb_it = 3
    i = 0

    solution = select_initial_solution_randomly(numberOfElements, listOfElements, backPackSize)
    #print("Initial solution: ", solution)

    while T>Tmin and i<nb_it:
        i = i + 1

        #Perturbation
        new_solution = create_new_solution(solution, listOfElements, backPackSize )

        #Comparison
        diff = solution[0] - new_solution[0]
        
        if (diff < 0):
            solution = new_solution            
        else : 
            if random.uniform(0,1) > math.exp(-diff/T): 
                solution = new_solution
        
        T = T * K
    #print("Initial solution: ", solution)
    return solution