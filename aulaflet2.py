import flet as ft

# Lista de pizzas do seu projeto
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

    # 1. Memória da execução (Estado compartilhado)
    estado = {"pizza": None, "tamanho": "M", "quantidade": 1}

    # 2. Container principal onde as telas serão trocadas
    area = ft.Container(expand=True)

    # --- TELA 1: INÍCIO ---
    def mostrar_inicio():
        area.content = ft.Column(
            controls=[
                ft.Text("PizzaDev", size=32, weight=ft.FontWeight.BOLD, color="#000000"),
                ft.Text("Bem-vindo ao PizzaDev", size=20, color="#000000"),
                ft.Text("Dupla responsável: Stefany e João", size=12, color="#000000"),
                ft.ElevatedButton("Abrir Cardápio", on_click=lambda e: mostrar_cardapio())
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        )
        area.update()

    # --- TELA 2: CARDÁPIO ---
    def mostrar_cardapio():
        cards = []
        for pizza in PIZZAS:
            card = ft.Container(
                padding=15,
                border_radius=12,
                bgcolor="#FFFFFF",
                on_click=lambda e, p=pizza: selecionar_pizza(p),
                content=ft.Column([
                    ft.Text(pizza["nome"], size=20, weight=ft.FontWeight.BOLD, color="#000000"),
                    ft.Text(pizza["ingredientes"], color="#000000"),
                    ft.Row([
                        ft.Text(f"M: R$ {pizza['m']}", color="#000000"),
                        ft.Text(f"G: R$ {pizza['g']}", color="#000000"),
                    ]),
                ])
            )
            cards.append(card)

        area.content = ft.Column(
            controls=[
                ft.Text("Nosso Cardápio", size=26, weight=ft.FontWeight.BOLD, color="#000000"),
                ft.Row(controls=cards, wrap=True, spacing=15, run_spacing=15),
                ft.ElevatedButton("Voltar para Início", on_click=lambda e: mostrar_inicio())
            ],
            spacing=15,
            scroll=ft.ScrollMode.AUTO
        )
        area.update()

    def selecionar_pizza(pizza):
        estado["pizza"] = pizza
        mostrar_selecao()

    # --- TELA 3: SELEÇÃO ---
    def mostrar_selecao():
        pizza = estado["pizza"]
        if not pizza:
            mostrar_cardapio()
            return

        quantidade_input = ft.TextField(label="Quantidade", value=str(estado["quantidade"]), width=150)
        tamanho_radio = ft.RadioGroup(
            content=ft.Row([
                ft.Radio(value="M", label="M"),
                ft.Radio(value="G", label="G"),
            ]),
            value=estado["tamanho"]
        )

        def avancar_carrinho(e):
            if quantidade_input.value.isdigit() and int(quantidade_input.value) > 0:
                estado["quantidade"] = int(quantidade_input.value)
                estado["tamanho"] = tamanho_radio.value
                mostrar_carrinho()

        area.content = ft.Column(
            controls=[
                ft.Text(f"Opções para: {pizza['nome']}", size=24, weight=ft.FontWeight.BOLD, color="#000000"),
                ft.Text("Tamanho da pizza:"),
                tamanho_radio,
                quantidade_input,
                ft.Row([
                    ft.ElevatedButton("Voltar ao Cardápio", on_click=lambda e: mostrar_cardapio()),
                    ft.ElevatedButton("Ver Carrinho", on_click=avancar_carrinho),
                ], spacing=10)
            ],
            spacing=15
        )
        area.update()

    # --- TELA 4: CARRINHO ---
    def mostrar_carrinho():
        pizza = estado["pizza"]
        if not pizza:
            area.content = ft.Column([
                ft.Text("Seu carrinho está vazio!", size=22, color="#000000"),
                ft.ElevatedButton("Ir para o Cardápio", on_click=lambda e: mostrar_cardapio())
            ])
        else:
            qtd = estado["quantidade"]
            tam = estado["tamanho"]
            preco_unitario = pizza["m"] if tam == "M" else pizza["g"]
            total = preco_unitario * qtd

            area.content = ft.Column([
                ft.Text("Seu Carrinho", size=26, weight=ft.FontWeight.BOLD, color="#000000"),
                ft.Text(f"Pizza: {pizza['nome']} ({tam})"),
                ft.Text(f"Quantidade: {qtd}"),
                ft.Text(f"Total: R$ {total:.2f}", size=18, weight=ft.FontWeight.BOLD, color="#280458"),
                ft.Row([
                    ft.ElevatedButton("Voltar para Seleção", on_click=lambda e: mostrar_selecao()),
                    ft.ElevatedButton("Voltar ao Cardápio", on_click=lambda e: mostrar_cardapio())
                ], spacing=10)
            ], spacing=15)
        
        area.update()

    # Adiciona a área principal e exibe a primeira tela
    page.add(area)
    mostrar_inicio()

ft.run(main)

#O layout não precisou ser duplicado, pois sua criação já é realizada pela unica função criar_cards(), que gera os cards das pizzas nos containers(espaços)
