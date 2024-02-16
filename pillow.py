from PIL import Image, ImageDraw, ImageFont

# Создаем новое изображение размером 800x600 пикселей
image = Image.new('RGB', (800, 600), 'black')

# Загружаем изображение кота
cat_image = Image.open('cat.jpg')
# Сжимаем изображение кота до размера 200x200 пикселей
cat_image = cat_image.resize((200, 200))

# Отрисовываем загруженное изображение кота на фоне (в центре)
image.paste(cat_image, (300, 200))

# Загружаем шрифт для текста
font = ImageFont.truetype("arial.ttf", 36)
draw = ImageDraw.Draw(image)

# Добавляем текст "Кот на Луне" на изображение
draw.text((300, 20), "Кот на Луне", font=font, fill='white')

# Сохраняем изображение
image.save('cat_on_moon.jpg')
