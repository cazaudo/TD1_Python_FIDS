To run a Python script with dependencies using **uv**, you can either declare the packages directly on the command line or embed them directly inside the script using standard PEP 723 inline metadata. \[1, 2\]

Here is how to use both approaches:

## **Method 1: Inline Metadata (Recommended)**

You can embed your script dependencies directly into the top of your Python file inside a special comment block. When you run the script, [uv](https://docs.astral.sh/uv/guides/scripts/) will automatically parse the block, create an isolated ephemeral virtual environment, install the packages, and execute the file. \[1, 2, 3, 4\]

> 1. Add the metadata block to your script.py file: \[1, 4\]

>   
*`# /// script`*  
*`# requires-python = ">=3.12"`*  
*`# dependencies = [`*  
*`#     "requests",`*  
*`#     "rich",`*  
*`# ]`*  
*`# ///`*

`import requests`  
`from rich import print`

`response = requests.get("https://httpbin.org")`  
`print(response.json())`

> 1. Run the script using the [uv run](https://docs.astral.sh/uv/concepts/projects/run/) command: \[1, 5\]

>   
`uv run script.py`

## **Method 2: Command Line Flag (--with)**

If you have a quick one-off script and don't want to edit the file content, you can supply packages on the fly using the \--with argument. \[2, 6\]

> * **Single Dependency:**  
>   `uv run --with requests script.py`

> * **Multiple Dependencies:**  
>   `uv run --with requests --with rich script.py`

> * **With Specific Versions:**  
>   `uv run --with "requests>=2.31.0" script.py`  
>   \[2, 5, 6\]

## **Useful Tips**

> * **Project isolation:** If you execute uv run inside an existing project directory containing a pyproject.toml, uv will automatically mix your command-line or inline dependencies with the current project's environment. If you want to safely bypass the local project environment completely, pass the \--no-project flag. \[6, 7\]  
> * **Lockfiles for scripts:** If you want deterministic builds for your standalone script, you can generate a script-specific lockfile by running uv lock \--script script.py. \[8\]

\[1\] [https://news.ycombinator.com](https://news.ycombinator.com/item?id=44641521)  
\[2\] [https://www.youtube.com](https://www.youtube.com/watch?v=ozy02OXTkZo)  
\[3\] [https://treyhunner.com](https://treyhunner.com/2024/12/lazy-self-installing-python-scripts-with-uv/)  
\[4\] [https://adver.tools](https://adver.tools/python/tutorial/running-python-scripts-uv/)  
\[5\] [https://docs.astral.sh](https://docs.astral.sh/uv/concepts/projects/run/)  
\[6\] [https://docs.astral.sh](https://docs.astral.sh/uv/guides/scripts/)  
\[7\] [https://github.com](https://github.com/astral-sh/uv/issues/9495)  
\[8\] [https://www.reddit.com](https://www.reddit.com/r/Python/comments/1jmyip9/selfcontained_python_scripts_with_uv/)