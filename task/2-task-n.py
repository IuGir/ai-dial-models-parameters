from task.app.main import run

deployment = 'gpt-4o'

print("Input the number of choices (1 to 5):")
n = int(input())

if n >= 1 and n <= 5:
    print(f"You chose: {n}")

if n >= 1 and n <= 5:
    run(
        deployment_name=deployment,
        n=n,
    )
else:
    print("Invalid number of choices")

