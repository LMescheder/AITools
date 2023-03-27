# AI Tools

This repository contains a small but useful suite of command line tools that use LLMs to perform tasks.

The commands take instructions as arguments, read text from STDIN, and output text to STDOUT.

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
aimod INSTRUCTION < INPUT_FILE > OUTPUT_FILE
```

For example, to rewrite code in Rust, run:
```bash
aimod "Rewrite in Rust" < mycode.cpp > mycode.rs
```

Please note that applying the tool may result in charges by OpenAI.

Tools that are available:

* `aiexplain`: Generate explanation for text from STDIN 
* `aigen INSTRUCTION`: Generate text or code given instruction
* `aimod INSTRUCTION`: Modifies text from STDIN given explanation

## Usage in VIM
You can execute external commands in VIM using the [bang symbol](https://vimways.org/2019/vim-and-the-shell/).

This way, you can use the tools directly VISUAL mode by typing:
```bash
:!aimod INSTRUCTION
```
or
```bash
:%!aimod INSTRUCTION
```
to apply the instruction to the entire document.

To generate an explanation for a given text or code fragment in a separate window, you can run
```bash
:w !aiexplain
```

