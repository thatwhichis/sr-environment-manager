from datetime import datetime as dt
import logging as log
import os, sys
import subprocess as sub
import tkinter as tk
import xml.etree.ElementTree as et

# EXTERNAL LOG FILE
S_LOGNAME = 'SR_EnvironmentManager.log'
S_LOGDIR = '\\logs'

# EXTERNAL FILE DEPENDENCY
S_FILENAME = 'SR_EMConfig.xml'
S_NOFILE = 'Not found'

# WINDOW STYLING
F_RELX = 0.5
FO_TEXT = ('helvetica', 12, 'bold')
I_WINDOW_WIDTH = 400
I_WINDOW_HEIGHT = 300
S_ANCHOR = 'center'
S_COLOR_BAD = 'red'
S_COLOR_GOOD = 'green'

# EXECUTABLE OR PY DIRNAME?
if getattr(sys, 'frozen', False):
  s_dir = os.path.dirname(sys.executable)
else:
  s_dir = os.path.dirname(os.path.abspath(__file__))

# CONFIGURE LOG OUTPUT FOR ERROR FILE GENERATION AND REPORTING
b_logr_fail = False
if os.path.exists(s_dir + S_LOGDIR):
  if os.path.isfile(s_dir + S_LOGDIR + '\\' + S_LOGNAME):
    s_log = open(s_dir + S_LOGDIR + '\\' + S_LOGNAME, "r").read().split('LAUNCHED:')
    s_timestamp = s_log[len(s_log) - 1][0:14]
    try:
      os.rename(s_dir + S_LOGDIR + '\\' + S_LOGNAME, s_dir + S_LOGDIR + '\\SR_EnvironmentManager_' + s_timestamp + '.log')
    except OSError:
      b_logr_fail = True
else:
  os.makedirs(s_dir + S_LOGDIR)
log.basicConfig(filename = s_dir + S_LOGDIR + '\\' + S_LOGNAME, level=log.DEBUG)
if b_logr_fail:
  log.debug('LOG FILE RENAME FAILURE')
log.info('ENVIRONMENT MANAGER LAUNCHED:' + dt.now().strftime("%Y%m%d%H%M%S"))
log.info('OPERATING PATH IS:' + s_dir)

# CREATE ROOT WINDOW VIA TKINTER
w_root = tk.Tk()
w_root.title("ENVIRONMENT MANAGER")

# DEFINE FUNTIONS
# callback function to execute environment configuration
def fu_environment ():
  if xml_root is None:
    log.debug('BUTTON PRESSED WITH NO VALID XML_ROOT')
  else:
    log.info('BUTTON PRESSED WITH VALID XML_ROOT')
    log.info('SEARCHING FOR VALID PROJECT NAME:' + tks_om.get())
    for xml_project in xml_root.findall('Project'):
      if xml_project.get('Name') == tks_om.get():
        log.info('VALID PROJECT NAME FOUND:' + tks_om.get())
        b_response = True
        for xml_variable in xml_project.findall('Variable'):
          log.info('ATTEMPTING TO SET VARIABLE NAME:' + xml_variable.get('Name') + ':WITH VALUE:' + xml_variable.get('Value'))
          # execute terminal process; using 'setx' for demo visibility under 'User variables'
          response = sub.run(['setx', xml_variable.get('Name'), xml_variable.get('Value')], shell = True, stdout = sub.PIPE, stderr = sub.PIPE)
          # handle subprocess responses
          if response.returncode > 0:
            b_response = False
            log.debug('ENVIRONMENT VARIABLE NOT SET:' + response.stderr.decode("utf-8"))
          else:
            log.info('ENVIRONMENT VARIABLE SET:' + response.stdout.decode("utf-8"))
        if b_response:
          tkl_result = tk.Label(w_root, text = 'Environment configured for ' + tks_om.get(), fg = S_COLOR_GOOD, font = FO_TEXT)
        else:
          tkl_result = tk.Label(w_root, text = 'Environment not configured (see log)', fg = S_COLOR_BAD, font = FO_TEXT)
        tkl_result.place(relx = F_RELX, rely = 0.8, anchor = S_ANCHOR)
        break

# CREATE CANVAS
tkc_canvas = tk.Canvas(w_root, width = I_WINDOW_WIDTH, height = I_WINDOW_HEIGHT)
tkc_canvas.pack()

# INSTRUCTIONAL LABEL
tkl_instruct = tk.Label(w_root, text = 'Select a Project, then Configure Environment', fg = 'black', font = FO_TEXT)
tkl_instruct.place(relx = F_RELX, rely = 0.2, anchor = S_ANCHOR)

# OPTION MENU
# pull in menu options from external file, handle missing file
if os.path.isfile(s_dir + '\\' + S_FILENAME):
  log.info('CONFIG.XML FOUND AT:' + s_dir)
  xml_root = et.parse(s_dir + '\\' + S_FILENAME)
  l_options = [project.get('Name') for project in xml_root.findall('Project')]
else:
  log.info('CONFIG.XML NOT FOUND AT:' + s_dir)
  xml_root = None
  l_options = [S_NOFILE]
  tkl_result = tk.Label(w_root, text = 'Config.xml not found', fg = S_COLOR_BAD, font = FO_TEXT)
  tkl_result.place(relx = F_RELX, rely = 0.8, anchor = S_ANCHOR)

# create a tk variable to pass to the tk option menu widget
tks_om = tk.StringVar(w_root)
tks_om.set(l_options[0])

# create and position the tk option menu widget
tkw_optionmenu = tk.OptionMenu(*(w_root, tks_om) + tuple(l_options))
tkw_optionmenu.place(relx = F_RELX, rely = 0.4, anchor = S_ANCHOR)
# END OPTION MENU

# BUTTON
s_button_color = S_COLOR_BAD if l_options[0] == S_NOFILE else S_COLOR_GOOD
tkb_button = tk.Button(text = 'Configure Environment', command = fu_environment, bg = s_button_color, fg = 'white')
tkb_button.place(relx = F_RELX, rely = 0.6, anchor = S_ANCHOR)

# RUN TKINTER ROOT WINDOW LOOP
w_root.mainloop()
