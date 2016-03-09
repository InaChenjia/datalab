# > nohup python my_python_program.py &

# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
# formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# console.setFormatter(formatter)
# logging.getLogger('').addHandler(console)

# logging.warning('This is warning message')
# logging.info('This is info message')
# logging.debug('This is debug message')

def sampling(info):
    try:
        import cPickle as pickle
    except ImportError:
        import pickle
        
    f = open('/home/sysadmin/zhicongchen/DataSets/phone_data/dumps/' + info + '_dump.txt', 'rb')
    callers = pickle.load(f)
    f.close()
    print len(callers)
    
    import pandas as pd
    user_data = pd.read_csv('/home/sysadmin/zhicongchen/DataSets/phone_data/tb_user_info_201202.csv')
    acc_nbrs = list(user_data['ACC_NBR'])
    acc_nbrs = map(lambda x: str(x), acc_nbrs)
    acc_nbrs = set(acc_nbrs)
    callers_distinct = list(set(callers) & acc_nbrs)
    
    import random
    N = len(callers_distinct)
    n = 1000
    samples = [callers_distinct[int(random.random()*N)] for i in range(n)]
    
    out = open('/home/sysadmin/zhicongchen/mobile-network-analysis/egonetwork/samples/' + info + '_samples.txt', 'w')
    for i in samples:
        out.write(i+'\r\n')
    out.close()

def calc_eg_size(info):
    import logging

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='/home/sysadmin/zhicongchen/mobile-network-analysis/egonetwork/logs/' + info + '_eg3size.log',
                        filemode='w')

    try:
        import cPickle as pickle
    except ImportError:
        import pickle
    import networkx as nx
    
    try:
        f = open('/home/sysadmin/zhicongchen/DataSets/phone_data/dumps/' + info + '_graph_dump.txt', 'rb')
        G = pickle.load(f)
        f.close()
        
        samples = map(lambda x: x.strip('\r\n'), open('/home/sysadmin/zhicongchen/mobile-network-analysis/egonetwork/samples/' + info + '_samples.txt', 'r').readlines())
        N = len(samples)
        
        for i in range(N):
            center = samples[i]
            #eg1 = nx.ego_graph(G, center, radius = 1)
            #eg2 = nx.ego_graph(G, center, radius = 2)
            eg3 = nx.ego_graph(G, center, radius = 3)
            #logging.info("Sample[%d], eg1 Size: %d", i, len(eg1.nodes()))
            #logging.info("Sample[%d], eg2 Size: %d", i, len(eg2.nodes()))
            logging.info("Sample[%d], id: " + samples[i] + ", eg3 Size: %d", i, len(eg3.nodes()))
    except Exception as e:
        print e

#print "call data sampling ..."
#sampling('call')
#print "sms data sampling ..."
#sampling('sms')

#print "call data calcing ..."
#calc_eg_size('call')
print "sms data calcing ..."
calc_eg_size('sms')