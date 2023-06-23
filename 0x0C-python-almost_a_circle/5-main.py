#!/usr/bin/python3
""" 5-main """
# from models.rectangle import Rectangle

# if __name__ == "__main__":

#     r1 = Rectangle(4, 6, 2, 1, 12)
#     print(r1)

#     r2 = Rectangle(5, 5, 1)
#     print(r2)

""" 6-main """
# from models.rectangle import Rectangle

# if __name__ == "__main__":

#     r1 = Rectangle(2, 3, 2, 2)
#     r1.display()

#     print("---")

#     r2 = Rectangle(3, 2, 1, 0)
#     r2.display()

""" Doc """
# from models.rectangle import Rectangle

# if __name__ == "__main__":

#     r1 = Rectangle(10, 10, 10, 10)
#     print(r1)

#     r1.update(89)
#     print(r1)

#     r1.update(89, 2)
#     print(r1)

#     r1.update(89, 2, 3)
#     print(r1)

#     r1.update(89, 2, 3, 4)
#     print(r1)

#     r1.update(89, 2, 3, 4, 5)
#     print(r1)

""" 8-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(height=1)
    print(r1)

    r1.update(width=1, x=2)
    print(r1)

    r1.update(y=1, width=2, x=3, id=89)
    print(r1)

    r1.update(x=1, height=2, y=3, width=4)
    print(r1)
    