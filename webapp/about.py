import justpy as jp


class About:
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-grey-200 h-screen")
        jp.Div(a=div, text="This is About Page", classes="text-4xl m-2")
        jp.Div(a=div, text="""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
        In rutrum erat faucibus tellus tincidunt, at tristique arcu elementum.
         Morbi tempor sagittis suscipit.
          Nunc dictum aliquet purus, sit amet tincidunt dui consectetur placerat. 
        """, classes="text-lg")
        return wp




