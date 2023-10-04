
package empleadosEmpresaJava;


import java.util.ArrayList;
import java.util.List;


public class Empleado {

    public String nombre;
    public int edad;
    public float salario;

    Empleado(String nombre, int edad, float salario)
    {
        this.nombre = nombre;
        this.edad = edad;
        this.salario = salario;

    }

    public void describir_rol() {
        System.out.println("Nombre: " + nombre + "edad" + edad + "salario" + salario);
    }
}


class Gerente extends Empleado {

    public String liderazgo;
    public List<String> grupos = new ArrayList<String>();

    Gerente(String nombre, int edad, float salario,String liderazgo, List<String> grupos) {
        super(nombre,edad,salario);
        this.liderazgo = liderazgo;
        this.grupos = grupos;

    }

    public void describir_rol() {
        System.out.println("Gerente - Nombre: " + nombre + "edad" + edad + "salario" + salario);
    }

}


class Ingeniero extends Empleado {

    public String tecnicatura;
    public List<String> habilidades = new ArrayList<String>();

    Ingeniero(String nombre, int edad, float salario,String tecnicatura, List<String> habilidades) {
        super(nombre,edad,salario);
        this.tecnicatura = tecnicatura;
        this.habilidades = habilidades;

    }

    public void describir_rol() {
        System.out.println("Ingeniero - Nombre: " + nombre + "edad" + edad + "salario" + salario);
    }
    
}


class Asistente extends Empleado {

    public List<String> tareas = new ArrayList<String>();
    public List<String> grupos = new ArrayList<String>();

    Asistente(String nombre, int edad, float salario) {
        super(nombre,edad,salario);

    }

    public void describir_rol() {
        System.out.println("Asistente - Nombre: " + nombre + "edad" + edad + "salario" + salario);
    }

    public void MostrarTarras() {
        for (int i = 0; i < grupos.size(); i++) {
            System.out.println(grupos.get(i));
        }
    }
    
}