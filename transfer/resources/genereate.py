# coding:utf-8

import sys
import re
from pathlib import Path

if __name__ == "__main__":
    path = Path(sys.path[0])
    result=[]
    for file in path.glob('**/*'):
        if re.findall("svg|png|ico|css|qss|md", str(file)):
            print(file)
            result.append(file)
        # if str(file).endswith(("svg","png","ico","css","qss","md")):
        #     print(file)
    print(len(result))
    