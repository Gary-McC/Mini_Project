# -*- coding: utf-8 -*-
import hmac, hashlib, time, base64, csv, copy, sys
from datetime import datetime, timedelta
import cbpro
def datemaker(date):#input string, return date from string as list

     
    s=datetime.strftime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
    return s #returns current time from date

def aggregate(coin): #inputs:matrix to hold datapoints,coin name as a string, amount of time to run aggregate over in minutes
    #create controller variables for loop
    start_time=datetime(year=2019,month=11,day=4,hour=0,minute=0,second=0,microsecond=0)
    five_min=timedelta(minutes=5)
    one_day=timedelta(days=1)
    end_time=datetime(year=2020,month=1,day=1,hour=0,minute=0,second=0,microsecond=0)
#    end_time=start_time+timedelta(days=183)
    

#Create variables that help the loop aggregate
    cur_time=copy.deepcopy(start_time)-one_day
    while cur_time < end_time:
        cur_time=cur_time+one_day
        
        client=cbpro.PublicClient()
        dat=client.get_product_historic_rates(start=datemaker(cur_time),end=datemaker(cur_time+one_day),granularity=300,product_id=coin)
        track_time=time.localtime(float(dat[0][0]))
        track=datetime(
                year=track_time.tm_year,
                month=track_time.tm_mon,
                day=track_time.tm_mday,
                hour=track_time.tm_hour,
                minute=track_time.tm_min,
                second=track_time.tm_sec,
                microsecond=0)
        for i in range(0,len(dat)):
            cut=dat[i]
            raw_time=time.localtime(float(cut[0]))
            rest=cut[1:]
            clean_time=datetime(
                year=raw_time.tm_year,
                month=raw_time.tm_mon,
                day=raw_time.tm_mday,
                hour=raw_time.tm_hour,
                minute=raw_time.tm_min,
                second=raw_time.tm_sec,
                microsecond=0)
            while (track != clean_time):
                csvfiller([track.strftime('%H:%M:%S'),None,None,None,None,None],coin,track)
                track=track-five_min
            csvfiller([track.strftime('%H:%M:%S')]+rest,coin,track)
            track=track-five_min
        
     
                
    return
def csvfiller(Candlestick,Coin,time): #writes data into csv file
    #inputs: data to input, list of coins names   
    with open('Historic_'+Coin+'_Prices_'+time.strftime('%m_%d_%Y')+'.csv', 'a+',newline='') as csvfile: 
    # 'a+' allows you to write into an already existing csv
        adder=csv.writer(csvfile,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
        adder.writerow(Candlestick)
    csvfile.close() 
    return

Coins=  ['BTC-USD',    #1
         'ETH-USD',    #2
         'XRP-USD',    #3
         'LTC-USD',    #4
         'BCH-USD',    #5
         'EOS-USD',    #6
         'DASH-USD',   #7
         'OXT-USD',    #8
         'MKR-USD',    #9
         'XLM-USD',    #10
         'ATOM-USD',   #11
         'XTZ-USD',    #12
         'ETC-USD',    #13
         'OMG-USD',    #14
         'LINK-USD',   #15
         'REP-USD',    #16
         'ZRX-USD',    #17
         'ALGO-USD',   #18
         'DAI-USD',    #19
         'KNC-USD'     #20
         ]
aggregate(Coins[1])


