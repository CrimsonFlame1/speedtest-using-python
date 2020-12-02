import speedtest
st = speedtest.Speedtest()
option = int(input('''What speed do you want to test:
1) Download speed
2) Upload speed
3) Ping
Your Choice: '''))
try:
    if option ==1:
        print(st.download(), 'b/s')
    elif option ==2:
        print(st.upload() , 'b/s')
    elif option ==3:
        servernames= []
        st.get_servers(servernames)
        print(st.results.ping, 'b/s')
except:
    print("Please enter the correct choice!")
