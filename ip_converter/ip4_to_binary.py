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
    ip_addresses = ['108.78.154.65','149.77.68.12','110.218.245.87','31.43.145.147','215.189.199.121','246.179.48.184','15.217.34.130','144.222.111.162','151.79.14.47','26.152.20.52']
    for i in ip_addresses:
        print(convert_ip4_to_binary(i))
