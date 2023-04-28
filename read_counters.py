from p4utils.utils.topology import Topology
from p4utils.utils.sswitch_API import SimpleSwitchAPI
import sys
import time

class ReadCounters(object):

    def __init__(self, sw_name):

        self.topo = Topology(db="topology.db")
        self.sw_name = sw_name
        self.thrift_port = self.topo.get_thrift_port(sw_name)
        self.controller = SimpleSwitchAPI(self.thrift_port)


    def direct(self):

        entries = self.controller.table_num_entries("count_table")
        for i in range(int(entries)):
            self.controller.counter_read("direct_port_counter", i)


    def indirect(self):
        count = []   

        for i in range(5):
            # self.controller.counter_read("port_counter", i)
            count.append(self.controller.counter_read("port_counter", i).packets)

        return count





if __name__ == "__main__":
    flag = 1
    while(flag):
        s1 = ReadCounters("s1").indirect()
        
        for j in s1:
            if((s1[2] - s1[1] > 60) or (s1[3] - s1[1] > 20)):
                print('No Talk from h2 to h1')

                
        time.sleep(2)
        s5 = ReadCounters("s5").indirect()
        
        for j in s1:
            if((s5[2] - s5[1] > 60) or (s5[3] - s5[1] > 20)):
                print('No Talk from h2 to h5')

        time.sleep(2)

