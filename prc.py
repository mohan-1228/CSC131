def rep(repstring , base):
    decimal = 0
    exp = len(repstring)-1
    for i in repstring:
        decimal = decimal+ int(i)* base **exp
        exp -= 1
    return decimal 


print(rep("576", 8 ))

