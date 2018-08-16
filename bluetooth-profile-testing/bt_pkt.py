import pyshark
src_adrs = 'd8:32:e3:38:02:9d'
start = pyshark.FileCapture('/home/user/mi_cw_a2dp.pcap',display_filter='btavdtp.signal_id == 7 or btavdtp.signal_id ==9 ')
#suspend = pyshark.FileCapture('/home/user/mi_cw_a2dp.pcap',display_filter='btavdtp.signal_id ==9')
#av_len=len([i for i in avdtp])
#print(av_len)
st_len=len([i for i in start])
print(st_len)
st=[]
for i in range(0,st_len,4):
    print(i)
    time = start[i].frame_info.time_relative
    st.append(time)
print(st)
sus_time=[]
for i in range(2,st_len,4):
    print(i)
    time = start[i].frame_info.time_relative
    sus_time.append(time)
print(sus_time)
#sus_len=len([i for i in suspend])
#print(sus_len)
diff=[]
for i,j in zip(st,sus_time):
    #difference = float(st[i]) - float(sus_time[i])
    diff.append (float(j) - float(i))
print(diff)
