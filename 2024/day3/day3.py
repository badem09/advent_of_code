import re

p = r"mul\((\d{1,3}),(\d{1,3})\)"
lines = open("input.txt").readlines()
res = [int(e[0]) * int(e[1]) for l in lines for e in re.findall(p, l)]



for l in lines:
    matches = re.finditer(p, l)

    valid_matches = []
    is_active = True  # Initial state: all mul() functions are valid

    for match in matches:
        print(is_active, " ", l[:match.start()])
        if "don't()" in l[:match.start()]:
            print('1 : ', match)
            is_active = False
            l.replace("don't()",'')
        elif "do()" in l[:match.start()]:
            print('2 : ', match, l[:match.start()])
            is_active = True
            l.replace("do()",'')

        if is_active:
            valid_matches.append((int(match.group(1)), int(match.group(2))))
print(valid_matches)