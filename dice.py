#dice.py
import random

def dice():
    a = random.randrange(1,7)
    b = random.randrange(1,7)
    if a > b:
        return "1번 승리!", 0xFF0000, str(a), str(b)
    elif a == b:
        return "무승부", 0xFAFA00, str(a), str(b)
    elif a < b:
        return "2번 승리!", 0x00ff56, str(a), str(b)