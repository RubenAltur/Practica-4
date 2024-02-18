"""
modul per a calcular el factorial d'un numero """
def factorial(num):

    """ parametres d'entrada: numero del que es vol saber el factorial
        parametres d'eixida: factorial del numero
        aquesta funcio retorna el factorial del numero que se li passa a la funció 
    """
    if not isinstance(num,int):
        raise TypeError("Sols es poden introduir numeros")
    if num<0:
        raise ValueError("No poden introduir numeros negatius")
    if num==1:
        return 1
    resultat = 1
    for i in range(2, num + 1):
            resultat *= i
    return resultat
