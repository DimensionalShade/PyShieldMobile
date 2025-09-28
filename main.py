from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

# Цветовая схема
colors = {
    'background': '#0A0F1F',
    'header': '#0055AA',
    'accent': '#00BFFF',
    'text': '#E0F7FF',
    'input_bg': '#0F1C33',
    'log_bg': '#0F1C33'
}

# Локализация
translations = {
    'en': {
        'update': 'Update Blocklist',
        'test': 'Test Domain',
        'logs': 'Show Logs',
        'settings': 'Settings',
        'title': 'PyShieldMobile',
        'version': 'v1.0.0',
        'placeholder': 'example.com'
    },
    'ru': {
        'update': 'Обновить блоклист',
        'test': 'Тестировать домен',
        'logs': 'Показать логи',
        'settings': 'Настройки',
        'title': 'PyShieldMobile',
        'version': 'v1.0.0',
        'placeholder': 'example.com'
    },
    'ar': {
        'update': 'تحديث القائمة',
        'test': 'اختبار النطاق',
        'logs': 'عرض السجلات',
        'settings': 'الإعدادات',
        'title': 'PyShieldMobile',
        'version': 'v1.0.0',
        'placeholder': 'example.com'
    },
    'zh': {
        'update': '更新封锁列表',
        'test': '测试域名',
        'logs': '查看日志',
        'settings': '设置',
        'title': 'PyShieldMobile',
        'version': 'v1.0.0',
        'placeholder': 'example.com'
    }
}

# Выбор языка
current_lang = 'ru'
t = translations[current_lang]

class PyShieldGUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)
        Window.clearcolor = self.hex_to_rgba(colors['background'])

        # Заголовок
        self.add_widget(Label(text=f"{t['title']} {t['version']}", font_size=24,
                              color=self.hex_to_rgba(colors['header']), size_hint=(1, 0.1)))

        # Кнопка обновления
        self.add_widget(Button(text=t['update'], background_color=self.hex_to_rgba(colors['accent']),
                               color=self.hex_to_rgba(colors['text']), size_hint=(1, 0.1)))

        # Тест домена
        self.add_widget(Button(text=t['test'], background_color=self.hex_to_rgba(colors['accent']),
                               color=self.hex_to_rgba(colors['text']), size_hint=(1, 0.1)))
        self.add_widget(TextInput(hint_text=t['placeholder'], background_color=self.hex_to_rgba(colors['input_bg']),
                                  foreground_color=self.hex_to_rgba(colors['text']), size_hint=(1, 0.1)))

        # Показать логи
        self.add_widget(Button(text=t['logs'], background_color=self.hex_to_rgba(colors['accent']),
                               color=self.hex_to_rgba(colors['text']), size_hint=(1, 0.1)))

        # Лог-вывод
        log_area = ScrollView(size_hint=(1, 0.3))
        log_content = GridLayout(cols=1, size_hint_y=None)
        log_content.bind(minimum_height=log_content.setter('height'))
        for line in ["[2025-09-25 17:20] example.com blocked", "[2025-09-25 17:21] test.com allowed"]:
            log_content.add_widget(Label(text=line, font_size=14,
                                         color=self.hex_to_rgba(colors['accent']),
                                         size_hint_y=None, height=30))
        log_area.add_widget(log_content)
        self.add_widget(log_area)

        # Настройки
        self.add_widget(Button(text=t['settings'], background_color=self.hex_to_rgba(colors['accent']),
                               color=self.hex_to_rgba(colors['text']), size_hint=(1, 0.1)))

    def hex_to_rgba(self, hex_color):
        hex_color = hex_color.lstrip('#')
        return [int(hex_color[i:i+2], 16)/255.0 for i in (0, 2, 4)] + [1]

class PyShieldApp(App):
    def build(self):
        return PyShieldGUI()

if __name__ == '__main__':
    PyShieldApp().run()
