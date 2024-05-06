namespace Program {
    class Day3 {
        int priority(char c) {
            if (char.IsUpper(c)) {
                return c - 'A' + 27;
            }
            return c - 'a' + 1;
        }
        void Part1() {
            var res = File.ReadAllLines("../input/day3.txt")
                .Select(line => {
                    var n = line.Length / 2;
                    var A = line[..n];
                    var B = line[n..];
                    var res = A.Intersect(B).ToArray()[0];
                    return res;
                }).Select(priority)
                .Sum();
            Console.WriteLine(res);
        }
        void Part2() {
            var res = File.ReadAllLines("../input/day3.txt")
                .Chunk(3)
                .Select(x => x[0].Intersect(x[1]).Intersect(x[2]).ToArray()[0])
                .Select(priority)
                .Sum();
            Console.WriteLine(res);
        }
        public Day3() {
            // Part1();
            Part2();
        }
    }
}