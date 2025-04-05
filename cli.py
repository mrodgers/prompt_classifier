import argparse

from src.main import run_classification


def main():
    parser = argparse.ArgumentParser(description="Bayesian Prompt Injection Classifier")
    parser.add_argument("--malicious", type=str, default="data/malicious.json")
    parser.add_argument(
        "--output", type=str, default="outputs/classified_sessions.json"
    )
    parser.add_argument("--n_innocent", type=int, default=100)
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()
    run_classification(args.malicious, args.output, args.n_innocent, args.verbose)


if __name__ == "__main__":
    main()
