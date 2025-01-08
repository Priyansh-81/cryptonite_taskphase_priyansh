import base64
str1="72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
middleman=bytes.fromhex(str1)
encodedmessage=base64.b64encode(middleman).decode('utf-8')
print(encodedmessage)
