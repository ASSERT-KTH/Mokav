
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = "3 3 3 3 3"
        self.assertEqual(patched_source(input_0), original_source(input_0))
            


    def test1(self):
        input_1 = "1 1 1 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9 10 10 11 11 12 12 13 13"
        self.assertEqual(patched_source(input_1), original_source(input_1))
            


    def test2(self):
        input_2 = "7 7 7 3 20"
        self.assertEqual(patched_source(input_2), original_source(input_2))
            


    def test3(self):
        input_3 = "10 20 10 20 30"
        self.assertEqual(patched_source(input_3), original_source(input_3))
            


    def test4(self):
        input_4 = "1 2 1 2 1 2 1 2"
        self.assertEqual(patched_source(input_4), original_source(input_4))
            


    def test5(self):
        input_5 = "1 1 1 1 2"
        self.assertEqual(patched_source(input_5), original_source(input_5))
            


    def test6(self):
        input_6 = "7 3 7 3 20 4 4 4 4 5 5 5 1 2 3"
        self.assertEqual(patched_source(input_6), original_source(input_6))
            


    def test7(self):
        input_7 = "6 1 1 1 1 6 6 6"
        self.assertEqual(patched_source(input_7), original_source(input_7))
            


    def test8(self):
        input_8 = "3 3 3 3 3 3 3 3"
        self.assertEqual(patched_source(input_8), original_source(input_8))
            


    def test9(self):
        input_9 = "5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 "
        self.assertEqual(patched_source(input_9), original_source(input_9))
            


    def test10(self):
        input_10 = "10 10 10 10 10"
        self.assertEqual(patched_source(input_10), original_source(input_10))
            


    def test11(self):
        input_11 = "1 1 2 2 3 3 4 4 5 5 6 6"
        self.assertEqual(patched_source(input_11), original_source(input_11))
            


    def test12(self):
        input_12 = "5 5 5 10 10 10 10 15 15 15 15 15 22 22 22 22 22 22"
        self.assertEqual(patched_source(input_12), original_source(input_12))
            


    def test13(self):
        input_13 = "1 1 1 2 2 2 3 3 3 4 4 4"
        self.assertEqual(patched_source(input_13), original_source(input_13))
            


    def test14(self):
        input_14 = "5 5 5 5"
        self.assertEqual(patched_source(input_14), original_source(input_14))
            


    def test15(self):
        input_15 = "5 5 5 5 5"
        self.assertEqual(patched_source(input_15), original_source(input_15))
            


    def test16(self):
        input_16 = "7 3 7 3 20 999"
        self.assertEqual(patched_source(input_16), original_source(input_16))
            


    def test17(self):
        input_17 = "4 4 4 4"
        self.assertEqual(patched_source(input_17), original_source(input_17))
            


    def test18(self):
        input_18 = "1 1 2 3 4 5 6 7 8 9 10"
        self.assertEqual(patched_source(input_18), original_source(input_18))
            


    def test19(self):
        input_19 = "3 3 3 3 3"
        self.assertEqual(patched_source(input_19), original_source(input_19))
            


    def test20(self):
        input_20 = "10 10 5 5 5 5"
        self.assertEqual(patched_source(input_20), original_source(input_20))
            


    def test21(self):
        input_21 = "6 2 6 2 3"
        self.assertEqual(patched_source(input_21), original_source(input_21))
            


    def test22(self):
        input_22 = "8 5 8 5 8"
        self.assertEqual(patched_source(input_22), original_source(input_22))
            


    def test23(self):
        input_23 = "1 1 1 2 2 3 3 4 4"
        self.assertEqual(patched_source(input_23), original_source(input_23))
            


    def test24(self):
        input_24 = "9 4 9 4 18"
        self.assertEqual(patched_source(input_24), original_source(input_24))
            


    def test25(self):
        input_25 = "7 3 7 3 20"
        self.assertEqual(patched_source(input_25), original_source(input_25))
            


    def test26(self):
        input_26 = "2 2 2 2 2 2 2 2 5"
        self.assertEqual(patched_source(input_26), original_source(input_26))
            


    def test27(self):
        input_27 = "2 2 2 2 2 3 4 4 4 4 4 5 5 6 6 6 6 6 7 7 7 8 8 8 9 9 9 9 9 10 10 10 10 10"
        self.assertEqual(patched_source(input_27), original_source(input_27))
            


    def test28(self):
        input_28 = "1 1 1 1 2 2 2 2 3 3 3 3"
        self.assertEqual(patched_source(input_28), original_source(input_28))
            


    def test29(self):
        input_29 = "8 8 8 8 8"
        self.assertEqual(patched_source(input_29), original_source(input_29))
            


    def test30(self):
        input_30 = "4 2 1 5 1 3 8 6 7 6"
        self.assertEqual(patched_source(input_30), original_source(input_30))
            


    def test31(self):
        input_31 = "3 3 3 3 3 3 3 5 8 4 3 3 2 4 7 8 6 9 0 1 4 5 6 7 8 9 0"
        self.assertEqual(patched_source(input_31), original_source(input_31))
            


    def test32(self):
        input_32 = "1 2 3 4 1 2 3 4 1 2 3 4 5"
        self.assertEqual(patched_source(input_32), original_source(input_32))
            


    def test33(self):
        input_33 = "2 2 2 4 4"
        self.assertEqual(patched_source(input_33), original_source(input_33))
            


    def test34(self):
        input_34 = "9 2 9 2 9"
        self.assertEqual(patched_source(input_34), original_source(input_34))
            


    def test35(self):
        input_35 = "1 2 3 4 5 6 7 8 9 10"
        self.assertEqual(patched_source(input_35), original_source(input_35))
            


    def test36(self):
        input_36 = "5 5 5 6 6"
        self.assertEqual(patched_source(input_36), original_source(input_36))
            


    def test37(self):
        input_37 = "5 5 5 5 5 5 5 5"
        self.assertEqual(patched_source(input_37), original_source(input_37))
            


    def test38(self):
        input_38 = "1 2 3 1 2 3 4 5 6"
        self.assertEqual(patched_source(input_38), original_source(input_38))
            


    def test39(self):
        input_39 = "1 2 1 3 2 1 4 5 2 1 4 5 5 6 3 2 4 5 1 6 3 2 3 1 5 4 6 2 3 1 4 6 3 5 4 1 2 3 4 5 6 1 2 3 4 5 1 3 2 4 6 5 1 2 3 5 6 1 2 3 4 5 6"
        self.assertEqual(patched_source(input_39), original_source(input_39))
            


    def test40(self):
        input_40 = "5 5 5 5 5"
        self.assertEqual(patched_source(input_40), original_source(input_40))
            


    def test41(self):
        input_41 = "1 2 3 4 5"
        self.assertEqual(patched_source(input_41), original_source(input_41))
            


    def test42(self):
        input_42 = "5 5 5 5 5 5 5 5 5 5"
        self.assertEqual(patched_source(input_42), original_source(input_42))
            


    def test43(self):
        input_43 = "2 4 6 8 10"
        self.assertEqual(patched_source(input_43), original_source(input_43))
            


    def test44(self):
        input_44 = "1 2 3 4 5 6 7 8 9 10 11"
        self.assertEqual(patched_source(input_44), original_source(input_44))
            


    def test45(self):
        input_45 = "4 4 4 4 4"
        self.assertEqual(patched_source(input_45), original_source(input_45))
            


    def test46(self):
        input_46 = "1 1 1 2 2"
        self.assertEqual(patched_source(input_46), original_source(input_46))
            


    def test47(self):
        input_47 = "5 5 5 5 5 10 10 10 10 10 15 15 15 15 15 20 20 20 20 20 25 25 25 25 25 30 30 30 30 30"
        self.assertEqual(patched_source(input_47), original_source(input_47))
            


    def test48(self):
        input_48 = "1 1 1 1 2 2 2 3 3 3 4 4 4 4 4"
        self.assertEqual(patched_source(input_48), original_source(input_48))
            


    def test49(self):
        input_49 = "4 2 4 2 4"
        self.assertEqual(patched_source(input_49), original_source(input_49))
            


    def test50(self):
        input_50 = "2 2 2 2 2 2"
        self.assertEqual(patched_source(input_50), original_source(input_50))
            


    def test51(self):
        input_51 = "5 5 5 10 10 10 15 15 15"
        self.assertEqual(patched_source(input_51), original_source(input_51))
            


    def test52(self):
        input_52 = "4 4 4 4 4 4 4 4 3 7 3 7"
        self.assertEqual(patched_source(input_52), original_source(input_52))
            


    def test53(self):
        input_53 = "7 3 7 3 20 100"
        self.assertEqual(patched_source(input_53), original_source(input_53))
            


    def test54(self):
        input_54 = "4 4 4 4 4 4"
        self.assertEqual(patched_source(input_54), original_source(input_54))
            


    def test55(self):
        input_55 = "9 2 9 2 9"
        self.assertEqual(patched_source(input_55), original_source(input_55))
            


    def test56(self):
        input_56 = "5 5 5 20 20 20 100 100 100 500 500 500 999 999 999"
        self.assertEqual(patched_source(input_56), original_source(input_56))
            


    def test57(self):
        input_57 = "1 1 2 2 3 3 4 4 5 5"
        self.assertEqual(patched_source(input_57), original_source(input_57))
            


    def test58(self):
        input_58 = "4 5 4 5 4 5"
        self.assertEqual(patched_source(input_58), original_source(input_58))
            


    def test59(self):
        input_59 = "1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9 10 10"
        self.assertEqual(patched_source(input_59), original_source(input_59))
            


    def test60(self):
        input_60 = "1 1 1 3 3 3 5 5 5 7 7 7"
        self.assertEqual(patched_source(input_60), original_source(input_60))
            


    def test61(self):
        input_61 = "5 5 10 10 10 5 5"
        self.assertEqual(patched_source(input_61), original_source(input_61))
            


    def test62(self):
        input_62 = "5 2 5 2 5 2 5 2"
        self.assertEqual(patched_source(input_62), original_source(input_62))
            


    def test63(self):
        input_63 = "10 20 10 20"
        self.assertEqual(patched_source(input_63), original_source(input_63))
            


    def test64(self):
        input_64 = "5 5 5 5 5 5 12 12 12 12 12 12 7 7 7 7 7 7 3 3 3 3 3 3 20 20 20 20 20 20"
        self.assertEqual(patched_source(input_64), original_source(input_64))
            


    def test65(self):
        input_65 = "3 3 1 1 1 1 2 2 2 2"
        self.assertEqual(patched_source(input_65), original_source(input_65))
            


    def test66(self):
        input_66 = "2 2 2 2 2 2 2 3 4 5"
        self.assertEqual(patched_source(input_66), original_source(input_66))
            


    def test67(self):
        input_67 = "5 5 5 5 5 5"
        self.assertEqual(patched_source(input_67), original_source(input_67))
            


    def test68(self):
        input_68 = "7 3 7 3 20 0 1 2 3 4 5 6 8 9 78 98 88 77 66 55 44 33 22 11 10 20 30 40 50 60 70 80 90 100 110 120 130 140 150 160 170 180 190 200 210 220 230 240 250 260 270 280 290 300 310 320 330 340 350 360 370 380 390 400 410 420 430 440 450 460 470 480 490 500 510 520 530 540 550 560 570 580 590 600 610 620 630 640 650 660 670 680 690 700 710 720 730 740 750 760 770 780 790 800 810 820 830 840 850 860 870 880 890 900 910 920 930 940 950 960 970 980 990 1000 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94 96 98 99 101 103 105 107 109 111 113 115 117 119 121 123 125 127 129 131 133 135 137 139 141 143 145 147 149 151 153 155 157 159 161 163 165 167 169 171 173 175 177 179 181 183 185 187 189 191 193 195 197 199 101 202 204 206 208 210 212 214 216 217 219 221 223 225 227 229 231 233 235 237 239 241 243 245 247 249 251 253 255 257 259 261 263 265 267 269 271 273 275 277 279 281 283 285 287 289 291 293 295 297 299 301 303 305 307 309 311 313 315 317 319 321 323 325 327 329 331 333 335 337 339 341 343 345 347 349 351 353 355 357 359 361 363 365 367 369 371 373 375 377 379 381 383 385 387 389 391 393 395 397 399 401 403 405 407 409 411 413 415 417 419 421 423 425 427 429 431 433 435 437 439 441 443 445 447 449 451 453 455 457 459 461 463 465 467 469 471 473 475 477 479 481 483 485 487 489 491 493 495 497 499 501 503 505 507 509 511 513 515 517 519 521 523 525 527 529 531 533 535 537 539 541 543 545 547 549 551 553 555 557 559 561 563 565 567 569 571 573 575 577 579 581 583 585 587 589 591 593 595 597 599 601 603 605 607 609 611 613 615 617 619 621 623 625 627 629 631 633 635 637 639 641 643 645 647 649 651 653 655 657 659 661 663 665 667 669 671 673 675 677 679 681 683 685 687 689 691 693 695 697 699 701 703 705 707 709 711 713 715 717 719 721 723 725 727 729 731 733 735 737 739 741 743 745 747 749 751 753 755 757 759 761 763 765 767 769 771 773 775 777 779 781 783 785 787 789 791 793 795 797 799 801 803 805 807 809 811 813 815 817 819 821 823 825 827 829 831 833 835 837 839 841 843 845 847 849 851 853 855 857 859 861 863 865 867 869 871 873 875 877 879 881 883 885 887 889 891 893 895 897 899 901 903 905 907 909 911 913 915 917 919 921 923 925 927 929 931 933 935 937 939 941 943 945 947 949 951 953 955 957 959 961 963 965 967 969 971 973 975 977 979 981 983 985 987 989 991 993 995 997 999 998 996 994 992 990 988 986 984 982 980 978 976 974 972 970 968 966 964 962 960 958 956 954 952 950 948 946 944 942 940 938 936 934 932 930 928 926 924 922 920 918 916 914 912 910 908 906 904 902 900 898 896 894 892 890 888 886 884 882 880 878 876 874 872 870 868 866 864 862 860 858 856 854 852 850 848 846 844 842 840 838 836 834 832 830 828 826 824 822 820 818 816 814 812 810 808 806 804 802 800 798 796 794 792 790 788 786 784 782 780 778 776 774 772 770 768 766 764 762 760 758 756 754 752 750 748 746 744 742 740 738 736 734 732 730 728 726 724 722 720 718 716 714 712 710 708 706 704 702 700 698 696 694 692 690 688 686 684 682 680 678 676 674 672 670 668 666 664 662 660 658 656 654 652 650 648 646 644 642 640 638 636 634 632 630 628 626 624 622 620 618 616 614 612 610 608 606 604 602 600 598 596 594 592 590 588 586 584 582 580 578 576 574 572 570 568 566 564 562 560 558 556 554 552 550 548 546 544 542 540 538 536 534 532 530 528 526 524 522 520 518 516 514 512 510 508 506 504 502 500 498 496 494 492 490 488 486 484 482 480 478 476 474 472 470 468 466 464 462 460 458 456 454 452 450 448 446 444 442 440 438 436 434 432 430 428 426 424 422 420 418 416 414 412 410 408 406 404 402 400 398 396 394 392 390 388 386 384 382 380 378 376 374 372 370 368 366 364 362 360 358 356 354 352 350 348 346 344 342 340 338 336 334 332 330 328 326 324 322 320 318 316 314 312 310 308 306 304 302 300 298 296 294 292 290 288 286 284 282 280 278 276 274 272 270 268 266 264 262 260 258 256 254 252 250 248 246 244 242 240 238 236 234 232 230 228 226 224 222 220 218 216 214 212 210 208 206 204 202 200 198 196 194 192 190 188 186 184 182 180 178 176 174 172 170 168 166 164 162 160 158 156 154 152 150 148 146 144 142 140 138 136 134 132 130 128 126 124 122 120 118 116 114 112 110 108 106 104 102 99 97 95 93 91 89 87 85 83 81 79 77 75 73 71 69 67 65 63 61 59 57 55 53 51 49 47 45 43 41 39 37 35 33 31 29 27 25 23 21 19 17 15 13 11 9 7 5 4 2 0 1 3 6 8 10 12 14 16 18 20"
        self.assertEqual(patched_source(input_68), original_source(input_68))
            


    def test69(self):
        input_69 = "7 3 7 3 20 20 20 20 20"
        self.assertEqual(patched_source(input_69), original_source(input_69))
            


    def test70(self):
        input_70 = "5 5 5 5 5"
        self.assertEqual(patched_source(input_70), original_source(input_70))
            


    def test71(self):
        input_71 = "7 3 7 3 20 10 10 10 10 10 10"
        self.assertEqual(patched_source(input_71), original_source(input_71))
            


    def test72(self):
        input_72 = "5 1 5 1 5 1 5 1 5 1 10"
        self.assertEqual(patched_source(input_72), original_source(input_72))
            


    def test73(self):
        input_73 = "1 2 1 1 1 1 1 1 1 1 1"
        self.assertEqual(patched_source(input_73), original_source(input_73))
            


    def test74(self):
        input_74 = "8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"
        self.assertEqual(patched_source(input_74), original_source(input_74))
            


    def test75(self):
        input_75 = "1 1 1 0 0"
        self.assertEqual(patched_source(input_75), original_source(input_75))
            


    def test76(self):
        input_76 = "9 2 2 9 5"
        self.assertEqual(patched_source(input_76), original_source(input_76))
            


    def test77(self):
        input_77 = "1 2 3 4 5 1 2 3 4 5"
        self.assertEqual(patched_source(input_77), original_source(input_77))
            


    def test78(self):
        input_78 = "5 5 5 5 5 5 5 5 5 5 5 5 5 5 5"
        self.assertEqual(patched_source(input_78), original_source(input_78))
            


    def test79(self):
        input_79 = "5 5 5 5 5"
        self.assertEqual(patched_source(input_79), original_source(input_79))
            


    def test80(self):
        input_80 = "1 5 1 5 1 5 1 5 1 5 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2"
        self.assertEqual(patched_source(input_80), original_source(input_80))
            


    def test81(self):
        input_81 = "1 2 1 3 2 3 1 2 3 4"
        self.assertEqual(patched_source(input_81), original_source(input_81))
            


    def test82(self):
        input_82 = "1 1 1 2 2"
        self.assertEqual(patched_source(input_82), original_source(input_82))
            


    def test83(self):
        input_83 = "5 5 5 0"
        self.assertEqual(patched_source(input_83), original_source(input_83))
            


    def test84(self):
        input_84 = "1 2 3 1 1 1 4 5 6"
        self.assertEqual(patched_source(input_84), original_source(input_84))
            


    def test85(self):
        input_85 = "7 3 7 3 20 999"
        self.assertEqual(patched_source(input_85), original_source(input_85))
            


    def test86(self):
        input_86 = "4 4 4 4 4 4"
        self.assertEqual(patched_source(input_86), original_source(input_86))
            


    def test87(self):
        input_87 = "2 2 2 2 2 2 2 2 2 2"
        self.assertEqual(patched_source(input_87), original_source(input_87))
            


    def test88(self):
        input_88 = "10 10 10 10 10"
        self.assertEqual(patched_source(input_88), original_source(input_88))
            


    def test89(self):
        input_89 = "10 10 10 10 10 5 5 5 5 5 5 5 5 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4 4 4 4 4 4 4 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 20"
        self.assertEqual(patched_source(input_89), original_source(input_89))
            


if __name__ == '__main__':
    unittest.main()  
    
    