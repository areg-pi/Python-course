
import speedtest

st = speedtest.Speedtest()

option = int(input('''What speed do you want to test?
1) Download speed
2) Upload speed
3) Ping
Option: '''))

if option == '1':
    print(st.download())
elif option == '2':
    print(st.upload())
elif option == '3':
    servernames = []
    st.get_servers(servernames)
    print(st.results.ping)
else:
    print("Please enter the correct option.")