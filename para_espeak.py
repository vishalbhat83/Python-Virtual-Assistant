import wx
import wikipedia
import wolframalpha
import pyttsx3

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="PARA")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hello I am Para, the Python virtual Assistant. How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        input = self.txt.GetValue()
        input = input.lower()
        try:
            #wolframalpha
            app_id = "65U2P2-LX969RK234"
            client = wolframalpha.Client(app_id)
            res = client.query(input)
            answer = next(res.results).text
            print answer
            #espeak.synth("The answer is "+answer)
        except:
            #wikipedia
            input = input.split(' ')
            input = " ".join(input[2:])
            #espeak.synth("Searched for "+input)
            print wikipedia.summary(input)

if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    engine = pyttsx3.init();
    engine.say("Hello I am Para, the Python virtual Assistant. How can I help you?");
    engine.runAndWait();
    app.MainLoop()
