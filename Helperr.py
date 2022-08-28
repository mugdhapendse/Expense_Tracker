screen_helper = """
ScreenManager:
    FirstScreen:
        id: screen1
    SecondScreen:
        id: screen2
    ThirdScreen:
        id:screen_work

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
        on_release: root.press()


    MDRectangleFlatButton:
        text : "Next ->"
        pos_hint :{'center_x' :0.73, 'center_y': 0.2}
        text_color :(0,0,0)
        font_style: "Body1"
        on_release : self.show_data
        on_press : root.manager.current = 'third'
        
<ThirdScreen>:
    name: 'third'
    MDLabel:
        id: showrupee
        text: ""
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: (0, 0, 0)
        size_hint: (1, 0.01)
        font_style: 'H6'
        pos_hint: {'center_x': 0.5, 'center_y': 0.95}

    MDLabel:
        text: "Budget:"
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: (0, 0, 0)
        size_hint: (1, 0.01)
        font_style: 'H6'
        pos_hint: {'center_x': 0.2, 'center_y': 0.95}
    MDLabel:
        text: "₹"
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: (0, 0, 0)
        size_hint: (1, 0.01)
        font_style: 'H6'
        pos_hint: {'center_x': 0.65, 'center_y': 0.95}

    MDLabel:
        text: "Date :"
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: (0, 0, 0)
        size_hint: (1, 0.01)
        font_style: 'H6'
        pos_hint: {'center_x': 0.17, 'center_y': 0.9}
    
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        text_color: (0, 0, 0)
        font_style: "Body1"
        on_release: root.manager.current = 'second'
        
    MDFloatingActionButton:
        icon: "calendar"
        pos_hint: {'center_x': 0.85, 'center_y': 0.9}
        text_color: (0, 0, 0)
        size_hint: (45, 45)
        font_style: "Body1"
        md_bg_color: 1, 1, 1
        on_release: app.show_date_picker()
    MDIconButton:
        id: tryy
        icon: "plus"
        pos_hint: {'center_x': 0.3, 'center_y': 0.85}
        md_bg_color: 1, 1, 1
        on_release: root.dropdown()

    MDDropDownItem:
        id: drop_item
        pos_hint: {'center_x': 0.3, 'center_y': 0.85}
        text: 'Food'
    
    MDLabel:
        id: date_label
        halign: "center"
        text: ""
        pos_hint: {'center_x': 0.45, 'center_y': 0.9}
"""


   

    
   

















