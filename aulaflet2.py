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

    card1 = ft.Container(
        padding=15,
        border_radius=12,
        bgcolor="#FFFFFF",
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

    def escolher_calabresa(e):
        mensagem.value = "Selecionada: Calabresa, "
        mensagem.color="#280458"
        page.update()
     
    def escolher_muçarela(e):
            mensagem.value = "Selecionada: Mussarela"
            mensagem.color="#280458"
            page.update()
    
    def escolher_frango(e):
            mensagem.value = "Selecionada: Frango"
            mensagem.color="#280458"
            page.update() 
    
    def escolher_portuguesa(e):
            mensagem.value = "Selecionada: Portuguesa"
            mensagem.color="#280458"
            page.update()
    
    escolha = ft.Row(
        controls=[
            ft.FilledButton("Calabresa", on_click=escolher_calabresa, color="#000000"),
            ft.FilledButton("Mussarela", on_click=escolher_muçarela, color="#000000"),
            ft.FilledButton("Frango", on_click=escolher_frango, color="#000000"),
            ft.FilledButton("Portuguesa", on_click=escolher_portuguesa, color="#000000"),
            mensagem,
        ],
        spacing=10,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    page.add(titulo, novo_titulo, slogan, didatica, orientacao, identificacao_dupla, escolha, linha_de_cards)


ft.run(main)


