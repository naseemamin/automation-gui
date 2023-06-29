import time   # importing time module 
import pyautogui   # importing pyautogui module 
import subprocess   # importing subprocess module 

subprocess.Popen('mspaint')  # automatically open MS Paint
time.sleep(3)   # pause script to let Paint open 
pyautogui.hotkey('alt', 'space') # this should make paint full screen 
pyautogui.press('x')

# I want to draw in the colour purple.. 
start_x, start_y = 100, 100   # setting start position of cursor at top of screen in line with colour pallete
pyautogui.moveTo(start_x, start_y, duration=0.5)   # moving cursor to this start point 
pyautogui.moveRel(1550, 30, duration=0.5)  # move's cursor to purple colour, 
   # this might be different on your screen resolution, change numbers to reflect / change colour choice
pyautogui.click(duration=0.2)   # automatically click on colour purple


screen_width, screen_height = pyautogui.size()   # automatically get screen dimensions

center_x = screen_width // 2   # calculate the center of the screen
center_y = screen_height // 2

draw_x = center_x  # setting start position of the mouse cursor
draw_y = center_y

pyautogui.moveTo(draw_x, draw_y, duration=0.5)   # moving cursor to start at center of screen 

distance = 350   # setting distance of 350
while distance > 0:   
    pyautogui.dragRel(distance, 0, duration=0.2)   # move the cursor to the right 350 pixels, for 2 seconds
    distance = distance - 5   # changing the distance to decrease by 5 
    pyautogui.dragRel(0, distance, duration=0.2)   # move the cursor down 
    pyautogui.dragRel(-distance, 0, duration=0.2)  # move the cursor left 
    distance = distance - 5   # changing the distance to dcrease by 5 again
    pyautogui.dragRel(0, -distance, duration=0.2)  # move up

   
pyautogui.moveTo(start_x, start_y, duration=0.5)   # move the cursor back to the start position 
   
# could add here automatically saving the drawing..??        
time.sleep(3)   # pause to enable manual saving of the drawing 

subprocess.Popen('taskkill /im mspaint.exe /f')   # end script by closing MS Paint
