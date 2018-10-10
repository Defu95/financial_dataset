# coding:utf-8
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
import pandas as pd
from pandas import DataFrame
import numpy as np
from pandas import concat
import warnings

warnings.filterwarnings("ignore")

train_file1 = r'C:\Users\Johnson\Desktop\dataset\dataset\train_fund_return.csv'
train_file2 = r'C:\Users\Johnson\Desktop\dataset\dataset\train_fund_benchmark_return.csv'
train_file3 = r'C:\Users\Johnson\Desktop\dataset\dataset\train_index_return.csv'  # 35个基准
train_file4 = r'C:\Users\Johnson\Desktop\dataset\dataset\train_correlation.csv'  # label


def data_processing(file1, file2, file3, file4):
    data1 = pd.read_csv(file1, encoding='gbk')
    data2 = pd.read_csv(file2, encoding='gbk')
    data3 = pd.read_csv(file3, encoding='gbk')
    res = pd.DataFrame([])
    for k in range(1, data1.shape[1]):
        tm1 = data1.ix[0:, k]
        tm2 = data2.ix[0:, k]
        res = concat([res, tm1, tm2], axis=1)
    res.to_csv("D:\\hebing.csv", index=False, header=None)


def data_combination(file):
    data = pd.read_csv(file, encoding='gbk',header=None)
    res = pd.DataFrame()
    for i in range(0, 5):
        for j in range(i + 1, 5):
            tmp = pd.DataFrame()
            for k in range(0, int(data.shape[1] / 2)):
                # tm1 = DataFrame(data.ix[[i], [2 * k, 2 * k + 1]].values)
                # tm2 = DataFrame(data.ix[[j], [2 * k, 2 * k + 1]].values)
                tm1 = data.ix[[i], [2 * k, 2 * k + 1]].values
                tm2 = data.ix[[j], [2 * k, 2 * k + 1]].values
                tm1=DataFrame(tm1)
                tm2=DataFrame(tm2)
                # tmp.append(tm1)
                # tmp.append(tm2)
                tmp = concat([tmp, tm1, tm2], axis=1, ignore_index=True)
                # print(tmp)
            # res.extend(tmp)
            # print(tmp)
            res = concat([res, tmp], axis=0, ignore_index=True)
            print(res)
    res.to_csv("D:\\combination.csv", index=False, header=None)


'''
    # for i in range(1, data2.shape[1]):
    #     tmp2 = data2.ix[0:, i]
    #     tmp3 = data3.ix[0:, i]
    #     res=concat([res,tmp2,tmp3],axis=1)
    # res=pd.DataFrame(res)
    Result = pd.DataFrame([])
    TMP = pd.DataFrame([])
    for k in range(1, data1.shape[1]):
        tm1 = data1.ix[1:, k]
        tm1 = pd.DataFrame(tm1).T
        TMP = concat([TMP, tm1], axis=1, ignore_index=True)
    print(TMP)
    # for i in range(0, data2.shape[0]):
    # while(TMP.shape[0]<200):
    #     TMP = concat([TMP, TMP], axis=0)
    TMP.to_csv("D:\\tmp.csv",index=False)
    for k in range(1, data1.shape[1]):
        # tm1 = data1.ix[0:, k]
        # tm1 = pd.DataFrame(tm1).T
        # for i in range(0, data2.shape[0]):
        #     T1 = concat([T1, tm1])
        # print(T1)
        tm2 = DataFrame(data2.ix[0:, k])
        tm3 = DataFrame(data3.ix[0:, k])
        Result = concat([Result, tm2, tm3], axis=1)
        # Result = concat([Result,T1, tm2, tm3], axis=1)
    Result.to_csv('D:\\res.csv', index=False,header=None)
'''


def Cmn(data_file):
    data = pd.read_csv(data_file, encoding='gbk', header=0)
    zuhe = pd.DataFrame([])
    for k in range(0, 1):  # int(data.shape[1]/2)
        for i in range(0, data.shape[0]):
            tmp = pd.DataFrame([])
            for j in range(i + 1, data.shape[0]):
                TMP = concat([data.ix[i, 2 * k:2 * k + 1], data.ix[j, 2 * k:2 * k + 1]], axis=1)
                # print(TMP)
                tmp = concat([tmp, TMP], axis=0)
        zuhe = concat([zuhe, tmp], axis=1)
    zuhe.to_csv("D:\\zuhe.csv", index=False)


if __name__ == '__main__':
    # data_processing(train_file1, train_file2, train_file3, train_file4)
    data_combination("D:\\hebing.csv")
    # Cmn("D:\\res.csv")
