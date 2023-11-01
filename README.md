# Example FastAPI Static

This is an example for building a FastAPI app and serving a static website on it.

## 1. Requirements

- Python 3.10+

    This example uses `|` operator on type annotations (PEP 604).

- Python 3.8+

    This example uses `:=` (Walrus) operator on file chunked reading (PEP 572).

## 2. Setup Environment

1. Create Python virtual environment.

    ```bash
    python -m venv py310venv
    ```

2. Activate the Python virtual environment.

    ```bash
    source py310venv/bin/activate
    ```

3. Upgrade `pip` and install dependencies.

    ```bash
    python -m pip install --no-cache-dir --upgrade pip
    python -m pip install --no-cache-dir --upgrade -r requirements.txt
    ```

## 3. Usage

It needs to build Tailwind CSS first. See `docs/tailwind_css.md` for more
information.

Afterwards, get into `src/fastapi_app` folder and run `python main.py`.

### 3.1 Development mode

To run in development mode, set `MODE` environment variable to `dev` and run
app:

```bash
MODE="dev" python main.py
```

In this mode, it will reload automatically if you save the changes to files in
`src/fastapi_app` folder.

### 3.2 File logger

To enable file logger, change `logger.enable` to `true` in
`src/fastapi_app/configs/settings.json` file.

The log files will be put in `src/fastapi_app/logs` folder.
To change the location to place log files, change `logger.path` in
`src/fastapi_app/configs/settings.json` file.

### 3.3 Default console logger

To change the log level of default console logger, set `LOGURU_LEVEL`
environment variable, e.g. set it to `INFO`:

```bash
LOGURU_LEVEL="INFO" python main.py
```

To disable the default console logger, change the following lines in
`src/fastapi_app/main.py` file:

```py
if settings.logger is not None:
    logger_util.setup_logger(settings.logger, True)
```

### 3.4 Docker

The examples below use `example-fastapi-static` as the image name.

#### 3.4.1 Full

To build a Docker image:

```bash
docker build -t example-fastapi-static .
```

Run a container (the default port is `3000`):

```bash
docker run -p 3000:3000 -d example-fastapi-static
```

#### 3.4.2 Environment Only

To build a Docker image that only contains environment:

```bash
docker build -t example-fastapi-static:env-only -f Dockerfile.env_only .
```

Run a container:

```bash
docker run -p 3000:3000 -v ./src:/ws/src -d example-fastapi-static:env-only
```

## 4. Troubleshooting

- **Browser doesn't reflect changes made in the files in `client` folder.**

  Browser might cache the content before changes made.

  To disable browser caching, open the developer tools (press the `F12` key
  generally) and get into **Network** tab then check **Disable cache** checkbox.

  Now refresh the website, it should reflect changes.
