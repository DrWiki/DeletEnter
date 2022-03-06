from PyQt5 import QtWidgets,QtGui, QtCore
import sys
from ParentUI import DeletEnter
import pyqtgraph as pg

class Win(DeletEnter.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Win, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        # 画布1
        self.PBDo.clicked.connect(self.do)
        self.TB1.setText("We present a soft haptic sensor named Insight that uses vision \n \
and learning to output a directional force map over its entire \n \
thumb-shaped surface. The sensor has a localization accuracy of\n \
0.4 mm, force magnitude accuracy of 0.03 N and force direction\n \
accuracy of 5°. It can independently infer the locations, normal\n \
forces and shear forces of multiple simultaneous contacts—up to\n \
five regions in our evaluation. Moreover, the sensor is so sensitive\n \
that its quasi-static orientation relative to gravity can be inferred\n \
with an accuracy around 2°. A particularly sensitive tactile fovea\n \
with a thinner elastomer layer allows it to detect contact forces as\n \
low as 0.03 N and perceive the detailed shape of an object. A detailed\n \
comparison between Insight and other sensors can be found in\n \
Table 1 and the Methods.\n \
The majority of sensors detect deformations with classical meth-\n \
ods and use linear elastic theory to compute interaction forces. This\n \
approach requires good calibration and special care with reflec-\n \
tion effects and inhomogeneous lighting. The linear relationship\n \
between deformations and forces is often violated for strong con-\n \
tacts and for inhomogeneous surfaces like the over-moulded shell of\n \
Insight. As our method is data-driven and uses end-to-end learning,\n \
all effects are modelled automatically. The downside of our approach\n \
is that it requires a precise test bed to collect reference data. Once\n \
constructed, the test bed can collect data for different sensor geom-\n \
etries—only a geometric model of the design is required.\n \
The inhomogeneity of our sensor’s surface might cause unwanted\n \
effects in some applications. Robotic systems that move with high\n \
angular velocities and high accelerations will probably see tactile\n \
sensing artefacts caused by inertial deformations of the soft sensing\n \
surface; data collected during dynamic trajectories could potentially\n \
mitigate these effects.\n \
In general, our sensor design concept can be applied and extended\n \
to a wide variety of robot body parts with different shapes and pre-\n \
cision requirements. The machine-learning architecture, training\n \
process and inference process are all general and can be applied to\n \
differently shaped sensors or other sensor designs. We also provide\n \
ideas on how to adjust Insight’s design parameters for other applica-\n \
tions, such as the field of view of the camera, the arrangement of the\n \
light sources and the composition of the elastomer.")


    def do(self):
        string = self.TB1.toPlainText()
        newstring = string.replace('.\n',"$$$")
        newstring = newstring.replace('\n'," ")
        newstring = newstring.replace('$$$',".\n")
        self.TB2.setText(newstring)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setAttribute(QtCore.Qt.AA_Use96Dpi)
    mainWindow = Win()
    mainWindow.show()
    sys.exit(app.exec_())