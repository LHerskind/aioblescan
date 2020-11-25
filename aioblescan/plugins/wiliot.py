#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#
# This file deals with the Wiliot formatted message
from struct import unpack
import aioblescan as aios
from datetime import datetime

WILIOT = 1280

class Wiliot(object):
    """
    Class defining the content of a Wiliot tag advertisement
    """

    def decode(self, packet):
        data = {}
        man_id = packet.retrieve("Manufacturer ID")
        if man_id:
            man_id = man_id[0].val
            if man_id == WILIOT:
                currentTime = datatime.now()
                data["time"] = currentTime.strftime("%H:%M:%S")
                payload = packet.retrieve("Payload")
                if payload:
                    data["payload"] = payload[0].val.hex()
                address = packet.retrieve("peer")
                if address:
                    data["ble-addr"] = address[0].val
        return data