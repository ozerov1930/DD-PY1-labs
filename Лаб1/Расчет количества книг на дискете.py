# TODO Найдите количество книг, которое можно разместить на дискете
a = 100*50*25*4  # Найдем вес книги в байтах
b = a/1024**2  # Найдем вес книги в мегабайтах
quant = 1.44 // b  # Найдем, сколько книг поместится, используя целлочисленное деление

print("Количество книг, помещающихся на дискету:", quant)
