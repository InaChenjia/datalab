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
    
    out = open('./samples/' + info + '_samples.txt', 'w')
    for i in samples:
        out.write(i+'\r\n')
    out.close()
    
sampling('call')
sampling('sms')