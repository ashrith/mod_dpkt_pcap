#! /usr/bin/env python

#================================================
# Example Python Script to parse pcap files
#================================================

import dpkt, sys, socket, binascii

if len(sys.argv) < 3 or len(sys.argv) > 3:
        print "Usage:\n",sys.argv[0], "filename.pcap", "filename.txt"
        sys.exit()

def parse_pcap(self,outfile):
        sys.stdout = outfile
        for ts, tus, buf in self:
                try: eth = dpkt.ethernet.Ethernet(buf)
                except:continue
                try: ip = eth.data
                except:continue
                if ip.p != 17:continue
                try: udp = ip.data
                except:continue
                try: dns = dpkt.dns.DNS(udp.data)
                except:continue
                if not dns.qd:continue
                else:  
                        for qus in dns.qd:
                                print "%i.%i"%(ts,tus),"\t", socket.inet_ntoa(ip.dst),"\t",dns.rcode,"\t",repr(qus.name),
                                if not dns.an: 
                                                print "\t","'NA'",
                                else:  
                                        for ans in dns.an:
                                                        if ans.type == 1:print "\t","'%s'"%(socket.inet_ntoa(ans.rdata)),
                                                        elif ans.type == 16:print"\t","'TXT'",
                                print

        return


f = open(sys.argv[1])
outfile = open(sys.argv[2],"w")
try:   
        pcap = dpkt.pcap.Reader(f)
        parse_pcap(pcap,outfile)
finally:
        f.close()
        outfile.close()

#example timestamp 1004345839.000100
#ts is the integer part of the timestamp 1004345839
#tus is the decimal part of the timestamp 000100
