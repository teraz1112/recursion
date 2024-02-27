def twosComplement(bits):
    # 関数を完成させてください
    def oneComplement(bits):
        # 関数を完成させてください
        list=[]
        for i in range(0,len(bits)):
            if bits[i]=='0':
                list.append('1')
            else:
                list.append('0')
        return ''.join(list)
    
    if bits=='00000000':
        return '100000000'
    oneComp=oneComplement(bits)
    
    reversed_number = oneComp[::-1]
    
    zero=reversed_number.find('0')
    modify=reversed_number.replace("0", "1", 1)
    comp=modify.replace("1", "0", zero)
    return comp[::-1]
