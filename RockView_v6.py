from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QCheckBox
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RockView(object):
    def setupUi(self, RockView):
        RockView.setObjectName("RockView")
        RockView.resize(752, 741)
        font = QtGui.QFont()
        font.setPointSize(12)
        RockView.setFont(font)
        RockView.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        RockView.setWindowIcon(QtGui.QIcon('RV_Icon.ico'))
        self.centralwidget = QtWidgets.QWidget(RockView)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_browse_button = QtWidgets.QVBoxLayout()
        self.verticalLayout_browse_button.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout_browse_button.setSpacing(0)
        self.verticalLayout_browse_button.setObjectName("verticalLayout_browse_button")
        self.browse_las_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browse_las_button.sizePolicy().hasHeightForWidth())
        self.browse_las_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.browse_las_button.setFont(font)
        self.browse_las_button.setObjectName("browse_las_button")
        self.verticalLayout_browse_button.addWidget(self.browse_las_button)
        self.gridLayout_2.addLayout(self.verticalLayout_browse_button, 0, 0, 1, 1)
        self.verticalLayout_browse_button_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_browse_button_6.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout_browse_button_6.setSpacing(0)
        self.verticalLayout_browse_button_6.setObjectName("verticalLayout_browse_button_6")
        self.browse_bedding_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browse_bedding_button.sizePolicy().hasHeightForWidth())
        self.browse_bedding_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.browse_bedding_button.setFont(font)
        self.browse_bedding_button.setObjectName("browse_bedding_button")
        self.verticalLayout_browse_button_6.addWidget(self.browse_bedding_button)
        self.gridLayout_2.addLayout(self.verticalLayout_browse_button_6, 1, 0, 1, 1)
        self.verticalLayout_browse_button_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_browse_button_7.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout_browse_button_7.setSpacing(0)
        self.verticalLayout_browse_button_7.setObjectName("verticalLayout_browse_button_7")
        self.conductivity_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.conductivity_label_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.conductivity_label_2.sizePolicy().hasHeightForWidth())
        self.conductivity_label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.conductivity_label_2.setFont(font)
        self.conductivity_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.conductivity_label_2.setObjectName("conductivity_label_2")
        self.verticalLayout_browse_button_7.addWidget(self.conductivity_label_2)
        self.gridLayout_2.addLayout(self.verticalLayout_browse_button_7, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.homo_label = QtWidgets.QLabel(self.centralwidget)
        self.homo_label.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.homo_label.setFont(font)
        self.homo_label.setAlignment(QtCore.Qt.AlignCenter)
        self.homo_label.setObjectName("homo_label")
        self.horizontalLayout.addWidget(self.homo_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.homo_value = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.homo_value.sizePolicy().hasHeightForWidth())
        self.homo_value.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.homo_value.setFont(font)
        self.homo_value.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.homo_value.setAlignment(QtCore.Qt.AlignCenter)
        self.homo_value.setObjectName("homo_value")
        self.horizontalLayout.addWidget(self.homo_value)
        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.verticalLayout_browse_button_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_browse_button_2.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout_browse_button_2.setSpacing(0)
        self.verticalLayout_browse_button_2.setObjectName("verticalLayout_browse_button_2")
        self.static_elastic_params_label = QtWidgets.QLabel(self.centralwidget)
        self.static_elastic_params_label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.static_elastic_params_label.sizePolicy().hasHeightForWidth())
        self.static_elastic_params_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.static_elastic_params_label.setFont(font)
        self.static_elastic_params_label.setAlignment(QtCore.Qt.AlignCenter)
        self.static_elastic_params_label.setObjectName("static_elastic_params_label")
        self.verticalLayout_browse_button_2.addWidget(self.static_elastic_params_label)
        self.gridLayout_2.addLayout(self.verticalLayout_browse_button_2, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.static_elastic_params_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.static_elastic_params_label_2.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.static_elastic_params_label_2.setFont(font)
        self.static_elastic_params_label_2.setTextFormat(QtCore.Qt.RichText)
        self.static_elastic_params_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.static_elastic_params_label_2.setObjectName("static_elastic_params_label_2")
        self.horizontalLayout_2.addWidget(self.static_elastic_params_label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.static_elastic_params_a_label = QtWidgets.QLabel(self.centralwidget)
        self.static_elastic_params_a_label.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.static_elastic_params_a_label.setFont(font)
        self.static_elastic_params_a_label.setAlignment(QtCore.Qt.AlignCenter)
        self.static_elastic_params_a_label.setObjectName("static_elastic_params_a_label")
        self.horizontalLayout_2.addWidget(self.static_elastic_params_a_label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.static_elastic_params_a_float = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.static_elastic_params_a_float.sizePolicy().hasHeightForWidth())
        self.static_elastic_params_a_float.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.static_elastic_params_a_float.setFont(font)
        self.static_elastic_params_a_float.setToolTip("")
        self.static_elastic_params_a_float.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.static_elastic_params_a_float.setAlignment(QtCore.Qt.AlignCenter)
        self.static_elastic_params_a_float.setObjectName("static_elastic_params_a_float")
        self.horizontalLayout_2.addWidget(self.static_elastic_params_a_float)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.static_elastic_params_b_label = QtWidgets.QLabel(self.centralwidget)
        self.static_elastic_params_b_label.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.static_elastic_params_b_label.setFont(font)
        self.static_elastic_params_b_label.setAlignment(QtCore.Qt.AlignCenter)
        self.static_elastic_params_b_label.setObjectName("static_elastic_params_b_label")
        self.horizontalLayout_2.addWidget(self.static_elastic_params_b_label)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.static_elastic_params_b_float = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.static_elastic_params_b_float.sizePolicy().hasHeightForWidth())
        self.static_elastic_params_b_float.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.static_elastic_params_b_float.setFont(font)
        self.static_elastic_params_b_float.setToolTip("")
        self.static_elastic_params_b_float.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.static_elastic_params_b_float.setAlignment(QtCore.Qt.AlignCenter)
        self.static_elastic_params_b_float.setObjectName("static_elastic_params_b_float")
        self.horizontalLayout_2.addWidget(self.static_elastic_params_b_float)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 5, 0, 1, 1)
        self.verticalLayout_browse_button_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_browse_button_3.setContentsMargins(-1, 5, 0, 5)
        self.verticalLayout_browse_button_3.setSpacing(0)
        self.verticalLayout_browse_button_3.setObjectName("verticalLayout_browse_button_3")
        self.frac_toughness_params_label = QtWidgets.QLabel(self.centralwidget)
        self.frac_toughness_params_label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frac_toughness_params_label.sizePolicy().hasHeightForWidth())
        self.frac_toughness_params_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.frac_toughness_params_label.setFont(font)
        self.frac_toughness_params_label.setAlignment(QtCore.Qt.AlignCenter)
        self.frac_toughness_params_label.setObjectName("frac_toughness_params_label")
        self.verticalLayout_browse_button_3.addWidget(self.frac_toughness_params_label)
        self.gridLayout_2.addLayout(self.verticalLayout_browse_button_3, 6, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.k1c_iso_label = QtWidgets.QLabel(self.centralwidget)
        self.k1c_iso_label.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.k1c_iso_label.setFont(font)
        self.k1c_iso_label.setTextFormat(QtCore.Qt.RichText)
        self.k1c_iso_label.setAlignment(QtCore.Qt.AlignCenter)
        self.k1c_iso_label.setObjectName("k1c_iso_label")
        self.horizontalLayout_3.addWidget(self.k1c_iso_label)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.k1c_m_label = QtWidgets.QLabel(self.centralwidget)
        self.k1c_m_label.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.k1c_m_label.setFont(font)
        self.k1c_m_label.setAlignment(QtCore.Qt.AlignCenter)
        self.k1c_m_label.setObjectName("k1c_m_label")
        self.horizontalLayout_3.addWidget(self.k1c_m_label)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.k1c_value = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.k1c_value.sizePolicy().hasHeightForWidth())
        self.k1c_value.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.k1c_value.setFont(font)
        self.k1c_value.setToolTip("")
        self.k1c_value.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.k1c_value.setAlignment(QtCore.Qt.AlignCenter)
        self.k1c_value.setObjectName("k1c_value")
        self.horizontalLayout_3.addWidget(self.k1c_value)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 7, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.k1c_vti_label = QtWidgets.QLabel(self.centralwidget)
        self.k1c_vti_label.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.k1c_vti_label.setFont(font)
        self.k1c_vti_label.setTextFormat(QtCore.Qt.RichText)
        self.k1c_vti_label.setAlignment(QtCore.Qt.AlignCenter)
        self.k1c_vti_label.setObjectName("k1c_vti_label")
        self.horizontalLayout_4.addWidget(self.k1c_vti_label)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.k1c_v_label = QtWidgets.QLabel(self.centralwidget)
        self.k1c_v_label.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.k1c_v_label.setFont(font)
        self.k1c_v_label.setTextFormat(QtCore.Qt.RichText)
        self.k1c_v_label.setAlignment(QtCore.Qt.AlignCenter)
        self.k1c_v_label.setObjectName("k1c_v_label")
        self.horizontalLayout_4.addWidget(self.k1c_v_label)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.k1c_v_value = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.k1c_v_value.sizePolicy().hasHeightForWidth())
        self.k1c_v_value.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.k1c_v_value.setFont(font)
        self.k1c_v_value.setToolTip("")
        self.k1c_v_value.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.k1c_v_value.setAlignment(QtCore.Qt.AlignCenter)
        self.k1c_v_value.setObjectName("k1c_v_value")
        self.horizontalLayout_4.addWidget(self.k1c_v_value)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.k1c_h_value = QtWidgets.QLabel(self.centralwidget)
        self.k1c_h_value.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.k1c_h_value.setFont(font)
        self.k1c_h_value.setTextFormat(QtCore.Qt.RichText)
        self.k1c_h_value.setAlignment(QtCore.Qt.AlignCenter)
        self.k1c_h_value.setObjectName("k1c_h_value")
        self.horizontalLayout_4.addWidget(self.k1c_h_value)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.k1c_h_label = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.k1c_h_label.sizePolicy().hasHeightForWidth())
        self.k1c_h_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.k1c_h_label.setFont(font)
        self.k1c_h_label.setToolTip("")
        self.k1c_h_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.k1c_h_label.setAlignment(QtCore.Qt.AlignCenter)
        self.k1c_h_label.setObjectName("k1c_h_label")
        self.horizontalLayout_4.addWidget(self.k1c_h_label)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 8, 0, 1, 1)
        self.verticalLayout_browse_button_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_browse_button_4.setContentsMargins(-1, 5, 0, 5)
        self.verticalLayout_browse_button_4.setSpacing(0)
        self.verticalLayout_browse_button_4.setObjectName("verticalLayout_browse_button_4")
        self.frac_toughness_params_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.frac_toughness_params_label_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frac_toughness_params_label_2.sizePolicy().hasHeightForWidth())
        self.frac_toughness_params_label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.frac_toughness_params_label_2.setFont(font)
        self.frac_toughness_params_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.frac_toughness_params_label_2.setObjectName("frac_toughness_params_label_2")
        self.verticalLayout_browse_button_4.addWidget(self.frac_toughness_params_label_2)
        self.gridLayout_2.addLayout(self.verticalLayout_browse_button_4, 9, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.cf_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.cf_label_2.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.cf_label_2.setFont(font)
        self.cf_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.cf_label_2.setObjectName("cf_label_2")
        self.horizontalLayout_6.addWidget(self.cf_label_2)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem11)
        self.leak_off_value = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leak_off_value.sizePolicy().hasHeightForWidth())
        self.leak_off_value.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.leak_off_value.setFont(font)
        self.leak_off_value.setToolTip("")
        self.leak_off_value.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.leak_off_value.setAlignment(QtCore.Qt.AlignCenter)
        self.leak_off_value.setObjectName("leak_off_value")
        self.horizontalLayout_6.addWidget(self.leak_off_value)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem12)
        self.leak_off_unit_label = QtWidgets.QLabel(self.centralwidget)
        self.leak_off_unit_label.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.leak_off_unit_label.setFont(font)
        self.leak_off_unit_label.setAlignment(QtCore.Qt.AlignCenter)
        self.leak_off_unit_label.setObjectName("leak_off_unit_label")
        self.horizontalLayout_6.addWidget(self.leak_off_unit_label)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 10, 0, 1, 1)
        self.verticalLayout_browse_button_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_browse_button_5.setContentsMargins(-1, 5, 0, 5)
        self.verticalLayout_browse_button_5.setSpacing(0)
        self.verticalLayout_browse_button_5.setObjectName("verticalLayout_browse_button_5")
        self.conductivity_label = QtWidgets.QLabel(self.centralwidget)
        self.conductivity_label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.conductivity_label.sizePolicy().hasHeightForWidth())
        self.conductivity_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.conductivity_label.setFont(font)
        self.conductivity_label.setAlignment(QtCore.Qt.AlignCenter)
        self.conductivity_label.setObjectName("conductivity_label")
        self.verticalLayout_browse_button_5.addWidget(self.conductivity_label)
        self.gridLayout_2.addLayout(self.verticalLayout_browse_button_5, 11, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.matrix_perm_label = QtWidgets.QLabel(self.centralwidget)
        self.matrix_perm_label.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.matrix_perm_label.setFont(font)
        self.matrix_perm_label.setAlignment(QtCore.Qt.AlignCenter)
        self.matrix_perm_label.setObjectName("matrix_perm_label")
        self.horizontalLayout_5.addWidget(self.matrix_perm_label)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem13)
        self.matrix_perm_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.matrix_perm_label_2.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.matrix_perm_label_2.setFont(font)
        self.matrix_perm_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.matrix_perm_label_2.setObjectName("matrix_perm_label_2")
        self.horizontalLayout_5.addWidget(self.matrix_perm_label_2)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem14)
        self.matrix_perm_value = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.matrix_perm_value.sizePolicy().hasHeightForWidth())
        self.matrix_perm_value.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.matrix_perm_value.setFont(font)
        self.matrix_perm_value.setToolTip("")
        self.matrix_perm_value.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.matrix_perm_value.setAlignment(QtCore.Qt.AlignCenter)
        self.matrix_perm_value.setObjectName("matrix_perm_value")
        self.horizontalLayout_5.addWidget(self.matrix_perm_value)
        self.matrix_perm_unit = QtWidgets.QLabel(self.centralwidget)
        self.matrix_perm_unit.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.matrix_perm_unit.setFont(font)
        self.matrix_perm_unit.setAlignment(QtCore.Qt.AlignCenter)
        self.matrix_perm_unit.setObjectName("matrix_perm_unit")
        self.horizontalLayout_5.addWidget(self.matrix_perm_unit)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 12, 0, 1, 1)
        self.verticalLayout_browse_button_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_browse_button_9.setContentsMargins(5, 5, 5, 0)
        self.verticalLayout_browse_button_9.setSpacing(0)
        self.verticalLayout_browse_button_9.setObjectName("verticalLayout_browse_button_9")
        self.form_characterization_label = QtWidgets.QLabel(self.centralwidget)
        self.form_characterization_label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.form_characterization_label.sizePolicy().hasHeightForWidth())
        self.form_characterization_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.form_characterization_label.setFont(font)
        self.form_characterization_label.setAlignment(QtCore.Qt.AlignCenter)
        self.form_characterization_label.setObjectName("form_characterization_label")
        self.verticalLayout_browse_button_9.addWidget(self.form_characterization_label)
        self.gridLayout_2.addLayout(self.verticalLayout_browse_button_9, 13, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(5, -1, 5, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.iso_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.iso_checkbox.setFont(font)
        self.iso_checkbox.setObjectName("iso_checkbox")
        self.gridLayout.addWidget(self.iso_checkbox, 0, 1, 1, 1)
        self.vti_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.vti_checkbox.setFont(font)
        self.vti_checkbox.setObjectName("vti_checkbox")
        self.gridLayout.addWidget(self.vti_checkbox, 0, 2, 1, 1)
        self.medium_label = QtWidgets.QLabel(self.centralwidget)
        self.medium_label.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.medium_label.setFont(font)
        self.medium_label.setObjectName("medium_label")
        self.gridLayout.addWidget(self.medium_label, 0, 0, 1, 1)
        self.medium_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.medium_label_2.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.medium_label_2.setFont(font)
        self.medium_label_2.setObjectName("medium_label_2")
        self.gridLayout.addWidget(self.medium_label_2, 1, 0, 1, 1)
        self.sand_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.sand_checkbox.setFont(font)
        self.sand_checkbox.setObjectName("sand_checkbox")
        self.gridLayout.addWidget(self.sand_checkbox, 1, 1, 1, 1)
        self.shale_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.shale_checkbox.setFont(font)
        self.shale_checkbox.setObjectName("shale_checkbox")
        self.gridLayout.addWidget(self.shale_checkbox, 1, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 14, 0, 1, 1)
        self.verticalLayout_browse_button_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_browse_button_8.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout_browse_button_8.setSpacing(0)
        self.verticalLayout_browse_button_8.setObjectName("verticalLayout_browse_button_8")
        self.view_plot_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.view_plot_button.sizePolicy().hasHeightForWidth())
        self.view_plot_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.view_plot_button.setFont(font)
        self.view_plot_button.setObjectName("view_plot_button")
        self.verticalLayout_browse_button_8.addWidget(self.view_plot_button)
        self.gridLayout_2.addLayout(self.verticalLayout_browse_button_8, 15, 0, 1, 1)
        RockView.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(RockView)
        self.statusbar.setObjectName("statusbar")
        RockView.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(RockView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 752, 26))
        self.menubar.setObjectName("menubar")
        RockView.setMenuBar(self.menubar)

        self.retranslateUi(RockView)
        QtCore.QMetaObject.connectSlotsByName(RockView)

       # Browse button functionality

        def open_csv_file(self):
            global rock_props
            filename, _ = QtWidgets.QFileDialog.getOpenFileName(filter = "*.csv")
            rock_props = pd.read_csv(filename)
            print(rock_props.columns)                    
        
        self.browse_las_button.clicked.connect(open_csv_file)

        def open_user_file(self):
            global df_user
            filename, _ = QtWidgets.QFileDialog.getOpenFileName(filter = "*.csv")
            df_user = pd.read_csv(filename)
            # print(df_user.columns)                    
        
        self.browse_bedding_button.clicked.connect(open_user_file)

        def iso_sand_calcs():
            if self.iso_checkbox.isChecked() == True & self.sand_checkbox.isChecked() == True: # ISO and SAND
   
                rock_props['v_iso'] = rock_props['v_iso_d']
                rock_props['E_iso [Mpsi]'] = float((self.static_elastic_params_a_float.text())) * rock_props['E_iso_d (Mpsi)'] + float((self.static_elastic_params_b_float.text()))

                # Effective  Modulus E_prime
                rock_props['E_prime [Mpsi]'] = rock_props['E_iso [Mpsi]'] / (1 - rock_props['v_iso']**2) 

                rock_props['UCS_iso [MPa]'] = 2.28 + 4.1089 * (rock_props['E_iso [Mpsi]']*6.89476)

                rock_props['FANG_sand [degree]'] = np.abs(57.8 - 105 * rock_props['Porosity'])
                rock_props['FANG_r_sand [radian]'] = rock_props['FANG_sand [degree]']*np.pi/180

                rock_props['Friction_coef_sand'] = np.tan(rock_props['FANG_r_sand [radian]'])

                rock_props['COH_iso_sand'] = rock_props['UCS_iso [MPa]'] * (1 - np.sin(rock_props['FANG_r_sand [radian]'])) / (2 * np.cos(rock_props['FANG_r_sand [radian]']))
                # print(rock_props['COH_iso_sand'])

                rock_props['K [MPa/sqrt(m)]'] = float((self.k1c_value.text()))*(0.003672 * (rock_props['E_iso_d (Mpsi)']*6.89476) + 0.45034)
                # print(rock_props['K1c [MPa/sqrt(m)]'])

                # Getting minimum (non-zero) porosity
                rock_props['porosity_filtered'] = np.where(rock_props['Porosity'] < 0.05, 0, rock_props['Porosity'])
                porosity_list = rock_props['porosity_filtered'].to_list()
                porosity_list.sort()
                porosity_list = [x for x in porosity_list if x != 0]
                min_porosity = porosity_list[1]

                rock_props['C_L [ft/sqrt(min)]'] = float((self.leak_off_value.text())) * (rock_props['Porosity'] / min_porosity)
                rock_props['C_L [ft/sqrt(min)]'] = np.where(rock_props['C_L [ft/sqrt(min)]'] < 0, 0, rock_props['C_L [ft/sqrt(min)]'])
                # print(rock_props['C_L [ft/sqrt(min)]'])

                ### Fracture toughness scaling
                user_depth = df_user.iloc[:, 0].to_list()
                user_COF = df_user.iloc[:, 1].to_list()
                user_COH = df_user.iloc[:, 2].to_list()
                user_perm = df_user.iloc[:, 3].to_list()
                search_index = []
                for x in range(0,len(user_depth)):
                    search_idx = rock_props['Depth (m)'].sub(user_depth[x]).abs().idxmin()
                    rock_props.loc[search_idx, ['Friction_coef_sand']] = user_COF[x]
                    rock_props.loc[search_idx, ['COH_iso_sand']] = user_COH[x]
                    rock_props.loc[search_idx, ['C_L [ft/sqrt(min)]']] = rock_props.loc[search_idx, ['C_L [ft/sqrt(min)]']] * (user_perm[x]/float((self.matrix_perm_value.text())))
                    search_index.append(search_idx)

                # Crossing Stress Ratio (mu')
                Overburden = 1.0 # psi/ft
                rock_props['Vertical_Stress [psi]'] = Overburden*rock_props['Depth (m)']/0.3048
                rock_props['M'] = rock_props['Friction_coef_sand']*rock_props['Vertical_Stress [psi]'] / (rock_props['COH_iso_sand'] + rock_props['Friction_coef_sand']*rock_props['Min Stress'])
                rock_props['CSR'] = (0.35 + 0.35/rock_props['Friction_coef_sand'])/1.06
                # rock_props.loc[rock_props['M'] > rock_props['CSR'], 'Crossing?'] = 'Yes'
                # rock_props.loc[rock_props['M'] < rock_props['CSR'], 'Crossing?'] = 'NO'

                rock_props['g'] = rock_props['M'] / rock_props['CSR']

                for index in search_index:
                    if rock_props.loc[index, 'g'] < 1:
                        rock_props.loc[index, 'K [MPa/sqrt(m)]'] = rock_props.loc[index, 'K [MPa/sqrt(m)]'] / rock_props.loc[index, 'g']

                my_cols = ['Depth (m)', 'Porosity', 'v_iso', 'E_iso [Mpsi]', 'UCS_iso [MPa]','FANG_sand [degree]','FANG_r_sand [radian]', 'Friction_coef_sand', 'COH_iso_sand', 'K [MPa/sqrt(m)]', 'C_L [ft/sqrt(min)]', 'Vertical_Stress [psi]', 'M', 'CSR', 'g', 'Min Stress', 'Max Stress']
                rock_props_filtered = rock_props.reindex(columns = my_cols)
                rock_props_filtered.to_csv('RockPropCalcsOutput_Iso_Sand.csv', index = False)

                 # Homogenization of Elastic Properties

                ### How many layers to combine
                user_weight = int((self.homo_value.text())) 

                ### Get layer thickness and use as weights for averaging 
                rock_props['weights'] = rock_props['Depth (m)'].shift(-1) - rock_props['Depth (m)']
                weights = rock_props['weights'].to_list()

                ### For plotting purposes
                depth_list = rock_props['Depth (m)'].to_list()

                ### Homogenizing v

                ## Must find the actual values first
                v_x1 = rock_props_filtered['v_iso'] * rock_props_filtered['E_iso [Mpsi]'] / ((1 - rock_props_filtered['v_iso']**2))
                v_x2 = rock_props_filtered['E_iso [Mpsi]'] / ((1 - rock_props_filtered['v_iso']**2))

                ## Prepare lists for weighted averages
                user_weighted_v_x1 = []
                user_weighted_v_x2 = []

                ## Weighted average of values based on user weight
                for i in range(0, len(v_x1), user_weight):
                    user_weighted_v_x1_temp = np.average(v_x1[i:i+user_weight], weights = weights[i:i+user_weight])
                    user_weighted_v_x1.append(user_weighted_v_x1_temp)
                    user_weighted_v_x2_temp = np.average(v_x2[i:i+user_weight], weights = weights[i:i+user_weight])
                    user_weighted_v_x2.append(user_weighted_v_x2_temp)

                v_hom = np.array(user_weighted_v_x1) * np.array(user_weighted_v_x2)**(-1)

                ## Repeat value 'user weight' times to get the step plot
                v_hom_value = np.repeat(v_hom, user_weight)

                ### Homogenizing E

                ## Must find the actual values first
                E_x1 = (1 - v_hom_value[:len(rock_props_filtered['E_iso [Mpsi]'])]**2) 
                E_x2 = rock_props_filtered['E_iso [Mpsi]'] / (1 - v_hom_value[:len(rock_props_filtered['E_iso [Mpsi]'])]**2)

                ## Prepare lists for weighted averages
                user_weighted_E_x1 = []
                user_weighted_E_x2 = []

                ## Weighted average of values based on user weight
                for i in range(0, len(E_x2), user_weight):
                    user_weighted_E_x2_temp = np.average(E_x2[i:i+user_weight], weights = weights[i:i+user_weight])
                    user_weighted_E_x2.append(user_weighted_E_x2_temp)

                E_hom = E_x1[:len(user_weighted_E_x2)] * user_weighted_E_x2

                ## Repeat value 'user weight' times to get the step plot
                E_hom_value = np.repeat(E_hom, user_weight)

                #Homogenized Effective Horizontal Modulus E_prime_hom (bar)
                E_prime_hom = E_hom/(1 - v_hom**2)
                E_prime_hom_value = np.repeat(E_prime_hom, user_weight)

                # Effective Horizontal Modulus E_prime
                rock_props_filtered['E_prime [Mpsi]'] = rock_props_filtered['E_iso [Mpsi]'] / (1-rock_props_filtered['v_iso']**2)

                ### Homogenizing stress_min, stress_max, leak_off

                ## Must find the actual values first
                stress_min = rock_props_filtered['Min Stress']
                stress_min = stress_min.to_list()

                stress_max = rock_props_filtered['Max Stress']
                stress_max = stress_max.to_list()

                leak_off = rock_props_filtered['C_L [ft/sqrt(min)]']
                leak_off = leak_off.to_list()

                ## Prepare lists for weighted averages
                user_weighted_stress_min = []
                user_weighted_stress_max = []
                user_weighted_leak_off = []

                ## Weighted average of values based on user weight
                for i in range(0, len(stress_min), user_weight):
                    user_weighted_stress_min_temp = np.average(stress_min[i:i+user_weight], weights = weights[i:i+user_weight])
                    user_weighted_stress_min.append(user_weighted_stress_min_temp)

                stress_min_hom = user_weighted_stress_min

                for i in range(0, len(stress_max), user_weight):
                    user_weighted_stress_max_temp = np.average(stress_max[i:i+user_weight], weights = weights[i:i+user_weight])
                    user_weighted_stress_max.append(user_weighted_stress_max_temp)

                stress_max_hom = user_weighted_stress_max

                for i in range(0, len(leak_off), user_weight):
                    user_weighted_leak_off_temp = np.average(leak_off[i:i+user_weight], weights = weights[i:i+user_weight])
                    user_weighted_leak_off.append(user_weighted_leak_off_temp)

                leak_off_hom = user_weighted_leak_off

                ## Repeat value 'user weight' times to get the step plot
                stress_min_hom_value = np.repeat(stress_min_hom, user_weight)
                stress_max_hom_value = np.repeat(stress_max_hom, user_weight)
                leak_off_hom_value = np.repeat(leak_off_hom, user_weight)

                ### Fracture Toughness

                ## Homogenize K_x1
                ## Must find the actual values first
                K_x1 = rock_props_filtered['K [MPa/sqrt(m)]']**2/ rock_props_filtered['E_prime [Mpsi]']
                weighted_K_x1 = np.average(K_x1, weights = weights)

                ## Prepare lists for weighted averages
                user_weighted_K_x1 = []

                # Weighted average of values based on user weight
                for i in range(0, len(K_x1), user_weight):
                    user_weighted_K_x1_temp = np.average(K_x1[i:i+user_weight], weights = weights[i:i+user_weight])
                    user_weighted_K_x1.append(user_weighted_K_x1_temp)

                K_hom = np.array(np.array(E_prime_hom[:len(user_weighted_K_x1)]) * np.array(user_weighted_K_x1)) ** (0.5)

                ## Repeat value 'user weight' times to get the step plot
                K_hom_value = np.repeat(K_hom, user_weight)

                df = pd.DataFrame(list(zip(depth_list, E_hom_value, v_hom_value, K_hom_value, stress_min_hom_value, stress_max_hom_value, leak_off_hom_value)))
                df.columns = ['Depth', 'E_hom [Mpsi]', 'v_hom', 'K_hom [MPa/sqrt(m)]', 'Stress_Min_hom [psi]','Stress_Max_hom [psi]', 'leak_off_hom [ft/sqrt(min)]']

                df.to_csv('HomogenizedOutput_Iso_Sand.csv', index = False)

        self.iso_checkbox.stateChanged.connect(iso_sand_calcs)
        self.sand_checkbox.stateChanged.connect(iso_sand_calcs)

        def iso_shale_calcs():
            if self.iso_checkbox.isChecked() == True & self.shale_checkbox.isChecked() == True: # ISO and SHALE
                rock_props['v_iso'] = rock_props['v_iso_d']
                rock_props['E_iso [Mpsi]'] = float((self.static_elastic_params_a_float.text())) * rock_props['E_iso_d (Mpsi)'] + float((self.static_elastic_params_b_float.text()))

                # Effective  Modulus E_prime
                rock_props['E_prime [Mpsi]'] = rock_props['E_iso [Mpsi]'] / (1 - rock_props['v_iso']**2) 

                rock_props['UCS_iso [MPa]'] = 2.28 + 4.1089 * (rock_props['E_iso [Mpsi]']*6.89476)

                rock_props['FANG_r_shale [radian]'] = np.arcsin((rock_props['Vp(0) (m/s)'] - 1000)/(rock_props['Vp(0) (m/s)'] + 1000))
                # print(rock_props['FANG_r_shale [radian]'])
                rock_props['FANG_shale [degree]'] = rock_props['FANG_r_shale [radian]']*180/np.pi

                rock_props['Friction_coef_shale'] = np.tan(rock_props['FANG_r_shale [radian]'])

                rock_props['COH_iso_shale'] = rock_props['UCS_iso [MPa]'] * (1 - np.sin(rock_props['FANG_r_shale [radian]'])) / (2 * np.cos(rock_props['FANG_r_shale [radian]']))

                # print(rock_props['COH_iso_shale'])
                rock_props['K [MPa/sqrt(m)]'] = float((self.k1c_value.text()))*(0.003672 * (rock_props['E_iso_d (Mpsi)']*6.89476) + 0.45034)
                # print(rock_props['K1c [MPa/sqrt(m)]'])

                # Getting minimum (non-zero) porosity
                rock_props['porosity_filtered'] = np.where(rock_props['Porosity'] < 0.05, 0, rock_props['Porosity'])
                porosity_list = rock_props['porosity_filtered'].to_list()
                porosity_list.sort()
                porosity_list = [x for x in porosity_list if x != 0]
                min_porosity = porosity_list[1]

                rock_props['C_L [ft/sqrt(min)]'] = float((self.leak_off_value.text())) * (rock_props['Porosity'] / min_porosity)
                rock_props['C_L [ft/sqrt(min)]'] = np.where(rock_props['C_L [ft/sqrt(min)]'] < 0, 0, rock_props['C_L [ft/sqrt(min)]'])
                # print(rock_props['C_L [ft/sqrt(min)]'])

                ### Fracture toughness scaling
                user_depth = df_user.iloc[:, 0].to_list()
                user_COF = df_user.iloc[:, 1].to_list()
                user_COH = df_user.iloc[:, 2].to_list()
                user_perm = df_user.iloc[:, 3].to_list()
                search_index = []
                for x in range(0,len(user_depth)):
                    search_idx = rock_props['Depth (m)'].sub(user_depth[x]).abs().idxmin()
                    rock_props.loc[search_idx, ['Friction_coef_shale']] = user_COF[x]
                    rock_props.loc[search_idx, ['COH_iso_shale']] = user_COH[x]
                    rock_props.loc[search_idx, ['C_L [ft/sqrt(min)]']] = rock_props.loc[search_idx, ['C_L [ft/sqrt(min)]']] * (user_perm[x]/float((self.matrix_perm_value.text())))
                    search_index.append(search_idx)

                # Crossing Stress Ratio (mu')
                Overburden = 1.0 # psi/ft
                rock_props['Vertical_Stress [psi]'] = Overburden*rock_props['Depth (m)']/0.3048
                rock_props['M'] = rock_props['Friction_coef_shale']*rock_props['Vertical_Stress [psi]'] / (rock_props['COH_iso_shale'] + rock_props['Friction_coef_shale']*rock_props['Min Stress'])
                rock_props['CSR'] = (0.35 + 0.35/rock_props['Friction_coef_shale'])/1.06
                # rock_props.loc[rock_props['M'] > rock_props['CSR'], 'Crossing?'] = 'Yes'
                # rock_props.loc[rock_props['M'] < rock_props['CSR'], 'Crossing?'] = 'NO'

                rock_props['g'] = rock_props['M'] / rock_props['CSR']

                for index in search_index:
                    if rock_props.loc[index, 'g'] < 1:
                        rock_props.loc[index, 'K [MPa/sqrt(m)]'] = rock_props.loc[index, 'K [MPa/sqrt(m)]'] / rock_props.loc[index, 'g']

                my_cols = ['Depth (m)', 'Porosity', 'v_iso', 'E_iso [Mpsi]', 'UCS_iso [MPa]','FANG_shale [degree]','FANG_r_shale [radian]', 'Friction_coef_shale', 'COH_iso_shale', 'K [MPa/sqrt(m)]', 'C_L [ft/sqrt(min)]', 'Vertical_Stress [psi]', 'M', 'CSR', 'g', 'Min Stress', 'Max Stress']

                rock_props_filtered = rock_props.reindex(columns = my_cols)

                rock_props_filtered.to_csv('RockPropCalcsOutput_Iso_Shale.csv', index = False)

                 # Homogenization of Elastic Properties

                ### How many layers to combine
                user_weight = int((self.homo_value.text()))

                ### Get layer thickness and use as weights for averaging 
                rock_props['weights'] = rock_props['Depth (m)'].shift(-1) - rock_props['Depth (m)']
                weights = rock_props['weights'].to_list()

                ### For plotting purposes
                depth_list = rock_props['Depth (m)'].to_list()

                ### Homogenizing v

                ## Must find the actual values first
                v_x1 = rock_props_filtered['v_iso'] * rock_props_filtered['E_iso [Mpsi]'] / ((1 - rock_props_filtered['v_iso']**2))
                v_x2 = rock_props_filtered['E_iso [Mpsi]'] / ((1 - rock_props_filtered['v_iso']**2))

                ## Prepare lists for weighted averages
                user_weighted_v_x1 = []
                user_weighted_v_x2 = []

                ## Weighted average of values based on user weight
                for i in range(0, len(v_x1), user_weight):
                    user_weighted_v_x1_temp = np.average(v_x1[i:i+user_weight], weights = weights[i:i+user_weight])
                    user_weighted_v_x1.append(user_weighted_v_x1_temp)
                    user_weighted_v_x2_temp = np.average(v_x2[i:i+user_weight], weights = weights[i:i+user_weight])
                    user_weighted_v_x2.append(user_weighted_v_x2_temp)

                v_hom = np.array(user_weighted_v_x1) * np.array(user_weighted_v_x2)**(-1)

                ## Repeat value 'user weight' times to get the step plot
                v_hom_value = np.repeat(v_hom, user_weight)

                ### Homogenizing E

                ## Must find the actual values first
                E_x1 = (1 - v_hom_value[:len(rock_props_filtered['E_iso [Mpsi]'])]**2) 
                E_x2 = rock_props_filtered['E_iso [Mpsi]'] / (1 - v_hom_value[:len(rock_props_filtered['E_iso [Mpsi]'])]**2)

                ## Prepare lists for weighted averages
                user_weighted_E_x1 = []
                user_weighted_E_x2 = []

                ## Weighted average of values based on user weight
                for i in range(0, len(E_x2), user_weight):
                    user_weighted_E_x2_temp = np.average(E_x2[i:i+user_weight], weights = weights[i:i+user_weight])
                    user_weighted_E_x2.append(user_weighted_E_x2_temp)

                E_hom = E_x1[:len(user_weighted_E_x2)] * user_weighted_E_x2

                ## Repeat value 'user weight' times to get the step plot
                E_hom_value = np.repeat(E_hom, user_weight)

                #Homogenized Effective Horizontal Modulus E_prime_hom (bar)
                E_prime_hom = E_hom/(1 - v_hom**2)
                E_prime_hom_value = np.repeat(E_prime_hom, user_weight)

                # Effective Horizontal Modulus E_prime
                rock_props_filtered['E_prime [Mpsi]'] = rock_props_filtered['E_iso [Mpsi]'] / (1-rock_props_filtered['v_iso']**2)

                ### Homogenizing stress_min, stress_max, leak_off

                ## Must find the actual values first
                stress_min = rock_props_filtered['Min Stress']
                stress_min = stress_min.to_list()

                stress_max = rock_props_filtered['Max Stress']
                stress_max = stress_max.to_list()

                leak_off = rock_props_filtered['C_L [ft/sqrt(min)]']
                leak_off = leak_off.to_list()

                ## Prepare lists for weighted averages
                user_weighted_stress_min = []
                user_weighted_stress_max = []
                user_weighted_leak_off = []

                ## Weighted average of values based on user weight
                for i in range(0, len(stress_min), user_weight):
                    user_weighted_stress_min_temp = np.average(stress_min[i:i+user_weight], weights = weights[i:i+user_weight])
                    user_weighted_stress_min.append(user_weighted_stress_min_temp)

                stress_min_hom = user_weighted_stress_min

                for i in range(0, len(stress_max), user_weight):
                    user_weighted_stress_max_temp = np.average(stress_max[i:i+user_weight], weights = weights[i:i+user_weight])
                    user_weighted_stress_max.append(user_weighted_stress_max_temp)

                stress_max_hom = user_weighted_stress_max

                for i in range(0, len(leak_off), user_weight):
                    user_weighted_leak_off_temp = np.average(leak_off[i:i+user_weight], weights = weights[i:i+user_weight])
                    user_weighted_leak_off.append(user_weighted_leak_off_temp)

                leak_off_hom = user_weighted_leak_off

                ## Repeat value 'user weight' times to get the step plot
                stress_min_hom_value = np.repeat(stress_min_hom, user_weight)
                stress_max_hom_value = np.repeat(stress_max_hom, user_weight)
                leak_off_hom_value = np.repeat(leak_off_hom, user_weight)

                # ### Fracture Toughness

                ## Homogenize K_x1
                ## Must find the actual values first
                K_x1 = rock_props_filtered['K [MPa/sqrt(m)]']**2/ rock_props_filtered['E_prime [Mpsi]']
                weighted_K_x1 = np.average(K_x1, weights = weights)

                ## Prepare lists for weighted averages
                user_weighted_K_x1 = []

                # Weighted average of values based on user weight
                for i in range(0, len(K_x1), user_weight):
                    user_weighted_K_x1_temp = np.average(K_x1[i:i+user_weight], weights = weights[i:i+user_weight])
                    user_weighted_K_x1.append(user_weighted_K_x1_temp)

                K_hom = np.array(np.array(E_prime_hom[:len(user_weighted_K_x1)]) * np.array(user_weighted_K_x1)) ** (0.5)

                ## Repeat value 'user weight' times to get the step plot
                K_hom_value = np.repeat(K_hom, user_weight)

                df = pd.DataFrame(list(zip(depth_list, E_hom_value, v_hom_value, K_hom_value, stress_min_hom_value, stress_max_hom_value, leak_off_hom_value)))
                df.columns = ['Depth', 'E_hom [Mpsi]', 'v_hom', 'K_hom [MPa/sqrt(m)]', 'Stress_Min_hom [psi]','Stress_Max_hom [psi]', 'leak_off_hom [ft/sqrt(min)]']

                df.to_csv('HomogenizedOutput_Iso_Shale.csv', index = False)

        self.iso_checkbox.stateChanged.connect(iso_shale_calcs)
        self.shale_checkbox.stateChanged.connect(iso_shale_calcs)

        def vti_sand_calcs():
            if self.vti_checkbox.isChecked() == True & self.sand_checkbox.isChecked() == True: # VTI and SAND
                
                rock_props['v_VTI_v'] = rock_props['vv_d']
                rock_props['v_VTI_h'] = rock_props['vh_d']

                rock_props['E_VTI_v [Mpsi]'] = float((self.static_elastic_params_a_float.text())) * rock_props['Ev_d (Mpsi)'] + float((self.static_elastic_params_b_float.text()))
                rock_props['E_VTI_h [Mpsi]'] = float((self.static_elastic_params_a_float.text())) * rock_props['Eh_d (Mpsi)'] + float((self.static_elastic_params_b_float.text()))

                # Effective  Modulus E_prime
                rock_props['E_prime_h [Mpsi]'] = rock_props['E_VTI_h [Mpsi]'] / (1 - rock_props['v_VTI_h']**2) 
                rock_props['E_prime_v [Mpsi]'] = rock_props['E_VTI_v [Mpsi]'] / (1 - rock_props['v_VTI_v']**2) 

                rock_props['UCS_VTI [MPa]'] = 2.28 + 4.1089 * (rock_props['E_VTI_v [Mpsi]']*6.89476)

                rock_props['FANG_sand [degree]'] = np.abs(57.8 - 105 * rock_props['Porosity'])
                rock_props['FANG_r_sand [radian]'] = rock_props['FANG_sand [degree]']*np.pi/180

                rock_props['Friction_coef_sand'] = np.tan(rock_props['FANG_r_sand [radian]'])

                rock_props['COH_VTI_sand'] = rock_props['UCS_VTI [MPa]'] * (1 - np.sin(rock_props['FANG_r_sand [radian]'])) / (2 * np.cos(rock_props['FANG_r_sand [radian]']))

                rock_props['K_v [MPa/sqrt(m)]'] = float((self.k1c_v_value.text()))*(0.003672 * (rock_props['Ev_d (Mpsi)']*6.89476) + 0.45034)
                rock_props['K_h [MPa/sqrt(m)]'] = float((self.k1c_h_label.text()))*(0.003672 * (rock_props['Eh_d (Mpsi)']*6.89476) + 0.45034)

                # Getting minimum (non-zero) porosity
                rock_props['porosity_filtered'] = np.where(rock_props['Porosity'] < 0.05, 0, rock_props['Porosity'])
                porosity_list = rock_props['porosity_filtered'].to_list()
                porosity_list.sort()
                porosity_list = [x for x in porosity_list if x != 0]
                min_porosity = porosity_list[1]

                rock_props['C_L [ft/sqrt(min)]'] = float((self.leak_off_value.text())) * (rock_props['Porosity'] / min_porosity)
                rock_props['C_L [ft/sqrt(min)]'] = np.where(rock_props['C_L [ft/sqrt(min)]'] < 0, 0, rock_props['C_L [ft/sqrt(min)]'])
                # print(rock_props['C_L [ft/sqrt(min)]'])

                # Crossing Stress Ratio (mu')
                Overburden = 1.0 # psi/ft
                rock_props['Vertical_Stress [psi]'] = Overburden*rock_props['Depth (m)']/0.3048
                rock_props['M'] = rock_props['Friction_coef_sand']*rock_props['Vertical_Stress [psi]'] / (rock_props['COH_VTI_sand'] + rock_props['Friction_coef_sand']*rock_props['Min Stress'])
                rock_props['CSR'] = (0.35 + 0.35/rock_props['Friction_coef_sand'])/1.06
                rock_props.loc[rock_props['M'] > rock_props['CSR'], 'Crossing?'] = 'Yes'
                rock_props.loc[rock_props['M'] < rock_props['CSR'], 'Crossing?'] = 'NO'

                rock_props['g'] = rock_props['M'] / rock_props['CSR']
                
                ### Fracture toughness scaling
                user_depth = df_user.iloc[:, 0].to_list()
                user_COF = df_user.iloc[:, 1].to_list()
                user_COH = df_user.iloc[:, 2].to_list()
                user_perm = df_user.iloc[:, 3].to_list()
                search_index = []
                for x in range(0,len(user_depth)):
                    search_idx = rock_props['Depth (m)'].sub(user_depth[x]).abs().idxmin()
                    rock_props.loc[search_idx, ['Friction_coef_sand']] = user_COF[x]
                    rock_props.loc[search_idx, ['COH_VTI_sand']] = user_COH[x]
                    rock_props.loc[search_idx, ['C_L [ft/sqrt(min)]']] = rock_props.loc[search_idx, ['C_L [ft/sqrt(min)]']] * (user_perm[x]/float((self.matrix_perm_value.text())))
                    search_index.append(search_idx)

                for index in search_index:
                    if rock_props.loc[index, 'g'] < 1:
                        rock_props.loc[index, 'K_v [MPa/sqrt(m)]'] = rock_props.loc[index, 'K_v [MPa/sqrt(m)]'] / rock_props.loc[index, 'g']

                # #Saving CSV file
                my_cols = ['Depth (m)', 'Porosity', 'v_VTI_v', 'E_VTI_v [Mpsi]', 'E_prime_v [Mpsi]', 'v_VTI_h', 'E_VTI_h [Mpsi]', 'E_prime_h [Mpsi]',  'UCS_VTI [MPa]', 'FANG_sand [degree]', 'FANG_r_sand [radian]', 'Friction_coef_sand', 'COH_VTI_sand', 'K_v [MPa/sqrt(m)]', 'K_h [MPa/sqrt(m)]', 'C_L [ft/sqrt(min)]', 'M', 'CSR', 'g', 'Min Stress', 'Max Stress']
                rock_props_filtered = rock_props.reindex(columns = my_cols)
                rock_props_filtered.to_csv('RockPropCalcsOutput_VTI_Sand.csv', index = False)

                # Homogenization of Elastic Properties

                ### How many layers to combine
                user_weight = int((self.homo_value.text())) 

                ### Get layer thickness and use as weights for averaging 
                rock_props['weights'] = rock_props['Depth (m)'].shift(-1) - rock_props['Depth (m)']
                weights = rock_props['weights'].to_list()

                ### For plotting purposes
                depth_list = rock_props['Depth (m)'].to_list()

                ### Homogenizing v_h

                ## Must find the actual values first
                v_h_x1 = rock_props_filtered['v_VTI_h'] * rock_props_filtered['E_VTI_h [Mpsi]'] / ((1 - rock_props_filtered['v_VTI_h']**2))
                v_h_x2 = rock_props_filtered['E_VTI_h [Mpsi]'] / ((1 - rock_props_filtered['v_VTI_h']**2))

                ## Prepare lists for weighted averages
                user_weighted_v_h_x1 = []
                user_weighted_v_h_x2 = []

                ## Weighted average of values based on user weight
                for i in range(0, len(v_h_x1), user_weight):
                    user_weighted_v_h_x1_temp = np.average(v_h_x1[i:i+user_weight], weights = weights[i:i+user_weight])
                    user_weighted_v_h_x1.append(user_weighted_v_h_x1_temp)
                    user_weighted_v_h_x2_temp = np.average(v_h_x2[i:i+user_weight], weights = weights[i:i+user_weight])
                    user_weighted_v_h_x2.append(user_weighted_v_h_x2_temp)

                v_h_hom = np.array(user_weighted_v_h_x1) * np.array(user_weighted_v_h_x2)**(-1)

                ## Repeat value 'user weight' times to get the step plot
                v_h_hom_value = np.repeat(v_h_hom, user_weight)

                ### Homogenizing E_h

                ## Must find the actual values first
                E_h_x1 = (1 - v_h_hom_value[:len(rock_props_filtered['E_VTI_h [Mpsi]'])]**2) 
                E_h_x2 = rock_props_filtered['E_VTI_h [Mpsi]'] / (1 - v_h_hom_value[:len(rock_props_filtered['E_VTI_h [Mpsi]'])]**2)

                ## Prepare lists for weighted averages
                user_weighted_E_h_x1 = []
                user_weighted_E_h_x2 = []

                ## Weighted average of values based on user weight
                for i in range(0, len(E_h_x2), user_weight):
                    user_weighted_E_h_x2_temp = np.average(E_h_x2[i:i+user_weight], weights = weights[i:i+user_weight])
                    user_weighted_E_h_x2.append(user_weighted_E_h_x2_temp)

                E_h_hom = E_h_x1[:len(user_weighted_E_h_x2)] * user_weighted_E_h_x2

                ## Repeat value 'user weight' times to get the step plot
                E_h_hom_value = np.repeat(E_h_hom, user_weight)

                #Homogenized Effective Horizontal Modulus E_prime_h_hom (bar)
                E_prime_h_hom = E_h_hom/(1 - v_h_hom**2)
                E_prime_h_hom_value = np.repeat(E_prime_h_hom, user_weight)

                ### Homogenizing E_v (by finding the weighted average of Ev/Eh)
                ## Must find the actual values first
                Ev_over_Eh = rock_props_filtered['E_VTI_v [Mpsi]'] / rock_props_filtered['E_VTI_h [Mpsi]']

                ## Prepare lists for weighted averages
                user_weighted_Ev_over_Eh = []

                ## Weighted average of values based on user weight
                for i in range(0, len(Ev_over_Eh), user_weight):
                    user_weighted_Ev_over_Eh_temp = np.average(Ev_over_Eh[i:i+user_weight], weights = weights[i:i+user_weight])
                    user_weighted_Ev_over_Eh.append(user_weighted_Ev_over_Eh_temp)

                Ev_over_Eh_hom = Ev_over_Eh[:len(user_weighted_Ev_over_Eh)] * user_weighted_Ev_over_Eh

                ## Repeat value 'user weight' times to get the step plot
                Ev_over_Eh_hom_value = np.repeat(Ev_over_Eh_hom, user_weight)

                ## Homogenized Vertical Modulus E_v_hom (bar)
                E_v_hom = E_h_hom * Ev_over_Eh_hom
                E_v_hom_value = np.repeat(E_v_hom, user_weight)

                ### Homogenizing E_prime_v (by finding the weighted average of E_prime_v/E_prime_h)
                ## Must find the actual values first
                E_prime_v_over_E_prime_h = rock_props_filtered['E_prime_v [Mpsi]'] / rock_props_filtered['E_prime_h [Mpsi]']

                ## Prepare lists for weighted averages
                user_weighted_E_prime_v_over_E_prime_h = []

                ## Weighted average of values based on user weight
                for i in range(0, len(E_prime_v_over_E_prime_h), user_weight):
                    user_weighted_E_prime_v_over_E_prime_h_temp = np.average(E_prime_v_over_E_prime_h[i:i+user_weight], weights = weights[i:i+user_weight])
                    user_weighted_E_prime_v_over_E_prime_h.append(user_weighted_E_prime_v_over_E_prime_h_temp)

                ## Homogenized Effective Vertical Modulus E_prime_v_hom (bar)
                E_prime_v_hom = E_prime_h_hom * user_weighted_E_prime_v_over_E_prime_h
                ## Repeat value 'user weight' times to get the step plot
                E_prime_v_hom_value = np.repeat(E_prime_v_hom, user_weight)

                ### Homogenizing stress_min, stress_max, leak_off

                ## Must find the actual values first
                stress_min = rock_props_filtered['Min Stress']
                stress_min = stress_min.to_list()

                stress_max = rock_props_filtered['Max Stress']
                stress_max = stress_max.to_list()

                leak_off = rock_props_filtered['C_L [ft/sqrt(min)]']
                leak_off = leak_off.to_list()

                ## Prepare lists for weighted averages
                user_weighted_stress_min = []
                user_weighted_stress_max = []
                user_weighted_leak_off = []

                ## Weighted average of values based on user weight
                for i in range(0, len(stress_min), user_weight):
                    user_weighted_stress_min_temp = np.average(stress_min[i:i+user_weight], weights = weights[i:i+user_weight])
                    user_weighted_stress_min.append(user_weighted_stress_min_temp)

                stress_min_hom = user_weighted_stress_min

                for i in range(0, len(stress_max), user_weight):
                    user_weighted_stress_max_temp = np.average(stress_max[i:i+user_weight], weights = weights[i:i+user_weight])
                    user_weighted_stress_max.append(user_weighted_stress_max_temp)

                stress_max_hom = user_weighted_stress_max

                for i in range(0, len(leak_off), user_weight):
                    user_weighted_leak_off_temp = np.average(leak_off[i:i+user_weight], weights = weights[i:i+user_weight])
                    user_weighted_leak_off.append(user_weighted_leak_off_temp)

                leak_off_hom = user_weighted_leak_off

                ## Repeat value 'user weight' times to get the step plot
                stress_min_hom_value = np.repeat(stress_min_hom, user_weight)
                stress_max_hom_value = np.repeat(stress_max_hom, user_weight)
                leak_off_hom_value = np.repeat(leak_off_hom, user_weight)

                ### Fracture Toughness

                ## Homogenize K_h_x1
                ## Must find the actual values first
                K_h_x1 = rock_props_filtered['K_h [MPa/sqrt(m)]']**2/ rock_props_filtered['E_prime_h [Mpsi]']
                weighted_K_h_x1 = np.average(K_h_x1, weights = weights)

                ## Prepare lists for weighted averages
                user_weighted_K_h_x1 = []

                # Weighted average of values based on user weight
                for i in range(0, len(K_h_x1), user_weight):
                    user_weighted_K_h_x1_temp = np.average(K_h_x1[i:i+user_weight], weights = weights[i:i+user_weight])
                    user_weighted_K_h_x1.append(user_weighted_K_h_x1_temp)

                K_h_hom = np.array(np.array(E_prime_h_hom[:len(user_weighted_K_h_x1)]) * np.array(user_weighted_K_h_x1)) ** (0.5)

                ## Repeat value 'user weight' times to get the step plot
                K_h_hom_value = np.repeat(K_h_hom, user_weight)

                ## Homogenize K_v_x1
                ## Must find the actual values first
                K_v_x1 = rock_props_filtered['K_v [MPa/sqrt(m)]']**2/ rock_props_filtered['E_prime_v [Mpsi]']
                # print(K_v_x1)

                ## Prepare lists for weighted averages
                user_maxed_K_v_x1 = []

                # Maximum value of values based on user weight
                for i in range(0, len(K_v_x1), user_weight):
                    user_maxed_K_v_x1_temp = np.max(K_v_x1[i:i+user_weight])
                    # print(user_maxed_K_v_x1_temp)
                    user_maxed_K_v_x1.append(user_maxed_K_v_x1_temp)

                K_v_hom = (E_prime_v_hom * user_maxed_K_v_x1) ** (0.5)

                ## Repeat value 'user weight' times to get the step plot
                K_v_hom_value = np.repeat(K_v_hom, user_weight)

                df = pd.DataFrame(list(zip(depth_list, E_h_hom_value, v_h_hom_value, K_h_hom_value, K_v_hom_value, stress_min_hom_value, stress_max_hom_value, leak_off_hom_value)))
                df.columns = ['Depth', 'E_h_hom [Mpsi]', 'v_h_hom', 'K_h_hom [MPa/sqrt(m)]', 'K_v_hom [MPa/sqrt(m)]', 'Stress_Min_hom [psi]','Stress_Max_hom [psi]', 'leak_off_hom [ft/sqrt(min)]']

                df.to_csv('HomogenizedOutput_VTI_Sand.csv', index = False)

        self.vti_checkbox.stateChanged.connect(vti_sand_calcs)
        self.sand_checkbox.stateChanged.connect(vti_sand_calcs)

        def vti_shale_calcs():
            if self.vti_checkbox.isChecked() == True & self.shale_checkbox.isChecked() == True: # VTI and SHALE
                rock_props['v_VTI_v'] = rock_props['vv_d']
                rock_props['v_VTI_h'] = rock_props['vh_d']

                rock_props['E_VTI_v [Mpsi]'] = float((self.static_elastic_params_a_float.text())) * rock_props['Ev_d (Mpsi)'] + float((self.static_elastic_params_b_float.text()))
                rock_props['E_VTI_h [Mpsi]'] = float((self.static_elastic_params_a_float.text())) * rock_props['Eh_d (Mpsi)'] + float((self.static_elastic_params_b_float.text()))

                # Effective  Modulus E_prime
                rock_props['E_prime_h [Mpsi]'] = rock_props['E_VTI_h [Mpsi]'] / (1 - rock_props['v_VTI_h']**2) 
                rock_props['E_prime_v [Mpsi]'] = rock_props['E_VTI_v [Mpsi]'] / (1 - rock_props['v_VTI_v']**2) 

                rock_props['UCS_VTI [MPa]'] = 2.28 + 4.1089 * ((rock_props['E_VTI_v [Mpsi]']+rock_props['E_VTI_h [Mpsi]'])/2*6.89476)

                rock_props['FANG_r_shale [radian]'] = np.arcsin((rock_props['Vp(0) (m/s)'] - 1000)/(rock_props['Vp(0) (m/s)'] + 1000))
                rock_props['FANG_shale [degree]'] = rock_props['FANG_r_shale [radian]']*180/np.pi

                rock_props['Friction_coef_shale'] = np.tan(rock_props['FANG_r_shale [radian]'])

                rock_props['COH_VTI_shale'] = rock_props['UCS_VTI [MPa]'] * (1 - np.sin(rock_props['FANG_r_shale [radian]'])) / (2 * np.cos(rock_props['FANG_r_shale [radian]']))

                rock_props['K_v [MPa/sqrt(m)]'] = float((self.k1c_v_value.text()))*(0.003672 * (rock_props['Ev_d (Mpsi)']*6.89476) + 0.45034)
                rock_props['K_h [MPa/sqrt(m)]'] = float((self.k1c_h_label.text()))*(0.003672 * (rock_props['Eh_d (Mpsi)']*6.89476) + 0.45034)

                # Getting minimum (non-zero) porosity
                rock_props['porosity_filtered'] = np.where(rock_props['Porosity'] < 0.05, 0, rock_props['Porosity'])
                porosity_list = rock_props['porosity_filtered'].to_list()
                porosity_list.sort()
                porosity_list = [x for x in porosity_list if x != 0]
                min_porosity = porosity_list[1]

                rock_props['C_L [ft/sqrt(min)]'] = float((self.leak_off_value.text())) * (rock_props['Porosity'] / min_porosity)
                rock_props['C_L [ft/sqrt(min)]'] = np.where(rock_props['C_L [ft/sqrt(min)]'] < 0, 0, rock_props['C_L [ft/sqrt(min)]'])
                # print(rock_props['C_L [ft/sqrt(min)]'])

                ### Fracture toughness scaling
                user_depth = df_user.iloc[:, 0].to_list()
                user_COF = df_user.iloc[:, 1].to_list()
                user_COH = df_user.iloc[:, 2].to_list()
                user_perm = df_user.iloc[:, 3].to_list()
                search_index = []
                for x in range(0,len(user_depth)):
                    search_idx = rock_props['Depth (m)'].sub(user_depth[x]).abs().idxmin()
                    rock_props.loc[search_idx, ['Friction_coef_shale']] = user_COF[x]
                    rock_props.loc[search_idx, ['COH_VTI_shale']] = user_COH[x]
                    rock_props.loc[search_idx, ['C_L [ft/sqrt(min)]']] = rock_props.loc[search_idx, ['C_L [ft/sqrt(min)]']] * (user_perm[x]/float((self.matrix_perm_value.text())))
                    search_index.append(search_idx)
                    
                # Crossing Stress Ratio (mu')
                Overburden = 1.0 # psi/ft
                rock_props['Vertical_Stress [psi]'] = Overburden*rock_props['Depth (m)']/0.3048
                rock_props['M'] = rock_props['Friction_coef_shale']*rock_props['Vertical_Stress [psi]'] / (rock_props['COH_VTI_shale'] + rock_props['Friction_coef_shale']*rock_props['Min Stress'])
                rock_props['CSR'] = (0.35 + 0.35/rock_props['Friction_coef_shale'])/1.06
                # rock_props.loc[rock_props['M'] > rock_props['CSR'], 'Crossing?'] = 'Yes'
                # rock_props.loc[rock_props['M'] < rock_props['CSR'], 'Crossing?'] = 'NO'

                rock_props['g'] = rock_props['M'] / rock_props['CSR']
                
                for index in search_index:
                    if rock_props.loc[index, 'g'] < 1:
                        rock_props.loc[index, 'K_v [MPa/sqrt(m)]'] = rock_props.loc[index, 'K_v [MPa/sqrt(m)]'] / rock_props.loc[index, 'g']

                #Saving CSV file
                my_cols = ['Depth (m)', 'Porosity', 'v_VTI_v', 'E_VTI_v [Mpsi]', 'E_prime_v [Mpsi]', 'v_VTI_h', 'E_VTI_h [Mpsi]', 'E_prime_h [Mpsi]',  'UCS_VTI [MPa]','FANG_r_shale [radian]', 'FANG_shale [degree]', 'Friction_coef_shale', 'COH_VTI_shale', 'K_v [MPa/sqrt(m)]', 'K_h [MPa/sqrt(m)]', 'C_L [ft/sqrt(min)]', 'M', 'CSR', 'g', 'Min Stress', 'Max Stress']
                rock_props_filtered = rock_props.reindex(columns = my_cols)
                rock_props_filtered.to_csv('RockPropCalcsOutput_VTI_Shale.csv', index = False)

                # Homogenization of Elastic Properties

                ### How many layers to combine
                user_weight = int((self.homo_value.text())) 

                ### Get layer thickness and use as weights for averaging 
                rock_props['weights'] = rock_props['Depth (m)'].shift(-1) - rock_props['Depth (m)']
                weights = rock_props['weights'].to_list()

                ### For plotting purposes
                depth_list = rock_props['Depth (m)'].to_list()

                ### Homogenizing v_h

                ## Must find the actual values first
                v_h_x1 = rock_props_filtered['v_VTI_h'] * rock_props_filtered['E_VTI_h [Mpsi]'] / ((1 - rock_props_filtered['v_VTI_h']**2))
                v_h_x2 = rock_props_filtered['E_VTI_h [Mpsi]'] / ((1 - rock_props_filtered['v_VTI_h']**2))

                ## Prepare lists for weighted averages
                user_weighted_v_h_x1 = []
                user_weighted_v_h_x2 = []

                ## Weighted average of values based on user weight
                for i in range(0, len(v_h_x1), user_weight):
                    user_weighted_v_h_x1_temp = np.average(v_h_x1[i:i+user_weight], weights = weights[i:i+user_weight])
                    user_weighted_v_h_x1.append(user_weighted_v_h_x1_temp)
                    user_weighted_v_h_x2_temp = np.average(v_h_x2[i:i+user_weight], weights = weights[i:i+user_weight])
                    user_weighted_v_h_x2.append(user_weighted_v_h_x2_temp)

                v_h_hom = np.array(user_weighted_v_h_x1) * np.array(user_weighted_v_h_x2)**(-1)

                ## Repeat value 'user weight' times to get the step plot
                v_h_hom_value = np.repeat(v_h_hom, user_weight)

                ### Homogenizing E_h

                ## Must find the actual values first
                E_h_x1 = (1 - v_h_hom_value[:len(rock_props_filtered['E_VTI_h [Mpsi]'])]**2) 
                E_h_x2 = rock_props_filtered['E_VTI_h [Mpsi]'] / (1 - v_h_hom_value[:len(rock_props_filtered['E_VTI_h [Mpsi]'])]**2)

                ## Prepare lists for weighted averages
                user_weighted_E_h_x1 = []
                user_weighted_E_h_x2 = []

                ## Weighted average of values based on user weight
                for i in range(0, len(E_h_x2), user_weight):
                    user_weighted_E_h_x2_temp = np.average(E_h_x2[i:i+user_weight], weights = weights[i:i+user_weight])
                    user_weighted_E_h_x2.append(user_weighted_E_h_x2_temp)

                E_h_hom = E_h_x1[:len(user_weighted_E_h_x2)] * user_weighted_E_h_x2

                ## Repeat value 'user weight' times to get the step plot
                E_h_hom_value = np.repeat(E_h_hom, user_weight)

                #Homogenized Effective Horizontal Modulus E_prime_h_hom (bar)
                E_prime_h_hom = E_h_hom/(1 - v_h_hom**2)
                E_prime_h_hom_value = np.repeat(E_prime_h_hom, user_weight)

                ### Homogenizing E_v (by finding the weighted average of Ev/Eh)
                ## Must find the actual values first
                Ev_over_Eh = rock_props_filtered['E_VTI_v [Mpsi]'] / rock_props_filtered['E_VTI_h [Mpsi]']

                ## Prepare lists for weighted averages
                user_weighted_Ev_over_Eh = []

                ## Weighted average of values based on user weight
                for i in range(0, len(Ev_over_Eh), user_weight):
                    user_weighted_Ev_over_Eh_temp = np.average(Ev_over_Eh[i:i+user_weight], weights = weights[i:i+user_weight])
                    user_weighted_Ev_over_Eh.append(user_weighted_Ev_over_Eh_temp)

                Ev_over_Eh_hom = Ev_over_Eh[:len(user_weighted_Ev_over_Eh)] * user_weighted_Ev_over_Eh

                ## Repeat value 'user weight' times to get the step plot
                Ev_over_Eh_hom_value = np.repeat(Ev_over_Eh_hom, user_weight)

                ## Homogenized Vertical Modulus E_v_hom (bar)
                E_v_hom = E_h_hom * Ev_over_Eh_hom
                E_v_hom_value = np.repeat(E_v_hom, user_weight)

                ### Homogenizing E_prime_v (by finding the weighted average of E_prime_v/E_prime_h)
                ## Must find the actual values first
                E_prime_v_over_E_prime_h = rock_props_filtered['E_prime_v [Mpsi]'] / rock_props_filtered['E_prime_h [Mpsi]']

                ## Prepare lists for weighted averages
                user_weighted_E_prime_v_over_E_prime_h = []

                ## Weighted average of values based on user weight
                for i in range(0, len(E_prime_v_over_E_prime_h), user_weight):
                    user_weighted_E_prime_v_over_E_prime_h_temp = np.average(E_prime_v_over_E_prime_h[i:i+user_weight], weights = weights[i:i+user_weight])
                    user_weighted_E_prime_v_over_E_prime_h.append(user_weighted_E_prime_v_over_E_prime_h_temp)

                ## Homogenized Effective Vertical Modulus E_prime_v_hom (bar)
                E_prime_v_hom = E_prime_h_hom * user_weighted_E_prime_v_over_E_prime_h
                ## Repeat value 'user weight' times to get the step plot
                E_prime_v_hom_value = np.repeat(E_prime_v_hom, user_weight)

                ### Homogenizing stress_min, stress_max, leak_off

                ## Must find the actual values first
                stress_min = rock_props_filtered['Min Stress']
                stress_min = stress_min.to_list()

                stress_max = rock_props_filtered['Max Stress']
                stress_max = stress_max.to_list()

                leak_off = rock_props_filtered['C_L [ft/sqrt(min)]']
                leak_off = leak_off.to_list()

                ## Prepare lists for weighted averages
                user_weighted_stress_min = []
                user_weighted_stress_max = []
                user_weighted_leak_off = []

                ## Weighted average of values based on user weight
                for i in range(0, len(stress_min), user_weight):
                    user_weighted_stress_min_temp = np.average(stress_min[i:i+user_weight], weights = weights[i:i+user_weight])
                    user_weighted_stress_min.append(user_weighted_stress_min_temp)

                stress_min_hom = user_weighted_stress_min

                for i in range(0, len(stress_max), user_weight):
                    user_weighted_stress_max_temp = np.average(stress_max[i:i+user_weight], weights = weights[i:i+user_weight])
                    user_weighted_stress_max.append(user_weighted_stress_max_temp)

                stress_max_hom = user_weighted_stress_max

                for i in range(0, len(leak_off), user_weight):
                    user_weighted_leak_off_temp = np.average(leak_off[i:i+user_weight], weights = weights[i:i+user_weight])
                    user_weighted_leak_off.append(user_weighted_leak_off_temp)

                leak_off_hom = user_weighted_leak_off

                ## Repeat value 'user weight' times to get the step plot
                stress_min_hom_value = np.repeat(stress_min_hom, user_weight)
                stress_max_hom_value = np.repeat(stress_max_hom, user_weight)
                leak_off_hom_value = np.repeat(leak_off_hom, user_weight)

                ### Fracture Toughness

                ## Homogenize K_h_x1
                ## Must find the actual values first
                K_h_x1 = rock_props_filtered['K_h [MPa/sqrt(m)]']**2/ rock_props_filtered['E_prime_h [Mpsi]']
                weighted_K_h_x1 = np.average(K_h_x1, weights = weights)

                ## Prepare lists for weighted averages
                user_weighted_K_h_x1 = []

                # Weighted average of values based on user weight
                for i in range(0, len(K_h_x1), user_weight):
                    user_weighted_K_h_x1_temp = np.average(K_h_x1[i:i+user_weight], weights = weights[i:i+user_weight])
                    user_weighted_K_h_x1.append(user_weighted_K_h_x1_temp)

                K_h_hom = np.array(np.array(E_prime_h_hom[:len(user_weighted_K_h_x1)]) * np.array(user_weighted_K_h_x1)) ** (0.5)

                ## Repeat value 'user weight' times to get the step plot
                K_h_hom_value = np.repeat(K_h_hom, user_weight)

                ## Homogenize K_v_x1
                ## Must find the actual values first
                K_v_x1 = rock_props_filtered['K_v [MPa/sqrt(m)]']**2/ rock_props_filtered['E_prime_v [Mpsi]']
                # print(K_v_x1)

                ## Prepare lists for weighted averages
                user_maxed_K_v_x1 = []

                # Maximum value of values based on user weight
                for i in range(0, len(K_v_x1), user_weight):
                    user_maxed_K_v_x1_temp = np.max(K_v_x1[i:i+user_weight])
                    # print(user_maxed_K_v_x1_temp)
                    user_maxed_K_v_x1.append(user_maxed_K_v_x1_temp)

                K_v_hom = (E_prime_v_hom * user_maxed_K_v_x1) ** (0.5)

                ## Repeat value 'user weight' times to get the step plot
                K_v_hom_value = np.repeat(K_v_hom, user_weight)

                df = pd.DataFrame(list(zip(depth_list, E_h_hom_value, v_h_hom_value, K_h_hom_value, K_v_hom_value, stress_min_hom_value, stress_max_hom_value, leak_off_hom_value)))
                df.columns = ['Depth', 'E_h_hom [Mpsi]', 'v_h_hom', 'K_h_hom [MPa/sqrt(m)]', 'K_v_hom [MPa/sqrt(m)]', 'Stress_Min_hom [psi]','Stress_Max_hom [psi]', 'leak_off_hom [ft/sqrt(min)]']

                df.to_csv('HomogenizedOutput_VTI_Shale.csv', index = False)

        self.vti_checkbox.stateChanged.connect(vti_shale_calcs)
        self.shale_checkbox.stateChanged.connect(vti_shale_calcs)

        ## Final Plotting
        def plotting():

            if self.iso_checkbox.isChecked() == True & self.shale_checkbox.isChecked() == True: # ISO and SHALE
                df = pd.read_csv('HomogenizedOutput_Iso_Shale.csv')
                figure = plt.figure(num = 'Homogenized Parameters')
                axis1 = figure.add_subplot(1,6,1)

                figure.suptitle('Homogenized Parameters', size = 18)

                axis1.plot(rock_props['K [MPa/sqrt(m)]'].to_list(), rock_props['Depth (m)'].to_list(), color = 'grey', alpha = 0.75)
                axis1.plot(df['K_hom [MPa/sqrt(m)]'] , df['Depth'], color = 'black')
                axis1.invert_yaxis()
                axis1.set_xlabel(r'$K$ ($MPa/\sqrt{m}$)', size = 14)
                axis1.set_ylabel('Depth (m)', size = 16)
                axis1.tick_params(axis='x', labelsize = 12)
                axis1.tick_params(axis='y', labelsize = 12)

                axis3 = figure.add_subplot(162, sharey = axis1)

                axis3.plot(rock_props['E_iso [Mpsi]'].to_list(), rock_props['Depth (m)'].to_list(), color = 'grey', alpha = 0.75)
                axis3.plot(df['E_hom [Mpsi]'] , df['Depth'], color = 'black')
                axis3.set_xlabel(r'$E$ ($Mpsi$)', size = 14)
                axis3.tick_params(axis='x', labelsize = 12)
                axis3.tick_params(axis='y', labelsize = 12)

                axis4 = figure.add_subplot(163, sharey = axis1)

                axis4.plot(rock_props['v_iso'].to_list(), rock_props['Depth (m)'].to_list(), color = 'grey', alpha = 0.75)
                axis4.plot(df['v_hom'] , df['Depth'], color = 'black')
                axis4.set_xlabel(r'$\nu$', size = 14)
                axis4.tick_params(axis='x', labelsize = 12)
                axis4.tick_params(axis='y', labelsize = 12)

                axis5 = figure.add_subplot(164, sharey = axis1)

                axis5.plot(rock_props['C_L [ft/sqrt(min)]'].to_list(), rock_props['Depth (m)'].to_list(), color = 'grey', alpha = 0.75)
                axis5.plot(df['leak_off_hom [ft/sqrt(min)]'] , df['Depth'], color = 'black')
                axis5.set_xlabel(r'$C_l$ ($ft/\sqrt{min}$)', size = 14)
                axis5.tick_params(axis='x', labelsize = 12)
                axis5.tick_params(axis='y', labelsize = 12)

                axis6 = figure.add_subplot(165, sharey = axis1)

                axis6.plot(rock_props['Min Stress'].to_list(), rock_props['Depth (m)'].to_list(), color = 'grey', alpha = 0.75)
                axis6.plot(df['Stress_Min_hom [psi]'] , df['Depth'], color = 'black')
                axis6.set_xlabel(r'$\sigma_h$ ($psi$)', size = 14)
                axis6.tick_params(axis='x', labelsize = 12)
                axis6.tick_params(axis='y', labelsize = 12)

                # axis7 = figure.add_subplot(166, sharey = axis1)

                # axis7.plot(rock_props['Max Stress'].to_list(), rock_props['Depth (m)'].to_list(), color = 'grey', alpha = 0.75)
                # axis7.plot(df['Stress_Max_hom [psi]'] , df['Depth'], color = 'black')
                # axis7.set_xlabel(r'$\sigma_H$ ($psi$)', size = 14)
                # axis7.tick_params(axis='x', labelsize = 12)
                # axis7.tick_params(axis='y', labelsize = 12)

                # plt.close()
                plt.subplots_adjust(left=0.039, bottom=0.063, right=0.992, top=0.944, wspace=0.194, hspace=0.4)
                figManager = plt.get_current_fig_manager()
                figManager.window.showMaximized()
                plt.show()
                # plt.savefig('Homogenized_Params', dpi = 1000)

            if self.iso_checkbox.isChecked() == True & self.sand_checkbox.isChecked() == True: # ISO and SAND
                df = pd.read_csv('HomogenizedOutput_Iso_Sand.csv')
                figure = plt.figure(num = 'Homogenized Parameters')
                axis1 = figure.add_subplot(1,6,1)

                figure.suptitle('Homogenized Parameters', size = 18)

                axis1.plot(rock_props['K [MPa/sqrt(m)]'].to_list(), rock_props['Depth (m)'].to_list(), color = 'grey', alpha = 0.75)
                axis1.plot(df['K_hom [MPa/sqrt(m)]'] , df['Depth'], color = 'black')
                axis1.invert_yaxis()
                axis1.set_xlabel(r'$K$ ($MPa/\sqrt{m}$)', size = 14)
                axis1.set_ylabel('Depth (m)', size = 16)
                axis1.tick_params(axis='x', labelsize = 12)
                axis1.tick_params(axis='y', labelsize = 12)

                axis3 = figure.add_subplot(162, sharey = axis1)

                axis3.plot(rock_props['E_iso [Mpsi]'].to_list(), rock_props['Depth (m)'].to_list(), color = 'grey', alpha = 0.75)
                axis3.plot(df['E_hom [Mpsi]'] , df['Depth'], color = 'black')
                axis3.set_xlabel(r'$E$ ($Mpsi$)', size = 14)
                axis3.tick_params(axis='x', labelsize = 12)
                axis3.tick_params(axis='y', labelsize = 12)

                axis4 = figure.add_subplot(163, sharey = axis1)

                axis4.plot(rock_props['v_iso'].to_list(), rock_props['Depth (m)'].to_list(), color = 'grey', alpha = 0.75)
                axis4.plot(df['v_hom'] , df['Depth'], color = 'black')
                axis4.set_xlabel(r'$\nu$', size = 14)
                axis4.tick_params(axis='x', labelsize = 12)
                axis4.tick_params(axis='y', labelsize = 12)

                axis5 = figure.add_subplot(164, sharey = axis1)

                axis5.plot(rock_props['C_L [ft/sqrt(min)]'].to_list(), rock_props['Depth (m)'].to_list(), color = 'grey', alpha = 0.75)
                axis5.plot(df['leak_off_hom [ft/sqrt(min)]'] , df['Depth'], color = 'black')
                axis5.set_xlabel(r'$C_l$ ($ft/\sqrt{min}$)', size = 14)
                axis5.tick_params(axis='x', labelsize = 12)
                axis5.tick_params(axis='y', labelsize = 12)

                axis6 = figure.add_subplot(165, sharey = axis1)

                axis6.plot(rock_props['Min Stress'].to_list(), rock_props['Depth (m)'].to_list(), color = 'grey', alpha = 0.75)
                axis6.plot(df['Stress_Min_hom [psi]'] , df['Depth'], color = 'black')
                axis6.set_xlabel(r'$\sigma_h$ ($psi$)', size = 14)
                axis6.tick_params(axis='x', labelsize = 12)
                axis6.tick_params(axis='y', labelsize = 12)

                axis7 = figure.add_subplot(166, sharey = axis1)

                # axis7.plot(rock_props['Max Stress'].to_list(), rock_props['Depth (m)'].to_list(), color = 'grey', alpha = 0.75)
                # axis7.plot(df['Stress_Max_hom [psi]'] , df['Depth'], color = 'black')
                # axis7.set_xlabel(r'$\sigma_H$ ($psi$)', size = 14)
                # axis7.tick_params(axis='x', labelsize = 12)
                # axis7.tick_params(axis='y', labelsize = 12)

                # plt.close()
                plt.subplots_adjust(left=0.039, bottom=0.063, right=0.992, top=0.944, wspace=0.194, hspace=0.4)
                figManager = plt.get_current_fig_manager()
                figManager.window.showMaximized()
                plt.show()
                # plt.savefig('Homogenized_Params', dpi = 1000)
            
            if self.vti_checkbox.isChecked() == True & self.sand_checkbox.isChecked() == True: # VTI and SHALE
                df = pd.read_csv('HomogenizedOutput_VTI_Sand.csv')
                figure = plt.figure(num = 'Homogenized Parameters')
                axis1 = figure.add_subplot(1,7,1)

                figure.suptitle('Homogenized Parameters', size = 18)

                axis1.plot(rock_props['K_h [MPa/sqrt(m)]'].to_list(), rock_props['Depth (m)'].to_list(), color = 'grey', alpha = 0.75)
                axis1.plot(df['K_h_hom [MPa/sqrt(m)]'] , df['Depth'], color = 'black')
                axis1.invert_yaxis()
                axis1.set_xlabel(r'$K_{h}$ ($MPa/\sqrt{m}$)', size = 14)
                axis1.set_ylabel('Depth (m)', size = 16)
                axis1.tick_params(axis='x', labelsize = 12)
                axis1.tick_params(axis='y', labelsize = 12)

                axis2 = figure.add_subplot(172, sharey = axis1)

                axis2.plot(rock_props['K_v [MPa/sqrt(m)]'].to_list(), rock_props['Depth (m)'].to_list(), color = 'grey', alpha = 0.75)
                axis2.plot(df['K_v_hom [MPa/sqrt(m)]'] , df['Depth'], color = 'black')
                axis2.set_xlabel(r'$K_{v}$ ($MPa/\sqrt{m}$)', size = 14)
                axis2.tick_params(axis='x', labelsize = 12)
                axis2.tick_params(axis='y', labelsize = 12)

                axis3 = figure.add_subplot(173, sharey = axis1)

                axis3.plot(rock_props['E_VTI_h [Mpsi]'].to_list(), rock_props['Depth (m)'].to_list(), color = 'grey', alpha = 0.75)
                axis3.plot(df['E_h_hom [Mpsi]'] , df['Depth'], color = 'black')
                axis3.set_xlabel(r'$E$ ($Mpsi$)', size = 14)
                axis3.tick_params(axis='x', labelsize = 12)
                axis3.tick_params(axis='y', labelsize = 12)

                axis4 = figure.add_subplot(174, sharey = axis1)

                axis4.plot(rock_props['v_VTI_h'].to_list(), rock_props['Depth (m)'].to_list(), color = 'grey', alpha = 0.75)
                axis4.plot(df['v_h_hom'] , df['Depth'], color = 'black')
                axis4.set_xlabel(r'$\nu$', size = 14)
                axis4.tick_params(axis='x', labelsize = 12)
                axis4.tick_params(axis='y', labelsize = 12)

                axis5 = figure.add_subplot(175, sharey = axis1)

                axis5.plot(rock_props['C_L [ft/sqrt(min)]'].to_list(), rock_props['Depth (m)'].to_list(), color = 'grey', alpha = 0.75)
                axis5.plot(df['leak_off_hom [ft/sqrt(min)]'] , df['Depth'], color = 'black')
                axis5.set_xlabel(r'$C_l$ ($ft/\sqrt{min}$)', size = 14)
                axis5.tick_params(axis='x', labelsize = 12)
                axis5.tick_params(axis='y', labelsize = 12)

                axis6 = figure.add_subplot(176, sharey = axis1)

                axis6.plot(rock_props['Min Stress'].to_list(), rock_props['Depth (m)'].to_list(), color = 'grey', alpha = 0.75)
                axis6.plot(df['Stress_Min_hom [psi]'] , df['Depth'], color = 'black')
                axis6.set_xlabel(r'$\sigma_h$ ($psi$)', size = 14)
                axis6.tick_params(axis='x', labelsize = 12)
                axis6.tick_params(axis='y', labelsize = 12)

                # axis7 = figure.add_subplot(177, sharey = axis1)

                # axis7.plot(rock_props['Max Stress'].to_list(), rock_props['Depth (m)'].to_list(), color = 'grey', alpha = 0.75)
                # axis7.plot(df['Stress_Max_hom [psi]'] , df['Depth'], color = 'black')
                # axis7.set_xlabel(r'$\sigma_H$ ($psi$)', size = 14)
                # axis7.tick_params(axis='x', labelsize = 12)
                # axis7.tick_params(axis='y', labelsize = 12)

                # plt.close()
                plt.subplots_adjust(left=0.039, bottom=0.063, right=0.992, top=0.944, wspace=0.194, hspace=0.4)
                figManager = plt.get_current_fig_manager()
                figManager.window.showMaximized()
                plt.show()
                # plt.savefig('Homogenized_Params', dpi = 1000)

            if self.vti_checkbox.isChecked() == True & self.shale_checkbox.isChecked() == True: # VTI and SHALE
                df = pd.read_csv('HomogenizedOutput_VTI_Shale.csv')
                figure = plt.figure(num = 'Homogenized Parameters')
                axis1 = figure.add_subplot(1,7,1)

                figure.suptitle('Homogenized Parameters', size = 18)

                axis1.plot(rock_props['K_h [MPa/sqrt(m)]'].to_list(), rock_props['Depth (m)'].to_list(), color = 'grey', alpha = 0.75)
                axis1.plot(df['K_h_hom [MPa/sqrt(m)]'] , df['Depth'], color = 'black')
                axis1.invert_yaxis()
                axis1.set_xlabel(r'$K_{h}$ ($MPa/\sqrt{m}$)', size = 14)
                axis1.set_ylabel('Depth (m)', size = 16)
                axis1.tick_params(axis='x', labelsize = 12)
                axis1.tick_params(axis='y', labelsize = 12)

                axis2 = figure.add_subplot(172, sharey = axis1)

                axis2.plot(rock_props['K_v [MPa/sqrt(m)]'].to_list(), rock_props['Depth (m)'].to_list(), color = 'grey', alpha = 0.75)
                axis2.plot(df['K_v_hom [MPa/sqrt(m)]'] , df['Depth'], color = 'black')
                axis2.set_xlabel(r'$K_{v}$ ($MPa/\sqrt{m}$)', size = 14)
                axis2.tick_params(axis='x', labelsize = 12)
                axis2.tick_params(axis='y', labelsize = 12)

                axis3 = figure.add_subplot(173, sharey = axis1)

                axis3.plot(rock_props['E_VTI_h [Mpsi]'].to_list(), rock_props['Depth (m)'].to_list(), color = 'grey', alpha = 0.75)
                axis3.plot(df['E_h_hom [Mpsi]'] , df['Depth'], color = 'black')
                axis3.set_xlabel(r'$E$ ($Mpsi$)', size = 14)
                axis3.tick_params(axis='x', labelsize = 12)
                axis3.tick_params(axis='y', labelsize = 12)

                axis4 = figure.add_subplot(174, sharey = axis1)

                axis4.plot(rock_props['v_VTI_h'].to_list(), rock_props['Depth (m)'].to_list(), color = 'grey', alpha = 0.75)
                axis4.plot(df['v_h_hom'] , df['Depth'], color = 'black')
                axis4.set_xlabel(r'$\nu$', size = 14)
                axis4.tick_params(axis='x', labelsize = 12)
                axis4.tick_params(axis='y', labelsize = 12)

                axis5 = figure.add_subplot(175, sharey = axis1)

                axis5.plot(rock_props['C_L [ft/sqrt(min)]'].to_list(), rock_props['Depth (m)'].to_list(), color = 'grey', alpha = 0.75)
                axis5.plot(df['leak_off_hom [ft/sqrt(min)]'] , df['Depth'], color = 'black')
                axis5.set_xlabel(r'$C_l$ ($ft/\sqrt{min}$)', size = 14)
                axis5.tick_params(axis='x', labelsize = 12)
                axis5.tick_params(axis='y', labelsize = 12)

                axis6 = figure.add_subplot(176, sharey = axis1)

                axis6.plot(rock_props['Min Stress'].to_list(), rock_props['Depth (m)'].to_list(), color = 'grey', alpha = 0.75)
                axis6.plot(df['Stress_Min_hom [psi]'] , df['Depth'], color = 'black')
                axis6.set_xlabel(r'$\sigma_h$ ($psi$)', size = 14)
                axis6.tick_params(axis='x', labelsize = 12)
                axis6.tick_params(axis='y', labelsize = 12)

                # axis7 = figure.add_subplot(177, sharey = axis1)

                # axis7.plot(rock_props['Max Stress'].to_list(), rock_props['Depth (m)'].to_list(), color = 'grey', alpha = 0.75)
                # axis7.plot(df['Stress_Max_hom [psi]'] , df['Depth'], color = 'black')
                # axis7.set_xlabel(r'$\sigma_H$ ($psi$)', size = 14)
                # axis7.tick_params(axis='x', labelsize = 12)
                # axis7.tick_params(axis='y', labelsize = 12)

                # plt.close()
                plt.subplots_adjust(left=0.039, bottom=0.063, right=0.992, top=0.944, wspace=0.194, hspace=0.4)
                figManager = plt.get_current_fig_manager()
                figManager.window.showMaximized()
                plt.show()
                # plt.savefig('Homogenized_Params', dpi = 1000)

        self.view_plot_button.clicked.connect(plotting)

    def retranslateUi(self, RockView):
        _translate = QtCore.QCoreApplication.translate
        RockView.setWindowTitle(_translate("RockView", "RockView"))
        self.browse_las_button.setToolTip(_translate("RockView", "Open CSV log file"))
        self.browse_las_button.setText(_translate("RockView", "Browse log files"))
        self.browse_bedding_button.setToolTip(_translate("RockView", "Open CSV bedding data"))
        self.browse_bedding_button.setText(_translate("RockView", "Browse bedding data"))
        self.conductivity_label_2.setText(_translate("RockView", "Homogenization"))
        self.homo_label.setText(_translate("RockView", "Layers to homogenize"))
        self.homo_value.setToolTip(_translate("RockView", "Number of layer to homogenize over"))
        self.homo_value.setText(_translate("RockView", "50"))
        self.static_elastic_params_label.setText(_translate("RockView", "Static Elastic Parameters"))
        self.static_elastic_params_label_2.setText(_translate("RockView", "<i>E</i><sub>s</sub> = a<i>E</i><sub>d</sub> + b"))
        self.static_elastic_params_a_label.setText(_translate("RockView", "a"))
        self.static_elastic_params_a_float.setText(_translate("RockView", "0.5"))
        self.static_elastic_params_b_label.setText(_translate("RockView", "b"))
        self.static_elastic_params_b_float.setText(_translate("RockView", "0"))
        self.frac_toughness_params_label.setText(_translate("RockView", "Fracture Toughness Parameters"))
        self.k1c_iso_label.setText(_translate("RockView", "K<sub>1c</sub><sup><i>iso</i></sup>"))
        self.k1c_m_label.setText(_translate("RockView", "m"))
        self.k1c_value.setText(_translate("RockView", "5"))
        self.k1c_vti_label.setText(_translate("RockView", "K<sub>1c</sub><sup><i>vti</i></sup>"))
        self.k1c_v_label.setText(_translate("RockView", "m<sub>v</sub>"))
        self.k1c_v_value.setText(_translate("RockView", "5"))
        self.k1c_h_value.setText(_translate("RockView", "m<sub>h</sub>"))
        self.k1c_h_label.setText(_translate("RockView", "5"))
        self.frac_toughness_params_label_2.setText(_translate("RockView", "Leak-off Coefficient"))
        self.cf_label_2.setText(_translate("RockView", "C<sub>L</sub>"))
        self.leak_off_value.setText(_translate("RockView", "0.0001"))
        self.leak_off_unit_label.setText(_translate("RockView", "ft/<span>&#8730;min</span>"))
        self.conductivity_label.setText(_translate("RockView", "Interface Conductivity"))
        self.matrix_perm_label.setText(_translate("RockView", "Matrix Permeability"))
        self.matrix_perm_label_2.setText(_translate("RockView", "k"))
        self.matrix_perm_value.setText(_translate("RockView", "10"))
        self.matrix_perm_unit.setText(_translate("RockView", "mD"))
        self.form_characterization_label.setText(_translate("RockView", "Formation Characterization"))
        self.iso_checkbox.setText(_translate("RockView", "Isotropic"))
        self.vti_checkbox.setText(_translate("RockView", "VTI"))
        self.medium_label.setText(_translate("RockView", "Medium"))
        self.medium_label_2.setText(_translate("RockView", "Lithology"))
        self.sand_checkbox.setText(_translate("RockView", "Sandstone"))
        self.shale_checkbox.setText(_translate("RockView", "Shale"))
        self.view_plot_button.setText(_translate("RockView", "View Homogenization"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RockView = QtWidgets.QMainWindow()
    ui = Ui_RockView()
    ui.setupUi(RockView)
    RockView.show()
    sys.exit(app.exec_())
