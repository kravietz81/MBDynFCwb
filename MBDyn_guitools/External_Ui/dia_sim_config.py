# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dia_sim_config.ui',
# licensing of 'dia_sim_config.ui' applies.
#
# Created: Sun Sep 20 00:42:49 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_dia_sim_config(object):
    def setupUi(self, dia_sim_config):
        dia_sim_config.setObjectName("dia_sim_config")
        dia_sim_config.resize(394, 751)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dia_sim_config.sizePolicy().hasHeightForWidth())
        dia_sim_config.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(dia_sim_config)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(dia_sim_config)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.bDefault = QtWidgets.QPushButton(self.frame)
        self.bDefault.setObjectName("bDefault")
        self.gridLayout.addWidget(self.bDefault, 1, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.frame)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 2, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setObjectName("tabWidget")
        self.GeneralTab = QtWidgets.QWidget()
        self.GeneralTab.setObjectName("GeneralTab")
        self.formLayout_8 = QtWidgets.QFormLayout(self.GeneralTab)
        self.formLayout_8.setObjectName("formLayout_8")
        self.label_7 = QtWidgets.QLabel(self.GeneralTab)
        self.label_7.setObjectName("label_7")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.leSimName = QtWidgets.QLineEdit(self.GeneralTab)
        self.leSimName.setText("")
        self.leSimName.setObjectName("leSimName")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.leSimName)
        self.label_8 = QtWidgets.QLabel(self.GeneralTab)
        self.label_8.setObjectName("label_8")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.frame_2 = QtWidgets.QFrame(self.GeneralTab)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leWorkingDir = QtWidgets.QLineEdit(self.frame_2)
        self.leWorkingDir.setObjectName("leWorkingDir")
        self.horizontalLayout.addWidget(self.leWorkingDir)
        self.bSelectWorkingDir = QtWidgets.QPushButton(self.frame_2)
        self.bSelectWorkingDir.setObjectName("bSelectWorkingDir")
        self.horizontalLayout.addWidget(self.bSelectWorkingDir)
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.frame_2)
        self.label_9 = QtWidgets.QLabel(self.GeneralTab)
        self.label_9.setEnabled(False)
        self.label_9.setObjectName("label_9")
        self.formLayout_8.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.cbSolver = QtWidgets.QComboBox(self.GeneralTab)
        self.cbSolver.setEnabled(False)
        self.cbSolver.setObjectName("cbSolver")
        self.formLayout_8.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cbSolver)
        self.tabWidget.addTab(self.GeneralTab, "")
        self.ProblemTab = QtWidgets.QWidget()
        self.ProblemTab.setObjectName("ProblemTab")
        self.formLayout_2 = QtWidgets.QFormLayout(self.ProblemTab)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_10 = QtWidgets.QLabel(self.ProblemTab)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.leInitialTime = QtWidgets.QLineEdit(self.ProblemTab)
        self.leInitialTime.setText("")
        self.leInitialTime.setObjectName("leInitialTime")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.leInitialTime)
        self.label_11 = QtWidgets.QLabel(self.ProblemTab)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.leFinalTime = QtWidgets.QLineEdit(self.ProblemTab)
        self.leFinalTime.setText("")
        self.leFinalTime.setObjectName("leFinalTime")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.leFinalTime)
        self.label_12 = QtWidgets.QLabel(self.ProblemTab)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.leTimeStep = QtWidgets.QLineEdit(self.ProblemTab)
        self.leTimeStep.setObjectName("leTimeStep")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.leTimeStep)
        self.cbMaxIterations = QtWidgets.QCheckBox(self.ProblemTab)
        self.cbMaxIterations.setChecked(True)
        self.cbMaxIterations.setObjectName("cbMaxIterations")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.cbMaxIterations)
        self.leMaxIterations = QtWidgets.QLineEdit(self.ProblemTab)
        self.leMaxIterations.setObjectName("leMaxIterations")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.leMaxIterations)
        self.cbTol = QtWidgets.QCheckBox(self.ProblemTab)
        self.cbTol.setChecked(True)
        self.cbTol.setObjectName("cbTol")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.cbTol)
        self.leTol = QtWidgets.QLineEdit(self.ProblemTab)
        self.leTol.setObjectName("leTol")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.leTol)
        self.cbDerTol = QtWidgets.QCheckBox(self.ProblemTab)
        self.cbDerTol.setObjectName("cbDerTol")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.cbDerTol)
        self.leDerTol = QtWidgets.QLineEdit(self.ProblemTab)
        self.leDerTol.setEnabled(False)
        self.leDerTol.setObjectName("leDerTol")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.leDerTol)
        self.cbOutput = QtWidgets.QGroupBox(self.ProblemTab)
        self.cbOutput.setCheckable(True)
        self.cbOutput.setChecked(False)
        self.cbOutput.setObjectName("cbOutput")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.cbOutput)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox_11 = QtWidgets.QCheckBox(self.cbOutput)
        self.checkBox_11.setObjectName("checkBox_11")
        self.gridLayout_2.addWidget(self.checkBox_11, 1, 3, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.cbOutput)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_2.addWidget(self.checkBox_3, 0, 2, 1, 1)
        self.checkBox_9 = QtWidgets.QCheckBox(self.cbOutput)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout_2.addWidget(self.checkBox_9, 3, 0, 1, 2)
        self.checkBox_7 = QtWidgets.QCheckBox(self.cbOutput)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout_2.addWidget(self.checkBox_7, 1, 1, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.cbOutput)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_2.addWidget(self.checkBox_4, 0, 3, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.cbOutput)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout_2.addWidget(self.checkBox_6, 1, 0, 1, 1)
        self.checkBox_10 = QtWidgets.QCheckBox(self.cbOutput)
        self.checkBox_10.setObjectName("checkBox_10")
        self.gridLayout_2.addWidget(self.checkBox_10, 3, 2, 1, 2)
        self.checkBox_5 = QtWidgets.QCheckBox(self.cbOutput)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout_2.addWidget(self.checkBox_5, 2, 0, 1, 2)
        self.checkBox = QtWidgets.QCheckBox(self.cbOutput)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)
        self.checkBox_8 = QtWidgets.QCheckBox(self.cbOutput)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout_2.addWidget(self.checkBox_8, 1, 2, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.cbOutput)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_2.addWidget(self.checkBox_2, 0, 1, 1, 1)
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.cbOutput)
        self.cbMethod = QtWidgets.QGroupBox(self.ProblemTab)
        self.cbMethod.setCheckable(True)
        self.cbMethod.setChecked(False)
        self.cbMethod.setObjectName("cbMethod")
        self.formLayout_7 = QtWidgets.QFormLayout(self.cbMethod)
        self.formLayout_7.setObjectName("formLayout_7")
        self.method = QtWidgets.QComboBox(self.cbMethod)
        self.method.setEnabled(False)
        self.method.setObjectName("method")
        self.method.addItem("")
        self.method.addItem("")
        self.method.addItem("")
        self.method.addItem("")
        self.method.addItem("")
        self.method.addItem("")
        self.method.addItem("")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.method)
        self.methods_stack = QtWidgets.QStackedWidget(self.cbMethod)
        self.methods_stack.setEnabled(False)
        self.methods_stack.setObjectName("methods_stack")
        self.select = QtWidgets.QWidget()
        self.select.setObjectName("select")
        self.methods_stack.addWidget(self.select)
        self.cn = QtWidgets.QWidget()
        self.cn.setObjectName("cn")
        self.methods_stack.addWidget(self.cn)
        self.ms = QtWidgets.QWidget()
        self.ms.setObjectName("ms")
        self.formLayout_3 = QtWidgets.QFormLayout(self.ms)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label = QtWidgets.QLabel(self.ms)
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.ms_differential_radius = QtWidgets.QLineEdit(self.ms)
        self.ms_differential_radius.setObjectName("ms_differential_radius")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ms_differential_radius)
        self.label_2 = QtWidgets.QLabel(self.ms)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.ms_algebraic_radius = QtWidgets.QLineEdit(self.ms)
        self.ms_algebraic_radius.setObjectName("ms_algebraic_radius")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ms_algebraic_radius)
        self.methods_stack.addWidget(self.ms)
        self.hope = QtWidgets.QWidget()
        self.hope.setObjectName("hope")
        self.formLayout_4 = QtWidgets.QFormLayout(self.hope)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_3 = QtWidgets.QLabel(self.hope)
        self.label_3.setObjectName("label_3")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.hope_differential_radius = QtWidgets.QLineEdit(self.hope)
        self.hope_differential_radius.setObjectName("hope_differential_radius")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.hope_differential_radius)
        self.label_4 = QtWidgets.QLabel(self.hope)
        self.label_4.setObjectName("label_4")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.hope_algebraic_radius = QtWidgets.QLineEdit(self.hope)
        self.hope_algebraic_radius.setObjectName("hope_algebraic_radius")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.hope_algebraic_radius)
        self.methods_stack.addWidget(self.hope)
        self.thirdOrder = QtWidgets.QWidget()
        self.thirdOrder.setObjectName("thirdOrder")
        self.formLayout_5 = QtWidgets.QFormLayout(self.thirdOrder)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_5 = QtWidgets.QLabel(self.thirdOrder)
        self.label_5.setObjectName("label_5")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.thirdOrder_algebraic_radius = QtWidgets.QLineEdit(self.thirdOrder)
        self.thirdOrder_algebraic_radius.setObjectName("thirdOrder_algebraic_radius")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.thirdOrder_algebraic_radius)
        self.cbAdHoc = QtWidgets.QCheckBox(self.thirdOrder)
        self.cbAdHoc.setObjectName("cbAdHoc")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.cbAdHoc)
        self.methods_stack.addWidget(self.thirdOrder)
        self.bdf = QtWidgets.QWidget()
        self.bdf.setObjectName("bdf")
        self.formLayout_6 = QtWidgets.QFormLayout(self.bdf)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_6 = QtWidgets.QLabel(self.bdf)
        self.label_6.setObjectName("label_6")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.bdf_order = QtWidgets.QLineEdit(self.bdf)
        self.bdf_order.setObjectName("bdf_order")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.bdf_order)
        spacerItem1 = QtWidgets.QSpacerItem(191, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout_6.setItem(0, QtWidgets.QFormLayout.SpanningRole, spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(134, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout_6.setItem(1, QtWidgets.QFormLayout.SpanningRole, spacerItem2)
        self.methods_stack.addWidget(self.bdf)
        self.ie = QtWidgets.QWidget()
        self.ie.setObjectName("ie")
        self.methods_stack.addWidget(self.ie)
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.methods_stack)
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.cbMethod)
        self.cbPbCustomParam = QtWidgets.QGroupBox(self.ProblemTab)
        self.cbPbCustomParam.setCheckable(True)
        self.cbPbCustomParam.setChecked(False)
        self.cbPbCustomParam.setObjectName("cbPbCustomParam")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.cbPbCustomParam)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ptePbCustomParam = QtWidgets.QPlainTextEdit(self.cbPbCustomParam)
        self.ptePbCustomParam.setObjectName("ptePbCustomParam")
        self.verticalLayout.addWidget(self.ptePbCustomParam)
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.cbPbCustomParam)
        self.tabWidget.addTab(self.ProblemTab, "")
        self.ControlDataTab = QtWidgets.QWidget()
        self.ControlDataTab.setObjectName("ControlDataTab")
        self.formLayout = QtWidgets.QFormLayout(self.ControlDataTab)
        self.formLayout.setObjectName("formLayout")
        self.cbCtrlCustomParam = QtWidgets.QGroupBox(self.ControlDataTab)
        self.cbCtrlCustomParam.setCheckable(True)
        self.cbCtrlCustomParam.setChecked(False)
        self.cbCtrlCustomParam.setObjectName("cbCtrlCustomParam")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.cbCtrlCustomParam)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pteCtrlCustomParam = QtWidgets.QPlainTextEdit(self.cbCtrlCustomParam)
        self.pteCtrlCustomParam.setObjectName("pteCtrlCustomParam")
        self.verticalLayout_2.addWidget(self.pteCtrlCustomParam)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.cbCtrlCustomParam)
        self.tabWidget.addTab(self.ControlDataTab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 3)
        self.verticalLayout_3.addWidget(self.frame)

        self.retranslateUi(dia_sim_config)
        self.tabWidget.setCurrentIndex(1)
        self.methods_stack.setCurrentIndex(0)
        QtCore.QObject.connect(self.method, QtCore.SIGNAL("currentIndexChanged(int)"), self.methods_stack.setCurrentIndex)
        QtCore.QObject.connect(self.cbMaxIterations, QtCore.SIGNAL("clicked(bool)"), self.leMaxIterations.setEnabled)
        QtCore.QObject.connect(self.cbTol, QtCore.SIGNAL("clicked(bool)"), self.leTol.setEnabled)
        QtCore.QObject.connect(self.cbDerTol, QtCore.SIGNAL("clicked(bool)"), self.leDerTol.setEnabled)
        QtCore.QObject.connect(self.cbMethod, QtCore.SIGNAL("clicked(bool)"), self.method.setEnabled)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), dia_sim_config.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), dia_sim_config.reject)
        QtCore.QObject.connect(self.bDefault, QtCore.SIGNAL("clicked()"), dia_sim_config.setDefault)
        QtCore.QObject.connect(self.cbMethod, QtCore.SIGNAL("clicked(bool)"), self.methods_stack.setEnabled)
        QtCore.QObject.connect(self.cbAdHoc, QtCore.SIGNAL("clicked(bool)"), self.thirdOrder_algebraic_radius.setDisabled)
        QtCore.QObject.connect(self.bSelectWorkingDir, QtCore.SIGNAL("clicked()"), dia_sim_config.SetWorkingDirectory)
        QtCore.QMetaObject.connectSlotsByName(dia_sim_config)

    def retranslateUi(self, dia_sim_config):
        dia_sim_config.setWindowTitle(QtWidgets.QApplication.translate("dia_sim_config", "Dialog", None, -1))
        self.bDefault.setText(QtWidgets.QApplication.translate("dia_sim_config", "Default", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("dia_sim_config", "Simulation Name", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("dia_sim_config", "Working directory", None, -1))
        self.bSelectWorkingDir.setText(QtWidgets.QApplication.translate("dia_sim_config", "Browse...", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("dia_sim_config", "Solver", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.GeneralTab), QtWidgets.QApplication.translate("dia_sim_config", "General", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("dia_sim_config", "Initial Time", None, -1))
        self.leInitialTime.setProperty("unit", QtWidgets.QApplication.translate("dia_sim_config", "\"s\"", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("dia_sim_config", "Final Time", None, -1))
        self.label_12.setText(QtWidgets.QApplication.translate("dia_sim_config", "Time Step", None, -1))
        self.cbMaxIterations.setText(QtWidgets.QApplication.translate("dia_sim_config", "Max Iterations", None, -1))
        self.cbTol.setText(QtWidgets.QApplication.translate("dia_sim_config", "Tolerence", None, -1))
        self.cbDerTol.setText(QtWidgets.QApplication.translate("dia_sim_config", "Der. Tolerance", None, -1))
        self.cbOutput.setTitle(QtWidgets.QApplication.translate("dia_sim_config", "Output", None, -1))
        self.checkBox_11.setText(QtWidgets.QApplication.translate("dia_sim_config", "cpu time", None, -1))
        self.checkBox_3.setText(QtWidgets.QApplication.translate("dia_sim_config", "residual", None, -1))
        self.checkBox_9.setText(QtWidgets.QApplication.translate("dia_sim_config", "matrix condition number", None, -1))
        self.checkBox_7.setText(QtWidgets.QApplication.translate("dia_sim_config", "counter", None, -1))
        self.checkBox_4.setText(QtWidgets.QApplication.translate("dia_sim_config", "solution", None, -1))
        self.checkBox_6.setText(QtWidgets.QApplication.translate("dia_sim_config", "messages", None, -1))
        self.checkBox_10.setText(QtWidgets.QApplication.translate("dia_sim_config", "solver condition number", None, -1))
        self.checkBox_5.setText(QtWidgets.QApplication.translate("dia_sim_config", "jacobian matrix", None, -1))
        self.checkBox.setText(QtWidgets.QApplication.translate("dia_sim_config", "none", None, -1))
        self.checkBox_8.setText(QtWidgets.QApplication.translate("dia_sim_config", "bailout", None, -1))
        self.checkBox_2.setText(QtWidgets.QApplication.translate("dia_sim_config", "iterations", None, -1))
        self.cbMethod.setTitle(QtWidgets.QApplication.translate("dia_sim_config", "Method", None, -1))
        self.method.setItemText(0, QtWidgets.QApplication.translate("dia_sim_config", "--Select--", None, -1))
        self.method.setItemText(1, QtWidgets.QApplication.translate("dia_sim_config", "Crank Nicolson", None, -1))
        self.method.setItemText(2, QtWidgets.QApplication.translate("dia_sim_config", "ms", None, -1))
        self.method.setItemText(3, QtWidgets.QApplication.translate("dia_sim_config", "Hope", None, -1))
        self.method.setItemText(4, QtWidgets.QApplication.translate("dia_sim_config", "Third Order", None, -1))
        self.method.setItemText(5, QtWidgets.QApplication.translate("dia_sim_config", "bdf", None, -1))
        self.method.setItemText(6, QtWidgets.QApplication.translate("dia_sim_config", "Implicit Euler", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("dia_sim_config", "Dif. radius:", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("dia_sim_config", "Alg. radius:", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("dia_sim_config", "Dif. radius:", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("dia_sim_config", "Alg. radius:", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("dia_sim_config", "Alg. radius:", None, -1))
        self.cbAdHoc.setText(QtWidgets.QApplication.translate("dia_sim_config", "ad hoc", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("dia_sim_config", "Order", None, -1))
        self.cbPbCustomParam.setTitle(QtWidgets.QApplication.translate("dia_sim_config", "Custom Parameters", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ProblemTab), QtWidgets.QApplication.translate("dia_sim_config", "Problem", None, -1))
        self.cbCtrlCustomParam.setTitle(QtWidgets.QApplication.translate("dia_sim_config", "Custom Parameters", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ControlDataTab), QtWidgets.QApplication.translate("dia_sim_config", "Control Data", None, -1))

