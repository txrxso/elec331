# Show all interfaces
`ip addr`

`lo` - the loopback so that host machine can use it for processes on the same host to communicate.

`eth0` is for public internet access (SSH in). <br>
`eth1` is the experiment interface (the actual private link between the VMs in Cloudlab). 

For each one, `link/ether` shows the **MAC address** (e.g., 02:47:50:12:a8:78) at the link layer (network access layer). <br>`inet` shows the **IP address** for the IP layer.

Routers will only operate at network layer (IP) and lower (network access, physical). Routers look at dest IP address and decide next hop, then forwards the packet. So for the router between `juno` and `europa`, there will be 2 interfaces `eth1` and `eth2` because it connects the two (so one is the private link b/w `juno` and RTR, and the other is for `europa` and RTR).

# Neighbour Table (ARP) on RTR
`ip neigh show dev eth1`

This will show IP of Juno and MAC found on interface eth1.

Similarly, if running this on `juno`, `juno` only knows MAC address of router on interface `eth1` and oes not know the MAC address of `europa`. `europa` is on a different subnet and so traffic must go through the router.

If ran this on `juno`, then:
```
twu@juno:~$ ip neigh show dev eth1
10.0.1.10 lladdr <MAC address of RTR eth1 (link/ether field)> REACHABLE 
```
where 10.0.1.10 is the IP of the router on `eth1`.

# Getting the Route
`traceroute <dest_IP>`


# Running `netcat`
`netcat` is for reading/writing to network connections using TCP/UDP.

On `europa`: <br>
`netcat -l <PORT_NUMBER>` opens TCP port 4444 to listen for incoming connections. 

On `juno`: <br>
`netcat <DEST_IP> <PORT_NUMBER>` connects to the destination IP and uses destination port. 

`ss -p dst <DEST_IP>` shows that `juno` opened a random TCP port (e.g., 54410). DEST_IP in this case is the IP of `europa`. This should show `Local Address:Port` which is `juno`'s socket and `Peer Address:Port` which is `europa`'s socket.
Also will show the `pid` and file descriptor number used for the socket.
