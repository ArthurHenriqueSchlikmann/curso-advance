package com.arthur.aula2;
import java.util.Scanner;
import com.arthur.aula2.Libex02;

public class ex01 {
    public static void main(String[] args) {
        Libex02 lib = new Libex02();
        Scanner teclado = new Scanner(System.in);
        System.out.print("Você tem quantos anos? ");
        int idade = teclado.nextInt();
        boolean idadeOk = lib.idade(idade);
        if (idadeOk) {
            System.out.println("quanto dinheiro você tem? ");
            int dinheiro = teclado.nextInt();
            boolean dinheiroOk = lib.dinheiro(dinheiro);
            if (dinheiroOk) {
                System.out.print("Você trabalha? (S/N) ");
                char trabalha = teclado.next().charAt(0);
                boolean trabalhaOk = lib.trabalha(trabalha);
                if (trabalhaOk) {
                    System.out.println("Você pode entrar na balada!");
                } else {System.out.println("Você não pode entrar na balada!");}}
            else {System.out.println("Você não pode entrar na balada!");}
        } else {System.out.println("Você não pode entrar na balada!");}
        teclado.close();
    }
}