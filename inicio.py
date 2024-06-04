from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class TestApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Hello, Kivy!"))
        layout.add_widget(Button(text='Começar'))
        return layout

if __name__ == "__main__":
    TestApp().run()