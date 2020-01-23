# probabilistic-selection-task
Version of the PST for DIVA, implemented in E-Prime.

There are two versions in this repository: `PST_Diva_Train` and `PST_Diva_Scan`.
`PST_Diva_Train` is for out-of-scanner training to ensure that participants understand the task.
`PST_Diva_Scan` is the scanner task.
This task has two runs: training and test.

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
