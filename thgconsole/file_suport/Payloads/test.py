from glob import glob
import os
for i in glob("*"):
    print("{} = 'file://' + pkg_resources.resource_filename(__name__, '{}')".format(i,i))