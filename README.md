# Prompt Classifier

A Bayesian inference system for detecting prompt injections in multi-turn LLM chat sessions.

---

## 🚀 Features

- Classify user chat sessions as malicious or innocent using Bayesian updates
- Track belief across multi-turn interactions
- Generate synthetic "innocent" prompts based on domain-specific style
- Evaluate model accuracy using precision, recall, and F1
- Fully tested with >90% code coverage
- Pre-configured with `uv`, `ruff`, `pytest`, `mypy`, and `pre-commit`

---

## 🖥️ CLI Usage

Run the pipeline from the command line using:

```bash
python cli.py --malicious data/malicious.json \\
              --output outputs/classified_sessions.json \\
              --n_innocent 100 \\
              --verbose
```

**Arguments:**

| Argument       | Description |
|----------------|-------------|
| `--malicious`  | Path to input JSON file with known malicious sessions |
| `--output`     | Where to write the classified sessions JSON |
| `--n_innocent` | Number of synthetic innocent sessions to generate |
| `--verbose`    | Print belief updates and classifications in real-time |

---

## 🧪 Testing

This project uses `pytest` with full coverage enabled.

### 🔍 Run All Tests

```bash
pytest --cov=src
```

### ✅ Expect Output Like:

```
collected 15 items
...
---------- coverage ----------
Name                     Stmts   Miss  Cover
--------------------------------------------
src/...                     ...     0   100%
```

---

## 🛠️ Dev Environment

Recommended setup using `uv`:

```bash
uv venv
source .venv/bin/activate
uv pip install -r <(uv pip compile --extra dev pyproject.toml)
```

---

## 🔍 Code Quality

Use the built-in tools via `pre-commit`:

```bash
pre-commit install
pre-commit run --all-files
```

Includes:
- `black` for formatting
- `isort` for import sorting
- `ruff` for fast linting
- `mypy` for type checking

---

## 📂 Folder Structure

```
prompt_classifier/
├── cli.py
├── pyproject.toml
├── .pre-commit-config.yaml
├── README.md
├── data/
│   └── malicious.json
├── outputs/
│   └── classified_sessions.json
├── src/
│   ├── *.py  (core modules)
├── tests/
│   ├── test_*.py (unit tests)
```
