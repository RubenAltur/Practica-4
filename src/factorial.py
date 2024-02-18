"""
modul per a calcular el factorial d'un numero """
def factorial(num):

    """ parametres d'entrada: numero del que es vol saber el factorial
        parametres d'eixida: factorial del numero
        aquesta funcio retorna el factorial del numero que se li passa a la funció 
    """
    if isinstance(num,int):
        if num>0:
            if num==1:
                return 1
            resultat = 1
            for i in range(2, num + 1):
                resultat *= i
            return resultat
        raise ValueError("No poden introduir numeros negatius")
    raise TypeError("Sols es poden introduir numeros")
