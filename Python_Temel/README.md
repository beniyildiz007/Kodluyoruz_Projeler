# Kodluyoruz_Flatten
Bir listeyi düzleştiren (flatten) fonksiyon yazın.
Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi,
non-scalar verilerden de oluşabilir. Örnek olarak:
input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output: [1,'a','cat',2,3,'dog',4,5]

```python
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
```
# Kodluyoruz_Reverse-List
Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın.
Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün.
Örnek olarak:
input: [[1, 2], [3, 4], [5, 6, 7]]
output: [[[7, 6, 5], [4, 3], [2, 1]]
```python
def reverse(x):
    for i in range(int(len(x)/2)):
        temp = x[i]
        x[i] = x[len(x)-(i+1)]
        x[len(x)-(i+1)] = temp        
    counter = 0
    for i in x:
        if isinstance(i,list):             
            for a in range(int(len(i)/2)):
                temp = x[counter][a]
                x[counter][a] = x[counter][len(i)-(a+1)]
                x[counter][len(i)-(a+1)] = temp
                counter +=1
    print(x)
x = [[1, 2], [3, 4], [5, 6, 7]] # given input 
reverse(x)
```
