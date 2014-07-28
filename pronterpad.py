
import pygame
import wx
import time




pygame.init()

class pronterPadFrame(wx.Frame):
  
    
    def __init__(self, *args, **kwds):
        # begin wxGlade: pronterPadFrame.__init__
        self.port = None
        kwds["style"] = wx.DEFAULT_FRAME_STYLE        
        wx.Frame.__init__(self, *args, **kwds)   

        self.TIMER_ID = 100  # pick a number
        
        self.controller = Joystick()
        
        self.timer = wx.Timer(self, self.TIMER_ID)  # message will be sent to the panel
        self.timer.Start(100)  # 100 milliseconds
        
        self.numAxes = self.controller.countAxes()
        self.numButtons = self.controller.countButtons()
        
        self.axesList = [0.0] * self.numAxes 
        self.axesSpeeds = [] * self.numAxes
        self.buttonsList = [0] * self.numButtons     
        
        self.axesLabels = []  
        self.buttonsLabels = []  
        
        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        
        for i in range(0, self.numAxes) :
            text = 'Axis ' + str(i) + ': 0.0'
            self.axesLabels.append(wx.StaticText(self.panel_1, wx.ID_ANY, text))
            self.axesSpeeds.append(wx.TextCtrl(self.panel_1, value='10'))
            
          
        print self.axesSpeeds
        for i in range(0, self.numButtons) :
            text = 'Button ' + str(i) + ': 0'
            self.buttonsLabels.append(wx.StaticText(self.panel_1, wx.ID_ANY, text))        

        self.Bind(wx.EVT_TIMER, self.on_timer, self.timer)     
        self.__set_properties()
        self.__do_layout()
        # end wxGlade
        

    def __set_properties(self):
        # begin wxGlade: pronterPadFrame.__set_properties
        self.SetTitle("Gamepad")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: pronterPadFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        
        for i in range(0, self.numAxes) :         
            sizer_2.Add(self.axesLabels[i], 0, 0, 0)   
            sizer_2.Add(self.axesSpeeds[i], 0, 0, 0)
            
        for i in range(0, self.numButtons) :
            sizer_2.Add(self.buttonsLabels[i], 0, 0, 0)
            
        self.panel_1.SetSizer(sizer_2)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade
        
    def on_timer(self, event):
        data = self.controller.readAxes()        

        for i in range(0, self.numAxes) :
            out = 'Axis ' + str(i) + ': ' + str(data[i])
            self.axesLabels[i].SetLabel(out)
            
        data = self.controller.readButtons()  
        for i in range(0, self.numButtons) :
            out = 'Button ' + str(i) + ': ' + str(data[i])
            self.buttonsLabels[i].SetLabel(out)    
        
        print com.port
    
    
    
    
class Joystick() :
    def __init__ (self, *args, **kwds):
        self.joy = pygame.joystick.Joystick(0)
        self.joy.init()        
        
    def countAxes(self) :
        return self.joy.get_numaxes()
        
    def countButtons(self) :
        return self.joy.get_numbuttons()
        
    def readButtons(self) :
        out = []
        index = 0
        pygame.event.pump()
        for i in range(0, self.joy.get_numbuttons()):        
            out.append(self.joy.get_button(i))
        
        return out
    
    def readAxes(self) :
        out = []
        index = 0
        pygame.event.pump()
        for i in range(0, self.joy.get_numaxes()):        
            out.append(self.joy.get_axis(i))
        
        return out
   

        
class Com() :
    def __init__(self, *args, **kwds) :
        self.port = None       
        
    def _send(self, data) :
        port.write(data)
        
    def sendGCode(axis, steps) :
        line = 'G91 ' + axis + ' ' + str(steps) + ' G90'
        self._send(line)
        
    def setCom(self, *args, **kwds) :
        self.port = kwds['port']


# end of class pronterPadFrame
if __name__ == "__main__":  
    import serial
    ser = serial.Serial('/dev/ttyS0', 115200)  
    com = Com()
    com.setCom(port=ser)  
    
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
 
    ppFrame = pronterPadFrame(None, wx.ID_ANY, '')
    app.SetTopWindow(ppFrame)
    ppFrame.Show() 
    
    app.MainLoop()





        


