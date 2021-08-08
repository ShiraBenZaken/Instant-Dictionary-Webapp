import justpy as jp
from webapp import layout
from webapp import page


class Home(page.Page):
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)

        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen p-2")
        jp.Div(a=div, text="This is the Home page!", classes="text-4xl m-2")
        jp.Div(a=div, text="""
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
            In rutrum erat faucibus tellus tincidunt, at tristique arcu elementum.
            Morbi tempor sagittis suscipit.
            Nunc dictum aliquet purus, sit amet tincidunt dui consectetur placerat.
        """, classes="text-lg")

        return wp


