#include <iostream>

class Animal {

    public:
    std::string nombre;
    int edad;


    Animal(std::string _nombre, int _edad) {
        nombre = _nombre;
        edad = _edad;

    }

    void sonido() {
        std::cout << "El Animal llamado que se llama " << nombre << "hace un sonido"<< std::endl;
    }
};

class Perro : Animal {

    public:

    Perro(std::string _nombre, int _edad) : Animal(_nombre, _edad) {

    }

    void sonido() {
        std::cout << "El Animal llamado que se llama " << nombre << "hace un wau wau wau"<< std::endl;
    }
};

class Gato : Animal {

    public:
    Gato(std::string _nombre, int _edad) :  Animal(_nombre, _edad){

    }

    void sonido() {
        std::cout << "El Animal llamado que se llama " << nombre << "hace un sonido miau miau miau"<< std::endl;
    }
};

class Pajaro : Animal {

    public:

    Pajaro(std::string _nombre, int _edad) : Animal(_nombre,_edad){

    }

    void sonido() {
        std::cout << "El Animal llamado que se llama " << nombre << "hace un sonido piu piu"<< std::endl;
    }
};





int main(){

    Pajaro gorrion("Pablo",2);
    gorrion.sonido();

}


