#!/usr/bin/python3

import json, os

IP: str = "127.0.0.1"
PORT: int = 8080
IN_FILE: str = "../static/system_prompt.txt"
OUT_FILE: str = "../target/conv_system_prompt.txt"
MAX_REQUEST: int = 1

# Compile human readable system prompt to json
with open(IN_FILE, "r") as input_file:

    # Escape chars that
    content = input_file.read() \
        .replace("\n", "\\n")   \
        .replace("\"", "\\\"")

    with open(OUT_FILE, "w") as output_file:
        output_file.write(
            json.dumps({
                "system_prompt": {
                    "prompt": content
                }
            })
        )

os.system(f"""

../static/llama* \\
    --system-prompt-file {OUT_FILE} \\
    --nobrowser \\
    --parallel {MAX_REQUEST} \\
    --host {IP} \\
    --port {PORT}

""")
