# Function to get the average of n records, producing a shortened version of
# the FHR (e.g. shorterned by getting average of every 8 records)

# Equivalent to FHRMA's avgsubsamp()

import numpy as np

def avg_subsample(fhr, n):
    '''
    Find the average of every n records, producing shorterned FHR.

    Parameters
    ----------
    fhr : array
        Fetal heart rate
    n : integer
        How frequently to divide the FHR and find average (i.e. every n records)

    Returns
    -------
    sfhr : array
        Shortened version of fetal heart rate
    '''
    # Create empty list to store the shortened heart rate
    sfhr = []

    # Run a for loop, finding average every n records
    start = 0
    end = len(fhr)
    step = n
    for i in range(start, end, step):
        sfhr.append(np.mean(fhr[i:i+step]))

    # If there is a remainder (ie. fhr doesn't perfectly divide by n), drop
    # the final element in sFHR as it's based on less than n data points
    if len(fhr) % n != 0:
        sfhr.pop()

    return (sfhr)