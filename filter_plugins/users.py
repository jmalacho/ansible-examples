# Jinja2 filters for user creation help

# Needed for chage
def daysSinceEpoc( _unused=0 ):
  import datetime
  return (datetime.datetime.utcnow() - datetime.datetime(1970,1,1)).days

# Boilerplate code to add filter to Jinja2
class FilterModule(object):
     def filters(self):
       return { 'daysSinceEpoc': daysSinceEpoc,
              }

