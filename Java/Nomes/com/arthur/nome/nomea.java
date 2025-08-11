package com.arthur.nome;
import java.util.Scanner;

public class nomea {
    public static void main(String[] args) {
        // Cria um objeto Scanner para ler a entrada do usuário
        Scanner teclado = new Scanner(System.in);
        //Faz um questionário sobre a vida do usuário
        System.out.print("Qual o seu nome? ");
        String nome = teclado.nextLine();
        System.out.print("Qual a sua idade? ");
        int idade = teclado.nextInt();
        System.out.print("Qual a sua cor favorita? ");
        String cor = teclado.next();
        // Verifica se a idade é maior que 150
        if(idade > 150) {
            // Se a idade for maior que 150, exibe uma mensagem de erro meme
            System.out.println("Você já viveu demais, considere descansar LOL :)");
            teclado.close();
            System.err.println("Erro: Idade inválida.");
        } else {
            // Se a idade for válida, exibe uma mensagem de saudação, com nome, idade e cor favorita
            System.out.printf("Olá %s, de %d anos, que tem a cor favorita %s \n", nome, idade, cor);
            teclado.close();
        }
    }
}
