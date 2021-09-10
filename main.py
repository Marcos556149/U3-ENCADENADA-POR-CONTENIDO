from claseListaEncadenadaCont import ListaEncadenadaCont
if __name__=='__main__':
    unaLista=ListaEncadenadaCont()
    unaLista.insertar(60)
    unaLista.insertar(50)
    unaLista.insertar(40)
    unaLista.insertar(30)
    unaLista.recorrer()
    unaLista.suprimirCont(50)
    input()
    unaLista.recorrer()
