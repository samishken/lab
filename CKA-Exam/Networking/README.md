# Networking

### Switching and Routing
##### Switching: 
- - Switch connects two systmes by creating a network (192.168.1.0) within the same network. 
- - Both systems need to have a INTERFACE (physical or virtual).  Interface names (eth0)
- - System A has Interface called eth0 uses SWITCH to connect with System B with Interface eth0
- - (System-A - Interface - eth0) <----SWITCH----> (eth0 - Interface - System-B)
- - "ip link" command to see the Interface for the host.
##### Routing
- - Router helps connect systems that are in different network.
- - Since it connects two networks, it gets two IPs assigned.
- - (192.168.1.11) <---- ROUTER ----> (192.168.2.10)

##### Default Gateway
- - Gateway allows a system to communicate with another system in different network.
- - System A need to pass through a GATEWAY before reaching ROUTER to reach another system in different network.
- - `ip route add <IP-ADDRESS> via <IP-ADDRESS>`
- - `cat /proc/sys/net/ipv4/ip_forward`
- - `echo 1 > /proc/sys/net/ipv4/ip_forward`


##### key command lines (restart needed after changes)
- - `ip link`: list & modify interfaces
- - `ip addr`: ip address assigned to interfaces
- - `ip addr add`: used to set IP addresses on the interfaces (`ip add add 192.168.10/24 dev eth0`)
- - `ip route`: used to view routing table
- - `ip route add`: used to add entries into the routing table.
- - `cat /proc/sys/net/ipv4/ip_forward`: used to check "IP FORWARDING" is enabled on a host.
- - `arp`: used to display and modify the Address Resolution Protocol (ARP) cache. run arp <node_name> to resolve the node's MAC address.
- - `netstat -plnt`: tool for retrieving network statistics.
- - `ip address show type bridge`
- - kube-scheduler port listening on `netstat -npl | grep -i scheduler -n`
- - To Inspect the kubelet service and identify the container runtime endpoint value is set for k8s `ps -aux | grep -i kubelet`
- - To get POD IP address range configured by plugin (weave): ``
- - 

### DNS
##### DNS Configurations on host (Linux)
- - host A vs host B (db)
- - `cat >> /etc/hosts` -> (add: 192.168.1.11   db)
- - If add `db is 192.168.1.11` then we can use `ping db` to connect from another host.
- - a "DNS SERVER" was created so we stop updating the `/etc/hosts` file whenever their is a change
- - by default `/etc/hosts` has more power than "DNS SERVER".  This can be changed at `/etc/nsswitch.conf` file. In this file we 
- - add `Forward All to 8.8.8.8.` to forward any unknown hostnames to the public name server on the internet.
- - "DOMAIN NAME" (www.google.com)
- - ".com" - top-level domain
- - "google": domain name 
- - "www": subdomain. Subdomains help in further grouping things together. 
- - (maps.google.com), apps.google.com, mail.google.com
- - `nslookup google.com`
- - `dig www.google.com`

##### CoreDNS Introduction
- -
### Network Namespaces
- - provides privacy
- - List namespaces (`ip netns`)
- - Create namespace on linux (`ip netns add red` `ip netns add blue`)
- - move default namespace to custom ns called red `ip netns exec red ip link` (`ip -n exec red ip link`)
- - Connect two namespaces 
- - - - FIRST (`ip link add veth-red type veth peer name veth-blue`): creates a pipe. connect the red and blue namespaces
- - - - SECOND (`ip link set veth-red netns red`) (`ip link set veth-blue netns blue`)attach each interface to the appropriate namespace.
- - - - THIRD (`ip -n red addr add 192.168.15.1 veth-red`) (`ip -n blue addr add 192.168.15.2 veth-blue`)  attach IP addresses to each namespace
- - - - FINALLY (`ip -n red link set veth-red up`) (`ip -n blue link set veth-blue up`)  Turn on the ip link setup command for each device within their respective namespace.  when the links are up, the namespaces can reach one another.
- - - - DELETE (`ip -n red link del veth-red`) the other side (blue) will automatically delete too.

##### for multiple namespaces
- Linux Bridge 
- create linux bridge (`ip link add v-net-0 type bridge`)
- create cable for the name spaces.
- - - - add namesapces to this bridge network (`ip link add veth-add type peer name veth-red-br`)
- - - - add namesapces to this bridge network (`ip link add veth-add type peer name veth-blue-br`)
- connect/add one end of the cable into Bridge network and the other to the namespaces
- - - - `ip link set veth-red netns red`
- - - - `ip link set veth-red-br master v-net-0`
- - - - `ip link set veth-blue netns blue`
- - - - `ip link set veth-blue-br master v-net-0`
-  attach IP addresses to each namespace (`ip -n red addr add 192.168.15.1 veth-red`) (`ip -n blue addr add 192.168.15.2 veth-blue`)
- - - - FINALLY turn the devices up (`ip -n red link set veth-red up`) (`ip -n blue link set veth-blue up`)  


### Docker Networking
##### Bridge
- when docker is installed on a host it creates an internal private network called bridge by default.
- - - - Create network namespace
- - - - create bridge network/Interface
- - - - create VETH Pairs (Pipe, virtual Cable)
- - - - Attach vETH to namespace
- - - - Attache other vEth to Bridge
- - - - Assign IP Addresses
- - - - Bring the interfaces up
- - - - Enable NAT-IP Masquerade

##### CNI (Container Networking Interface)
- CNI defines the responsibilities of container runtime as per CNI container runtimes.
- configure k8s to use network plugins
- Container runtime is the component responsible for creating containers... then invoke the appropriate netwok plugin after the container is created.
- All CNI supported plugins are stored under `/opt/cni/bin`
- to see which CNI plugin is configured to be used in our k8s cluster  `ls /etc/cni/net.d`

##### Networking Cluster Nodes
- Each node must have al least one interface connected to a network. 
- Each interface must have an address configured.

##### Pod Networking
- Every POD should have an IP Address
- Every POD should be able to communicate with every other POD in the same node
- Every POD should be able to communicate with every other POD on other nodes without NAT.
- Bridge network: 
- 