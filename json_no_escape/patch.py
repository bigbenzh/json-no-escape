import json
from functools import partial

json.dump = partial(json.dump,ensure_ascii=False)
json.dumps = partial(json.dumps,ensure_ascii=False)
json.JSONEncoder = partial(json.JSONEncoder,ensure_ascii=False)