import os
import openpyxl
import xlsxwriter
import clickable_label
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QFileDialog, QMessageBox, QListWidget


class UiQuizMainWindow(object):
    def __init__(self):
        super().__init__()
        QuizMainWindow.setObjectName("QuizMainWindow")
        QuizMainWindow.resize(688, 690)
        QuizMainWindow.setGeometry(800, 300, 500, 500)
        self.quiz_main_widget = QtWidgets.QWidget(QuizMainWindow)
        self.quiz_main_widget.setObjectName("quiz_main_widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.quiz_main_widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.quiz_right_frame = QtWidgets.QFrame(self.quiz_main_widget)
        self.quiz_right_frame.setEnabled(True)
        self.quiz_right_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.quiz_right_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.quiz_right_frame.setObjectName("quiz_right_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.quiz_right_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.answer_a_button = QtWidgets.QPushButton(self.quiz_right_frame)
        self.answer_a_button.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                           "color: rgb(255, 255, 255);")
        self.answer_a_button.setObjectName("answer_a_button")
        self.gridLayout.addWidget(self.answer_a_button, 19, 0, 1, 2)
        self.label_a = QtWidgets.QLabel(self.quiz_right_frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_a.setFont(font)
        self.label_a.setObjectName("label_a")
        self.gridLayout.addWidget(self.label_a, 17, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        self.main_question_text_display = QtWidgets.QTextBrowser(self.quiz_right_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_question_text_display.sizePolicy().hasHeightForWidth())
        self.main_question_text_display.setSizePolicy(sizePolicy)
        self.main_question_text_display.setMinimumSize(QtCore.QSize(0, 50))
        self.main_question_text_display.setObjectName("main_question_text_display")
        self.gridLayout.addWidget(self.main_question_text_display, 7, 1, 1, 4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 11, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.quiz_right_frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 18, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 20, 0, 1, 1)
        self.label_possible_answers = QtWidgets.QLabel(self.quiz_right_frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_possible_answers.setFont(font)
        self.label_possible_answers.setObjectName("label_possible_answers")
        self.gridLayout.addWidget(self.label_possible_answers, 16, 0, 1, 1)
        self.label_number_questions = QtWidgets.QLabel(self.quiz_right_frame)
        self.label_number_questions.setObjectName("label_number_questions")
        self.gridLayout.addWidget(self.label_number_questions, 3, 0, 1, 1)
        self.a_text_display = QtWidgets.QTextBrowser(self.quiz_right_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(11)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a_text_display.sizePolicy().hasHeightForWidth())
        self.a_text_display.setSizePolicy(sizePolicy)
        self.a_text_display.setMinimumSize(QtCore.QSize(220, 0))
        self.a_text_display.setObjectName("a_text_display")
        self.gridLayout.addWidget(self.a_text_display, 18, 0, 1, 2)
        self.label_quiz_details = QtWidgets.QLabel(self.quiz_right_frame)
        self.label_quiz_details.setObjectName("label_quiz_details")
        self.gridLayout.addWidget(self.label_quiz_details, 2, 0, 1, 5)
        self.label_d = QtWidgets.QLabel(self.quiz_right_frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_d.setFont(font)
        self.label_d.setObjectName("label_d")
        self.gridLayout.addWidget(self.label_d, 24, 3, 1, 1)
        self.d_text_display = QtWidgets.QTextBrowser(self.quiz_right_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d_text_display.sizePolicy().hasHeightForWidth())
        self.d_text_display.setSizePolicy(sizePolicy)
        self.d_text_display.setMinimumSize(QtCore.QSize(220, 0))
        self.d_text_display.setObjectName("d_text_display")
        self.gridLayout.addWidget(self.d_text_display, 25, 3, 1, 2)
        self.Answer_b_button = QtWidgets.QPushButton(self.quiz_right_frame)
        self.Answer_b_button.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                           "color: rgb(255, 255, 255);")
        self.Answer_b_button.setObjectName("Answer_b_button")
        self.gridLayout.addWidget(self.Answer_b_button, 19, 3, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 23, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 15, 0, 1, 1)
        self.answer_c_button = QtWidgets.QPushButton(self.quiz_right_frame)
        self.answer_c_button.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                           "color: rgb(255, 255, 255);")
        self.answer_c_button.setObjectName("answer_c_button")
        self.gridLayout.addWidget(self.answer_c_button, 26, 0, 1, 2)
        self.label_project_title_questionnaire = QtWidgets.QLabel(self.quiz_right_frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_project_title_questionnaire.setFont(font)
        self.label_project_title_questionnaire.setObjectName("label_project_title_questionnaire")
        self.gridLayout.addWidget(self.label_project_title_questionnaire, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 22, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 8, 0, 1, 1)
        self.c_text_display = QtWidgets.QTextBrowser(self.quiz_right_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c_text_display.sizePolicy().hasHeightForWidth())
        self.c_text_display.setSizePolicy(sizePolicy)
        self.c_text_display.setMinimumSize(QtCore.QSize(220, 0))
        self.c_text_display.setObjectName("c_text_display")
        self.gridLayout.addWidget(self.c_text_display, 25, 0, 1, 2)
        self.label_question = QtWidgets.QLabel(self.quiz_right_frame)
        self.label_question.setObjectName("label_question")
        self.gridLayout.addWidget(self.label_question, 7, 0, 1, 1)
        self.label_c = QtWidgets.QLabel(self.quiz_right_frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_c.setFont(font)
        self.label_c.setObjectName("label_c")
        self.gridLayout.addWidget(self.label_c, 24, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.quiz_right_frame)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 25, 2, 1, 1)
        self.quiz_stats_table = QtWidgets.QTableWidget(self.quiz_right_frame)
        self.quiz_stats_table.setAlternatingRowColors(True)
        self.quiz_stats_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.quiz_stats_table.setGridStyle(QtCore.Qt.SolidLine)
        self.quiz_stats_table.setRowCount(1)
        self.quiz_stats_table.setObjectName("quiz_stats_table")
        self.quiz_stats_table.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.quiz_stats_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.quiz_stats_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.quiz_stats_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.quiz_stats_table.setHorizontalHeaderItem(3, item)
        self.quiz_stats_table.horizontalHeader().setCascadingSectionResizes(True)
        self.quiz_stats_table.horizontalHeader().setDefaultSectionSize(110)
        self.quiz_stats_table.horizontalHeader().setSortIndicatorShown(False)
        self.quiz_stats_table.horizontalHeader().setStretchLastSection(True)
        self.quiz_stats_table.verticalHeader().setVisible(False)
        self.quiz_stats_table.verticalHeader().setDefaultSectionSize(35)
        self.quiz_stats_table.verticalHeader().setMinimumSectionSize(30)
        self.quiz_stats_table.verticalHeader().setSortIndicatorShown(False)
        self.quiz_stats_table.verticalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.quiz_stats_table, 29, 0, 1, 5)
        self.answer_d_button = QtWidgets.QPushButton(self.quiz_right_frame)
        self.answer_d_button.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                           "color: rgb(255, 255, 255);")
        self.answer_d_button.setObjectName("answer_d_button")
        self.gridLayout.addWidget(self.answer_d_button, 26, 3, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 13, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 5, 0, 1, 1)
        self.label_stats = QtWidgets.QLabel(self.quiz_right_frame)
        self.label_stats.setObjectName("label_stats")
        self.gridLayout.addWidget(self.label_stats, 28, 0, 1, 1)
        self.label_b = QtWidgets.QLabel(self.quiz_right_frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_b.setFont(font)
        self.label_b.setObjectName("label_b")
        self.gridLayout.addWidget(self.label_b, 17, 3, 1, 1)
        self.b_text_display = QtWidgets.QTextBrowser(self.quiz_right_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_text_display.sizePolicy().hasHeightForWidth())
        self.b_text_display.setSizePolicy(sizePolicy)
        self.b_text_display.setMinimumSize(QtCore.QSize(220, 0))
        self.b_text_display.setObjectName("b_text_display")
        self.gridLayout.addWidget(self.b_text_display, 18, 3, 1, 2)
        self.label_average_difficulty = QtWidgets.QLabel(self.quiz_right_frame)
        self.label_average_difficulty.setObjectName("label_average_difficulty")
        self.gridLayout.addWidget(self.label_average_difficulty, 3, 3, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem9, 21, 0, 1, 1)
        self.label_tags_question = QtWidgets.QLabel(self.quiz_right_frame)
        self.label_tags_question.setObjectName("label_tags_question")
        self.gridLayout.addWidget(self.label_tags_question, 9, 0, 1, 1)
        self.cancel_quiz_button = QtWidgets.QPushButton(self.quiz_right_frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cancel_quiz_button.setFont(font)
        self.cancel_quiz_button.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.cancel_quiz_button.setObjectName("cancel_quiz_button")
        self.gridLayout.addWidget(self.cancel_quiz_button, 30, 4, 1, 1)
        self.finish_quiz_button = QtWidgets.QPushButton(self.quiz_right_frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.finish_quiz_button.setFont(font)
        self.finish_quiz_button.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.finish_quiz_button.setCheckable(False)
        self.finish_quiz_button.setAutoDefault(False)
        self.finish_quiz_button.setDefault(False)
        self.finish_quiz_button.setFlat(False)
        self.finish_quiz_button.setObjectName("finish_quiz_button")
        self.gridLayout.addWidget(self.finish_quiz_button, 30, 0, 1, 4)
        self.label_tag_1 = QtWidgets.QLabel(self.quiz_right_frame)
        self.label_tag_1.setEnabled(True)
        self.label_tag_1.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                       "color: rgb(255, 255, 255);")
        self.label_tag_1.setObjectName("label_tag_1")
        self.gridLayout.addWidget(self.label_tag_1, 9, 1, 1, 1)
        self.label_tag_2 = QtWidgets.QLabel(self.quiz_right_frame)
        self.label_tag_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                       "color: rgb(255, 255, 255);")
        self.label_tag_2.setObjectName("label_tag_2")
        self.gridLayout.addWidget(self.label_tag_2, 9, 3, 1, 1)
        self.gridLayout_2.addWidget(self.quiz_right_frame, 0, 2, 1, 1)
        self.quiz_left_frame = QtWidgets.QFrame(self.quiz_main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(12)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.quiz_left_frame.sizePolicy().hasHeightForWidth())
        self.quiz_left_frame.setSizePolicy(sizePolicy)
        self.quiz_left_frame.setMinimumSize(QtCore.QSize(180, 0))
        self.quiz_left_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.quiz_left_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.quiz_left_frame.setObjectName("quiz_left_frame")
        self.formLayout = QtWidgets.QFormLayout(self.quiz_left_frame)
        self.formLayout.setObjectName("formLayout")
        self.new_quiz_button = QtWidgets.QPushButton(self.quiz_left_frame)
        self.new_quiz_button.setMinimumSize(QtCore.QSize(45, 50))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.new_quiz_button.setFont(font)
        self.new_quiz_button.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.new_quiz_button.setObjectName("new_quiz_button")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.new_quiz_button)
        self.label_3 = QtWidgets.QLabel(self.quiz_left_frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.restart_quiz_button = QtWidgets.QPushButton(self.quiz_left_frame)
        self.restart_quiz_button.setMinimumSize(QtCore.QSize(0, 50))
        self.restart_quiz_button.setStyleSheet("background-color: rgb(170, 255, 0);")
        self.restart_quiz_button.setObjectName("restart_quiz_button")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.restart_quiz_button)
        self.label_4 = QtWidgets.QLabel(self.quiz_left_frame)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.label_project_nav = QtWidgets.QLabel(self.quiz_left_frame)
        self.label_project_nav.setWordWrap(True)
        self.label_project_nav.setObjectName("label_project_nav")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.label_project_nav)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.LabelRole, spacerItem10)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(6, QtWidgets.QFormLayout.LabelRole, spacerItem11)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.LabelRole, spacerItem12)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(8, QtWidgets.QFormLayout.LabelRole, spacerItem13)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(9, QtWidgets.QFormLayout.LabelRole, spacerItem14)
        self.main_list_widget = QtWidgets.QListWidget(self.quiz_left_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_list_widget.sizePolicy().hasHeightForWidth())
        self.main_list_widget.setSizePolicy(sizePolicy)
        self.main_list_widget.setMinimumSize(QtCore.QSize(81, 0))
        self.main_list_widget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.main_list_widget.setLineWidth(3)
        self.main_list_widget.setObjectName("main_list_widget")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.main_list_widget)
        self.change_quiz_button = QtWidgets.QPushButton(self.quiz_left_frame)
        self.change_quiz_button.setObjectName("change_quiz_button")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.change_quiz_button)
        self.go_to_questionnaire_button = QtWidgets.QPushButton(self.quiz_left_frame)
        self.go_to_questionnaire_button.setObjectName("go_to_questionnaire_button")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.SpanningRole, self.go_to_questionnaire_button)
        self.label_3.raise_()
        self.new_quiz_button.raise_()
        self.restart_quiz_button.raise_()
        self.label_4.raise_()
        self.label_project_nav.raise_()
        self.main_list_widget.raise_()
        self.change_quiz_button.raise_()
        self.go_to_questionnaire_button.raise_()
        self.gridLayout_2.addWidget(self.quiz_left_frame, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.quiz_main_widget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 0, 1, 1, 1)
        QuizMainWindow.setCentralWidget(self.quiz_main_widget)
        self.quiz_menu_bar = QtWidgets.QMenuBar(QuizMainWindow)
        self.quiz_menu_bar.setGeometry(QtCore.QRect(0, 0, 688, 21))
        self.quiz_menu_bar.setObjectName("quiz_menu_bar")
        QuizMainWindow.setMenuBar(self.quiz_menu_bar)
        self.quiz_status_bar = QtWidgets.QStatusBar(QuizMainWindow)
        self.quiz_status_bar.setObjectName("quiz_status_bar")
        QuizMainWindow.setStatusBar(self.quiz_status_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.textify(QuizMainWindow)
        QtCore.QMetaObject.connectSlotsByName(QuizMainWindow)

        # Connections
        self.go_to_questionnaire_button.clicked.connect(self.switch_to_questionnaire)

    def textify(self, QuizMainWindow):
        _translate = QtCore.QCoreApplication.translate
        QuizMainWindow.setWindowTitle(_translate("QuizMainWindow", "Quiz"))
        self.answer_a_button.setText(_translate("QuizMainWindow", "Answer a)"))
        self.label_a.setText(_translate("QuizMainWindow", "a)"))
        self.label_possible_answers.setText(_translate("QuizMainWindow", "Possible Answers"))
        self.label_number_questions.setText(_translate("QuizMainWindow", "# of questions:"))
        self.label_quiz_details.setText(_translate("QuizMainWindow", "Quiz Details:"))
        self.label_d.setText(_translate("QuizMainWindow", "d)"))
        self.Answer_b_button.setText(_translate("QuizMainWindow", "Answer b)"))
        self.answer_c_button.setText(_translate("QuizMainWindow", "Answer c)"))
        self.label_project_title_questionnaire.setText(_translate("QuizMainWindow", "Quiz Title"))
        self.label_question.setText(_translate("QuizMainWindow", "Question:"))
        self.label_c.setText(_translate("QuizMainWindow", "c)"))
        item = self.quiz_stats_table.horizontalHeaderItem(0)
        item.setText(_translate("QuizMainWindow", "Questions"))
        item = self.quiz_stats_table.horizontalHeaderItem(1)
        item.setText(_translate("QuizMainWindow", "Answered"))
        item = self.quiz_stats_table.horizontalHeaderItem(2)
        item.setText(_translate("QuizMainWindow", "Percentage"))
        item = self.quiz_stats_table.horizontalHeaderItem(3)
        item.setText(_translate("QuizMainWindow", "Percentage Correct"))
        self.answer_d_button.setText(_translate("QuizMainWindow", "Answer d)"))
        self.label_stats.setText(_translate("QuizMainWindow", "Stats"))
        self.label_b.setText(_translate("QuizMainWindow", "b)"))
        self.label_average_difficulty.setText(_translate("QuizMainWindow", "Average Difficulty:"))
        self.label_tags_question.setText(_translate("QuizMainWindow", "Tags"))
        self.cancel_quiz_button.setText(_translate("QuizMainWindow", "(X) Cancel"))
        self.finish_quiz_button.setText(_translate("QuizMainWindow", "(✓) Finish Quiz"))
        self.label_tag_1.setText(_translate("QuizMainWindow", "Tag 1"))
        self.label_tag_2.setText(_translate("QuizMainWindow", "Tag 2"))
        self.new_quiz_button.setText(_translate("QuizMainWindow", "(+)"))
        self.label_3.setText(_translate("QuizMainWindow", "New Quiz \n"
                                                          "(This goes first!)"))
        self.restart_quiz_button.setText(_translate("QuizMainWindow", "(<--)"))
        self.label_4.setText(_translate("QuizMainWindow", "Restart current Quiz"))
        self.label_project_nav.setText(_translate("QuizMainWindow", "Click here to navigate through projects:"))
        self.change_quiz_button.setText(_translate("QuizMainWindow", "Change current quiz"))
        self.go_to_questionnaire_button.setText(_translate("QuizMainWindow", "Lets prepare more\n"
                                                                             " questionnaires!"))

    @staticmethod
    def switch_to_questionnaire():
        QuizMainWindow.hide()
        questionnaireMainWindow.show()


class UiQuestionnaireMainWindow(object):
    def __init__(self):
        super().__init__()
        questionnaireMainWindow.setObjectName("QuestionnaireMainWindow")
        questionnaireMainWindow.resize(686, 726)
        questionnaireMainWindow.setGeometry(800, 300, 500, 500)
        self.questionnaire_main_widget = QtWidgets.QWidget(questionnaireMainWindow)
        self.questionnaire_main_widget.setObjectName("questionnaire_main_widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.questionnaire_main_widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.questionnaire_left_frame = QtWidgets.QFrame(self.questionnaire_main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.questionnaire_left_frame.sizePolicy().hasHeightForWidth())
        self.questionnaire_left_frame.setSizePolicy(sizePolicy)
        self.questionnaire_left_frame.setMinimumSize(QtCore.QSize(180, 0))
        self.questionnaire_left_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.questionnaire_left_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.questionnaire_left_frame.setObjectName("questionnaire_left_frame")
        self.formLayout = QtWidgets.QFormLayout(self.questionnaire_left_frame)
        self.formLayout.setObjectName("formLayout")
        self.new_questionnaire_button = QtWidgets.QPushButton(self.questionnaire_left_frame)
        self.new_questionnaire_button.setMinimumSize(QtCore.QSize(45, 50))
        self.new_questionnaire_button.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.new_questionnaire_button.setObjectName("new_questionnaire_button")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.new_questionnaire_button)
        self.label_new_questionnaire = QtWidgets.QLabel(self.questionnaire_left_frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_new_questionnaire.setFont(font)
        self.label_new_questionnaire.setWordWrap(True)
        self.label_new_questionnaire.setObjectName("label_new_questionnaire")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_new_questionnaire)
        self.new_question_button = QtWidgets.QPushButton(self.questionnaire_left_frame)
        self.new_question_button.setMinimumSize(QtCore.QSize(0, 50))
        self.new_question_button.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.new_question_button.setObjectName("new_question_button")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.new_question_button)
        self.label_new_question = QtWidgets.QLabel(self.questionnaire_left_frame)
        self.label_new_question.setWordWrap(True)
        self.label_new_question.setObjectName("label_new_question")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_new_question)
        self.label_project_nav = QtWidgets.QLabel(self.questionnaire_left_frame)
        self.label_project_nav.setWordWrap(True)
        self.label_project_nav.setObjectName("label_project_nav")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.label_project_nav)
        self.main_list_widget = QtWidgets.QListWidget(self.questionnaire_left_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_list_widget.sizePolicy().hasHeightForWidth())
        self.main_list_widget.setSizePolicy(sizePolicy)
        self.main_list_widget.setMinimumSize(QtCore.QSize(81, 0))
        self.main_list_widget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.main_list_widget.setLineWidth(3)
        self.main_list_widget.setObjectName("main_list_widget")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.main_list_widget)
        self.select_current_questionnaire = QtWidgets.QPushButton(self.questionnaire_left_frame)
        self.select_current_questionnaire.setObjectName("change_quiz_button")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.select_current_questionnaire)
        # UI CHANGE ----------------------------------------------------------------------------------------------
        self.modify_questionnaire_title_button = QtWidgets.QPushButton()
        self.modify_questionnaire_title_button.setText("Modify questionnaire Title")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.modify_questionnaire_title_button)
        self.delete_questionnaire_button = QtWidgets.QPushButton()
        self.delete_questionnaire_button.setText("Delete questionnaire")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.delete_questionnaire_button)
        self.modify_question_button = QtWidgets.QPushButton()
        self.modify_question_button.setText("Modify question")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.modify_question_button)
        self.delete_question_button = QtWidgets.QPushButton()
        self.delete_question_button.setText("Delete question")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.delete_question_button)
        # UI CHANGE FINISH ---------------------------------------------------------------------------------------
        self.go_to_quizbutton = QtWidgets.QPushButton(self.questionnaire_left_frame)
        self.go_to_quizbutton.setObjectName("go_to_questionnaire_button")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.SpanningRole, self.go_to_quizbutton)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(9, QtWidgets.QFormLayout.SpanningRole, spacerItem4)
        self.gridLayout_2.addWidget(self.questionnaire_left_frame, 0, 0, 1, 1)
        self.questionnaire_right_frame = QtWidgets.QFrame(self.questionnaire_main_widget)
        self.questionnaire_right_frame.setEnabled(True)
        self.questionnaire_right_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.questionnaire_right_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.questionnaire_right_frame.setObjectName("questionnaire_right_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.questionnaire_right_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.wrong_answer_text_edit_3 = QtWidgets.QTextEdit(self.questionnaire_right_frame)
        self.wrong_answer_text_edit_3.setEnabled(False)
        self.wrong_answer_text_edit_3.setObjectName("alternate_answer_text_edit_3")
        self.gridLayout.addWidget(self.wrong_answer_text_edit_3, 15, 3, 1, 2)
        self.medium_check_box = QtWidgets.QCheckBox(self.questionnaire_right_frame)
        self.medium_check_box.setAutoExclusive(True)
        self.medium_check_box.setObjectName("medium_check_box")
        self.gridLayout.addWidget(self.medium_check_box, 17, 2, 1, 1)
        self.label_number_of_questions = QtWidgets.QLabel(self.questionnaire_right_frame)
        self.label_number_of_questions.setObjectName("label_number_of_questions")
        self.gridLayout.addWidget(self.label_number_of_questions, 3, 0, 1, 1)
        self.remove_tag_button = QtWidgets.QPushButton(self.questionnaire_right_frame)
        self.remove_tag_button.setObjectName("remove_tag_button")
        self.gridLayout.addWidget(self.remove_tag_button, 10, 4, 1, 1)
        self.add_tag_to_question_button = QtWidgets.QPushButton(self.questionnaire_right_frame)
        self.add_tag_to_question_button.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                                      "color: rgb(255, 255, 255);")
        self.add_tag_to_question_button.setObjectName("add_tag_to_question_button")
        self.gridLayout.addWidget(self.add_tag_to_question_button, 9, 4, 1, 1)
        self.label_tags = QtWidgets.QLabel(self.questionnaire_right_frame)
        self.label_tags.setObjectName("label_tags")
        self.gridLayout.addWidget(self.label_tags, 9, 0, 1, 1)
        self.answer_text_edit = QtWidgets.QTextEdit(self.questionnaire_right_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answer_text_edit.sizePolicy().hasHeightForWidth())
        self.answer_text_edit.setSizePolicy(sizePolicy)
        self.answer_text_edit.setMinimumSize(QtCore.QSize(0, 150))
        self.answer_text_edit.setObjectName("answer_text_edit")
        self.gridLayout.addWidget(self.answer_text_edit, 12, 0, 1, 5)
        self.add_question_button = QtWidgets.QPushButton(self.questionnaire_right_frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.add_question_button.setFont(font)
        self.add_question_button.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.add_question_button.setCheckable(False)
        self.add_question_button.setAutoDefault(False)
        self.add_question_button.setDefault(False)
        self.add_question_button.setFlat(False)
        self.add_question_button.setObjectName("add_question_button")
        self.gridLayout.addWidget(self.add_question_button, 18, 0, 1, 4)
        self.add_tag_button = QtWidgets.QPushButton(self.questionnaire_right_frame)
        self.add_tag_button.setObjectName("add_tag_button")
        self.gridLayout.addWidget(self.add_tag_button, 10, 1, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 5, 0, 1, 1)
        self.tag_combo_box = QtWidgets.QComboBox(self.questionnaire_right_frame)
        self.tag_combo_box.setFixedHeight(23)  # UI SIZE CHANGED
        self.tag_combo_box.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: rgb(255, 255, 255);")
        self.tag_combo_box.setObjectName("tag_combo_box")
        self.gridLayout.addWidget(self.tag_combo_box, 9, 1, 1, 3)
        self.easy_check_box = QtWidgets.QCheckBox(self.questionnaire_right_frame)
        self.easy_check_box.setChecked(True)
        self.easy_check_box.setAutoExclusive(True)
        self.easy_check_box.setObjectName("easy_check_box")
        self.gridLayout.addWidget(self.easy_check_box, 17, 0, 1, 1)
        self.label_average_difficulty = QtWidgets.QLabel(self.questionnaire_right_frame)
        self.label_average_difficulty.setObjectName("label_average_difficulty")
        self.gridLayout.addWidget(self.label_average_difficulty, 3, 3, 1, 1)
        self.label_project_title_questionnaire = QtWidgets.QLabel(self.questionnaire_right_frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_project_title_questionnaire.setFont(font)
        self.label_project_title_questionnaire.setObjectName("label_project_title_questionnaire")
        self.gridLayout.addWidget(self.label_project_title_questionnaire, 0, 0, 1, 3)
        self.wrong_answer_text_edit_2 = QtWidgets.QTextEdit(self.questionnaire_right_frame)
        self.wrong_answer_text_edit_2.setEnabled(False)
        self.wrong_answer_text_edit_2.setObjectName("alternate_answer_text_edit_2")
        self.gridLayout.addWidget(self.wrong_answer_text_edit_2, 15, 0, 1, 3)
        self.label_remove_tag = QtWidgets.QLabel(self.questionnaire_right_frame)
        self.label_remove_tag.setObjectName("label_remove_tag")
        self.gridLayout.addWidget(self.label_remove_tag, 10, 3, 1, 1)
        self.possible_wrong_answers_check_box = QtWidgets.QCheckBox(self.questionnaire_right_frame)
        self.possible_wrong_answers_check_box.setMinimumSize(QtCore.QSize(0, 32))
        self.possible_wrong_answers_check_box.setIconSize(QtCore.QSize(16, 32))
        self.possible_wrong_answers_check_box.setObjectName("possible_wrong_answers_check_box")
        self.gridLayout.addWidget(self.possible_wrong_answers_check_box, 14, 0, 1, 3)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 6, 0, 1, 1)
        self.question_line_edit = QtWidgets.QLineEdit(self.questionnaire_right_frame)
        self.question_line_edit.setMinimumSize(QtCore.QSize(0, 40))
        self.question_line_edit.setText("")
        self.question_line_edit.setObjectName("question_line_edit")
        self.gridLayout.addWidget(self.question_line_edit, 8, 0, 1, 5)
        self.label_questionnaire_details = QtWidgets.QLabel(self.questionnaire_right_frame)
        self.label_questionnaire_details.setObjectName("label_questionnaire_details")
        self.gridLayout.addWidget(self.label_questionnaire_details, 2, 0, 1, 5)
        self.label_add_tag = QtWidgets.QLabel(self.questionnaire_right_frame)
        self.label_add_tag.setObjectName("label_add_tag")
        self.gridLayout.addWidget(self.label_add_tag, 10, 0, 1, 1)
        self.cancel_button = QtWidgets.QPushButton(self.questionnaire_right_frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cancel_button.setFont(font)
        self.cancel_button.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.cancel_button.setObjectName("cancel_button")
        self.gridLayout.addWidget(self.cancel_button, 18, 4, 1, 1)
        self.wrong_answer_text_edit_1 = QtWidgets.QTextEdit(self.questionnaire_right_frame)
        self.wrong_answer_text_edit_1.setEnabled(False)
        self.wrong_answer_text_edit_1.setObjectName("alternate_answer_text_edit_1")
        self.gridLayout.addWidget(self.wrong_answer_text_edit_1, 14, 3, 1, 2)
        self.label_answer = QtWidgets.QLabel(self.questionnaire_right_frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_answer.setFont(font)
        self.label_answer.setObjectName("label_answer")
        self.gridLayout.addWidget(self.label_answer, 11, 0, 1, 1)
        self.label_question = QtWidgets.QLabel(self.questionnaire_right_frame)
        self.label_question.setObjectName("label_question")
        self.gridLayout.addWidget(self.label_question, 7, 0, 1, 1)
        self.expert_check_box = QtWidgets.QCheckBox(self.questionnaire_right_frame)
        self.expert_check_box.setAutoExclusive(True)
        self.expert_check_box.setObjectName("expert_check_box")
        self.gridLayout.addWidget(self.expert_check_box, 17, 4, 1, 1)
        self.hard_check_box = QtWidgets.QCheckBox(self.questionnaire_right_frame)
        self.hard_check_box.setAutoExclusive(True)
        self.hard_check_box.setObjectName("hard_check_box")
        self.gridLayout.addWidget(self.hard_check_box, 17, 3, 1, 1)
        self.gridLayout_2.addWidget(self.questionnaire_right_frame, 0, 2, 1, 1)
        self.line = QtWidgets.QFrame(self.questionnaire_main_widget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 0, 1, 1, 1)
        questionnaireMainWindow.setCentralWidget(self.questionnaire_main_widget)
        self.questionnaire_menu_bar = QtWidgets.QMenuBar(questionnaireMainWindow)
        self.questionnaire_menu_bar.setGeometry(QtCore.QRect(0, 0, 686, 21))
        self.questionnaire_menu_bar.setObjectName("questionnaire_menu_bar")
        questionnaireMainWindow.setMenuBar(self.questionnaire_menu_bar)
        self.questionnaire_status_bar = QtWidgets.QStatusBar(questionnaireMainWindow)
        self.questionnaire_status_bar.setObjectName("questionnaire_status_bar")
        questionnaireMainWindow.setStatusBar(self.questionnaire_status_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.textify(questionnaireMainWindow)
        self.possible_wrong_answers_check_box.toggled['bool'].connect(self.wrong_answer_text_edit_1.setEnabled)
        self.possible_wrong_answers_check_box.toggled['bool'].connect(self.wrong_answer_text_edit_2.setEnabled)
        self.possible_wrong_answers_check_box.toggled['bool'].connect(self.wrong_answer_text_edit_3.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(questionnaireMainWindow)

        # Class Variables
        self.window = QtWidgets.QWidget()
        self.window.setGeometry(800, 300, 500, 500)

        # UI Additions
        self.menuOpciones = QtWidgets.QMenu(self.questionnaire_menu_bar)
        self.menuOpciones.setTitle("Opciones")
        self.label_added_tag_one = QtWidgets.QLabel(self.questionnaire_right_frame)
        self.label_added_tag_one.setText("")
        self.gridLayout.addWidget(self.label_added_tag_one, 7, 3, 1, 1)
        self.label_added_tag_two = QtWidgets.QLabel(self.questionnaire_right_frame)
        self.label_added_tag_two.setText("")
        self.gridLayout.addWidget(self.label_added_tag_two, 7, 4, 1, 1)
        self.mod_add_question_button = QtWidgets.QPushButton(self.questionnaire_right_frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.mod_add_question_button.setFont(font)
        self.mod_add_question_button.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.mod_add_question_button.setCheckable(False)
        self.mod_add_question_button.setAutoDefault(False)
        self.mod_add_question_button.setDefault(False)
        self.mod_add_question_button.setFlat(False)
        self.gridLayout.addWidget(self.mod_add_question_button, 18, 0, 1, 4)
        self.mod_add_question_button.setText("(-) Modify Question!")
        self.mod_add_question_button.hide()
        self.questionnaire_left_frame.setFixedWidth(180)
        # Placeholder texts
        self.question_line_edit.setPlaceholderText("Your question goes here:")
        self.answer_text_edit.setPlaceholderText("Your answer goes here:")
        self.wrong_answer_text_edit_1.setPlaceholderText("Your wrong answer goes here: (Trickery)")
        self.wrong_answer_text_edit_2.setPlaceholderText("Your wrong answer goes here: (Banditry)")
        self.wrong_answer_text_edit_3.setPlaceholderText("Your wrong answer goes here: (Deception)")
        # Tooltips
        self.new_questionnaire_button.setToolTip("You can add new Questionnaires here!")
        self.select_current_questionnaire.setToolTip("Select a Questionnaire from above to set it as active")

        # Added tab order
        MainWindow.setTabOrder(self.question_line_edit, self.answer_text_edit)

        # Additional init
        self.path = os.getcwd()
        for file in os.listdir():  # Adds current saved quizzes to main list widget
            if file.startswith("Quiz"):
                self.main_list_widget.addItem(file[5:-5])
        if self.main_list_widget.count() == 0:
            self.questionnaire_right_frame.setEnabled(False)
        else:
            self.set_active_questionnaire(self.main_list_widget.count() - 1)
        if self.label_added_tag_one.text() != "" and self.label_added_tag_two.text() != "":
            self.add_tag_to_question_button.setText("Remove tags >")
        self.difficulty_dict = {1: "Easy", 3: "Medium", 5: "Hard", 7: "Expert"}

        # Connections
        self.go_to_quizbutton.clicked.connect(self.switch_to_quiz)
        self.new_questionnaire_button.clicked.connect(self.new_questionnaire)
        self.modify_questionnaire_title_button.clicked.connect(self.modify_title)
        self.delete_questionnaire_button.clicked.connect(self.delete_questionnaire)
        self.new_question_button.clicked.connect(self.new_question)
        self.add_question_button.clicked.connect(self.new_question)
        self.select_current_questionnaire.clicked.connect(self.select_current)
        self.delete_question_button.clicked.connect(self.delete_question)
        self.add_tag_button.clicked.connect(self.add_tags)
        self.remove_tag_button.clicked.connect(self.remove_tags)
        self.add_tag_to_question_button.clicked.connect(self.add_tag_to_question)
        self.modify_question_button.clicked.connect(self.modify_question)
        self.mod_add_question_button.clicked.connect(self.add_mod_question)

    def textify(self, questionnaireMainWindow):
        _translate = QtCore.QCoreApplication.translate
        questionnaireMainWindow.setWindowTitle(_translate("QuestionnaireMainWindow", "Questionnaire"))
        self.new_questionnaire_button.setText(_translate("QuestionnaireMainWindow", "(+)"))
        self.label_new_questionnaire.setText(_translate("QuestionnaireMainWindow", "New questionnaire \n"
                                                                                   "(This goes first!)"))
        self.new_question_button.setText(_translate("QuestionnaireMainWindow", "(+++)"))
        self.label_new_question.setText(_translate("QuestionnaireMainWindow", "New Question"))
        self.label_project_nav.setText(
            _translate("QuestionnaireMainWindow", "Click here to navigate through projects:"))
        self.select_current_questionnaire.setText(_translate("QuestionnaireMainWindow", "Select current questionnaire"))
        self.go_to_quizbutton.setText(_translate("QuestionnaireMainWindow", "Lets take a\n"
                                                                            " Quiz!"))
        self.medium_check_box.setText(_translate("QuestionnaireMainWindow", "Medium (+3 points)"))
        self.label_number_of_questions.setText(_translate("QuestionnaireMainWindow", "# of questions:"))
        self.remove_tag_button.setText(_translate("QuestionnaireMainWindow", "(-)"))
        self.add_tag_to_question_button.setText(_translate("QuestionnaireMainWindow", "Add tag >"))
        self.label_tags.setText(_translate("QuestionnaireMainWindow", "Tags"))
        self.add_question_button.setText(_translate("QuestionnaireMainWindow", "(✓) Add Question!"))
        self.add_tag_button.setText(_translate("QuestionnaireMainWindow", "(+)"))
        self.easy_check_box.setText(_translate("QuestionnaireMainWindow", "Easy (+1 point)"))
        self.label_average_difficulty.setText(_translate("QuestionnaireMainWindow", "Average Difficulty:"))
        self.label_project_title_questionnaire.setText(_translate("QuestionnaireMainWindow", "Questionnaire Title"))
        self.label_remove_tag.setText(_translate("QuestionnaireMainWindow", "Remove Tag"))
        self.possible_wrong_answers_check_box.setText(_translate("QuestionnaireMainWindow", "Possible Wrong Answers"))
        self.label_questionnaire_details.setText(_translate("QuestionnaireMainWindow", "Questionnaire Details:"))
        self.label_add_tag.setText(_translate("QuestionnaireMainWindow", "Add Tag"))
        self.cancel_button.setText(_translate("QuestionnaireMainWindow", "(X) Cancel"))
        self.label_answer.setText(_translate("QuestionnaireMainWindow", "Answer"))
        self.label_question.setText(_translate("QuestionnaireMainWindow", "Question"))
        self.expert_check_box.setText(_translate("QuestionnaireMainWindow", "Expert (+7 points)"))
        self.hard_check_box.setText(_translate("QuestionnaireMainWindow", "Hard (+5 points)"))

    def set_active_questionnaire(self, index=0):
        wb = openpyxl.load_workbook(f"Quiz_{self.main_list_widget.item(index).text()}.xlsx")
        sheet = wb.active
        question_list = []
        for cell in sheet["A"]:
            if cell.value != "QUESTIONS" and cell.value is not None:
                question_list.append(cell.value)
        self.label_number_of_questions.setText(f"""# of Questions: {len(question_list)}""")  # QUESTIONS
        self.label_question.setText(f"""Question {len(question_list) + 1}:""")
        self.questionnaire_status_bar.showMessage(f"Active questionnaire: "
                                                  f"{self.main_list_widget.item(index).text()}")
        self.label_project_title_questionnaire.setText(self.main_list_widget.item(index).text())
        self.tag_combo_box.clear()
        for cell in sheet["B"]:  # TAGS
            if cell.value != "TAGS" and cell.value is not None:
                self.tag_combo_box.addItem(cell.value)
        current_question = int(self.label_question.text().replace(":", "")[9:])  # QUESTION TAGS
        if sheet["C" + str(current_question + 1)].value is not None:
            tags = sheet["C" + str(current_question + 1)].value.split("//")
            self.label_added_tag_one.setText(tags[0])
            try:
                self.label_added_tag_two.setText(tags[1])
            except IndexError:
                pass
        else:
            self.label_added_tag_one.setText("")
            self.label_added_tag_two.setText("")
        if sheet["H2"].value != "" and sheet["H2"].value is not None:  # DIFFICULTY  # TODO: Handle deleted questions
            diff_average = 0
            count = 0
            for cell in sheet["H"]:
                if cell.value != "DIFFICULTY" and cell.value is not None:
                    diff_average = diff_average + cell.value
                    count += 1
            average = round(diff_average / count, 2)
            self.label_average_difficulty.setText(f"Average Difficulty: {str(average)}")
        else:
            self.label_average_difficulty.setText("Average Difficulty: Pending...")
        wb.save(f"Quiz_{self.main_list_widget.item(index).text()}.xlsx")
        wb.close()

    def new_questionnaire(self):
        quiz_title, ok = QtWidgets.QInputDialog.getText(self.window, "Create a Quiz", "Select a title for your "
                                                                                      "questionnaire: ",
                                                        QtWidgets.QLineEdit.Normal)
        if ok and quiz_title:
            wb = xlsxwriter.Workbook(f"Quiz_{quiz_title.upper()}.xlsx")
            wb.close()
            open_workbook = openpyxl.load_workbook(f"Quiz_{quiz_title.upper()}.xlsx")
            sheet = open_workbook.active
            # Formatting
            sheet["A1"] = "QUESTIONS"
            sheet["B1"] = "TAGS"
            sheet["C1"] = "QUESTION TAGS"
            sheet["D1"] = "ANSWER"
            sheet["E1"] = "WRONG ANSWER 1"
            sheet["F1"] = "WRONG ANSWER 2"
            sheet["G1"] = "WRONG ANSWER 3"
            sheet["H1"] = "DIFFICULTY"
            # Column width
            sheet.column_dimensions["A"].width = 30
            sheet.column_dimensions["B"].width = 24
            sheet.column_dimensions["C"].width = 24
            sheet.column_dimensions["D"].width = 30
            sheet.column_dimensions["E"].width = 30
            sheet.column_dimensions["F"].width = 30
            sheet.column_dimensions["G"].width = 30
            sheet.column_dimensions["H"].width = 15
            # Filter and freeze
            sheet.auto_filter.ref = "A1:H1"
            sheet.freeze_panes = "A2"
            open_workbook.save(f"Quiz_{quiz_title.upper()}.xlsx")
            open_workbook.close()
            questionnaire_ui.__init__()

    def select_current(self):
        if len(self.main_list_widget.selectedItems()) > 0:  # Checks if there is any item selected
            item_list = []
            for i in range(len(self.main_list_widget)):  # Loop to add all listwidget values to a list for further index
                item_list.append(self.main_list_widget.item(i).text())
            self.set_active_questionnaire(item_list.index(self.main_list_widget.selectedItems()[0].text()))
            if self.label_added_tag_one.text() == "" or self.label_added_tag_two.text() == "":
                self.add_tag_to_question_button.setText("Add tag >")
            elif self.label_added_tag_one.text() != "" or self.label_added_tag_two.text() != "":
                self.add_tag_to_question_button.setText("Remove tags >")
        else:
            self.generic_error("No questionnaire selected",
                               "Please select a questionnaire to switch to from the list shown above.")

    def modify_title(self):
        if len(self.main_list_widget.selectedItems()) > 0:
            new_title, ok = QtWidgets.QInputDialog.getText(self.window, "Change questionnaire Title",
                                                           'Select new questionnaire title',
                                                           QtWidgets.QLineEdit.Normal)
            if new_title and ok:
                old_title = f"Quiz_{self.main_list_widget.selectedItems()[0].text()}.xlsx"
                new_title = f"Quiz_{new_title.upper()}.xlsx"
                if old_title.lower() == new_title.lower():
                    self.generic_error("Identical Titles",
                                       "The two selected titles were identical, operation was cancelled.")
                    return None
                wb = openpyxl.load_workbook(old_title)
                wb.save(new_title)
                wb.close()
                os.remove(old_title)
                questionnaire_ui.__init__()
        else:
            self.generic_error("No title selected", "Select a title from the list above to modify its title")

    def delete_questionnaire(self):
        confirmation = QtWidgets.QMessageBox.question(self.window, "Confirmation",
                                                      "Are you sure you want to permanently delete this questionnaire:")
        if confirmation == QMessageBox.Yes:
            try:
                deleted_quiz = f"Quiz_{self.main_list_widget.selectedItems()[0].text()}.xlsx"
                os.remove(deleted_quiz)
                questionnaire_ui.__init__()
            except IndexError:
                self.generic_error("No questionnaire selected", "Please select a questionnaire from the list above to "
                                                                "delete it")
        else:
            self.generic_information("", "Questionnaire was not deleted.")

    def new_question(self):
        if self.main_list_widget.count() == 0:  # Counts the items in ItemListWidget
            ask = QtWidgets.QMessageBox.question(self.window, "No quiz created", "It appears you have not created "
                                                                                 "a quiz yet to assign this question\n"
                                                                                 "\nWould you like to create one now?")
            if ask == QMessageBox.Yes:
                self.new_questionnaire()
        else:
            if self.question_line_edit.text() == "":
                self.generic_error("Empty question", "Please add text to your question.")
            elif self.answer_text_edit.toPlainText() == "":
                self.generic_error("Empty answer", "Please add a correct answer to your question.")
            elif self.possible_wrong_answers_check_box.isChecked():
                if self.wrong_answer_text_edit_1.toPlainText() == "":
                    self.generic_error("Empty answer", "Please add another wrong answer to your question.\n\n"
                                                       "Otherwise, uncheck possible wrong answer mode.")
                elif self.wrong_answer_text_edit_2.toPlainText() == "":
                    self.generic_error("Empty answer", "Please add another wrong answer to your question.\n\n"
                                                       "Otherwise, uncheck possible wrong answer mode.")
                elif self.wrong_answer_text_edit_3.toPlainText() == "":
                    self.generic_error("Empty answer", "Please add another wrong answer to your question.\n\n"
                                                       "Otherwise, uncheck possible wrong answer mode.")
                else:  # If all fields are correctly filled, adds question data to file
                    wb = openpyxl.load_workbook(f"Quiz_{self.label_project_title_questionnaire.text()}.xlsx")
                    sheet = wb.active
                    current_question = int(self.label_question.text().replace(":", "")[9:])
                    sheet["A" + str(current_question + 1)] = self.question_line_edit.text().capitalize()  # QUESTION
                    sheet["D" + str(current_question + 1)] = self.answer_text_edit.toPlainText().capitalize()  # ANSWER
                    if self.possible_wrong_answers_check_box.isChecked():  # POSSIBLE WRONG ANSWERS
                        sheet[
                            "E" + str(current_question + 1)] = self.wrong_answer_text_edit_1.toPlainText().capitalize()
                        sheet[
                            "F" + str(current_question + 1)] = self.wrong_answer_text_edit_2.toPlainText().capitalize()
                        sheet[
                            "G" + str(current_question + 1)] = self.wrong_answer_text_edit_3.toPlainText().capitalize()
                    if self.easy_check_box.isChecked():  # DIFFICULTY
                        difficulty = 1
                        sheet["H" + str(current_question + 1)] = difficulty
                    elif self.medium_check_box.isChecked():
                        difficulty = 3
                        sheet["H" + str(current_question + 1)] = difficulty
                    elif self.hard_check_box.isChecked():
                        difficulty = 5
                        sheet["H" + str(current_question + 1)] = difficulty
                    else:
                        difficulty = 7
                        sheet["H" + str(current_question + 1)] = difficulty

                    wb.save(f"Quiz_{self.label_project_title_questionnaire.text()}.xlsx")
                    wb.close()
                    self.generic_information("Successfully added",
                                             f"Question {current_question} was added correctly.\n\n"
                                             f"Question: {self.question_line_edit.text().capitalize()}\n\n"
                                             f"Answer: {self.answer_text_edit.toPlainText().capitalize()}\n\n"
                                             f"Tags: {self.label_added_tag_one.text()} / {self.label_added_tag_two.text()}"
                                             f"\n\nDifficulty: {self.difficulty_dict.get(difficulty)}")
                    self.question_line_edit.clear()
                    self.answer_text_edit.clear()
                    self.wrong_answer_text_edit_1.clear()
                    self.wrong_answer_text_edit_2.clear()
                    self.wrong_answer_text_edit_3.clear()
                    self.label_added_tag_one.setText("")
                    self.label_added_tag_two.setText("")
                    self.add_tag_to_question_button.setText("Add tag >")
            else:
                wb = openpyxl.load_workbook(f"Quiz_{self.label_project_title_questionnaire.text()}.xlsx")
                sheet = wb.active
                current_question = int(self.label_question.text().replace(":", "")[9:])
                sheet["A" + str(current_question + 1)] = self.question_line_edit.text().capitalize()  # QUESTION
                sheet["D" + str(current_question + 1)] = self.answer_text_edit.toPlainText().capitalize()  # ANSWER

                if self.easy_check_box.isChecked():  # DIFFICULTY
                    difficulty = 1
                    sheet["H" + str(current_question + 1)] = difficulty
                elif self.medium_check_box.isChecked():
                    difficulty = 3
                    sheet["H" + str(current_question + 1)] = difficulty
                elif self.hard_check_box.isChecked():
                    difficulty = 5
                    sheet["H" + str(current_question + 1)] = difficulty
                else:
                    difficulty = 7
                    sheet["H" + str(current_question + 1)] = difficulty

                wb.save(f"Quiz_{self.label_project_title_questionnaire.text()}.xlsx")
                wb.close()
                self.generic_information("Successfully added",
                                         f"Question {current_question} was added correctly.\n\n"
                                         f"Question: {self.question_line_edit.text().capitalize()}\n\n"
                                         f"Answer: {self.answer_text_edit.toPlainText().capitalize()}\n\n"
                                         f"Tags: {self.label_added_tag_one.text()} / {self.label_added_tag_two.text()}"
                                         f"\n\nDifficulty: {self.difficulty_dict.get(difficulty)}")
                self.question_line_edit.clear()
                self.answer_text_edit.clear()
                self.wrong_answer_text_edit_1.clear()
                self.wrong_answer_text_edit_2.clear()
                self.wrong_answer_text_edit_3.clear()
                self.label_added_tag_one.setText("")
                self.label_added_tag_two.setText("")
                self.add_tag_to_question_button.setText("Add tag >")

    def modify_question(self):
        # DONE: Add modify functionality
        if self.label_project_title_questionnaire != "Questionnaire Title":
            wb = openpyxl.load_workbook(f"Quiz_{self.label_project_title_questionnaire.text()}.xlsx")
            sheet = wb.active
            question_list = []
            for cell in sheet["A"]:
                if cell.value != "QUESTIONS" and cell.value is not None:
                    question_list.append(cell.value)
            question, ok = QtWidgets.QInputDialog.getItem(self.window, "Modify Question",
                                                          "Select a question to modify:",
                                                          question_list, 0, False)
            if question and ok:
                # Depending on selection, bring the question parameters into the UI for modification
                # Set Question
                self.question_line_edit.setText(sheet["A" + str(question_list.index(question) + 2)].value)
                # Set Answer
                answer = sheet["D" + str(question_list.index(question) + 2)].value
                self.answer_text_edit.setText(answer)
                # DONE: Don't add question, but modify the one selected
                self.add_question_button.hide()
                self.mod_add_question_button.show()
                self.label_question.setText(f"Modifying Question {str(question_list.index(question) + 1)}:")

            wb.save(f"Quiz_{self.label_project_title_questionnaire.text()}.xlsx")
            wb.close()

    def add_mod_question(self):
        if self.question_line_edit.text() == "":
            self.generic_error("Empty question", "Please add text to your question.")
        elif self.answer_text_edit.toPlainText() == "":
            self.generic_error("Empty answer", "Please add a correct answer to your question.")
        elif self.possible_wrong_answers_check_box.isChecked():
            if self.wrong_answer_text_edit_1.toPlainText() == "":
                self.generic_error("Empty answer", "Please add another wrong answer to your question.\n\n"
                                                   "Otherwise, uncheck possible wrong answer mode.")
            elif self.wrong_answer_text_edit_2.toPlainText() == "":
                self.generic_error("Empty answer", "Please add another wrong answer to your question.\n\n"
                                                   "Otherwise, uncheck possible wrong answer mode.")
            elif self.wrong_answer_text_edit_3.toPlainText() == "":
                self.generic_error("Empty answer", "Please add another wrong answer to your question.\n\n"
                                                   "Otherwise, uncheck possible wrong answer mode.")
            else:  # If all fields are correctly filled, adds question data to file
                wb = openpyxl.load_workbook(f"Quiz_{self.label_project_title_questionnaire.text()}.xlsx")
                sheet = wb.active
                current_question = int(self.label_question.text().replace(":", "")[9:])
                sheet["A" + str(current_question + 1)] = self.question_line_edit.text().capitalize()  # QUESTION
                sheet["D" + str(current_question + 1)] = self.answer_text_edit.toPlainText().capitalize()  # ANSWER
                if self.possible_wrong_answers_check_box.isChecked():  # POSSIBLE WRONG ANSWERS
                    sheet[
                        "E" + str(current_question + 1)] = self.wrong_answer_text_edit_1.toPlainText().capitalize()
                    sheet[
                        "F" + str(current_question + 1)] = self.wrong_answer_text_edit_2.toPlainText().capitalize()
                    sheet[
                        "G" + str(current_question + 1)] = self.wrong_answer_text_edit_3.toPlainText().capitalize()
                if self.easy_check_box.isChecked():  # DIFFICULTY
                    difficulty = 1
                    sheet["H" + str(current_question + 1)] = difficulty
                elif self.medium_check_box.isChecked():
                    difficulty = 3
                    sheet["H" + str(current_question + 1)] = difficulty
                elif self.hard_check_box.isChecked():
                    difficulty = 5
                    sheet["H" + str(current_question + 1)] = difficulty
                else:
                    difficulty = 7
                    sheet["H" + str(current_question + 1)] = difficulty

                wb.save(f"Quiz_{self.label_project_title_questionnaire.text()}.xlsx")
                wb.close()
                self.generic_information("Successfully added",
                                         f"Question {current_question} was added correctly.\n\n"
                                         f"Question: {self.question_line_edit.text().capitalize()}\n\n"
                                         f"Answer: {self.answer_text_edit.toPlainText().capitalize()}\n\n"
                                         f"Tags: {self.label_added_tag_one.text()} / {self.label_added_tag_two.text()}"
                                         f"\n\nDifficulty: {self.difficulty_dict.get(difficulty)}")
                self.question_line_edit.clear()
                self.answer_text_edit.clear()
                self.wrong_answer_text_edit_1.clear()
                self.wrong_answer_text_edit_2.clear()
                self.wrong_answer_text_edit_3.clear()
                self.label_added_tag_one.setText("")
                self.label_added_tag_two.setText("")
                self.add_tag_to_question_button.setText("Add tag >")
        else:
            wb = openpyxl.load_workbook(f"Quiz_{self.label_project_title_questionnaire.text()}.xlsx")
            sheet = wb.active
            current_question = int(self.label_question.text().replace(":", "")[19:])
            sheet["A" + str(current_question + 1)] = self.question_line_edit.text().capitalize()  # QUESTION
            sheet["D" + str(current_question + 1)] = self.answer_text_edit.toPlainText().capitalize()  # ANSWER

            if self.easy_check_box.isChecked():  # DIFFICULTY
                difficulty = 1
                sheet["H" + str(current_question + 1)] = difficulty
            elif self.medium_check_box.isChecked():
                difficulty = 3
                sheet["H" + str(current_question + 1)] = difficulty
            elif self.hard_check_box.isChecked():
                difficulty = 5
                sheet["H" + str(current_question + 1)] = difficulty
            else:
                difficulty = 7
                sheet["H" + str(current_question + 1)] = difficulty

            wb.save(f"Quiz_{self.label_project_title_questionnaire.text()}.xlsx")
            wb.close()
            self.generic_information("Successfully added",
                                     f"Question {current_question} was added correctly.\n\n"
                                     f"Question: {self.question_line_edit.text().capitalize()}\n\n"
                                     f"Answer: {self.answer_text_edit.toPlainText().capitalize()}\n\n"
                                     f"Tags: {self.label_added_tag_one.text()} / {self.label_added_tag_two.text()}"
                                     f"\n\nDifficulty: {self.difficulty_dict.get(difficulty)}")
            self.question_line_edit.clear()
            self.answer_text_edit.clear()
            self.wrong_answer_text_edit_1.clear()
            self.wrong_answer_text_edit_2.clear()
            self.wrong_answer_text_edit_3.clear()
            self.label_added_tag_one.setText("")
            self.label_added_tag_two.setText("")
            self.add_tag_to_question_button.setText("Add tag >")

            # Great way to access current questionnaire, could be used in a lot more places
            items = []
            for i in range(self.main_list_widget.count()):
                items.append(self.main_list_widget.item(i).text())

            current_questionnaire = items.index(self.label_project_title_questionnaire.text())
            self.set_active_questionnaire(current_questionnaire)
            self.mod_add_question_button.hide()
            self.add_question_button.show()

    def delete_question(self):
        # Check if there is no active questionnaire
        if not self.main_list_widget.selectedItems():
            self.generic_error("No quiz selected",
                               "Please select a quiz which contains the question you want to delete")
        # If there is an active questionnaire, show current questions, then delete selected question
        else:
            if self.label_project_title_questionnaire != "Questionnaire Title":
                wb = openpyxl.load_workbook(f"Quiz_{self.label_project_title_questionnaire.text()}.xlsx")
                sheet = wb.active
                current_question = int(self.label_question.text().replace(":", "")[9:])
                question_list = []
                for cell in sheet["A"]:  # Adds all question values to a list
                    if cell.value != "QUESTIONS" and cell.value is not None:
                        question_list.append(cell.value)
                choice, ok = QtWidgets.QInputDialog.getItem(self.window,
                                                            "Delete Question",
                                                            "Select a question from the list to delete",
                                                            question_list, 0, False)
                if choice and ok:
                    print(sheet["A" + str(question_list.index(choice) + 2)].value)  # It adds 2 to compensate
                wb.save(f"Quiz_{self.label_project_title_questionnaire.text()}.xlsx")
                wb.close()

    def add_tags(self):
        tag, ok = QtWidgets.QInputDialog.getText(self.window,
                                                 "Add tag", "Enter tag name", QtWidgets.QLineEdit.Normal)
        if tag and ok:
            wb = openpyxl.load_workbook(f"Quiz_{self.label_project_title_questionnaire.text()}.xlsx")
            sheet = wb.active
            sheet["B" + str(sheet.max_row + 1)] = tag.upper()  # High sus on this, might break tags in future
            self.tag_combo_box.addItem(tag.upper())
            wb.save(f"Quiz_{self.label_project_title_questionnaire.text()}.xlsx")
            wb.close()

    def remove_tags(self):
        wb = openpyxl.load_workbook(f"Quiz_{self.label_project_title_questionnaire.text()}.xlsx")
        sheet = wb.active
        tag_list = []
        for cell in sheet["B"]:
            if cell.value != "TAGS" and cell.value is not None:
                tag_list.append(cell.value)
        tag, ok = QtWidgets.QInputDialog.getItem(self.window, "Delete a tag",
                                                 "Please select a tag from the dropdown list to delete it.",
                                                 tag_list, 0, False)
        if tag and ok:
            index = tag_list.index(tag)
            for cell in sheet["B"]:
                if cell.value == tag:
                    sheet[cell.coordinate] = ""
                    self.tag_combo_box.removeItem(index)
        wb.save(f"Quiz_{self.label_project_title_questionnaire.text()}.xlsx")
        wb.close()

    def add_tag_to_question(self):
        wb = openpyxl.load_workbook(f"Quiz_{self.label_project_title_questionnaire.text()}.xlsx")
        sheet = wb.active
        current_tag_one = self.label_added_tag_one.text()
        current_tag_two = self.label_added_tag_two.text()
        # Very delicate, if program breaks, high sus
        current_question = int(self.label_question.text().replace(":", "")[9:])
        if current_tag_one != "" and current_tag_two != "":  # Reverse functionality, to remove tags
            self.label_added_tag_one.setText("")
            self.label_added_tag_two.setText("")
            self.add_tag_to_question_button.setText("Add tag >")
            sheet["C" + str(current_question + 1)].value = None
            wb.save(f"Quiz_{self.label_project_title_questionnaire.text()}.xlsx")
            wb.close()
            return None
        if self.label_added_tag_one.text() == "":  # Checks if no tags have been added, then adds first one
            self.label_added_tag_one.setText(self.tag_combo_box.currentText().upper())
            self.label_added_tag_one.show()
            sheet["C" + str(current_question + 1)] = self.tag_combo_box.currentText().upper()
        elif self.tag_combo_box.currentText().upper() == current_tag_one \
                or self.tag_combo_box.currentText().upper() == current_tag_two:  # Checks for duplicate tags
            self.generic_error("Repeated Tag", "You can't add the same tag twice to the same question.")
        elif self.label_added_tag_one.text() != "" and self.label_added_tag_two.text() == "":  # Checks for second tag
            self.label_added_tag_two.setText(self.tag_combo_box.currentText().upper())
            self.label_added_tag_two.show()
            if sheet["C" + str(current_question + 1)].value is not None:
                db_tag_one = sheet["C" + str(current_question + 1)].value
                sheet["C" + str(current_question + 1)] = db_tag_one + "//" + self.tag_combo_box.currentText().upper()
            self.add_tag_to_question_button.setText("Remove tags >")
        wb.save(f"Quiz_{self.label_project_title_questionnaire.text()}.xlsx")
        wb.close()

    @staticmethod
    def generic_information(title="Information", text="Details", icon=QMessageBox.Information):
        parent = QtWidgets.QMessageBox()
        parent.setGeometry(800, 300, 500, 500)
        parent.setWindowTitle(title)
        parent.setText(text)
        parent.setIcon(icon)
        parent.exec_()

    @staticmethod
    def generic_error(title="Error", text="Error Details", icon=QMessageBox.Warning):
        parent = QtWidgets.QMessageBox()
        parent.setGeometry(800, 300, 500, 500)
        parent.setWindowTitle(title)
        parent.setText(text)
        parent.setIcon(icon)
        parent.exec_()

    @staticmethod
    def switch_to_quiz():
        questionnaireMainWindow.close()
        QuizMainWindow.show()


class QuizzerMainWindow(object):
    def __init__(self):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(483, 492)
        MainWindow.setGeometry(800, 300, 500, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.home_frame = QtWidgets.QFrame(self.centralwidget)
        self.home_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.home_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.home_frame.setObjectName("home_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.home_frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pix_label_questionnaire = clickable_label.QClickableLabel(self.home_frame)
        self.pix_label_questionnaire.setMinimumSize(QtCore.QSize(215, 215))
        self.pix_label_questionnaire.setAutoFillBackground(False)
        self.pix_label_questionnaire.setFrameShape(QtWidgets.QFrame.Panel)
        self.pix_label_questionnaire.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pix_label_questionnaire.setLineWidth(5)
        self.pix_label_questionnaire.setMidLineWidth(0)
        self.pix_label_questionnaire.setText("")
        self.pix_label_questionnaire.setPixmap(QtGui.QPixmap("questionnaire.gif"))
        self.pix_label_questionnaire.setAlignment(QtCore.Qt.AlignCenter)
        self.pix_label_questionnaire.setObjectName("pix_label_questionnaire")
        self.gridLayout_2.addWidget(self.pix_label_questionnaire, 1, 0, 1, 1)
        self.label_questionnaire = QtWidgets.QLabel(self.home_frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_questionnaire.setFont(font)
        self.label_questionnaire.setAlignment(QtCore.Qt.AlignCenter)
        self.label_questionnaire.setObjectName("label_questionnaire")
        self.gridLayout_2.addWidget(self.label_questionnaire, 2, 0, 1, 1)
        self.label_quiz = QtWidgets.QLabel(self.home_frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_quiz.setFont(font)
        self.label_quiz.setAlignment(QtCore.Qt.AlignCenter)
        self.label_quiz.setObjectName("label_quiz")
        self.gridLayout_2.addWidget(self.label_quiz, 2, 2, 1, 1)
        self.pix_label_quiz = clickable_label.QClickableLabel(self.home_frame)
        self.pix_label_quiz.setMinimumSize(QtCore.QSize(215, 215))
        self.pix_label_quiz.setFrameShape(QtWidgets.QFrame.Panel)
        self.pix_label_quiz.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pix_label_quiz.setLineWidth(5)
        self.pix_label_quiz.setText("")
        self.pix_label_quiz.setPixmap(QtGui.QPixmap("quiz-icon.gif"))
        self.pix_label_quiz.setAlignment(QtCore.Qt.AlignCenter)
        self.pix_label_quiz.setObjectName("pix_label_quiz")
        self.gridLayout_2.addWidget(self.pix_label_quiz, 1, 2, 1, 1)
        self.label_home_title = QtWidgets.QLabel(self.home_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_home_title.sizePolicy().hasHeightForWidth())
        self.label_home_title.setSizePolicy(sizePolicy)
        self.label_home_title.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_home_title.setFont(font)
        self.label_home_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_home_title.setObjectName("label_home_title")
        self.gridLayout_2.addWidget(self.label_home_title, 0, 0, 1, 3)
        self.label_questionnaire_description = QtWidgets.QLabel(self.home_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_questionnaire_description.sizePolicy().hasHeightForWidth())
        self.label_questionnaire_description.setSizePolicy(sizePolicy)
        self.label_questionnaire_description.setMinimumSize(QtCore.QSize(0, 20))
        self.label_questionnaire_description.setWordWrap(True)
        self.label_questionnaire_description.setObjectName("label_questionnaire_description")
        self.gridLayout_2.addWidget(self.label_questionnaire_description, 3, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.home_frame)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 1, 3, 1)
        self.label_quizzes_description = QtWidgets.QLabel(self.home_frame)
        self.label_quizzes_description.setObjectName("label_quizzes_description")
        self.gridLayout_2.addWidget(self.label_quizzes_description, 3, 2, 1, 1)
        self.gridLayout.addWidget(self.home_frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 483, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.textify(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connections
        self.pix_label_questionnaire.clicked.connect(self.show_questionnaire)
        self.pix_label_quiz.clicked.connect(self.show_quiz)
        self.pix_label_questionnaire.clicked.connect(self.show_questionnaire)

    def textify(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quizzer App"))
        self.label_questionnaire.setText(_translate("MainWindow", "Questionnaires"))
        self.label_quiz.setText(_translate("MainWindow", "Quizzes"))
        self.label_home_title.setText(_translate("MainWindow", "Quizzes App"))
        self.label_questionnaire_description.setText(_translate("MainWindow", "Create your own questionnaires and "
                                                                              "prepare them to transform into "
                                                                              "quizzes!"))
        self.label_quizzes_description.setText(_translate("MainWindow", "Test your own quizzes!"))

    def show_quiz(self):
        MainWindow.close()
        QuizMainWindow.show()

    def show_questionnaire(self):
        MainWindow.close()
        questionnaireMainWindow.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    quizzer_ui = QuizzerMainWindow()
    quizzer_ui.__init__()
    MainWindow.show()
    QuizMainWindow = QtWidgets.QMainWindow()
    quiz_ui = UiQuizMainWindow()
    quiz_ui.__init__()
    questionnaireMainWindow = QtWidgets.QMainWindow()
    questionnaire_ui = UiQuestionnaireMainWindow()
    questionnaire_ui.__init__()
    sys.exit(app.exec_())
