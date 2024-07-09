from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class FoodTracking(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10

        self.add_widget(Label(text='Alimento/Bebida:'))
        self.food_input = TextInput(multiline=False)
        self.food_input.disabled = True
        self.add_widget(self.food_input)

        self.add_widget(Label(text='Cantidad:'))
        self.amount_input = TextInput(input_filter='float', multiline=False)
        self.amount_input.disabled = True
        self.add_widget(self.amount_input)

        self.add_widget(Label(text='Hora:'))
        self.time_input = TextInput(multiline=False)
        self.time_input.disabled = True
        self.add_widget(self.time_input)

        self.track_button = Button(text='Registrar')
        self.track_button.bind(on_press=self.track)
        self.add_widget(self.track_button)

        self.modify_button = Button(text='Modificar')
        self.modify_button.bind(on_press=self.enable_inputs)
        self.add_widget(self.modify_button)

        self.new_button = Button(text='Nuevo')
        self.new_button.bind(on_press=self.reset_inputs)
        self.add_widget(self.new_button)

        self.result_label = Label(text='')
        self.add_widget(self.result_label)

    def track(self, instance):
        food = self.food_input.text
        amount = self.amount_input.text
        time = self.time_input.text

        if food and amount and time:
            self.result_label.text += f'{time}: {food} - {amount}\n'
            self.food_input.text = ''
            self.amount_input.text = ''
            self.time_input.text = ''
        else:
            self.result_label.text = 'Por favor, complete todos los campos.'

    def enable_inputs(self, instance):
        self.food_input.disabled = False
        self.amount_input.disabled = False
        self.time_input.disabled = False

    def reset_inputs(self, instance):
        self.food_input.text = ''
        self.amount_input.text = ''
        self.time_input.text = ''
        self.result_label.text = ''
        self.food_input.disabled = True
        self.amount_input.disabled = True
        self.time_input.disabled = True

class FoodTrackingApp(App):
    def build(self):
        return FoodTracking()

if __name__ == '__main__':
    FoodTrackingApp().run()
