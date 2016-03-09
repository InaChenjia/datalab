# txt to csv
sms_data = open('/home/sysadmin/zhicongchen/DataSets/phone_data/phone_data/tb_sms_201202.txt').readlines() 
output = open('/home/sysadmin/zhicongchen/DataSets/phone_data/phone_data/tb_sms_201202.csv', 'wb')
output.write('day_id,send_nbr,acpt_nbr,send_nbr_oprt,acpt_nbr_oprt,send_time\r\n')
for i in sms_data:
    output.write(",".join(i.split("\t")))
    
user_data = open('/home/sysadmin/zhicongchen/DataSets/phone_data/phone_data/tb_user_info_201202.txt').readlines()
output = open('/home/sysadmin/zhicongchen/DataSets/phone_data/phone_data/tb_user_201202.csv', 'wb')
output.write('ACC_NBR,URBAN_RURAL_ID,CERTI_LATN,GENDER,AGE,CUST_LEVEL,CUST_WORK_TYPE,OS_TYPE,TERMINAL_PRICE,INNET_DATE,IS_3G,IS_VIP,PROB_LEVEL,CONSUME_AMT,WEB_FEE,LOCAL_CALL_FEE,LONG_CALL_FEE,ROAM_CALL_FEE,CALL_FEE,VALUE_ADDED_FEE,SMS_FEE,STOP_CNT,OFR_CHANGE_CNT,INNET_FLOAT_AMT,INNET_DUR\r\n')
for i in user_data:
    output.write(",".join(i.split("\t")))
    
call_data = open('/home/sysadmin/zhicongchen/DataSets/phone_data/phone_data/tb_call_201202.txt').readlines()
output = open('/home/sysadmin/zhicongchen/DataSets/phone_data/phone_data/tb_call_201202.csv', 'wb')
output.write('day_id,calling_nbr,called_nbr,calling_optr,called_optr,calling_city,called_city,calling_roam_city,called_roam_city,start_time,end_time,raw_dur,call_type,calling_cell\r\n')
for i in call_data:
    output.write(",".join(i.split("\t")))