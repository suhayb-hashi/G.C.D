# control variable
play_again = 'y'
while play_again == 'y':
    # get user input
    input_1 = int(input("Enter the smaller number: "))
    input_2 = int(input("Enter the larger number: "))
    # check if input_1 number is greater than 0
    if input_1 < 1:
        while input_1 < 1:
            print("First number must be greater than 0!")
            input_1 = int(input("Enter the smaller number: "))
            input_2 = int(input("Enter the larger number: "))
    # chech if first number is smaller than input_2
    if input_1 > input_2:
        while input_1 > input_2:
            print("First number must be smaller than second number!")
            input_1 = int(input("Enter the smaller number: "))
            input_2 = int(input("Enter the larger number: "))
#   get what the user inuted first
    firts_input = input_1
    second_input = input_2
    # calculate the GCD
    while input_1 > 0:
        remainder = input_2 % input_1
        input_2 = input_1
        input_1 = remainder
    # display output
    print("The greatest common divisor of", firts_input,
          "and", second_input, "is", input_2)
    # ask if they wanna continue
    play_again = input(
        "Do you want to enter in two additional numbers? (y/n): ")
