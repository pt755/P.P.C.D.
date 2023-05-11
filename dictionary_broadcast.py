from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get.rank()

if rank == 0:
    data = {'key1' : [7, 2.72, 2+3]
            'key2' : []}