import sys
sys.path.append('../')

from controls.tda.linked.linkedList import Linked_List
from controls.facturaDaoControl import FacturaDaoControl
from controls.retencionDaoControl import RetencionDaoControl
import random
import time

listaNumber = Linked_List()
listaString = Linked_List()

list10000numbres = []
for i in range(0,10000):
    list10000numbres.append(randint(0,10000))
    
    inicio = time()
    listquick = quicksort.sort(list10000numbres)
    print("---------------------------------------------")
    print("QuickSort with 10000 numbers: ", time()-inicio)
    inicio = time()
    listshell = shell.sort_descendent(list10000numbres)
    print("ShellSort with 10000 numbers: ", time()-inicio)
    inicio = time() 
    listamerge = merge.sort_descendent(list10000numbres)
    print("MergeSort with 10000 numbers: ", time()-inicio)
    
    list20000numbres = []
    for i in range(0,20000):
        list20000numbres.append(randint(0,20000))

    inicio = time()
    listquick = quick.sort_acendent(list20000numbres)
    print("---------------------------------------------")
    print("QuickSort with 20000 numbers: ", time()-inicio)
    inicio = time()
    listshell = shell.sort_descendent(list20000numbres)
    print("ShellSort with 20000 numbers: ", time()-inicio)
    inicio = time() 
    listamerge = merge.sort_descendent(list20000numbres)
    print("MergeSort with 20000 numbers: ", time()-inicio)

    
 