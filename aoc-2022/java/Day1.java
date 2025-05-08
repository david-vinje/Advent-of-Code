import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Day1 {
  public static void main(String[] args) throws IOException {
    var cwd = System.getProperty("user.dir");
    BufferedReader reader = new BufferedReader(new FileReader(cwd + "/input/day1.txt"));
    List<Integer> calories = new ArrayList<>();
    int sum = 0;
    String line = reader.readLine();
    while (line != null) {
      if (line.isEmpty()) {
        calories.add(sum);
        sum = 0;
        line = reader.readLine();
      }
      sum += Integer.parseInt(line);
      line = reader.readLine();
    }
    Collections.sort(calories, (a, b) -> b - a);
    System.out.println(calories.get(0));
    System.out.println(calories.get(0) + calories.get(1) + calories.get(2));
  }
}