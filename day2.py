from collections import Counter


def part_1(input='day2.txt'):
    num_trips = 0
    num_dubs = 0
    with open(input, 'r') as f:
        lines = f.readlines()
        for a_line in lines:
            # print(a_line)
            cnt_letrs = Counter()
            for a_letter in a_line:
                cnt_letrs[a_letter] +=1

            already_counted_trips = False
            already_counted_dubs = False
            for a_ltr_count in cnt_letrs:
                # print(a_ltr_count, cnt_letrs[a_ltr_count])
                if already_counted_dubs and already_counted_trips:
                    break
                elif cnt_letrs[a_ltr_count] == 3 and not already_counted_trips:
                    num_trips += 1
                    already_counted_trips = True
                elif cnt_letrs[a_ltr_count] == 2 and not already_counted_dubs:
                    num_dubs += 1
                    already_counted_dubs = True

            # print(cnt_letrs)
        return num_dubs,num_trips, num_trips*num_dubs

# print(part_1())


def part_2(input='day2.txt'):
    with open(input, 'r') as f:
        lines = f.readlines()
        for i, a_line in enumerate(lines):
            for a_second_line in lines[i:]:
                if len(a_line) != len(a_second_line):
                    continue
                match_count = len(a_line) - 1
                for i, a_letter in enumerate(a_line):
                    if a_letter == a_second_line[i]:
                        match_count -= 1
                if match_count == 0:
                    print("match found:", a_second_line, a_line)
                    return a_second_line, a_line

one, two = part_2()
result = ''
for i, a_letter in enumerate(one):
    if a_letter == two[i]:
        result += a_letter
print(one, two, result)


