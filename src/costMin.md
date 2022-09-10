# costMin.py

```
$ python costMin.py
cost= 31
34 {34} NAND 3
33 {33} NOT 2
32 {32} NAND 3
28 {28} NOT 2
27 {27} NAND 3
25 {25} NAND 3
23 {23} NAND 3
24 {24} NOT 2
26 {26} NOT 2
31 {31} NAND 3
30 {30} NOT 2
29 {29} NAND 3
==========successCount( 1 )=============
removeSet= {29, 30, 31}
addPartSet= {29, 30, 31}
34 {34} NAND 3
33 {33} NOT 2
32 {32} NAND 3
28 {28} NOT 2
27 {27} NAND 3
25 {25} NAND 3
23 {23} NAND 3
24 {24} NOT 2
26 {26} NOT 2
31 {29, 30, 31} NAND3 4
cost= 27
==========successCount( 2 )=============
removeSet= {32, 27, 28}
addPartSet= {32, 27, 28}
34 {34} NAND 3
33 {33} NOT 2
25 {25} NAND 3
23 {23} NAND 3
24 {24} NOT 2
26 {26} NOT 2
31 {29, 30, 31} NAND3 4
32 {32, 27, 28} NAND3 4
cost= 23
==========successCount( 3 )=============
removeSet= {32, 25, 26, 27, 28}
addPartSet= {25, 26, 27, 28}
34 {34} NAND 3
33 {33} NOT 2
23 {23} NAND 3
24 {24} NOT 2
31 {29, 30, 31} NAND3 4
28 {25, 26, 27, 28} AOI21 4
32 {32} NAND 3
cost= 21
==========successCount( 4 )=============
removeSet= {32, 33, 34}
addPartSet= {32, 33, 34}
23 {23} NAND 3
24 {24} NOT 2
31 {29, 30, 31} NAND3 4
28 {25, 26, 27, 28} AOI21 4
34 {32, 33, 34} NAND3 4
cost= 17
```
