

#exo 1-2
def square(x):
    return x*x

def product(a,b):
    return a*b

def division(a,b):
    return a/b

def calcul(a,b):
    return product(square(a),square(b)), division(square(a),square(b))

def main():

    x = eval(input("Entrer un nombre: "))
    calcul_a = square(x)
    print("Le carré du x est: ", calcul_a )

    a = eval(input("Entrer le premier nombre: "))
    b = eval(input("Entrer le deuxième nombre: "))
    produit_b, division_b = calcul (a,b)

    print("Le produit est: ", produit_b )
    print("La division est: ", division_b )


main()


#exo 3-4

def cube(x):
    return x*x*x

def product(a,b):
    return a*b

def division(a,b):
    return a/b

def calcul(a,b):
    return product(cube(a),cube(b)), division(cube(a),cube(b))

def main():

    x = eval(input("Entrer un nombre: "))
    calcul_a = cube(x)
    print("Le cube du x est: ", calcul_a )

    a = eval(input("Entrer le premier nombre: "))
    b = eval(input("Entrer le deuxième nombre: "))
    produit_b, division_b = calcul (a,b)

    print("Le produit est: ", produit_b )
    print("La division est: ", division_b )


main()


#exo 5

def rec_somme(n):
    if n == 1:
        return 1
    elif:
        n== 0
        return 0
    else:
        return n+rec_somme(n-2)

def main():
    n = eval(input("Entrer un nombre: "))
    res = rec_somme(n)

    print ("La somme est: ", res)
main()

#exo 6

def multiplication(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            res+= i*j
    return res

def main():
    list1 = [1,2,3,4,5]
    list2 = [5,12,45,56,55,0]
    res = multiplication(list1, list2)

    print ("La produit de deux listes est: ", res)
main()

#exo 7
def main():
    print("La table de 8  est : ", [x*8 for x in range(1,11)])

main()
