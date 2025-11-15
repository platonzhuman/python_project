import pandas as pd
import os

# ====== 1. Пути к файлам ======
# Получаем текущую папку где лежит скрипт
current_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_dir, 'task2.xlsx')  # файл в той же папке
output_path = os.path.join(current_dir, 'homework_result.xlsx')

print(f"Ищу файл по пути: {input_path}")
print(f"Файл существует: {os.path.exists(input_path)}")

# ====== 2. Чтение данных ======
df = pd.read_excel(input_path)



# ====== 3. Подготовка возрастной группы ======
df['Возраст'] = pd.to_numeric(df['Возраст'], errors='coerce')
df = df[df['Возраст'].notna()]

# Берём только возраст 18–35
df = df[(df['Возраст'] >= 18) & (df['Возраст'] <= 35)]

df['age_group'] = pd.cut(
    df['Возраст'],
    bins=[17, 24, 35],
    labels=['18-24', '25-35'],
    include_lowest=True
)


# ====== 4. Сводная таблица по профессиональной активности ======
# Колонки 8–12 (индексы в Excel начинаются с 0)
prof_cols = df.columns[8:13]

pivot_prof = df.groupby('age_group')[prof_cols].mean()


# ====== 5. Сводная таблица по мероприятиям ======
# Колонки осведомлённости (13,15,17,19,21)
event_cols = [df.columns[i] for i in [13, 15, 17, 19, 21]]

# Считаем количество каждого варианта ответа
event_counts = df[event_cols].apply(lambda x: x.value_counts())


# ====== 6. Сохраняем результат в Excel ======
with pd.ExcelWriter(output_path) as writer:
    pivot_prof.to_excel(writer, sheet_name='ProfActivity')
    event_counts.to_excel(writer, sheet_name='Events')

print("Готово! Файл сохранён как:", output_path)