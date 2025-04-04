import flet as ft

def main(page: ft.Page):
    page.title = "Anamur Kent Konseyi Gençlik Meclisi"
    page.bgcolor = "#FFFFFF"  # Sayfa arka planını beyaz yaptık
    page.padding = 0

    # Sabit başlık (her zaman üstte kalır) ve başlık kısmının arka planını mavi yapma
    header = ft.Container(
        content=ft.Row(
            [
                ft.Text("Anamur Kent Konseyi Gençlik Meclisi", size=32, weight="bold", color="white")
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,  # Başlık yatayda ortalandı
            spacing=15
        ),
        bgcolor="#1E90FF",  # Başlık kısmının arka planını mavi yaptık
        padding=20
    )

    # Dinamik içerik alanı
    content_container = ft.Container(expand=True, padding=30)

    # Menü başlıkları ve içerikleri (dinamik)
    menu_items = [
        {
            "title": "Ana Sayfa",
            "content": lambda: ft.Column([
                ft.Text("Ana Sayfa", size=22, weight="bold", color="black"),
                ft.Text("Gençlik Meclisi'ne hoş geldiniz. Burada güncel haberler ve etkinlikler bulunur.", color="black")
            ], spacing=10)
        },
        {
            "title": "Haberler",
            "content": lambda: ft.Column([
                ft.Text("Haberler", size=22, weight="bold", color="black"),
                ft.Text("Son dakika gelişmeleri ve meclis duyuruları burada yayınlanır.", color="black")
            ], spacing=10)
        },
        {
            "title": "Etkinlikler",
            "content": lambda: ft.Column([
                ft.Text("Etkinlikler", size=22, weight="bold", color="black"),
                ft.Text("Geçmiş ve gelecek tüm etkinlik detaylarını burada bulabilirsiniz.", color="black")
            ], spacing=10)
        },
        {
            "title": "İletişim",
            "content": lambda: ft.Column([
                ft.Text("İletişim", size=22, weight="bold", color="black"),
                ft.Text("Bize ulaşmak için aşağıdaki formu kullanabilirsiniz.", color="black"),
                ft.TextField(label="Adınız", color="black"),
                ft.TextField(label="Email", color="black"),
                ft.TextField(label="Mesaj", multiline=True, color="black"),
                ft.ElevatedButton("Gönder", bgcolor="linear-gradient(to right, #1E90FF, #00BFFF)", color="white")
            ], spacing=10)
        }
    ]

    selected_index = ft.Ref[int]()
    menu_column = ft.Column()

    # Menü oluşturma
    def build_menu():
        items = []
        for i, item in enumerate(menu_items):
            is_selected = selected_index.value == i
            text = ft.Text(
                item["title"],
                size=18,
                weight="bold" if is_selected else "normal",
                color="#1E90FF" if is_selected else "black"
            )

            gesture = ft.GestureDetector(
                content=text,
                on_tap=lambda e, index=i: navigate(index),
                on_hover=lambda e: setattr(text, "color", "#1E90FF" if e.data == "true" else "black")
            )

            items.append(gesture)

            if i < len(menu_items) - 1:
                items.append(ft.Divider(height=1, color="#DDDDDD"))

        return items

    # Sayfa değiştirme
    def navigate(index):
        selected_index.value = index
        content_container.content = menu_items[index]["content"]()
        rebuild_menu()
        page.update()

    def rebuild_menu():
        menu_column.controls = build_menu()

    # Başlangıçta ilk içerik
    selected_index.value = 0
    content_container.content = menu_items[0]["content"]()
    rebuild_menu()

    # Sol menü alanı
    sidebar = ft.Container(
        content=menu_column,
        bgcolor="white",
        width=220,
        padding=20,
        border=ft.border.only(right=ft.BorderSide(1, "#E0E0E0"))
    )

    # Ana sayfa düzeni
    page.add(
        header,
        ft.Row(
            controls=[
                sidebar,
                content_container
            ],
            expand=True
        )
    )

# Uygulama başlat
ft.app(target=main, view=ft.WEB_BROWSER)