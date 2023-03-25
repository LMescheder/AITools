# AI Edit

This repository contains a small but useful `aiedit` command that takes instructions as arguments, reads text from STDIN, and outputs text to STDOUT.

To install, simply run:
```bash
pip install .
```

This will install all dependencies and make the `aiedit` tool available. Please note that we currently require Python version 3.10. If this version is not supported by your operating system, you can install it using [asdf](https://asdf-vm.com/) or a similar tool.

## Usage
To use the tool, first obtain an API key from the OpenAI [website](https://platform.openai.com/) and set the `OPENAI_API_KEY` environment variable by running:
```bash
export OPENAI_API_KEY=<your-openai-api-key>
```

You can now apply the tool to a text file by running:
```bash
aiedit INSTRUCTION < INPUT_FILE > OUTPUT_FILE
```

For example, to rewrite code in Rust, run:
```bash
aiedit "Rewrite in Rust" < mycode.cpp > mycode.rs
```

Please note that applying the tool may result in charges by OpenAI.

You can also use this tool in VIM by selecting text in VISUAL mode and typing:
```bash
:!aiedit INSTRUCTION
```
or
```bash
:%!aiedit INSTRUCTION
```
to apply the instruction to the entire document.

