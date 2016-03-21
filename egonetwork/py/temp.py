import logging

try:
    import cPickle as pickle
except ImportError:
    import pickle

import networkx as nx

def cal_degree_assortativity(info):
    

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='/home/sysadmin/zhicongchen/data/phone_data/logs/' + info + '_eg2_degree_assortativity.log',
                        filemode='w')


    
    try:        
        samples = map(lambda x: x.strip('\r\n'), open('/home/sysadmin/zhicongchen/mobile-network-analysis/egonetwork/samples/' + info + '_samples.txt', 'r').readlines())
        N = len(samples)
        
        for i in range(N):
            dump_file = '/home/sysadmin/zhicongchen/data/phone_data/dumps/call_eg_dump/call_' + samples[i] + '_eg2_dump.txt'
            f = open(dump_file, 'rb')
            eg2 = pickle.load(f)
            f.close()
            r=nx.degree_assortativity_coefficient(eg2)
            #ac=nx.average_clustering(eg2)
            dc=nx.degree_centrality(eg2)
            logging.info("Sample[%d], id: " + samples[i] + ", eg2 degree_assortativity: %d", i, r)
            #logging.info("Sample[%d], id: " + samples[i] + ", eg2 average_clustering: %d", i, ac)
            logging.info("Sample[%d], id: " + samples[i] + ", eg2 degree_centrality: %d", i, dc)
    except Exception as e:
        print e
        
print "call data calcing ..."
cal_degree_assortativity('call')
#print "sms data calcing ..."
#cal_degree_assortativity('sms')
