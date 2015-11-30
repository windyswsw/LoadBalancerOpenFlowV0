#!/bin/bash
ifconfig l1-eth1 hw ether 00:00:00:00:00:51
ifconfig l1-eth1 20.0.0.11 netmask 255.255.255.0
ip route add 30.0.0.0/24 via 20.0.0.21 dev l1-eth1
sysctl -w net.ipv4.ip_forward=1
