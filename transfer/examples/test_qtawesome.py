import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import qtawesome as qta


class MyWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("空白测试模板")
        self.resize(800, 600)
        self.layout = QVBoxLayout(self)
        
        # Get FontAwesome 5.x icons by name in various styles:
        fa5_icon = qta.icon('fa5.flag')
        fa5_button = QPushButton(fa5_icon, 'Font Awesome! (regular)')
        self.layout.addWidget(fa5_button)
        
        fa5s_icon = qta.icon('fa5s.flag')
        fa5s_button = QPushButton(fa5s_icon, 'Font Awesome! (solid)')
        self.layout.addWidget(fa5s_button)
        
        fa5b_icon = qta.icon('fa5b.github')
        fa5b_button = QPushButton(fa5b_icon, 'Font Awesome! (brands)')
        self.layout.addWidget(fa5b_button)

        # or Elusive Icons:
        asl_icon = qta.icon('ei.asl')
        elusive_button = QPushButton(asl_icon, 'Elusive Icons!')
        self.layout.addWidget(elusive_button)
        

        # or Material Design Icons:
        apn_icon = qta.icon('mdi6.access-point-network')
        mdi6_button = QPushButton(apn_icon, 'Material Design Icons!')
        self.layout.addWidget(mdi6_button)

        # or Phosphor:
        mic_icon = qta.icon('ph.microphone-fill')
        ph_button = QPushButton(mic_icon, 'Phosphor!')
        self.layout.addWidget(ph_button)

        # or Remix Icon:
        truck_icon = qta.icon('ri.truck-fill')
        ri_button = QPushButton(truck_icon, 'Remix Icon!')
        self.layout.addWidget(ri_button)

        # or Microsoft's Codicons:
        squirrel_icon = qta.icon('msc.squirrel')
        msc_button = QPushButton(squirrel_icon, 'Codicons!')
        self.layout.addWidget(msc_button)

        
        ##################################
        # Styling icons
        styling_icon = qta.icon('fa5s.music',
                                active='fa5s.balance-scale',
                                color='blue',
                                color_active='orange')
        music_button = QPushButton(styling_icon, 'Styling')
        self.layout.addWidget(msc_button)

        # Setting an alpha of 120 to the color of this icon. Alpha must be a number
        # between 0 and 255.
        icon_with_alpha = qta.icon('mdi.heart',
                                color=('red', 120))
        heart_button = QPushButton(icon_with_alpha, 'Setting alpha')
        self.layout.addWidget(heart_button)

        # Stacking icons
        camera_ban = qta.icon('fa5s.camera', 'fa5s.ban',
                            options=[{'scale_factor': 0.5,
                                        'active': 'fa5s.balance-scale'},
                                    {'color': 'red'}])
        stack_button = QPushButton(camera_ban, 'Stack')
        stack_button.setIconSize(QSize(32, 32))
        self.layout.addWidget(stack_button)

        # Icon drawn with the `image` option
        drawn_image_icon = qta.icon('ri.truck-fill',
                                    options=[{'draw': 'image'}])
        drawn_image_button = QPushButton(drawn_image_icon,
                                                'Icon drawn as an image')
        self.layout.addWidget(drawn_image_button)

        # Spining icons
        spin_button = QPushButton(' Spinning icon')
        spin_icon1 = qta.icon('fa5s.spinner', color='red',
                            animation=qta.Spin(spin_button))
        spin_button.setIcon(spin_icon1)
        self.layout.addWidget(spin_button)
        
        # disable Spining icons
        qta.set_defaults(color_disabled=QColor(150, 150, 150))
        spin_button_copy = QPushButton(' Spinning icon')
        spin_icon1 = qta.icon('fa5s.spinner', color='red',
                            animation=qta.Spin(spin_button_copy))
        spin_button_copy.setIcon(spin_icon1)
        spin_button_copy.setEnabled(False)
        self.layout.addWidget(spin_button_copy)
        
        toggle_icon = qta.icon('fa5s.spinner', active='fa5s.balance-scale',
                                color_off='black',
                                color_off_active='blue',
                                color_on='orange',
                                color_on_active='yellow')
        toggle_button = QPushButton(toggle_icon, 'Toggle')
        toggle_button.setEnabled(False)
        self.layout.addWidget(toggle_button)

        # Spining icon widget
        spin_widget = qta.IconWidget()
        spin_icon2 = qta.icon('mdi.loading', color='red',
                            animation=qta.Spin(spin_widget))
        spin_widget.setIcon(spin_icon2)
        self.layout.addWidget(spin_widget)

        # Simple icon widget
        simple_widget = qta.IconWidget('mdi.web', color='blue', 
                                    size=QSize(16, 16))
        self.layout.addWidget(simple_widget)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())