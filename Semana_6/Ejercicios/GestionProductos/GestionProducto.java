
class GestionProducto {

    class Producto {
        public
        String nombre;
        int precio;
        String categorias;

        Producto(String _nombre, int _precio, String _categorias ) {
            nombre = _nombre;
            precio = _precio;
            categorias = _categorias;
        }

        void mostrar_detalle(){
            System.out.println("Nombre: " + nombre);
        }
    }

    public static void main(String[] args) {
        System.out.println("Hello World");
        
        Producto kevin = new Producto("kevin",19,"Villarica");
        kevin.mostrar_detalle();

    }

}
