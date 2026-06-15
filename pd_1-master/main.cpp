#include <iostream>
#define SIZE 10

int main() {
    printf("Tablice\n");
    int numbers[SIZE] = {1, 2, 3, 40, -5, 6, 7, 8, 9, 10};

    printf("\n");
    for (int i = 0; i < SIZE; i++) {
        printf("numbers[%d] = %d\n", i, numbers[i]);
    }

    int max = numbers[0];
    for (int i = 0; i < SIZE; i++) {
        if (numbers[i] > max) {
            max = numbers[i];
        }
    }

    printf("\n");
    printf("max = %d\n", max);

    int min = numbers[0];
    for (int i = 0; i < SIZE; i++) {
        if (numbers[i] < min) {
            min = numbers[i];
        }
    }

    printf("min = %d\n", min);

    int sum = 0;
    for (int i = 0; i < SIZE; i++) {
        sum += numbers[i];
    }
    printf("sum = %d\n", sum);
    float average = (float) sum / SIZE;
    printf("average = %.2f\n", average);

    //wprowadzanie danych, wyznaczenie mediany*

    return 0;
}

// int main() {
//
//    printf("Prosty kalkulator\n");
//
//    printf("Podaj 1 liczbe:\n");
//    int number1 = 0;
//    scanf("%d", &number1);
//
//    printf("Podaj 2 liczbe:\n");
//    int number2 = 0;
//    scanf("%d", &number2);
//
//    printf("%d + %d = %d\n" , number1, number2, number1 + number2);
//   printf("%d - %d = %d\n" , number1, number2, number1 - number2);
//    printf("%d * %d = %d\n" , number1, number2, number1 * number2);
//    printf("%d / %d = %d\n" , number1, number2, number1 / number2);
//
//    return 0;
//}