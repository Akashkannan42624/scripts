import os
import random
from datetime import datetime 

# it uses `feh`  to get random walls from a folder containing wallpapers by time.
# working directory for me is:  (w_dir)
# ~/Pictures/BetterWallpaperByTime
# w_dir/Dark-themes
# w_dir/Light-themes
# w_dir/Mountain_nature_kinda/Mountain_dark
# w_dir/Mountain_nature_kinda/Mountain_light
# w_dir/Mountain_nature_kinda/mountain_sunset
# you can prefer mountain or normal ones 
# mostly mountain ones are prefered by me.
# so get random.random()
# if random.random() > 0.6 then normal theme
# otherwise mountain ones.

# Algorithm
now=datetime.now()
hour=int(now.strftime('%H'))
ran=random.random()
if ran > 0.6:
	theme='N'
else:
	theme='M'

default_w_dir = "~/Pictures/BetterWallpaperByTime/"
command = f"feh --randomize --bg-fill "

if 0 <= hour < 6:
	if theme == 'N':
		path_to_image = f'{default_w_dir}Dark-themes/'
		os.system(f'{command} {path_to_image}')		
		print(hour)
	if theme == 'M':
		path_to_image = f'{default_w_dir}Mountain_nature_kinda/Mountain_dark'
		os.system(f'{command} {path_to_image}')		
		print(hour)
if 6 <= hour < 18:
	if theme == 'N':
		path_to_image = f'{default_w_dir}Light-themes'
		os.system(f'{command} {path_to_image}')		
		print(hour)
	if theme == 'M':
		path_to_image = f'{default_w_dir}Mountain_nature_kinda/Mountain_light'
		os.system(f'{command} {path_to_image}')		
		print(hour)
if 18 <= hour < 20:
	if theme == 'N':
		path_to_image = f'{default_w_dir}Light-themes'
		os.system(f'{command} {path_to_image}')		
		print(hour)
	if theme == 'M':
		path_to_image = f'{default_w_dir}Mountain_nature_kinda/mountain_sunset'
		os.system(f'{command} {path_to_image}')		
		print(hour)
if 20 <= hour < 24:
	if theme == 'N':
		path_to_image = f'{default_w_dir}Dark-themes/'
		os.system(f'{command} {path_to_image}')		
		print(hour)
	if theme == 'M':
		path_to_image = f'{default_w_dir}Mountain_nature_kinda/Mountain_dark'
		os.system(f'{command} {path_to_image}')		
		print(hour)
