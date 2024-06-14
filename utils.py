def bcd_to_decimal(value):
    high_nibble, low_nibble = ((value >> 16) & 0xF, (value >> 8) & 0xF), ((value >> 4) & 0xF, value & 0xF)     
    return float(f'''{high_nibble[0]}{high_nibble[1]}.{low_nibble[0]}{low_nibble[1]}''')

def decimal_to_bcd(value):
    value_as_string = f'{value:.2f}'

    # BCD used in USB specification is defined on 2 bytes only and we have to
    # remove the dot from the created string. 
    if len(value_as_string) > 5:
        raise ValueError("Value must follow 0.00 <= value <= 99.99")

    high_nibble, low_nibble = [divmod(int(number), 10) for number in value_as_string.split('.')]
    return high_nibble[0] << 12 | high_nibble[1] << 8 | low_nibble[0] << 4 | low_nibble[1]