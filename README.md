# linuxSystemStats
How to access linux system statistics

## Platform: 
	• System - system type linux/windows
	• Node - node/user name
	• Release
	• Version
	• Machine - machine architecture type
	• Processor - processor details
	• Linux_distribution - name, version, code-name
	• Architecture - bit architecture, linkage
## CPU info: /proc/cpuinfo
	• No of CPU
	• Each dict per CPU model
	• Or one dict of dicts
## Memory info: /proc/meminfo
	• Same as CPU or aggregated value
## Network Stat: /proc/net/dev
	• Print rx, tx
## Process details: /proc/[int]
	• No of processes
	• Name 
	• Status
	• Memory info
	• CPU info
## Block devices: /proc/block/*
	• Mount point
	• Size
	• Used
	• Free
## All users: /etc/passwd


#### References:
http://echorand.me/site/notes/articles/python_linux/article.html
https://ruslanspivak.com/lsbaws-part3/


