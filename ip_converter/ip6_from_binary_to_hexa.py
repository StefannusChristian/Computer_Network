def make_groups(hexa_list: list):
    groups = []
    curr = 0
    curr_bin = ''
    for i in hexa_list:
        curr_bin += i
        curr += 1
        if curr == 4:
            groups.append(curr_bin)
            curr_bin = ''
            curr = 0
    return groups


def split_four(binary_address: str):
    binary_address = binary_address.replace(':', '')
    result = []
    curr = 0
    curr_bin = ''
    for i in binary_address:
        curr_bin += i
        curr += 1
        if curr == 4:
            result.append(curr_bin)
            curr_bin = ''
            curr = 0
    result_test = ''.join(result)
    assert result_test == binary_address
    return result


def find_index(binary_len_four):
    one_index = []
    for i in range(len(binary_len_four)):
        if binary_len_four[i] == '1':
            one_index.append(i)
    return one_index


def find_sum(binary_len_four):
    the_sums = []
    for i in binary_len_four:
        the_index = find_index(i)
        curr_sum = 0
        for index in the_index:
            if index == 0:
                curr_sum += 8
            elif index == 1:
                curr_sum += 4
            elif index == 2:
                curr_sum += 2
            elif index == 3:
                curr_sum += 1
        the_sums.append(curr_sum)
    return the_sums


def make_hexa_dict():
    hexas = {i: str(i) for i in range(10)}
    letters = ['A', 'B', 'C', 'D', 'E', 'F']
    left_numbers = [i for i in range(10, 16)]
    for num, letter in zip(left_numbers, letters):
        hexas[num] = letter
    return hexas


def add_double_dots(groups):
    groups = ''.join(groups)
    count = 0
    result = ''
    for i in groups:
        result += i
        count += 1
        if count == 4:
            result += ':'
            count = 0
    result = result[:len(result)-1]
    return result


def convert_to_hexadecimal(binary_address: str):
    hexa_dict = make_hexa_dict()
    # type(fours) = list
    fours = split_four(binary_address)
    the_sums = find_sum(fours)
    hexa_result = []
    for sums in the_sums:
        the_hexa = hexa_dict[sums]
        hexa_result.append(the_hexa)
    groups = make_groups(hexa_result)
    result = add_double_dots(groups)
    return result
