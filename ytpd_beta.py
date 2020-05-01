# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ytpd_beta.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(825, 517)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:rgb(180, 182, 182)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(340, 10, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Menlo")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("color: rgb(252, 1, 7)")
        self.title_label.setText("TurboTubeMp3")
        self.title_label.setObjectName("title_label")
        self.enter_playlist_url_label = QtWidgets.QLabel(self.centralwidget)
        self.enter_playlist_url_label.setGeometry(QtCore.QRect(120, 330, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.enter_playlist_url_label.setFont(font)
        self.enter_playlist_url_label.setObjectName("enter_playlist_url_label")
        self.url_input = QtWidgets.QLineEdit(self.centralwidget)
        self.url_input.setGeometry(QtCore.QRect(120, 350, 480, 21))
        self.url_input.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.url_input.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.url_input.setObjectName("url_input")
        self.url_load_button = QtWidgets.QPushButton(self.centralwidget)
        self.url_load_button.setGeometry(QtCore.QRect(30, 350, 71, 23))
        self.url_load_button.setObjectName("url_load_button")
        self.remove_from_table_button = QtWidgets.QPushButton(self.centralwidget)
        self.remove_from_table_button.setGeometry(QtCore.QRect(660, 260, 131, 23))
        self.remove_from_table_button.setObjectName("remove_from_table_button")
        self.url_error_label = QtWidgets.QLabel(self.centralwidget)
        self.url_error_label.setGeometry(QtCore.QRect(440, 332, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.url_error_label.setFont(font)
        self.url_error_label.setObjectName("url_error_label")
        self.url_fetching_data_label = QtWidgets.QLabel(self.centralwidget)
        self.url_fetching_data_label.setGeometry(QtCore.QRect(520, 330, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        self.url_fetching_data_label.setFont(font)
        self.url_fetching_data_label.setObjectName("url_fetching_data_label")
        self.listWidget_label = QtWidgets.QLabel(self.centralwidget)
        self.listWidget_label.setGeometry(QtCore.QRect(30, 40, 101, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.listWidget_label.setFont(font)
        self.listWidget_label.setObjectName("listWidget_label")
        self.download_button = QtWidgets.QPushButton(self.centralwidget)
        self.download_button.setGeometry(QtCore.QRect(30, 450, 91, 23))
        self.download_button.setObjectName("download_button")
        self.downloaded_label = QtWidgets.QLabel(self.centralwidget)
        self.downloaded_label.setGeometry(QtCore.QRect(230, 380, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.downloaded_label.setFont(font)
        self.downloaded_label.setText("")
        self.downloaded_label.setObjectName("downloaded_label")
        self.download_path = QtWidgets.QPushButton(self.centralwidget)
        self.download_path.setGeometry(QtCore.QRect(30, 400, 71, 23))
        self.download_path.setAutoDefault(False)
        self.download_path.setObjectName("download_path")
        self.download_folder_select = QtWidgets.QLabel(self.centralwidget)
        self.download_folder_select.setGeometry(QtCore.QRect(120, 400, 480, 21))
        self.download_folder_select.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.download_folder_select.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.download_folder_select.setFrameShadow(QtWidgets.QFrame.Plain)
        self.download_folder_select.setObjectName("download_folder_select")
        self.video_table = QtWidgets.QTableWidget(self.centralwidget)
        self.video_table.setGeometry(QtCore.QRect(30, 60, 761, 192))
        self.video_table.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.video_table.setMidLineWidth(0)
        self.video_table.setRowCount(250)
        self.video_table.setColumnCount(5)
        self.video_table.setObjectName("video_table")
        item = QtWidgets.QTableWidgetItem()
        self.video_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.video_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.video_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.video_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.video_table.setHorizontalHeaderItem(4, item)
        self.video_table.horizontalHeader().setVisible(True)
        self.video_table.horizontalHeader().setCascadingSectionResizes(False)
        self.video_table.horizontalHeader().setDefaultSectionSize(143)
        self.video_table.verticalHeader().setDefaultSectionSize(25)
        self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_button.setGeometry(QtCore.QRect(140, 450, 91, 23))
        self.cancel_button.setObjectName("cancel_button")
        self.enter_playlist_url_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.enter_playlist_url_label_2.setGeometry(QtCore.QRect(120, 380, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.enter_playlist_url_label_2.setFont(font)
        self.enter_playlist_url_label_2.setObjectName("enter_playlist_url_label_2")
        self.set_artist = QtWidgets.QPushButton(self.centralwidget)
        self.set_artist.setGeometry(QtCore.QRect(100, 260, 71, 21))
        self.set_artist.setObjectName("set_artist")
        self.set_album = QtWidgets.QPushButton(self.centralwidget)
        self.set_album.setGeometry(QtCore.QRect(30, 260, 71, 21))
        self.set_album.setObjectName("set_album")
        self.set_genre = QtWidgets.QPushButton(self.centralwidget)
        self.set_genre.setGeometry(QtCore.QRect(171, 260, 71, 21))
        self.set_genre.setObjectName("set_genre")
        self.video_info_input = QtWidgets.QLineEdit(self.centralwidget)
        self.video_info_input.setGeometry(QtCore.QRect(340, 260, 260, 21))
        self.video_info_input.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.video_info_input.setObjectName("video_info_input")
        self.itunes_annotate = QtWidgets.QPushButton(self.centralwidget)
        self.itunes_annotate.setGeometry(QtCore.QRect(30, 290, 111, 21))
        self.itunes_annotate.setObjectName("itunes_annotate")
        self.revert_annotate = QtWidgets.QPushButton(self.centralwidget)
        self.revert_annotate.setGeometry(QtCore.QRect(30, 290, 111, 21))
        self.revert_annotate.setObjectName("revert_annotate")
        self.album_artwork = QtWidgets.QLabel(self.centralwidget)
        self.album_artwork.setGeometry(QtCore.QRect(630, 310, 171, 171))
        self.album_artwork.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.album_artwork.setFrameShape(QtWidgets.QFrame.Panel)
        self.album_artwork.setFrameShadow(QtWidgets.QFrame.Plain)
        self.album_artwork.setText("")
        self.album_artwork.setPixmap(QtGui.QPixmap("default_artwork.png"))
        self.album_artwork.setScaledContents(True)
        self.album_artwork.setAlignment(QtCore.Qt.AlignCenter)
        self.album_artwork.setObjectName("album_artwork")
        self.set_artwork = QtWidgets.QPushButton(self.centralwidget)
        self.set_artwork.setGeometry(QtCore.QRect(242, 260, 81, 21))
        self.set_artwork.setObjectName("set_artwork")
        self.change_video_info_input = QtWidgets.QPushButton(self.centralwidget)
        self.change_video_info_input.setGeometry(QtCore.QRect(529, 290, 71, 21))
        self.change_video_info_input.setObjectName("change_video_info_input")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 825, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.enter_playlist_url_label.setText(_translate("MainWindow", "Playlist or Video URL"))
        self.url_load_button.setText(_translate("MainWindow", "Load"))
        self.remove_from_table_button.setText(_translate("MainWindow", "Remove from table"))
        self.url_error_label.setText(_translate("MainWindow", "Could not retrieve URL. Try again."))
        self.url_fetching_data_label.setText(_translate("MainWindow", "Loading playlist..."))
        self.listWidget_label.setText(_translate("MainWindow", "Loaded videos:"))
        self.download_button.setText(_translate("MainWindow", "Download"))
        self.download_path.setText(_translate("MainWindow", "Folder"))
        self.download_folder_select.setText(_translate("MainWindow", "Folder: "))
        self.video_table.setSortingEnabled(False)
        item = self.video_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "song"))
        item = self.video_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "album"))
        item = self.video_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "artist"))
        item = self.video_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "genre"))
        item = self.video_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "artwork"))
        self.cancel_button.setText(_translate("MainWindow", "Cancel"))
        self.enter_playlist_url_label_2.setText(_translate("MainWindow", "Download Folder"))
        self.set_artist.setText(_translate("MainWindow", "Set artist"))
        self.set_album.setText(_translate("MainWindow", "Set album"))
        self.set_genre.setText(_translate("MainWindow", "Set genre"))
        self.itunes_annotate.setText(_translate("MainWindow", "iTunes annotate"))
        self.revert_annotate.setText(_translate("MainWindow", "Revert"))
        self.set_artwork.setText(_translate("MainWindow", "Set artwork"))
        self.change_video_info_input.setText(_translate("MainWindow", "Replace"))
