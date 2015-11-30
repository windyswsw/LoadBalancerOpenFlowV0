Read Me file will give you step by step instructions to start the controller, to start the mininet topology and to start the hosts.

(1) Start the controller
a. Copy the Controller.py to ryu/ryu/app/ folder
b. $cd ryu
c. ryu$ PYTHONPATH=. ./bin/ryu-manager ryu/app/Controller.py

(2) Start the mininet topology
$sudo python ./Topology.py

(3) Access mininet host terminals
a. Once you start the mininet topology, you will see the mininet prompt ( mininet > )
b. mininet > xterm h1 h2 n1 n2 l1 l2

(4) Configure routing for hosts
a. In each host's xterm, execute the relavant host script. (ex: in host1 xterm, execute ./h1.sh)

(5) Useful mininet commands
a. To see the mininet topology:
mininet> net

b. To see the switch rules: (ex: switch1 - s1)
mininet> sh ovs-ofctl -O OpenFlow13 dump-flows s1

(6) Stop mininet topology
a. mininet> exit
b. $sudo mn -c

(7) Stop the controller
ctrl + c
