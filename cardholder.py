import math
import string
import random


class Cardholder:
    def __init__(self, cardNum, pin, balance, firstName, lastName) -> None:
        self.cardNum = cardNum
        self.pin = pin
        self.balance = balance
        self.firstName = firstName
        self.lastName = lastName


def random_num_generator(max_length: int) -> int:
    """ Random number generator based on specified max length

    Args:
        max_length (int): Maximum number length

    Returns:
        int: Random generated number based on specified max length
    """
    temp_num = string.digits
    
    if len(temp_num) < max_length:
        multiplier = math.ceil(max_length/len(temp_num))
        temp_num = "".join([temp_num]*multiplier)
    
    final_num = int("".join(random.sample(temp_num, max_length)))
        
    return final_num


if __name__ == "__main__":
    
    ch = Cardholder(random_num_generator(16), random_num_generator(6), 123456.78, "Clement", "Lee")
    print(ch.cardNum)
    print(ch.pin)
    print(ch.balance)
    print(ch.firstName)
    print(ch.lastName)
    

