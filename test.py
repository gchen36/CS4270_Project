from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.link import TCLink
from CustomTopo import *
from mininet.cli import CLI

setLogLevel('info')
linkopts1 = {'bw':50, 'delay':'5ms'}
linkopts2 = {'bw':30, 'delay':'10ms'}

topo = CustomTopo(linkopts1, linkopts2, edge_fanout=3,host_fanout=4)

net = Mininet(topo=topo, link=TCLink)
net.start()
CLI(net)
