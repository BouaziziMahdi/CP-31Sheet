import java.io.*;
import java.util.*;

public class Game {

    public static void main(String[] args) throws Exception {

        FileInputStream fis = new FileInputStream(System.getProperty("user.dir") + "/test.txt");
        System.setIn(fis);

        Scanner sc = new Scanner(System.in);
        Game game = new Game();

        while (sc.hasNextInt()) {
            int n = sc.nextInt();
            System.out.println(game.nestedGame(n));
        }

        sc.close();
    }

    public String nestedGame(int n) {
        if (n % 3 == 0) {
            return "Second";
        }
        if ((n + 1) % 3 == 0 || (n - 1) % 3 == 0) {
            return "First";
        }
        return "Second";
    }
}
