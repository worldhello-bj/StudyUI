from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.carousel import Carousel
from kivy.uix.image import Image, AsyncImage
from kivy.uix.textinput import TextInput
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.clock import Clock
from functools import partial

class RoundedButton(Button):
    def __init__(self, **kwargs):
        super(RoundedButton, self).__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (0.2, 0.6, 1, 1)  # 蓝色
        self.border = (0, 0, 0, 0)

    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(self.background_color[0], self.background_color[1], 
                  self.background_color[2], self.background_color[3])
            RoundedRectangle(pos=self.pos, size=self.size, radius=[10,])

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        
        # 使用BoxLayout作为主布局
        main_layout = BoxLayout(orientation='vertical', spacing=dp(10), padding=dp(10))
        
        # 添加背景图
        with main_layout.canvas.before:
            Color(0.95, 0.95, 0.95, 1)  # 淡灰色背景
            self.rect = Rectangle(size=Window.size, pos=main_layout.pos)
        
        # 窗口大小变化时更新背景大小
        Window.bind(size=self._update_rect)
        
        # 顶部状态栏
        status_bar = BoxLayout(orientation='horizontal', size_hint=(1, 0.05))
        time_label = Label(text="时间", size_hint=(0.2, 1), font_name='SimHei', color=(0.3, 0.3, 0.3, 1))
        status_bar.add_widget(Label(size_hint=(0.6, 1)))  # 空间
        battery_label = Label(text="你好！用户名", size_hint=(0.2, 1), font_name='SimHei', color=(0.3, 0.3, 0.3, 1))
        status_bar.add_widget(time_label)
        status_bar.add_widget(battery_label)
        main_layout.add_widget(status_bar)
        
        # 搜索栏 - 使用圆角设计
        search_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.07), 
                                 padding=[dp(5), dp(5), dp(5), dp(5)])
        
        # 搜索框背景
        search_bg = BoxLayout(orientation='horizontal', size_hint=(0.9, 1))
        with search_bg.canvas.before:
            Color(0.9, 0.9, 0.9, 1)
            self.search_rect = RoundedRectangle(size=search_bg.size, 
                                               pos=search_bg.pos, radius=[20,])
        
        search_icon = Image(source='icon/search.jpg', size_hint=(0.1, 1))
        self.search_input = TextInput(hint_text='搜索课程、问题或话题...', 
                                     font_name='SimHei', 
                                     size_hint=(0.8, 1),
                                     multiline=False,
                                     background_color=(0,0,0,0),
                                     foreground_color=(0.3, 0.3, 0.3, 1),
                                     cursor_color=(0.2, 0.6, 1, 1),
                                     padding=[10, 10, 0, 0])
                                     
        search_bg.add_widget(search_icon)
        search_bg.add_widget(self.search_input)
        search_bg.bind(size=self._update_search_rect, pos=self._update_search_rect)
        
        search_button = RoundedButton(text='搜索', 
                                     font_name='SimHei', 
                                     size_hint=(0.2, 1),
                                     color=(1, 1, 1, 1))
        search_button.bind(on_press=self.on_search)
        
        search_layout.add_widget(search_bg)
        search_layout.add_widget(search_button)
        main_layout.add_widget(search_layout)
        
        # 欢迎标题
        title_box = BoxLayout(orientation='vertical', size_hint=(1, 0.1))
        title_label = Label(text="欢迎来到学境空间", 
                           font_size='24sp', 
                           font_name='YouYuan',
                           color=(0.2, 0.2, 0.8, 1),
                           bold=True)
        subtitle_label = Label(text="与知识相伴，与未来同行", 
                              font_size='14sp', 
                              font_name='SimHei',
                              color=(0.5, 0.5, 0.5, 1))
        title_box.add_widget(title_label)
        title_box.add_widget(subtitle_label)
        main_layout.add_widget(title_box)
        
        # 轮播广告位
        carousel = Carousel(direction='right', size_hint=(1, 0.25), loop=True)
        
        # 添加三张轮播图
        for i in range(1, 4):
            slide = BoxLayout()
            with slide.canvas.before:
                Color(1, 1, 1, 1)
                RoundedRectangle(pos=slide.pos, size=slide.size, radius=[15,])
        
            img = AsyncImage(source=f'background{i}.jpg', allow_stretch=True, keep_ratio=False)
            slide.add_widget(img)
            carousel.add_widget(slide)
        
        main_layout.add_widget(carousel)
        
        # 自动轮播
        Clock.schedule_interval(lambda dt: carousel.load_next(), 5)
        
        # 功能模块 - 使用卡片设计
        module_label = Label(text="常用功能", 
                            font_size='18sp',
                            font_name='SimHei',
                            color=(0.3, 0.3, 0.3, 1),
                            size_hint=(1, 0.05),
                            halign='left')
        module_label.bind(size=self._update_label_text_size)
        main_layout.add_widget(module_label)
        
        modules_layout = GridLayout(cols=3, spacing=dp(15), size_hint=(1, 0.2), padding=[dp(5), dp(5), dp(5), dp(5)])
        
        # 创建模块卡片
        my_care_card = self._create_module_card('icon/heart.png', "我的关心", self.go_to_my_care)
        my_reply_card = self._create_module_card('icon/reply.png', "我的回复", self.go_to_my_reply)
        campus_info_card = self._create_module_card('icon/news.png', "校园资讯", self.go_to_campus_info)
        
        modules_layout.add_widget(my_care_card)
        modules_layout.add_widget(my_reply_card)
        modules_layout.add_widget(campus_info_card)
        main_layout.add_widget(modules_layout)
        
        # 热门课程推荐
        course_label = Label(text="热门课程", 
                           font_size='18sp',
                           font_name='SimHei',
                           color=(0.3, 0.3, 0.3, 1),
                           size_hint=(1, 0.05),
                           halign='left')
        course_label.bind(size=self._update_label_text_size)
        main_layout.add_widget(course_label)
        
        # 使用滚动视图展示热门课程
        scroll_view = ScrollView(size_hint=(1, 0.2), do_scroll_x=True, do_scroll_y=False)
        courses_layout = BoxLayout(orientation='horizontal', spacing=dp(15), size_hint=(None, 1))
        courses_layout.bind(minimum_width=courses_layout.setter('width'))
        
        # 添加热门课程
        course_data = [
            {"title": "微积分基础", "image": "background1.jpg", "author": "张教授"},
            {"title": "数据结构", "image": "background2.jpg", "author": "李教授"},
            {"title": "机器学习", "image": "background3.jpg", "author": "王教授"},
            {"title": "网络开发", "image": "background1.jpg", "author": "刘教授"}
        ]
        
        for course in course_data:
            course_card = self._create_course_card(course["image"], course["title"], course["author"])
            courses_layout.add_widget(course_card)
            
        scroll_view.add_widget(courses_layout)
        main_layout.add_widget(scroll_view)
        
        # 论坛入口
        forum_label = Label(text="热门讨论", 
                          font_size='18sp',
                          font_name='SimHei',
                          color=(0.3, 0.3, 0.3, 1),
                          size_hint=(1, 0.05),
                          halign='left')
        forum_label.bind(size=self._update_label_text_size)
        main_layout.add_widget(forum_label)
        
        # 论坛预览卡片
        forum_preview = BoxLayout(orientation='vertical', size_hint=(1, 0.15))
        with forum_preview.canvas.before:
            Color(1, 1, 1, 1)
            RoundedRectangle(pos=forum_preview.pos, size=forum_preview.size, radius=[15,])
            
        forum_title = Label(text="如何高效学习编程？", 
                           font_size='16sp',
                           font_name='SimHei',
                           color=(0.2, 0.2, 0.2, 1),
                           size_hint=(1, 0.4),
                           halign='left')
        forum_title.bind(size=self._update_label_text_size)
        
        forum_stats = BoxLayout(orientation='horizontal', size_hint=(1, 0.3))
        forum_stats.add_widget(Label(text="回复: 暂无", font_size='12sp', font_name='SimHei', color=(0.5, 0.5, 0.5, 1)))
        forum_stats.add_widget(Label(text="点赞: 暂无", font_size='12sp', font_name='SimHei', color=(0.5, 0.5, 0.5, 1)))
        
        forum_button = Button(text="查看更多讨论", 
                             font_size='14sp',
                             font_name='SimHei',
                             background_color=(0.2, 0.6, 1, 1),
                             color=(1, 1, 1, 1),
                             size_hint=(1, 0.3))
        forum_button.bind(on_press=self.go_to_forum)
        
        forum_preview.add_widget(forum_title)
        forum_preview.add_widget(forum_stats)
        forum_preview.add_widget(forum_button)
        forum_preview.bind(size=self._update_forum_bg, pos=self._update_forum_bg)
        
        main_layout.add_widget(forum_preview)

        # 底部导航栏
        nav_bar = BoxLayout(orientation='horizontal', size_hint=(1, 0.1), spacing=dp(5))
        with nav_bar.canvas.before:
            Color(1, 1, 1, 1)
            self.nav_rect = Rectangle(size=nav_bar.size, pos=nav_bar.pos)

        nav_items = [
            {"icon": "icon/学长问答.png", "text": "学长问答", "callback": None},
            {"icon": "icon/学境空间.png", "text": "学境空间", "callback": self.go_to_courses},
            {"icon": "icon/增值服务.png", "text": "增值服务", "callback": None},
            {"icon": "icon/我的.png", "text": "我的", "callback": None}
        ]

        for item in nav_items:
            nav_item = self._create_nav_item(item["icon"], item["text"], item["callback"])
            nav_bar.add_widget(nav_item)

        nav_bar.bind(size=self._update_nav_rect, pos=self._update_nav_rect)
        main_layout.add_widget(nav_bar)

        self.add_widget(main_layout)

    def _update_rect(self, instance, value):
        """更新背景矩形大小"""
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def _update_search_rect(self, instance, value):
        """更新搜索框背景"""
        self.search_rect.size = instance.size
        self.search_rect.pos = instance.pos

    def _update_forum_bg(self, instance, value):
        """更新论坛预览背景"""
        instance.canvas.before.clear()
        with instance.canvas.before:
            Color(1, 1, 1, 1)
            RoundedRectangle(pos=instance.pos, size=instance.size, radius=[15,])
    
    def _update_nav_rect(self, instance, value):
        """更新导航栏背景"""
        self.nav_rect.size = instance.size
        self.nav_rect.pos = instance.pos
    
    def _update_label_text_size(self, instance, value):
        """更新标签文本大小，使其左对齐"""
        instance.text_size = (instance.width, None)
    
    def _create_module_card(self, icon_src, text, callback):
        """创建功能模块卡片"""
        card = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(120))
    
        # 添加卡片背景和阴影效果
        with card.canvas.before:
            # 添加阴影效果 (深色背景)
            Color(0.9, 0.9, 0.9, 0.5)
            RoundedRectangle(pos=(card.pos[0]+dp(2), card.pos[1]-dp(2)), 
                             size=(card.size[0], card.size[1]), 
                             radius=[15,])
            # 添加主卡片背景 (白色)
            Color(1, 1, 1, 1)
            RoundedRectangle(pos=card.pos, size=card.size, radius=[15,])
    
        # 添加图标
        icon = Image(source=icon_src, size_hint=(1, 0.7))
    
        # 添加文字标签
        label = Label(text=text, 
                     font_name='SimHei', 
                     size_hint=(1, 0.3), 
                     color=(0.2, 0.2, 0.2, 1))
    
        card.add_widget(icon)
        card.add_widget(label)
    
        # 绑定点击事件
        if callback:
            card.bind(on_touch_down=lambda instance, touch: self._on_card_touch(instance, touch, callback))
    
        return card

    def _create_course_card(self, image_src, title, author):
        """创建课程卡片"""
        card = BoxLayout(orientation='vertical', size_hint=(None, 1), width=dp(160))
    
        # 添加卡片背景
        with card.canvas.before:
            Color(1, 1, 1, 1)
            RoundedRectangle(pos=card.pos, size=card.size, radius=[15,])
    
        # 课程封面图
        image = AsyncImage(source=image_src, 
                          allow_stretch=True, 
                          keep_ratio=True,
                          size_hint=(1, 0.7))
    
        # 标题和作者信息
        info_layout = BoxLayout(orientation='vertical', size_hint=(1, 0.3), padding=[dp(5), dp(5), dp(5), dp(5)])
        title_label = Label(text=title, 
                           font_name='SimHei', 
                           font_size='14sp', 
                           color=(0.2, 0.2, 0.2, 1),
                           size_hint=(1, 0.6),
                           halign='left')
        title_label.bind(size=self._update_label_text_size)
    
        author_label = Label(text=author, 
                            font_name='SimHei', 
                            font_size='12sp', 
                            color=(0.5, 0.5, 0.5, 1),
                            size_hint=(1, 0.4),
                            halign='left')
        author_label.bind(size=self._update_label_text_size)
    
        info_layout.add_widget(title_label)
        info_layout.add_widget(author_label)
    
        card.add_widget(image)
        card.add_widget(info_layout)
    
        # 绑定点击事件
        card.bind(on_touch_down=lambda instance, touch: self._on_card_touch(instance, touch, self.go_to_courses))
    
        return card

    def _create_nav_item(self, icon_src, text, callback):
        """创建底部导航项"""
        item = BoxLayout(orientation='vertical')
    
        icon = Image(source=icon_src, size_hint=(1, 0.7))
        label = Label(text=text, font_name='SimHei', font_size='12sp', size_hint=(1, 0.3), color=(0.3, 0.3, 0.3, 1))
    
        item.add_widget(icon)
        item.add_widget(label)
    
        # 绑定点击事件
        if callback:
            item.bind(on_touch_down=lambda instance, touch: self._on_card_touch(instance, touch, callback))
    
        return item

    def _on_card_touch(self, instance, touch, callback):
        """处理卡片点击事件"""
        if instance.collide_point(*touch.pos) and touch.is_double_tap == False:
            callback(instance)
            return True
        return False

    def on_search(self, instance):
        """处理搜索按钮点击"""
        search_text = self.search_input.text
        print(f"搜索内容: {search_text}")
        # TODO: 实现搜索功能
    
    def go_to_courses(self, instance):
        """跳转到课程页面"""
        self.manager.current = 'courses'
    
    def go_to_my_care(self, instance):
        """跳转到我的关心页面"""
        self.manager.current = 'my_care'
    
    def go_to_my_reply(self, instance):
        """跳转到我的回复页面"""
        self.manager.current = 'my_reply'
    
    def go_to_campus_info(self, instance):
        """跳转到校园资讯页面"""
        self.manager.current = 'campus_info'
    
    def go_to_forum(self, instance):
        """跳转到论坛页面"""
        self.manager.current = 'forum'
