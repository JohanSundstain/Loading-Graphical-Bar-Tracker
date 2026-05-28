# Loading Graphical Bar Tracker
> **Disclaimer**  
> This is not propaganda. Any resemblance to real abbreviations or symbols is purely coincidental.

 
## `lgbt`- Красочный прогресс бар для Python

## Новости обновления 3.0.1
- Улучшена производительность
- Удален Advanced progress bar и все зависимости
- Удалены Heroes, теперь передача идёт напрямую через `desc`
- Добавлен аргумент `fixed` с параметрами [True, False](по умолчанию False), для фиксации прогресс бара на месте

## Установка
```bash
pip install lgbt
```

## Использование
### Обычный способ
```python
from lgbt import lgbt

for i in lgbt(range(1000000)):
	pass
```
![GIF](https://github.com/JohanSundstain/Loading-Graphical-Bar-Tracker/blob/release/media/standard_use.gif?raw=true)

### С использованием update
```python
from lgbt import lgbt

# total is necessary argument
bar = lgbt(total=1000) 
for i in range(1000):
	bar.update(1)
```
![GIF](https://github.com/JohanSundstain/Loading-Graphical-Bar-Tracker/blob/release/media/update_use.gif?raw=true)

## Доступные параметры
```python
from lgbt import lgbt

lgbt(iterable, total, desc, mode, miniter, mininterval)
```
- `iterable` - Итерируемый объект или генератор.
- `total` - Число элементов в коллекции, если не указано, пытается посчитать кол-во элементов в коллекции.
- `desc` - Описание перед прогресс баром.
- `mode` - Возможные кастомизации, посмотреть все можно через метод `lgbt.modes()`. По умолчанию `='rainbow'`.
- `miniter` - Минимальное число итераций между отрисовками, По умолчанию `=2500`. 
- `mininterval` - Минимальное время между отрисовками. По умолчанию `=0.1`.