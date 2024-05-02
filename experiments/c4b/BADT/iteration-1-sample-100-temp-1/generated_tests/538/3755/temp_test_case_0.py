
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = "3 3 3 3 3"
        self.assertEqual(patched_source(input_0), original_source(input_0))
            


    def test1(self):
        input_1 = "5 5 5 10 10"
        self.assertEqual(patched_source(input_1), original_source(input_1))
            


    def test2(self):
        input_2 = "3 3 3 3 3"
        self.assertEqual(patched_source(input_2), original_source(input_2))
            


    def test3(self):
        input_3 = "5 5 5 5 5"
        self.assertEqual(patched_source(input_3), original_source(input_3))
            


    def test4(self):
        input_4 = "1 1 1 2 2 2 3 3 3"
        self.assertEqual(patched_source(input_4), original_source(input_4))
            


    def test5(self):
        input_5 = "5 5 5 2 2 2"
        self.assertEqual(patched_source(input_5), original_source(input_5))
            


    def test6(self):
        input_6 = "1 1 1 2 2 3 3 3 4 4 4 5 5 5"
        self.assertEqual(patched_source(input_6), original_source(input_6))
            


    def test7(self):
        input_7 = "4 4 4 5 5 5 5 6 6 6"
        self.assertEqual(patched_source(input_7), original_source(input_7))
            


    def test8(self):
        input_8 = "7 3 7 3 20 20 20 20 20 20 20"
        self.assertEqual(patched_source(input_8), original_source(input_8))
            


    def test9(self):
        input_9 = "5 5 5 5 5"
        self.assertEqual(patched_source(input_9), original_source(input_9))
            


    def test10(self):
        input_10 = "7 3 7 3 20 5"
        self.assertEqual(patched_source(input_10), original_source(input_10))
            


    def test11(self):
        input_11 = "3 3 3 4 4"
        self.assertEqual(patched_source(input_11), original_source(input_11))
            


    def test12(self):
        input_12 = "5 5 5 5 5"
        self.assertEqual(patched_source(input_12), original_source(input_12))
            


    def test13(self):
        input_13 = "2 2 2 2 2 2 3 3 3 4 4 5 5 6 6"
        self.assertEqual(patched_source(input_13), original_source(input_13))
            


    def test14(self):
        input_14 = "7 7 7 3 3 3 20"
        self.assertEqual(patched_source(input_14), original_source(input_14))
            


    def test15(self):
        input_15 = "1 1 1 5 5 5 2 2 3 4 10 10 10"
        self.assertEqual(patched_source(input_15), original_source(input_15))
            


    def test16(self):
        input_16 = "7 3 7 3 20 10 10"
        self.assertEqual(patched_source(input_16), original_source(input_16))
            


    def test17(self):
        input_17 = "10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 1 2 3 4 5 6 7 8 9 11 12 13 14 15 16 17 18 19 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 41 42 43 44 45 46 47 48 49 51 52 53 54 55 56 57 58 59 61 62 63 64 65 66 67 68 69 71 72 73 74 75 76 77 78 79 81 82 83 84 85 86 87 88 89 91 92 93 94 95 96 97 98 99 101 102 103 104 105 106 107 108 109 111 112 113 114 115 116 117 118 119 121 122 123 124 125 126 127 128 129 131 132 133 134 135 136 137 138 139 141 142 143 144 145 146 147 148 149 151 152 153 154 155 156 157 158 159 161 162 163 164 165 166 167 168 169 171 172 173 174 175 176 177 178 179 181 182 183 184 185 186 187 188 189 191 192 193 194 195 196 197 198 199 201 202 203 204 205 206 207 208 209 211 212 213 214 215 216 217 218 219 221 222 223 224 225 226 227 228 229 231 232 233 234 235 236 237 238 239 241 242 243 244 245 246 247 248 249 251 252 253 254 255 256 257 258 259 261 262 263 264 265 266 267 268 269 271 272 273 274 275 276 277 278 279 281 282 283 284 285 286 287 288 289 291 292 293 294 295 296 297 298 299 301 302 303 304 305 306 307 308 309 311 312 313 314 315 316 317 318 319 321 322 323 324 325 326 327 328 329 331 332 333 334 335 336 337 338 339 341 342 343 344 345 346 347 348 349 351 352 353 354 355 356 357 358 359 361 362 363 364 365 366 367 368 369 371 372 373 374 375 376 377 378 379 381 382 383 384 385 386 387 388 389 391 392 393 394 395 396 397 398 399 401 402 403 404 405 406 407 408 409 411 412 413 414 415 416 417 418 419 421 422 423 424 425 426 427 428 429 431 432 433 434 435 436 437 438 439 441 442 443 444 445 446 447 448 449 451 452 453 454 455 456 457 458 459 461 462 463 464 465 466 467 468 469 471 472 473 474 475 476 477 478 479 481 482 483 484 485 486 487 488 489 491 492 493 494 495 496 497 498 499 501 502 503 504 505 506 507 508 509 511 512 513 514 515 516 517 518 519 521 522 523 524 525 526 527 528 529 531 532 533 534 535 536 537 538 539 541 542 543 544 545 546 547 548 549 551 552 553 554 555 556 557 558 559 561 562 563 564 565 566 567 568 569 571 572 573 574 575 576 577 578 579 581 582 583 584 585 586 587 588 589 591 592 593 594 595 596 597 598 599 601 602 603 604 605 606 607 608 609 611 612 613 614 615 616 617 618 619 621 622 623 624 625 626 627 628 629 631 632 633 634 635 636 637 638 639 641 642 643 644 645 646 647 648 649 651 652 653 654 655 656 657 658 659 661 662 663 664 665 666 667 668 669 671 672 673 674 675 676 677 678 679 681 682 683 684 685 686 687 688 689 691 692 693 694 695 696 697 698 699 701 702 703 704 705 706 707 708 709 711 712 713 714 715 716 717 718 719 721 722 723 724 725 726 727 728 729 731 732 733 734 735 736 737 738 739 741 742 743 744 745 746 747 748 749 751 752 753 754 755 756 757 758 759 761 762 763 764 765 766 767 768 769 771 772 773 774 775 776 777 778 779 781 782 783 784 785 786 787 788 789 791 792 793 794 795 796 797 798 799 801 802 803 804 805 806 807 808 809 811 812 813 814 815 816 817 818 819 821 822 823 824 825 826 827 828 829 831 832 833 834 835 836 837 838 839 841 842 843 844 845 846 847 848 849 851 852 853 854 855 856 857 858 859 861 862 863 864 865 866 867 868 869 871 872 873 874 875 876 877 878 879 881 882 883 884 885 886 887 888 889 891 892 893 894 895 896 897 898 899 901 902 903 904 905 906 907 908 909 911 912 913 914 915 916 917 918 919 921 922 923 924 925 926 927 928 929 931 932 933 934 935 936 937 938 939 941 942 943 944 945 946 947 948 949 951 952 953 954 955 956 957 958 959 961 962 963 964 965 966 967 968 969 971 972 973 974 975 976 977 978 979 981 982 983 984 985 986 987 988 989 991 992 993 994 995 996 997 998 999 1001 1002 1003 1004 1005 1006 1007 1008 1009 1011 1012 1013 1014 1015 1016 1017 1018 1019 1021 1022 1023 1024 1025 1026 1027 1028 1029 1031 1032 1033 1034 1035 1036 1037 1038 1039 1041 1042 1043 1044 1045 1046 1047 1048 1049 1051 1052 1053 1054 1055 1056 1057 1058 1059 1061 1062 1063 1064 1065 1066 1067 1068 1069 1071 1072 1073 1074 1075 1076 1077 1078 1079 1081 1082 1083 1084 1085 1086 1087 1088 1089 1091 1092 1093 1094 1095 1096 1097 1098 1099 1101 1102 1103 1104 1105 1106 1107 1108 1109 1111 1112 1113 1114 1115 1116 1117 1118 1119 1152 3000 3001 3002 3003 3004 3005 3006 3007 3008 3009 3010"
        self.assertEqual(patched_source(input_17), original_source(input_17))
            


    def test18(self):
        input_18 = "5 5 5 5 5 5 5 5 5 5"
        self.assertEqual(patched_source(input_18), original_source(input_18))
            


    def test19(self):
        input_19 = "5 5 5 6 6"
        self.assertEqual(patched_source(input_19), original_source(input_19))
            


    def test20(self):
        input_20 = "1 2 1 2 1"
        self.assertEqual(patched_source(input_20), original_source(input_20))
            


    def test21(self):
        input_21 = "1 1 2 2 3 3 4 4 5 6 7"
        self.assertEqual(patched_source(input_21), original_source(input_21))
            


    def test22(self):
        input_22 = "5 5 5 5 5 5 5 10"
        self.assertEqual(patched_source(input_22), original_source(input_22))
            


    def test23(self):
        input_23 = "1 1 2 2 3 3 4 4 5 5 6 6 7"
        self.assertEqual(patched_source(input_23), original_source(input_23))
            


    def test24(self):
        input_24 = "7 3 7 3 20 20"
        self.assertEqual(patched_source(input_24), original_source(input_24))
            


    def test25(self):
        input_25 = "1 1 2 2 3 3 4 4 5 5"
        self.assertEqual(patched_source(input_25), original_source(input_25))
            


    def test26(self):
        input_26 = "5 5 5 4"
        self.assertEqual(patched_source(input_26), original_source(input_26))
            


    def test27(self):
        input_27 = "2 4 2 4 2 4"
        self.assertEqual(patched_source(input_27), original_source(input_27))
            


    def test28(self):
        input_28 = "7 7 3 3 20"
        self.assertEqual(patched_source(input_28), original_source(input_28))
            


    def test29(self):
        input_29 = "5 5 5 5 5 5"
        self.assertEqual(patched_source(input_29), original_source(input_29))
            


    def test30(self):
        input_30 = "5 5 5 10 15 15 15 20 20 20"
        self.assertEqual(patched_source(input_30), original_source(input_30))
            


    def test31(self):
        input_31 = "2 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 3 3 4 4 4 4 5 5 5 5 5 5 5 5 5 5"
        self.assertEqual(patched_source(input_31), original_source(input_31))
            


    def test32(self):
        input_32 = "55 55 55 55 55 55 55 55 55 55 55 55 55 55 55 55 55 55 55 55 55 55 55 55 55 55 55 55 55 55"
        self.assertEqual(patched_source(input_32), original_source(input_32))
            


    def test33(self):
        input_33 = "4 4 4 5 5 6 6"
        self.assertEqual(patched_source(input_33), original_source(input_33))
            


    def test34(self):
        input_34 = "7 3 7 3 20 3"
        self.assertEqual(patched_source(input_34), original_source(input_34))
            


    def test35(self):
        input_35 = "4 4 4 2"
        self.assertEqual(patched_source(input_35), original_source(input_35))
            


    def test36(self):
        input_36 = "1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9 10 10 11 11 12 12 13 13 14 14 15 15 16 16 17 17 18 18 19 19 20 20"
        self.assertEqual(patched_source(input_36), original_source(input_36))
            


    def test37(self):
        input_37 = "1 1 1 2 3 3 3 4"
        self.assertEqual(patched_source(input_37), original_source(input_37))
            


    def test38(self):
        input_38 = "5 5 5 10 10 10"
        self.assertEqual(patched_source(input_38), original_source(input_38))
            


    def test39(self):
        input_39 = "1 1 1 2 2 2 3 3 3 4 4 4"
        self.assertEqual(patched_source(input_39), original_source(input_39))
            


    def test40(self):
        input_40 = "5 5 5 2 3"
        self.assertEqual(patched_source(input_40), original_source(input_40))
            


    def test41(self):
        input_41 = "1 1 1 2 2 2 3 3 3"
        self.assertEqual(patched_source(input_41), original_source(input_41))
            


    def test42(self):
        input_42 = "5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5"
        self.assertEqual(patched_source(input_42), original_source(input_42))
            


    def test43(self):
        input_43 = "1 1 1 2 2 2 3 3 3"
        self.assertEqual(patched_source(input_43), original_source(input_43))
            


    def test44(self):
        input_44 = "5 5 5 5 5"
        self.assertEqual(patched_source(input_44), original_source(input_44))
            


    def test45(self):
        input_45 = "5 5 5 5 5 5"
        self.assertEqual(patched_source(input_45), original_source(input_45))
            


    def test46(self):
        input_46 = "1 1 2 2 2 3 3 3"
        self.assertEqual(patched_source(input_46), original_source(input_46))
            


    def test47(self):
        input_47 = "2 2 3 3 3 4 4"
        self.assertEqual(patched_source(input_47), original_source(input_47))
            


    def test48(self):
        input_48 = "8 8 9 8 8 9 9"
        self.assertEqual(patched_source(input_48), original_source(input_48))
            


    def test49(self):
        input_49 = "1 1 1 2 2 2"
        self.assertEqual(patched_source(input_49), original_source(input_49))
            


    def test50(self):
        input_50 = "1 1 1 2 2 2 3 3 3 4 4 4"
        self.assertEqual(patched_source(input_50), original_source(input_50))
            


    def test51(self):
        input_51 = "1 1 1 2 2 2 3 3 3 4 4 4 5 5 5"
        self.assertEqual(patched_source(input_51), original_source(input_51))
            


    def test52(self):
        input_52 = "1 1 1 2 2 3 3 4 4 4 5 5"
        self.assertEqual(patched_source(input_52), original_source(input_52))
            


    def test53(self):
        input_53 = "2 2 2 2 2 2 2 3 4 5 6 6 6 6 6 7 8 9 29 30 31"
        self.assertEqual(patched_source(input_53), original_source(input_53))
            


    def test54(self):
        input_54 = "10 10 5 5 5 5 5"
        self.assertEqual(patched_source(input_54), original_source(input_54))
            


    def test55(self):
        input_55 = "5 5 5 5 5 5 50"
        self.assertEqual(patched_source(input_55), original_source(input_55))
            


    def test56(self):
        input_56 = "5 5 10 10 15 15 20 20 25 25"
        self.assertEqual(patched_source(input_56), original_source(input_56))
            


    def test57(self):
        input_57 = "9 9 9 5 5"
        self.assertEqual(patched_source(input_57), original_source(input_57))
            


    def test58(self):
        input_58 = "5 5 5 5 5"
        self.assertEqual(patched_source(input_58), original_source(input_58))
            


    def test59(self):
        input_59 = "7 3 7 3 5"
        self.assertEqual(patched_source(input_59), original_source(input_59))
            


    def test60(self):
        input_60 = "4 4 4 4 4 4 4 4 4 4 4"
        self.assertEqual(patched_source(input_60), original_source(input_60))
            


    def test61(self):
        input_61 = "4 4 4 4 4 4 8"
        self.assertEqual(patched_source(input_61), original_source(input_61))
            


    def test62(self):
        input_62 = "4 4 4 4 4 4 4"
        self.assertEqual(patched_source(input_62), original_source(input_62))
            


    def test63(self):
        input_63 = "7 3 7 3 20 20 20 20 20 15 5"
        self.assertEqual(patched_source(input_63), original_source(input_63))
            


    def test64(self):
        input_64 = "1 1 1 2 2 3"
        self.assertEqual(patched_source(input_64), original_source(input_64))
            


    def test65(self):
        input_65 = "1 1 2 2 3 3 4 4 5 5"
        self.assertEqual(patched_source(input_65), original_source(input_65))
            


    def test66(self):
        input_66 = "4 4 4 4 4 4 4 4 4"
        self.assertEqual(patched_source(input_66), original_source(input_66))
            


    def test67(self):
        input_67 = "1 1 2 2 3 3 4 4"
        self.assertEqual(patched_source(input_67), original_source(input_67))
            


    def test68(self):
        input_68 = "7 3 7 3 20 20"
        self.assertEqual(patched_source(input_68), original_source(input_68))
            


    def test69(self):
        input_69 = "1 1 2 2 3 3 4 4 5 5"
        self.assertEqual(patched_source(input_69), original_source(input_69))
            


    def test70(self):
        input_70 = "2 2 2 3 3 3"
        self.assertEqual(patched_source(input_70), original_source(input_70))
            


    def test71(self):
        input_71 = "3 3 3 3 3 3 4 4 4"
        self.assertEqual(patched_source(input_71), original_source(input_71))
            


    def test72(self):
        input_72 = "3 3 3 3 3"
        self.assertEqual(patched_source(input_72), original_source(input_72))
            


    def test73(self):
        input_73 = "5 5 5 10 10 15"
        self.assertEqual(patched_source(input_73), original_source(input_73))
            


    def test74(self):
        input_74 = "7 3 7 3 20 20"
        self.assertEqual(patched_source(input_74), original_source(input_74))
            


    def test75(self):
        input_75 = "1 1 2 2 3 3 4 4 5 5"
        self.assertEqual(patched_source(input_75), original_source(input_75))
            


    def test76(self):
        input_76 = "2 2 2 3 3 3 4 4 4 5 5 5"
        self.assertEqual(patched_source(input_76), original_source(input_76))
            


    def test77(self):
        input_77 = "7 3 7 3 20 20"
        self.assertEqual(patched_source(input_77), original_source(input_77))
            


    def test78(self):
        input_78 = "5 5 18 18 18 18 20 20"
        self.assertEqual(patched_source(input_78), original_source(input_78))
            


    def test79(self):
        input_79 = "2 2 2 3 3 3 3 3 3 4 4 4"
        self.assertEqual(patched_source(input_79), original_source(input_79))
            


    def test80(self):
        input_80 = "5 5 5 1 2 3 4 5 6 7 8 9 10"
        self.assertEqual(patched_source(input_80), original_source(input_80))
            


    def test81(self):
        input_81 = "7 3 7 3 5"
        self.assertEqual(patched_source(input_81), original_source(input_81))
            


    def test82(self):
        input_82 = "4 4 4 4 4"
        self.assertEqual(patched_source(input_82), original_source(input_82))
            


    def test83(self):
        input_83 = "5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 4"
        self.assertEqual(patched_source(input_83), original_source(input_83))
            


    def test84(self):
        input_84 = "1 1 2 2 3 3 4 4 5 5 6 6"
        self.assertEqual(patched_source(input_84), original_source(input_84))
            


    def test85(self):
        input_85 = "6 6 6 5 5"
        self.assertEqual(patched_source(input_85), original_source(input_85))
            


    def test86(self):
        input_86 = "4 4 4 4 4 4 4 4 4"
        self.assertEqual(patched_source(input_86), original_source(input_86))
            


    def test87(self):
        input_87 = "1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9 10 10 11 11 12 12 99 99 100"
        self.assertEqual(patched_source(input_87), original_source(input_87))
            


    def test88(self):
        input_88 = "7 7 7 7 7 7 7 20"
        self.assertEqual(patched_source(input_88), original_source(input_88))
            


    def test89(self):
        input_89 = "7 3 7 3 20 20 20 30"
        self.assertEqual(patched_source(input_89), original_source(input_89))
            


    def test90(self):
        input_90 = "1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9 10 10"
        self.assertEqual(patched_source(input_90), original_source(input_90))
            


    def test91(self):
        input_91 = "1 1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9 11 11 12 12 13 13 14 14 15 15 16 16 17 17 18 18 19 19 20"
        self.assertEqual(patched_source(input_91), original_source(input_91))
            


    def test92(self):
        input_92 = "1 1 1 1 2"
        self.assertEqual(patched_source(input_92), original_source(input_92))
            


    def test93(self):
        input_93 = "7 3 7 3 20 20"
        self.assertEqual(patched_source(input_93), original_source(input_93))
            


    def test94(self):
        input_94 = "5 5 5 5"
        self.assertEqual(patched_source(input_94), original_source(input_94))
            


    def test95(self):
        input_95 = "1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10"
        self.assertEqual(patched_source(input_95), original_source(input_95))
            


    def test96(self):
        input_96 = "1 1 1 2 2 2 3 3 3"
        self.assertEqual(patched_source(input_96), original_source(input_96))
            


    def test97(self):
        input_97 = "2 2 2 3 3 3 3"
        self.assertEqual(patched_source(input_97), original_source(input_97))
            


if __name__ == '__main__':
    unittest.main()  
    
    