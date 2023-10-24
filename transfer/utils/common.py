from PySide6.QtCore import QFile, QIODevice, QTextStream

class CommonHelper:

    @staticmethod
    def readQssResource(resource_path):
        stream = QFile(resource_path)
        stream.open(QIODevice.ReadOnly)
        return QTextStream(stream).readAll()

    @staticmethod
    def repalceAllColors():
        pass