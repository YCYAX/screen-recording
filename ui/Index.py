"""
主页
"""
import tomlkit
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog


class Index(QWidget):
    def __init__(self, width, high):
        """
        :param width: 屏幕宽
        :param high: 屏幕高
        """
        super().__init__()
        """
        全局属性
        """
        self.HIGH = int(high * 0.5)
        self.WIDTH = int(width * 0.5)
        """
        窗口属性
        """
        # 大小
        self.resize(self.WIDTH, self.HIGH)
        # 标题
        self.setWindowTitle("全屏录制助手")
        """
        全布局
        """
        # 主垂直布局
        self.mainLayout = QHBoxLayout()
        self.setLayout(self.mainLayout)
        # 功能按钮布局第一行
        self.oneFunctionLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.oneFunctionLayout)
        # init ui
        self.ui()

    def ui(self):
        # 存储路径按钮
        self.outPathButton = QPushButton("存储按钮")
        self.outPathButton.clicked.connect(self.out_path_url)
        self.oneFunctionLayout.addWidget(self.outPathButton)

    def out_path_url(self):

        """
        选择模板路径
        :return: None
        """
        # get dir url
        url = QFileDialog.getExistingDirectoryUrl().path()[1:]
        # set ui url and config url
        self.openurlEdit.setText(url)
        with open('./config/cfg.toml', 'r', encoding='utf-8') as f:
            file = tomlkit.load(f)
            file['config']['openUrl'] = url
        with open('./config/cfg.toml', 'w', encoding='utf-8') as f:
            tomlkit.dump(file, f)
        self.openurl = url
