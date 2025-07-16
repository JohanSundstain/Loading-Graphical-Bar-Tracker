# Loading Graphical Bar Tracker
> **Disclaimer**  
> This is not propaganda. Any resemblance to real abbreviations or symbols is purely coincidental.

 
## `lgbt`- Beautiful progress bar with rainbow colors and other ways to customize the appearance

## Update news 2.3.2
- Optimized the console output method
- Removed some progress bar mods 
- Fixed minor errors and bugs.

## Download
```bash
pip install lgbt
```

## Usage
### The standard way
```python
from lgbt import lgbt

for i in lgbt(range(1000000)):
	pass
```
![GIF](https://github.com/JohanSundstain/Loading-Graphical-Bar-Tracker/blob/release/media/standard_use.gif?raw=true)

### With update
```python
from lgbt import lgbt

# total is necessary argument
bar = lgbt(total=1000) 
for i in range(1000):
	bar.update(1)
```
![GIF](https://github.com/JohanSundstain/Loading-Graphical-Bar-Tracker/blob/release/media/update_use.gif?raw=true)

### Advanced mode
```python
import time
from math import cos

from lgbt import lgbt

# returns a special type for monitoring values
tracker = lgbt.tracker()
x = 0.0
dx = 0.2

for i in lgbt(range(1000), desc="Cosinus", tracker=tracker, max_value=1.0):
	# property item for change value of the current bar
	tracker.item = cos(x)
	x += dx
	# static method to move to the next bar
	lgbt.step(tracker)
	time.sleep(0.1)
```
![GIF](https://github.com/JohanSundstain/Loading-Graphical-Bar-Tracker/blob/release/media/advanced_use.gif?raw=true)

## Possible parameters
### Without tracker
```python
from lgbt import lgbt

lgbt(iterable, total, desc, mode, miniter, mininterval, hero)
```
- `iterable` -  An iterable object or generator.
- `total` - The number of elements in the iterable, if not specified, is the length of the iterable.
- `desc` - Description in front of the progress bar.
- `mode` - Customizing the progress bar. To see which modes are available, use `lgbt.modes()`. Default `='white'`.
- `miniter` - Minimum number of iterations between renders. Default `=2500`. 
- `mininterval` - Minimum time between renderings. Default `=0.1`.
- `hero` - Customization of the description string (emoji). To view all available options, use `lgbt.heroes()`. Default `='rainbow'`

### With tracker
All previous parameters work with the tracker, but new ones are also added.
```python
from lgbt import lgbt

lgbt(..., tracker, desc_hist, fix, max_value)
```
- `tracker` - A special type of container for a value that is displayed in the bars of a histogram.
- `desc_hist` - The description line for the table caption.
- `fix` - A Boolean value that controls the auto-scaling of the histogram. Default `=True`.
- `max_value` - The maximum absolute starting value for the histogram, if `fix=False` can be changed. Default `=0.5`

### About tracker
Tracker is a class with an item property that allows you to change the value of the current bar in the histogram. To move to the next bar, use `lgbt.step(tracker)`
