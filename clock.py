from __future__ import division

from kivy.app import App
from kivy.uix.widget import Widget
from kivy import Config
Config.set('graphics', 'multisamples', '0')

class show(Widget):
    def angle(self, instance):
        hr = int(self.hour.text)
        min = int(self.min.text)
        if hr >= 12:
          hr = hr - 12
        if min == 0:
          hrm = hr * 5
        else:
          first = float(hr*5)
          second = float(min/12)
          hrm = first + second
        if min > hrm:
           diff = min - hrm
           if diff > 30:
               diff = 60 - diff
           self.ans.text = str(round(float(diff * 6),2))
        elif min < hrm:
          diff = hrm - min
          if diff > 30:
            diff = 60 - diff
          self.ans.text = str(round(float(diff * 6),2))
        else:
            self.ans.text = "0.0"


class ClockApp(App):
    def build(self):
        return show()
if __name__ == '__main__':
    ClockApp().run()


