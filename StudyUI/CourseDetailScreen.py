from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.core.text import LabelBase
from kivy.core.window import Window

class CourseDetailScreen(Screen):
    def __init__(self, **kwargs):
        super(CourseDetailScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # 添加背景图
        background = Image(source='background.jpg', allow_stretch=True, keep_ratio=False)
        self.add_widget(background)
        
        # 添加搜索框和搜索按钮
        search_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        self.search_input = TextInput(hint_text='搜索...', font_name='SimHei', size_hint=(0.8, 1), multiline=False)
        search_button = Button(text='搜索', font_name='SimHei', size_hint=(0.2, 1))
        search_button.bind(on_press=self.on_search)
        search_layout.add_widget(self.search_input)
        search_layout.add_widget(search_button)
        layout.add_widget(search_layout)
        
        title_label = Label(text="课程详情", font_size='24sp', halign='center', font_name='SimHei')
        layout.add_widget(title_label)
        
        description_label = Label(text="这是一个关于基础编程的课程，涵盖变量、条件语句和循环等内容。", halign='left', valign='top', font_name='SimHei')
        layout.add_widget(description_label)
        
        back_button = Button(text="返回课程列表", size_hint=(1, 0.1), font_name='SimHei')
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)
        
        # 添加广告位
        ad_label = Label(text="广告位", size_hint=(1, 0.1), font_name='SimHei')
        layout.add_widget(ad_label)
        
        # 添加切换控件
        toggle_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1), spacing=10)
        
        qna_button = ToggleButton(text="学长问答", font_name='SimHei')
        live_button = ToggleButton(text="学境空间", font_name='SimHei')
        service_button = ToggleButton(text="增值服务", font_name='SimHei')
        
        toggle_layout.add_widget(qna_button)
        toggle_layout.add_widget(live_button)
        toggle_layout.add_widget(service_button)
        
        layout.add_widget(toggle_layout)
        
        self.add_widget(layout)
    
    def on_search(self, instance):
        search_text = self.search_input.text
        print(f"搜索内容: {search_text}")
    
    def go_back(self, instance):
        self.manager.current = 'courses'




