# run.py
from tasks.calc import calculate
from tasks.log import log_message

links = calculate.s(3, 2) | calculate.s(5) | log_message.s()
# link_tasks = calc.calculate.apply_async(args=[1, 2], links=links)
links()
