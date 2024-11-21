import sys
from utils.cli_menu import display_menu
from charts.bar_chart import draw_bar_chart
from charts.line_graph import draw_line_graph
from utils.data_reader import read_csv, read_json

def main():
    print("Welcome to Data Visualizer with ASCII Charts")
    while True:
        choice = display_menu()
        if choice == "1":
            file_path = input("Enter the CSV file path: ")
            data = read_csv(file_path)
            draw_bar_chart(data)
        elif choice == "2":
            file_path = input("Enter the JSON file path: ")
            data = read_json(file_path)
            draw_line_graph(data)
        elif choice == "3":
            print("Thanks for using!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
