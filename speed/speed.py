import speedtest as st

def Speed_Test():
    test = st.Speedtest()
    
    down_speed = test.download()
    down_speed = round(down_speed / 10**6, 2)
    print(f"Download Speed: {down_speed} Mbps")
    
    up_speed = test.upload()
    up_speed = round(up_speed / 10**6, 2)
    print(f"Upload Speed: {up_speed} Mbps")
    
    ping = test.results.ping
    print(f"Ping: {ping} ms")

def main():
    Speed_Test()


if __name__ == "__main__":
    main()
