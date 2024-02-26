def stringCompression(s):
    # 関数を完成させてください
    compressed = ''  # 結果を格納する変数
    def compressHelper(s,n,compressed,count):
        if n<len(s)-1:
            if s[n]!=s[n+1]:
                if count==0:
                    compressed += s[n]
                    return compressHelper(s,n+1,compressed,0)
                else:
                    compressed += s[n]+str(count+1)
                    return compressHelper(s,n+1,compressed,0)
            else:
                count+=1
                return compressHelper(s,n+1,compressed,count)
        else:
            if count==0:
                compressed+=s[n]
                return compressed
            else:
                compressed+=s[n]+str(count+1)
                return compressed
        
    
    return compressHelper(s,0,compressed,0)

