# 별 그리기
i = 1
s1 = '  '
s2 = '\u2605'

while i < 10 :
     if i < 6 :
          print((5-i)*s1 + (2*i -1)*s2)
     else :
          print((i-5)*s1 + (2*(10-i) -1)*s2)
     i = i + 1
