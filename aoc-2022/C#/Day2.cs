
namespace Program
{
    class Day2
    {
        enum Result
        {
            Loss = 0, Draw = 3, Win = 6
        }
        enum Hand
        {
            Rock = 1, Paper, Scissors
        }

        int battle(Hand opponent, Hand me)
        {
            var result = (opponent, me) switch
            {
                (Hand.Rock, Hand.Paper) => Result.Win,
                (Hand.Rock, Hand.Scissors) => Result.Loss,
                (Hand.Paper, Hand.Rock) => Result.Loss,
                (Hand.Paper, Hand.Scissors) => Result.Win,
                (Hand.Scissors, Hand.Rock) => Result.Win,
                (Hand.Scissors, Hand.Paper) => Result.Loss,
                _ => Result.Draw
            };
            var score = (int)result + (int)me;
            return score;
        }

        void Part1()
        {
            var result = File.ReadAllLines("../input/day2.txt")
                .Select(line => line.Split())
                .Select(line =>
                {
                    return (line[0], line[1]) switch
                    {
                        ("A", "X") => (Hand.Rock, Hand.Rock),
                        ("A", "Y") => (Hand.Rock, Hand.Paper),
                        ("A", _) => (Hand.Rock, Hand.Scissors),
                        ("B", "X") => (Hand.Paper, Hand.Rock),
                        ("B", "Y") => (Hand.Paper, Hand.Paper),
                        ("B", _) => (Hand.Paper, Hand.Scissors),
                        (_, "X") => (Hand.Scissors, Hand.Rock),
                        (_, "Y") => (Hand.Scissors, Hand.Paper),
                        _ => (Hand.Scissors, Hand.Scissors)
                    };
                }).Aggregate(0, (acc, elem) =>
                {
                    var score = battle(elem.Item1, elem.Item2);
                    return acc + score;
                });
            Console.WriteLine(result);
        }

        void Part2()
        {
            var result = File.ReadAllLines("../input/day2.txt")
                .Select(line => line.Split())
                .Select(line =>
                {
                    return (line[0], line[1]) switch
                    {
                        ("A", "X") => (Hand.Rock, Hand.Scissors),
                        ("A", "Y") => (Hand.Rock, Hand.Rock),
                        ("A", _) => (Hand.Rock, Hand.Paper),
                        ("B", "X") => (Hand.Paper, Hand.Rock),
                        ("B", "Y") => (Hand.Paper, Hand.Paper),
                        ("B", _) => (Hand.Paper, Hand.Scissors),
                        (_, "X") => (Hand.Scissors, Hand.Paper),
                        (_, "Y") => (Hand.Scissors, Hand.Scissors),
                        _ => (Hand.Scissors, Hand.Rock)
                    };
                }).Aggregate(0, (acc, elem) =>
                {
                    var score = battle(elem.Item1, elem.Item2);
                    return acc + score;
                });
            Console.WriteLine(result);
        }

        public Day2()
        {
            // Part1();
            Part2();
        }
    }
}