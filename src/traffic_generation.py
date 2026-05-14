from mininet.node import Controller
from mininet.log import setLogLevel, info

from mn_wifi.net import Mininet_wifi
from mn_wifi.cli import CLI
from mn_wifi.link import wmediumd
from mn_wifi.wmediumdConnector import interference

import time
import random


def traffic_topology():

    net = Mininet_wifi(
        controller=Controller,
        link=wmediumd,
        wmediumd_mode=interference
    )

    info("*** Creating Controller\n")
    c0 = net.addController('c0')

    info("*** Creating Access Points\n")

    ap1 = net.addAccessPoint(
        'ap1',
        ssid='ap1-ssid',
        mode='g',
        channel='1',
        position='30,50,0'
    )

    ap2 = net.addAccessPoint(
        'ap2',
        ssid='ap2-ssid',
        mode='g',
        channel='6',
        position='70,50,0'
    )

    info("*** Creating Stations\n")

    stations = []

    for i in range(1, 11):

        sta = net.addStation(
            f'sta{i}',
            ip=f'10.0.0.{i}/8',
            position=f'{10+i*5},20,0'
        )

        stations.append(sta)

    info("*** Configuring WiFi Nodes\n")

    net.configureWifiNodes()

    net.plotGraph(max_x=100, max_y=100)

    info("*** Configuring Mobility\n")

    net.startMobility(time=0)

    for i, sta in enumerate(stations):

        net.mobility(
            sta,
            'start',
            time=1,
            position=f'{10+i*5},20,0'
        )

        net.mobility(
            sta,
            'stop',
            time=20,
            position=f'{80-i*2},80,0'
        )

    net.stopMobility(time=25)

    info("*** Starting Network\n")

    net.build()

    c0.start()

    ap1.start([c0])
    ap2.start([c0])

    info("*** Starting iperf Servers\n")

    stations[0].cmd('iperf -s &')
    stations[1].cmd('iperf -s &')

    time.sleep(2)

    info("*** Generating Traffic\n")

    for i in range(2, 10):

        target = random.choice([stations[0], stations[1]])

        bandwidth = random.randint(1, 10)

        stations[i].cmd(
            f'iperf -c {target.IP()} -t 30 -i 1 -b {bandwidth}M &'
        )

    info("*** Traffic Running\n")

    CLI(net)

    info("*** Stopping Network\n")

    net.stop()


if __name__ == '__main__':

    setLogLevel('info')

    traffic_topology()


