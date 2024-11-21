from colorama import Fore, Style, init

# Initialize colorama for cross-platform compatibility
init(autoreset=True)

def display_header():
    """Displays the header information."""
    print(Fore.MAGENTA + Style.BRIGHT + "\n" + "=" * 60)
    print(Fore.CYAN + "🌟  Welcome to the Data Visualizer with ASCII Charts  🌟")
    print(Fore.WHITE + "    Version: 1.0.0 | Author: NinjaXP")
    print(Fore.WHITE + "    GitHub : https://github.com/Ninja-XP")
    print(Fore.MAGENTA + "=" * 60 + Style.RESET_ALL)

def display_menu_options():
    """Displays the main menu options."""
    print(Fore.YELLOW + """
        [1] 📊  Visualize CSV as Bar Chart
        [2] 📈  Visualize JSON as Line Graph
        [3] ❌  Exit
    """)

def display_footer():
    """Displays the footer line after the menu."""
    print(Fore.MAGENTA + "=" * 60 + Style.RESET_ALL)

def display_menu():
    """Displays the full CLI menu."""
    display_header()
    display_menu_options()
    display_footer()
    choice = input(Fore.BLUE + Style.BRIGHT + "👉 Enter your choice (1-3): " + Style.RESET_ALL)
    print(Fore.MAGENTA + "\n" + "-" * 60 + Style.RESET_ALL)
    return choice
