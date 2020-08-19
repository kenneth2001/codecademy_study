class SortedList(list):
  def append(self, value):
    super().append(value)
    self.sort()

ls = SortedList([1, 4, 3])
print(ls)

ls.append(1)
print(ls)