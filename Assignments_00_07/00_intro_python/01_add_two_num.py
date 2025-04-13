def main():
    print("\033[1;3m Two Numbers Addition Program 📝 \033[0m")
    num1 = input("Enter the First Number: ")
    num1 = int(num1)
    num2 = input("Enter the Second Number: ")
    num2 = int(num2)
    result = num1 + num2
    print(f"The Result is: {result}")
if __name__ == "__main__":
    main()
