import base64

def decode_base64(encoded_text):
    try:
        # Decode Base64 encoded text
        decoded_bytes = base64.b64decode(encoded_text)
        # Convert bytes to string using UTF-8 encoding
        decoded_text = decoded_bytes.decode('utf-8')
        return decoded_text
    except Exception as e:
        return f"Error decoding: {e}"

if __name__ == "__main__":
    print("Base64 Decoder")
    print("-----------------")
    while True:
        encoded_text = input("Enter Base64 encoded text (or 'q' to quit): ")
        
        if encoded_text.lower() == 'q':
            print("Exiting...")
            break
        
        decoded_text = decode_base64(encoded_text)
        print(f"Decoded text: {decoded_text}\n")

