# Prompt Classifier Documentation

Welcome to the official documentation for the **Prompt Classifier** system.

This system detects prompt injection in LLM chat sessions using Bayesian inference and synthetic data generation.

## 📦 Project Modules

| Module               | Purpose |
|----------------------|---------|
| `preprocess.py`      | Tokenizes and prepares chat sessions |
| `generator.py`       | Synthesizes innocent prompts and mirrors malicious ones |
| `likelihood.py`      | Heuristics or LLM-based intent likelihood scoring |
| `bayes_classifier.py`| Belief tracking and session classification |
| `evaluate.py`        | Precision, recall, and F1 metrics |
| `main.py`            | CLI orchestration |
| `config.py`          | Central configuration |

## 🧪 How to Test

Run tests with coverage:

```bash
pytest --cov=src
```

## 🚀 Run the Classifier

```bash
python cli.py --malicious data/malicious.json --n_innocent 5 --verbose
```

## 🛠️ Development Environment

This project uses:

- `uv` for dependency management
- `pre-commit` for formatting and linting
- `pytest` with coverage enforcement
- `mypy` for static type checking
