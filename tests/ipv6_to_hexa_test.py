from ip_converter.ip6_from_binary_to_hexa import convert_to_hexadecimal

def test_ip6_to_hexadecimal():
    binary_address = '00100110110110110100001100001101:0110001100001101:0100001000001101:0101001010001101:0100001000001001:0100001000001101:0100001010000101'
    expected = '26DB:430D:630D:420D:528D:4209:420D:4285'
    assert convert_to_hexadecimal(binary_address) == expected