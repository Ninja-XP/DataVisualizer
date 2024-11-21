def draw_line_graph(data):
    if not data:
        print("No data to visualize.")
        return
    print("\nASCII Line Graph:")
    max_value = max(max(int(row[key]) for key in row if key != "label") for row in data)
    for level in range(max_value, 0, -10):
        line = f"{level:>4} | "
        for row in data:
            for key, value in row.items():
                if key != "label" and int(value) >= level:
                    line += "X "
                else:
                    line += "  "
        print(line)
    print("     +" + "-" * len(data) * 2)
