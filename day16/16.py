

filename = 'data.txt'

with open(filename) as f:
    line = f.readlines()[0]

# line = 'D2FE28'
# line = '38006F45291200'
# line = '8A004A801A8002F478'
# line = 'C0015000016115A2E0802F182340'
# line = 'A0016C880162017C3686B18A3D4780'

hex2bin = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111',
}

data = ''.join(hex2bin[char] for char in line)

VERSIONS = []

def grab_next_value(data, n):
    try:
        raw = ''.join((next(data) for i in range(n)))
    except RuntimeError:
        raise ValueError('End of data')

    intval = int(raw, 2)
    return intval


def parse_type_4(data):
    litval = ''

    while True:
        leading_bit = grab_next_value(data, 1)
        raw = ''.join((next(data) for i in range(4)))

        litval += raw

        if leading_bit == 0:
            break

    value = int(litval, 2)

    return value


def parse_type_other(data):
    leading_bit = grab_next_value(data, 1)

    # length
    if leading_bit == 0:
        subpacket_len = grab_next_value(data, 15)
        
        packets = []
        raw = ''.join((next(data) for i in range(subpacket_len)))
        raw = iter(raw)

        packets = []
        while packet := parse_data(raw):
            packets.append(packet)
    
    # number
    else:
        subpacket_no = grab_next_value(data, 11)

        packets = []
        for i in range(subpacket_no):
            packets.append(parse_data(data))

    return packets


def parse_data(data):
    try:
        version = grab_next_value(data, 3)
        type_id = grab_next_value(data, 3)
    except ValueError:
        return None

    metadata = {"version": version, "type_id": type_id}

    VERSIONS.append(version)

    if type_id == 4:
        value = parse_type_4(data)
        return {**metadata, "value": value}

    elif type_id != 4:
        packets = parse_type_other(data)

    return {**metadata, "packets": packets}


data = iter(data)
result = parse_data(data)

# part 1
print(f'part 1: {sum(VERSIONS)=}')


from math import prod

def gt(lst):
    return lst[0] > lst[1]

def lt(lst):
    return lst[0] < lst[1]

def eq(lst):
    return lst[0] == lst[1]


operators = {
    0: sum,
    1: prod,
    2: min,
    3: max,
    5: gt,
    6: lt,
    7: eq, 
}

def compute(packet):
    type_id = packet['type_id']

    if type_id == 4:
        return packet['value']

    subpackets = packet['packets']
    operator = operators[type_id]

    value = operator([compute(subpacket) for subpacket in subpackets]) 

    return value

# part 2
print(f'part 2: {compute(result)=}')
