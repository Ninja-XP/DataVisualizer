# Data Visualizer with ASCII Charts

[![Version](https://img.shields.io/static/v1?label=Version&message=1.0&color=blue&style=for-the-badge&logo=appveyor)](https://github.com/Ninja-XP/DataVisualizer.git)
[![Build Status](https://img.shields.io/static/v1?label=Build&message=Passing&color=green&style=for-the-badge&logo=github)](https://github.com/Ninja-XP/DataVisualizer/actions)
[![License](https://img.shields.io/static/v1?label=License&message=MIT&color=darkviolet&style=for-the-badge&logo=github)](https://github.com/Ninja-XP/DataVisualizer/blob/main/LICENSE)
[![Contributors](https://img.shields.io/github/contributors/Ninja-XP/DataVisualizer?style=for-the-badge&color=orange)](https://github.com/Ninja-XP/DataVisualizer/graphs/contributors)
[![Stars](https://img.shields.io/github/stars/Ninja-XP/DataVisualizer?style=for-the-badge&color=gold&logo=github)](https://github.com/Ninja-XP/DataVisualizer)
[![Python Version](https://img.shields.io/static/v1?label=Python&message=3.x&color=blue&style=for-the-badge&logo=python)](https://github.com/Ninja-XP/DataVisualizer)
[![Issues](https://img.shields.io/github/issues/Ninja-XP/DataVisualizer?style=for-the-badge&color=red&logo=github)](https://github.com/Ninja-XP/DataVisualizer/issues) [![Last Commit](https://img.shields.io/github/last-commit/Ninja-XP/DataVisualizer?style=for-the-badge&color=purple&logo=github)](https://github.com/Ninja-XP/DataVisualizer/commits/main)

---

![Screenshot_2024_1121_181319](https://github.com/user-attachments/assets/6ef4ec92-c177-451e-85ab-135d9a1ac0e6)

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
![Screenshot_2024_1121_181319](https://github.com/user-attachments/assets/98950bcf-1e0d-4435-80a8-44ea7d7af290)

### CSV Bar Chart Visualization
![Screenshot_2024_1121_181437](https://github.com/user-attachments/assets/a6819822-9940-4e57-bdaa-405c914ce80e)

### JSON Line Graph Visualization
![Screenshot_2024_1121_181809](https://github.com/user-attachments/assets/c48c8292-f4b5-4f7d-8178-dc1db61d0dfd)

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
