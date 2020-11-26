

def get_units(n):
    units = {
        0: '', # Zero is not spelt in units
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
    }
    return units[int(n)]


def get_tens(n):
    tens = {
        0: '',
        2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninety',
    }
    return tens[int(n)]

def get_text(place, digit):
    # if place == 1: return get_units(digit)
    # elif place == 2: return get_tens(digit)
    if place%7 == 0: return get_units(digit)+('' if int(digit)==0 else ' hundred')
    elif place%7 == 1: return get_units(digit)+('' if int(digit)==0 else ' thousand')
    elif place%7 == 2: return get_tens(digit)
    elif place%7 == 3: return get_units(digit)+('' if int(digit)==0 else ' lakh')
    elif place%7 == 4: return get_tens(digit)
    elif place%7 == 5: return get_units(digit)+('' if int(digit)==0 else ' crore')
    elif place%7 == 6: return get_tens(digit)

def get_teens(n):
    ten_nineteen = {
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
    }
    return ten_nineteen[n]

def one_two_digits(number):
    if number[-2] == '1':
        return get_teens(int(number))
    return get_tens(number[-2]) + ' ' + get_units(number[-1])

def morethan2digits(number):
    for i, v in enumerate(reversed(str(number))):
        output.append(get_text(i,v))

    output.reverse()
    return ' '.join(output)

if __name__ == "__main__":
    number = input("Enter number: " ).strip()
    output = []

    digit_list = list(number)
    # if len(digit_list) > 9:
    #     print("Only till 9 digits supported")
    #     exit()

    text = ('' if len(digit_list) <=2 else morethan2digits(number[:-2])) + ' ' +  one_two_digits(number)

    print(text)
