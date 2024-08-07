# WebSocket Chat Project

This project is a simple WebSocket-based chat application built with Quart

## Prerequisites

Before you begin, ensure you have the following installed on your system:
- Python 3.7 or higher
- [Poetry](https://python-poetry.org/) for dependency management

## Installation

1. Install dependencies using Poetry:
   ```
   poetry install
   ```

## Running the Application

1. Activate the poetry shell:
   ```
   poetry shell
   ```

2. Start the application:
   ```
   poetry run start
   ```

3. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

## Project Structure

```
websocket-chat-project/
├── src/
│   └── chat/
│       ├── templates/
│       │   └── index.html
│       └── __init__.py
├── tests/
│   └── __init__.py
├── poetry.lock
├── pyproject.toml
└── README.md
```

## Features

- Real-time WebSocket communication
- Unique client ID for each connection
- Simple HTML/JavaScript frontend

