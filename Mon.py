import socket
import datetime
from config import dport, host1, host2

def servstatus():
    tsstat = 'Не определено'
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = dport
    conn.settimeout(5)
    conn2.settimeout(5)
#    print(host1 + ':' +str(port))
    try:
        #host = '109.87.25.174'
#        print(host1 + ':' + str(port))
        conn.connect((host1, port))
        tsstat = 'Сервер доступен по основному каналу '
#        print(tsstat+str(datetime.datetime.now()))
    except:
        tsstat = 'ISP1 is down'
        print('ISP1 is down')
        if tsstat == 'ISP1 is down':
            try:
             #   conn.close()
                #host = '77.122.30.236'
 #               print(host2 + ':' +str(port))
                conn2.connect((host2, port))
                tsstat = 'Сервер доступен по резервному каналу '
#                print(tsstat+str(datetime.datetime.now()))
            except:
#                print("ISP2 is down")
                tsstat = 'Сервер временно недоступен '
#                print(tsstat + str(datetime.datetime.now()))
            finally:
                conn2.close()
    finally:
        conn.close()
    return tsstat
print('Final '+servstatus()+str(datetime.datetime.now()))