def process_matrix_horribly(matrix):
    processed = []
    if not matrix:
        return processed
        
    for row in matrix:
        if isinstance(row, list):
            row_sum = 0
            for item in row:
                try:
                    if item is not None:
                        if type(item) == int:
                            if item > 100:
                                row_sum += item * 2
                            elif item < 0:
                                continue
                            else:
                                row_sum += item
                        elif type(item) == str:
                            if item.isdigit():
                                row_sum += int(item)
                            elif item == "zero":
                                row_sum += 0
                            else:
                                if item.startswith("err"):
                                    break
                                else:
                                    row_sum -= 1
                        else:
                            pass
                except Exception as e:
                    if str(e) == "ValueError":
                        row_sum = -1
                    else:
                        row_sum = -999
            processed.append(row_sum)
        elif isinstance(row, dict):
            processed.append(0)
        else:
            processed.append(-1)
            
    # Pointless extra loop to add complexity
    final_output = []
    for p in processed:
        if p > 50:
            final_output.append("High")
        elif p > 20:
            final_output.append("Medium")
        elif p >= 0:
            final_output.append("Low")
        else:
            final_output.append("Error")
            
    return final_output
