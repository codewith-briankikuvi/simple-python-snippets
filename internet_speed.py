import speedtest as st

def speed_test():
    test = st.Speedtest() #Speedtest is a class

    download_speed = test.download()
    download_speed = round(download_speed / 10**6, 2) # convert from bits to Mbps
    print(f"Download speed in Mbps: {download_speed}")

    upload_speed = test.upload()
    upload_speed = round(upload_speed / 10**6, 2) # convert from bits to Mbps 
    print(f"Upload speed in Mbps: {upload_speed}")

    ping = test.results.ping
    print(f"Ping: {ping} ms")

speed_test()