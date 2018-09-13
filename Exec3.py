# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 11:35:17 2018

@author: syadava
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
import http.client
import threading
import time


    
def Console_Proxy(url, apiEndUrl):
    session = requests.Session()
    session.verify = False
    conn = http.client.HTTPSConnection(url)
    headers = {
    'content-type': "application/*+xml;version=30.0",
    'authorization': "Basic YWRtaW5pc3RyYXRvckBTeXN0ZW06Y2EkaGMwdw==",
    'accept': "application/*+xml;version=30.0",
    'x-vcloud-authorization': "1333248a43c34c6ebde88bea805ef307",
    'cache-control': "no-cache",
    'postman-token': "149e1b0c-8c61-68b4-9cd1-76d6d3c43d36"
    }
    conn.request("POST", apiEndUrl, headers=headers)
 
    res = conn.getresponse()
    print(res.code)
    data = res.read()
    readData(res)
    print(data.decode("utf-8"))
    
def readData(Ress):
    f = open('urltest4.txt','w')
    data=Ress.read()
    f.write(data.decode("utf-8"))
    f.close()

def prepareCall(list2):
    #print(test)
    #vmid="/api/vApp/vm-005fefcc-204d-47f8-aecf-31f9859eb002/screen/action/acquireTicket"
    for x in range(2):
        for y in range(201, 300):
            t1 = threading.Thread(target=Console_Proxy, args=("stella-vcd1.eng.vmware.com",list[y]))
            t1.start()
            t1.join()
            t2 = threading.Thread(target=Console_Proxy, args=("stella-vcd2.eng.vmware.com",list[y+x],))
#            t3 = threading.Thread(target=Console_Proxy, args=("stella-vcd3.eng.vmware.com","/api/vApp/vm-89daba4a-99e8-4ed4-90e8-008105dd7201/screen/action/acquireTicket",))
#            t4 = threading.Thread(target=Console_Proxy, args=("stella-vcd4.eng.vmware.com","/api/vApp/vm-89daba4a-99e8-4ed4-90e8-008105dd7201/screen/action/acquireTicket",))
#            t5 = threading.Thread(target=Console_Proxy, args=("stella-vcd5.eng.vmware.com","/api/vApp/vm-89daba4a-99e8-4ed4-90e8-008105dd7201/screen/action/acquireTicket",))
#            t6 = threading.Thread(target=Console_Proxy, args=("stella-vcd1.eng.vmware.com","/api/vApp/vm-89daba4a-99e8-4ed4-90e8-008105dd7201/screen/action/acquireTicket",))
#            t7 = threading.Thread(target=Console_Proxy, args=("stella-vcd2.eng.vmware.com","/api/vApp/vm-89daba4a-99e8-4ed4-90e8-008105dd7201/screen/action/acquireTicket",))
#        t8 = threading.Thread(target=Console_Proxy, args=("stella-vcd3.eng.vmware.com","/api/vApp/vm-89daba4a-99e8-4ed4-90e8-008105dd7201/screen/action/acquireTicket",))
#        t9 = threading.Thread(target=Console_Proxy, args=("stella-vcd4.eng.vmware.com","/api/vApp/vm-89daba4a-99e8-4ed4-90e8-008105dd7201/screen/action/acquireTicket",))
#        t10 = threading.Thread(target=Console_Proxy, args=("stella-vcd5.eng.vmware.com","/api/vApp/vm-89daba4a-99e8-4ed4-90e8-008105dd7201/screen/action/acquireTicket",))
#        t11 = threading.Thread(target=Console_Proxy, args=("stella-vcd1.eng.vmware.com","/api/vApp/vm-89daba4a-99e8-4ed4-90e8-008105dd7201/screen/action/acquireTicket",))
#        t12 = threading.Thread(target=Console_Proxy, args=("stella-vcd2.eng.vmware.com","/api/vApp/vm-89daba4a-99e8-4ed4-90e8-008105dd7201/screen/action/acquireTicket",))
#        t13 = threading.Thread(target=Console_Proxy, args=("stella-vcd3.eng.vmware.com","/api/vApp/vm-89daba4a-99e8-4ed4-90e8-008105dd7201/screen/action/acquireTicket",))
#        t14 = threading.Thread(target=Console_Proxy, args=("stella-vcd4.eng.vmware.com","/api/vApp/vm-89daba4a-99e8-4ed4-90e8-008105dd7201/screen/action/acquireTicket",))
#        t15 = threading.Thread(target=Console_Proxy, args=("stella-vcd5.eng.vmware.com","/api/vApp/vm-89daba4a-99e8-4ed4-90e8-008105dd7201/screen/action/acquireTicket",))
#        t16 = threading.Thread(target=Console_Proxy, args=("stella-vcd1.eng.vmware.com","/api/vApp/vm-89daba4a-99e8-4ed4-90e8-008105dd7201/screen/action/acquireTicket",))
#        t17 = threading.Thread(target=Console_Proxy, args=("stella-vcd2.eng.vmware.com","/api/vApp/vm-89daba4a-99e8-4ed4-90e8-008105dd7201/screen/action/acquireTicket",))
#        t18 = threading.Thread(target=Console_Proxy, args=("stella-vcd3.eng.vmware.com","/api/vApp/vm-89daba4a-99e8-4ed4-90e8-008105dd7201/screen/action/acquireTicket",))
#        t19 = threading.Thread(target=Console_Proxy, args=("stella-vcd4.eng.vmware.com","/api/vApp/vm-89daba4a-99e8-4ed4-90e8-008105dd7201/screen/action/acquireTicket",))
#        t20 = threading.Thread(target=Console_Proxy, args=("stella-vcd5.eng.vmware.com","/api/vApp/vm-89daba4a-99e8-4ed4-90e8-008105dd7201/screen/action/acquireTicket",))
#        t21 = threading.Thread(target=Console_Proxy, args=("stella-vcd1.eng.vmware.com","/api/vApp/vm-89daba4a-99e8-4ed4-90e8-008105dd7201/screen/action/acquireTicket",))
#        t22 = threading.Thread(target=Console_Proxy, args=("stella-vcd2.eng.vmware.com","/api/vApp/vm-89daba4a-99e8-4ed4-90e8-008105dd7201/screen/action/acquireTicket",))
#        t23 = threading.Thread(target=Console_Proxy, args=("stella-vcd3.eng.vmware.com","/api/vApp/vm-89daba4a-99e8-4ed4-90e8-008105dd7201/screen/action/acquireTicket",))
#        t24 = threading.Thread(target=Console_Proxy, args=("stella-vcd4.eng.vmware.com","/api/vApp/vm-89daba4a-99e8-4ed4-90e8-008105dd7201/screen/action/acquireTicket",))
#        t25 = threading.Thread(target=Console_Proxy, args=("stella-vcd5.eng.vmware.com","/api/vApp/vm-89daba4a-99e8-4ed4-90e8-008105dd7201/screen/action/acquireTicket",))
#        t26 = threading.Thread(target=Console_Proxy, args=("stella-vcd1.eng.vmware.com","/api/vApp/vm-89daba4a-99e8-4ed4-90e8-008105dd7201/screen/action/acquireTicket",))
#        t27 = threading.Thread(target=Console_Proxy, args=("stella-vcd2.eng.vmware.com","/api/vApp/vm-89daba4a-99e8-4ed4-90e8-008105dd7201/screen/action/acquireTicket",))
#        t28 = threading.Thread(target=Console_Proxy, args=("stella-vcd3.eng.vmware.com","/api/vApp/vm-89daba4a-99e8-4ed4-90e8-008105dd7201/screen/action/acquireTicket",))
#        t29 = threading.Thread(target=Console_Proxy, args=("stella-vcd4.eng.vmware.com","/api/vApp/vm-55922fbd-6f55-4b12-9677-cbbe6fb4e4c4/screen/action/acquireTicket",))
#        t30 = threading.Thread(target=Console_Proxy, args=("stella-vcd5.eng.vmware.com","/api/vApp/vm-55922fbd-6f55-4b12-9677-cbbe6fb4e4c4/screen/action/acquireTicket",))
#        t31 = threading.Thread(target=Console_Proxy, args=("stella-vcd6.eng.vmware.com","/api/vApp/vm-55922fbd-6f55-4b12-9677-cbbe6fb4e4c4/screen/action/acquireTicket",))
#        t32 = threading.Thread(target=Console_Proxy, args=("stella-vcd7.eng.vmware.com","/api/vApp/vm-55922fbd-6f55-4b12-9677-cbbe6fb4e4c4/screen/action/acquireTicket",))
#        t33 = threading.Thread(target=Console_Proxy, args=("stella-vcd10.eng.vmware.com","/api/vApp/vm-55922fbd-6f55-4b12-9677-cbbe6fb4e4c4/screen/action/acquireTicket",))
#        t34 = threading.Thread(target=Console_Proxy, args=("stella-vcd11.eng.vmware.com","/api/vApp/vm-55922fbd-6f55-4b12-9677-cbbe6fb4e4c4/screen/action/acquireTicket",))
#        t35 = threading.Thread(target=Console_Proxy, args=("stella-vcd13.eng.vmware.com","/api/vApp/vm-55922fbd-6f55-4b12-9677-cbbe6fb4e4c4/screen/action/acquireTicket",))
#        t36 = threading.Thread(target=Console_Proxy, args=("stella-vcd14.eng.vmware.com","/api/vApp/vm-55922fbd-6f55-4b12-9677-cbbe6fb4e4c4/screen/action/acquireTicket",))
#        t37 = threading.Thread(target=Console_Proxy, args=("stella-vcd1.eng.vmware.com","/api/vApp/vm-55922fbd-6f55-4b12-9677-cbbe6fb4e4c4/screen/action/acquireTicket",))
#        t38 = threading.Thread(target=Console_Proxy, args=("stella-vcd2.eng.vmware.com","/api/vApp/vm-55922fbd-6f55-4b12-9677-cbbe6fb4e4c4/screen/action/acquireTicket",))
#        t39 = threading.Thread(target=Console_Proxy, args=("stella-vcd15.eng.vmware.com","/api/vApp/vm-55922fbd-6f55-4b12-9677-cbbe6fb4e4c4/screen/action/acquireTicket",))
#        t40 = threading.Thread(target=Console_Proxy, args=("stella-vcd4.eng.vmware.com","/api/vApp/vm-55922fbd-6f55-4b12-9677-cbbe6fb4e4c4/screen/action/acquireTicket",))
#        t41 = threading.Thread(target=Console_Proxy, args=("stella-vcd23.eng.vmware.com","/api/vApp/vm-55922fbd-6f55-4b12-9677-cbbe6fb4e4c4/screen/action/acquireTicket",))
#        t42 = threading.Thread(target=Console_Proxy, args=("stella-vcd22.eng.vmware.com","/api/vApp/vm-55922fbd-6f55-4b12-9677-cbbe6fb4e4c4/screen/action/acquireTicket",))
#        t43 = threading.Thread(target=Console_Proxy, args=("stella-vcd25.eng.vmware.com","/api/vApp/vm-55922fbd-6f55-4b12-9677-cbbe6fb4e4c4/screen/action/acquireTicket",))
#        t44 = threading.Thread(target=Console_Proxy, args=("stella-vcd24.eng.vmware.com","/api/vApp/vm-55922fbd-6f55-4b12-9677-cbbe6fb4e4c4/screen/action/acquireTicket",))
#        t45 = threading.Thread(target=Console_Proxy, args=("stella-vcd15.eng.vmware.com","/api/vApp/vm-55922fbd-6f55-4b12-9677-cbbe6fb4e4c4/screen/action/acquireTicket",))
#        t46 = threading.Thread(target=Console_Proxy, args=("stella-vcd22.eng.vmware.com","/api/vApp/vm-55922fbd-6f55-4b12-9677-cbbe6fb4e4c4/screen/action/acquireTicket",))
#        t47 = threading.Thread(target=Console_Proxy, args=("stella-vcd22.eng.vmware.com","/api/vApp/vm-55922fbd-6f55-4b12-9677-cbbe6fb4e4c4/screen/action/acquireTicket",))
#       
#       
#       
#        
#        
#        
#        
            
            t2.start()
#             t3.start()
#             t4.start()
#             t5.start()
#             t6.start()
#             t7.start()
#        t8.start()
#        t9.start()
#        t10.start()
#        t11.start()
#        t12.start()
#        t13.start()
#        t14.start()
#        t15.start()
#        t16.start()
#        t17.start()
#        t18.start()
#        t19.start()
#        t20.start()
#        t21.start()
#        t22.start()
#        t23.start()
#        t24.start()
#        t25.start()
#        t26.start()
#        t27.start()
#        t28.start()
#        t29.start()
#        t30.start()
#        
#        t31.start()
#        t32.start()
#        t33.start()
#        t34.start()
#        t35.start()
#        t36.start()
#        t37.start()
#        t38.start()
#        t39.start()
#        t40.start()
#        t41.start()
#        t42.start()
#        t43.start()
#        t44.start()
#        t45.start()
#        t46.start()
#        t47.start()
#       
#        
#       
#        
#        
#        
            
            t2.join()
#             t3.join()
#             t4.join()
#             t5.join()
#             t6.join()
#             t7.join()
#        t8.join()
#        t9.join()
#        t10.join()
#        t11.join()
#        t12.join()
#        t13.join()
#        t14.join()
#        t15.join()
#        t16.join()
#        t17.join()
#        t18.join()
#        t19.join()
#        t20.join()
#        t21.join()
#        t22.join()
#        t23.join()
#        t24.join()
#        t25.join()
#        t26.join()
#        t27.join()
#        t28.join()
#        t29.join()
#        t30.join()
#        
#        t31.join()
#        t32.join()
#        t33.join()
#        t34.join()
#        t35.join()
#        t36.join()
#        t37.join()
#        t38.join()
#        t39.join()
#        t40.join()
#        t41.join()
#        t42.join()
#        t43.join()
#        t44.join()
#        t45.join()
#        t46.join()
#        t47.join()
            
            
         


if __name__ == "__main__":
    list=[]
    f = open('urltest2.txt','r')
    line = f.readline()
    while line:
        print(line.strip())
        list.append(line.strip())
        line = f.readline()  
    f.close()
    print(len(list))
    prepareCall(list)
    
       
      
      
      
        
        
    
	
    

