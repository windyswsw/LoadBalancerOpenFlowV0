#!/bin/bash
ifconfig n2-eth1 hw ether 00:00:00:00:00:32
ifconfig n2-eth1 20.0.0.32 netmask 255.255.255.0
sysctl -w net.ipv4.ip_forward=1
ip route add 10.0.0.0/24 via 20.0.0.11 dev n2-eth0
ip route add 30.0.0.0/24 via 20.0.0.41 dev n2-eth1
