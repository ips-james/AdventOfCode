import re
input_text = open('day4_input.txt', 'r').read().split("\n\n")

keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
eye_cols = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def passport_checker(input_text):
    answer1 = answer2 = 0
    for passport in input_text:
        chunks = re.split('[\n ]', passport)
        d = dict(chunk.split(":") for chunk in chunks)

        if all(key in d for key in keys):
            answer1 += 1

            rules = [1920 <= int(d['byr']) <= 2002,
                     2010 <= int(d['iyr']) <= 2020,
                     2020 <= int(d['eyr']) <= 2030,
                     (d['hgt'].endswith('cm') and 150 <= int(d['hgt'][:-2]) <= 193) or (d['hgt'].endswith('in') and 59 <= int(d['hgt'][:-2]) <= 76),
                     bool(re.fullmatch(r'#[0-9a-f]{6}', d['hcl'])),
                     d['ecl'] in eye_cols,
                     bool(re.fullmatch(r'[0-9]{9}', d['pid']))]

            if all(rules):
                answer2 += 1

    return(answer1, answer2)


print(passport_checker(input_text))
