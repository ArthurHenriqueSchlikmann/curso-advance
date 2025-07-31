package com.arthur.juros;
import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        // Solicita o capital inicial ao usuário
        System.out.print("Digite o capital inicial da aplicação: ");
        double capitalInicial = teclado.nextDouble();
        // Solicita a taxa de juros ao usuário
        System.out.print("Digite a taxa de juros (em decimal, exemplo: 0.05 para 5%): ");
        double taxaJuros = teclado.nextDouble();
        // Solicita o tempo de aplicação ao usuário
        System.out.print("Digite o tempo de aplicação (em anos): ");
        int tempo = teclado.nextInt();
        teclado.close();
        // Calcula o montante(quanto vai render) final usando a fórmula do montante
        double montante = capitalInicial * Math.pow((1 + taxaJuros), tempo);
        // Exibe o resultado do montante final
        System.out.printf("O montante final após %d anos é: %.2f\n", tempo, montante);
    }
}
