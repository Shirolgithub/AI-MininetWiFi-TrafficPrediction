from mininet.node import Controller
from mininet.log import setLogLevel, info

from mn_wifi.net import Mininet_wifi
from mn_wifi.cli import CLI
from mn_wifi.link import wmediumd
from mn_wifi.wmediumdConnector import interference


def topology():

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
            position=f'{10 + i*5},20,0'
        )

        stations.append(sta)

    info("*** Configuring WiFi Nodes\n")
    net.configureWifiNodes()

    info("*** Plotting Network Graph\n")
    net.plotGraph(max_x=100, max_y=100)

    info("*** Starting Network\n")

    net.build()

    c0.start()

    ap1.start([c0])
    ap2.start([c0])

    info("*** Testing Connectivity\n")

    net.pingAll()

    info("*** Running CLI\n")

    CLI(net)

    info("*** Stopping Network\n")

    net.stop()


if __name__ == '__main__':

    setLogLevel('info')

    topology()
