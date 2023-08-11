import unittest
from model import HashCrackerModel
from controller import HashCrackerController
from unittest.mock import Mock
from unittest.mock import patch, Mock
from PyQt5.QtWidgets import QApplication


class TestHashCrackerIntegration(unittest.TestCase):

    app = None

    def setUp(self):

        if TestHashCrackerIntegration.app is None:
            TestHashCrackerIntegration.app = QApplication([])

        # Mocking the view since we're not testing GUI interactions in integration tests.
        self.mock_view = Mock()
        self.model = HashCrackerModel()

        with patch('PyQt5.QtCore.QTimer'):
            self.controller = HashCrackerController(self.mock_view)

    @patch('PyQt5.QtWidgets.QMessageBox.information')
    def test_analyze_hash_integration(self, mock_msgbox):
        self.mock_view.hash_analyze_input.text.return_value = "d41d8cd98f00b204e9800998ecf8427e"
        self.controller.analyze_hash()
        self.mock_view.hash_analyze_input.text.assert_called_once()
        mock_msgbox.assert_called()


@patch('model.DictionaryAttackThread')
@patch('PyQt5.QtWidgets.QMessageBox.warning')
@patch('PyQt5.QtWidgets.QFileDialog.getOpenFileName', return_value=("/path/to/dictionary.txt", "Text Files (*.txt)"))
def test_upload_and_crack_integration(self, mock_file_dialog, mock_warning_msgbox, mock_thread):

    mock_instance = mock_thread.return_value
    mock_instance.run = lambda: self.controller.queue.put(
        ("d41d8cd98f00b204e9800998ecf8427e", "password123"))

    self.mock_view.hash_input.text.return_value = "d41d8cd98f00b204e9800998ecf8427e"
    self.mock_view.hash_type.currentText.return_value = "MD5"
    self.controller.upload_dictionary_file()
    self.controller.start_cracking()


    self.controller.check_queue()


    self.mock_view.output_area.appendPlainText.assert_called_with(
        "Hash: d41d8cd98f00b204e9800998ecf8427e, Password: password123")

    # Add more integration tests as needed...

def tearDownClass(cls):

    if cls.app:
        cls.app.quit()

if __name__ == "__main__":
    unittest.main()
