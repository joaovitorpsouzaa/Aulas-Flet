import flet as ft


def main(page: ft.Page):
    page.title = "PizzaDev"
    page.bgcolor = "#FBFBFBFF"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text(
        "PizzaDev",
        size=32,
        weight=ft.FontWeight.BOLD,
        width=300,
        text_align=ft.TextAlign.CENTER,
        color=ft.Colors.BLACK,
    )
    novo_titulo = ft.Text(
        "Bem-vindo ao PizzaDev",
        size=28,
        weight=ft.FontWeight.W_100,
        color=ft.Colors.BLACK,
    )
    slogan = ft.Text(
        "O melhor lugar para aprender programação.",
        size=18,
        weight=ft.FontWeight.NORMAL,
        color=ft.Colors.BLACK,
    )
    didatica = ft.Text(
        "Versão didatica",
        size=14,
        weight=ft.FontWeight.NORMAL,
        color=ft.Colors.BLACK,
    )
    orientacao = ft.Text(
        "Área de gerenciamento de pedidos",
        size=14,
        weight=ft.FontWeight.NORMAL,
        color=ft.Colors.BLACK,
    )
    identificacao_dupla = ft.Text(
        "Dupla responsável: Stefany e João",
        size=12,
        weight=ft.FontWeight.NORMAL,
        text_align=ft.TextAlign.LEFT,
        color=ft.Colors.BLACK,
    )

    card1 = ft.Container(
        padding=15,
        border_radius=12,
        bgcolor=ft.Colors.WHITE,
        content=ft.Column([
            ft.Text("Calabresa", size=20, weight=ft.FontWeight.BOLD),
            ft.Text("calabresa, cebola e mussarela"),
            ft.Row([
                ft.Text("M: R$ 32"),
                ft.Text("G: R$ 42"),
            ]),
        ]),
    )

    card2 = ft.Container(
        padding=15,
        border_radius=12,
        bgcolor=ft.Colors.WHITE,
        content=ft.Column([
            ft.Text("Mussarela", size=20, weight=ft.FontWeight.BOLD),
            ft.Text("mussarela, tomate e orégano"),
            ft.Row([
                ft.Text("M: R$ 30"),
                ft.Text("G: R$ 38"),
            ]),
        ]),
    )

    card3 = ft.Container(
        padding=15,
        border_radius=12,
        bgcolor=ft.Colors.WHITE,
        content=ft.Column([
            ft.Text("Frango", size=20, weight=ft.FontWeight.BOLD),
            ft.Text("pizza de frango com borda recheada"),
            ft.Row([
                ft.Text("M: R$ 32"),
                ft.Text("G: R$ 42"),
            ]),
        ]),
    )

    card4 = ft.Container(
        padding=15,
        border_radius=12,
        bgcolor=ft.Colors.WHITE,
        content=ft.Column([
            ft.Text("Portuguesa", size=20, weight=ft.FontWeight.BOLD),
            ft.Text("presunto, ovos, cebola e azeitona"),
            ft.Row([
                ft.Text("M: R$ 35"),
                ft.Text("G: R$ 45"),
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

    def escolher_calabresa(e):
        mensagem.value = "Selecionada: Calabresa"
        page.update()

    page.add(
    ft.Button("Escolher Calabresa", on_click=escolher_calabresa),
    mensagem
)



    page.add(titulo, novo_titulo, slogan, didatica, orientacao, identificacao_dupla, linha_de_cards)


ft.app(target=main)


