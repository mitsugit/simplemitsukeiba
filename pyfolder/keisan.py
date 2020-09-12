# codifn: utf-8
# hoge.py

from flask import request
import numpy as np
import math
import decimal

def sum_cal():
    total = 0
    
    budget = request.form["budget"]

    odds1 = request.form["keyword1"]
    odds2 = request.form["keyword2"]
    odds3 = request.form["keyword3"]
    
    #budget = int(budget)

    odds_list = [float(i) for i in [odds1,odds2,odds3]]

    odds_dict={}
    for num,i in enumerate(odds_list):
        num=num+1
        key = "odds"+str(num)
        odds_dict[key]=i
    
    ################### 合成オッズの計算 ###################
    goukei = 0
    pre_gousei_odds = 0

    n = 1

    for i in range(len(odds_list)):
        goukei +=  1 / odds_list[i]    

    pre_gousei_odds = 1 / goukei

    gousei_odds = math.floor(pre_gousei_odds*10**n)/(10**n)


    ################### 資金分配の計算 ###################

    each_bet = []

    C = 0

    # リスト内の最小値を取得し、１００を乗じる
    A = min(odds_list) * 100


    budget = int(budget)

    # オッズの最小値を各オッズで割ったものをリスト化する
    B_list = [A / i for i in odds_list]

    # 小数切り捨て
    B_list = list(map(lambda x: math.floor(x), B_list))

    #print(B_list)

    C = sum(B_list)

    #print("C", C)
    ratio = [B_list[i] / C * 100 for i in range(0, len(B_list))]

    ratio = np.round(ratio, 1)

    each_bet = [int(np.round(budget * i/100,-2)) for i in ratio]

    bet_dict={}
    for num,i in enumerate(each_bet):
        num=num+1
        key = "odds"+str(num)
        bet_dict[key]=i


    print("each_bet:   ",each_bet)


################### 利益計算 ###################

    return_list = [xx * yy for (xx,yy) in zip(each_bet,odds_list)]
    return_list = list(map(lambda x: math.floor(x), return_list))

    return_dict={}
    for num,i in enumerate(return_list):
        num=num+1
        key = "odds"+str(num)
        return_dict[key]=i

    print("return_list:   ",return_list)

    total_bet = sum(each_bet)

    print("合計ベット金額:  ",total_bet,"円")

    profit_list = [x-total_bet for x in return_list]

    profit_dict={}
    for num,i in enumerate(profit_list):
        num=num+1
        key = "odds"+str(num)
        profit_dict[key]=i


    result = {'odds_dict':odds_dict,'bet_dict':bet_dict,'total_bet':total_bet,\
              'return_dict':return_dict,'profit_dict':profit_dict,'budget':budget}
    return result

