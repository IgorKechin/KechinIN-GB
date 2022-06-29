import json

res = {}
av_profit = 0
num = 0
with open('my_file_5', 'r', encoding='utf-8') as f:
    for line in f:
        name, forma, income, cost = line.split()
        profit = int(income) - int(cost)
        if profit >=0:
            av_profit += profit
            num += 1
        res[name] = profit
av_profit /= num
with open('json.json', 'w', encoding='utf-8') as f:
    json.dump([res,{'average_profit':av_profit}],f,ensure_ascii=False)
