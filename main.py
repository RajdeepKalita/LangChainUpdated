import os
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


def main():
    print("Welcome to LangChain Project Workspace!")
    print(f"Working Directory: {os.getcwd()}")


if __name__ == "__main__":
    main()
