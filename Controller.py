# Copyright (C) 2011 Nippon Telegraph and Telephone Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3, ether
from ryu.ofproto import ofproto_v1_3_parser
from ryu.ofproto import ofproto_v1_0
from ryu.ofproto import ofproto_v1_0_parser
from ryu.lib.mac import haddr_to_bin
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import ether_types
from ryu.lib.packet import ipv4
from ryu.topology import switches
from ryu.topology.event import EventSwitchEnter, EventSwitchLeave
from ryu.lib.dpid import dpid_to_str
from ryu.ofproto.ether import ETH_TYPE_8021Q


class AddRules(app_manager.RyuApp):
    _CONTEXTS = {'switches':switches.Switches,}

    @set_ev_cls(EventSwitchEnter) 
    def _ev_switch_enter_handler(self,ev):
        datapath = ev.switch.dp
        dpToStr = dpid_to_str(datapath.id)
        
        ofproto = ofproto_v1_3
        parser = ofproto_v1_3_parser

        actions = []
        match = parser.OFPMatch(eth_type = 0x806)
        actions.append(parser.OFPActionOutput(ofproto.OFPP_FLOOD))
        priority = 20
        self.add_flow(datapath,match,actions,priority)


        if (dpToStr == '0000000000000001'):

            actions1 = []
            match1 = parser.OFPMatch(in_port = 1)
            actions1.append(parser.OFPActionOutput(2))
            priority1 = 1
            self.add_flow(datapath,match1,actions1,priority1)

            actions1 = []
            match1 = parser.OFPMatch(in_port = 2)
            actions1.append(parser.OFPActionOutput(1))
            priority1 = 1
            self.add_flow(datapath,match1,actions1,priority1)

            actions1 = []
            match1 = parser.OFPMatch(in_port = 3)
            actions1.append(parser.OFPActionOutput(4))
            priority1 = 1
            self.add_flow(datapath,match1,actions1,priority1)

            actions1 = []
            match1 = parser.OFPMatch(in_port = 4)
            actions1.append(parser.OFPActionOutput(3))
            priority1 = 1
            self.add_flow(datapath,match1,actions1,priority1)

        elif (dpToStr == '0000000000000002'):

            actions1 = []
            match1 = parser.OFPMatch(in_port = 2)
            actions1.append(parser.OFPActionOutput(3))
            priority1 = 1
            self.add_flow(datapath,match1,actions1,priority1)

            actions1 = []
            match1 = parser.OFPMatch(in_port = 3)
            actions1.append(parser.OFPActionOutput(2))
            priority1 = 1
            self.add_flow(datapath,match1,actions1,priority1)

            actions1 = []
            match1 = parser.OFPMatch(in_port = 4)
            actions1.append(parser.OFPActionOutput(5))
            priority1 = 1
            self.add_flow(datapath,match1,actions1,priority1)

            actions1 = []
            match1 = parser.OFPMatch(in_port = 5)
            actions1.append(parser.OFPActionOutput(4))
            priority1 = 1
            self.add_flow(datapath,match1,actions1,priority1)

        elif (dpToStr == '0000000000000003'):
            actions1 = []
            match1 = parser.OFPMatch(eth_type=0x800, ipv4_src='20.0.0.11', ipv4_dst='20.0.0.41')
            actions1.append(parser.OFPActionOutput(4))
            priority1 = 10
            self.add_flow(datapath,match1,actions1,priority1)

	    actions1 = []
            match1 = parser.OFPMatch(eth_type=0x800, ipv4_dst='20.0.0.11', ipv4_src='20.0.0.41')
            actions1.append(parser.OFPActionOutput(1))
            priority1 = 10
            self.add_flow(datapath,match1,actions1,priority1)
            
            actions1 = []
            match1 = parser.OFPMatch(in_port = 1)
            actions1.append(parser.OFPActionOutput(2))
            priority1 = 1
            self.add_flow(datapath,match1,actions1,priority1)

            actions1 = []
            match1 = parser.OFPMatch(in_port = 2)
            actions1.append(parser.OFPActionOutput(1))
            priority1 = 1
            self.add_flow(datapath,match1,actions1,priority1)

            actions1 = []
            match1 = parser.OFPMatch(in_port = 3)
            actions1.append(parser.OFPActionOutput(4))
            priority1 = 1
            self.add_flow(datapath,match1,actions1,priority1)

            actions1 = []
            match1 = parser.OFPMatch(in_port = 4)
            actions1.append(parser.OFPActionOutput(3))
            priority1 = 1
            self.add_flow(datapath,match1,actions1,priority1)

        elif (dpToStr == '0000000000000004'):

            actions1 = []
            match1 = parser.OFPMatch(in_port = 1)
            actions1.append(parser.OFPActionOutput(2))
            priority1 = 1
            self.add_flow(datapath,match1,actions1,priority1)

            actions1 = []
            match1 = parser.OFPMatch(in_port = 2)
            actions1.append(parser.OFPActionOutput(1))
            priority1 = 1
            self.add_flow(datapath,match1,actions1,priority1)

            actions1 = []
            match1 = parser.OFPMatch(in_port = 3)
            actions1.append(parser.OFPActionOutput(4))
            priority1 = 1
            self.add_flow(datapath,match1,actions1,priority1)

            actions1 = []
            match1 = parser.OFPMatch(in_port = 4)
            actions1.append(parser.OFPActionOutput(3))
            priority1 = 1
            self.add_flow(datapath,match1,actions1,priority1)   

    def add_flow(self, datapath, match, actions, priority):

        ofproto = ofproto_v1_3
        parser = ofproto_v1_3_parser
        inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,actions)]

        mod = parser.OFPFlowMod(datapath=datapath, match=match, idle_timeout=0, hard_timeout=0, priority=priority, instructions = inst)
        datapath.send_msg(mod)
