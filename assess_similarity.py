import numpy as np
from vti_to_numpy import vti_to_numpy


def assess_similarity(spin_array):

    similarity_array = []

    for i in range(1, 1000):
        if (i+1) < 10:
            vti_filename_compare = 'seed-00' + str(i+1) + '-potts_3d.50.vti'
        elif (i+1) >= 10 and (i+1) < 100:
            vti_filename_compare = 'seed-0' + str(i+1) + '-potts_3d.50.vti'
        else:
            vti_filename_compare = 'seed-' + str(i+1) + '-potts_3d.50.vti'
        print(vti_filename_compare)
        spin_array_compare = vti_to_numpy(vti_filename_compare)
        total_spin_diff = 0

        for k in range(100):
            spin_diff = abs(spin_array[-1][-1][k] - spin_array_compare[-1][0][k])
            total_spin_diff += spin_diff 
        similarity_array.append(total_spin_diff/(10000))

        # Whole surface comparison:
        #for j in range(100):
        #    for k in range(100):
        #        spin_diff = abs(spin_array[j][-1][k] - spin_array_compare[j][0][k])
        #        total_spin_diff += spin_diff
        #similarity_array.append(total_spin_diff/(10000))

    return similarity_array

if __name__ == "__main__":
    vti_filename = 'seed-001-potts_3d.50.vti'
    spin_array = vti_to_numpy(vti_filename)
    similarity_array = assess_similarity(spin_array)
    min_value = min(similarity_array)
    min_index = similarity_array.index(min_value)
    print(min_value)
    print(min_index + 2)
    print(similarity_array)