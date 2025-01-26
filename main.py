"""
入口文件
"""
import sys

from PyQt5.QtWidgets import QApplication

from ui.Index import Index

if __name__ == '__main__':
    # 创建app
    app = QApplication(sys.argv)
    # 获取屏幕信息
    screen = app.primaryScreen()
    geometry = screen.geometry()
    # 获取屏幕的宽度和高度
    screen_width = geometry.width()
    screen_height = geometry.height()
    # 运行主页面
    myWindow = Index(screen_width, screen_height)
    myWindow.show()
    # 退出
    sys.exit(app.exec_())
