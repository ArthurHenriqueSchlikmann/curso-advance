package Java.Nomes.com.arthur.nome;
import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        System.out.print("Qual o seu nome? ");
        String nome = teclado.nextLine();
        System.out.print("Qual a sua idade? ");
        int idade = teclado.nextInt();
        System.out.print("Qual a sua cor favorita? ");
        String cor = teclado.nextLine();
        System.out.printf("");
    }
}
