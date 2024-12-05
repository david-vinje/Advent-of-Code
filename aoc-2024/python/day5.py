raw_orders, raw_updates = [x.split() for x in open('./input/day5.txt').read().split("\n\n")]

orders = {}
for order in raw_orders:
  a, b = [int(x) for x in order.split('|')]
  if a not in orders:
    orders[a] = []
  orders[a].append(b)

updates = []
for update in raw_updates:
  update = [int(x) for x in update.split(',')]
  updates.append(update)


def check_order(update):
  previous = set()
  for index, page in enumerate(update):
    previous.add(page)
    if page in orders:
      for order in orders[page]:
        if order in previous:
          return (False, index)
  return (True, -1)
    
total = 0
    
for update in updates:
  if check_order(update)[0]:
    m = int(len(update)/2)
    total += update[m]
    # print(update[m])
print(total)

total = 0

def put_in_order(update):
  in_order, index = check_order(update)
  put_in_order = False
  while not in_order:
    put_in_order = True
    tmp = update[index]
    update[index] = update[index-1]
    update[index-1] = tmp
    in_order, index = check_order(update)
  return put_in_order

for update in updates:
  if put_in_order(update):
    m = int(len(update)/2)
    total += update[m]
    # print(update[m])
print(total)