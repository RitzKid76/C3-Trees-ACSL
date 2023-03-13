def maxv(output, i):
    left = -1
    right = output[i][1]

    if(i > 0):
        left = output[i - 1][1]
    return max(left, right)

def string_pairs(input):
    input = [c for c in input]
    output = [(input.pop(0), 0)]
    while len(input) > 0:
        c = input.pop(0)

        #stupid fix cause python enumerate is a while loop
        didntinsert = False

        for i, (char, value) in enumerate(output):
            if(c > char):
                max = maxv(output, i) + 1
                output.insert(i, (c, max))
                break

            if(i == len(output) - 1):
                didntinsert = True

        #continued fix pain
        if(didntinsert):
            max = output[len(output) - 1][1] + 1
            output.append((c, max))

    output.reverse()
    return output

def string_one_builder(string, index, output):
    value = string[index][1]
    output.append(string[index][0])

    #left check
    for i in reversed(range(index)):
        check_value = string[i][1]
        if(check_value <= value):
            break
        if(check_value == value + 1):
            string_one_builder(string, i, output)

    #right check
    if(index < len(string) - 1):
        for i in range(index + 1, len(string)):
            check_value = string[i][1]
            if(check_value <= value):
                break
            if(check_value == value + 1):
                string_one_builder(string, i, output)

def string_two_builder(string, index, output):
    value = string[index][1]

    #left check
    for i in reversed(range(index)):
        check_value = string[i][1]
        if(check_value <= value):
            break
        if(check_value == value + 1):
            string_two_builder(string, i, output)

    #right check
    if(index < len(string) - 1):
        for i in range(index + 1, len(string)):
            check_value = string[i][1]
            if(check_value <= value):
                break
            if(check_value == value + 1):
                string_two_builder(string, i, output)
    output.append(string[index][0])

def c3trees(string):
    pairs = string_pairs(string)
    start_index = -1
    for i, p in enumerate(pairs):
        if p[1] == 0:
            start_index = i
            break

    #one
    string_one_array = []

    string_one_builder(pairs, start_index, string_one_array)

    string_one = ""
    for c in string_one_array:
        string_one += c

    #two
    string_two_array = []

    string_two_builder(pairs, start_index, string_two_array)

    string_two = ""
    for c in string_two_array:
        string_two += c

    return string_one + ' ' + string_two
    

string = 'CORONAVIRUS'
print(c3trees(string))
