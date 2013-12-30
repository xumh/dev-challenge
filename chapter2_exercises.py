# Exercises for chapter 2:
# 2.1
01 #1
010 #8
0100 #64
01000 #512
# 2.2
print 5
x = 5
print x + 1
# 2.3
width = 17
height = 12.0
delimiter = "."
# 2.3.1: 8
print width/2.0
# 2.3.2: 8.5
print height/3
# 2.3.3: 4.0
print 1+2*5
# 2.3.4: 11
print delimiter *5
# 2.3.5: .....
# 2.4.1: 523.60
import math
print 4/3 * math.pi * 5**3
# 2.4.2: 945.45
print 59*0.75+3+24.95*0.6*60
# 2.4.3: 7:30
start = (6*60+52)*60
easy = (8*60+15)*2
fast = (7*60+12)*3
finish_hour = (start + easy + fast)/(60*60.0)
finish_floored = (start + easy + fast)/(60*60)
finish_minute  = (finish_hour - finish_floored)*60
print finish_floored,":",finish_minute