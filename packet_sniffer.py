from scapy.all import sniff, Raw

def packet_callback(packet):
    print("=" * 80)
    print("Packet Summary:", packet.summary())

    # Try to decode the payload if available
    if Raw in packet:
        try:
            payload = packet[Raw].load
            decoded_payload = payload.decode("utf-8", errors="replace")  # Replace undecodable parts
            print("Payload (decoded):")
            print(decoded_payload)
        except Exception as e:
            print("Payload could not be decoded:", e)

# Sniff packets
sniff(count=10, prn=packet_callback)


