def glouton_search_method(numberOfElements, listOfElements , backPackSize):
    #variable initialization
    position=-1
    weight=0
    optimalValue=0
    objectsSelected=[0]*numberOfElements
    listSelected=[[0,0]]*numberOfElements
    result=list()
    #sorting the elements of the backpack by decreasing value
    listOfElementsSorted= list(reversed(sorted(listOfElements)))
    #print(listOfElementsSorted)
    #calculation of the optimal value and creation of the list of selected objects
    for i in range(numberOfElements):
        if weight+listOfElementsSorted[i][1]<=backPackSize:
            #objectsSelected[i]=1
            listSelected[i]=listOfElementsSorted[i]
            if listSelected[i] in listOfElements:
                    position=listOfElements.index(listSelected[i],0,len(listOfElements))
                    objectsSelected[position]=1
            optimalValue=optimalValue+listOfElementsSorted[i][0]
            weight=weight+listOfElementsSorted[i][1]
    #print(listSelected)
    result.append(optimalValue)
    result.append("".join(str(i) for i in objectsSelected))
    return result


#Test
#glouton_search_method(4,[[8,5],[11,7],[6,4],[4,3]],14)
#glouton_search_method(3,[[3,4],[4,1],[6,5]],8)
#glouton_search_method(5,[[2,1],[5,4],[3,2],[1,5],[6,7]],17)



        
                   
                   




