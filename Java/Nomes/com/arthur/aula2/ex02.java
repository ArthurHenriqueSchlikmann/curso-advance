package com.arthur.aula2;
import java.util.Scanner;

public class ex02{
    public static void main(String[] args) {
        while (true) {
            
            Scanner teclado = new Scanner(System.in);
            System.out.print("Você tem quantos anos? ");
            int idade = teclado.nextInt();
            System.out.print("Você quer continuar? (S/N) ");
            char continuar = teclado.next().charAt(0);
            if (continuar == 'N' || continuar == 'n') {
                System.out.println("Programa encerrado.");
                teclado.close();
                System.exit(0);
            }
        }
    }
}