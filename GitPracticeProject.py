# Git Practice Project.py

# Practice project to demonstrate git workflow

def main():
    # find the nth fibonacci number
    #eg. 1, 1, 2, 3, 5, 8, 13, 21, 34,...
    n = int(input("What fibonacci number do u want to find?"))

    if n in [1, 2]:
        print(f"The{n}st/nd Fib number is 1")

if __name__ == "__main__":
    main()
