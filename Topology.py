#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def emptyNet():

    net = Mininet(controller=RemoteController, switch=OVSKernelSwitch, build=False, listenPort=6633)

    c1 = net.addController('c1', controller=RemoteController, defaultIP="127.0.0.1", port=6633)

    s1 = net.addSwitch( 's1', protocols = 'OpenFlow13' )
    s2 = net.addSwitch( 's2', protocols = 'OpenFlow13' )
    s3 = net.addSwitch( 's3', protocols = 'OpenFlow13' )
    s4 = net.addSwitch( 's4', protocols = 'OpenFlow13' )

    h1 = net.addHost( 'h1', ip='10.0.0.1/24', mac = '00:00:00:00:00:01' )
    h2 = net.addHost( 'h2', ip='30.0.0.42/24', mac = '00:00:00:00:00:42' )

    l1 = net.addHost( 'l1', ip='10.0.0.11/24', mac = '00:00:00:00:00:11' )
    l2 = net.addHost( 'l2', ip='20.0.0.41/24', mac = '00:00:00:00:00:41' )

    n1 = net.addHost( 'n1', ip='20.0.0.21/24', mac = '00:00:00:00:00:21' )
    n2 = net.addHost( 'n2', ip='20.0.0.31/24', mac = '00:00:00:00:00:31' )
 
    s1_h1 = net.addLink(s1,h1)
    s1_l1 = net.addLink(s1,l1)
    s1_l12 = net.addLink(s1,l1)
    s1_s3 = net.addLink(s1,s3)
    s1_s4 = net.addLink(s1,s4)

    s4_n2 = net.addLink(s4,n2)
    s4_n22 = net.addLink(s4,n2)
    s4_s2 = net.addLink(s4,s2)

    s3_n1 = net.addLink(s3,n1)
    s3_n12 = net.addLink(s3,n1)
    s3_s2 = net.addLink(s3,s2)

    s2_l2 = net.addLink(s2,l2)
    s2_l22 = net.addLink(s2,l2)
    s2_h2 = net.addLink(s2,h2)
   
    net.build()
    c1.start()
    s1.start([c1])
    s2.start([c1])
    s3.start([c1])
    s4.start([c1])
    net.start()
    net.staticArp()
    CLI( net )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()
