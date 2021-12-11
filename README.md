# rep10

# Время выполнения filter.py :
![filter.py](https://user-images.githubusercontent.com/84004210/144651372-11a5fe63-9ba3-4700-9013-c1d2387c6a4d.png)

# Время выполнения old_filter.py :
![old_filter.py](https://user-images.githubusercontent.com/84004210/144651583-ef6c7c5d-32cc-415b-8568-7a7455514e1c.png)

Старый фильтр работает быстрее, т.к. в filter.py большая часть времени выполнения затрачивается на ввод данных пользователем.

filter_with_filename.py работает быстрее двух предыдущих, потому что по сути это filter.py (отрефакторенный old_filter.py), в котором все параметры задаются внутри функции main() (пользовательский ввод исключен)
![filter_with_filename.py](https://user-images.githubusercontent.com/84004210/144653461-a8b45213-5cd3-4ede-b7e6-5d067161148e.png)


# Первоначальное изображение:
<img src="img.jpg" width="500" />

# Результат выполнения filter.py:
* размер блока 6 и 5 градаций серого
<img src="new_imgg.jpg" width="500" />

# Результат выполнения old_filter.py:
* размер блока 10 и 50 градаций серого
<img src="res.jpg" width="500" />

# Результат выполнения filter_with_filename.py:
* размер блока 10 и 50 градаций серого
<img src="result.jpg" width="500" />

