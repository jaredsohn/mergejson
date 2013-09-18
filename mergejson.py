# Quick tool to merge two JSON files together
# Used in MuteTab to get Manifest file how I want it with OpenForge.
#
# Usage: mergejson file1 file2 outfile
#
# Order matters (i.e. if same field is in both, then the contents of file2 will overwrite the contents of file1).
#
# Written by Jared Sohn 9/15/13
#
# TODO: At the moment this unfortunately does not merge arrays but instead replaces one instance with the other.

import simplejson
import sys
import copy

# from http://blog.impressiver.com/post/31434674390/deep-merge-multiple-python-dicts
def dict_merge(target, *args):
  # Merge multiple dicts
  if len(args) > 1:
    for obj in args:
      dict_merge(target, obj)
    return target
 
  # Recursively merge dicts and set non-dict values
  obj = args[0]
  if not isinstance(obj, dict):
    return obj
  for k, v in obj.iteritems():
    if k in target and isinstance(target[k], dict):
      dict_merge(target[k], v)
    else:
      target[k] = copy.deepcopy(v)
  return target



# get args (filenames)
if len(sys.argv) == 4:
	input1_filename = sys.argv[1]
	input2_filename = sys.argv[2]
	output_filename = sys.argv[3]
else:
	print 'Usage: mergejson inputfile1 inputfile2 outputfile'
	sys.exit(0)

# read files
f = open(input1_filename, 'r')
file1_contents = f.read()
f.close()
f = open(input2_filename, 'r')
file2_contents = f.read()
f.close()

# combine files
json1 = simplejson.loads(file1_contents)
json2 = simplejson.loads(file2_contents)
merged = dict_merge(json1, json2)
outputjson = simplejson.dumps(merged, indent=2)

# write output
f = open(output_filename, 'w')
f.write(outputjson)
f.close()
