def main():
    #write your code below this line
    count = 0
    sum_of_num = 0

    while True:
        number = int(input())

        if number == 0:
            break
        if number > 0:
            count = count + 1
            sum_of_num = sum_of_num + number

    if count == 0:
        print("Cannot calculate the average")
    else:
        average = sum_of_num / count
        print(average)

if __name__ == '__main__':
    main()
