import numpy as np
import pandas as pd

"""
Why Data Cleaning Exists?

In the real world, data is collected by humans, exported from different systems, merged from multiple sources, and passed through pipelines
that nobody fully understands anymore. By the time it reaches you, it's almost never clean. Missing values, wrong types, duplicate rows,
inconsistent formatting — these are not edge cases. They are the norm.

The danger is not that dirty data throws errors. Errors are actually the good outcome — you know something is wrong. The real danger is
dirty data that silently produces wrong results. A missing value that gets treated as zero. A duplicate row that inflates your average. A
column that looks numeric but is secretly a string. Your analysis runs fine, produces a number, and that number is wrong. Nobody notices.

Data cleaning is how you prevent that.
"""
