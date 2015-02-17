# coding=utf-8
__author__ = 'sebastiengenty'

import numpy as np
import pandas as pd

"""
This program is made to take the utilities from a CBC/HBC estimation. It then outputs summary relative utilities and
importances for the attributes and levels included.
"""


def conjoint_utltilites(utilities_file, demo_var=None):
    """
    Computes the rescaled utility values for all the attribute levels
    :param utilities_file: CSV file containing the utility scores. Top row should be labels.
    :param demo_var: CSV file containing the grouping variables. Top row should be labels.
    :return: Table of the average utilities. All scores are indexed.
    """

    # Loading the data files
    raw_df = pd.read_csv(utilities_file, index_col='Respondent')
    raw_df = raw_df.drop('RLH', axis=1)

    # This is where the function will go

    return output_df


def conjoint_importance(utilities_file, demo_car=None):
    """
    Computes the importances for the attributes of the product
    :param utilities_file: CSV file containing the utility scores. Top row should be labels
    :param demo_car: CSV file containing the grouping variables. Top row should be labels.
    :return:Table of the attribute importances. All scores are indexed.
    """

    # Loading the data files
    raw_df = pd.read_csv(utilities_file, index_col='Respondent')
    raw_df = raw_df.drop('RLH', axis=1)

    return output_df