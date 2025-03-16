from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.config import Config
from kivy.metrics import dp

from ForumScreen import ForumScreen
from HomeScreen import HomeScreen
from CourseScreen import CoursesScreen
from CourseDetailScreen import CourseDetailScreen
from MyCareScreen import MyCareScreen
from MyReplyScreen import MyReplyScreen
from CampusInfoScreen import CampusInfoScreen

# 配置窗口大小和标题
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '700')
Config.set('kivy', 'window_icon', 'icon/app_icon.png')
Config.write()

# 注册自定义字体
LabelBase.register(name='SimHei', fn_regular='fonts/simhei.ttf')
# 可以添加更多字体
LabelBase.register(name='YouYuan', fn_regular='fonts/youyuan.ttf')

class LearningApp(App):
    def build(self):
        # 设置窗口标题
        self.title = '学境空间 - 学习平台'
        
        # 使用过渡动画效果
        sm = ScreenManager(transition=FadeTransition())
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
