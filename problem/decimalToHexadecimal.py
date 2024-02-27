def decimalToHexadecimal(decNumber):
    # 関数を完成させてください
    binaryNumberString=''
    hex_chars = "0123456789ABCDEF"
    while(decNumber>0):
        a=decNumber%16
        decNumber=decNumber//16
        binaryNumberString=hex_chars[a]+binaryNumberString
    return binaryNumberString
