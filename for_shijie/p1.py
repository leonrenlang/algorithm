# 第一题
def process(payments):
    dic = {5: 0, 10: 0, 20: 0}
    for idx, payment in enumerate(payments):
        if payment == 5:
            dic[5] += 1
        elif payment == 10:
            if dic[5] == 0:
                print('false,%s' % str(idx + 1))
                exit()
            else:
                dic[5] -= 1
                dic[10] += 1
        elif payment == 20:
            if dic[10] >= 1 and dic[5] >= 1:
                dic[10] -= 1
                dic[5] -= 1
                dic[20] += 1
            elif dic[5] >= 3:
                dic[5] -= 3
                dic[20] += 1
            else:
                print('false,%s' % str(idx + 1))
                exit()
    print('true,%s' % str(len(payments)))


payments = [int(item) for item in input().split(',')]
process(payments)
