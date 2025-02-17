# Check Internet Speed
import speedtest

def check_internet_speed():
    st = speedtest.Speedtest()
    
    # Get best server based on ping
    st.get_best_server()
    
    # Measure download, upload, and ping
    download_speed = st.download() / 1_000_000  # Convert from bits/s to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert from bits/s to Mbps
    ping = st.results.ping
    
    # Print the results
    print(f"Download speed: {download_speed:.2f} Mbps")
    print(f"Upload speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping} ms")

# Call the function to check the internet speed
check_internet_speed()
