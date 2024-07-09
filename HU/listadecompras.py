from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class ShoppingList(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10

        self.generate_button = Button(text='Generar Lista de Compras')
        self.generate_button.bind(on_press=self.generate_list)
        self.add_widget(self.generate_button)

        self.new_button = Button(text='Nuevo')
        self.new_button.bind(on_press=self.reset_list)
        self.add_widget(self.new_button)

        self.result_label = Label(text='')
        self.add_widget(self.result_label)

    def generate_list(self, instance):
        shopping_items = ["Frutas", "Verduras", "Proteínas", "Granos"]
        self.result_label.text = 'Lista de Compras:\n' + '\n'.join(shopping_items)

    def reset_list(self, instance):
        self.result_label.text = ''

class ShoppingListApp(App):
    def build(self):
        return ShoppingList()

if __name__ == '__main__':
    ShoppingListApp().run()
