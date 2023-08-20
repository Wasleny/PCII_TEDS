def obtem_mes(num_mes):
    if(num_mes < 0 or num_mes > 11):
        return (f"{num_mes} é inválido")

    meses = [
        "janeiro",
        "fevereiro",
        "março",
        "abril",
        "maio",
        "junho",
        "julho",
        "agosto",
        "setembro",
        "outubro",
        "novembro",
        "dezembro"
    ]

    return meses[num_mes]

#testes
print(f"Mês: {obtem_mes(1)}")
print(obtem_mes(15))