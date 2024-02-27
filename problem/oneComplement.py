def oneComplement(bits):
    # 関数を完成させてください
    list=[]
    for i in range(0,len(bits)):
        if bits[i]=='0':
            list.append('1')
        else:
            list.append('0')
    return ''.join(list)
