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
        f = open('/home/sysadmin/zhicongchen/data/phone_data/dumps/' + info + '_graph_dump.txt', 'rb')
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
        
#print "call data calcing ..."
#calc_eg_size('call')
#print "sms data calcing ..."
#calc_eg_size('sms')