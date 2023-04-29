# Rule-Enforcement-Verification-In-the-Data-Plane-Devices

## Introduction

The objective of this exercise is to write a P4 program that
implements Rule-Enforcement-Verification-In-the-Data-Plane-Devices. To keep things simple, we will just
implement forwarding for IPv4.

The switch will have a single table, which the control plane will
populate with static rules. Each rule will map an IP address to the
MAC address and output port for the next hop. We have already defined
the control plane rules, so you only need to implement the data plane
logic of your P4 program.

## Topology

![Frame 1](https://user-images.githubusercontent.com/85515381/235284880-59b535f2-afc2-45f8-849d-fc918c7ee1b9.png)



## How to run

Run the topology:

```
sudo p4run
```


Try to ping from one host to another:

```
mininet> h1 ping h2
```

Ping from all host pairs to test for connectivity:

```
mininet> pingall
```

In terminal run the attack login code

```
sudo python drop.py
```

Ping from all host pairs to test for connectivity:
It will drop some packets

```
mininet> pingall
```

Send traffic using xterm window:

```
mininet> xterm h1 h2
```
In xterm h1 window run receive script to receive traffic

```
sudo python receive.py
```
In xterm h2 window run send script to send traffic

```
sudo python send.py 10.0.1.1
```

To get the information of victim hosts, run:

```
sudo python read_counters.py
```

To mitigate the attack, run:

```
sudo python forward.py

```


<p>Authored By: Sudhanshu Tripathi</p>
<p>Co-authored By: Vikash Kumar</p>
