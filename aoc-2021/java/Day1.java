import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Day1 {
  public static void main(String[] args) throws FileNotFoundException {
    File file = new File("day1.txt");
    Scanner scan = new Scanner(file);
    List<Integer> floors = new ArrayList<>();
    while (scan.hasNext()) {
      floors.add(scan.nextInt());
    }
    part_one(floors);
    part_two(floors);
  }

  public static void part_one(List<Integer> floors) {
    int current = floors.get(0);
    int count = 0;
    for (int floor : floors) {
      if (floor > current)
        count++;
      current = floor;
    }
    System.out.println(count);
  }

  public static void part_two(List<Integer> floors) {
    int count = 0;
    int windowSize = 3;
    int n = floors.size() - windowSize;
    int current = 0;
    for (int i = 0; i < windowSize; i++) {
      current += floors.get(i);
    }
    for (int i = 0; i <= n; i++) {
      int sum = 0;
      for (int j = 0; j < windowSize; j++) {
        sum += floors.get(i + j);
      }
      if (current < sum) count++;
      current = sum;
    }
    System.out.println(count);
  }
}