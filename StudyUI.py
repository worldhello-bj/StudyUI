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

# 注册自定义字体
LabelBase.register(name='SimHei', fn_regular='fonts/simhei.ttf')

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

class CoursesScreen(Screen):
    def __init__(self, **kwargs):
        super(CoursesScreen, self).__init__(**kwargs)
        layout = GridLayout(cols=1, spacing=10, padding=10)
        
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
        
        back_button = Button(text="返回主菜单", size_hint=(1, 0.1), font_name='SimHei')
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)
        
        course1_button = Button(text="课程1: 基础编程", size_hint=(1, 0.2), font_name='SimHei')
        course1_button.bind(on_press=self.go_to_course_detail)
        layout.add_widget(course1_button)
        
        course2_button = Button(text="课程2: 数据结构", size_hint=(1, 0.2), font_name='SimHei')
        course2_button.bind(on_press=self.go_to_course_detail)
        layout.add_widget(course2_button)
        
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
        self.manager.current = 'home'
    
    def go_to_course_detail(self, instance):
        self.manager.current = 'course_detail'

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

class MyCareScreen(Screen):
    def __init__(self, **kwargs):
        super(MyCareScreen, self).__init__(**kwargs)
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
        
        title_label = Label(text="我的关心", font_size='24sp', halign='center', font_name='SimHei')
        layout.add_widget(title_label)
        
        exit_button = Button(text="退出", size_hint=(1, 0.1), font_name='SimHei')
        exit_button.bind(on_press=self.go_back)
        layout.add_widget(exit_button)
        
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
        self.manager.current = 'home'

class MyReplyScreen(Screen):
    def __init__(self, **kwargs):
        super(MyReplyScreen, self).__init__(**kwargs)
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
        
        title_label = Label(text="我的回复", font_size='24sp', halign='center', font_name='SimHei')
        layout.add_widget(title_label)
        
        exit_button = Button(text="退出", size_hint=(1, 0.1), font_name='SimHei')
        exit_button.bind(on_press=self.go_back)
        layout.add_widget(exit_button)
        
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
        self.manager.current = 'home'

class CampusInfoScreen(Screen):
    def __init__(self, **kwargs):
        super(CampusInfoScreen, self).__init__(**kwargs)
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
        
        title_label = Label(text="校园资讯", font_size='24sp', halign='center', font_name='SimHei')
        layout.add_widget(title_label)
        
        exit_button = Button(text="退出", size_hint=(1, 0.1), font_name='SimHei')
        exit_button.bind(on_press=self.go_back)
        layout.add_widget(exit_button)
        
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
        self.manager.current = 'home'

class ForumScreen(Screen):
    def __init__(self, **kwargs):
        super(ForumScreen, self).__init__(**kwargs)
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
        
        title_label = Label(text="论坛", font_size='24sp', halign='center', font_name='SimHei')
        layout.add_widget(title_label)
        
        exit_button = Button(text="退出", size_hint=(1, 0.1), font_name='SimHei')
        exit_button.bind(on_press=self.go_back)
        layout.add_widget(exit_button)
        
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
        self.manager.current = 'home'

class LearningApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(CoursesScreen(name='courses'))
        sm.add_widget(CourseDetailScreen(name='course_detail'))
        sm.add_widget(MyCareScreen(name='my_care'))
        sm.add_widget(MyReplyScreen(name='my_reply'))
        sm.add_widget(CampusInfoScreen(name='campus_info'))
        sm.add_widget(ForumScreen(name='forum'))
        return sm

if __name__ == '__main__':
    LearningApp().run()
