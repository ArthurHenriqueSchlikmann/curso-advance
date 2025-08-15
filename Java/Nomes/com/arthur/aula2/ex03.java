package com.arthur.aula2;
import java.util.Scanner;

public class ex03 {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        System.out.print("Digite o início dos múltiplos: ");
        int cmc = teclado.nextInt();
        System.out.println("Digite o fim dos múltiplos: ");
        int fim = teclado.nextInt();
        System.out.println("Diga o número para descobrir os múltiplos: ");
        int numero = teclado.nextInt();
        if(cmc > fim || cmc < 0 || fim < 0 || numero > fim) {
            System.out.println("O início deve ser menor que o fim.");
            return;
        } else {
            System.out.println("Múltiplos de " + numero +" entre " + cmc + " e " + fim + ":");
            for (int i = cmc; i <= fim; i++) {
                if (i % numero == 0) {
                    System.out.print(i + " ");
                }
            } 
        }
    }
}
