def steps(stairs):
    if stairs >= 0:
        if stairs == 2:
            return 2
        if stairs == 0:
            return 0
        if stairs == 1:
            return 1
        return steps(stairs - 1) + steps(stairs - 2)
    return None

stairs = int(input())
print(steps(stairs))
