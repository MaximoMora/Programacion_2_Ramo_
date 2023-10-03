#include <iostream>



int main() {
    int contador  = 0;
    int n = 100;
    for (int i = 0; i < n; i += 1) {
        for (int k = 0; k <= i; k += 1) {

            std::cout << "i: " << i << " k " << k << std::endl;
            contador += 1;
        }
    }

    std::cout << "numero de operaciones:  " << contador << std::endl;
}