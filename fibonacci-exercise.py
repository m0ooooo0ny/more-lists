"""A fibonacci sequence is a series of numbers in which each number is the sum of the two preceding numbers.
Starting with 0 and 1, the first ten terms are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

Your task here is to write code that will fill in the list called 'fib' so that it contains
the first 50 terms of the fibonacci sequence, starting with 0"""


# Don't try writing the code all at once. Break it down into pieces
# I have some tips below that will help you figure this out. You can delete them (and the code that goes with them) when you no longer need them


fib = [0, 1]

# TIP: How can you refer to the last item in a list? Print the last item in the list called fib
print(fib[-1])

# TIP: How about the second to last item?
print(fib[-2])

# TIP: How could you use the two items you've already accessed to generate the next term? Print the next term of the fibonacci sequence
print(fib[-1] + fib[-2])

# TIP: Now that you've figured out how to generate the next item in your sequence, how would you add it to the end of your list
fib.append(fib[-1] + fib[-2])
print(fib[:])

# TIP: You've gotten the next item in the sequence and added it to your list - now how do you repeat it?
# There are two good options based on your current knowledge - you could repeat a certain number of times (what type of loop is that?)
# or you could repeat as long as there are too few items in the list (what type of loop is that?)
# You might want to refresh your memory by creating a simple loop of the type you want first
for x in range(47):
    fib.append(fib[-1] + fib[-2])





# DON'T EDIT BELOW THIS LINE #
# I have code here that will help you know if your answer works
# Don't just copy and paste the list - that is NOT a valid answer
# Don't change the name of the list above or the error checking will not work correctly

fibonacci_results = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887
, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049]

def test_length(student_results):
    """Determine if student results contain the right number of terms"""
    if len(student_results) == len(fibonacci_results):
        print("First test successful - you have the right number of terms")
        return True
    else:
        print("First test failed. ", end='')
        if len(student_results) > len(fibonacci_results):
            print("You have too many terms in your sequence")
        else:
            print("You have too few terms in your sequence")
        return False


def test_contents(student_results):
    """Check each term to see if students have the correct answer"""
    is_correct = True
    num_terms_to_check = min(len(fib), len(fibonacci_results))
    for n in range(num_terms_to_check):
        if fib[n] == fibonacci_results[n]:
            print(f"Term at index{n} is correct: {fib[n]}")
        else:
            print(f"Term at index{n} is incorrect. You have {fib[n]} and I have {fibonacci_results[n]}")
            is_correct = False


test_length(fib)
test_contents(fib)
