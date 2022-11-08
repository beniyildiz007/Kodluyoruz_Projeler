"""
Bir listeyi düzleştiren (flatten) fonksiyon yazın.
Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi,
non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]
"""


def flatten(n):
    for i in n :
        if isinstance(i,list):
            flatten(i)
        else:
            l1.append(i)
l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
l1 = []
flatten(l)
print(l1)
