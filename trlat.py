def strlat(strin):
    trd = {
        ' ': ' ', 
        '-': '-',
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'g',
        'д': 'd',
        'е': 'e',
        'ё': 'jo',
        'ж': 'zh',
        'з': 'z',
        'и': 'i',
        'й': 'j',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 'c',
        'т': 't',
        'у': 'u',
        'ф': 'f',
        'х': 'h',
        'ц': 'tc',
        'ч': 'ch',
        'ш': 'sh',
        'щ': 'shсh',
        'ъ': 'j',
        'ы': 'u',
        'ь': ' ',
        'э': 'e',
        'ю': 'ju',
        'я': 'ja',
        'А': 'A',
        'Б': 'B',
        'В': 'V',
        'Г': 'G',
        'Д': 'D',
        'Е': 'E',
        'Ё': 'Jo',
        'Ж': 'Zh',
        'З': 'Z',
        'И': 'I',
        'Й': 'J',
        'К': 'K',
        'Л': 'L',
        'М': 'M',
        'Н': 'N',
        'О': 'O',
        'П': 'P',
        'Р': 'R',
        'С': 'C',
        'Т': 'T',
        'У': 'U',
        'Ф': 'F',
        'Х': 'H',
        'Ц': 'Tc',
        'Ч': 'Ch',
        'Ш': 'Sh',
        'Щ': 'Shсh',
        'Ъ': ' ',
        'Ы': 'U',
        'Ь': ' ',
        'Э': 'E',
        'Ю': 'Ju',
        'Я': 'Ja'
    }
    tranout = ''
    for i in range(len(strin)):
        tranout+=trd[strin[i]]
    return tranout
print(strlat('Щеглов Цуркан Шаломович'))