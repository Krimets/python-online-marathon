import re

def figure_perimetr(test):
    c = re.findall(r'#[A-z]{2}([0-9]):([0-9])', test)
    lb1, lb2 = int(c[0][0]), int(c[0][1])
    rb1, rb2 = int(c[1][0]), int(c[1][1])
    lt1, lt2 = int(c[2][0]), int(c[2][1])
    rt1, rt2 = int(c[3][0]), int(c[3][1])

    a = ((rb1 - lb1) ** 2 + (rb2 - lb2) ** 2) ** 0.5
    b = ((lb1 - lt1) ** 2 + (lb2 - lt2) ** 2) ** 0.5
    c = ((rb1 - rt1) ** 2 + (rt2 - rb2) ** 2) ** 0.5
    d = ((rt1 - lt1) ** 2 + (rt2 - lt2) ** 2) ** 0.5
    return a + b + c + d

test1 = "#LB1:1#RB4:1#LT1:3#RT4:3"
print(figure_perimetr(test1))

test2 = "#LB0:1#RB5:1#LT4:5#RT8:3"
print(figure_perimetr(test2))
