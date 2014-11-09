'''
Coursera:
- Software Defined Networking (SDN) course
-- Programming Assignment 2

Professor: Nick Feamster
Teaching Assistant: Arpit Gupta, Muhammad Shahbaz
'''

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.util import irange, dumpNodeConnections
from mininet.link import TCLink
from mininet.cli import CLI
defa = dict(bw=1000, delay='5ms', loss=1, max_queue_size=1000, use_htb=True)

class CustomTopo(Topo):
    "Simple Data Center Topology"
    "linkopts - (1:core, 2:aggregation, 3: edge) parameters"
    "fanout - number of child switch per parent switch"
    def __init__(self, linkopts1=defa, linkopts2=defa, linkopts3=defa, fanout=2, **opts):
        # Initialize topology and default options
        Topo.__init__(self, **opts)
        core = self.addSwitch('c1')
	self.fanout = fanout
	for i in irange(1,fanout):
		aggr = self.addSwitch('a%s' % i)
		self.addLink(core, aggr, **linkopts1)
		for j in irange((1+(fanout*(i-1))),fanout*i):
			edge=self.addSwitch('e%s' %j)
			self.addLink(aggr, edge, **linkopts2)
			for k in irange((1+(fanout*(j-1))),fanout*j):
		        	host=self.addHost('h%s' %k)
                		self.addLink(edge, host, **linkopts3)
## Test script##
if __name__ == '__main__':
   linkopts3 = dict(bw=100, delay='100ms', loss=1, max_queue_size=1000, use_htb=True)
   linkopts2 = dict(bw=100, delay='10ms', loss=1, max_queue_size=1000, use_htb=True)
   linkopts1 = dict(bw=1000, delay='5ms', loss=1, max_queue_size=1000, use_htb=True)
   topo=CustomTopo(linkopts1=linkopts1,linkopts2=linkopts2,linkopts3=linkopts3,fanout=2)
   net= Mininet(topo=topo, link=TCLink,controller=RemoteController)
   net.start()
#   net.pingAll()
   CLI(net)
   net.stop() 
topos = { 'custom': ( lambda: CustomTopo() ) }
