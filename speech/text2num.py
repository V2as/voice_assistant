def convert_text_to_number(text):
    text = text.lower()
    numbers = {
        'один': 1,
        'два': 2,
        'две': 2,
        'три': 3,
        'четыре': 4,
        'пять': 5,
        'шесть': 6,
        'семь': 7,
        'восемь': 8,
        'девять': 9,
        'десять': 10,
        'одиннадцать': 11,
        'двенадцать': 12,
        'тринадцать': 13,
        'четырнадцать': 14,
        'пятнадцать': 15,
        'шестнадцать': 16,
        'семнадцать': 17,
        'восемнадцать': 18,
        'девятнадцать': 19,
        'двадцать': 20,
        'тридцать': 30,
        'сорок': 40,
        'пятьдесят': 50,
        'шестьдесят': 60,
        'семьдесят': 70,
        'восемьдесят': 80,
        'девяносто': 90,
        'сто': 100,
        'двести': 200,
        'триста': 300,
        'четыреста': 400,
        'пятьсот': 500,
        'шестьсот': 600,
        'семьсот': 700,
        'восемьсот': 800,
        'девятьсот': 900,
        'тысяча': 1000,
        'тысячи': 1000,
        'миллион': 1000000,
        'миллиард': 1000000000
    }

    number_parts = text.split()
    result = 0
    temp_result = 0
    for part in number_parts:
        if part not in numbers:
            return None
        else:
            num = numbers[part]
            if num >= 1000:
                if temp_result == 0:
                    temp_result = 1
                temp_result *= num
                result += temp_result
                temp_result = 0
            elif num >= 100:
                temp_result += num
            else:
                temp_result += num
    result += temp_result
    return result

def after(sentenece):
    index = sentenece.find("через")
    if index != -1:
        print(sentenece[index + len("через"):])
    else:
        print("Значение 'через' не найдено в строке.")