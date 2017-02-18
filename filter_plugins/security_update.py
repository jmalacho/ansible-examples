# Jinja2 filters for needs_reboot question in security update role

def matchFromList( inString, rexList ):
  import re
  for rexS in rexList:
    if re.search( rexS, inString ):
      return True
  return False

def isRebootNeeded( inString, pkgList ):
   rexList=map( lambda x: "Package %s\\.\\S+ \\S+" % x, pkgList)
   return matchFromList( inString, rexList )
 
  

# Boilerplate code to add filter to Jinja2
class FilterModule(object):
     def filters(self):
       return { 'isRebootNeeded': isRebootNeeded,
                'matchFromList': matchFromList
              }

