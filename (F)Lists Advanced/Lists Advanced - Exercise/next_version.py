software_version = [int(num) for num in input().split('.')]
software_version[-1] += 1
for index in range(len(software_version) - 1, -1, -1):
    if software_version[index] > 9:
        software_version[index] = 0
        if software_version[index - 1] >= 0:
            software_version[index - 1] += 1

result = [str(num) for num in software_version]
print('.'.join(result))
