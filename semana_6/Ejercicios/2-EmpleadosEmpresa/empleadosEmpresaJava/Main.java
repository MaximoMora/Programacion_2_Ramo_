package empleadosEmpresaJava;


import java.util.Arrays;



public class Main {
    public static void main(String[] args) {
        

        Gerente kevin = new Gerente("Kevin", 19, 300.0f, "liderazgo", Arrays.asList("Tecnicos Informaticos", "Soldadores"));
        kevin.describir_rol();

        Asistente Can = new Asistente("Candel", 20, 200.0f);
        Can.describir_rol();
        
        
    }
}
