# AI Agent in Python

## Introduction

## Installation

- Install Python 3.x
- Install [uv](https://github.com/astral-sh/uv)

```bash
pip install uv
```

## Usage

-  Clone the repository

```bash
git clone https://github.com/tomdu3/ai-agent.git
cd ai-agent
```

- Create a `.env` file in the root directory of the project with the following content:

```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
ANTHROPIC_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
``` 

- The dependencies will be installed automatically by uv on the first run

```bash
uv run main.py
```
