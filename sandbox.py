"""
AP Computer Science Principles Sandbox
This is a repo you can use to store small warm-up problems and try out code.
"""

# Imports go at the top
from microbit import *




def main() -> None:
        time: list[int] = []
        display_interval: int = 3000
        record_interval: int = 57000
        recording: bool = False
        loud: float = float(0)
        import log
        log.set_labels("temperature", timestamp=log.SECONDS)
        
        
         
   
   
        while True:
            if button_a.was_pressed():
               recording = True

            if button_b.is_pressed():
               recording = False
               display.show(Image.NO)
               sleep(display_interval)
               display.clear()
            
               
           
            if recording:
                log.add({"sound" : loud})
                display.show(len
            # record
                time.append(running_time())
                
                if microphone.sound_level() > 10:
                    loud == microphone.sound_level()
                    display.show(Image.ANGRY)
                    log.add({"sound" : loud})
                display.show(len
                    
                    
                
                
                    
                
                
            sleep(3000)
            display.clear()
