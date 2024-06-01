import java.util.Scanner;

public class Tabla {

    public static void main (String[] args) {
        try (Scanner in = new Scanner(System.in)) {
            int i, numero, resultado;
            System.out.print("Ingrese un n\243mero: ");
            numero = in.nextInt();
            System.out.println();
            for (i=1; i<=10; i++) {
                resultado = i * numero;
                System.out.println(numero + " x " + i + " = " + resultado);
            }
        }
        System.out.println();
    }

}