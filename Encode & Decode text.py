'''
task :
Create a code generator. Create 2 functions , the first one takes text as input,
replaces each letter with another letter, and outputs the “encoded” message. , the
second one decode the message to the original text
'''

def encode(text):
    text = list(text)
    text_to_num = [ord(x) for x in text]
    t = [x*2 for x in text_to_num]
    text_encode = [chr(x) for x in t]
    return "".join(text_encode)


def Decode(text):
    text = list(text)
    text_to_num = [ord(x) for x in text]
    t = [x//2 for x in text_to_num]
    text_dencode = [chr(x) for x in t]
    return "".join(text_dencode)
    

text_proccess = input("Enter the text that you want Encode it :")

encode_text = encode(text_proccess)
print(f"Encoder text is :{encode_text}")
decode_text = Decode(encode_text)
print(f"Dncoder text is :{decode_text}")
