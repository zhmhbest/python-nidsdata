# python-nidsdata

这是一个封装了KDDCup99、NSL-KDD、UNSW-NB15等入侵监测数据集的Python包。

## 安装

```bash
pip install nidsdata
```

## 使用

### [KDDCup99](http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html)

```python
from nidsdata import load_kddcup99_data
"""
    load_kddcup99_data(index: int)
        index=0: 'kddcup.names',
        index=1: 'kddcup.data.gz',
        index=2: 'kddcup.data_10_percent.gz',
        index=3: 'kddcup.newtestdata_10_percent_unlabeled.gz',
        index=4: 'kddcup.testdata.unlabeled.gz',
        index=5: 'kddcup.testdata.unlabeled_10_percent.gz',
        
"""
# 获取names
data = load_kddcup99_data(index=0)

val_label = data.loc[0].apply(lambda item: item.split('.')[0])
print(val_label, type(val_label))

val_names = data.loc[1:, 0].apply(lambda item: item.split(':')[0])
print(val_names, type(val_names))
```

### [NSL-KDD](https://www.unb.ca/cic/datasets/nsl.html)

```python
from nidsdata import load_naslkdd_data
"""
    load_naslkdd_data(index: int)
        index=0: 'KDDTest+.txt',
        index=1: 'KDDTest-21.txt',
        index=2: 'KDDTrain+.txt',
        index=3: 'KDDTrain+_20Percent.txt'
"""
print(load_naslkdd_data(3))
```

### [UNSW-NB15](https://www.unsw.adfa.edu.au/unsw-canberra-cyber/cybersecurity/ADFA-NB15-Datasets/)

```python
from nidsdata import load_unswnb15_data
"""
    load_unswnb15_data(index: int)
        index=0: 'NUSW-NB15_features.csv',
        index=1: 'UNSW-NB15_1.csv',
        index=2: 'UNSW-NB15_2.csv',
        index=3: 'UNSW-NB15_3.csv',
        index=4: 'UNSW-NB15_4.csv',
        index=5: 'NUSW-NB15_GT.csv',
        index=6: 'UNSW-NB15_LIST_EVENTS.csv',
        index=7: 'UNSW_NB15_training-set.csv',
        index=8: 'UNSW_NB15_testing-set.csv'
"""
print(load_unswnb15_data(0))
```
