def findXTimes(teams):
    hash = {}
    for team in teams:
        if team in hash:
            hash[team] += 1
        else:
            hash[team] = 1
    
    for team in hash:
        if hash[team] != hash[teams[0]]:
            return False
    
    return True
