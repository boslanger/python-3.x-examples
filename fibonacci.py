"""
fibonacci's sequence to x number of places.
updated 9 NOV 2018
added try/except/else block and more comments
"""


def fibonacci():
    """Outputs a requested length of Fibonacci's sequence starting from 1"""
    answer = input("How many digits of Fibonacci's sequence do you want?")
    try:
        # Verifies the user supplied an integer
        answer = int(answer)
    except ValueError:
        # Feedback to user
        print("You must give an integer.")
    else:
        sequence = []
        for x in range(int(answer)):
            if len(sequence) <= 1:
                sequence.append(1)
            else:
                sequence.append(sequence[-1]+sequence[-2])

        # Information output block.
        print("\nThis is the full sequence requested:")
        print(sequence)
        print("\nThis is the total number of digits requested:")
        print(len(sequence))
        print("This is the last digit requested:")
        print(sequence[-1])
        print("The sum of the sequence is:")
        print(sum(sequence))


fibonacci()

