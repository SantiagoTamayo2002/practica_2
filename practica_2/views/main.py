import sys
sys.path.append('../')

from controls.tda.linked.linkedList import Linked_List
from controls.facturaDaoControl import FacturaDaoControl
from controls.retencionDaoControl import RetencionDaoControl
import random
import time

listaNumber = Linked_List()
listaString = Linked_List()
try:
    fact = FacturaDaoControl()
    ret = RetencionDaoControl()
    for i in range(10000):
        listaNumber.add(random.randint(0,100000))
    #
    inicio = time.time()
    listaNumber.sort(1,0)
    fin = time.time()
    print("Tiempo de ejecucion: ", fin-inicio)

    listaString.add("Juan Perez")
    listaString.add("William Chamba")
    listaString.add("Andres Pardo")
    listaString.add("Rafael Chuquihuanca")
    listaString.add("David Jimenez")
    listaString.add("Carlos Andrade")
    listaString.add("Brandon Gutierrez")
    listaString.add("Estefania Cale")
    listaString.add("Ximena Yanayaco")
    listaString.add("Ximena Yanayaco")
    
    listaAuxx = listaString.binary_search_secuencial("Ximena Yanayaco", 1)
    listaString.sort(1)
    listaAux = fact._list().sort_models('_monto', 1, 0) 
except Exception as e:
    print(f"Error: {e}")