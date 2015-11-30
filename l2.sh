#!/bin/bash
ifconfig l2-eth1 hw ether 00:00:00:00:00:52
ifconfig l2-eth1 30.0.0.41 netmask 255.255.255.0
ip route add 10.0.0.0/24 via 20.0.0.22 dev l2-eth0
sysctl -w net.ipv4.ip_forward=1
