# Functions that use the output from create_accident_df() to produce comparison
# between the accelerations or decelerations from Python versus FHRMA

import matplotlib.pyplot as plt
import numpy as np

def compare_means(df, x, y, title):
    '''
    Create scatterplot comparing two columns from df.

    Parameters:
    -----------
    df : dataframe
        Dataframe to create plot from
    x : string
        Name of column for x axis
    y : string
        Name of column for y axis
    title : string
        Title for the figure
    '''
    fig, ax = plt.subplots()
    ax.scatter(x=df[x], y=df[y])
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(title)
    plt.grid()
    ax.set_box_aspect(1)
    plt.show()


def find_length(arr):
    '''
    Find the length of each acceleration or deceleration and save to array

    Parameters:
    -----------
    arr : array
        Array with pairs of start and stop times for acceleration or deceleration

    Returns:
    --------
    lengths : array
        Array with length of each acceleration or deceleration
    '''
    lengths = []
    for row in np.arange(0, len(arr)):
        lengths.append(arr[row][1] - arr[row][0])
    return(lengths)


def validation_against_fhrma(result, type):
    '''
    Conduct a series of tests that compare FHRMA and Python results in the
    provided dataframe

    Parameters
    ----------
    result : dataframe
        Dataframe containing FHRMA and Python results for each record
    type : string
        Either 'accelerations' or 'decelerations'
    '''
    # Get number of acc/dec for each record
    result['fhrma_count'] = [len(x) for x in result['fhrma']]
    result['python_count'] = [len(x) for x in result['python']]

    # Show difference
    result['count_diff'] = result['python_count'] - result['fhrma_count']
    print(result['count_diff'].value_counts())

    # Plot comparison
    compare_means(result, 'fhrma_count', 'python_count',
                f'Number of detected {type}')

    # Find lengths of each of the accelerations and decelerations
    result['fhrma_length'] = [find_length(x) for x in result['fhrma']]
    result['python_length'] = [find_length(x) for x in result['python']]

    # Get total length for each
    result['fhrma_total'] = [sum(x) for x in result['fhrma_length']]
    result['python_total'] = [sum(x) for x in result['python_length']]

    # Get difference in total length
    result['total_diff'] = result['python_total'] - result['fhrma_total']
    print(result['total_diff'].value_counts())

    # Plot comparison
    compare_means(result, 'fhrma_total', 'python_total',
                f'Total length of detected {type}')