# Jinja2 filters for use in building dictionary with /etc/hosts to template

# Initialize a Dictionary keys with default value (usefull for preseting the value to an array)
def initDict( in_default, keyarray ):
  r={}
  for k in keyarray:
    r[k]=in_default
  return r

# Appends the hostname with subdomain first, then its shortname
def mergeInventory( in_dict, domain, groups, hostvars ):
  for host in groups[group]:
    in_dict[ host ].append( hostvars[host]["hostname"] + "." + domain )
    in_dict[ host ].append( hostvars[host]["hostname"] )
  return in_dict

# Generally Merges a Dictionary of array by appending to each array
# Used to merge in the dictionary of host-aliases
def mergeDictOfArrays( in_dict, update ):
  for k, v in update.iteritems():
    in_dict.setdefault(k, [] )
    in_dict[k]+=v
  return in_dict 

# Boilerplate code to add filter to Jinja2
class FilterModule(object):
     def filters(self):
       return { 'initDict': initDict,
                'mergeInventory': mergeInventory,
                'mergeDictOfArrays': mergeDictOfArrays,
              }

