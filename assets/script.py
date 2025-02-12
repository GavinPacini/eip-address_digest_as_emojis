import scrypt
import json
import sys

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

if __name__ == "__main__":
    with open('./emoji-list.json') as emoji_list:
      data = json.load(emoji_list)
      emojis = list(data)

      address = bytes(bytearray.fromhex(sys.argv[1]))

      addr_hash = scrypt.hash(address, bytes(bytearray()), N=1048576, r=8)

      emoji_str = ""
      for i in chunks(addr_hash, 16):
          hash_chunk = int.from_bytes(i, "big")
          idx = hash_chunk % len(emojis)
          emoji_str += emojis[idx] + " "
      print(emoji_str)