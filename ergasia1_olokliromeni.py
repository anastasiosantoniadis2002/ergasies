# ergasia1
import random
small = [0, 0, 0, 0, 0, 0, 0, 0, 0]
medium = [0, 0, 0, 0, 0, 0, 0, 0, 0]
big = [0, 0, 0, 0, 0, 0, 0, 0, 0]
count = 0
def winner_is(small, medium, big):
    for h in range(0, 8, 3):
        if small[h] == 1 and small[h+1] == 1 and small[h+2] == 1:
            return 0
        elif medium[h] == 1 and medium[h+1] == 1 and medium[h+2] == 1:
            return 0
        elif big[h] == 1 and big[h+1] == 1 and big[h+2] == 1:
            return 0
        elif small[h] == 1 and medium[h+1] == 1 and big[h+2] == 1:
            return 0
        elif small[h+2] == 1 and medium[h+1] == 1 and big[h] == 1:
            return 0
    for h in range(0, 2):
        if small[h] == 1 and small[h+3] == 1 and small[h+6] == 1:
            return 0
        elif medium[h] == 1 and medium[h+3] == 1 and medium[h+6] == 1:
            return 0
        elif big[h] == 1 and big[h+3] == 1 and big[h+6] == 1:
            return 0
        elif small[h] == 1 and medium[h+3] == 1 and big[h+6] == 1:
            return 0
        elif small[h+6] == 1 and medium[h+3] == 1 and big[h] == 1:
            return 0
    if small[0] == 1 and small[4] == 1 and small[8] == 1:
        return 0
    elif medium[0] == 1 and medium[4] == 1 and medium[8] == 1:
        return 0
    elif big[0] == 1 and big[4] == 1 and big[8] == 1:
        return 0
    elif small[0] == 1 and medium[4] == 1 and big[8] ==1:
        return 0
    elif small[8] == 1 and medium[4] == 1 and big[0]:
        return 0
    elif small[2] == 1 and small[4] == 1 and small[6] == 1:
        return 0
    elif medium[2] == 1 and medium[4] == 1 and medium[6] == 1:
        return 0
    elif big[2] == 1 and big[4] == 1 and big[6] == 1:
        return 0
    elif small[2] == 1 and medium[4] == 1 and big[6] == 1:
        return 0
    elif small[6] == 1 and medium[4] == 1 and big[2] == 1:
        return 0
    return 1
for i in range(100):
    small = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    medium = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    big = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    count1 = 0
    index1 = random.randint(1, 3)
    exit_number = 1
    while exit_number != 0:
        if index1 == 1:
            index2 = random.randint(0, 8)
            while small[index2] != 0 and count1 < 10:
                index2 = random.randint(0, 8)
                count1 = count1 + 1
            small[index2] = 1
        elif index1 == 2:
            index2 = random.randint(0, 8)
            while medium[index2] != 0 and count1 < 10:
                index2 = random.randint(0, 8)
                count1 = count1 + 1
            medium[index2] = 1
        else:
            index2 = random.randint(0, 8)
            while big[index2] != 0 and count1 < 10:
                index2 = random.randint(0, 8)
                count1 = count1 + 1
            big[index2] = 1
        count = count + 1
        exit_number = winner_is(small, medium, big)
print("it took on average", count/100, "steps")


