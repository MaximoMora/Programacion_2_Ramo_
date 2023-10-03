#include <iostream>


int main() {

    int numbers[] = {1,2,3,4,5};
    int sum = 1;
    for (int i = 0; i < 5; i++) {
        sum = sum * numbers[i];
    }

    std::cout << sum;

    return 0;

}