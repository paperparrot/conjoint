# coding=utf-8
__author__ = 'sebastiengenty'

import numpy as np
import pandas as pd

"""
This program is made to take the utilities from a CBC/HBC estimation. It then outputs summary relative utilities and
importances for the attributes and levels included.
"""


def conjoint_summary(utilities_file, demo_var=None):
    """
    Program that does the work of summarizing the conjoint results
    :param utilities_file: CSV file containing the utility scores. Top row should be labels
    :param demo_var: CSV file containing the filter valied. Each fi
    :return: table of the summary importances and average utilities. All scores are indexed.
    """

    # Loading the data files
    raw_df = pd.read_csv(utilities_file, index_col='Respondent')
    raw_df = raw_df.drop('RLH', axis=1)
