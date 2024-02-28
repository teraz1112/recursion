def hasSameType(user1,user2):
    if len(user1)!=len(user2):
        return False
    hash={}
    for i in range(len(user1)):
        if user1[i] not in hash:
            hash[user1[i]]=user2[i]
        else:
            if hash[user1[i]]!=user2[i]:
                return False
    # ハッシュの値が重複しているかどうかを確認する
    if len(hash.values())!=len(set(hash.values())):
        return False
    return True
        
