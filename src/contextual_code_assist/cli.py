import argparse
from .main import CodeCompleter

def main():
    parser = argparse.ArgumentParser(description='Contextual Code Assistant')
    parser.add_argument('context', type=str, help='Code context for completion')
    args = parser.parse_args()

    completer = CodeCompleter()
    suggestion = completer.complete(args.context)
    print(f"Suggestion: {suggestion}")

if __name__ == "__main__":
    main()