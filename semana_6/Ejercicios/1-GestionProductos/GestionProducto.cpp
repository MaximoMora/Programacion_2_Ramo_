
#include <iostream>

class Producto {

    public:
        std::string _nombre;
        int _precio;
        std::string _categoria;

        Producto(std::string nombre, int precio, std::string categoria) {
            _nombre = nombre;
            _precio = precio;
            _categoria = categoria;

        }

        void mostrar_detalle() {
            std::cout << "Producto:" << _nombre << "-";
            std::cout << "Precio:" << _precio << "-";
            std::cout << "Categoria:" << _categoria;

        }
};

class Electrónico : public Producto {

    public:
        int _consumo;

        Electrónico(std::string nombre, int precio, std::string categoria, int consumo) : Producto(nombre,precio,categoria) {

            _consumo = consumo;
        }

        void mostrar_detalle() {
            std::cout << "Producto:" << _nombre << "-";
            std::cout << "Precio:" << _precio << "-";
            std::cout << "Consumo:" << _consumo;

        }
};


class Alimenticio : public Producto {

    public:
        int _calorias;

        Alimenticio(std::string nombre, int precio, std::string categoria, int calorias) : Producto(nombre,precio,categoria) {

            _calorias = calorias;

        }

        void mostrar_detalle() {
            std::cout << "Producto:" << _nombre << "-";
            std::cout << "Precio:" << _precio << "-";
            std::cout << "Categoria:" << _categoria  << "-";
            std::cout << "Calorias:" << _calorias;
        }
};

class Vestimenta : public Producto {
    public:
        std::string _talla;
        Vestimenta(std::string nombre, int precio, std::string categoria, std::string talla) : Producto(nombre,precio,categoria) {

            _talla = talla;

        }
        void mostrar_detalle() {
            std::cout << "Producto:" << _nombre << "-";
            std::cout << "Precio:" << _precio << "-";
            std::cout << "Categoria:" << _categoria  << "-";
            std::cout << "Talla:" << _talla;
        }
};

int main() {

    Vestimenta cristian("Cristian",3000,"Polera","L");
    cristian.mostrar_detalle();

    

}