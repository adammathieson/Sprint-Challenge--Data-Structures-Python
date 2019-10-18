class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    print('current--->', self.current)
    print('storage--->', self.storage)
    self.storage[self.current] = item

    if self.current < self.capacity - 1:
      self.current += 1
    else:
      self.current = 0
      # self.storage = self.storage[1:]
      # self.storage += [item]
    # else:
    #   self.storage.append(item)

  def get(self):
    print_list = []
    for i in self.storage:
      if i != None:
        print_list.append(i)

    print("======>>>>>>", print_list)
    return print_list



# test = RingBuffer(3)

# test.storage.append('something')

# test.append('test')
# test.append('test2')
# test.append('test3')
# test.append('test4')
# test.get()

# print(test.storage)
