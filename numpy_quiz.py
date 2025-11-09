# Numpy Quiz - 10 Questions

import numpy as np

# Q1: What will be the output of the following code?
a = np.array([1, 2, 3])
print(a + 2)

# Q2: How do you create a 3x3 array filled with True values?
# A) np.ones((3,3))
# B) np.full((3,3), True)
# C) np.array((3,3), True)

# Q3: Which function is used to find the mean of an array?
# Example: np.mean(arr)

# Q4: What will be the shape of np.zeros((2,3,4))?

# Q5: How can you generate a NumPy array with numbers from 0 to 9?
# Example: np.arange(? , ?)

# Q6: What is the difference between np.array() and np.asarray()?

# Q7: Given arr = np.array([1,2,3,4,5]), what will arr[1:4] return?

# Q8: How do you get the transpose of a 2D NumPy array?
# Example: arr.T

# Q9: What function would you use to compute the standard deviation of an array?
# Example: np.std(arr)

# Q10: How do you reshape a 1D array of size 9 into a 3x3 array?
# Example: arr.reshape(3,3)

# BONUS TASK:
# Implement a simple grading function that checks user's answers (for multiple choice questions):

answers = {
    'Q2': 'B',
}

def check_answer(question, user_answer):
    correct = answers.get(question)
    if correct is None:
        return f"Question {question} is open-ended."
    elif user_answer.strip().upper() == correct:
        return f"Correct! {question} = {correct}"
    else:
        return f"Incorrect. {question} = {correct}, you answered {user_answer}"

# Example usage:
# print(check_answer('Q2', 'b'))
