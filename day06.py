test ="""Time:      7  15   30
Distance:  9  40  200"""

data="""Time:        53     89     76     98
Distance:   313   1090   1214   1201"""

from devtools import debug
from functools import reduce
import operator as op
from time import perf_counter
import sys
import math


def read(data:str) -> list[tuple[int, int]]:
    (time, dist), tru = data.split("\n"), lambda x: bool(x)
    return zip(
        list(map(int, filter(tru, time.split(":")[1].split(" ")))),
        list(map(int, filter(tru, dist.split(":")[1].split(" "))))
    )
    
def calc1(total_time: int, total_dist: int) -> int:
    def inner(btn_time: int=1):
        if btn_time > total_time:
            return []
        new_dist = btn_time * (total_time - btn_time)
        return inner(btn_time + 1) + ([new_dist] if new_dist > total_dist else [])
    return len(inner(total_time//2)) * 2 - (1 if total_time % 2 == 0 else 2)

def calc2(total_time: int, total_dist: int) -> int:
    end_time, start_time = total_time, total_time // 2
    while abs(start_time - end_time) > 0.05 :
        hop = (start_time + end_time) / 2
        if hop * (total_time - hop) <= total_dist:
            end_time = hop
        else:
            start_time = hop
    return (int(end_time) - (total_time // 2) + 1) * 2 - (1 if total_time % 2 == 0 else 2)
    

def part1(data) -> int:
    return reduce(op.mul, (calc1(*d) for d in read(data)))
    
def part2(data: str) -> int:
    # yea why simple :D don't do this at work
    return calc2(*tuple(map(int, ("".join(str(it) for it in list(zip(*read(data)))[i]) for i in range(2)))))
    
   
s = perf_counter()    
print(
    "Part 1:",
    part1(test),
    f" in {((perf_counter()-s)*1000):.2f}ms"
)
s = perf_counter()
print(
    "Part 2: ",
    part2(data),
    f" in {((perf_counter()-s)*1000):.2f}ms"
)

#and yes i know there's an analitic solution for it ;) 