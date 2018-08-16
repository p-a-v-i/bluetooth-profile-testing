#pyshark version == 0.3.6.2
import pyshark
capture = pyshark.LiveCapture(interface='bluetooth0', output_file='/tmp/.pcap')
capture.sniff(timeout=30)
capture

