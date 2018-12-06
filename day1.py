result = 0
d = dict()
d[0] = 1
cycles = 0
with open('day1.txt', 'r') as f:
    lines = f.readlines()
    while True:
        cycles +=1
        for a_line in lines:
            # print("a_line", a_line, 'result is ', result)
            res = int(a_line.replace('+', ''))
            result += res
            if d.get(result):
                print(result, a_line)
                print("cycles", cycles)
                exit(1)
            d[result] = 1
            # print(res, result, d)

