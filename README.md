
# MOD_DPKT_PCAY #

This is a modified (extremely tiny mod) version of the pcap.py file in the dpkt library. This modification provides the pcap time stamp the whole number and the micro part of the time seperately (tv_sec,tv_usec). 
*To use this mod, download the pcap.py, compile it as follows and move it to lib location.
````
python -m compileall pcap.py
sudo mv pcap.pyc /usr/lib/pymodules/python2.7/dpkt/pcap.pyc
````
or any other location where the dpkt library is installed.
* Follow the example you would like to see implementation
