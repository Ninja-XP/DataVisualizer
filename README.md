# Data Visualizer with ASCII Charts

![Build Status](https://img.shields.io/github/workflow/status/Ninja-XP/DataVisualizer/CI?style=flat-square&logo=github&logoColor=white&color=2bbc8a)
![Version](https://img.shields.io/github/v/release/Ninja-XP/DataVisualizer?style=flat-square&color=blue)
![License](https://img.shields.io/github/license/Ninja-XP/DataVisualizer?style=flat-square&color=brightgreen)
![Contributors](https://img.shields.io/github/contributors/Ninja-XP/DataVisualizer?style=flat-square&color=orange)
![Issues](https://img.shields.io/github/issues/Ninja-XP/DataVisualizer?style=flat-square&color=red&logo=github)
![Last Commit](https://img.shields.io/github/last-commit/Ninja-XP/DataVisualizer?style=flat-square&color=purple&logo=github)
![Python Version](https://img.shields.io/pypi/pyversions/data-visualizer?style=flat-square&color=blueviolet)
![Stars](https://img.shields.io/github/stars/Ninja-XP/DataVisualizer?style=flat-square&color=gold&logo=github)
![Forks](https://img.shields.io/github/forks/Ninja-XP/DataVisualizer?style=flat-square&color=yellow&logo=github)

---

![Project Banner](https://via.placeholder.com/1200x400?text=Data+Visualizer+with+ASCII+Charts)  

🚀 **Data Visualizer with ASCII Charts** is a terminal-based tool for quick and intuitive data visualization. It supports CSV and JSON data files and generates beautiful ASCII-based bar charts and line graphs directly in your terminal.  

---

## 🌟 Features

- 📊 **CSV Data Visualization**: View data in the form of ASCII bar charts.
- 📈 **JSON Data Visualization**: Generate ASCII line graphs from JSON data.
- 💻 **Cross-Platform**: Works on Linux, macOS, and Windows (via Termux or WSL).
- 🔄 **Easy Updates**: Update the tool with a single script.
- 🛠️ **Lightweight & Fast**: No need for heavy graphical libraries.

---

## 📸 Screenshots

### Main Menu
![Main Menu Screenshot](https://via.placeholder.com/800x400?text=Main+Menu+Screenshot)

### CSV Bar Chart Visualization
![Bar Chart Screenshot](https://via.placeholder.com/800x400?text=Bar+Chart+Screenshot)

### JSON Line Graph Visualization
![Line Graph Screenshot](https://via.placeholder.com/800x400?text=Line+Graph+Screenshot)

---

## 📂 Folder Structure

```plaintext
DataVisualizer/
├── data/               # Sample data files (CSV, JSON)
├── docs/               # Documentation files
├── scripts/            # Shell scripts for setup, running, and updates
├── src/                # Main source code and modules
│   ├── charts/         # Chart visualization modules
│   ├── utils/          # Helper modules (CLI menu, data readers)
│   ├── main.py         # Entry point for the application
├── config/             # Configuration files
├── requirements.txt    # Python dependencies
├── README.md           # Project overview
```
---

## 🚀 Getting Started

### Prerequisites

Ensure the following tools are installed on your system:

  - Python 3.7 or later
  - pip (Python package manager)
  - Git

### Installation

1. Clone the repository:
  
    ```bash
    git clone https://github.com/Ninja-XP/DataVisualizer.git
    cd DataVisualizer
    ```

2. Install dependencies:

    ```bash
    bash scripts/install_dependencies.sh
    ```

3. Run the tool:

    ```bash
    bash scripts/run_visualizer.sh
    ```

4. Update the tool:

    ```bash
    bash scripts/update_tool.sh
    ```
---

## 🎮 Usage

When you run the tool, you’ll see a menu like this:

```
============================================================
🌟  Welcome to the Data Visualizer with ASCII Charts  🌟
    Version: 1.0.0 | Author: NinjaXP
    GitHub : https://github.com/Ninja-XP
============================================================

        [1] 📊  Visualize CSV as Bar Chart
        [2] 📈  Visualize JSON as Line Graph
        [3] ❌  Exit

============================================================
👉 Enter your choice (1-3):

```

1. Select an option (e.g., `[1]`` for CSV bar charts).

2. Provide the path to your data file (e.g., `data/sample_data.csv`).

3. View the ASCII chart output in the terminal.

---

## 📖 Documentation

- User Guide: Step-by-step instructions for using the tool.

- Developer Guide: Information for contributors and developers.

---

## 🙌 Contributors

Thanks to the following people who have contributed to this project:  

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Ninja-XP">
        <img src="https://avatars.githubusercontent.com/u/189180265?v=4" width="100px;" alt="NinjaXP"/>
        <br />
        <sub><b>NinjaXP</b></sub>
      </a>
      <br />
      🚀 Maintainer
    </td>
    <td align="center">
      <a href="https://github.com/YourContributor">
        <img src="https://via.placeholder.com/100" width="100px;" alt="Contributor"/>
        <br />
        <sub><b>ContributorName</b></sub>
      </a>
      <br />
      💡 Contributor
    </td>
  </tr>
</table>

Want to see your name here? Contribute to the project!

---

## 📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## 💬 Contact

If you have any questions, issues, or feedback, feel free to open an issue in this repository or contact the author at:

   - GitHub: NinjaXP
   - Email: reachninjaxp@gmail.com
