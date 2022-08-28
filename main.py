from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import  StringProperty
from kivymd.uix.pickers import MDDatePicker
from Helperr import screen_helper
from OmSriGanesh import screen_helperr

Window.size = (310,580)

# screen_helper was here
screen_helper = """
ScreenManager:
    FirstScreen:
        id: screen1
    SecondScreen:
        id: screen2
    WorkScreen:
        id:screen_work
    FourScreen:
        

<FirstScreen>:
    name: 'Intro'
    #MDList:
    Image:
        source: "money_edited.jpg" 
        size_hint: (0.6, 0.6)
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        allow_stretch : False
        keep_ratio : True
    MDLabel:
        text :"Hello there ! I see you've decided to track your expenses, how very responsible !"
        halign: 'center'
        theme_text_color : 'Custom'
        text_color : (0,0,0)
        size_hint : (1,0.01)
        font_style :'H6'
        pos_hint :{'center_x':0.5, 'center_y':0.8}

    MDRectangleFlatButton:
        text : "Get Started"
        pos_hint :{'center_x' :0.5, 'center_y': 0.2}
        on_press : root.manager.current = 'second'
        text_color :(0,0,0)
        font_style: "H6"

<SecondScreen>:
    name : 'second'
    MDTextField:
        id : amount
        hint_text: "Enter an amount"
        mode: "rectangle"
        helper_text : "Set your monthly budget"
        helper_text_mode: "persistent"
        pos_hint: {'center_x': 0.5, 'center_y' : 0.45}
        line_color_normal : [0,0,0,1]
        line_color_focus : [0,0,0,1]
        text_color_normal : [0,0,0,1]
        text_color_focus : [0,0,0,1]
        size_hint_x : None
        width : 200
        input_filter: 'float'

    MDTextField:
        id : submit
        hint_text: "Enter username"
        mode: "rectangle"
        icon_right : "account"
        icon_right_color : [0,0,0]
        helper_text : ""
        helper_text_mode: "persistent"
        pos_hint: {'center_x': 0.5, 'center_y' : 0.6}
        size_hint_x : None
        line_color_normal : [0,0,0,1]
        line_color_focus : [0,0,0,1]
        text_color_normal : [0,0,0,1]
        text_color_focus : [0,0,0,1]
        width : 200

    Image:
        source: "money_edited.jpg" 
        size_hint: (0.3, 0.3)
        pos_hint:{'center_x': 0.2, 'center_y': 0.8}
        allow_stretch : False
        keep_ratio : True
    MDLabel:
        text :"Let's setup our profile!"
        halign: 'center'
        theme_text_color : 'Custom'
        text_color : (0,0,0)
        size_hint : (1,0)
        font_style :'Subtitle1'
        pos_hint :{'center_x':0.65, 'center_y':0.83}
    MDLabel:
        text :"Don't forget to save it!" #figure out how to do a newline pls
        halign: 'center'
        theme_text_color : 'Custom'
        text_color : (0,0,0)
        size_hint : (1,0)
        font_style :'Subtitle1'
        pos_hint :{'center_x':0.65, 'center_y':0.77}

    MDRectangleFlatButton:
        id: submitBtn
        text : "Save"
        pos_hint :{'center_x' :0.5, 'center_y': 0.3}
        text_color :(0,0,0)
        font_style: "Body1"
        #on_release: root.press()


    MDRectangleFlatButton:
        text : "Next ->"
        pos_hint :{'center_x' :0.73, 'center_y': 0.2}
        text_color :(0,0,0)
        font_style: "Body1"
        #on_release : self.show_data
        on_press : root.manager.current = 'third'

<WorkScreen>:
    name: "third"
    MDTextField:
        id : submit
        hint_text: "Enter expense"
        mode: "rectangle"
        helper_text : ""
        helper_text_mode: "persistent"
        pos_hint: {'center_x': 0.25, 'center_y' : 0.7}
        size_hint_x : None
        line_color_normal : [0,0,0,1]
        line_color_focus : [0,0,0,1]
        text_color_normal : [0,0,0,1]
        text_color_focus : [0,0,0,1]
        width : 120
    MDTextField:
        id : submit
        hint_text: "Enter amount"
        mode: "rectangle"
        helper_text : ""
        helper_text_mode: "persistent"
        pos_hint: {'center_x': 0.7, 'center_y' : 0.7}
        size_hint_x : None
        line_color_normal : [0,0,0,1]
        line_color_focus : [0,0,0,1]
        text_color_normal : [0,0,0,1]
        text_color_focus : [0,0,0,1]
        width : 120
     
    MDRectangleFlatButton:
        text : "Next ->"
        pos_hint :{'center_x' :0.73, 'center_y': 0.2}
        text_color :(0,0,0)
        font_style: "Body1"
        #on_release : self.show_data
        on_press : root.manager.current = 'four'
<FourScreen>:
    name : 'four'
    MDLabel:
        text: "Budget: 3500  ₹ "
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: (0, 0, 0)
        size_hint: (1, 0.01)
        font_style: 'H6'
        pos_hint: {'center_x': 0.35, 'center_y': 0.95}

        
    MDIconButton:
        icon: "pen"
        size_hint: (1, 0.01)
        font_style: 'H6'
        pos_hint: {'center_x': 0.25, 'center_y': 0.85}
        md_bg_colour : 1,1,1
        
    MDTextField:
        id : submit
        hint_text: "Food"
        pos_hint: {'center_x': 0.25, 'center_y' : 0.7}
        size_hint_x : None
        line_color_normal : [0,0,0,1]
        line_color_focus : [0,0,0,1]
        text_color_normal : [0,0,0,1]
        text_color_focus : [0,0,0,1]
        width : 120
    MDTextField:
        id : submit
        hint_text: "500"
        mode: "rectangle"
        helper_text : ""
        helper_text_mode: "persistent"
        pos_hint: {'center_x': 0.65, 'center_y' : 0.7}
        size_hint_x : None
        line_color_normal : [0,0,0,1]
        line_color_focus : [0,0,0,1]
        text_color_normal : [0,0,0,1]
        text_color_focus : [0,0,0,1]
        width : 120
    MDRectangleFlatButton:
        text : "Exit"
        pos_hint :{'center_x' :0.5, 'center_y': 0.2}
        text_color :(0,0,0)
        font_style: "Body1"
        #on_release : self.show_data
        on_press : root.manager.current = 'third'
        
    
       

    
   
"""


#class first screen

class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    #pass
    def press(self):
        self.root.get_screen('third').ids.date_label.text = str(self.ids.amount.text)
        #MDApp.get_running_app().root.third.ids.showrupee.text = self.ids.amount.text# show live amt hereeeeeeeeeeeeeeeeeeeeeee
        #MDApp.get_running_app().root.ids.screen_manager.get_screen("screen3").ids.my_id
class WorkScreen(Screen):
    pass

class FourScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(FirstScreen(name='Intro'))
sm.add_widget(SecondScreen(name='second'))
sm.add_widget(WorkScreen(name='third'))
sm.add_widget(WorkScreen(name='four'))

class Expense_Tracker(MDApp):

    def build(self):
        screen = Screen()#img = Image(source="money_edited.jpg", size_hint=(0.65, 0.9),
         #           pos_hint={'center_x': 0.5, 'center_y': 0.5})
        username = StringProperty()
        self.root = Builder.load_string(screen_helper)
        return self.root

#Date Picker
    def on_save(self,instance,value,date_range):
       print(instance,value,date_range)
       self.root.get_screen('third').ids.date_label.text = str(value)

    def on_cancel(self,instance,value):
        self.root.ids.date_label.text = "cancel"

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.open()
        date_dialog.bind(on_save = self.on_save, on_cancel = self.on_cancel)


#dropdown
    # to store username and amount
    def show_data(self):

       username = self.root.get_screen('second').ids.submit.text
       amount = self.root.get_screen('second').ids.amount.text
       print(username, amount)

Expense_Tracker().run()