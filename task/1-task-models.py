import questionary
from task.app.main import run

deployment_list = [
    'gpt-4o',
    'claude-3-7-sonnet@20250219',
    'gemini-2.5-pro',
]

model_name = questionary.select("Select one of the following models:", choices=deployment_list).ask()

if model_name:
    print(f"You chose: {model_name}")

if model_name:
    run(
        deployment_name=model_name,
        print_request=False,
        print_only_content=False,
    )
else:
    print("Invalid model name")