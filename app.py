import flet as ft

def main(page: ft.Page):
    page.title = "Gençlik Meclisi Dinamik Web Sitesi"
    page.bgcolor = "#F4F4F4"
    page.padding = 20

    # Dinamik içerik fonksiyonları
    def home_content():
        return ft.Column(
            [
                ft.Text("Ana Sayfa", size=24, weight="bold", color="#FF6F61"),
                ft.Text("Gençlik Meclisi'ne hoş geldiniz!", size=16),
                ft.Text("Burada güncel haberler, etkinlikler ve duyurular bulunacaktır.", size=14),
            ],
            spacing=10
        )

    def news_content():
        return ft.Column(
            [
                ft.Text("Haberler", size=24, weight="bold", color="#6A5ACD"),
                ft.Text("En son haberler burada listelenecek.", size=16)
            ],
            spacing=10
        )

    def events_content():
        return ft.Column(
            [
                ft.Text("Etkinlikler", size=24, weight="bold", color="#FF6F61"),
                ft.Text("Yaklaşan etkinlikler ve geçmiş etkinlikler burada gösterilecek.", size=16)
            ],
            spacing=10
        )

    def contact_content():
        return ft.Column(
            [
                ft.Text("İletişim", size=24, weight="bold", color="#6A5ACD"),
                ft.Text("Bizimle iletişime geçmek için formu doldurun.", size=16),
                ft.TextField(label="Adınız"),
                ft.TextField(label="Email"),
                ft.TextField(label="Mesajınız", multiline=True),
                ft.ElevatedButton("Gönder")
            ],
            spacing=10
        )

    # Üst kısımda sabit header (başlık)
    header = ft.Container(
        content=ft.Text("GENÇLİK MECLİSİ", size=30, weight="bold", color="white"),
        bgcolor="#FF6F61",
        padding=20,
        alignment=ft.alignment.center
    )

    # Dinamik içerik için bir container
    content_container = ft.Container()

    # Menü çubuğu (sayfalar arası geçiş)
    def navigate(e, destination):
        if destination == "home":
            content_container.content = home_content()
        elif destination == "news":
            content_container.content = news_content()
        elif destination == "events":
            content_container.content = events_content()
        elif destination == "contact":
            content_container.content = contact_content()
        page.update()

    menu = ft.Row(
        [
            ft.TextButton("Ana Sayfa", on_click=lambda e: navigate(e, "home")),
            ft.TextButton("Haberler", on_click=lambda e: navigate(e, "news")),
            ft.TextButton("Etkinlikler", on_click=lambda e: navigate(e, "events")),
            ft.TextButton("İletişim", on_click=lambda e: navigate(e, "contact")),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    # Sayfayı düzenleme: header, menü ve içerik alanı
    page.add(header, menu, ft.Divider(), content_container)

    # İlk olarak Ana Sayfa içeriğini yükle
    content_container.content = home_content()
    page.update()

# Uygulamayı tarayıcıda çalıştırmak için:
ft.app(target=main, view=ft.WEB_BROWSER)
