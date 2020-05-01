###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):

    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cows2 = cows.copy()

    sorted_cows = sorted(cows,key=cows.get,reverse = True)
    sorted_weights = sorted(cows.values(),reverse= True)

    
    big_result =[]
    check = len(sorted_cows)
    while check > 0:
        available = limit
        small_result =[]
        for cow in sorted_cows:
            try:
                if cows2[cow] <= available and available != 0:
                    available -= cows2[cow]
                    small_result.append(cow)
                    cows2.pop(cow)
                    check -= 1
            except KeyError:
                continue
        big_result.append(small_result)
    return big_result

# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    result_big_list = []
    minimum_trips = len(cows)+4
    for big_list in (get_partitions(cows)):
        check = 0

        for small_list in big_list:
            check+=1
            totalval = 0
            maxval = 0
            for particular_item in small_list:
                totalval += cows[particular_item]
            if totalval > limit:

                break
            else:
                if totalval > maxval:
                    maxval = totalval
                    if len(big_list)== check and len(big_list)< minimum_trips:
                        minimum_trips = len(big_list)
                        result_big_list = big_list
    return result_big_list,limit
    

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    start = time.time()
    greedy_cow_transport(cows, limit)
    end = time.time()
    print(end - start)
    start = time.time()
    brute_force_cow_transport(cows, limit)
    end = time.time()
    print(end - start)



    
    
    


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("D:\Visual\Mit_python_course 2\pset1\ps1_cow_data.txt")
limit=10
compare_cow_transport_algorithms()
# print(cows)

# print(greedy_cow_transport(cows, limit))
# print(brute_force_cow_transport(cows, limit))


