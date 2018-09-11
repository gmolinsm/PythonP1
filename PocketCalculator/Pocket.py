print("\n***Pocket calculator***"
      "\nType your operation below or type 'finish' to exit")

while True:
    print("Your operation:")
    value = input()

    if value == "finish":
        print("Bye!")
        exit(1)
    else:
        command = eval(value)
        print("The result is ", command)
