import flet as ft

PIZZAS = [
    {"id": "P01", "nome": "Muçarela", "m": 30, "g": 40, "ingredientes": "mussarela, tomate e orégano"},
    {"id": "P02", "nome": "Calabresa", "m": 32, "g": 42, "ingredientes": "calabresa, cebola e mussarela"},
    {"id": "P03", "nome": "Frango", "m": 32, "g": 42, "ingredientes": "frango com borda recheada"},
    {"id": "P04", "nome": "Portuguesa", "m": 35, "g": 45, "ingredientes": "presunto, ovos, cebola e azeitona"},
]


def main(page: ft.Page):
    page.title = "PizzaDev"
    page.bgcolor = "#F5F5F5"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text(
        "PizzaDev",
        size=32,
        weight=ft.FontWeight.BOLD,
        width=300,
        text_align=ft.TextAlign.CENTER,
        color="#000000",
    )
    novo_titulo = ft.Text(
        "Bem-vindo ao PizzaDev",
        size=28,
        weight=ft.FontWeight.W_100,
        color="#000000",
    )
    slogan = ft.Text(
        "O melhor lugar para aprender programação.",
        size=18,
        weight=ft.FontWeight.NORMAL,
        color="#000000",
    )
    orientacao = ft.Text(
        "Área de gerenciamento de pedidos",
        size=14,
        weight=ft.FontWeight.NORMAL,
        color="#000000",
    )
    identificacao_dupla = ft.Text(
        "Dupla responsável: Stefany e João",
        size=12,
        weight=ft.FontWeight.NORMAL,
        text_align=ft.TextAlign.LEFT,
        color="#000000",
    )

    pedido = {"pizza": None}
    mensagem = ft.Text("Nenhuma pizza selecionada", color="#000000")
    quantidade = ft.TextField(label="Quantidade", value="1")
    tamanho = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="M", label="M"),
            ft.Radio(value="G", label="G"),
        ]),
        value="M",
    )
    resultado = ft.Text("")

    def escolher(pizza):
        pedido["pizza"] = pizza
        mensagem.value = f"Selecionada: {pizza['nome']}"
        mensagem.color = "#280458"
        resultado.value = f"Preço: M R$ {pizza['m']} | G R$ {pizza['g']}"
        page.update()

    def calcular(e):
        pizza = pedido["pizza"]
        if pizza is None:
            resultado.value = "Selecione uma pizza primeiro."
            page.update()
            return

        if not quantidade.value or not quantidade.value.isdigit():
            resultado.value = "Digite uma quantidade inteira."
            page.update()
            return

        qtd = int(quantidade.value)

        if qtd < 1 or qtd > 10:
            resultado.value = "Quantidade deve ficar entre 1 e 10."
            page.update()
            return

        tipo = tamanho.value if tamanho.value else "M"
        preco = pizza["m"] if tipo == "M" else pizza["g"]
        resultado.value = f"Parcial: {qtd}x {pizza['nome']} ({tipo}) = R$ {preco * qtd:.2f}"
        page.update()

#Parte responsável por gerar os cards, removendo a duplicação para criação dos espaços com sabores de pizza.
    cards = []
    for pizza in PIZZAS:
        card = ft.Container(
            padding=15,
            border_radius=12,
            bgcolor="#FFFFFF",
            on_click=lambda e, p=pizza: escolher(p),
            content=ft.Column([
                ft.Text(pizza["nome"], size=20, weight=ft.FontWeight.BOLD, color="#000000"),
                ft.Text(pizza["ingredientes"], color="#000000"),
                ft.Row([
                    ft.Text(f"M: R$ {pizza['m']}", color="#000000"),
                    ft.Text(f"G: R$ {pizza['g']}", color="#000000"),
                ]),
            ]),
        )
        cards.append(card)

    linha_de_cards = ft.Row(
        controls=cards,
        wrap=True,
        spacing=20,
        run_spacing=20,
    )

    botoes_pedido = ft.Column(
        controls=[
            quantidade,
            ft.Text("Tamanho da pizza:"),
            tamanho,
            mensagem,
            resultado,
        ],
        spacing=10,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    page.add(
        titulo,
        novo_titulo,
        slogan,
        orientacao,
        identificacao_dupla,
        linha_de_cards,
        ft.ElevatedButton("Fazer pedido", on_click=calcular, color="#000000"),
        botoes_pedido,
    )


ft.run(main)

#O layout não precisou ser duplicado, pois sua criação já é realizada pela unica função criar_cards(), que gera os cards das pizzas nos containers(espaços)
