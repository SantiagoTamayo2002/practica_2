import sys
sys.path.append('../')

from random import randint
from time import time
from controls.tda.linked.ordenar.quickSort import QuickSort
from controls.tda.linked.ordenar.shellSort import ShellSort
from controls.tda.linked.ordenar.mergeSort import MergeSort

quicksort = QuickSort()
shell = ShellSort()
merge = MergeSort()

list10000numbres = []
for i in range(0,10000):
    list10000numbres.append(randint(0,10000))

inicio = time()
listquick = quicksort.sort_primitive_ascendent(list10000numbres)
print("---------------------------------------------")
print("QuickSort with 10000 numbers: ", time()-inicio)
inicio = time()
listshell = shell.sort_primitive_ascendent(list10000numbres)
print("ShellSort with 10000 numbers: ", time()-inicio)
inicio = time() 
listamerge = merge.sort_primitive_descendent(list10000numbres)
print("MergeSort with 10000 numbers: ", time()-inicio)

list20000numbres = []
for i in range(0,20000):
    list20000numbres.append(randint(0,20000))
inicio = time()
listquick = quicksort.sort_primitive_descendent(list20000numbres)
print("---------------------------------------------")
print("QuickSort with 20000 numbers: ", time()-inicio)
inicio = time()
listshell = shell.sort_primitive_descendent(list20000numbres)
print("ShellSort with 20000 numbers: ", time()-inicio)
inicio = time() 
listamerge = merge.sort_primitive_descendent(list20000numbres)
print("MergeSort with 20000 numbers: ", time()-inicio)