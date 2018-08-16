import pyshark
avdtp_st_sus = pyshark.FileCapture('/home/user/bt_automation/bt/s6_2_a2dp_260.pcap',display_filter='btavdtp.signal_id == 7 or btavdtp.signal_id ==9')
av_len=len([i for i in avdtp_st_sus])
print("Total Available AVDTP Packets",av_len)
st=[]
for i in range(av_len):
    if('Start (Command)' in (avdtp_st_sus[i].layers[4].signal)):
        print(i)
        time = avdtp_st_sus[i].frame_info.time_relative
        st.append(time)
print("\nTime of a start command")
print(st)
sus_time=[]
for i in range(av_len):
    if('Suspend (Command)' in (avdtp_st_sus[i].layers[4].signal)):
        print(i)
        time = avdtp_st_sus[i].frame_info.time_relative
        sus_time.append(time)
print("\nTime of a suspend command")
print(sus_time)
diff=[]
for i,j in zip(st,sus_time):
    diff.append(float(j) - float(i))
print("\nTime Difference during start and suspend")
print(diff)