#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='The input file')
parser.add_argument('-D', '--debug', action='store_true')

args = parser.parse_args()

PART_1 = True

with open(args.filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

data = lines[0]
# data = "8A004A801A8002F478"
# data = "620080001611562C8802118E34"
# data = "C0015000016115A2E0802F182340"
# data = "A0016C880162017C3686B18A3D4780"


bit_bytes = [str(bin(int(x, 16)))[2:].zfill(4) for x in data]
bit_str = ''.join(bit_bytes)

if args.debug:
    print(bit_str)
    print()


LENGTH_TYPE_ID_INDEX = 6
LITERAL_VALUE_START_INDEX = 6
SUBPACKET_LENGTH_INDEX = 7
TYPE_0_CONTENTS_INDEX = 22
TYPE_1_CONTENTS_INDEX = 18

def parse_packet(bits):
    packet = {}
    packet['version'] = int(bits[0:3], 2)
    packet['type'] = int(bits[3:6], 2)
    if args.debug:
        print(f"PARSE({bits})")
        print(f"--- version: {packet['version']}, type: {packet['type']}")

    num_packets = 1
    version_number_sum = packet['version']

    if packet['type'] == 4:
        # Literal value
        vals = bits[6:]
        blocks = [vals[ix*5:ix*5+5] for ix in range(len(vals)//5)]
        nibbles = []
        for block in blocks:
            nibbles.append(block[1:])
            if block[0] == '0':
                break
        
        packet['value'] = int(''.join(nibbles), 2)
        max_length = LITERAL_VALUE_START_INDEX + 5*len(nibbles)
    else:
        # Operator
        length_type = bits[LENGTH_TYPE_ID_INDEX]

        if length_type == '0':
            # Defined number of bits
            subpacket_length = int(bits[SUBPACKET_LENGTH_INDEX:TYPE_0_CONTENTS_INDEX], 2)
            max_length = TYPE_0_CONTENTS_INDEX + subpacket_length
            subpacket_bits = bits[TYPE_0_CONTENTS_INDEX:max_length]
            packet['subpackets'], new_packets, new_version_sum = parse_packets(subpacket_bits)
            num_packets += new_packets
            version_number_sum += new_version_sum
        else:
            # Defined number of subpackets
            num_subpackets = int(bits[SUBPACKET_LENGTH_INDEX:TYPE_1_CONTENTS_INDEX], 2)

            start_index = TYPE_1_CONTENTS_INDEX
            packet['subpackets'] = []
            for i in range(num_subpackets):
                new_packet, new_count, length, new_version_sum = parse_packet(bits[start_index:])
                packet['subpackets'].append(new_packet)
                num_packets += new_count
                start_index += length
                version_number_sum += new_version_sum
            max_length = start_index

    if args.debug:
        print()
    return packet, num_packets, max_length, version_number_sum


def parse_packets(bits):
    if args.debug:
        print("parsing multiple packets...")
        print("> ", bits)
    start_index = 0
    packets = []
    num_packets = 0
    version_number_sum = 0
    while start_index < len(bits) and '1' in bits[start_index:]:
        packet, new_packets, packet_length, new_version_sum = parse_packet(bits[start_index:])
        num_packets += new_packets
        start_index += packet_length
        packets.append(packet)
        version_number_sum += new_version_sum
        if args.debug:
            print("> Parsed packet:", new_packets, packet)
            print()
    return packets, num_packets, version_number_sum



parsed, num_packets, version_number_sum = parse_packets(bit_str)

print()
print("Parsed:")
# print(parsed)
print(f"Parsed {num_packets} packets")
print("Version number sum:", version_number_sum)



