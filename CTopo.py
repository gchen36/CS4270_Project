'''
Coursera:
- Software Defined Networking (SDN) course
-- Module 3 Programming Assignment

Professor: Nick Feamster
Teaching Assistant: Muhammad Shahbaz
'''
# SDN Project 

from mininet.topo import Topo

class CustomTopo(Topo):
    "Simple Data Center Topology"

    "linkopts - (1:core, 2:aggregation, 3: edge) parameters"
    "fanout - number of child switch per parent switch"
    def __init__(self, linkopts1={}, linkopts2={}, access_fanout=2, host_fanout=2, **opts):
        # Initialize topology and default options
        Topo.__init__(self, **opts)

        # Add your logic here ...
        self.access_fanout = access_fanout
        self.host_fanout = host_fanout

        # Create counters for Agg,Edge,Host
        counterAgg = 0
        counterEdge = 0
        counterHost = 0

        # Create Aggregate Switch
        c1 = self.addSwitch('agg1')
        # Create Tree of Switches and Hosts
        for i in range(1,access_fanout+1):
        	counterEdge += 1
        	edgeSwitch = self.addSwitch('edge%s'%counterEdge)
        	self.addLink(edgeSwitch,c1,**linkopts1)
       		for j in range(1,host_fanout+1):
       			counterHost += 1
       			host = self.addHost('h%s'%counterHost)
       			self.addLink(host,edgeSwitch,**linkopts2)
                    
topos = { 'custom': ( lambda: CustomTopo() ) }
