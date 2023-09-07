# coding:utf-8

import sys
import re
from pathlib import Path

if __name__ == "__main__":
    path = Path(sys.path[0])
    result=[]
    for file in path.glob('**/*'):
        file_str = str(file)
        if re.findall("(svg|png|ico|css|qss|md)$", file_str):
            resource = file_str.replace(str(path), "")[1:]
            resource = resource.replace("\\", "/")
            if "feather" in resource: continue
            result.append(resource)
        # if str(file).endswith(("svg","png","ico","css","qss","md")):
        #     print(file)
    print(len(result))
    content = "".join([f"        <file>{x}</file>\n" for x in result])
    
    resources_rc_file = str(path) + "/resources.qrc"
    with open(resources_rc_file, "w", encoding="utf-8") as f:
        f.write("""<!DOCTYPE RCC>
<RCC>
<!-- prefix 配合 alias 才会增加效率，单独使用prefix路径更长 -->
    <qresource>
{}
    </qresource>
</RCC>""".format(content))
    