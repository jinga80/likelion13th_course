import pandas as pd



def basicinfo(data):
    #행과 열
    print(data.describe())

    #기본정보
    print(data.info())