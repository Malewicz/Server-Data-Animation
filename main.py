import os
import sys
import time
import threading
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#from matplotlib import style
import numpy as np
from flask import Flask, render_template, url_for, flash, redirect, request, abort
app = Flask(__name__)

@app.route('/')
@app.route('/home', methods=['GET','POST'])
def glob():
    return render_template('global.html')

def button():
    return render_template('toggle_button.html')

def param():
    return render_template('parameter.html')

@app.route('/fig')
def animate():
    class animationthingy():

        def __init__(self):
            #style.use('fivethirtyeight')
            self.mytime = np.zeros(100, dtype = float)
            self.value = np.zeros(100, dtype = float)
            self.fig, self.ax1 = plt.subplots(1,1)


            print ("Declared arrays")

            self.mytime_data = 1
            self.value_data = 1

            print ("Starting animation")
            self.ani = animation.FuncAnimation(self.fig, self.animate,interval=1000)
            print ("Showing plot")
            plt.show()
            print ("Ending init")


        # need to make connection to server here

        def shift(self,l, n):
            return np.append(l[n:],l[:n])

        def update_list(self,targetlist, new_data):
            targetlist =  self.shift(targetlist,1)
            targetlist[-1] = new_data
            return targetlist

        def animate(self,i):
            self.mytime = self.update_list(self.mytime, self.mytime_data)
            self.value = self.update_list(self.value, self.value_data)
            self.mytime_data = self.mytime_data+1
            self.value_data = np.random.rand()
            self.ax1.clear()
            self.ax1.scatter(self.mytime, self.value)
            self.ax1.set_xlabel('time')
            self.ax1.set_ylabel('data')
            self.ax1.set_title('Yippee')

    bob = animationthingy()


@app.route('/terminate', methods=['GET'])
def shutdown_server():
    func = request.environ.get('werzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werzeug Server')
    func()


if __name__ == '__main__':
    app.run(debug=True)
