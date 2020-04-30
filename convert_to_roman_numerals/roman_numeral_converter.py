def convert_to_roman(n):

    roman = ''

    while n > 0:
        while n % 5 != 0:
            roman += 'I'
            n -= 1
        while n % 10 != 0:
            roman += 'V'
            n -= 5
        while n % 50 != 0:
            roman += 'X'
            n -= 10
        while n % 100 != 0:
            roman += 'L'
            n -= 50
        while n % 500 != 0:
            roman += 'C'
            n -= 100
        while n % 1000 != 0:
            roman += 'D'
            n -= 500
        while n % 5000 != 0:
            roman += 'M'
            n -= 1000

    roman = roman[::-1]
    roman = roman.replace('DCCCC', 'CM')
    roman = roman.replace('CCCC', 'CD')
    roman = roman.replace('LXXXX', 'XC')
    roman = roman.replace('XXXX', 'XL')
    roman = roman.replace('VIIII', 'IX')
    roman = roman.replace('IIII', 'IV')

    return roman

n = int(input("Enter a number to turn into Roman Numerals: "))

print(str(n) + " in Roman Numerals is " + str(convert_to_roman(n)))