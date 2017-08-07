import base64

def shuffle(code):
  return "".join(i+j  for i,j in zip(code[::2],code[1::2][::-1]+"=")).strip("=")

def encode(string,key):
    l=len(key)
    ens = "".join(chr(ord(s) + ord(key[i % l])+l-i) for i,s in enumerate(string))
    code = base64.urlsafe_b64encode(ens.encode()).decode().strip("=")
    return shuffle(code)

def decode(decode_string,key):
    string = shuffle(decode_string)
    padding = 4-(len(string)%4)
    if padding!=4:string += "="*padding
    l=len(key)
    return "".join(chr(ord(s) + i - (ord(key[i % l]) + l))
                   for i,s in enumerate(base64.urlsafe_b64decode(string).decode()))


