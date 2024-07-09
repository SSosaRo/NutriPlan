from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class DietPlanCustomization(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10

        self.add_widget(Label(text='Objetivo de Calorías:'))
        self.calorie_goal_input = TextInput(input_filter='float', multiline=False)
        self.calorie_goal_input.disabled = True
        self.add_widget(self.calorie_goal_input)

        self.add_widget(Label(text='Preferencias Alimenticias:'))
        self.preferences_input = TextInput(multiline=False)
        self.preferences_input.disabled = True
        self.add_widget(self.preferences_input)

        self.customize_button = Button(text='Generar Plan')
        self.customize_button.bind(on_press=self.customize_plan)
        self.add_widget(self.customize_button)

        self.modify_button = Button(text='Modificar')
        self.modify_button.bind(on_press=self.enable_inputs)
        self.add_widget(self.modify_button)

        self.new_button = Button(text='Nuevo')
        self.new_button.bind(on_press=self.reset_inputs)
        self.add_widget(self.new_button)

        self.result_label = Label(text='')
        self.add_widget(self.result_label)

    def customize_plan(self, instance):
        calorie_goal = self.calorie_goal_input.text
        preferences = self.preferences_input.text

        if calorie_goal and preferences:
            self.result_label.text = f'Plan generado para {calorie_goal} calorías con preferencias: {preferences}'
            self.calorie_goal_input.text = ''
            self.preferences_input.text = ''
        else:
            self.result_label.text = 'Por favor, complete todos los campos.'

    def enable_inputs(self, instance):
        self.calorie_goal_input.disabled = False
        self.preferences_input.disabled = False

    def reset_inputs(self, instance):
        self.calorie_goal_input.text = ''
        self.preferences_input.text = ''
        self.result_label.text = ''
        self.calorie_goal_input.disabled = True
        self.preferences_input.disabled = True

class DietPlanApp(App):
    def build(self):
        return DietPlanCustomization()

if __name__ == '__main__':
    DietPlanApp().run()
