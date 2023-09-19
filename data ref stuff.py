# load in obj file

# input hex format (5 vertices)
# 0A 76 20 2D 32 2E 38 31 32 35 30 30 20 35 37 2E 32 35 37 38 30 31 20 33 2E 34 36 30 38 39 36 
# 0A 76 20 2D 32 2E 38 33 32 30 30 30 20 35 37 2E 31 34 34 35 30 31 20 33 2E 36 38 33 35 39 36 
# 0A 76 20 2D 32 2E 36 35 36 32 30 30 20 35 37 2E 31 39 31 33 39 39 20 33 2E 36 31 37 31 39 36 
# 0A 76 20 2D 33 2E 30 31 31 37 30 30 20 35 37 2E 32 37 37 33 30 32 20 33 2E 34 38 34 33 39 36 
# 0A 76 20 32 2E 38 31 32 35 30 30 20 35 37 2E 32 35 37 38 30 31 20 33 2E 34 36 30 38 39 36  

# v start = 0A 76 20, vt start = 0A 76 74 20
# 20 = divider between values 

# output example (first 12 bytes are vertices - 4 each for XYZ) first two = ones place signed, second two = decimal place (x/256)
# 00 21 3E 59 05 AB    0.1289 62.3477 5.6680
# FF C9 3E 5B 05 93   -0.2148 62.3555 5.5742
# 00 37 3E 5B 05 93    0.2148 62.3555 5.5742
# FF DF 3E 59 05 AB   -0.1289 62.3477 5.6680
# FC 29 3C 78 02 D3   -3.8398 60.4688 2.8242

# RSF Reference facemask
# vx vx vy vy vz vz sp sp            
# 00 21 3E 59 05 AB|00 04|F6 F1 13 85 00 00 3B B2|00 00 00 00 13 13 13 13 
# FF C9 3E 5B 05 93|00 04|40 A6 2E CB 00 00 3C 00|00 00 00 00 13 13 13 13 
# 00 37 3E 5B 05 93|00 04|40 A6 29 35 00 00 3C 00|00 00 00 00 13 13 13 13 
# FF DF 3E 59 05 AB|00 04|F6 F1 14 7B 00 00 3B B2|00 00 00 00 13 13 13 13 
# FC 29 3C 78 02 D3|00 04|DE F4 4C 6E 00 00 3B 85|00 00 00 00 13 13 13 13 
# FC B5 3B C5 03 AD|00 04|68 CE EE AE 3C 00 38 7D|00 00 00 00 13 13 13 13 

## RSF Reference Helmet
# vx vx vy vy vz vz sp sp                         u1 u2 v1 v2
# FF 9F 3A 97 FC 8B|00 13|E9 FF 9B EF F7 5F E8 06|00 00 39 FF|A4 D5 25 7D A4 D5 25 7D 
# FF FF 3A 96 FC 7F|00 13|F5 96 8A D1 F1 1F C7 FD|00 00 39 FF|A4 DD 25 7D A4 DD 25 7D 
# FF FF 3B 4D FC 6A|00 13|FF C0 4B FF EC 9F 9F FD|00 00 39 FF|A4 DD 25 67 A4 DD 25 67 
# FD 7D 3D CF 04 80|00 13|AF 4A 62 D0 92 FD D5 F3|24 3A 39 C1|34 7F 32 E4 34 7F 32 E4 
# FD 39 3D BA 04 52|00 13|F9 9F 78 AD 9F 3D A5 6B|25 33 39 B6|34 66 33 08 34 66 33 08

# 00 B9 3A 1E FC 9C 00 13 FA 9B 92 05 05 A4 75 FB|00 00 39 FF|A7 A4 24 46 A7 A4 24 46 
# 01 54 3A 1E FC BF 00 13 DB 97 CD 95 24 A8 3A 6B|00 00 39 FF|A7 90 24 48 A7 90 24 48
# 00 EC 3A D7 FC 88 00 13 D8 9B 86 61 27 A4 81 9F|00 00 39 FF|A7 9C 24 2E A7 9C 24 2E 
# FC C5 3A 00 FF F7 00 13 1D 09 BB B3 FB FB 0C 0E|33 0A 39 14|30 49 37 2C 30 49 37 2C 
# FC BF 39 FC FF F3 00 13 1D 09 BB B3 FB FB 0C 0E|33 06 39 14|30 42 37 2F 30 42 37 2F


# v start = 0A 76 20, vt start = 0A 76 74 20

# index
# 00 00 00 01 00 02 
# 00 00 00 03 00 01 
# 00 04 00 05 00 06 
# 00 04 00 07 00 05 
# 00 07 00 08 00 05 
# 00 07 00 09 00 08 
# 00 0A 00 08 00 09 
# 00 0A 00 09 00 0B 
# 00 0C 00 0A 00 0B 
# 00 0C 00 0D 00 0A
