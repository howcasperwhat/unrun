# Contributing

Thank you for being interested in this project! We are excited to have you here. This document will guide you through the process of contributing to this project.

## Setup (locally)

1.  **Fork & Clone the repository:**
    Start by forking the repository to your own GitHub account and then clone it to your local machine:
    ```bash
    git clone https://github.com/YOUR_USERNAME/unrun.git
    cd unrun
    ```

2.  **Create a Virtual Environment:**
    It's recommended to use a virtual environment to manage dependencies.
    ```bash
    python -m venv venv
    ```
    Activate the virtual environment:
    *   On Windows (pwsh):
        ```powershell
        .\\venv\\Scripts\\Activate.ps1
        ```
    *   On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

3.  **Install Dependencies:**
    Install the project dependencies, including development dependencies.
    ```bash
    pip install -e '.[dev]'
    ```

## Code Style

We follow [PEP 8](https://pep8.org/) style guide for Python code. You can check the code style by running:

```bash
unrun lint
```

## Running Tests

To run the tests, use the following command:

```bash
unrun test
```

# For Owners
## Build
To build the package, use the following command:

```bash
unrun build
```

## Publish
To publish a new version, you can use the following command:

```bash
unrun publish
```

