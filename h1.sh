#!/bin/bash
ip route add 20.0.0.0/24 via 10.0.0.11 dev h1-eth0
ip route add 30.0.0.0/24 via 10.0.0.11 dev h1-eth0
