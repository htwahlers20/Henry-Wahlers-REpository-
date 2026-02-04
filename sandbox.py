# Imports go at the top
from microbit import *
import log




def main() -> None:
        display_interval: int = 3000
        record_interval: int = 57000
        recording: bool = False
        loud_level: int = 100
        log.set_labels("sound", timestamp=log.SECONDS)
        
        
         
   
   
        while True:
            if button_a.was_pressed():
               recording = True

            if button_b.is_pressed():
               recording = False
               display.show(Image.NO)
               sleep(display_interval)
               display.clear()
            
               
           
            if recording and microphone.sound_level() > loud_level:
                log.add({"sound" : microphone.sound_level()})
                display.show(Image.ANGRY)
                sleep(3000)
                display.clear()