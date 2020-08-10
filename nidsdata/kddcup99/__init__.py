"""
    KDD CUP 1999
    http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html

    # 获取names
    data = load_kddcup99_data()
    val_label = data.loc[0].apply(lambda item: item.split('.')[0])
    print(val_label, type(val_label))
    val_names = data.loc[1:, 0].apply(lambda item: item.split(':')[0])
    print(val_names, type(val_names))
"""
import pandas as pd
import os
from pyzhmh import __dirname__, download_one_file
__dirname__ = __dirname__()


KDD_CUP_99_URL = "http://kdd.ics.uci.edu/databases/kddcup99"
KDD_CUP_99_FILE_LIST = [
    'kddcup.names',
    'kddcup.data.gz',
    'kddcup.data_10_percent.gz',
    'kddcup.newtestdata_10_percent_unlabeled.gz',
    'kddcup.testdata.unlabeled.gz',
    'kddcup.testdata.unlabeled_10_percent.gz',
]
KDD_CUP_99_CACHE = os.path.join(__dirname__, 'data')
if not os.path.exists(KDD_CUP_99_CACHE):
    os.makedirs(KDD_CUP_99_CACHE)


def load_kddcup99_data(index: int = 0):
    """
    加载数据
    :param index: 数据集，详见 KDD_CUP_99_FILE_LIST
    :return:
    """
    if index < 0 or index > len(KDD_CUP_99_FILE_LIST) - 1:
        return None
    filename = KDD_CUP_99_FILE_LIST[index]
    fullname = os.path.join(KDD_CUP_99_CACHE, filename)
    if download_one_file(fullname, {'url': f"{KDD_CUP_99_URL}/{filename}"}):
        return pd.read_csv(fullname, header=None)
    else:
        return None
