import sys
import re
import stackexchange
import os

def getErrs():
    stderr = []
    for line in sys.stdin.readlines():
        stderr.append(re.sub('[\n]', '', line).strip(" "))
    print stderr
    return stderr[-1]

def getDiff():
    userCode = list()
    with open("pystack.txt.tmp", 'r') as userCodeFi:
        for line in userCodeFi:
            userCode.append(re.sub('[\n]', '', line).strip(" "))
    userCodeFi.close()
    os.remove("pystack.txt.tmp")
    return userCode
           
#def parseErrs():
#    stderr = getErrs()
#    errRoot = stderr[-1]
#    if "TypeError" in errRoot:
#        print errRoot
#    elif "IndexError" in errRoot:
#        print errRoot
#    elif "NameError" in errRoot:
#        print errRoot
#    elif "UnboundLocalError" in errRoot:
#        print errRoot

def searchSO(term1,term2, limit):
    user_api_key = '5se*FOHNKmiw3H9miisy8w(('
    so = stackexchange.Site(stackexchange.StackOverflow, app_key = user_api_key, impose_throttling = False)
    so.throttle_stop = False
    qs = so.search_advanced(q=term1, tagged=['python'], body=term2)
    expanded_q = []
    for q in qs:
        r = so.question(q.id, body = True, filter = "!b0OfMwwD.s*79x") 
        expanded_q.append(r)
    for i in range(limit):
        try:
            q = so.question(qs[i].id, body=True, filter = "!b0OfMwwD.s*79x")
        except IndexError:
            break
        expanded_q.append(q)
    expanded_q.sort(key=lambda x: x.up_vote_count, reverse=True)
    for i in range(limit):
        print expanded_q[i].url
def getSO(limit):
    searchSO(getErrs(), 'tuple', limit)

if __name__=="__main__":
    getSO(5)
    print getDiff()
