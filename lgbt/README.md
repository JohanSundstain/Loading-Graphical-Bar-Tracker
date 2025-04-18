# 🌈 Rainbow TQDM - LGBT (Loading Graphical Bar Tracker)
> ⚠️ **Disclaimer**  
> This is not propaganda. Any resemblance to real abbreviations or symbols is purely coincidental.

### GitHub 🔗[Rainbow TQDM](https://github.com/JohanSundstain/Rainbow-TQDM/tree/master/lgbt)

Beautiful progress bar with rainbow colors.
In v 0.1.0 - Optimized loading for large lists.
Added the option to select a placeholder. Check the `placeholder` argument.
In v 0.2.0 - The loading strip update is even better optimized. Added new heroes :)
1. 'rainbow': '🌈', 
2. 'unicorn':'🦄', 
3. 'teddy': '🧸', 
4. 'bunny': '🐰', 
5. 'kitten':'🐱', 
6. 'sakura':'🌸', 
7. 'heart':'🩷'

### 🧠 BIG UPDATE 1.0.0
This program has been refactored using Object-Oriented Programming (OOP) principles. The `update` function now includes manual control over the download progress bar, with added parameters `total` and `mode`, but `placeholder` was deleted. Additionally, flags of various countries can be used as visual indicators in the loading bar.

### 🌍 Available 21 Flags for `mode` argument
1. Russian Federation (rus)
2. USSR (ussr)
3. Russian Empire (rue)
4. USA (usa)
5. China (chn)
6. Italy (ita)
7. France (fra)
8. Germany (deu)
9. Sweden (swe)
10. Finland (fin)
11. Norway (nor)
12. England (eng)
13. Denmark (dnk)
14. Canada (can)
15. Japan (jpn)
16. Turkey (tur)
17. Spain (esp)
18. Mexico (mex)
19. Kazakhstan (kaz)
20. Israel (isr)
21. India (ind)

### Available new emoji

1. 'gonechar':'🐝',
2. 'tralalero':'🦈',
3. 'crocodillo': '🐊',
4. 'tumtumtum': '🗿',
5. 'shimpanzini': '🍌',
6. 'trippi':'🦐',
7. 'goozinni':'🪿'


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

# With update
bar = lgbt(total=100) # Necessary argument

for i in range(100):
	time.sleep(0.1)
	bar.update(1)

```

### Some view
![Example](screenshot1.png)
