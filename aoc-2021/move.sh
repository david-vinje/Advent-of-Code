
for i in $(seq 1 16);
do
  mkdir "day"${i}
  mv "python/day${i}.py" "day"${i}
  mv "input/day${i}.txt" "day"${i}
done

# a=5
# b="day"$a
# mkdir $b
