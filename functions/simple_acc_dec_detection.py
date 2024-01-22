# Simple method for detection of accelerations and decelerations

# It is the equivalent of FHRMA's detectaccident()

# Not presently incorporated the wrapper simpleadddetection() which runs
# acceleration and deceleration detection, and false detection too, and returns
# all four sets of results.

# Also not presently implemented the false acc/dec detection from the minusint()
# function - this function would take inputs of a (outcome of detectaccident())
# and f (a rerun of detectaccident() but with a threshold of 5 instead of 15).
# The function would then removes elements from f that are also in a.

# Presently does includes a function to run this on all records and save in 
# a dataframe along with the equivalent FHRMA results. This function is
# create_accident_df().


import numpy as np
import pandas as pd


def detect_accident(sig, thre):
    '''
    Detect accelerations or decelerations by comparing difference betweeen FHR
    and FHR baseline against a specified threshold.

    This function identifies regions of the signal that are above the threshold
    and find the start, end and max heart rate in those regions. If that region
    is longer than 15 seconds, then it is classed as an accident, but if it is
    shorter than 15 seconds then it is ignored/dropped.

    Parameters:
    -----------
    sig: array
        Difference between signal and baseline - for accelerations this is
        fhr-baseline, and for decelerations this is baseline-fhr
    thre: int
        Threshold for difference

    Outputs:
    --------
    result: dataframe
        Dataframe with the time in seconds where a peak start and began, and 
        index for the maximum of the peak (and for decelerations, this is
        referring to a trough and the max of that trough)
    '''
    # Create empty list to store result
    res = []

    # Find points where value is greater than the threshold
    peaks = np.argwhere(sig > thre).ravel()

    # While we have points in peaks
    while len(peaks) > 0:

        # Extract all of sig before the first peak
        before = sig[:peaks[0]]

        # Find index of last point before peak that is < 0
        # E.g. For accelerations, last point where FHR is not past baseline
        dacc = np.argwhere(before < 0).ravel()
        if len(dacc) > 0:
            dacc = dacc[-1]
        else:
            dacc = 0

        # Extract all of signal after that point
        after = sig[dacc+1:]

        # Find index of first point after then that is < 0
        # Adding dacc+1 to convert it to actual location in signal (not just after peak)
        facc = np.argwhere(after < 0).ravel()
        if len(facc > 0):
            facc = facc[0] + dacc + 1
        else:
            facc = len(sig)-1

        # Filter to the values between dacc and facc (so array just has values > 0)
        interval = sig[dacc+1:facc]

        # Find the index of the maximum value in that interval
        # Adding dacc+1 to convert it to actual location in signal
        macc = np.argmax(interval) + dacc + 1

        # Check if length of interval is more than 15 seconds - if so, save result,
        # dividing each value by 4 so it is in seconds rather than quarter seconds -
        # and by 60 so it is in minutes rather than seconds - and plus 1 so it
        # matches the MATLAB results (as that is 1-indexed)
        if len(interval) >= 15*4:
            res.append([(x+1)/4/60 for x in [dacc, facc, macc]])

        # Filter to peaks that fall after interval explored
        peaks = peaks[peaks > facc]

    # Convert result to dataframe
    result = pd.DataFrame(res, columns=['start', 'end', 'max'])

    return (result)


def create_accident_df(raw_fhr, fhrma_base, fhrma_dict, type):
    '''
    Run the detect_accident function on all the FHR records, either detecting
    accelerations or decelerations, creating a dataframe with the accidents.

    Parameters:
    -----------
    raw_fhr : dictionary
        Dictionary with the raw FHR (cleaned) for each record
    fhrma_base : dictionary
        Dictionary with the baseline FHR for each record
    fhrma_dict : dictionary
        Dictionary with either acceleration or deceleration results from FHRMA
    type : string
        Either 'acc' (accelerations) or 'dec' (decelerations)

    Outputs:
    --------
    result: dataframe
        Dataframe with accelerations or decelerations for each record, from
        FHRMA and from Python function
    '''
    # Initialise list for storing results
    res = []

    # Loop through each of the FHR signals
    for record, fhr in raw_fhr.items():

        # Get baseline for that record
        baseline = fhrma_base[record]

        # Get results from FHRMA for that record
        fhrma_res = fhrma_dict[record]

        # Find accelerations or decelerations
        if type == 'acc':
            python_res = detect_accident(
                fhr-baseline, 15)[['start', 'end']].to_numpy()
        elif type == 'dec':
            python_res = detect_accident(
                baseline-fhr, 15)[['start', 'end']].to_numpy()

        # Check if all the elements match
        match = np.array_equal(fhrma_res, python_res)

        # Store in results
        res.append([record, fhrma_res, python_res, match])
    
    # Convert to dataframe
    result = pd.DataFrame(res, columns=['record', 'fhrma', 'python', 'match'])

    return (result)