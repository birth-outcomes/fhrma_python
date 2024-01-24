# Functions to load the FHR and FHRMA data required to run and validate the
# functions for calculation of baseline, accelerations and decelerations

import glob
import numpy as np
import os
import pandas as pd
from scipy import io

def import_csv(directory, output_dict):
    '''
    Import csv files from provided directory and save to output_dict

    Parameters
    ----------
    directory : string
        Location of the csv files
    output_dict : dictionary
        Object to save the files into

    Returns
    -------
    output_dict : dictionary
        Dictionary with  record name as key and content of csv files as values
    '''
    # Get list of .csv files in directory
    files = glob.glob(os.path.join(directory, '*.csv'))

    # Loop through files in the directory
    for file in files:
        # Get raw name of record (without path or file type)
        name = file.replace(directory, '').replace('.csv', '')
        # Import and save to dictionary
        output_dict[name] = pd.read_csv(file, header=None)[0].values

    return output_dict


def load_data(fhrma_path, fhr_path='./data/clean_fhr_matlab/'):
    '''
    Load the FHR and FHRMA data required to run and validate the functions for
    calculation of baseline, accelerations and decelerations

    Parameters
    ----------
    fhrma_path : string
        Location of the FHRMA results (mat file with baseline, accelerations
        and decelerations)
    fhr_path : string
        Location of the cleaned FHR files to use in the calculations
    '''
    # Load the cleaned FHR data
    raw_fhr = import_csv(directory=fhr_path, output_dict=dict())

    # Load FHRMA version of results
    mat_file = io.loadmat(fhrma_path)

    # Get array listing filenames (and hence order of the data)
    fhrma_files = np.concatenate(np.concatenate(mat_file['data']['filename']))

    # Get array with the FHRMA baseline and convert to dictionary
    # where keys are the record name and values are the baseline
    fhrma_base_arr = np.concatenate(mat_file['data']['baseline'])
    fhrma_base = {
        fhrma_files[i].replace('.fhr', ''): 
        fhrma_base_arr[i][0] for i in range(len(fhrma_files))}

    # Same for accelerations
    fhrma_acc_arr = np.concatenate(mat_file['data']['accelerations'])
    fhrma_acc = {
        fhrma_files[i].replace('.fhr', ''): 
        fhrma_acc_arr[i] for i in range(len(fhrma_files))}

    # Same for decelerations
    fhrma_dec_arr = np.concatenate(mat_file['data']['decelerations'])
    fhrma_dec = {
        fhrma_files[i].replace('.fhr', ''): 
        fhrma_dec_arr[i] for i in range(len(fhrma_files))}

    return(raw_fhr, fhrma_base, fhrma_acc, fhrma_dec)
