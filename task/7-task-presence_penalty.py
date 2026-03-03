from task.app.main import run

presence_penalty = 0.0

print("Input the presence penalty (-2.0 to 2.0):")
presence_penalty = float(input())

if presence_penalty >= -2.0 and presence_penalty <= 2.0:
    print(f"You chose: {presence_penalty}")
    run(
        deployment_name='gpt-4o',
        presence_penalty=presence_penalty,
        print_only_content=True,
    )
else:
    print("Invalid presence penalty")

