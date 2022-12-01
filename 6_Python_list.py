import numpy as np
def func (numberFrom, numberTo, numbersCount):
    if numberFrom > numberTo:
        print("NumberFrom cannot be higher than numberTo.")
    else:
        lst = np.random.randint(numberFrom, numberTo, numbersCount)
        print(lst)
        print("Amount:", len(lst))
func (0,9,10)
