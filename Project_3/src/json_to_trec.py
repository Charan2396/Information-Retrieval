# -*- coding: utf-8 -*-


import json
# if you are using python 3, you should 
import urllib.request 
#import urllib2


# change the url according to your own corename and query

#inurl = 'http://localhost:8983/solr/BM25/select?fl=*,score&indent=on&q=Russia%27s%20intervention%20in%20Syria&rows=20&wt=json'
outfn = '1.txt'

# change query id and IRModel name accordingly
qid = '001'
IRModel='BM25'
outf = open(outfn, 'w+')
#data = urllib2.urlopen(inurl)
# if you're using python 3, you should use
#data = urllib.request.urlopen(inurl)


# the ranking should start from 1 and increase
rank = 1
x=[]
with open('testqueries.txt', 'r') as f:
    for l in f:
        
        q=l.strip('\n').replace(':','')
        q=urllib.parse.quote(q)
        #qid=l.split(' ', 1)[0]
        inurl = 'http://localhost:8983/solr/BM25/select?fl=*,score&indent=on&q='+q+'&rows=20&wt=json'
        data = urllib.request.urlopen(inurl)
        docs = json.load(data)['response']['docs']
        for doc in docs:
            outf.write(qid + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + IRModel + '\n')
            rank += 1
outf.close()
