

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
    if place == 1: return get_units(digit)
    elif place == 2: return get_tens(digit)
    elif place == 3: return get_units(digit)+('' if int(digit)==0 else ' hundred')
    elif place == 4: return get_units(digit)+('' if int(digit)==0 else ' thousand')
    elif place == 5: return get_tens(digit)
    elif place == 6: return get_units(digit)+('' if int(digit)==0 else ' lakh')
    elif place == 7: return get_tens(digit)
    elif place == 8: return get_units(digit)+('' if int(digit)==0 else ' crore')
    elif place == 9: return get_tens(digit)
    else:
        raise Exception("Only 9 digits allowed. Further not yet implemented")

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

if __name__ == "__main__":
    number = input("Enter number: " ).strip()
    output = []

    digit_list = list(number)
    if len(digit_list) > 9:
        print("Only till 9 digits supported")
        exit()

    if len(digit_list) == 2 and number[-2] == '1':
        text = get_teens(int(number))
    else:
        for i, v in enumerate(reversed(digit_list)):
            output.append(get_text(i+1,v))

        output.reverse()
        text = ' '.join(output)
    print(text)
