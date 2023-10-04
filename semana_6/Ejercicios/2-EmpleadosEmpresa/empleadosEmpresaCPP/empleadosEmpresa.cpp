#include <iostream>
#include <vector>

class Empleado {
    public:
    std::string nombre;
    int edad;
    int salario;

    Empleado(std::string _nombre, int _edad,int _salario) {
        nombre = _nombre;
        edad = _edad;
        salario = _salario;
    }

    void describir_rol() {
        std::cout << "nombre: " << nombre << std::endl;
        std::cout << "edad: " << edad << std::endl;
        std::cout << "salario: " << salario << std::endl; 
    }

};

class Gerente : public Empleado {

    public:
    std::string liderazgo;
    std::vector<std::string> grupos;


    Gerente(std::string _nombre, int _edad, int _salario,std::string _liderazgo) : Empleado(_nombre,_edad,_salario), grupos() {
        liderazgo = _liderazgo;

    }

    void describir_rol() {
        std::cout << "nombre: " << nombre << std::endl;
        std::cout << "edad: " << edad << std::endl;
        std::cout << "salario: " << salario << std::endl; 
        std::cout << "liderazgo: " << liderazgo << std::endl;
    }

};

class Ingeniero  : public Empleado {

    public:
    std::string tecnicatura;
    std::vector<std::string> habilidades;


    Ingeniero (std::string _nombre, int _edad, int _salario,std::string _tecnicatura)
    : Empleado(_nombre,_edad,_salario), habilidades() {
        _tecnicatura = tecnicatura;

    }

    void describir_rol() {
        std::cout << "nombre: " << nombre << std::endl;
        std::cout << "edad: " << edad << std::endl;
        std::cout << "salario: " << salario << std::endl; 
        std::cout << "liderazgo: " << tecnicatura << std::endl;
    }

};


class Asistente  : public Empleado {

    public:
    std::vector<std::string> tareas;
    std::vector<std::string> citas;


    Asistente (std::string _nombre, int _edad, int _salario) : Empleado(_nombre,_edad,_salario), tareas(), citas() {

    }

    void describir_rol() {
        std::cout << "nombre: " << nombre << std::endl << "edad: " << edad << std::endl << "salario: " << salario << std::endl;
        for (int i = 0; i < tareas.size(); i++)
        {
            std::cout << "Tarea " << i << ":"<< tareas[i];
        }
    }

    void Agregar_tareas(std::string nuevaTareas) {
        tareas.push_back(nuevaTareas);

    }

};


int main() {

    Gerente kevin("kevin",19,3000,"fuerte");
    kevin.describir_rol();

    Asistente Can("Can",20,3000);
    Can.Agregar_tareas("Administrar");
    Can.describir_rol();



}