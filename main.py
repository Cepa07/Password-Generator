import random
import string

def gen_password(
        length=12,            # Длина пароля
        use_digits=True,      # Использовать цифры
        use_spec_chars=True   # Использовать специальные символы
):
    
    chars = string.ascii_letters  # Набор букв верхнего и нижнего регистра
    if use_digits:
        chars += string.digits    # Добавляем цифры, если параметр use_digits установлен в True
    if use_spec_chars:
        chars += string.punctuation  # Добавляем специальные символы, если параметр use_spec_chars установлен в True
    
    password = ''.join(
        random.choice(chars)       # Выбираем случайный символ из набора chars
        for _ in range(length)      # Генерируем символы длиной, равной заданной длине пароля
    )
    return password

password = gen_password()  # Генерируем пароль с использованием параметров по умолчанию
print(password)  # Выводим сгенерированный пароль
