package GestionProductosJava;

public class Productos {
    String nombre;
    int precio;
    String categoria;

    Productos(String nombre, int precio, String categoria) {
        this.nombre = nombre;
        this.precio = precio;
        this.categoria = categoria;

    }

    public void Mostrar_detalle() {
        System.out.println("Nombre: " + nombre + " Precio: " + precio + " categoria: " + categoria);
    }
    

}

class Electronico extends Productos {

    public int consumo;

    Electronico(String nombre, int precio, String categoria, int consumo) {
        super(nombre, consumo, categoria);
        this.consumo = consumo;
    }

    public void Mostrar_detalle() {
        System.out.println("Nombre: " + nombre + " Precio: " + precio + " categoria: " + categoria + " consumo: " + consumo);
    }
}

class Alimenticio extends Productos {

    public int calorias;

    Alimenticio(String nombre, int precio, String categoria, int calorias) {
        super(nombre, precio, categoria);
        this.calorias = calorias;
    }

    public void Mostrar_detalle() {
        System.out.println("Nombre: " + nombre + " Precio: " + precio + " categoria: " + categoria + " calorias: " + calorias);
    }
}



class Vestimenta extends Productos {

    public String talla;

    Vestimenta(String nombre, int precio, String categoria, String talla) {
        super(nombre, precio, categoria);
        this.talla = talla;
    }

    public void Mostrar_detalle() {
        System.out.println("Nombre: " + nombre + " Precio: " + precio + " categoria: " + categoria + " talla: " + talla);
    }
}
