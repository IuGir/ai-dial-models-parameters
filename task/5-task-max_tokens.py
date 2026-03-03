from task.app.main import run

max_tokens = 10

print("Input the maximum number of tokens (10 to 1000):")
max_tokens = int(input())

if max_tokens >= 10 and max_tokens <= 1000:
    print(f"You chose: {max_tokens}")
    run(
        deployment_name='gpt-4o',
        max_tokens=max_tokens,
        print_only_content=True,
    )
else:
    print("Invalid maximum number of tokens")