def draw_bar_chart(data):
    if not data:
        print("No data to visualize.")
        return
    print("\nASCII Bar Chart:")
    for row in data:
        for key, value in row.items():
            if key != "label":  # Assuming "label" is a column for row labels
                print(f"{row['label']} - {key}: {'#' * int(value)}")
