"""
This script takes a prompt as a command line argument and uses OpenAI's GPT-3 to generate text
based on the prompt. The generated text is printed to stdout.
"""
import sys
import click
import openai


INSTRUCTION_TEMPLATE: str = """
You are an automatic writing and code improver that modifies text or code inputs according to a task description.
Your task is the following: {task}.
Only output the updated version to replace the original text or code.
I want you to only reply the replacement text or code and nothing else, do not write explanations.
Only perform your task, do not add additional content.
"""


def generate_text(
    history: list[dict], temperature: float = 1.0, model: str = "gpt-3.5-turbo"
) -> str:
    """Generate text based on the 'history' argument using OpenAI's GPT-3."""
    response = openai.ChatCompletion.create(
        model=model,
        messages=history,
        temperature=temperature,
    )
    # TODO: deal with error
    content: str = response["choices"][0]["message"]["content"]
    # The model sometimes outputs extra "```" characters to denote
    # code boundaries. This hack removes them.
    lines = content.split("\n")
    lines = [line for line in lines if not line.startswith("```")]
    content = "\n".join(lines)
    return content


@click.command()
@click.argument("prompt", type=str, nargs=-1)
def cli(prompt: str):
    """Modify STDIN based on PROMPT and print the generated text to STDOUT."""
    task = " ".join(prompt)
    instruction = INSTRUCTION_TEMPLATE.format(task=task)
    history = [
        {"role": "system", "content": instruction},
        {"role": "user", "content": sys.stdin.read()},
    ]
    content = generate_text(history)
    print(content)
