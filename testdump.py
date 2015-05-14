__author__ = 'shindave'

import pickle

clist = pickle.load(open('data/disconnect_cookies.p','r'))
print clist
"""
clist = list()
alist = [{'a':1, 'b':2}, {'c':3, 'd':4}, {'e':5, 'f':6}]
blist = [{'aa':1, 'bb':2}, {'cc':3, 'dd':4}, {'ee':5, 'ff':6}]

for dic in alist:
    pfile = open('hello.p', 'wb')
    clist.append(dic)
    pickle.dump(clist, pfile)
    pfile.close()
for dic in blist:
    pfile = open('hello.p', 'wb')
    clist.append(dic)
    pickle.dump(clist, pfile)
    pfile.close()
"""