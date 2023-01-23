# ingridientes cliente
ing_pedidos = []
continuar = 'sim'

while continuar.lower() == 'sim':
    ig = input('Digite o ingrediente de sua escola: ')
    ing_pedidos.append(ig.lower())
    continuar = input('Deseja continuar?\nSim ou Não\n')

    # ingredientes da pizzaria
    ingrediente = ['mostarda', 'pimentão', 'mussarela', 'tomate']
    for i in ing_pedidos:
        if i in ingrediente:
            print("Adicionando "+ i + " a sua pizza.")
            print("\nSua pizza está pronta")
        else:
                print("Sinto muito, não temos o "+ i + ".")