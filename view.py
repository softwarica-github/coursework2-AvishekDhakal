import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QProgressBar, QPlainTextEdit, QComboBox,  QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPixmap
from controller import HashCrackerController

# The HashCrackerGUI class is a widget for a graphical user interface for cracking hashes.
class HashCrackerGUI(QWidget):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("PyCrackHash")
        self.setGeometry(100, 100, 800, 600)

        # main layout
        main_layout = QVBoxLayout()


        title_logo_layout = QHBoxLayout()


        logo = QLabel(self)
        pixmap = QPixmap('logo/logo.jpeg')  # Update with your logo file path
        logo.setPixmap(pixmap.scaled(64, 64))
        title_logo_layout.addWidget(logo)


        title_logo_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Add a title
        title = QLabel("PyCrackHash")
        title.setStyleSheet("font-size: 32px;")
        title_logo_layout.addWidget(title)


        title_logo_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum))


        main_layout.addLayout(title_logo_layout)


        main_layout.addWidget(QLabel("Analyze Hash:"))
        self.hash_analyze_input = QLineEdit()
        main_layout.addWidget(self.hash_analyze_input)


        self.analyze_hash_button = QPushButton("Analyze Hash")
        main_layout.addWidget(self.analyze_hash_button)

        # Hash input field
        main_layout.addWidget(QLabel("Enter Hash:"))
        self.hash_input = QLineEdit()
        main_layout.addWidget(self.hash_input)


        # Hash file upload
        self.hash_file_upload = QPushButton("Upload Hash File")
        main_layout.addWidget(self.hash_file_upload)

        # Hash type selection
        main_layout.addWidget(QLabel("Select Hash Type:"))
        self.hash_type = QComboBox()
        self.hash_type.addItems(["MD5", "SHA1", "SHA256"])
        main_layout.addWidget(self.hash_type)

        # Dictionary file upload
        self.file_upload = QPushButton("Upload Dictionary File")
        main_layout.addWidget(self.file_upload)

        # Start button
        self.start_button = QPushButton("Start Cracking")
        main_layout.addWidget(self.start_button)

        # Output area
        main_layout.addWidget(QLabel("Output:"))
        self.output_area = QPlainTextEdit()
        self.output_area.setReadOnly(True)
        main_layout.addWidget(self.output_area)

        # Save to DB and export as file buttons
        save_export_layout = QHBoxLayout()
        self.save_to_db_button = QPushButton("Save to DB")
        save_export_layout.addWidget(self.save_to_db_button)

        self.export_to_file_button = QPushButton("Export as File")
        save_export_layout.addWidget(self.export_to_file_button)

        main_layout.addLayout(save_export_layout)

        # Set the main layout
        self.setLayout(main_layout)

        # Create the controller
        self.controller = HashCrackerController(self)

        # Connect GUI events to controller methods
        self.hash_file_upload.clicked.connect(self.controller.upload_hash_file)
        self.file_upload.clicked.connect(self.controller.upload_dictionary_file)
        self.start_button.clicked.connect(self.controller.start_cracking)
        self.save_to_db_button.clicked.connect(self.controller.save_to_db)
        self.export_to_file_button.clicked.connect(self.controller.export_to_file)
        self.analyze_hash_button.clicked.connect(self.controller.analyze_hash)


# Create the application
app = QApplication(sys.argv)

# Create the main window
window = HashCrackerGUI()
window.show()

# Start the event loop
sys.exit(app.exec_())




