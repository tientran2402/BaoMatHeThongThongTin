from PyQt6.QtWidgets import QFileDialog
def ReadDataInFile(fileName):
    data = []
    with open(fileName, 'r', encoding='utf-8-sig') as file:
        for line in file:
            data.append(line)
    return data

def WriteDataInFileOut(data, fileOut):
    with open(fileOut + '.txt', 'w', encoding='utf-8-sig') as file:
        for line in data:
            file.write(line)

def ChooseFileFromDevice():
    file_path, _ = QFileDialog.getOpenFileName(None, "Choose file", "", "Text files (*.txt)")
    return file_path

if __name__ == '__main__':
    data = ReadDataInFile("plain_text.txt")
