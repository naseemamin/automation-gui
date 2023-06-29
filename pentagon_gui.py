import time   
import pyautogui  
import subprocess   
import math

subprocess.Popen('mspaint')  
time.sleep(3)   
pyautogui.hotkey('alt', 'space')  
pyautogui.press('x')

# I want to draw in the colour purple.. 
start_x, start_y = 100, 100   
pyautogui.moveTo(start_x, start_y, duration=0.5)  
pyautogui.moveRel(1550, 30, duration=0.5)    
pyautogui.click(duration=0.2)   

screen_width, screen_height = pyautogui.size()   
center_x = screen_width // 2   
center_y = screen_height // 2
draw_x = center_x 
draw_y = center_y
pyautogui.moveTo(draw_x, draw_y, duration=0.5)  

def draw_star(center_x, center_y, outer_radius, inner_radius, num_points):
    angle = 360 / num_points
    outer_points = []
    inner_points = []

    # Calculate the outer and inner points of the star
    for i in range(num_points):
        # Outer points
        outer_x = center_x + outer_radius * math.cos(math.radians(angle * i))
        outer_y = center_y - outer_radius * math.sin(math.radians(angle * i))
        outer_points.append((outer_x, outer_y))

        # Inner points
        inner_x = center_x + inner_radius * math.cos(math.radians(angle * i + angle / 2))
        inner_y = center_y - inner_radius * math.sin(math.radians(angle * i + angle / 2))
        inner_points.append((inner_x, inner_y))

    # Drag the mouse to draw the star
    pyautogui.moveTo(outer_points[0][0], outer_points[0][1])
    for i in range(num_points):
        pyautogui.dragRel(outer_points[i][0] - inner_points[i][0],
                          outer_points[i][1] - inner_points[i][1],
                          duration=0.25)

# Example usage
draw_star(500, 500, 100, 50, 5)
