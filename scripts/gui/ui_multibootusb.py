# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/multibootusb.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(629, 605)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_disk = QtWidgets.QGridLayout()
        self.gridLayout_disk.setContentsMargins(-1, 10, -1, -1)
        self.gridLayout_disk.setObjectName("gridLayout_disk")
        self.label_select_usb_disk = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_select_usb_disk.sizePolicy().hasHeightForWidth())
        self.label_select_usb_disk.setSizePolicy(sizePolicy)
        self.label_select_usb_disk.setMinimumSize(QtCore.QSize(100, 0))
        self.label_select_usb_disk.setObjectName("label_select_usb_disk")
        self.gridLayout_disk.addWidget(self.label_select_usb_disk, 0, 0, 1, 3)
        self.combo_drives = QtWidgets.QComboBox(self.centralwidget)
        self.combo_drives.setObjectName("combo_drives")
        self.gridLayout_disk.addWidget(self.combo_drives, 1, 0, 1, 3)
        self.button_detect_drives = QtWidgets.QPushButton(self.centralwidget)
        self.button_detect_drives.setObjectName("button_detect_drives")
        self.gridLayout_disk.addWidget(self.button_detect_drives, 1, 3, 1, 1)
        self.checkbox_all_drives = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_all_drives.setObjectName("checkbox_all_drives")
        self.gridLayout_disk.addWidget(self.checkbox_all_drives, 0, 3, 1, 1)
        self.group_usb_details = QtWidgets.QGroupBox(self.centralwidget)
        self.group_usb_details.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.group_usb_details.setFlat(False)
        self.group_usb_details.setCheckable(False)
        self.group_usb_details.setObjectName("group_usb_details")
        self.formLayout = QtWidgets.QFormLayout(self.group_usb_details)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.label_usb_dev = QtWidgets.QLabel(self.group_usb_details)
        self.label_usb_dev.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_usb_dev.setObjectName("label_usb_dev")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_usb_dev)
        self.usb_dev = QtWidgets.QLabel(self.group_usb_details)
        self.usb_dev.setText("")
        self.usb_dev.setObjectName("usb_dev")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.usb_dev)
        self.label_usb_vendor = QtWidgets.QLabel(self.group_usb_details)
        self.label_usb_vendor.setObjectName("label_usb_vendor")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_usb_vendor)
        self.usb_vendor = QtWidgets.QLabel(self.group_usb_details)
        self.usb_vendor.setText("")
        self.usb_vendor.setObjectName("usb_vendor")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.usb_vendor)
        self.label_usb_model = QtWidgets.QLabel(self.group_usb_details)
        self.label_usb_model.setObjectName("label_usb_model")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_usb_model)
        self.usb_model = QtWidgets.QLabel(self.group_usb_details)
        self.usb_model.setText("")
        self.usb_model.setObjectName("usb_model")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.usb_model)
        self.label_usb_size = QtWidgets.QLabel(self.group_usb_details)
        self.label_usb_size.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_usb_size.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_usb_size.setObjectName("label_usb_size")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_usb_size)
        self.usb_size = QtWidgets.QLabel(self.group_usb_details)
        self.usb_size.setText("")
        self.usb_size.setObjectName("usb_size")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.usb_size)
        self.label_usb_mount = QtWidgets.QLabel(self.group_usb_details)
        self.label_usb_mount.setObjectName("label_usb_mount")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_usb_mount)
        self.usb_mount = QtWidgets.QLabel(self.group_usb_details)
        self.usb_mount.setText("")
        self.usb_mount.setObjectName("usb_mount")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.usb_mount)
        self.label_usb_type = QtWidgets.QLabel(self.group_usb_details)
        self.label_usb_type.setObjectName("label_usb_type")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_usb_type)
        self.usb_type = QtWidgets.QLabel(self.group_usb_details)
        self.usb_type.setText("")
        self.usb_type.setObjectName("usb_type")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.usb_type)
        self.label_usb_fs = QtWidgets.QLabel(self.group_usb_details)
        self.label_usb_fs.setObjectName("label_usb_fs")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_usb_fs)
        self.usb_fs = QtWidgets.QLabel(self.group_usb_details)
        self.usb_fs.setText("")
        self.usb_fs.setObjectName("usb_fs")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.usb_fs)
        self.gridLayout_disk.addWidget(self.group_usb_details, 3, 0, 1, 4)
        self.horizontalLayout.addLayout(self.gridLayout_disk)
        self.gridLayout_image = QtWidgets.QGridLayout()
        self.gridLayout_image.setContentsMargins(10, 10, -1, -1)
        self.gridLayout_image.setObjectName("gridLayout_image")
        self.image_details_group = QtWidgets.QGroupBox(self.centralwidget)
        self.image_details_group.setObjectName("image_details_group")
        self.formLayout_2 = QtWidgets.QFormLayout(self.image_details_group)
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_image_type = QtWidgets.QLabel(self.image_details_group)
        self.label_image_type.setObjectName("label_image_type")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_image_type)
        self.label_image_type_value = QtWidgets.QLabel(self.image_details_group)
        self.label_image_type_value.setText("")
        self.label_image_type_value.setObjectName("label_image_type_value")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_image_type_value)
        self.label_image_size = QtWidgets.QLabel(self.image_details_group)
        self.label_image_size.setObjectName("label_image_size")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_image_size)
        self.label_image_size_value = QtWidgets.QLabel(self.image_details_group)
        self.label_image_size_value.setText("")
        self.label_image_size_value.setObjectName("label_image_size_value")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_image_size_value)
        self.label_image_bootable = QtWidgets.QLabel(self.image_details_group)
        self.label_image_bootable.setObjectName("label_image_bootable")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_image_bootable)
        self.label_image_bootable_value = QtWidgets.QLabel(self.image_details_group)
        self.label_image_bootable_value.setText("")
        self.label_image_bootable_value.setObjectName("label_image_bootable_value")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_image_bootable_value)
        self.gridLayout_image.addWidget(self.image_details_group, 2, 0, 1, 2)
        self.button_browse_image = QtWidgets.QPushButton(self.centralwidget)
        self.button_browse_image.setCheckable(False)
        self.button_browse_image.setFlat(False)
        self.button_browse_image.setObjectName("button_browse_image")
        self.gridLayout_image.addWidget(self.button_browse_image, 0, 1, 1, 1)
        self.label_select_image = QtWidgets.QLabel(self.centralwidget)
        self.label_select_image.setObjectName("label_select_image")
        self.gridLayout_image.addWidget(self.label_select_image, 0, 0, 1, 1)
        self.image_path = QtWidgets.QLineEdit(self.centralwidget)
        self.image_path.setObjectName("image_path")
        self.gridLayout_image.addWidget(self.image_path, 1, 0, 1, 2)
        self.horizontalLayout.addLayout(self.gridLayout_image)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_multibootusb = QtWidgets.QWidget()
        self.tab_multibootusb.setEnabled(True)
        self.tab_multibootusb.setObjectName("tab_multibootusb")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_multibootusb)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.button_uninstall_distro = QtWidgets.QPushButton(self.tab_multibootusb)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon_uninstall"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_uninstall_distro.setIcon(icon)
        self.button_uninstall_distro.setIconSize(QtCore.QSize(16, 18))
        self.button_uninstall_distro.setObjectName("button_uninstall_distro")
        self.gridLayout.addWidget(self.button_uninstall_distro, 0, 3, 1, 1)
        self.button_install_distro = QtWidgets.QPushButton(self.tab_multibootusb)
        self.button_install_distro.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon_install"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_install_distro.setIcon(icon1)
        self.button_install_distro.setIconSize(QtCore.QSize(16, 18))
        self.button_install_distro.setObjectName("button_install_distro")
        self.gridLayout.addWidget(self.button_install_distro, 0, 2, 1, 1)
        self.slider_persistence = QtWidgets.QSlider(self.tab_multibootusb)
        self.slider_persistence.setEnabled(False)
        self.slider_persistence.setAutoFillBackground(False)
        self.slider_persistence.setOrientation(QtCore.Qt.Horizontal)
        self.slider_persistence.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.slider_persistence.setObjectName("slider_persistence")
        self.gridLayout.addWidget(self.slider_persistence, 2, 0, 1, 2)
        self.installed_distros = QtWidgets.QListWidget(self.tab_multibootusb)
        self.installed_distros.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.installed_distros.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.installed_distros.setResizeMode(QtWidgets.QListView.Fixed)
        self.installed_distros.setObjectName("installed_distros")
        self.gridLayout.addWidget(self.installed_distros, 2, 2, 2, 2)
        self.label_persistence = QtWidgets.QLabel(self.tab_multibootusb)
        self.label_persistence.setEnabled(False)
        self.label_persistence.setMouseTracking(True)
        self.label_persistence.setStyleSheet("font-weight: 600")
        self.label_persistence.setObjectName("label_persistence")
        self.gridLayout.addWidget(self.label_persistence, 0, 0, 1, 1)
        self.label_persistence_value = QtWidgets.QLabel(self.tab_multibootusb)
        self.label_persistence_value.setEnabled(False)
        self.label_persistence_value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_persistence_value.setObjectName("label_persistence_value")
        self.gridLayout.addWidget(self.label_persistence_value, 0, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.tab_multibootusb, "")
        self.tab_imager = QtWidgets.QWidget()
        self.tab_imager.setEnabled(True)
        self.tab_imager.setObjectName("tab_imager")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.tab_imager)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_9.setObjectName("gridLayout_9")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem, 3, 2, 1, 1)
        self.button_write_image_to_disk = QtWidgets.QPushButton(self.tab_imager)
        self.button_write_image_to_disk.setObjectName("button_write_image_to_disk")
        self.gridLayout_9.addWidget(self.button_write_image_to_disk, 3, 1, 1, 1)
        self.widget_7 = QtWidgets.QWidget(self.tab_imager)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_9.addWidget(self.widget_7, 3, 3, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem1, 3, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem2, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_imager)
        self.label_6.setObjectName("label_6")
        self.gridLayout_9.addWidget(self.label_6, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem3, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem4, 2, 1, 1, 1)
        self.horizontalLayout_7.addLayout(self.gridLayout_9)
        self.tabWidget.addTab(self.tab_imager, "")
        self.tab_syslinux = QtWidgets.QWidget()
        self.tab_syslinux.setObjectName("tab_syslinux")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_syslinux)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_syslinux)
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.check_install_sys_only = QtWidgets.QRadioButton(self.groupBox_2)
        self.check_install_sys_only.setObjectName("check_install_sys_only")
        self.gridLayout_3.addWidget(self.check_install_sys_only, 0, 0, 1, 1)
        self.check_install_sys_all = QtWidgets.QRadioButton(self.groupBox_2)
        self.check_install_sys_all.setObjectName("check_install_sys_all")
        self.gridLayout_3.addWidget(self.check_install_sys_all, 1, 0, 1, 1)
        self.button_install_syslinux = QtWidgets.QPushButton(self.groupBox_2)
        self.button_install_syslinux.setObjectName("button_install_syslinux")
        self.gridLayout_3.addWidget(self.button_install_syslinux, 0, 2, 2, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 0, 1, 2, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_3)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem6, 3, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_syslinux)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.button_edit_syslinux = QtWidgets.QPushButton(self.groupBox_3)
        self.button_edit_syslinux.setObjectName("button_edit_syslinux")
        self.gridLayout_4.addWidget(self.button_edit_syslinux, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem7, 0, 1, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout_4)
        self.gridLayout_2.addWidget(self.groupBox_3, 2, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem8, 1, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        self.tabWidget.addTab(self.tab_syslinux, "")
        self.tab_testboot = QtWidgets.QWidget()
        self.tab_testboot.setObjectName("tab_testboot")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_testboot)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setContentsMargins(-1, 10, -1, -1)
        self.gridLayout_6.setVerticalSpacing(20)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_testboot)
        self.groupBox_4.setStyleSheet("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.combo_usb_boot_ram = QtWidgets.QComboBox(self.groupBox_4)
        self.combo_usb_boot_ram.setObjectName("combo_usb_boot_ram")
        self.combo_usb_boot_ram.addItem("")
        self.combo_usb_boot_ram.addItem("")
        self.combo_usb_boot_ram.addItem("")
        self.combo_usb_boot_ram.addItem("")
        self.combo_usb_boot_ram.addItem("")
        self.combo_usb_boot_ram.addItem("")
        self.gridLayout_8.addWidget(self.combo_usb_boot_ram, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setObjectName("label_4")
        self.gridLayout_8.addWidget(self.label_4, 0, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem9, 0, 5, 1, 1)
        self.boot_usb_qemu = QtWidgets.QPushButton(self.groupBox_4)
        self.boot_usb_qemu.setObjectName("boot_usb_qemu")
        self.gridLayout_8.addWidget(self.boot_usb_qemu, 0, 4, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem10, 0, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.gridLayout_8.addWidget(self.label_5, 0, 2, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_8)
        self.gridLayout_6.addWidget(self.groupBox_4, 1, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_testboot)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setObjectName("label_3")
        self.gridLayout_7.addWidget(self.label_3, 0, 0, 1, 1)
        self.boot_iso_qemu = QtWidgets.QPushButton(self.groupBox_5)
        self.boot_iso_qemu.setObjectName("boot_iso_qemu")
        self.gridLayout_7.addWidget(self.boot_iso_qemu, 0, 4, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem11, 0, 3, 1, 1)
        self.combo_iso_boot_ram = QtWidgets.QComboBox(self.groupBox_5)
        self.combo_iso_boot_ram.setObjectName("combo_iso_boot_ram")
        self.combo_iso_boot_ram.addItem("")
        self.combo_iso_boot_ram.addItem("")
        self.combo_iso_boot_ram.addItem("")
        self.combo_iso_boot_ram.addItem("")
        self.combo_iso_boot_ram.addItem("")
        self.combo_iso_boot_ram.addItem("")
        self.gridLayout_7.addWidget(self.combo_iso_boot_ram, 0, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem12, 0, 5, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_5)
        self.label.setObjectName("label")
        self.gridLayout_7.addWidget(self.label, 0, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_7)
        self.gridLayout_6.addWidget(self.groupBox_5, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_6)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem13)
        self.tabWidget.addTab(self.tab_testboot, "")
        self.verticalLayout_7.addWidget(self.tabWidget)
        self.progressbar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressbar.setProperty("value", 0)
        self.progressbar.setInvertedAppearance(False)
        self.progressbar.setObjectName("progressbar")
        self.verticalLayout_7.addWidget(self.progressbar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 629, 19))
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Quit = QtWidgets.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")
        self.action_About = QtWidgets.QAction(MainWindow)
        self.action_About.setObjectName("action_About")
        self.menuFile.addAction(self.action_Quit)
        self.menu_Help.addAction(self.action_About)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MultiBootUSB"))
        self.label_select_usb_disk.setText(_translate("MainWindow", "<b>Select USB disk</b>"))
        self.button_detect_drives.setText(_translate("MainWindow", "Detect Drives"))
        self.checkbox_all_drives.setText(_translate("MainWindow", "All Drives"))
        self.group_usb_details.setTitle(_translate("MainWindow", "USB Details"))
        self.label_usb_dev.setText(_translate("MainWindow", "Drive:"))
        self.label_usb_vendor.setText(_translate("MainWindow", "Vendor:"))
        self.label_usb_model.setText(_translate("MainWindow", "Model:"))
        self.label_usb_size.setText(_translate("MainWindow", "Size:"))
        self.label_usb_mount.setText(_translate("MainWindow", "Mount:"))
        self.label_usb_type.setText(_translate("MainWindow", "Type:"))
        self.label_usb_fs.setText(_translate("MainWindow", "Filesystem:"))
        self.image_details_group.setTitle(_translate("MainWindow", "Image Details"))
        self.label_image_type.setText(_translate("MainWindow", "Type:"))
        self.label_image_size.setText(_translate("MainWindow", "Size:"))
        self.label_image_bootable.setText(_translate("MainWindow", "Boot:"))
        self.button_browse_image.setText(_translate("MainWindow", "Browse"))
        self.label_select_image.setText(_translate("MainWindow", "<b>Select image</b>"))
        self.button_uninstall_distro.setText(_translate("MainWindow", "Uninstall distro"))
        self.button_install_distro.setText(_translate("MainWindow", "Install distro"))
        self.slider_persistence.setToolTip(_translate("MainWindow", "Choose Persistence size. Not all distros supports persistence..."))
        self.label_persistence.setText(_translate("MainWindow", "Persistence"))
        self.label_persistence_value.setText(_translate("MainWindow", "0 MB"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_multibootusb), _translate("MainWindow", "MultiBootUSB"))
        self.button_write_image_to_disk.setText(_translate("MainWindow", "Write image to USB"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ff0000;\">WARNING!</span></p><p align=\"center\"><span style=\" color:#000000;\">This operation destroys </span><span style=\" font-weight:600; color:#000000;\">ALL</span><span style=\" color:#000000;\"> data on the selected disk.</span></p><p align=\"center\"><span style=\" color:#000000;\">Please select the destination disk carefully.</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_imager), _translate("MainWindow", "Write Image to disk"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Install Syslinux"))
        self.check_install_sys_only.setText(_translate("MainWindow", "Install only syslinu&x (existing configurations will not be altered)."))
        self.check_install_sys_all.setText(_translate("MainWindow", "Install syslinux and copy all re&quired files."))
        self.button_install_syslinux.setText(_translate("MainWindow", "Install"))
        self.groupBox_3.setTitle(_translate("MainWindow", "syslinux.cfg"))
        self.button_edit_syslinux.setText(_translate("MainWindow", "Edit"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\">Edit syslinux.cfg file using the default editor. </p><p align=\"justify\">Be <span style=\" font-weight:600; color:#ff0000;\">CAREFUL</span> while editing syslinux.cfg!</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_syslinux), _translate("MainWindow", "Install Syslinux"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Boot USB :: Test bootable USB drive without reboot"))
        self.combo_usb_boot_ram.setItemText(0, _translate("MainWindow", "Default"))
        self.combo_usb_boot_ram.setItemText(1, _translate("MainWindow", "256"))
        self.combo_usb_boot_ram.setItemText(2, _translate("MainWindow", "512"))
        self.combo_usb_boot_ram.setItemText(3, _translate("MainWindow", "768"))
        self.combo_usb_boot_ram.setItemText(4, _translate("MainWindow", "1024"))
        self.combo_usb_boot_ram.setItemText(5, _translate("MainWindow", "2048"))
        self.label_4.setText(_translate("MainWindow", "Choose RAM size:"))
        self.boot_usb_qemu.setText(_translate("MainWindow", "Boot &USB"))
        self.label_5.setText(_translate("MainWindow", "MB"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Boot ISO :: Test bootable ISOs without reboot"))
        self.label_3.setText(_translate("MainWindow", "Choose RAM size:"))
        self.boot_iso_qemu.setText(_translate("MainWindow", "Boot &ISO"))
        self.combo_iso_boot_ram.setItemText(0, _translate("MainWindow", "Default"))
        self.combo_iso_boot_ram.setItemText(1, _translate("MainWindow", "256"))
        self.combo_iso_boot_ram.setItemText(2, _translate("MainWindow", "512"))
        self.combo_iso_boot_ram.setItemText(3, _translate("MainWindow", "768"))
        self.combo_iso_boot_ram.setItemText(4, _translate("MainWindow", "1024"))
        self.combo_iso_boot_ram.setItemText(5, _translate("MainWindow", "2048"))
        self.label.setText(_translate("MainWindow", "MB"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_testboot), _translate("MainWindow", "Boot ISO/USB"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help"))
        self.action_Quit.setText(_translate("MainWindow", "&Quit"))
        self.action_About.setText(_translate("MainWindow", "&About"))

