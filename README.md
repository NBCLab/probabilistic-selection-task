# probabilistic-selection-task
Version of the PST for DIVA, implemented in E-Prime.

There are two E-Prime tasks in this repository: `PST_Diva_Train` and `PST_Diva_Scan`.

`PST_Diva_Train` is for out-of-scanner training to ensure that participants understand the task.
The document `PS_task_training_script.docx` contains a script for walking the participant through the training task.

`PST_Diva_Scan` is the scanner task.
This task has two runs: training and test.

• Stimuli Counter-Balancing
           o 6 pictures are randomly assigned to the A-F stimuli with their respective probabilistic outcomes for each subject so the stimuli are not always represented by the same picture to minimize any biases inherent to the individual pictures across participants. 
          o 6 additional pictures are used as practice stimuli pairs during the instruction screens, walk-through examples and practice rounds. 

• Training
          o There are 60 trials: 20 of each stimuli pair (10/10 split of which stim is on the left and right). 
          o For each of the 20 stimuli for each pair type feedback is presented based on the pairs respective probabilities. 
          o During training as each trial happens the count of pair type trial is updated.
          o Each time the participant picks the stimuli that gives them a correct outcome, the number correct for each pair type is updated.
          o The stimuli chosen each trial is also logged to compute win-stay, lose-shift behavior and because feedback of correctness is variable across the same choice. 

          o Participants only advance to the testing round after they have at least 65% correct on AB trials, 60% correct on CD trials and 50% correct on EF trials.
          o After every 60 trials the number correct/total trials for each stimuli pair is calculated.
          o Otherwise they do another round of 60 training trials.
          o This continues until 360 trials and then participants advance regardless of their correct percentages but they will most likely be excluded from future analyses. 

• Testing
          o There are 120 trials in the testing round. 
          o 40 approach A trials, 40 avoid B trials and 40 control trials with only the C, D, E and F stimuli. 
          o There is no feedback in this condition. 


Probabilistic Selection (PS) Task. The PS task will be used to separately calculate positive and negative reinforcement learning rates and learning performances, in addition to win-stay and loose-shift behavioral choices. The task involves an initial instruction phase (~4min) in which the task is explained to the participant and the experimenter walks through example trials with the participant. This is followed by a practice phase (~12min) in which the participant will practice all task procedures with different stimuli than those presented in the actual task as to prevent any pre-task learning about the stimuli. Once the experimenter has ensured that the participant understands the task rules, the participant will then complete the real task which involves a training phase (~7min) followed by a testing phase (~7min). During the training phase, 3 different stimuli pairs (AB, CD, EF) are presented and through ‘trial and error’ participants learn to choose which stimuli is ‘the best choice’ based on probabilistic feedback indicating correct or erroneous selections. In AB trials, stimulus A leads to positive feedback 80% of the time whereas stimulus B leads to negative feedback 80% of the time. CD and EF pairs are less reliable, such that stimulus C leads to positive feedback on 70% of selections and D leads to negative feedback on 70% of selections. Stimulus E leads to positive feedback on 60% of EF trials and F leads to negative feedback on 60% of EF trials. Over the course of training, participants learn to choose stimuli A, C, and E more often than B, D, or F. During the testing phase, novel combinations of stimuli pairs that include either an A (AC, AD, AE, AF) or a B (BC, BD, BE, BF) are presented and no feedback is provided29. Participants’ choices are used to evaluate whether they learned more from positive or negative feedback. Positive reinforcement learning is then operationalized as the ability to choose stimulus A during testing, which had the highest probability of positive outcomes during training. Negative reinforcement learning is operationalized as the ability to avoid choosing stimulus B during testing which had the highest possibility of negative outcomes during training. Trial to trial adaptation will be assessed as average win-stay, loose-shift behavior during training phase. Stimuli in this task consist of affectively-neutral, nonrepresentational white markings/symbols on black background that have been used in previous implementations of this task. The probabilistic properties of symbols are randomly reassigned at the start of the task (e.g. which symbol will be the “A” stimulus) to prevent any symbol-specific effects. We will utilize response time and percent accuracy separately for trials in which participants should choose picture A and trials where they should avoid picture B as objective measures of positive and negative reinforcement learning, respectively.


## Implementation Notes
1. This task is set up to work with FIU's scanner's BioPac.
However, it was developed on a computer that does not have a serial port, which breaks the task if a serial port device is enabled.
As such, there are a number of if/else statements throughout the task to call the serial port when BioPac is enabled and to not call it when it isn't.
This doesn't completely solve the issue, though, so you need to check the devices that are selected under the experiment's main settings before running the task.
If the task will be run on a computer with a serial port, simply turn on the "Serial" device.
Otherwise, make sure it's off.
2. This task writes out a BIDS-compatible tsv file (i.e., an "events" file).
In BIDS events files, the first column should be "onset" (in seconds).
However, E-Prime has an odd behavior where it writes out numeric values with a leading space, so instead we write out a string-based variable as the first column.
Thus, events files written out by this task need to be corrected (i.e., columns need to be reordered to follow BIDS convention) before they will pass the BIDS validator.
3. The BIDS events files are also not quite tab-delimited, so you will need to convert them.
Pandas can do this pretty easily.
For example, the following should work:

```python
import pandas as pd

df = pd.read_table('example_data/sub-777_ses-1_task-PST_run-1.tsv', sep='\s+')
df.to_csv('example_data/sub-777_ses-1_task-PST_run-1.tsv', sep='\t',
          line_terminator='\n', na_rep='n/a', index=False)
```
