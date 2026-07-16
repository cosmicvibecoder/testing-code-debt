def very_complex_function(data):
    result = 0
    if data:
        if isinstance(data, list):
            for item in data:
                if item > 10:
                    result += 1
                elif item < 0:
                    if item == -5:
                        result -= 5
                    else:
                        result -= 1
                else:
                    result += 0
        elif isinstance(data, dict):
            for key, value in data.items():
                if key == "add":
                    if value > 0:
                        result += value
                    elif value < 0:
                        if value == -10:
                            result += 100
                        else:
                            result -= value
                elif key == "sub":
                    if value > 0:
                        result -= value
                    else:
                        result += value
        else:
            if data == 42:
                result = 42
            elif data == 0:
                result = 0
            elif data == 1:
                result = 1
            else:
                result = -1
    else:
        if data is None:
            result = -99
        elif data == "":
            result = -98
        else:
            result = -97
            
    while result < 100:
        if result % 2 == 0:
            result += 3
        else:
            result += 5
            if result > 50:
                result += 10
                if result > 80:
                    break
    return result
