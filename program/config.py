# Simulation config
ticks_per_second = 60
windowed_screen_size = (1280, 720)
fullscreen_screen_size = (1500, 900) #(1920, 1080)

# Block config
block_size = 100
block_text_color = (200,200,200)
block_color = (25, 25, 25)
block_heghlight_color = (150,150,255)
block_char_limit = 5
font_size = 40
title_color = (200,200,200)
title_font_size = 50

# Boards config
title_height = 40
board_offset = 20
block_spacing = 20
blocks_width = 8

# Hover on block config
hover_color = (120,120,200)
hover_text_color = (0,0,0)
hover_font_size = 40
hover_height = block_size * 1.5
hover_border_size = 15

# Globals config
globals_height = 600

# ShowCode config
showCode_width = 450
showCode_font_size = 50
showCode_plain = (210,210,250)
showCode_colored = (150,50,200)

# Action config
action_tick_time = 1*ticks_per_second
action_delay = .5*ticks_per_second
change_color = (50,50,255)
add_color = (50, 255, 0)
mul_color = (100, 255, 0)
div_color = (150, 255, 0)

# Loading queue config
queue_file_name = 'queue.txt'

# Code Editor config
editor_width = 880
editor_height = 860
editor_offset_x = 1000
editor_offset_y = 40
editor_font_size = 30

# Button config
button_font_size = 40
button_width = 200
button_height = 80
button_color = (150,0,150)
button_text_color = (0, 0, 0)
button_text_offset_x = 10
button_text_offset_y = 10
button_paused_color = (160, 50, 50)
button_pressed_color = (100, 0, 100)
button_pressed_color_ticks = 4

# Errors config
error_title_color = (250, 50, 50)
error_color=(250, 50, 50)
error_font_size = 40
error_line_height = 50
error_width_limit = editor_offset_x - board_offset*2