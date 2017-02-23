#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.84.2),
    on Fri Feb 10 14:07:23 2017
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
from psychopy.data import *
from psychopy.iohub import *
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
import pylink # Still waiting on account activation, which is weird that I need it but whatever

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'BasicTrial'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1280, 800), fullscr=True, screen=0,
    allowGUI=False, allowStencil=True,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='deg')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "BlankWait"
BlankWaitClock = core.Clock()
BlankPic = visual.ImageStim(
    win=win, name='BlankPic',
    image=u'./BlankPic.png', mask=None,
    ori=0, pos=(0, 0), size=(16, 16),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "Focal"
FocalClock = core.Clock()


# Initialize components for Routine "RandomStimuli"
RandomStimuliClock = core.Clock()


# Initialize components for Routine "Reward"
RewardClock = core.Clock()
RewardImage = visual.ImageStim(
    win=win, name='RewardImage',
    image=u'./RewardPic.jpg', mask=None,
    ori=0, pos=(0, 0), size=(16, 16),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=5, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    # ------Prepare to start Routine "BlankWait"-------
    t = 0
    BlankWaitClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    BlankWaitComponents = [BlankPic]
    for thisComponent in BlankWaitComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "BlankWait"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = BlankWaitClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *BlankPic* updates
        if t >= 0.0 and BlankPic.status == NOT_STARTED:
            # keep track of start time/frame for later
            BlankPic.tStart = t
            BlankPic.frameNStart = frameN  # exact frame index
            BlankPic.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if BlankPic.status == STARTED and t >= frameRemains:
            BlankPic.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankWaitComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "BlankWait"-------
    for thisComponent in BlankWaitComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "Focal"-------
    t = 0
    FocalClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    from psychopy import visual, core
    from PIL import Image
    import numpy as np
    import glob, os, random, copy, time
    
    randomTime = random.uniform(1,2)
    f1 = Image.open('./FocalPic.png', 'r')
    visual.ImageStim(win, f1).draw()
    win.flip()
    core.wait(randomTime)
    # keep track of which components have finished
    FocalComponents = []
    for thisComponent in FocalComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Focal"-------
    while continueRoutine:
        # get current time
        t = FocalClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FocalComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Focal"-------
    for thisComponent in FocalComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "Focal" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "RandomStimuli"-------
    t = 0
    RandomStimuliClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    from psychopy import visual, core, event
    from PIL import Image
    import numpy as np
    import glob, os, random, copy, time

    aperture1 = visual.Aperture(win, size=2, pos=(4,-4), ori=1, shape='circle')
    aperture1.enable = False
    aperture2 = visual.Aperture(win, size=2, pos=(-4,4), ori=1, shape='circle')
    aperture2.enable = False
    aperture3 = visual.Aperture(win, size=2, pos=(4,4), ori=1, shape='circle')
    aperture3.enable = False
    aperture4 = visual.Aperture(win, size=2, pos=(-4,-4), ori=1, shape='circle')
    aperture4.enable = False

    f1 = Image.open('./SolidRedPic.png', 'r')
    f2 = Image.open('./BlankPic.png', 'r')
    visual.ImageStim(win, f2).draw()
    aperture1.enable = True
    visual.ImageStim(win, f1).draw()
    randomNumber = randint(0,4)
    #win.flip()
    #event.waitKeys()
    if randomNumber==0:
        aperture1.enable = True
        visual.ImageStim(win, f1).draw()
    elif randomNumber==1:
        aperture2.enable = True
        visual.ImageStim(win, f1).draw()
    elif randomNumber==2:
        aperture3.enable = True
        visual.ImageStim(win, f1).draw()
    else:
        aperture4.enable = True
        visual.ImageStim(win, f1).draw()
    win.flip()
    core.wait(2.0)
    aperture1.enable = False
    aperture2.enable = False
    aperture3.enable = False
    aperture4.enable = False
    # `sizes in Aperture refers to the diameter when shape='circle';
    # vertices or other shapes are scaled accordingl

    # The contents of this file are in the public domain.
    # keep track of which components have finished
    RandomStimuliComponents = []
    for thisComponent in RandomStimuliComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "RandomStimuli"-------
    while continueRoutine:
        # get current time
        t = RandomStimuliClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RandomStimuliComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "RandomStimuli"-------
    for thisComponent in RandomStimuliComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "RandomStimuli" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Reward"-------
    t = 0
    RewardClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    RewardComponents = [RewardImage]
    for thisComponent in RewardComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Reward"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = RewardClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *RewardImage* updates
        if t >= 0.0 and RewardImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            RewardImage.tStart = t
            RewardImage.frameNStart = frameN  # exact frame index
            RewardImage.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if RewardImage.status == STARTED and t >= frameRemains:
            RewardImage.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RewardComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Reward"-------
    for thisComponent in RewardComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 5 repeats of 'trials'



# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
