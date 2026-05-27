print("Welcome to the Cake Cipher!!!")
choice = input("Would you like to cipher or decipher?\nd/c\n").lower().strip()
while choice not in ['d','c']:
    print("Not an option, please try again")
    choice = input("Would you like to cipher or decipher?\nd/c\n").lower().strip()
message = input("Please enter your message\n>>>\n").strip()
if choice == 'c':
   table = str.maketrans(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()-_=+[{]}\\|;:,<.>/?",
        "mzqvnturswbxcpfyaokhdgijleEKCVDLBSNHFGMPOAWUQZRJTXIY3071986254;|/+.`[{<\\}]~>?-=^)@(#*:!$%,_&"
    )
else:
    table = str.maketrans(
        "mzqvnturswbxcpfyaokhdgijleEKCVDLBSNHFGMPOAWUQZRJTXIY3071986254;|/+.`[{<\\}]~>?-=^)@(#*:!$%,_&",
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()-_=+[{]}\\|;:,<.>/?"
    )
print(message.translate(table))
