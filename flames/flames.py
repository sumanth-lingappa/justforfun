def strike_common_chars(partner1, partner2):
    partner1_char_count = {}
    for c in partner1:
        partner1_char_count[c] = partner1_char_count.setdefault(c, 0) + 1

    partner2_char_count = {}
    for c in partner2:
        partner2_char_count[c] = partner2_char_count.setdefault(c, 0) + 1

    for c in partner1_char_count.keys():
        if c in partner2:
            partner1_char_count[c] -= 1
            partner2_char_count[c] -= 1

    return sum(partner1_char_count.values()) + sum(partner2_char_count.values())


def find_relation(char_count):
    flames = ["FRIENDS", "LOVE", "ATTRACTION", "MARRIAGE", "ENEMY", "SISTER"]
    while len(flames) > 1:
        index = char_count % len(flames) - 1  # since index starts from zero
        if index == -1:
            index = len(flames) - 1
        # start counting from where the last character is elimenated.
        # remaining flames chars
        flames = flames[index+1:] + flames[0:index]
    return flames[0]


def output_relationship(partner1, partner2, relationship):
    print()
    print(f"{partner1} and {partner2} have {relationship} relationship!")
    print()

def take_input():
    partner1 = input("Enter Partner1 name: ")
    partner2 = input("Enter Partner2 name: ")
    return partner1, partner2

if __name__ == "__main__":
    partner1, partner2 = take_input()
    remaining_char_count = strike_common_chars(partner1, partner2)
    relationship = find_relation(remaining_char_count)
    output_relationship(partner1, partner2, relationship)