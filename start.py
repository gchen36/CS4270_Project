from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.node import Controller, RemoteController
from mininet.log import setLogLevel
from mininet.link import TCLink
from CTopo import *
from mininet.cli import CLI

setLogLevel('info')
linkopts1 = {'bw':50, 'delay':'5ms'}
linkopts2 = {'bw':30, 'delay':'10ms'}

#topo = CustomTopo(linkopts1, linkopts2, access_fanout=2,host_fanout=2)
topo = CustomTopo(access_fanout=2,host_fanout=2)

net = Mininet(topo=topo,
 controller=lambda name: RemoteController( name, ip='127.0.0.1' ),listenPort=6633)
net.start()
CLI(net)
