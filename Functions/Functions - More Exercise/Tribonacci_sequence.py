def sequence(num):
    tribonacci_list = []
    counter = 0
    for i in range(1, num + 1):
        if i == 1:
            tribonacci_list.append(i)
        else:
            if len(tribonacci_list) > 3:
                counter += 1
                next_num = sum(tribonacci_list[counter:])
                tribonacci_list.append(next_num)
            else:
                next_num = sum(tribonacci_list[:])
                tribonacci_list.append(next_num)
    tribonacci_list = [str(i) for i in tribonacci_list]
    return tribonacci_list


number = int(input())
print(' '.join(sequence(number)))
