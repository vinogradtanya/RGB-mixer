from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        main_layout = StackLayout(orientation='tb-lr')

        slider1 = Slider(size_hint = (0.5, 0.1), min = 0, max = 255, value = 255, value_track = True,
                         value_track_color = [0, 0.7, 0, 1])
        slider2 = Slider(size_hint=(0.5, 0.1), min=0, max=255, value=255, value_track=True,
                         value_track_color=[0, 0.7, 0, 1])
        slider3 = Slider(size_hint=(0.5, 0.1), min=0, max=255, value=255, value_track=True,
                         value_track_color=[0, 0.7, 0, 1])
        slider4 = Slider(size_hint=(0.5, 0.1), min=0, max=100, value=100, value_track=True,
                         value_track_color=[0, 0.7, 0, 1])

        button = Button(background_normal = '')

        lbl = Label(text = f'{str(int(slider1.value))} : {str(int(slider2.value))} : {str(int(slider3.value))} / {100}%',
                    size_hint = (0.5, 0.1), font_size = 30, bold=True)

        """Реализуем функцию, которая будет задавать значение цвета кнопки и 
        изменять текст Label на соответствующее цвету значение."""

        def on_value(instance, value):
            button.background_color = [int(slider1.value) / 255, int(slider2.value) / 255, int(slider3.value) / 255,
                                       int(slider4.value) / 100]
            lbl.text = (f'{str(int(slider1.value))} : {str(int(slider2.value))} : {str(int(slider3.value))} / {str(int(slider4.value))}%')
        #Делаем привязку ползунков к функции
        slider1.bind(value= on_value)
        slider2.bind(value=on_value)
        slider3.bind(value=on_value)
        slider4.bind(value=on_value)
        #Добавляем все виджеты в StackLayout
        main_layout.add_widget(slider1)
        main_layout.add_widget(slider2)
        main_layout.add_widget(slider3)
        main_layout.add_widget(slider4)
        main_layout.add_widget(lbl)
        main_layout.add_widget(button)

        return main_layout

if __name__ == '__main__':
    MyApp().run()





