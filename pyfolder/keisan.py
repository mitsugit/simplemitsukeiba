# codifn: utf-8
# hoge.py

from flask import request
import numpy as np
import math
import decimal

def sum_cal():
    total = 0
    
    odds1 = request.form["keyword1"]
    odds2 = request.form["keyword2"]
    odds3 = request.form["keyword3"]
    
    #budget = int(budget)

    odds_list = [float(i) for i in [odds1,odds2,odds3]]

    total = float(odds1) + float(odds2) + float(odds3)

    total = str(total)

    result = {'odds1':odds1,'odds2':odds2,'odds3':odds3,'total':total}
    return result

