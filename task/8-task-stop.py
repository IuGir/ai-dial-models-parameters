from task.app.main import run

stop = '\n\n'

#  1. Use `stop` parameter with value "\n\n"
#  2. Use `stop` parameter with values ["**Embedding Layer**", "**Transformer Blocks**", "**Training**"]

run(
    deployment_name='gpt-4o',
    print_only_content=False,
    stop=stop,
)
