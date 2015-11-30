#!/bin/bash
ip route add 10.0.0.0/24 via 30.0.0.41 dev h2-eth0
ip route add 20.0.0.0/24 via 30.0.0.41 dev h2-eth0
