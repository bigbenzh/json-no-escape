import json as _json
from functools import partial

class JSON_no_escape():
    pass
    
for i in _json.__all__:
    if not hasattr(JSON_no_escape, i):
        setattr(JSON_no_escape, i, getattr(_json, i))


JSON_no_escape.dump = partial(JSON_no_escape.dump,ensure_ascii=False)
JSON_no_escape.dumps = partial(JSON_no_escape.dumps,ensure_ascii=False)
JSON_no_escape.JSONEncoder = partial(JSON_no_escape.JSONEncoder,ensure_ascii=False)