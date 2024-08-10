
helloIntent = ["hey","hi","wassup","hie","hello"]
byeIntent = ["ttyl","see you later","cu","tata","bye"]
chat = True
while chat==True:
    msg = input("enter msg:").lower()
    if msg in helloIntent:
        print("hey")
    elif msg in byeIntent:
        print("bye...")
        chat=False
    else:
        print("sorry i didn't understand")