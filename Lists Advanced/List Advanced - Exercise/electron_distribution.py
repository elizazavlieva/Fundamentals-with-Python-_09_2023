def electron_shell(num_of_electrons):
    shell = []
    counter = 1

    while True:
        if num_of_electrons <= 0:
            break
        electrons = 2 * (counter**2)
        if electrons <= num_of_electrons:
            shell.append(electrons)
            num_of_electrons -= electrons
            counter += 1
        else:
            shell.append(num_of_electrons)
            num_of_electrons -= num_of_electrons
    return shell


num = int(input())
print(electron_shell(num))