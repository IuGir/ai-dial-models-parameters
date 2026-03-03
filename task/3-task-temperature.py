from task.app.main import run

print("Input the temperature (0.0 to 2.0):")
temperature = float(input())

if temperature >= 0.0 and temperature <= 2.0:
    print(f"You chose: {temperature}")
    run(
        deployment_name='gpt-4o',
        print_only_content=True,
        temperature=temperature,
    )
else:
    print("Invalid temperature")