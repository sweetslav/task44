import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создаем пустой DataFrame для хранения one hot encoding
one_hot = pd.DataFrame()

# Проходимся по уникальным значениям в столбце 'whoAmI'
for category in data['whoAmI'].unique():
    # Создаем новый бинарный столбец для каждой категории
    one_hot[category] = (data['whoAmI'] == category).astype(int)

# Выводим первые строки преобразованного DataFrame
print(one_hot.head())
