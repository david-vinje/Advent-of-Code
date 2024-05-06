namespace Program
{
    class Day1
    {
        readonly int[] elves;
        public Day1() {
            elves = [.. File.ReadAllText("../input/day1.txt").Split("\n\n")
                .Select(x => x.Split().Select(Int32.Parse))
                .Select(x => x.Sum())
                .OrderDescending()];
            Console.WriteLine(elves[0]);
            Console.WriteLine(elves[0] + elves[1] + elves[2]);
        }
    }
}