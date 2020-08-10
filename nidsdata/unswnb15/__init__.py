"""
    UNSW-NB15
    https://www.unsw.adfa.edu.au/unsw-canberra-cyber/cybersecurity/ADFA-NB15-Datasets/
"""
import pandas as pd
import os
from pyzhmh import __dirname__, download_one_file
__dirname__ = __dirname__()


UNSWNB15_URL = "https://www.unsw.adfa.edu.au/unsw-canberra-cyber/cybersecurity/ADFA-NB15-Datasets"
UNSWNB15_FILE_LIST = [
    'NUSW-NB15_features.csv',
    'UNSW-NB15_1.csv',
    'UNSW-NB15_2.csv',
    'UNSW-NB15_3.csv',
    'UNSW-NB15_4.csv',
    'NUSW-NB15_GT.csv',
    'UNSW-NB15_LIST_EVENTS.csv',
    'a%20part%20of%20training%20and%20testing%20set/UNSW_NB15_training-set.csv',
    'a%20part%20of%20training%20and%20testing%20set/UNSW_NB15_testing-set.csv'
]
UNSWNB15_CACHE = os.path.join(__dirname__, 'data')
if not os.path.exists(UNSWNB15_CACHE):
    os.makedirs(UNSWNB15_CACHE)


def load_unswnb15_data(index: int = 0):
    if index < 0 or index > len(UNSWNB15_FILE_LIST) - 1:
        return None
    filename = UNSWNB15_FILE_LIST[index]
    fullname = os.path.join(UNSWNB15_CACHE, os.path.basename(filename))
    if download_one_file(fullname, {'url': f"{UNSWNB15_URL}/{filename}"}):
        return pd.read_csv(fullname, header=None, encoding='iso-8859-1', low_memory=False)
    else:
        return None
