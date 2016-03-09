# dump whole graph and callers

def get_users(info):
    try:
        data  = open("/home/sysadmin/zhicongchen/DataSets/phone_data/tb_" + info + "_201202.txt", "r").readlines()
        out = open("/home/sysadmin/zhicongchen/DataSets/phone_data/tb_" + info + "_users.txt", "w")
    except Exception as e:
        print e

    for i in data:
        line = i.strip('\r\n').split('\t')
        out.write(line[1]+',')
        out.write(line[2]+'\r\n')
        
get_users("call")
get_users("sms")

def dump_relations(info):
    try:
        users = open('/home/sysadmin/zhicongchen/DataSets/phone_data/tb_' + info + '_users.txt').readlines()
    except Exception as e:
        print e
    
    import networkx as nx
    G = nx.Graph()
    callers = []
    
    for i in users:
        line = i.strip('\r\n').split(',')
        G.add_edge(line[0], line[1])
        callers.append(line[0])
    
    try:
        import cPickle as pickle
    except ImportError:
        import pickle

    try:
        f = open('../dumps/' + info + '_dump.txt', 'wb')
        pickle.dump(callers, f)
        f.close()
        
        f = open('../dumps/' + info + '_graph_dump.txt', 'wb')
        pickle.dump(G, f)
        f.close()
    except Exception as e:
        print e
    

dump_relations('call')
dump_relations('sms')