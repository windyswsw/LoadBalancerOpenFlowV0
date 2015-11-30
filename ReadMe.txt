Topology for this project can be found under "Issues" tab

This project can be used to check the client traffic flow between h1 and h2, which follows the following path:
 h1 - s1 - l1 - s1 - s3 - n1 - s3 - s2 - l2 - s2 - h2

Also it can be used to check the load balancers synchronization traffic flows, which follows the following path:
 l1 - s1 - s3 - s2 - l2
 
Client's traffic openflow rules are based on ports, while load balancers synchronization traffic flows openflow rules are based on ip addresses.

Following are the step by step instructions to start the controller, to start the mininet topology and to start the hosts.

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
