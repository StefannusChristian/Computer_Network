def find_groups(ip_address: str):
    groups = []
    curr = ''
    for i in range(len(ip_address)):
        if ip_address[i] != '.':
            curr += ip_address[i]
        else:
            groups.append(curr)
            curr = ''
    last = len(ip_address)-1
    add = ''
    while True:
        if ip_address[last] != '.':
            add += ip_address[last]
        else:
            add = add[::-1]
            groups.append(add)
            break
        last -= 1
    return groups


def convert_to_binary(chosen: list, bit_octet: list):
    binaries = ''
    for i in bit_octet:
        if i in chosen:
            binaries += '1'
        else:
            binaries += '0'
    return binaries


def find_sum(bit_octet, num):
    chosen = []
    for i in bit_octet:
        if i <= num and num >= 0:
            num -= i
            chosen.append(i)
    return chosen


def add_dots(binaries):
    result = ''
    for i in binaries:
        result += i+'.'
    return result


def convert_ip4_to_binary(ip_address: str):
    bit_octet = [2**i for i in range(7, -1, -1)]
    binaries = []
    groups = find_groups(ip_address)
    for num in groups:
        num = int(num)
        chosen = find_sum(bit_octet, num)
        curr_bin = convert_to_binary(chosen, bit_octet)
        expected_bin = bin(num)[2:]
        while len(expected_bin) < 8:
            expected_bin = '0'+expected_bin
        assert curr_bin == expected_bin
        binaries.append(curr_bin)
    binaries = add_dots(binaries)
    binaries = binaries[:len(binaries)-1]
    return binaries


if __name__ == '__main__':
    result = (convert_ip4_to_binary('66.94.29.13'))
    expected_result = '01000010.01011110.00011101.00001101'
    assert result == expected_result
    print(result)
