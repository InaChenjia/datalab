# > nohup python my_python_program.py &

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='../logs/call_100eg3.log',
                    filemode='w')

# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
# formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# console.setFormatter(formatter)
# logging.getLogger('').addHandler(console)

# logging.warning('This is warning message')
# logging.info('This is info message')
# logging.debug('This is debug message')

def calc_eg_size(info):
    try:
        import cPickle as pickle
    except ImportError:
        import pickle
    import networkx as nx
    
    try:
        f = open('../dumps/' + info + '_graph_dump.txt', 'rb')
        G = pickle.load(f)
        f.close()
        
        samples = map(lambda x: x.strip('\r\n'), open('../samples/' + info + '_samples.txt', 'r').readlines())
        N = len(samples)
        
        for i in range(N):
            center = samples[i]
            #eg1 = nx.ego_graph(G, center, radius = 1)
            #eg2 = nx.ego_graph(G, center, radius = 2)
            eg3 = nx.ego_graph(G, center, radius = 3)
            #logging.info("Sample[%d], eg1 Size: %d", i, len(eg1.nodes()))
            #logging.info("Sample[%d], eg2 Size: %d", i, len(eg2.nodes()))
            logging.info("Sample[%d], eg3 Size: %d", i, len(eg3.nodes()))
    except Exception as e:
        print e
        
calc_eg_size('call')
calc_eg_size('sms')