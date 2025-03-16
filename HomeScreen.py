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




class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
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
        
        title_label = Label(text="欢迎来到学境空间", font_size='30sp', halign='center', font_name='SimHei',color='black')
        layout.add_widget(title_label)
        
        # 添加三个模块按钮
        modules_layout = GridLayout(cols=3, spacing=10, size_hint=(1, 0.3))
        
        my_care_button = Button(text="我的关心", font_name='SimHei')
        my_care_button.bind(on_press=self.go_to_my_care)
        modules_layout.add_widget(my_care_button)
        
        my_reply_button = Button(text="我的回复", font_name='SimHei')
        my_reply_button.bind(on_press=self.go_to_my_reply)
        modules_layout.add_widget(my_reply_button)
        
        campus_info_button = Button(text="校园资讯", font_name='SimHei')
        campus_info_button.bind(on_press=self.go_to_campus_info)
        modules_layout.add_widget(campus_info_button)
        
        layout.add_widget(modules_layout)
        
        # 添加论坛入口按钮
        forum_button = Button(text="进入论坛", size_hint=(1, 0.2), font_name='SimHei')
        forum_button.bind(on_press=self.go_to_forum)
        layout.add_widget(forum_button)
        
        # 添加广告位
        ad_label = Label(text="广告位", size_hint=(1, 0.1), font_name='SimHei')
        layout.add_widget(ad_label)
        
        # 添加切换控件
        toggle_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.2), spacing=10)

        # 创建“学长问答”按钮和文字布局
        qna_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(100, 150))
        qna_button = ToggleButton(text="", background_normal='icon/学长问答.png', size_hint=(None, None), size=(100, 100))
        qna_label = Label(text="学长问答", font_name='SimHei', size_hint=(None, None), size=(100, 50))
        qna_layout.add_widget(qna_button)
        qna_layout.add_widget(qna_label)

        # 创建“学境空间”按钮和文字布局
        live_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(100, 150))
        live_button = ToggleButton(text="", background_normal='icon/学境空间.png', size_hint=(None, None), size=(100, 100))
        live_label = Label(text="学境空间", font_name='SimHei', size_hint=(None, None), size=(100, 50))
        live_layout.add_widget(live_button)
        live_layout.add_widget(live_label)

        # 创建“增值服务”按钮和文字布局
        service_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(100, 150))
        service_button = ToggleButton(text="", background_normal='icon/增值服务.png', size_hint=(None, None), size=(100, 100))
        service_label = Label(text="增值服务", font_name='SimHei', size_hint=(None, None), size=(100, 50))
        service_layout.add_widget(service_button)
        service_layout.add_widget(service_label)

        # 创建“我的”按钮和文字布局
        my_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(100, 150))
        my_button = ToggleButton(text="", background_normal='icon/我的.png', size_hint=(None, None), size=(100, 100))
        my_label = Label(text="我的", font_name='SimHei', size_hint=(None, None), size=(100, 50))
        my_layout.add_widget(my_button)
        my_layout.add_widget(my_label)

        # 将每个按钮和文字的布局添加到主布局中
        toggle_layout.add_widget(qna_layout)
        toggle_layout.add_widget(live_layout)
        toggle_layout.add_widget(service_layout)
        toggle_layout.add_widget(my_layout)


        layout.add_widget(toggle_layout)

        self.add_widget(layout)
    
    def on_search(self, instance):
        search_text = self.search_input.text
        print(f"搜索内容: {search_text}")
    
    def go_to_courses(self, instance):
        self.manager.current = 'courses'
    
    def go_to_my_care(self, instance):
        self.manager.current = 'my_care'
    
    def go_to_my_reply(self, instance):
        self.manager.current = 'my_reply'
    
    def go_to_campus_info(self, instance):
        self.manager.current = 'campus_info'
    
    def go_to_forum(self, instance):
        self.manager.current = 'forum'




