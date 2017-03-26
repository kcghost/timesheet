import datetime
import sublime, sublime_plugin

def roundTime(dt=None, roundTo=60):
  """Round a datetime object to any time laps in seconds
  dt : datetime.datetime object, default now.
  roundTo : Closest number of seconds to round to, default 1 minute.
  Author: Thierry Husson 2012 - Use it as you want but don't blame me.
  """
  if dt == None : dt = datetime.datetime.now()
  seconds = (dt - dt.min).seconds
  rounding = (seconds+roundTo/2) // roundTo * roundTo
  return dt + datetime.timedelta(0,rounding-seconds,-dt.microsecond)

class TimestampCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    timestamp = "[%s]" % (roundTime(roundTo=60*15).strftime("%Y-%m-%d %I:%M%p"))
    self.view.insert(edit, self.view.sel()[0].begin(), timestamp)