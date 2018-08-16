#pyshark version == 0.3.6.2
import pyshark
# for i in range(1,4):
#     file_path="/tmp/new_a2dp" + str(i) +  ".pcap"
#     capture = pyshark.LiveCapture(interface='bluetooth0', output_file='file_path')
#     capture.sniff(timeout=300)
print("capture started...")
capture = pyshark.LiveCapture(interface='bluetooth0', output_file='/bt/s6_2_a2dp_260.pcap')
capture.sniff(timeout=260)
print("packets captured")