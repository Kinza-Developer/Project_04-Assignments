def main():
    side1 = float(input("\033[1;3m Enter the length of Side 1: \033[0m"))
    side2 = float(input("\033[1;3m Enter the length of Side 2: \033[0m"))
    side3 = float(input("\033[1;3m Enter the length of Side 3: \033[0m"))
    perimeter = side1 + side2 + side3
    print(f"The Perimeter of the Triangle is: {perimeter}")
if __name__ == "__main__":
    main()