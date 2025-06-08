from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle, Line, Rectangle
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.metrics import dp, sp
import random


class NeonButton(Button):
    def __init__(self, neon_color=(0, 0.8, 1, 1), bg_color=(0.1, 0.1, 0.15, 1), **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_down = ''
        self.background_color = (0, 0, 0, 0)
        self.neon_color = neon_color
        self.bg_color = bg_color
        self.current_color = neon_color
        self.bind(pos=self.update_graphics, size=self.update_graphics)
        self.bind(on_press=self.on_press_animation)
        self.bind(on_release=self.on_release_animation)

    def update_graphics(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            # Внешнее свечение (неоновый эффект)
            Color(*self.neon_color, 0.6)
            RoundedRectangle(
                pos=(self.x - dp(3), self.y - dp(3)),
                size=(self.width + dp(6), self.height + dp(6)),
                radius=[dp(20)]
            )

            # Основной фон кнопки
            Color(*self.bg_color)
            RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[dp(20)]
            )

            # Неоновая граница
            Color(*self.neon_color)
            Line(
                rounded_rectangle=(self.x, self.y, self.width, self.height, dp(20)),
                width=dp(2)
            )

            # Световой блик
            Color(1, 1, 1, 0.15)
            RoundedRectangle(
                pos=(self.x + dp(4), self.y + self.height * 0.65),
                size=(self.width - dp(8), self.height * 0.2),
                radius=[dp(10)]
            )

    def on_press_animation(self, instance):
        anim = Animation(
            size=(self.width * 0.95, self.height * 0.95),
            duration=0.1
        )
        anim.start(self)

        # Усиление свечения при нажатии
        self.canvas.before.clear()
        with self.canvas.before:
            # Усиленное внешнее свечение
            Color(*self.neon_color, 0.8)
            RoundedRectangle(
                pos=(self.x - dp(5), self.y - dp(5)),
                size=(self.width + dp(10), self.height + dp(10)),
                radius=[dp(20)]
            )

            # Основной фон кнопки
            Color(*self.bg_color)
            RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[dp(20)]
            )

            # Усиленная неоновая граница
            Color(*self.neon_color)
            Line(
                rounded_rectangle=(self.x, self.y, self.width, self.height, dp(20)),
                width=dp(3)
            )

    def on_release_animation(self, instance):
        anim = Animation(
            size=(self.width / 0.95, self.height / 0.95),
            duration=0.1
        )
        anim.start(self)
        self.update_graphics()


class HintButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_down = ''
        self.background_color = (0, 0, 0, 0)
        self.bind(pos=self.update_graphics, size=self.update_graphics)
        self.bind(on_press=self.on_press_animation)
        self.bind(on_release=self.on_release_animation)

    def update_graphics(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            # Внешнее свечение
            Color(1, 0.8, 0, 0.6)  # Золотистое свечение
            RoundedRectangle(
                pos=(self.x - dp(2), self.y - dp(2)),
                size=(self.width + dp(4), self.height + dp(4)),
                radius=[dp(15)]
            )

            # Основной фон
            Color(0.2, 0.15, 0.1, 1)
            RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[dp(15)]
            )

            # Золотистая граница
            Color(1, 0.8, 0, 1)
            Line(
                rounded_rectangle=(self.x, self.y, self.width, self.height, dp(15)),
                width=dp(2)
            )

    def on_press_animation(self, instance):
        anim = Animation(size=(self.width * 0.9, self.height * 0.9), duration=0.1)
        anim.start(self)

    def on_release_animation(self, instance):
        anim = Animation(size=(self.width / 0.9, self.height / 0.9), duration=0.1)
        anim.start(self)


class StableTextInput(TextInput):
    def __init__(self, neon_color=(0, 0.8, 1, 1), **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_active = ''
        self.background_color = (0, 0, 0, 0)
        self.multiline = False
        self.neon_color = neon_color
        self.is_focused = False

        self.halign = 'center'
        self.valign = 'middle'

        self.bind(size=self.update_text_size)
        self.bind(pos=self.update_graphics, size=self.update_graphics)
        self.bind(focus=self.on_focus_change)
        self.bind(text=self.on_text_change)

    def update_text_size(self, *args):
        self.text_size = (self.width - dp(40), self.height)

    def on_text_change(self, instance, text):
        self.halign = 'center'

    def update_graphics(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            # Внешнее свечение при фокусе
            if self.is_focused:
                Color(*self.neon_color, 0.5)
                RoundedRectangle(
                    pos=(self.x - dp(3), self.y - dp(3)),
                    size=(self.width + dp(6), self.height + dp(6)),
                    radius=[dp(15)]
                )

            # Основной фон
            Color(0.18, 0.18, 0.22, 1)
            RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[dp(15)]
            )

            # Граница
            if self.is_focused:
                Color(*self.neon_color)
                Line(
                    rounded_rectangle=(self.x, self.y, self.width, self.height, dp(15)),
                    width=dp(2)
                )
            else:
                Color(0.4, 0.4, 0.45, 1)
                Line(
                    rounded_rectangle=(self.x, self.y, self.width, self.height, dp(15)),
                    width=dp(1)
                )

    def on_focus_change(self, instance, focus):
        self.is_focused = focus
        self.update_graphics()


class DarkCard(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(pos=self.update_graphics, size=self.update_graphics)

    def update_graphics(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            # Внешняя тень
            Color(0, 0, 0, 0.8)
            RoundedRectangle(
                pos=(self.x + dp(10), self.y - dp(10)),
                size=self.size,
                radius=[dp(30)]
            )

            # Средняя тень
            Color(0, 0, 0, 0.5)
            RoundedRectangle(
                pos=(self.x + dp(5), self.y - dp(5)),
                size=self.size,
                radius=[dp(30)]
            )

            # Основной фон карточки
            Color(0.15, 0.15, 0.2, 1)
            RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[dp(30)]
            )

            # Верхний блик
            Color(1, 1, 1, 0.05)
            RoundedRectangle(
                pos=(self.x + dp(6), self.y + self.height * 0.85),
                size=(self.width - dp(12), self.height * 0.1),
                radius=[dp(25), dp(25), 0, 0]
            )

            # Нижний градиент
            Color(0.1, 0.1, 0.15, 1)
            RoundedRectangle(
                pos=(self.x, self.y),
                size=(self.width, self.height * 0.3),
                radius=[0, 0, dp(30), dp(30)]
            )


class GuessNumberWidget(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Темный фон
        Window.clearcolor = (0.08, 0.08, 0.1, 1)

        # Адаптивные размеры в зависимости от экрана
        self.screen_width = Window.width
        self.screen_height = Window.height

        # Привязываем к изменению размера окна
        Window.bind(on_resize=self.on_window_resize)

        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.hint_shown = False

        # Основная игровая карточка
        self.game_card = DarkCard(
            orientation='vertical',
            padding=[dp(20), dp(20)],
            spacing=dp(15),
            size_hint=(0.9, 0.85),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        # Заголовок с адаптивным размером шрифта
        self.title_label = Label(
            text="УГАДАЙ ЧИСЛО",
            font_size=sp(32),  # Используем sp для адаптивности
            color=(0, 0.8, 1, 1),
            size_hint=(1, 0.12),
            bold=True
        )
        self.game_card.add_widget(self.title_label)

        # Подзаголовок
        self.subtitle_label = Label(
            text="Современная игра на логику",
            font_size=sp(14),
            color=(0.6, 0.6, 0.7, 1),
            size_hint=(1, 0.08)
        )
        self.game_card.add_widget(self.subtitle_label)

        # Разделитель
        separator = Widget(size_hint=(1, 0.02))
        self.game_card.add_widget(separator)

        # Подсказка
        self.hint_label = Label(
            text="Я загадал число от 1 до 100",
            font_size=sp(18),
            color=(0.8, 0.8, 0.9, 1),
            size_hint=(1, 0.12),
            bold=True
        )
        self.game_card.add_widget(self.hint_label)

        # Счетчик попыток
        self.attempts_label = Label(
            text="",
            font_size=sp(14),
            color=(0.7, 0.4, 1, 1),
            size_hint=(1, 0.08)
        )
        self.game_card.add_widget(self.attempts_label)

        # Поле ввода с адаптивными размерами
        self.guess_input = StableTextInput(
            hint_text="Введите число от 1 до 100",
            font_size=sp(20),
            size_hint=(1, 0.20),
            input_filter='int',
            foreground_color=(0.95, 0.95, 1, 1),
            cursor_color=(0, 0.8, 1, 1),
            hint_text_color=(0.7, 0.7, 0.8, 1),
            padding=[dp(15), dp(15)],
            neon_color=(0, 0.8, 1, 1)
        )
        self.game_card.add_widget(self.guess_input)

        # Пространство
        spacer1 = Widget(size_hint=(1, 0.03))
        self.game_card.add_widget(spacer1)

        # Кнопка "Проверить"
        self.submit_button = NeonButton(
            text="ПРОВЕРИТЬ",
            font_size=sp(18),
            size_hint=(1, 0.12),
            neon_color=(0, 1, 0.5, 1),
            bg_color=(0.12, 0.18, 0.15, 1),
            color=(0, 1, 0.5, 1),
            bold=True
        )
        self.submit_button.bind(on_press=self.check_guess)
        self.game_card.add_widget(self.submit_button)

        # Результат
        self.result_label = Label(
            text="",
            font_size=sp(16),
            color=(0.8, 0.8, 0.9, 1),
            size_hint=(1, 0.13),
            text_size=(None, None),
            halign='center',
            valign='middle'
        )
        self.game_card.add_widget(self.result_label)

        # Кнопка "Новая игра"
        self.restart_button = NeonButton(
            text="НОВАЯ ИГРА",
            font_size=sp(16),
            size_hint=(1, 0.11),
            neon_color=(1, 0.5, 0, 1),
            bg_color=(0.2, 0.15, 0.1, 1),
            color=(1, 0.5, 0, 1),
            bold=True
        )
        self.restart_button.bind(on_press=self.restart_game)
        self.game_card.add_widget(self.restart_button)

        self.add_widget(self.game_card)

        # Кнопка подсказки в верхнем правом углу
        self.hint_button = HintButton(
            text="?",
            font_size=sp(20),
            size_hint=(None, None),
            size=(dp(50), dp(50)),
            pos_hint={'right': 0.95, 'top': 0.95},
            color=(1, 0.8, 0, 1),
            bold=True
        )
        self.hint_button.bind(on_press=self.show_hint)
        self.add_widget(self.hint_button)

        # Привязываем Enter
        self.guess_input.bind(on_text_validate=self.check_guess)

        # Обновляем размеры при инициализации
        self.update_adaptive_sizes()

    def on_window_resize(self, window, width, height):
        """Обработчик изменения размера окна"""
        self.screen_width = width
        self.screen_height = height
        self.update_adaptive_sizes()

    def update_adaptive_sizes(self):
        """Обновляет размеры элементов в зависимости от размера экрана"""
        # Адаптивные размеры шрифтов
        base_font_scale = min(self.screen_width, self.screen_height) / 400

        self.title_label.font_size = sp(32 * base_font_scale)
        self.subtitle_label.font_size = sp(14 * base_font_scale)
        self.hint_label.font_size = sp(18 * base_font_scale)
        self.attempts_label.font_size = sp(14 * base_font_scale)
        self.guess_input.font_size = sp(20 * base_font_scale)
        self.submit_button.font_size = sp(18 * base_font_scale)
        self.result_label.font_size = sp(16 * base_font_scale)
        self.restart_button.font_size = sp(16 * base_font_scale)
        self.hint_button.font_size = sp(20 * base_font_scale)

    def show_hint(self, instance):
        """Показывает загаданное число"""
        if not self.hint_shown and not self.guess_input.disabled:
            self.hint_shown = True
            self.hint_label.text = f"ПОДСКАЗКА: Загаданное число {self.target_number}"
            self.hint_label.color = (1, 0.8, 0, 1)  # Золотистый цвет

            # Анимация подсказки
            anim = Animation(font_size=self.hint_label.font_size * 1.2, duration=0.3) + \
                   Animation(font_size=self.hint_label.font_size, duration=0.3)
            anim.start(self.hint_label)

            # Меняем текст кнопки
            self.hint_button.text = "!"
            self.hint_button.color = (1, 0.5, 0, 1)

    def check_guess(self, instance):
        input_text = self.guess_input.text.strip()
        if not input_text:
            self.show_error("Введите число!")
            return

        try:
            user_guess = int(input_text)
            if user_guess < 1 or user_guess > 100:
                self.show_error("Число должно быть от 1 до 100!")
                return

            self.attempts += 1
            self.attempts_label.text = f"Попытка: {self.attempts}"

            if user_guess < self.target_number:
                if not self.hint_shown:
                    self.hint_label.text = "Загаданное число БОЛЬШЕ!"
                    self.hint_label.color = (1, 0.6, 0, 1)
                self.result_label.text = f"Ваше число: {user_guess}"
                self.result_label.color = (0.7, 0.7, 0.8, 1)
                self.animate_hint()
            elif user_guess > self.target_number:
                if not self.hint_shown:
                    self.hint_label.text = "Загаданное число МЕНЬШЕ!"
                    self.hint_label.color = (1, 0.6, 0, 1)
                self.result_label.text = f"Ваше число: {user_guess}"
                self.result_label.color = (0.7, 0.7, 0.8, 1)
                self.animate_hint()
            else:
                self.celebrate_win()

            # Автоматическая очистка поля ввода после проверки
            self.guess_input.text = ""

        except ValueError:
            self.show_error("Введите корректное число!")

    def show_error(self, message):
        self.hint_label.text = message
        self.hint_label.color = (1, 0.3, 0.3, 1)
        self.animate_error()
        self.guess_input.text = ""

    def celebrate_win(self):
        attempts_text = "попытку" if self.attempts == 1 else "попытки" if self.attempts < 5 else "попыток"

        self.result_label.text = f"ПОЗДРАВЛЯЮ!\n\nВы угадали число {self.target_number}\nза {self.attempts} {attempts_text}!"
        self.result_label.color = (0, 1, 0.5, 1)

        if not self.hint_shown:
            self.hint_label.text = "ОТЛИЧНАЯ РАБОТА!"
            self.hint_label.color = (0, 1, 0.5, 1)

        self.guess_input.disabled = True
        self.submit_button.disabled = True
        self.hint_button.disabled = True

        self.victory_animation()

    def victory_animation(self):
        anim = Animation(font_size=self.result_label.font_size * 1.4, color=(0, 1, 0.5, 1), duration=0.6) + \
               Animation(font_size=self.result_label.font_size, color=(0, 0.8, 0.4, 1), duration=0.6)
        anim.repeat = True
        anim.start(self.result_label)

    def animate_hint(self):
        anim = Animation(font_size=self.hint_label.font_size * 1.2, duration=0.2) + \
               Animation(font_size=self.hint_label.font_size, duration=0.2)
        anim.start(self.hint_label)

    def animate_error(self):
        original_x = self.guess_input.x
        shake_anim = (
                Animation(x=original_x + dp(20), duration=0.05) +
                Animation(x=original_x - dp(20), duration=0.05) +
                Animation(x=original_x + dp(15), duration=0.05) +
                Animation(x=original_x - dp(15), duration=0.05) +
                Animation(x=original_x, duration=0.05)
        )
        shake_anim.start(self.guess_input)

    def restart_game(self, instance):
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.hint_shown = False
        self.guess_input.text = ""
        self.guess_input.disabled = False
        self.submit_button.disabled = False
        self.hint_button.disabled = False
        self.hint_label.text = "Я загадал новое число от 1 до 100"
        self.hint_label.color = (0.8, 0.8, 0.9, 1)
        self.result_label.text = ""
        self.attempts_label.text = ""

        # Сбрасываем кнопку подсказки
        self.hint_button.text = "?"
        self.hint_button.color = (1, 0.8, 0, 1)

        Animation.cancel_all(self.result_label)
        Animation.cancel_all(self.hint_label)


class GuessNumberApp(App):
    def build(self):
        self.title = "Угадай число - Adaptive"
        # Убираем фиксированный размер для адаптивности
        return GuessNumberWidget()


if __name__ == "__main__":
    GuessNumberApp().run()