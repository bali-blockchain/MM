// Copyright (c) 2024 Anthony Seger
// Distributed under the MIT software license
// http://www.opensource.org/licenses/mit-license.php




from kivy.support import install_twisted_reactor
install_twisted_reactor()

from twisted.internet           import reactor
from twisted.internet.protocol  import Protocol, Factory
from twisted.internet.endpoints import TCP4ServerEndpoint

from kivy.config     import Config
Config.set('input', 'mouse', 'mouse, disable_multitouch')

Config.set('graphics',  'width',    '555')
Config.set('graphics',  'height',   '999')
Config.set('graphics',  'resizable',   0 )

from kivy.app        import App
from kivy.properties import StringProperty
from kivy.graphics   import Color, Rectangle
from kivy.clock      import Clock
from kivy.uix.popup  import Popup
from kivy.lang       import Builder

from kivy.uix.screenmanager import Screen




Builder.load_string("""
#:import C kivy.utils.get_color_from_hex

<Core> :

    BoxLayout:
        orientation: 'vertical'
        size: root.size
        size_hint: 1, 1

        canvas :
            Color:
                rgba: C("#000000")
            Rectangle:
                pos: self.pos
                size: self.size




        #  Canvas space

        BoxLayout
            orientation: 'horizontal'
            size: root.size
            size_hint: 1.00, 0.01

            canvas :
                Color:
                    rgba: C("#000000")
                Rectangle:
                    pos: self.pos
                    size: self.size


        #  Canvas 99

        BoxLayout
            orientation: 'horizontal'
            size: root.size
            size_hint: 1, 0.24

            canvas :
                Color:
                    rgba: C("#000000ff")
                Rectangle:
                    pos: self.pos
                    size: self.size


            ScrollView:
                id: _server_scroller_
                size_hint: 1, 1
                minimum_height: _server_scroller_.setter('height')
                bar_width: '12dp'
                bar_color: [ 0.999, 0.068, 0.638, 0.18 ]
                bar_inactive_color: [ 0.999, 0.068, 0.638, 0.68 ]
                scroll_type: ['bars','content']
                do_scroll_x: False

                canvas.before:
                    Color:
                        rgba: C("#1e0000ff")
                    Rectangle:
                        pos: self.pos
                        size: self.size

                Label:
                    id: _server_cli_
                    size_hint_y: None
                    size: self.texture_size
                    height: self.texture_size[1]
                    text_size: root.width, None
                    font_size: '10sp'
                    padding_x: '10sp'
                    color: C('#ffeebb')
                    text: root._s_
                    valign: 'top'



        #  Canvas space

        BoxLayout
            orientation: 'horizontal'
            size: root.size
            size_hint: 1.00, 0.01

            canvas :
                Color:
                    rgba: C("#000000")
                Rectangle:
                    pos: self.pos
                    size: self.size



        #  Canvas submit

        BoxLayout
            orientation: 'horizontal'
            size: root.size
            size_hint: 1.00, 0.05

            canvas :
                Color:
                    rgba: C("#ee0099")
                Rectangle:
                    pos: self.pos
                    size: self.size


            TextInput:
                id: _cmd_ops_
                size_hint: .7, 1
                padding_y: [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]
                padding_x: "5sp"
                #padding: "10sp"
                font_size: '18sp'
                #color: C('#ffee00')
                bold : True
                text: ""
                markup: True
                valign: 'middle'
                background_color: C("#000000")
                foreground_color: C("#9900ff")

            Button:
                id: _mm_cmd_btn_
                size_hint: 0.3, 1
                text: '[b]submit[/b]'
                markup: True
                font_size: '18sp'
                valign: 'top'
                halign: 'center'
                color: C('#ffee38')
                background_color: C('#000000')
                on_press: root.on_cmd(_cmd_ops_.text)




        #  Canvas space

        BoxLayout
            orientation: 'horizontal'
            size: root.size
            size_hint: 1.00, 0.01

            canvas :
                Color:
                    rgba: C("#000000")
                Rectangle:
                    pos: self.pos
                    size: self.size




        #  !!!!!!!!!!!!!!!!!

        #  Canvas MM Payline

        #  .................


        BoxLayout
            orientation: 'horizontal'
            size: root.size
            size_hint: 1.00, 0.69

            canvas :
                Color:
                    rgba: C("#1e0000")
                Rectangle:
                    pos: self.pos
                    size: self.size


            ScrollView:
                id: _client_scroller_
                size_hint: 1, 1
                minimum_height: _client_scroller_.setter('height')
                bar_width: '12dp'
                bar_color: [ 0.999, 0.068, 0.638, 0.18 ]
                bar_inactive_color: [ 0.999, 0.068, 0.638, 0.68 ]
                scroll_type: ['bars','content']
                do_scroll_x: False

                canvas.before:
                    Color:
                        rgba: C("#1e0000ff")
                    Rectangle:
                        pos: self.pos
                        size: self.size

                Label:
                    id: _client_cli_
                    size_hint_y: None
                    size: self.texture_size
                    height: self.texture_size[1]
                    text_size: root.width, None
                    font_size: '10sp'
                    padding_x: '10sp'
                    color: C('#ffeebb')
                    text: root._c_
                    valign: 'top'





        #  Canvas space

        BoxLayout
            orientation: 'horizontal'
            size: root.size
            size_hint: 1.00, 0.01

            canvas :
                Color:
                    rgba: C("#000000")
                Rectangle:
                    pos: self.pos
                    size: self.size

""")




class Core(Screen) :

    _s_ = StringProperty('')
    _c_ = StringProperty('')




    def __init__(self, **kwargs):
        super(Core, self).__init__(**kwargs)


    def on_cmd(self, _cmd_) :
        self.ids._cmd_ops_.text = ""
        _cmd_ops_ = _cmd_.split(' ')




        if _cmd_ops_[0] == '//font':
            try:
                self._s_  = ''
                self._c_  = ''

                self.ids._server_cli_.font_size =  '15sp'
                self.ids._client_cli_.font_size =  '15sp'

                self._s_  =  str("event:server")
                self._c_  =  str("event:client")
            except Exception as e :
                self._s_  =  str(e)




class CoreApp(App) :


    def build(self) :
        self.title="Core"
        return Core()




    def on_start( self ) :
        return True

    def on_pause( self ) :
        return True

    def on_resume( self ) :
        return True


    def on_stop( self ) :
        return True




if __name__ == "__main__" :
    CoreApp().run()



