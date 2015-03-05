# NXAPI_SaveConfig

Author Ryan Tischer @ Cisco
rytische at Cisco.com

Use at your own risk


NXAPI Script to download switch configs to local system.  

Requires:

NXAPI device…Nexus 9000 with ‘feature NXAPI’ enabled.  Only works with http - change URL var on line 68 to https

Usage 

python getConfig.py node switchusername switchPassword

example:

python getConfig.py 10.91.85.182 admin cisco

————————————

GetConfig can also take in a json formatted file of nodes.  For example…

{"1" : "10.91.85.182", "2" : "10.91.85.183"}

‘elements.json provided as a reference.  

*****Assumes all nodes have the same authentication 

Example

python getConfig.py elements.json admin cisco
