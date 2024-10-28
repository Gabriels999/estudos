import Animais.Cachorro;

public class Main {

    public static void main(String[] args){

        // printHelloWorld();
        // handleMath();

        // System.out.println(areWeGoingToTheBeach());

        Cachorro cachorro = new Cachorro();
        cachorro.nome = "Preulinha";
        cachorro.raca = "SRD";
        cachorro.idade = 10;

        System.out.println(cachorro);
    }

    public static void printHelloWorld(){
        System.out.println("Hello World");
    }

    public static void handleMath(){
        int a = 2;
        int b = 5;

        System.out.println("Soma: " + soma(a, b));
        System.out.println("Subtracao: " + subtracao(a, b));
        System.out.println("Multiplicacao: " + multiplicacao(a, b));
        System.out.println("Divisao: " + divisao(a, b));
    }
    
    public static int soma(int a, int b){
        return a + b;
    }

    public static int subtracao(int a, int b){
        return a - b;
    }

    public static int multiplicacao(int a, int b){
        return a * b;
    }

    public static float divisao(int a, int b){
        return (float) a / b;
    }

    
    public static boolean areWeGoingToTheBeach(){
        boolean sunnyDay = true;
        boolean weekendDay = true;
        System.out.println("Vamos pra praia ? " + (sunnyDay && weekendDay));
        return sunnyDay && weekendDay;
    }
}