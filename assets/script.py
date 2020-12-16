import scrypt
from emoji import unicode_codes
import sys

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

if __name__ == "__main__":
    single_char_emojis = list(filter(lambda i: len(i) == 1, unicode_codes.EMOJI_UNICODE.values()))

    address = bytes(bytearray.fromhex(sys.argv[1]))

    addr_hash = scrypt.hash(address, address)

    emoji_str = ""
    for i in chunks(addr_hash, 16):
        hash_chunk = int.from_bytes(i, "big")
        idx = hash_chunk % len(single_char_emojis)
        emoji_str += single_char_emojis[idx] + " "
    print(emoji_str)