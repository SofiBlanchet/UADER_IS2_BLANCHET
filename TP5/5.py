import os

class Memento:
	def __init__(self, file, content):
		self.file = file
		self.content = content

class FileWriterUtility:
	def __init__(self, file):
		self.file = file
		self.content = ""

	def write(self, string):
		self.content += string

	def save(self):
		return Memento(self.file, self.content)

	def undo(self, memento):
		self.file = memento.file
		self.content = memento.content

class FileWriterCaretaker:
	def __init__(self):
		self.mementos = []

	def save(self, writer):
		if len(self.mementos) == 4:
			self.mementos.pop(0)
		self.mementos.append(writer.save())

	def undo(self, writer, index=0):
		if index < len(self.mementos):
			memento = self.mementos[-(index + 1)]
			writer.undo(memento)
		else:
			print(f"No hay estado guardado en la posición {index}")

if __name__ == '__main__':
	os.system("clear")
	print("Crea un objeto que gestionará la versión anterior")
	caretaker = FileWriterCaretaker()

	print("Crea el objeto cuyo estado se quiere preservar")
	writer = FileWriterUtility("GFG.txt")

	writer.write("Estado 1\n")
	caretaker.save(writer)

	writer.write("Estado 2\n")
	caretaker.save(writer)

	writer.write("Estado 3\n")
	caretaker.save(writer)

	writer.write("Estado 4\n")
	caretaker.save(writer)

	writer.write("Estado 5\n") 
	print("\nEstado actual:")
	print(writer.content)

	print("\nSe hace undo al último estado (índice 0):")
	caretaker.undo(writer, 0)
	print(writer.content)

	print("\nSe hace undo al estado anterior (índice 1):")
	caretaker.undo(writer, 1)
	print(writer.content)

	print("\nSe hace undo al estado más antiguo (índice 3):")
	caretaker.undo(writer, 3)
	print(writer.content)
