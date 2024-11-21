## **`User Guide`**

Welcome to the **Data Visualizer with ASCII Charts**! This guide will walk you through the steps to make the most of this tool.

---

## Table of Contents

1. [Setting Up](#setting-up)
2. [Using the Menu](#using-the-menu)
3. [Examples](#examples)
4. [Troubleshooting](#troubleshooting)

---

## Setting Up

1. Clone the repository and navigate to its directory:
   ```bash
   git clone https://github.com/Ninja-XP/DataVisualizer.git
   cd DataVisualizer
   ```

2. Install all required dependencies:
    ```bash
    bash scripts/install_dependencies.sh
    ```

## Using the Menu

When you run the tool using:

   ```bash
   bash scripts/run_visualizer.sh
   ```

You’ll see the main menu:

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
1. Select an option (1, 2, or 3).
2. Follow the prompts to provide a data file for visualization.

## Examples

**Example 1: Visualize CSV Data**

1. Prepare your CSV file in the `data`/ folder (e.g., `sample_data.csv`).

2. Choose `[1] 📊 Visualize CSV as Bar Chart`.
3. Input the path to your CSV file:
    ```bash
    👉 Enter CSV file path: data/sample_data.csv
    ```
4. View the ASCII bar chart in the terminal.

Example 2: Visualize JSON Data

1. Prepare your JSON file in the `data/` folder (e.g., `example_data.json`).

2. Choose `[2] 📈 Visualize JSON as Line Graph`.

3. Input the path to your JSON file:
    ```bash
    👉 Enter JSON file path: data/example_data.json
    ```

4. View the ASCII line graph in the terminal.

## Troubleshooting

1. Missing Dependencies: Run the installation script:
    ```bash
    bash scripts/install_dependencies.sh
    ```
2. Error Running Tool: Ensure `Python 3` and pip are installed:
    ```bash
    python3 --version
    pip3 --version
    ```
3. Still Facing Issues? Submit a ticket on the GitHub Issues Page.
