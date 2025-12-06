import base64

s = "FIRESIDEdotDENSITYGAMESdotONLINE"
decoded_bytes = base64.b64decode(s)

# Show the bytes in hex (useful for embedding in a save file)
print(decoded_bytes.hex())
