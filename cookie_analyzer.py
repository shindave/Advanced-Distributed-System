__author__ = 'wd2248, Wei Dai'

import pickle

cookie_class = set()
cookie_list = pickle.load(open('data/adblock_plus_cookies.p','r'))

for dic in cookie_list:
    cookie_class.add(dic['domain'])

print 'total: '+str(len(cookie_list))
print 'class: '+str(len(cookie_class))