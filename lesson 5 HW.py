# 5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
#     - как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получания значений этого атрибута
#     нужно использовать методы get и set

class Book: # create class шаблон кода, с пом котор созд объекты
    def __init__(self, name, author):  # kонструктор класса
        self.name = name #self это ссылка
        self.author = author
    def pages(self):
        return "Has pages"

class binding(Book):
   def __init__(self, name, author, language):
       super().__init__(name, author)
       self.language = language
   def illustrations(self):
       return "Illustrations"

Book_1 = Book("Vianok", "Maksim Bahdanovich") #экземпляр класса

print(Book_1.name)
print(Book_1.author)

Book2 = Book("Spadchyna", "Yanka Kupala")
print(Book2.name)
print(Book2.author)




