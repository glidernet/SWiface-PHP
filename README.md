# SWiface-PHP
SWiface-PHP the PHP scripts 
This is the set of PHP/Python scripts that are invoked by the Silent Wings Studio program and conform the protocol defined on the document:
https://github.com/swingsopen/swtracking/wiki/Tracking-Protocol


# SWiface-PHP

**SWiface-PHP** is a collection of PHP and Python scripts designed to serve as an interface between **Silent Wings Studio** and the **Open Glider Network (OGN)**. It implements the [Silent Wings Tracking Protocol](https://github.com/swingsopen/swtracking/wiki/Tracking-Protocol) and provides real-time scoring capabilities, notably supporting [sgp.aero](http://sgp.aero).

## Overview

The system acts as a middleware that manages data gathered by collector routines, storing it in either **SQLite3** or **MySQL** databases. It is primarily invoked by the `SWviewer` program and facilitates the flow of glider tracking data (APRS) into a structured format suitable for scoring and visualization.

## Key Features

- **Protocol Implementation:** Fully conforms to the Silent Wings Tracking Protocol.
- **Real-time Scoring:** Provides live scoring data to the SGP (Sailplane Grand Prix) platform.
- **Data Management:** Handles complex glider tracking datasets, including turnpoints, pilots, and event groups.
- **Format Conversion:** Includes utilities to convert between various formats, such as SeeYou `.cucx` files to the pseudo `.cuc` format used by Silent Wings.
- **OGN Integration:** Interfaces with OGN data to provide context for glider flights.

## Architecture

The project uses a hybrid approach to leverage the strengths of different languages:

- **Python Scripts:** Handle the "heavy lifting," including data processing, protocol implementation, file conversions, and database interactions.
- **PHP Scripts:** Provide a web-based API and interface for Silent Wings Studio (invoked via Apache2).

### Core Components

| Component | Description |
|-----------|-------------|
| **Python Utilities** | Data conversion (`ccucxtocuc.py`), configuration generation (`genconfig.py`), and SGP/SoaringSpot integration (`sgp2sws.py`, `soa2sws.py`). |
| **PHP Interface** | JSON endpoints for Silent Wings (`event.php`, `trackpoints.php`, `eventgroups.php`) and contest information (`getcontestinfo.php`). |
| **Database Layer** | Support for both SQLite3 (lightweight) and MySQL (robust/distributed). |

## Installation & Setup

> [!IMPORTANT]
> This system is designed to run in an Apache2 environment, typically on a Linux-based system (e.g., Raspberry Pi).

1. **Clone the repository:**
   ```bash
   git clone https://github.com/acasadoalonso/SWiface-PHP.git
   cd SWiface-PHP
   ```

2. **Install Python dependencies:**
   Ensure you have `pip` installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the Web Server:**
   - Move the scripts to your Apache2 web directory (e.g., `/var/www/html`).
   - Create the necessary directories for data storage:
     ```bash
     mkdir cuc cucfiles
     ```
   - Place your `.cucx` files into the `cucfiles` directory and unzip them.

4. **Configure the System:**
   - Generate or adjust the configuration file (`config.py`) to match your database settings (path, host, user, password).
   - Adjust pilot information if necessary in `kpilot.py`.

5. **Initialize Data:**
   - Use the conversion utilities to prepare your data:
     ```bash
     python ccucxtocuc.py
     ```
   - Or fetch data from SoaringSpot:
     ```bash
     python gsoaringspot.py
     ```

6. **Restart Apache:**
   ```bash
   sudo service apache2 restart
   ```

## Dependencies

The project relies on several key Python libraries, including:
- `pandas`: Data manipulation.
- `geopy`: Geocoding and distance calculations.
- `beautifulsoup4`: HTML parsing/scraping.
- `ogn_client`: OGN data interaction.
- `MySQL-python` / `sqlite3`: Database connectivity.
- `playwright`: Browser automation for web tasks.

## Resources

- [Silent Wings Tracking Protocol Wiki](https://github.com/swingsopen/swtracking/wiki/Tracking-Protocol)
- [SGP (Sailplane Grand Prix)](http://sgp.aero)
- [OGN (Open Glider Network)](https://www.ogn.org/)
