def perfectSquare(number):
    
    
    perfect_square = int(number**0.5)
    
    if perfect_square * perfect_square == number:
        return True
    return False

number=int(input("enter number: "))
print(perfectSquare(number))