import flet as ft


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
    didatica = ft.Text(
        "Versão didatica",
        size=14,
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
#Adição da funcionaliade lambda, que torna a parte do código clicavel e volatil.
    card1 = ft.Container(
        padding=15,
        border_radius=12,
        bgcolor="#FFFFFF",
        on_click=lambda e: escolher("Calabresa"),
        content=ft.Column([
            ft.Text("Calabresa", size=20, weight=ft.FontWeight.BOLD, color="#000000"),
            ft.Text("calabresa, cebola e mussarela", color="#000000"),
            ft.Row([
                ft.Text("M: R$ 32", color="#000000"),
                ft.Text("G: R$ 42", color="#000000"),
            ]),
        ]),
    )

    card2 = ft.Container(
        padding=15,
        border_radius=12,
        bgcolor="#FFFFFF",
        on_click=lambda e: escolher("Muçarela"),
        content=ft.Column([
            ft.Text("Mussarela", size=20, weight=ft.FontWeight.BOLD, color="#000000"),
            ft.Text("mussarela, tomate e orégano", color="#000000"),
            ft.Row([
                ft.Text("M: R$ 30", color="#000000"),
                ft.Text("G: R$ 38", color="#000000"),
            ]),
        ]),
    )

    card3 = ft.Container(
        padding=15,
        border_radius=12,
        bgcolor="#FFFFFF",
        on_click=lambda e: escolher("Frango"),
        content=ft.Column([
            ft.Text("Frango", size=20, weight=ft.FontWeight.BOLD, color="#000000"),
            ft.Text("pizza de frango com borda recheada", color="#000000"),
            ft.Row([
                ft.Text("M: R$ 32", color="#000000"),
                ft.Text("G: R$ 42", color="#000000"),
            ]),
        ]),
    )

    card4 = ft.Container(
        padding=15,
        border_radius=12,
        bgcolor="#FFFFFF",
        on_click=lambda e: escolher("Portuguesa"),
        content=ft.Column([
            ft.Text("Portuguesa", size=20, weight=ft.FontWeight.BOLD, color="#000000"),
            ft.Text("presunto, ovos, cebola e azeitona", color="#000000"),
            ft.Row([
                ft.Text("M: R$ 35", color="#000000"),
                ft.Text("G: R$ 45", color="#000000"),
            ]),
        ]),
    )

    linha_de_cards = ft.Row(
        controls=[card1, card2, card3, card4],
        wrap=True,
        spacing=20,
        run_spacing=20,
    )

    mensagem = ft.Text("Nenhuma pizza selecionada")
#Função para escolher o sabor da pizza
    def escolher(sabor):
        mensagem.value = "Selecionada: {sabor}"
        mensagem.color = "#280458"
        page.update()

#Função para calcular o preço do pedidos
    def calcular(e):
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
        preco = 32 if tipo == "M" else 42
        resultado.value = f"Parcial: R$ {preco * qtd:.2f}"
        page.update()
        return

    
    quantidade = ft.TextField(label="Quantidade", value="1")
    tamanho = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="M", label="M"),
            ft.Radio(value="G", label="G"),
        ]),
        value="M"
    )
    resultado = ft.Text("")

    botoes_pedido = ft.Column(
        controls=[
            quantidade,
            ft.Text("Tamanho da pizza:"),
            tamanho,
            resultado,
        ],
        spacing=10,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    page.add(
        titulo,
        novo_titulo,
        slogan,
        didatica,
        orientacao,
        identificacao_dupla,
        ft.Text("Tamanho"),
        linha_de_cards,
        ft.ElevatedButton("Fazer pedido", on_click=calcular, color="#000000"),
        botoes_pedido,
    )


ft.run(main)

#Finalização do código que permite o calculo de valores de tamanhos M e G de pizza, e seus valores.

