def before_scenario(context, scenario):
    context.base_url = (
        "https://jsonplaceholder.typicode.com"
    )

    context.response = None