



#include <iostream>


int main() {

    int numbers[] = {1,2,3,4,5};
    int sum = 0;
    for (int i = 0; i < 5; i++) {
        sum += numbers[i];
    }

    std::cout << sum;

    return 0;

}