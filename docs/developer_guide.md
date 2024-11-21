## **`Developer_Guide`**

Welcome to the developer guide! This document explains the internal structure, code logic, and how to contribute to this project.

---

## Table of Contents

1. [Project Structure](#project-structure)
2. [Code Flow](#code-flow)
3. [Adding Features](#adding-features)
4. [Testing](#testing)
5. [Contributing](#contributing)

---

## Project Structure

```
plaintext
DataVisualizer/
├── data/               # Data files (CSV, JSON)
├── docs/               # Documentation files
├── scripts/            # Shell scripts for setup, running, and updates
├── src/                # Source code
│   ├── charts/         # Chart visualization modules
│   ├── utils/          # Helper modules (e.g., CLI menu, data readers)
│   ├── main.py         # Entry point for the application
├── config/             # Configuration files
├── requirements.txt    # Python dependencies
```
---
## Code Flow

1. Entry Point: `src/main.py`

    - Displays the menu and takes user input.
    - Calls the appropriate visualization functions.

2. Visualization Modules: `src/charts/`

    - `bar_chart.py`: Contains logic for ASCII bar charts.
    - `line_graph.py`: Contains logic for ASCII line graphs.

3. Utilities: `src/utils/``

    - `cli_menu.py`: Handles menu display and user input.
    - `data_reader.py`: Reads and validates data from files.
---
## Adding Features

1. Fork the repository and create a new branch:

    ```bash
    git checkout -b feature-name
    ```

2. Add your feature to the appropriate module.
3. Test your feature using sample data in the `data/`` folder.
4. Submit a pull request (PR) to the main branch.
---
## Testing

  - Use Python's built-in `unittest` framework to write tests for new modules.
  - Add test scripts under `src/tests/` (e.g., `test_bar_chart.py`).

---

## Contributing

1. Open an issue to discuss the feature or bug fix.
2. Follow the project's coding standards.
3. Ensure your PR passes all tests.
