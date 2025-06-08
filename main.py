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
                radius=[dp(15)]
            )

            # Основной фон кнопки
            Color(*self.bg_color)
            RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[dp(15)]
            )

            # Неоновая граница
            Color(*self.neon_color)
            Line(
                rounded_rectangle=(self.x, self.y, self.width, self.height, dp(15)),
                width=dp(2)
            )

            # Световой блик
            Color(1, 1, 1, 0.15)
            RoundedRectangle(
                pos=(self.x + dp(4), self.y + self.height * 0.65),
                size=(self.width - dp(8), self.height * 0.2),
                radius=[dp(8)]
            )

    def on_press_animation(self, instance):
        anim = Animation(
            size=(self.width * 0.95, self.height * 0.95),
            duration=0.1
        )
        anim.start(self)

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

    def update_graphics(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            # Внешнее свечение
            Color(1, 0.8, 0, 0.6)
            RoundedRectangle(
                pos=(self.x - dp(2), self.y - dp(2)),
                size=(self.width + dp(4), self.height + dp(4)),
                radius=[dp(12)]
            )

            # Основной фон
            Color(0.2, 0.15, 0.1, 1)
            RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[dp(12)]
            )

            # Золотистая граница
            Color(1, 0.8, 0, 1)
            Line(
                rounded_rectangle=(self.x, self.y, self.width, self.height, dp(12)),
                width=dp(2)
            )


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
        self.text_size = (self.width - dp(20), self.height)

    def on_text_change(self, instance, text):
        self.halign = 'center'

    def update_graphics(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            # Внешнее свечение при фокусе
            if self.is_focused:
                Color(*self.neon_color, 0.5)
                RoundedRectangle(
                    pos=(self.x - dp(2), self.y - dp(2)),
                    size=(self.width + dp(4), self.height + dp(4)),
                    radius=[dp(12)]
                )

            # Основной фон
            Color(0.18, 0.18, 0.22, 1)
            RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[dp(12)]
            )

            # Граница
            if self.is_focused:
                Color(*self.neon_color)
                Line(
                    rounded_rectangle=(self.x, self.y, self.width, self.height, dp(12)),
                    width=dp(2)
                )
            else:
                Color(0.4, 0.4, 0.45, 1)
                Line(
                    rounded_rectangle=(self.x, self.y, self.width, self.height, dp(12)),
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
                pos=(self.x + dp(8), self.y - dp(8)),
                size=self.size,
                radius=[dp(25)]
            )

            # Средняя тень
            Color(0, 0, 0, 0.5)
            RoundedRectangle(
                pos=(self.x + dp(4), self.y - dp(4)),
                size=self.size,
                radius=[dp(25)]
            )

            # Основной фон карточки
            Color(0.15, 0.15, 0.2, 1)
            RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[dp(25)]
            )

            # Верхний блик
            Color(1, 1, 1, 0.05)
            RoundedRectangle(
                pos=(self.x + dp(4), self.y + self.height * 0.85),
                size=(self.width - dp(8), self.height * 0.1),
                radius=[dp(20), dp(20), 0, 0]
            )


class GuessNumberWidget(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Темный фон
        Window.clearcolor = (0.08, 0.08, 0.1, 1)

        # Получаем размеры экрана
        self.screen_width = Window.width
        self.screen_height = Window.height

        # Привязываем к изменению размера окна
        Window.bind(on_resize=self.on_window_resize)

        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.hint_shown = False

        # Основная игровая карточка с улучшенными отступами
        self.game_card = DarkCard(
            orientation='vertical',
            padding=[dp(15), dp(15)],
            spacing=dp(8),
            size_hint=(0.95, 0.9),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        # Заголовок с адаптивным размером и переносом текста
        self.title_label = Label(
            text="УГАДАЙ ЧИСЛО",
            font_size=self.get_adaptive_font_size(24),
            color=(0, 0.8, 1, 1),
            size_hint=(1, 0.1),
            bold=True,
            text_size=(None, None),
            halign='center',
            valign='middle'
        )
        self.game_card.add_widget(self.title_label)

        # Подзаголовок с переносом текста
        self.subtitle_label = Label(
            text="Современная игра\nна логику",
            font_size=self.get_adaptive_font_size(12),
            color=(0.6, 0.6, 0.7, 1),
            size_hint=(1, 0.08),
            text_size=(None, None),
            halign='center',
            valign='middle'
        )
        self.game_card.add_widget(self.subtitle_label)

        # Подсказка с переносом текста
        self.hint_label = Label(
            text="Я загадал число\nот 1 до 100",
            font_size=self.get_adaptive_font_size(14),
            color=(0.8, 0.8, 0.9, 1),
            size_hint=(1, 0.12),
            bold=True,
            text_size=(None, None),
            halign='center',
            valign='middle'
        )
        self.game_card.add_widget(self.hint_label)

        # Счетчик попыток
        self.attempts_label = Label(
            text="",
            font_size=self.get_adaptive_font_size(12),
            color=(0.7, 0.4, 1, 1),
            size_hint=(1, 0.06),
            text_size=(None, None),
            halign='center',
            valign='middle'
        )
        self.game_card.add_widget(self.attempts_label)

        # Поле ввода с сокращенным hint_text
        self.guess_input = StableTextInput(
            hint_text="Введите число",
            font_size=self.get_adaptive_font_size(16),
            size_hint=(1, 0.12),
            input_filter='int',
            foreground_color=(0.95, 0.95, 1, 1),
            cursor_color=(0, 0.8, 1, 1),
            hint_text_color=(0.7, 0.7, 0.8, 1),
            padding=[dp(10), dp(10)],
            neon_color=(0, 0.8, 1, 1)
        )
        self.game_card.add_widget(self.guess_input)

        # Пространство
        spacer1 = Widget(size_hint=(1, 0.02))
        self.game_card.add_widget(spacer1)

        # Кнопка "Проверить"
        self.submit_button = NeonButton(
            text="ПРОВЕРИТЬ",
            font_size=self.get_adaptive_font_size(14),
            size_hint=(1, 0.1),
            neon_color=(0, 1, 0.5, 1),
            bg_color=(0.12, 0.18, 0.15, 1),
            color=(0, 1, 0.5, 1),
            bold=True
        )
        self.submit_button.bind(on_press=self.check_guess)
        self.game_card.add_widget(self.submit_button)

        # Результат с переносом текста
        self.result_label = Label(
            text="",
            font_size=self.get_adaptive_font_size(13),
            color=(0.8, 0.8, 0.9, 1),
            size_hint=(1, 0.15),
            text_size=(None, None),
            halign='center',
            valign='middle'
        )
        self.game_card.add_widget(self.result_label)

        # Кнопка "Новая игра"
        self.restart_button = NeonButton(
            text="НОВАЯ ИГРА",
            font_size=self.get_adaptive_font_size(13),
            size_hint=(1, 0.09),
            neon_color=(1, 0.5, 0, 1),
            bg_color=(0.2, 0.15, 0.1, 1),
            color=(1, 0.5, 0, 1),
            bold=True
        )
        self.restart_button.bind(on_press=self.restart_game)
        self.game_card.add_widget(self.restart_button)

        self.add_widget(self.game_card)

        # Кнопка подсказки в верхнем правом углу (уменьшенная)
        self.hint_button = HintButton(
            text="?",
            font_size=self.get_adaptive_font_size(16),
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            pos_hint={'right': 0.95, 'top': 0.95},
            color=(1, 0.8, 0, 1),
            bold=True
        )
        self.hint_button.bind(on_press=self.show_hint)
        self.add_widget(self.hint_button)

        # Привязываем Enter
        self.guess_input.bind(on_text_validate=self.check_guess)

        # Обновляем text_size для всех Label
        self.update_text_sizes()

    def get_adaptive_font_size(self, base_size):
        """Возвращает адаптивный размер шрифта"""
        scale_factor = min(self.screen_width / 400, self.screen_height / 600)
        return sp(max(base_size * scale_factor, 10))  # Минимум 10sp

    def update_text_sizes(self):
        """Обновляет text_size для всех Label чтобы текст переносился"""
        Clock.schedule_once(self._update_text_sizes, 0.1)

    def _update_text_sizes(self, dt):
        """Отложенное обновление text_size"""
        labels = [
            self.title_label,
            self.subtitle_label,
            self.hint_label,
            self.attempts_label,
            self.result_label
        ]

        for label in labels:
            if label.width > 0:
                label.text_size = (label.width - dp(20), None)

    def on_window_resize(self, window, width, height):
        """Обработчик изменения размера окна"""
        self.screen_width = width
        self.screen_height = height
        self.update_adaptive_sizes()

    def update_adaptive_sizes(self):
        """Обновляет размеры элементов"""
        # Обновляем размеры шрифтов
        self.title_label.font_size = self.get_adaptive_font_size(24)
        self.subtitle_label.font_size = self.get_adaptive_font_size(12)
        self.hint_label.font_size = self.get_adaptive_font_size(14)
        self.attempts_label.font_size = self.get_adaptive_font_size(12)
        self.guess_input.font_size = self.get_adaptive_font_size(16)
        self.submit_button.font_size = self.get_adaptive_font_size(14)
        self.result_label.font_size = self.get_adaptive_font_size(13)
        self.restart_button.font_size = self.get_adaptive_font_size(13)
        self.hint_button.font_size = self.get_adaptive_font_size(16)

        # Обновляем text_size
        self.update_text_sizes()

    def show_hint(self, instance):
        """Показывает загаданное число"""
        if not self.hint_shown and not self.guess_input.disabled:
            self.hint_shown = True
            self.hint_label.text = f"ПОДСКАЗКА:\nЧисло {self.target_number}"
            self.hint_label.color = (1, 0.8, 0, 1)

            # Анимация подсказки
            anim = Animation(font_size=self.hint_label.font_size * 1.1, duration=0.3) + \
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
                self.show_error("Число от 1 до 100!")
                return

            self.attempts += 1
            self.attempts_label.text = f"Попытка: {self.attempts}"

            if user_guess < self.target_number:
                if not self.hint_shown:
                    self.hint_label.text = "Загаданное число\nБОЛЬШЕ!"
                    self.hint_label.color = (1, 0.6, 0, 1)
                self.result_label.text = f"Ваше число: {user_guess}"
                self.result_label.color = (0.7, 0.7, 0.8, 1)
                self.animate_hint()
            elif user_guess > self.target_number:
                if not self.hint_shown:
                    self.hint_label.text = "Загаданное число\nМЕНЬШЕ!"
                    self.hint_label.color = (1, 0.6, 0, 1)
                self.result_label.text = f"Ваше число: {user_guess}"
                self.result_label.color = (0.7, 0.7, 0.8, 1)
                self.animate_hint()
            else:
                self.celebrate_win()

            # Автоматическая очистка поля ввода
            self.guess_input.text = ""

        except ValueError:
            self.show_error("Введите число!")

    def show_error(self, message):
        self.hint_label.text = message
        self.hint_label.color = (1, 0.3, 0.3, 1)
        self.animate_error()
        self.guess_input.text = ""

    def celebrate_win(self):
        attempts_text = "попытку" if self.attempts == 1 else "попытки" if self.attempts < 5 else "попыток"

        self.result_label.text = f"ПОЗДРАВЛЯЮ!\n\nВы угадали число\n{self.target_number}\nза {self.attempts} {attempts_text}!"
        self.result_label.color = (0, 1, 0.5, 1)

        if not self.hint_shown:
            self.hint_label.text = "ОТЛИЧНАЯ\nРАБОТА!"
            self.hint_label.color = (0, 1, 0.5, 1)

        self.guess_input.disabled = True
        self.submit_button.disabled = True
        self.hint_button.disabled = True

        self.victory_animation()

    def victory_animation(self):
        anim = Animation(font_size=self.result_label.font_size * 1.2, color=(0, 1, 0.5, 1), duration=0.6) + \
               Animation(font_size=self.result_label.font_size, color=(0, 0.8, 0.4, 1), duration=0.6)
        anim.repeat = True
        anim.start(self.result_label)

    def animate_hint(self):
        anim = Animation(font_size=self.hint_label.font_size * 1.1, duration=0.2) + \
               Animation(font_size=self.hint_label.font_size, duration=0.2)
        anim.start(self.hint_label)

    def animate_error(self):
        original_x = self.guess_input.x
        shake_anim = (
                Animation(x=original_x + dp(15), duration=0.05) +
                Animation(x=original_x - dp(15), duration=0.05) +
                Animation(x=original_x + dp(10), duration=0.05) +
                Animation(x=original_x - dp(10), duration=0.05) +
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
        self.hint_label.text = "Я загадал число\nот 1 до 100"
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
        self.title = "Угадай число"
        return GuessNumberWidget()


if __name__ == "__main__":
    GuessNumberApp().run()