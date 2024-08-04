import pyshark
import requests

# Network interface and Discord webhook URL
network_interface = 'ens33'
webhook_url = 'https://discordapp.com/api/webhooks/1238797925224550471/E3SL2QdqHKjV7VubF6Wn4vq-Vrmm37rJAuDetpQc_ebJkBdsmbScCy0PEoStgegDJaGM'

# Set to store unique IPs
reported_ips = set()

def send_to_discord(message):
    data = {
        "content": message
    }
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print("Message sent successfully")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")

def capture_packets():
    capture = pyshark.LiveCapture(interface=network_interface, bpf_filter='port 22')
    for packet in capture.sniff_continuously():
        try:
            src_ip = packet.ip.src
            src_mac = packet.eth.src
            if src_ip not in reported_ips:
                reported_ips.add(src_ip)
                message = f"SSH Access - Attacker IP: {src_ip}, Attacker MAC: {src_mac}"
                print(message)
                send_to_discord(message)
        except AttributeError as e:
            # Ignore packets that don't have the expected attributes
            pass

if __name__ == "__main__":
    HOST = '0.0.0.0'

    # Welcome message
    welcome_message = """
**************************************************
*                                                *
*           Welcome to Atif Cyber World          *
*                                                *
*     If you are coming here, there must be a    *
*                    reason.                     *
*   This is a honeypot designed to capture and   *
*      monitor access attempts on various        *
*                  fake services.                *
*                                                *
*           Proceed with caution!                *
**************************************************
    """
    print(welcome_message)
    
    # Start capturing packets
    capture_packets()

