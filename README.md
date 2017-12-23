timesheet
=========
'timesheet' is a python script that generates time reports from timesheet files.
A timesheet file is a file named in ISO 8601 style (%Y-%m-%d) that contains timestamps ([%Y-%m-%d %I:%M%p]), between which the first sentence is designated as a task.
The report totals all of the hours spent on unique tasks, and ignores those that start with '-'.

Tasks may be separated into projects of infinite depth with colons i.e. [Project:]Taskname e.g. Hobbies:Programming:Timesheet.
The report will total up the hours spent on projects as well as the tasks in them.

Notes per task may be provided after the first sentence, or on additional lines. Also the area before the first timestamp may be used for general notetaking or a list of tasks that should be kept in mind for the day. Notes are included in the report when at least the first level of verbosity is specified.

An example timesheet is provided in '1970-01-01'. A report of it may be generated with `timesheet -r 1970-01-01`.

Install
-------
To install the report generator:
```
make install
```

Uninstall with:
```
make uninstall
```

Additionally, it is recommended that you install timestamp keybindings for use in your favorite editor.
The timestamp should insert into the text the current time in the format of "[%Y-%m-%d %I:%M%p]".
It is additionally recommended that the time be rounded to the nearest 15 minute increment, or whatever you feel is an acceptable time interval (see TIMESHEET_INTERVAL).

A package is provided for those using Sublime Text:
```
cp run_cmd.py ~/.config/sublime-text-3/Packages/User/
Preferences > Key Bindings > Add '{ "keys": ["f2"], "command": "run_cmd", "args": {"cmd": "timesheet -s"} },'
```
And for those using vim, add this to your .vimrc:
```
:map <F2> :r !timesheet -s<CR>
```

Also, create a directory for storing timesheet files, pick your favorite editor and put the following in your .bashrc or equivalent:
```
export TIMESHEET_TIMEDIR='~/time'
export TIMESHEET_EDITOR='subl'
export TIMESHEET_INTERVAL='900'
```
TIMESHEET_TIMEDIR will default to the current directory when unset. TIMESHEET_EDITOR will default to 'vim'. TIMESHEET_INTERVAL will default to 900 (seconds, equal to 15 minutes).

Usage
-----
For full usage details, see `timesheet -h`.
For typical usage, at the begining of the day the user would use `timesheet` with no arguments, which will create a new timesheet file in their editor of choice.
The user will typically keep this file open throughout the day, using timestamps to delineate tasks, manually editing timestamps when necessary.
The use of `timesheet -r` will generate the report for the day (be sure to add a last untracked entry like "-Done.").
The use of `timesheet -d` will generate reports for the last 10 days of any timesheets that exist within that time. It will also generate a session report totaling all timesheets for the session.