from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class CaloricRequirementCalculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10

        self.add_widget(Label(text='Peso (kg):'))
        self.weight_input = TextInput(input_filter='float', multiline=False)
        self.weight_input.disabled = True
        self.add_widget(self.weight_input)

        self.add_widget(Label(text='Altura (cm):'))
        self.height_input = TextInput(input_filter='float', multiline=False)
        self.height_input.disabled = True
        self.add_widget(self.height_input)

        self.add_widget(Label(text='Edad:'))
        self.age_input = TextInput(input_filter='int', multiline=False)
        self.age_input.disabled = True
        self.add_widget(self.age_input)

        self.add_widget(Label(text='Nivel de Actividad (1-5):'))
        self.activity_input = TextInput(input_filter='float', multiline=False)
        self.activity_input.disabled = True
        self.add_widget(self.activity_input)

        self.calculate_button = Button(text='Calcular')
        self.calculate_button.bind(on_press=self.calculate)
        self.add_widget(self.calculate_button)

        self.modify_button = Button(text='Modificar')
        self.modify_button.bind(on_press=self.enable_inputs)
        self.add_widget(self.modify_button)

        self.new_button = Button(text='Nuevo')
        self.new_button.bind(on_press=self.reset_inputs)
        self.add_widget(self.new_button)

        self.result_label = Label(text='')
        self.add_widget(self.result_label)

    def calculate(self, instance):
        try:
            weight = float(self.weight_input.text)
            height = float(self.height_input.text)
            age = int(self.age_input.text)
            activity_level = float(self.activity_input.text)

            bmr = 10 * weight + 6.25 * height - 5 * age + 5
            caloric_requirement = bmr * activity_level

            self.result_label.text = f'Requerimiento Calórico Diario: {caloric_requirement:.2f} kcal'
        except ValueError:
            self.result_label.text = 'Por favor, ingrese valores válidos.'

    def enable_inputs(self, instance):
        self.weight_input.disabled = False
        self.height_input.disabled = False
        self.age_input.disabled = False
        self.activity_input.disabled = False

    def reset_inputs(self, instance):
        self.weight_input.text = ''
        self.height_input.text = ''
        self.age_input.text = ''
        self.activity_input.text = ''
        self.result_label.text = ''
        self.weight_input.disabled = True
        self.height_input.disabled = True
        self.age_input.disabled = True
        self.activity_input.disabled = True

class CaloricApp(App):
    def build(self):
        return CaloricRequirementCalculator()

if __name__ == '__main__':
    CaloricApp().run()
