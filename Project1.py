# https://www.codewars.com/kata/5b73fe9fb3d9776fbf00009e

import numpy as np
# рішення моє особисте
def sum_of_differences(arr):

    return np.diff(np.array(sorted(arr))).sum()

if __name__ == "__main__":

    print (sum_of_differences([-1, -9, 6, -12, 1, -4, 14, 10, 1, -13, 10]))
