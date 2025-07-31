package com.arthur.nome;
import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        System.out.print("Qual o seu nome? ");
        String nome = teclado.nextLine();
        System.out.print("Qual a sua idade? ");
        int idade = teclado.nextInt();
        System.out.print("Qual a sua cor favorita? ");
        String cor = teclado.next();
        if(idade > 150) {
            System.out.println("Você já viveu demais, considere descansar LOL. :)");
            teclado.close();
            System.err.println("Erro: Idade inválida.");
        } else {
            System.out.printf("Olá %s, de %d anos, que tem a cor favorita %s \n", nome, idade, cor);
            teclado.close();
        }
    }
}
