"""
    NSL-KDD
    https://www.unb.ca/cic/datasets/nsl.html
    http://205.174.165.80/CICDataset/NSL-KDD/Dataset/
"""
import pandas as pd
import os
from pyzhmh import __dirname__, download_one_file, unpack_one_file
__dirname__ = __dirname__()

NSL_KDD_URL = "http://205.174.165.80/CICDataset/NSL-KDD/Dataset/NSL-KDD.zip"
NSL_KDD_FILES = [
    'KDDTest+.txt',
    'KDDTest-21.txt',
    'KDDTrain+.txt',
    'KDDTrain+_20Percent.txt'
]
NSL_KDD_CACHE = os.path.join(__dirname__, 'data')
if not os.path.exists(NSL_KDD_CACHE):
    os.makedirs(NSL_KDD_CACHE)


def load_naslkdd_data(index: int = 3):
    if index < 0 or index > len(NSL_KDD_FILES) - 1:
        return None
    fullname = os.path.join(NSL_KDD_CACHE, 'NSL-KDD.zip')
    if download_one_file(fullname, {'url': NSL_KDD_URL}):
        try:
            for item in NSL_KDD_FILES:
                os.stat(os.path.join(NSL_KDD_CACHE, item))
        except OSError:
            # 有文件不存在
            unpack_one_file(fullname, NSL_KDD_CACHE)
        # 读取
        return pd.read_csv(os.path.join(NSL_KDD_CACHE, NSL_KDD_FILES[index]), header=None)
