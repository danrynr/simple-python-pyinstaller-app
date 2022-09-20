
"""import add2vals from sources"""
from sources import add2vals
import sys

sys.path.insert(0, 'sources')

def get_numbers():
    num1 = 5
    num2 = 21
    return num1, num2

def main():
    num1, num2 = get_numbers()
    add2vals.main(num1, num2)

if __name__ == '__main__':
    main()
