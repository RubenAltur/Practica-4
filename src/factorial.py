
def factorial(num):
    if isinstance(num,int):
        if num>0:
            if num==1 or num==0:
                return 1
            else:
                resultat = 1
                for i in range(2, num + 1):
                    resultat *= i
    
                return resultat
        else:
            raise ValueError("No poden introduir numeros negatius")
    else: 
        raise TypeError("Sols es poden introduir numeros")