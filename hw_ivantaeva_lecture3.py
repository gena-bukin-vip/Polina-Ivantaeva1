def convert_temperature():
    meaning = input("Введите температуру (12С или 100F): ").upper()
    t, sh = float(meaning[:-1]), meaning[-1]
    
    scales = {'C': lambda t: (t * 9/5) + 32, 'F': lambda t: (t - 32) * 5/9}
    
    try:
        result = scales[sh](t) 
        
        print(f"{t:.1f}{sh} = {result:.1f}{'F' if sh == 'C' else 'C'}")
    except:
        print("Некорректный ввод.")
        
convert_temperature()