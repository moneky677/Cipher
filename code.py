while True:
    message = input("Please enter your message\n>>>\n").strip()
    letters = str.maketrans(
    "abcdefghijklmnopqrstuvwxyz",
    "qwertyuiopasdfghjklzxcvbnm"
    )
    capletter = str.maketrans(
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'FGHQWERTYUIOPASDJKLZXCVBNM'
    )
    numbers = str.maketrans(
    '1234567890',
    '6789012345'    
    )
    symbols = str.maketrans(
    '`~!@#$%^&*()-_=+[{]}\|;:,<.>/?',
    '^&*()-_=+[{]}|\:;,<>.?/~`!@#$%'
    )
    message = message.translate(letters).translate(capletter).translate(numbers).translate(symbols)
    print(message)
