import random
import mpi4py

from mpi4py import MPI

#Simulate throwing a dice
def random_1_6(times = 1):
    """
    random_1_6 generates a random number between 1 and 6

    :return integer values of generated number under an array
    """
    times = range(times)
    result = []
    for time in times:
        result.append(random.randint(1,6)) 
    return result

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

match rank:
     case 0:
        #throw once
        rank_0_throws = random_1_6()
        #print
        print(f"Process {rank} threw a{rank_0_throws}.")
     case 1:
        #throw twice
        rank_1_throws = random_1_6()
        print(f"Process {rank} threw a{rank_1_throws}.")

        rank_1_throws = random_1_6()
        print(f"Process {rank} threw a{rank_1_throws}.")

        #sum_value
        sum_rank_1 = sum(rank_1_throws)
        print(f"Sum of values thrown by process {rank} is {sum_rank_1}")
     case 2:
        #throw and print
        rank_2_throws = random_1_6()
        print(f"Process {rank} threw a{rank_2_throws}.")

        rank_2_throws = random_1_6()
        print(f"Process {rank} threw a{rank_2_throws}.")

        rank_2_throws = random_1_6()
        print(f"Process {rank} threw a{rank_2_throws}.")
        


#print(random_1_6())