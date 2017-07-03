l = [128, 97, 121, 123, 98, 97, 105]

def find_biggest(l):
    biggest_diff = (None, None, None)
    for ind, n in enumerate(l):
        sliced_l = l[ind+1:]
        print 'sliced ', sliced_l
        for ind_s, num in enumerate(sliced_l):
            print num, n
            if num > n:
                diff = num - n
                if biggest_diff is not (None, None, None):
                    if diff > biggest_diff[0]:
                        biggest_diff = (diff, n, num)
                else:
                    biggest_diff = diff
        print biggest_diff
    return biggest_diff

print find_biggest(l)
