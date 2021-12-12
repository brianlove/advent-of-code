#filename = 'demo-08b.txt'
filename = 'input-08.txt'

segments_to_digits = {
  'a': [0, 2, 3, 5, 6, 7, 8, 9],
  'b': [0, 4, 5, 6, 8, 9],
  'c': [0, 1, 2, 34, 7, 8, 9],
  'd': [2, 3, 4, 5, 6, 8, 9],
  'e': [0, 2, 6, 8],
  'f': [0, 1, 3, 4, 5, 6, 7, 8, 9],
  'g': [0, 2, 3, 5, 6, 8, 9]
}
digits_to_segments = {
  '0': 'abcefg',
  '1': 'cf',
  '2': 'acdeg',
  '3': 'acdfg'
}

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

# Part 1
count = 0

for line in lines:
    inputs, outputs = line.split(' | ')
    inputs = inputs.split()
    outputs = outputs.split()

    #print(inputs)
    #print(outputs)

    # Count the 1, 4, 7, and 8 in the output
    # They are 2, 4, 3, and 7 segments long, respectively
    for output in outputs:
        length = len(output)
        if length in [2, 3, 4, 7]:
            count += 1

print (f"There are {count} instances of unique numbers")

# Part 2
print()
print("Part 2")

total = 0

for line in lines:
    inputs, outputs = line.split(' | ')
    inputs = [set(x) for x in inputs.split()]
    outputs = [set(x) for x in outputs.split()]

    print(inputs)
    print(outputs)
    #print()

    digits = {}
    mapping = {}
    decode = {}
    occurrences = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}
    
    map_1 = None
    map_7 = None
    map_4 = None
    map_8 = None

    for entry in inputs:
        if len(entry) == 2:
            digits[1] = entry
        elif len(entry) == 3:
            digits[7] = entry
        elif len(entry) == 4:
            digits[4] = entry
        elif len(entry) == 7:
            digits[8] = entry
        
        for ch in entry:
            occurrences[ch] += 1
            
    mapping['a'] = list(digits[7] - digits[1])[0]
    decode[mapping['a']] = 'a'
    
    for in_char in occurrences:
        print("> ", in_char, occurrences[in_char])
        if occurrences[in_char] == 4:
            mapping['e'] = in_char
            decode[in_char] = 'e'
        elif occurrences[in_char] == 6:
            mapping['b'] = in_char
            decode[in_char] = 'b'
        elif occurrences[in_char] == 9:
            mapping['f'] = in_char
            (c_char,) = digits[1] - set(in_char)
            mapping['c'] = c_char
            decode[in_char] = 'b'
    
    #At this point, we have mapped inputs to
    # a, b, c, e, and f.  This seems to be
    # sufficient to identify the remaining digits

    abcef = set([mapping['a'], mapping['b'], mapping['c'], mapping['e'], mapping['f']])

    for char in inputs:
        if len(char) == 5:
            if char & abcef == set([mapping['a'], mapping['c'], mapping['e']]):
                digits[2] = char
            elif char & abcef == set([mapping['a'], mapping['c'], mapping['f']]):
                digits[3] = char
            elif char & abcef == set([mapping['a'], mapping['b'], mapping['f']]):
                digits[5] = char
        elif len(char) == 6:
            if char & abcef == abcef:
                digits[0] = char
            elif char & abcef == set([mapping['a'], mapping['b'], mapping['e'], mapping['f']]):
                digits[6] = char
            elif char & abcef == set([mapping['a'], mapping['b'], mapping['c'], mapping['f']]):
                digits[9] = char

    print("digits:", digits)
    print("mapping:", mapping)
    print("decode:", decode)
    print("occurrences:", occurrences)
    print()
    
    num = []
    for output in outputs:
        print("  output:", output)
        for digit in digits:
            if output == digits[digit]:
                print("    digit", digit, digits[digit])
                num.append(digit)
                break
    print(num)
    val = int(''.join([str(x) for x in num]))
    print(f"  val: {val}")
    total += val
    
    
    print()
    print()

print(f"Part 2 total: {total}")
