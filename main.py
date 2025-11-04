import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QCheckBox, QLabel, QFileDialog, QMessageBox
from scanner import VirusScanner

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("阴杀毒")
        self.resize(800, 600)
        
        self.scan_button = QPushButton("扫描文件")
        self.scan_button.clicked.connect(self.scan_file)
        
        self.engine_frame = QWidget()
        self.engine_layout = QVBoxLayout()
        
        self.yin_engine = QCheckBox("阴引擎 (阴杀毒核心引擎)")
        self.yin_engine.setChecked(True)
        self.yin_engine.setEnabled(False)
        self.yin_engine_label = QLabel("阴引擎：基于特征码检测技术，阴杀毒的核心引擎")
        
        self.red_engine = QCheckBox("Red引擎 (红色引擎)")
        self.red_engine.setChecked(True)
        self.red_engine_label = QLabel("红色引擎：基于SHA1哈希值比对技术，快速检测已知病毒")
        
        self.engine_layout.addWidget(self.yin_engine)
        self.engine_layout.addWidget(self.yin_engine_label)
        self.engine_layout.addWidget(self.red_engine)
        self.engine_layout.addWidget(self.red_engine_label)
        self.engine_frame.setLayout(self.engine_layout)
        
        layout = QVBoxLayout()
        layout.addWidget(self.scan_button)
        layout.addStretch()
        layout.addWidget(self.engine_frame)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def scan_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "选择要扫描的文件")
        if file_path:
            engine_enabled = {
                'Yin': self.yin_engine.isChecked(),
                'Red': self.red_engine.isChecked()
            }
            scanner = VirusScanner()
            is_infected, message = scanner.scan_file(file_path, engine_enabled)
            msg = QMessageBox()
            if is_infected:
                msg.setIcon(QMessageBox.Icon.Critical)
                msg.setText(f"发现病毒！\n{message}")
            else:
                msg.setIcon(QMessageBox.Icon.Information)
                msg.setText(message)
            msg.setWindowTitle("扫描结果")
            msg.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())