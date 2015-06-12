import json

zero_block = [0x00]*16
keya = [0xFF]*6
keyb = [0xFF]*6
acc  = [0xFF, 0x07, 0x80, 0x69] # access controls
key_block  = keya + acc + keyb
zero_sector = zero_block*3 + key_block 
tag_block = [0xCD, 0x76, 0x92, 0x74, 
             0x5D, 0x88, 0x04, 0x00,
             0x85, 0x00, 0x00, 0x00,
             0x04, 0x13, 0x45, 0x01] 
tag_sector = tag_block + zero_block*2 + key_block
mem = tag_sector + 15*zero_sector

ar = [{'entry': 'tag', 
       'rands': [[0x0E, 0x61, 0x64, 0xD6], 
                 [0x8F, 0x82, 0x69, 0x9E],
                 [0xDC, 0xFC, 0x96, 0x2B], 
                 [0x7A, 0x03, 0xD0, 0x83], 
                 [0x21, 0x78, 0xEC, 0x8A], 
                 [0x1A, 0x73, 0x27, 0x7A], 
                 [0xC3, 0x29, 0xC5, 0xEF], 
                 [0xD6, 0x65, 0x37, 0xEB], 
                 [0x49, 0x9B, 0x28, 0xEA],
                 [0x24, 0x45, 0xE0, 0x5E],
                 [0x9D, 0x84, 0x0D, 0x39],
                 [0xF7, 0xA7, 0xCB, 0x67],
                 [0x46, 0xBD, 0x55, 0xC8],
                 [0x08, 0x59, 0xA3, 0xFE],
                 [0x40, 0xE8, 0x1A, 0xD8],
                 [0x68, 0x93, 0x44, 0x01]
                ],
        'type': 'CLASSIC1K',
        'mem':  mem
      },
      {'entry': 'reader',
       'rands': [[0x15, 0x45, 0x90, 0xA8], 
                 [0x01, 0x3A, 0x6B, 0xBA],
                 [0xEE, 0x08, 0xB0, 0x0A], 
                 [0x2F, 0x44, 0xA3, 0x06], 
                 [0xC7, 0xC9, 0xD8, 0x8B], 
                 [0xCE, 0x0C, 0xD2, 0x7C], 
                 [0x9B, 0xF6, 0xC8, 0x66], 
                 [0x73, 0xB3, 0xBB, 0x75], 
                 [0x96, 0x66, 0x8E, 0x10],
                 [0x72, 0x10, 0xA5, 0xFB],
                 [0x52, 0x3A, 0xA8, 0x5B],
                 [0xE0, 0x8E, 0x57, 0xCB],
                 [0x78, 0x81, 0xCB, 0x50],
                 [0x4D, 0x95, 0xCA, 0x3A],
                 [0xAE, 0x8D, 0x9C, 0x9C],
                 [0xD6, 0x8D, 0x04, 0x06]
                ]
      }]

f = open('classic1k.json', 'w')
json.dump(ar, f)
f.close()


ar = [{'entry': 'tag',
        'type': 'ULTRALIGHT',
        'mem':  [0x04, 0xBE, 0x6F, 0x5D,
                 0x22, 0x09, 0x29, 0x80,
                 0x82, 0x48, 0x00, 0x00,
                 0xE1, 0x10, 0x12, 0x00,
                 0x01, 0x03, 0xA0, 0x10,
                 0x44, 0x03, 0x00, 0xFE,
                 0x00, 0x00, 0x00, 0x00,
                 0x00, 0x00, 0x00, 0x00, 
                 0x00, 0x00, 0x00, 0x00,
                 0x00, 0x00, 0x00, 0x00,
                 0x00, 0x00, 0x00, 0x00,
                 0x00, 0x00, 0x00, 0x00, 
                 0x00, 0x00, 0x00, 0x00,
                 0x00, 0x00, 0x00, 0x00,
                 0x00, 0x00, 0x00, 0x00,
                 0x00, 0x00, 0x00, 0x00
                ]
      }]

f = open('ultralight.json', 'w')
json.dump(ar, f)
f.close()
