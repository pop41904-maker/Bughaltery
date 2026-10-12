# Simple Finance Manager (CLI)

A robust, lightweight Command Line Interface (CLI) application written in Python for personal finance tracking. The application features a secure multi-user architecture, cryptographic password hashing, real-time balance validation, and automated SQLite database management.

---

## 🌟 Key Features

### 👤 User Authentication & Security
* **Data Validation:** Automatic validation checks during registration to prevent duplicate usernames, enforce safe lengths (2–18 characters), and require strong passwords (minimum 6 characters).
* **Cryptographic Protection:** Safe login flow leveraging a combination of unique per-user salts (`uuid4`) and high-security `SHA-512` hashing to defend against rainbow table attacks.
* **Brute-Force Prevention:** Session security module restricts users to a maximum of 5 failed login attempts per session.

### 💰 Transaction Management
* **Double-Entry Simulation:** Seamless creation of monetary operations divided into Income (`+`) and Expense (`-`).
* **Overdraft Protection:** Smart balance verification ensuring expenses never exceed the user's available funds, maintaining financial log integrity.
* **Real-time Analytics:** Instant access to accurate current balance data and chronological transaction history logs.

### 💻 Interface & UX
* **Tabular Layouts:** Terminal rendering powered by `PrettyTable` to deliver structured data visually consistent with modern terminal apps.
* **Cross-Platform UI Utilities:** Native integration of automatic console screen clearing (`cls` / `clear`) across Windows, macOS, and Linux.

---

## 📁 Project Architecture & Components

The application is modularized to separate data storage, business logic, visual representation, and entry points.

```text
├── main.py                  # Global application entry point and startup loop
└── Main/                    # Core source code package
    ├── data/                # Data persistence layer
    │   ├── SQL.py           # SQLite connection pools, table schemas, and queries
    │   └── Tables.db        # Relational database file (auto-generated on launch)
    ├── main/                # User dashboard logic (post-authentication)
    │   ├── choise1.py       # Handles new expense/income transaction inputs
    │   ├── choise2.py       # Renders transaction history tables
    │   └── choise3.py       # Quick balance statement visualizer
    ├── start/               # Gateway logic (pre-authentication)
    │   ├── choise1.py       # User sign-up orchestrator (validates and creates accounts)
    │   └── choise2.py       # User login orchestrator (checks credentials and maps sessions)
    ├── module/              # Shared structural utilities
    │   ├── hashing/
    │   │   └── hashing.py   # Salt generation and SHA-512 data hashing functions
    │   ├── visual/
    │   │   ├── error.py     # Pre-configured graphical error warning components
    │   │   └── menu.py      # Declarative templates for Start and Main menus
    │   └── inputModule.py   # Type-safe input parsing, UI pauses, and screen refreshing
    └── secondPart.py        # Active session controller and main dashboard router
```

---

## 🛠 Prerequisites & Dependencies

Before running this project, ensure you have **Python 3.8 or higher** installed on your operating system.

The application relies on the following packages:
* **Standard Libraries:** `sqlite3`, `hashlib`, `uuid`, `os`, `time`, `datetime`, `pathlib` (No installation needed).
* **External Dependencies:** `prettytable` (Required for visual CLI tables).

---

## 🚀 Step-by-Step Installation & Setup

Follow these commands to clone, install, and run the project locally on your machine:

### 1. Clone or Download the Source Code
Download this repository to your local drive and navigate into the root directory:
```bash
cd path/to/your/project-root
```

### 2. Set Up a Virtual Environment (Optional but Recommended)
Isolation prevents conflicting dependency versions across different projects on your system:
```bash
# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Necessary Packages
Install the required table rendering toolkit from PyPI:
```bash
pip install prettytable
```

### 4. Execute the Application
Launch the main startup file to run the dashboard:
```bash
python main.py
```

---

## 🗄 Relational Database Schema

The script initializes an integrated SQLite database (`Main/data/Tables.db`) containing two relational tables on its initial execution:

### 1. `Users` Table
Maintains administrative metadata and live account balances for every registered user.
* `Id` (`INTEGER PRIMARY KEY AUTOINCREMENT`) — Unique internal identifier for the user.
* `Name` (`TEXT NOT NULL UNIQUE`) — Chosen username utilized for system login.
* `Password` (`TEXT NOT NULL`) — Secure 128-character hex string generated from SHA-512.
* `Salt` (`TEXT NOT NULL`) — High-entropy random UUID added to enhance hash strength.
* `Balance` (`REAL DEFAULT 0.0`) — Float variable tracking current financial assets.
* `Time_Registrate` (`TEXT NOT NULL`) — Calendar date recording when the profile was generated.

### 2. `History` Table
Keeps a permanent, immutable log of all accounting activities occurring inside the platform.
* `Id` (`INTEGER PRIMARY KEY AUTOINCREMENT`) — Unique reference index for the operation.
* `Id_User` (`INTEGER NOT NULL`) — Links the activity directly to a specific user ID (`Users.Id`).
* `Name_Operation` (`TEXT NOT NULL`) — String describing the purpose/title of the transaction.
* `Count_Transaction` (`REAL NOT NULL`) — The precise numerical value of funds moved.
* `Type_Transaction` (`INTEGER NOT NULL`) — Boolean toggle status (`1` for positive Income, `0` for negative Expense).
* `Data_Transaction` (`TEXT`) — Date string pinpointing when the activity was submitted.