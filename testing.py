from collections import Counter

users = [(1,"qw"),(2,"er")]
logins = [(1,1),(1,1),(1,3),(2,4),(2,5),(1,7)]


def getUserLogins(users, logins):
    loginCnt = {}
    res = {}
    for element in logins:
        user, time = element[0], element[1]
        if user not in loginCnt:
            loginCnt[user] = set([time])
        else:
            loginCnt[user].add(time)
    userDict = {}
    for user in users:
        userId, username = user[0], user[1]
        userDict[userId] = username
    res = {}
    for element in loginCnt:
        res[userDict[element]] = len(loginCnt[element])
    print(res)
    return res



getUserLogins(users, logins)
