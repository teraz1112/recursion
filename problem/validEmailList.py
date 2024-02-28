def validEmailList(emailList):
    def isValidEmail(email):
        if email.find(' ') != -1:
            return False
        if email.find('@') == 0 or email.find('@') == -1:
            return False
        if email.find('@') != email.rfind('@'):
            return False
        # 「@」の後に「.」があること
        if email.find('.', email.find('@')) == -1:
            return False
        return True
    validEmailList = []
    for email in emailList:
        if isValidEmail(email):
            validEmailList.append(email)
    return validEmailList
