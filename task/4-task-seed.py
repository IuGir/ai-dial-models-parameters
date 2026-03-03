from task.app.main import run

n = 5
print("Input the seed (any integer):")
seed = int(input())

if seed >= 0:
    print(f"You chose: {seed}")
    run(
        deployment_name='gpt-4o',
        seed=seed,
        n=n,
    )
else:
    print("Invalid seed")
