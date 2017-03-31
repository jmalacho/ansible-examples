#!/usr/bin/python

from ansible.module_utils.basic import *
def pkg2dict( s="0:MySQL-python-1.2.3-0.3.c1.1.el6" ):
  original=s
  a=s.split("-")
  release=a[-1]
  
  a=a[0:-1]
  version=a[-1]
  
  a=a[0:-1]
  key="-".join(a)
  epoc=0
  if key[0].isdigit():
    a=key.split(":")
    epoc=int( a[0] )
    name=a[1]
  else:
    name=key
    key="0:" + key

  return { "key":key, "name":name, "version":version, "release":release, "epoc":epoc, "original":original }

def main():
    fields = {
      "action": { "required": True, "type": "str",
                  "choices": ["add","list","delete","remove","clear"],
                },
      "name": { "default": "*", "type": "str"},
    }
    module = AnsibleModule(argument_spec=fields)
    rc, out, err = module.run_command( ["yum","versionlock", "-q","list"],  executable="/usr/bin/yum", use_unsafe_shell=False )
    packages=out.strip().split("\n")
    pdict={}
    for p in packages:
      d=pkg2dict(p)
      pdict[ d["key"] ]=d

   
    
    response = {"rc": rc,
                "out": pdict,
                "err": err
               }
    module.exit_json(changed=False, meta=response)


if __name__ == '__main__':  
    main()
