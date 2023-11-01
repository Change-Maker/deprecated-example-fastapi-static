# Tailwind CSS

## 1. VS Code Setup

Install extension: [Tailwind CSS IntelliSense](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss)

## 2. CDN

To activate Tailwind CSS IntelliSense, we have to create a file named `tailwind.config.{js,cjs,mjs,ts}` in our workspace.

I create `tailwind.config.js` in this example:

  ```text
  workspace_root_dir
  ├── Dockerfile
  ├── Dockerfile.env_only
  ├── docs
  │   └── tailwind_css.md
  ├── LICENSE
  ├── README.md
  ├── requirements.txt
  ├── src
  │   ├── client
  │   │   ├── css
  │   │   │   └── example.css
  │   │   ├── example.html
  │   │   ├── index.html
  │   │   └── js
  │   │       ├── example.js
  │   │       └── index.js
  │   └── fastapi_app
  │       ├── configs
  │       │   └── settings.json
  │       ├── main.py
  │       ├── routers
  │       │   ├── example.py
  │       │   ├── home.py
  │       │   └── __init__.py
  │       └── utils
  │           ├── config_util.py
  │           ├── __init__.py
  │           └── logger_util.py
  └── tailwind.config.js
  ```

  The `tailwind.config.js` file in the workspace root directory:

  ```js
  /** @type {import('tailwindcss').Config} */
  module.exports = {
    content: ["./src/client/**/*.{html,js}"],
    theme: {
      extend: {},
    },
    plugins: [],
  }
  ```

  Add CDN into `src/client/index.html` file:

  ```html
  <!DOCTYPE html>
  <html>
    <head>
      <!-- ... -->
      <script src="https://cdn.tailwindcss.com"></script>
      <!-- ... -->
  ```

  An empty `tailwind.config.js` file is also accepted.

But if you need customization, here is what to do:

  Refer to [Intellisense VsCode extension suggestions no working #875](https://github.com/tailwindlabs/tailwindcss-intellisense/issues/875)

  The file structure should be like this:

  ```text
  workspace_root_dir
  ├── Dockerfile
  ├── Dockerfile.env_only
  ├── docs
  │   └── tailwind_css.md
  ├── LICENSE
  ├── README.md
  ├── requirements.txt
  └── src
      ├── client
      │   ├── css
      │   │   └── example.css
      │   ├── example.html
      │   ├── index.html
      │   └── js
      │       ├── example.js
      │       ├── index.js
      │       └── tailwind.config.js
      └── fastapi_app
          ├── configs
          │   └── settings.json
          ├── main.py
          ├── routers
          │   ├── example.py
          │   ├── home.py
          │   └── __init__.py
          └── utils
              ├── config_util.py
              ├── __init__.py
              └── logger_util.py
  ```

  I create a color named `my-grey` in `src/client/js/tailwind.config.js` file:

  ```js
  /** @type {import('tailwindcss').Config} */
  export default {
    theme: {
      extend: {
        colors: {
          "my-grey": '#aaaaaa',
        },
      },
    },
  }
  ```

  Import Tailwind CSS configuration into `src/client/index.html` file:

  ```html
  <!DOCTYPE html>
  <html>
    <head>
      <!-- ... -->
      <script type="module">
        import config from "./js/tailwind.config.js";
        window.tailwind.config = config;
      </script>
      <!-- ... -->
  ```

But there will be a warning in web browser console:

```text
cdn.tailwindcss.com should not be used in production. To use Tailwind CSS in production, install it as a PostCSS plugin or use the Tailwind CLI
```

## 3. Tailwind CLI

1. Install `tailwindcss` as a development dependency.

    ```bash
    npm install -D tailwindcss
    ```

2. Initialize Tailwind CSS.

    ```bash
    npx tailwindcss init
    ```

    Afterward, there will be a `tailwind.config.js` file in our project.

3. Configure paths.

    ```js
    /** @type {import('tailwindcss').Config} */
    module.exports = {
      content: ['./src/client/**/*.{html,js}'],
      theme: {
        extend: {},
      },
      plugins: [],
    };
    ```

4. Add the Tailwind directives to `tailwind_input.css`.

    ```css
    @tailwind base;
    @tailwind components;
    @tailwind utilities;
    ```

5. Start Tailwind CLI build process.

    ```bash
    npx tailwindcss \
      -i ./tailwind_input.css \
      -o ./src/client/css/tailwind.css
    ```

    This will output `tailwind.css` into `src/client/css/` folder.

    To make it update Tailwind CSS output file after change
    `tailwind_input.css` file:

    ```bash
    npx tailwindcss \
      -i ./tailwind_input.css \
      -o ./src/client/css/tailwind.css \
      --watch
    ```

6. Start using Tailwind in your HTML.

    ```html
    <!DOCTYPE html>
    <html>
      <head>
        <!-- ... -->
        <link href="./css/tailwind.css" rel="stylesheet">
        <!-- ... -->
    ```
