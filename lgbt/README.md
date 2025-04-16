#  Rainbow TQDM - LGBT

Beautiful progress bar with rainbow colors.
In v 0.1.0 - Optimized loading for large lists.
Added the option to select a placeholder. Check the `placeholder` argument.
In v 0.2.0 - The loading strip update is even better optimized. Added new heroes :)
'rainbow': '🌈', 'unicorn':'🦄', 'teddy': '🧸', 'bunny': '🐰', 'kitten':'🐱', 'sakura':'🌸', 'heart':'🩷'

## Download
```bash
pip install lgbt
```

## Usage
```python
import time

from lgbt import lgbt

for i in lgbt(range(100)):
	time.sleep(0.1)
```
