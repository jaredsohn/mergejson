mergejson
=========

Merge together multiple json files 

Quickly-built tool to merge two JSON files together

Used in MuteTab to include features that don't seem to be supported by openforge into the manifest file.

Usage: mergejson file1 file2 outfile

Order matters (i.e. if same field is in both, then the contents of file2 will overwrite the contents of file1).

TODO: At the moment this unfortunately does not merge arrays but instead replaces one instance with the other.

