from task.app.main import run

frequency_penalty = 0.0

print("Input the frequency penalty (-2.0 to 2.0):")
frequency_penalty = float(input())

if frequency_penalty >= -2.0 and frequency_penalty <= 2.0:
    print(f"You chose: {frequency_penalty}")
    run(
        deployment_name='gpt-4o',
        frequency_penalty=frequency_penalty,
        print_only_content=True,
    )
else:
    print("Invalid frequency penalty")

