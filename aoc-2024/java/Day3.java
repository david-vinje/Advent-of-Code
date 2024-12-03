import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day3 {
  public static void main(String[] args) throws FileNotFoundException {
    File file = new File("./input/day3.txt");
    Scanner scan = new Scanner(file);
    Pattern pattern = Pattern.compile("(mul\\([0-9]*,[0-9]*\\)|don't|do?)");
    int total = 0;
    boolean enabled = true;
    while (scan.hasNextLine()) {
      String line = scan.nextLine();
      Matcher matcher = pattern.matcher(line);
      while (matcher.find()) {
        String match = matcher.group();
        if (match.equals("do")) {
          enabled = true;
        } else if (match.equals("don't")) {
          enabled = false;
        } else if (enabled) {
          String[] mults = match.replace("mul(", "").replace(")", "").split(",");
          int result = Integer.parseInt(mults[0]) * Integer.parseInt(mults[1]);
          total += result;
          System.out.println(match + ", "  + result);
        }
      }
    }
    System.out.println(total);
  }
}