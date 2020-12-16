---
eip: <to be assigned>
title: Address Digest as Emojis
author: Joshua Richardson (@josh-richardson), Gavin Pacini (@GavinPacini)
status: Draft
type: Meta
created: 2020-12-16
---

## Simple Summary
Avoid address substitution attacks by verifying with four simple emojis. e.g. Mitigate attacks like [the recent one against CEO of Nexus Mutual](https://twitter.com/nexusmutual/status/1338441873560571906).

## Abstract
We propose a standard method for creating a digest of an Ethereum address as emojis, which are human-friendly. **TODO**.

## Motivation
Mitigate attacks like [the recent one against CEO of Nexus Mutual](https://twitter.com/nexusmutual/status/1338441873560571906). Based on [Telegram's implementation for encrypted voice calls](https://core.telegram.org/api/end-to-end/voice-calls#key-verification). Address substiution is a common attack vector. Yet, showing only the first four and last four characters of an address is still a de-facto standard. There are some exising methods of visualising addresses as images with higher entropy than four emojis, however on a "human-readability" scale, the authors believe emojis to be much more user friendly. This would be easily implementable on different software and hardware wallets. Also, it would be very easy to send out-of-band i.e. via another means the same four emojis in order to verify the address. E.g. over a phone call, one could simple say "0, Traffic Lights, Film Clapperboard, T-Shirt" for `0️⃣ 🚦 🎬 👕`.

## Specification
Using a specific subset of emojis (in `./assets/emoji-list.txt`)
**TODO**.
The technical specification should describe the syntax and semantics of any new feature. The specification should be detailed enough to allow competing, interoperable implementations for any of the current Ethereum platforms (go-ethereum, parity, cpp-ethereum, ethereumj, ethereumjs, and [others](https://github.com/ethereum/wiki/wiki/Clients)).

## Rationale
 **TODO**.
The rationale fleshes out the specification by describing what motivated the design and why particular design decisions were made. It should describe alternate designs that were considered and related work, e.g. how the feature is supported in other languages.

## Backwards Compatibility
This is a new method of verifying addresses in a human-friendly manner and would create any backwards compatibility issues.

## Reference Implementation
python3, requires `pip3 install scrypt`.
```python
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
```

Running:  
`python3 script.py 8Cd5fB2229fbB84E260dd03c392c9621CdDc4820`  
Outputs:  
`0️⃣ 🚦 🎬 👕`  

Which could look something like this in Metamask (mockup):  
![Metamask Mockup with Emoji Digest](./assets/metamask-mockup.jpg)

## Security Considerations
 **TODO**.
All EIPs must contain a section that discusses the security implications/considerations relevant to the proposed change. Include information that might be important for security discussions, surfaces risks and can be used throughout the life cycle of the proposal. E.g. include security-relevant design decisions, concerns, important discussions, implementation-specific guidance and pitfalls, an outline of threats and risks and how they are being addressed. EIP submissions missing the "Security Considerations" section will be rejected. An EIP cannot proceed to status "Final" without a Security Considerations discussion deemed sufficient by the reviewers.

## Copyright
Copyright and related rights waived via [CC0](https://creativecommons.org/publicdomain/zero/1.0/).