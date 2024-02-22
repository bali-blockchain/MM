# Copyright (c) 2024 Anthony Seger
# Distributed under the MIT software license
# http://www.opensource.org/licenses/mit-license.php


from kivy.support import install_twisted_reactor
install_twisted_reactor()

from twisted.internet           import reactor
from twisted.internet.protocol  import Protocol, Factory
from twisted.internet.endpoints import TCP4ServerEndpoint

from kivy.config     import Config
Config.set('input', 'mouse', 'mouse, disable_multitouch')

Config.set('graphics', 'width',      '555')
Config.set('graphics', 'height',    '1024')
Config.set('graphics', 'resizable',     0 )

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.lang import Builder

from kivy.utils import get_color_from_hex as C



Builder.load_string("""
#:import C      kivy.utils.get_color_from_hex


<Coin> :

    BoxLayout:
        orientation: 'vertical'
        size: root.size
        size_hint: 1, 1

        canvas :
            Color:
                rgba: C("#000000ff")
            Rectangle:
                pos: self.pos
                size: self.size




        #  Canvas 99

        BoxLayout
            orientation: 'horizontal'
            size: root.size
            size_hint: 1.00, 0.24

            canvas :
                Color:
                    rgba: C("#000000ff")
                Rectangle:
                    pos: self.pos
                    size: self.size

            Button:
                id: mm_canvas_99
                background_normal:  './mm/mm.png'
                background_down  :  './mm/mm.png'
                background_color :  C("#000000")
                size_hint: 1, 1.18





        #  Canvas space

        BoxLayout
            orientation: 'horizontal'
            size: root.size
            size_hint: 1.00, 0.005

            canvas :
                Color:
                    rgba: C("#000000ff")
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
                    rgba: C("#ee0099ff")
                Rectangle:
                    pos: self.pos
                    size: self.size


            TextInput:
                id: _cmd_ops_
                size_hint: .7, 1
                padding_y: [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]
                padding_x: "5sp"
                font_size: '18sp'
                #color: C('#ffee00')
                bold : True
                text: ""
                markup: True
                valign: 'middle'
                background_color: C("#000000")
                foreground_color: C("#9900ff")

            Button:
                id: _cmd_btn_
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
            size_hint: 1.00, 0.005

            canvas :
                Color:
                    rgba: C("#000000ff")
                Rectangle:
                    pos: self.pos
                    size: self.size




        #  !!!!!!!!!!!!!!!!!

        #  Canvas MM Payline

        #  .................


        BoxLayout
            orientation: 'vertical'
            size: root.size
            size_hint: 1.00, 0.295

            canvas :
                Color:
                    rgba: C("#1e0000ff")
                Rectangle:
                    pos: self.pos
                    size: self.size




            # ROY Payline

            BoxLayout:
                orientation: 'horizontal'
                size_hint: 1, .03

                canvas :
                    Color:
                        rgba: C("#000000ff")
                    Rectangle:
                        pos: self.pos
                        size: self.size

                Button:
                    id: _mm_ful_colok_id_
                    size_hint: .2, 1
                    text_size: self.size
                    text: '[b]FUL = A[/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'left'
                    color: C('#000000')
                    background_color: C('#000000')


                Button:
                    id: _mm_xcoin_colok_id_
                    size_hint: .15, 1
                    text_size: self.size
                    text: '[b]x 1[/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'right'
                    color: C('#000000')
                    background_color: C('#000000')


                Button:
                    size_hint: .05, 1
                    text_size: self.size
                    text: '[b][/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'left'
                    color: C('#000000')
                    background_color: C('#000000')

                Button:
                    id: _mm_roy_symbol_id_
                    size_hint: .4, 1
                    text_size: self.size
                    text: '[b]ROYAL FLUSH[/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'left'
                    color: C('#000000')
                    background_color: C('#000000')

                Button:
                    id: _mm_roy_id_
                    size_hint: .2, 1
                    text_size: self.size
                    text: '[b]500[/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'right'
                    color: C('#000000')
                    background_color: C('#000000')





            # 5KI Payline

            BoxLayout:
                orientation: 'horizontal'
                size_hint: 1, .03

                canvas :
                    Color:
                        rgba: C("#000000ff")
                    Rectangle:
                        pos: self.pos
                        size: self.size


                Button:
                    id: _mm_credit_id_
                    size_hint: .35, 1
                    text_size: self.size
                    text: '[b]CREDIT[/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'left'
                    color: C('#000000')
                    background_color: C('#000000')

                Button:
                    size_hint: .05, 1
                    text_size: self.size
                    text: '[b][/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'left'
                    color: C('#000000')
                    background_color: C('#000000')

                Button:
                    id: _mm_5ki_symbol_id_
                    size_hint: .4, 1
                    text_size: self.size
                    text: '[b]5 OF A KIND[/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'left'
                    color: C('#000000')
                    background_color: C('#000000')

                Button:
                    id: _mm_5ki_id_
                    size_hint: .2, 1
                    text_size: self.size
                    text: '[b]200[/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'right'
                    color: C('#000000')
                    background_color: C('#000000')





            # SFL Payline

            BoxLayout:
                orientation: 'horizontal'
                size_hint: 1, .03

                canvas :
                    Color:
                        rgba: C("#000000ff")
                    Rectangle:
                        pos: self.pos
                        size: self.size


                Button:
                    id: _mm_coin_session_id_
                    size_hint: .35, 1
                    text_size: self.size
                    text: '[b]0[/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'right'
                    color: C("#000000")
                    background_color: C('#000000')

                Button:
                    size_hint: .05, 1
                    text_size: self.size
                    text: '[b][/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'left'
                    color: C('#000000')
                    background_color: C('#000000')

                Button:
                    id: _mm_sfl_symbol_id_
                    size_hint: .4, 1
                    text_size: self.size
                    text: '[b]STR FLUSH[/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'left'
                    color: C('#000000')
                    background_color: C('#000000')

                Button:
                    id: _mm_sfl_id_
                    size_hint: .2, 1
                    text_size: self.size
                    text: '[b]120[/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'right'
                    color: C('#000000')
                    background_color: C('#000000')





            # 4KI Payline

            BoxLayout:
                orientation: 'horizontal'
                size_hint: 1, .03

                canvas :
                    Color:
                        rgba: C("#000000ff")
                    Rectangle:
                        pos: self.pos
                        size: self.size


                Button:
                    id: _mm_coin_credit_id_
                    size_hint: .35, 1
                    text_size: self.size
                    text: '[b]0[/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'right'
                    color: C('#000000')
                    background_color: C('#000000')

                Button:
                    size_hint: .05, 1
                    text_size: self.size
                    text: '[b][/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'left'
                    color: C('#000000')
                    background_color: C('#000000')

                Button:
                    id: _mm_4ki_symbol_id_
                    size_hint: .4, 1
                    text_size: self.size
                    text: '[b]4 OF A KIND[/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'left'
                    color: C('#000000')
                    background_color: C('#000000')

                Button:
                    id: _mm_4ki_id_
                    size_hint: .2, 1
                    text_size: self.size
                    text: '[b]50[/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'right'
                    color: C('#000000')
                    background_color: C('#000000')




            # FUL Payline

            BoxLayout:
                orientation: 'horizontal'
                size_hint: 1, .03

                canvas :
                    Color:
                        rgba: C("#000000ff")
                    Rectangle:
                        pos: self.pos
                        size: self.size



                Button:
                    id: _mm_bonus_roy_id_
                    size_hint: .2, 1
                    text_size: self.size
                    text: '[b]10000[/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'right'
                    color: C('#000000')
                    background_color: C('#000000')

                Button:
                    id: _mm_coin_1_id_
                    size_hint: .15, 1
                    text_size: self.size
                    text: '[b]0[/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'right'
                    color: C('#000000')
                    background_color: C('#000000')

                Button:
                    size_hint: .05, 1
                    text_size: self.size
                    text: '[b][/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'left'
                    color: C('#000000')
                    background_color: C('#000000')

                Button:
                    id: _mm_ful_symbol_id_
                    size_hint: .4, 1
                    text_size: self.size
                    text: '[b]FULL HOUSE[/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'left'
                    color: C('#000000')
                    background_color: C('#000000')

                Button:
                    id: _mm_ful_id_
                    size_hint: .2, 1
                    text_size: self.size
                    text: '[b]7[/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'right'
                    color: C('#000000')
                    background_color: C('#000000')





            # FLU Payline

            BoxLayout:
                orientation: 'horizontal'
                size_hint: 1, .03

                canvas :
                    Color:
                        rgba: C("#000000ff")
                    Rectangle:
                        pos: self.pos
                        size: self.size



                Button:
                    id: _mm_bonus_5ki_id_
                    size_hint: .2, 1
                    text_size: self.size
                    text: '[b]4000[/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'right'
                    color: C('#000000')
                    background_color: C('#000000')

                Button:
                    id: _mm_coin_2_id_
                    size_hint: .15, 1
                    text_size: self.size
                    text: '[b]0[/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'right'
                    color: C('#000000')
                    background_color: C('#000000')

                Button:
                    size_hint: .05, 1
                    text_size: self.size
                    text: '[b][/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'left'
                    color: C('#000000')
                    background_color: C('#000000')

                Button:
                    id: _mm_flu_symbol_id_
                    size_hint: .4, 1
                    text_size: self.size
                    text: '[b]FLUSH[/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'left'
                    color: C('#000000')
                    background_color: C('#000000')

                Button:
                    id: _mm_flu_id_
                    size_hint: .2, 1
                    text_size: self.size
                    text: '[b]5[/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'right'
                    color: C('#000000')
                    background_color: C('#000000')





            # STR Payline

            BoxLayout:
                orientation: 'horizontal'
                size_hint: 1, .03

                canvas :
                    Color:
                        rgba: C("#000000ff")
                    Rectangle:
                        pos: self.pos
                        size: self.size




                Button:
                    id: _mm_bonus_sfl_id_
                    size_hint: .2, 1
                    text_size: self.size
                    text: '[b]2400[/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'right'
                    color: C('#000000')
                    background_color: C('#000000')

                Button:
                    id: _mm_coin_3_id_
                    size_hint: .15, 1
                    text_size: self.size
                    text: '[b]0[/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'right'
                    color: C('#000000')
                    background_color: C('#000000')

                Button:
                    size_hint: .05, 1
                    text_size: self.size
                    text: '[b][/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'left'
                    color: C('#000000')
                    background_color: C('#000000')

                Button:
                    id: _mm_str_symbol_id_
                    size_hint: .4, 1
                    text_size: self.size
                    text: '[b]STRAIGHT[/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'left'
                    color: C('#000000')
                    background_color: C('#000000')

                Button:
                    id: _mm_str_id_
                    size_hint: .2, 1
                    text_size: self.size
                    text: '[b]3[/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'right'
                    color: C('#000000')
                    background_color: C('#000000')






            # 3KI Payline

            BoxLayout:
                orientation: 'horizontal'
                size_hint: 1, .03

                canvas :
                    Color:
                        rgba: C("#000000ff")
                    Rectangle:
                        pos: self.pos
                        size: self.size



                Button:
                    id: _mm_bonus_4ki_id_
                    size_hint: .2, 1
                    text_size: self.size
                    text: '[b]1000[/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'right'
                    color: C('#000000')
                    background_color: C('#000000')

                Button:
                    id: _mm_coin_4_id_
                    size_hint: .15, 1
                    text_size: self.size
                    text: '[b]0[/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'right'
                    color: C('#000000')
                    background_color: C('#000000')

                Button:
                    size_hint: .05, 1
                    text_size: self.size
                    text: '[b][/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'left'
                    color: C('#000000')
                    background_color: C('#000000')

                Button:
                    id: _mm_3ki_symbol_id_
                    size_hint: .4, 1
                    text_size: self.size
                    text: '[b]3 OF A KIND[/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'left'
                    color: C('#000000')
                    background_color: C('#000000')

                Button:
                    id: _mm_3ki_id_
                    size_hint: .2, 1
                    text_size: self.size
                    text: '[b]2[/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'right'
                    color: C('#000000')
                    background_color: C('#000000')





            # 2KI Payline

            BoxLayout:
                orientation: 'horizontal'
                size_hint: 1, .03

                canvas :
                    Color:
                        rgba: C("#000000ff")
                    Rectangle:
                        pos: self.pos
                        size: self.size



                Button:
                    id: _mm_bonus_ful_id_
                    size_hint: .2, 1
                    text_size: self.size
                    text: '[b]3200[/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'right'
                    color: C('#000000')
                    background_color: C('#000000')

                Button:
                    size_hint: .15, 1
                    text_size: self.size
                    text: '[b][/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'center'
                    color: C('#000000')
                    background_color: C('#000000')

                Button:
                    size_hint: .05, 1
                    text_size: self.size
                    text: '[b][/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'left'
                    color: C('#000000')
                    background_color: C('#000000')

                Button:
                    id: _mm_2ki_symbol_id_
                    size_hint: .4, 1
                    text_size: self.size
                    text: '[b]2 PAIRS (J)[/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'left'
                    color: C('#000000')
                    background_color: C('#000000')

                Button:
                    id: _mm_2ki_id_
                    size_hint: .2, 1
                    text_size: self.size
                    text: '[b]1[/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'right'
                    color: C('#000000')
                    background_color: C('#000000')







            # 1KI Payline

            BoxLayout:
                orientation: 'horizontal'
                size_hint: 1, .03

                canvas :
                    Color:
                        rgba: C("#000000ff")
                    Rectangle:
                        pos: self.pos
                        size: self.size



                Button:
                    id: _mm_coin_in_id_
                    size_hint: .2, 1
                    text_size: self.size
                    text: '[b]0[/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'right'
                    color: C("#000000")
                    background_color: C('#000000')

                Button:
                    size_hint: .15, 1
                    text_size: self.size
                    text: '[b][/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'center'
                    color: C('#000000')
                    background_color: C('#000000')

                Button:
                    size_hint: .05, 1
                    text_size: self.size
                    text: '[b][/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'left'
                    color: C('#000000')
                    background_color: C('#000000')

                Button:
                    id: _mm_1ki_symbol_id_
                    size_hint: .4, 1
                    text_size: self.size
                    text: '[b]ACES PAIR[/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'left'
                    color: C('#000000')
                    background_color: C('#000000')

                Button:
                    id: _mm_1ki_id_
                    size_hint: .2, 1
                    text_size: self.size
                    text: '[b]1[/b]'
                    markup: True
                    font_size: '25sp'
                    height : "25sp"
                    valign: 'top'
                    halign: 'right'
                    color: C('#000000')
                    background_color: C('#000000')






        #  Canvas space

        BoxLayout
            orientation: 'horizontal'
            size: root.size
            size_hint: 1.00, 0.005

            canvas :
                Color:
                    rgba: C("#000000ff")
                Rectangle:
                    pos: self.pos
                    size: self.size




        #  !!!!!!!!!!!!!!!!!!!!!!

        #  Canvas MM Bola Tangkas

        #  ......................


        BoxLayout
            orientation: 'horizontal'
            size: root.size
            size_hint: 1.00, 0.340

            canvas :
                Color:
                    rgba: C("#000000ff")
                Rectangle:
                    pos: self.pos
                    size: self.size


            # card



        #  Canvas space

        BoxLayout
            orientation: 'horizontal'
            size: root.size
            size_hint: 1.00, 0.005

            canvas :
                Color:
                    rgba: C("#000000ff")
                Rectangle:
                    pos: self.pos
                    size: self.size




        #  !!!!!!!!!!!!!!!!!

        #  Canvas MM Logging

        #  .................


        BoxLayout
            orientation: 'horizontal'
            size: root.size
            size_hint: 1.00, 0.05

            canvas :
                Color:
                    rgba: C("#000008ff")
                Rectangle:
                    pos: self.pos
                    size: self.size


            # log

            Button:
                id: _mm_logging_
                size_hint: 1, 1
                text_size: self.size
                text: '[b]PLAY 1 TO 50  INSERT COIN[/b]'
                markup: True
                font_size: '25sp'
                height : "25sp"
                valign: 'middle'
                halign: 'center'
                color: C('#000000')
                background_color: C('#000000')




        #  Canvas space

        BoxLayout
            orientation: 'horizontal'
            size: root.size
            size_hint: 1.00, 0.005
            pY:  99
            pX: -999

            canvas :
                Color:
                    rgba: C("#000000ff")
                Rectangle:
                    pos: self.pos
                    size: self.size




""")




class Coin(Screen) :


    def __init__(self, **kwargs):
        super(Coin, self).__init__(**kwargs)

        # LOGGING
        self.ids._mm_logging_.color  =  C("#ffee00")
        self.ids._mm_logging_.text   = '[b]MM COIN[/b]'




class CoinApp(App) :


    def build(self) :
        self.title="Coin"
        return Coin()




    def on_start( self ) :
        return True

    def on_pause( self ) :
        return True

    def on_resume( self ) :
        return True

    def on_stop( self ) :
        return True




if __name__ == "__main__" :
    CoinApp().run()
