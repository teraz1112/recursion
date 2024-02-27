def decimalToBinary(decNumber):
    # 関数を完成させてください
    binaryNumberString=''
    while(decNumber>1):
        a=decNumber%2
        decNumber=decNumber//2
        binaryNumberString=str(a)+binaryNumberString
    binaryNumberString='1'+binaryNumberString
    return int(binaryNumberString)
