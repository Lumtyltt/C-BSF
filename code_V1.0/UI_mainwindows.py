# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 22:26:48 2024

@author: 花花
"""
import os
import time
import sys
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk,ImageDraw
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QDialog,QFileDialog, QGridLayout, QLineEdit, QHBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import matplotlib.pyplot as plt
import numpy as np


def main_program():
    # 模拟一些主程序逻辑

        
    def browse_file(line_edit):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName()
        line_edit.setText(file_path)

    def browse_output_folder(line_edit):
        folder_dialog = QFileDialog()
        folder_path = folder_dialog.getExistingDirectory()
        line_edit.setText(folder_path)

    class ResultWindow(QWidget):
        def __init__(self, image_path):
            super().__init__()

            self.init_ui(image_path)

        def init_ui(self, image_path):
            # Set the window title
            self.setWindowTitle('Result Window')

            # Create QLabel to display the image
            result_label = QLabel(self)
            pixmap = QPixmap(image_path)
            result_label.setPixmap(pixmap)

            # Create layout
            vbox = QVBoxLayout()
            vbox.addWidget(result_label, alignment=Qt.AlignCenter)

            # Set the window's layout
            self.setLayout(vbox)

            # Set the window size
            self.setGeometry(300, 300, pixmap.width(), pixmap.height())
            
            
    class ResultPopup(QDialog):
        def __init__(self, result_text):
            super().__init__()

            self.init_ui(result_text)

        def init_ui(self, result_text):
            self.setWindowTitle('Computational Results')

            result_label = QLabel(result_text, self)

            vbox = QVBoxLayout()
            vbox.addWidget(result_label)

            self.setLayout(vbox)        

    class MyWindow(QWidget):
        def __init__(self):
            super().__init__()

            self.init_ui()

        def init_ui(self):
            # Set the window title
            self.setWindowTitle('C-BSF V1.0')

            # Create a QLabel to hold the background image
            background_label = QLabel(self)
            pixmap = QPixmap("a.png")  # Set the background image path
            background_label.setPixmap(pixmap)
            background_label.setGeometry(0, 0, pixmap.width(), pixmap.height())

            # Create widgets
            title_label = QLabel('Brain Structure and Function Coupling \n Analysis and Visualization Platform', self)
            title_label.setStyleSheet("font-size: 32px; font-weight: bold; color: #333;")
            title_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)  # Align the title to the top-center

            btn_run_program = QPushButton('Run', self)
            btn_run_program.clicked.connect(lambda: run_program(line_edit1, line_edit2, line_edit3, line_edit4))
            btn_run_program.setStyleSheet("font-size: 14px;")
            btn_run_program.setMaximumWidth(150)  # Set maximum width for the button
            
            font = QFont()
            font.setPointSize(12)

            line_edit1 = QLineEdit(self)
            line_edit1_label = QLabel('Structural Network:', self)
            line_edit1_label.setFont(font)
            line_edit1.setPlaceholderText('Select File 1')
            line_edit1.setStyleSheet("font-size: 12px; padding: 5px;")
            line_edit1.setMaximumWidth(280)
            
        
            line_edit2 = QLineEdit(self)
            line_edit2_label = QLabel('Functional Network:', self)
            line_edit2_label.setFont(font)
            line_edit2.setPlaceholderText('Select File 2')
            line_edit2.setStyleSheet("font-size: 12px; padding: 5px;")
            line_edit2.setMaximumWidth(280)
            
            line_edit4 = QLineEdit(self)
            line_edit4_label = QLabel('Subject_ID:', self)
            line_edit4_label.setFont(font)
            line_edit4.setPlaceholderText('Subject_ID')
            line_edit4.setStyleSheet("font-size: 12px; padding: 5px;")
            line_edit4.setMaximumWidth(269)        
            
            
            text_in_between_label = QLabel('', self)
            text_in_between_label.setStyleSheet("font-size: 12px; padding: 5px;")

            
            line_edit3 = QLineEdit(self)
            line_edit3_label = QLabel('Output File:', self)
            line_edit3_label.setFont(font)
            line_edit3.setPlaceholderText('Select Output Folder')
            line_edit3.setStyleSheet("font-size: 12px; padding: 5px;")
            line_edit3.setMaximumWidth(280)

            btn_browse1 = QPushButton('Browse', self)
            btn_browse1.clicked.connect(lambda: browse_output_folder(line_edit1))
            btn_browse1.setStyleSheet("font-size: 12px;")
            btn_browse1.setMaximumWidth(80)

            btn_browse2 = QPushButton('Browse', self)
            btn_browse2.clicked.connect(lambda: browse_output_folder(line_edit2))
            btn_browse2.setStyleSheet("font-size: 12px;")
            btn_browse2.setMaximumWidth(80)
            
            btn_browse4 = QPushButton('Browse', self)
            btn_browse4.clicked.connect(lambda: browse_file(line_edit4))
            btn_browse4.setStyleSheet("font-size: 12px;")
            btn_browse4.setMaximumWidth(80)

            btn_browse_output = QPushButton('Browse', self)
            btn_browse_output.clicked.connect(lambda: browse_output_folder(line_edit3))
            btn_browse_output.setStyleSheet("font-size: 12px;")
            btn_browse_output.setMaximumWidth(80)
            # Create layout
            
            vbox = QVBoxLayout()
            vbox.addWidget(title_label)  # Add the title without the stretchable space
            #vbox.addStretch()
            vbox.addSpacing(100)
                  
            hbox1 = QHBoxLayout()
            hbox1.addStretch()
            hbox1.addWidget(line_edit1_label)
            hbox1.addWidget(line_edit1)
            hbox1.addWidget(btn_browse1,alignment=Qt.AlignRight)
            vbox.addLayout(hbox1)
            
            hbox2 = QHBoxLayout()
            hbox2.addStretch()
            hbox2.addWidget(line_edit2_label)
            hbox2.addWidget(line_edit2)
            hbox2.addWidget(btn_browse2,alignment=Qt.AlignRight)
            vbox.addLayout(hbox2)
            
            hbox4 = QHBoxLayout()
            hbox4.addStretch()
            hbox4.addWidget(line_edit4_label)
            hbox4.addWidget(line_edit4)
            hbox4.addWidget(btn_browse4,alignment=Qt.AlignRight)
            vbox.addLayout(hbox4)       
            
                 
            hbox3 = QHBoxLayout()
            vbox.addSpacing(150) 
            hbox3.addStretch()
            hbox3.addWidget(line_edit3_label)
            hbox3.addWidget(line_edit3)
            hbox3.addWidget(btn_browse_output,alignment=Qt.AlignRight)
            vbox.addLayout(hbox3)   
            
            vbox.addWidget(text_in_between_label, alignment=Qt.AlignCenter)


            vbox.addWidget(btn_run_program, alignment=Qt.AlignCenter)  # Center the button

            # Set the window's layout to the background label
            self.setLayout(vbox)
            # Set the window size and show it
            self.setGeometry(600, 600, 800, 550)
            self.show()

    def run_program(line_edit1, line_edit2, line_edit3, line_edit4):
        Func_path = line_edit2.text().replace('/', '\\')
        Dti_FA_path =line_edit1.text().replace('/', '\\')
        Subject_id = open(line_edit4.text().replace('/', '\\'))

        Outpath_Node = line_edit3.text().replace('/', '\\')+'\\Node_topological_overlap_coefficient'
        Outpath_Network =  line_edit3.text().replace('/', '\\')+'\\Network_topological_overlap_coefficient'

        lines = Subject_id.readlines()
        #Func_files = os.listdir(Func_path)
        #Dti_FA_files = os.listdir(Dti_FA_path)

        size = np.loadtxt(os.path.join(Func_path,lines[1].rstrip()))
        Network_topological_overlap_coefficient = [] 
        ALLsub_topological_overlap_coefficient = [] 
        for data_num in range(len(lines)):
            path_func = os.path.join(Func_path,lines[data_num].rstrip())
            path_dti = os.path.join(Dti_FA_path,lines[data_num].rstrip())
            Func_network = np.loadtxt(path_func)
            Dti_network = np.loadtxt(path_dti)
            Func_network[Func_network>0] = 1
            Dti_network[Dti_network>0] = 1
        	#将相关系数矩阵通过阈值处理形成脑网络，此时的网络为加权网络 
            Node_topological_overlap_coefficient = []
            for i in range(size.shape[0]):
                    #xs=0 #两个网络之间的拓扑重叠系数
                    if np.sum(Func_network[i,:]==0.0)!= size.shape[1] and np.sum(Dti_network[i,:]==0.0)!= size.shape[1]:
                        #print np.sum(g0[i1,:]!=0.0),np.sum(g1[i1,:]!=0.0),i1
                        fenmu=np.sqrt(np.sum(Func_network[i,:]!=0.0)*np.sum(Dti_network[i,:]!=0.0))
                        #print np.sum(g0[i1,:]!=0.0),np.sum(g1[i1,:]!=0.0),fenzi
                    else:
                        fenmu = 1000000000000  
                        
                    fenzi_array = []
                    for j in range(size.shape[1]):
                        if Func_network[i,j] == 1.0 and Dti_network[i,j] == 1.0:
                            fz = Func_network[i,j]
                            fenzi_array.append(fz)
                    fenzi = np.sum(fenzi_array)
                    Node_topological_overlap_coefficient_= fenzi/fenmu
                    Node_topological_overlap_coefficient.append(Node_topological_overlap_coefficient_)
                        
            np.savetxt(os.path.join(Outpath_Node,lines[data_num].rstrip()),Node_topological_overlap_coefficient) 
            print(str(lines[data_num].rstrip())+'_Node_Finish')
            Network_topological_overlap_coefficient_ = np.sum(Node_topological_overlap_coefficient)#/size.shape[0]
            Network_topological_overlap_coefficient.append(Network_topological_overlap_coefficient_/246)
            ALLsub_topological_overlap_coefficient.append(Node_topological_overlap_coefficient)
        np.savetxt(os.path.join(Outpath_Network,'All_SUB_Node_topological_overlap_coefficient.txt'),ALLsub_topological_overlap_coefficient) 
        np.savetxt(os.path.join(Outpath_Network,'AVG_All_BRAIN_Network_topological_overlap_coefficient.txt'),Network_topological_overlap_coefficient)
        # 创建一个矩阵（这里使用NumPy创建一个2x3的矩阵）
        
        path_matrix = Outpath_Network+'\\All_SUB_Node_topological_overlap_coefficient.txt'
        #matrix_data = np.loadtxt('r'+Outpath_Network+'All_SUB_Node_topological_overlap_coefficient.txt')
        # 绘制矩阵图
        plt.imshow(np.loadtxt(path_matrix.replace('/', '\\')), cmap='viridis', interpolation='nearest')
        # 添加颜色条
        plt.colorbar()
        # 显示图形
        plt.show()
        
            
        print('All_Finish')       

        with open(line_edit4.text().replace('/', '\\')) as subject_id_file:
                # Read lines from the file
            lines = subject_id_file.readlines()
            #print(lines)
            # Simulating a result string (replace this with your actual result)
            result_text = "All samples were calculated successfully!"

            # Display the result in a popup window
            result_popup = ResultPopup(result_text)
            result_popup.exec_() 
        
        # Example: You can print the file paths or use them in your program

        # Assuming result_image_path is the path to the resulting image
        result_image_path = "result_image.jpg"
        
        # Display the result image in a new window
        result_window = ResultWindow(result_image_path)
        result_window.show()
            
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = MyWindow()
        sys.exit(app.exec_())
    
    print("Main program is running!")
    
def update_progress(progress_var):
    for i in range(101):
        time.sleep(0.04)  # 模拟耗时操作，每个进度间隔30毫秒
        progress_var.set(i)
        start_window.update_idletasks()
    # 销毁启动界面窗口
    start_window.destroy()    
    # 调用主程序
    main_program()    
#ef start_program():

    

# 创建启动界面窗口
start_window = tk.Tk()
start_window.title("Splash Screen")

# 加载背景图片
bg_image = Image.open("a.png")  # 用你的图片路径替换这里
bg_photo = ImageTk.PhotoImage(bg_image)

# 创建标签以显示背景图片
bg_label = ttk.Label(start_window, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# 设置启动窗口的大小和位置
start_window.geometry("800x550")  # 根据你的需求调整窗口大小
start_window.resizable(False, False)


# 创建进度条
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(start_window, variable=progress_var, length=300, mode="determinate")
progress_bar.place(relx=0.5, rely=0.5, anchor="center")



# 创建样式对象
style = ttk.Style()

# 设置按钮样式，包括字体大小
style.configure("TButton", font=("Helvetica", 16))

# 添加启动按钮，放在界面下方居中
start_button = ttk.Button(start_window, text="Click to start", command=lambda: update_progress(progress_var), style="TButton")
start_button.place(relx=0.5, rely=0.9, anchor="center")
# 启动Tkinter主循环
start_window.mainloop()
