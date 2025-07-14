# Loading Graphical Bar Tracker
> ⚠️ **Disclaimer**  
> This is not propaganda. Any resemblance to real abbreviations or symbols is purely coincidental.

 
lgbt - Beautiful progress bar with rainbow colors and other ways to customize the appearance

## Download
```bash
pip install lgbt
```

## Usage
```python
from lgbt import lgbt

for i in lgbt(range(100)):
	pass

# With update
bar = lgbt(total=100) # Necessary argument

for i in range(100):
	time.sleep(0.1)
	bar.update(1)

```