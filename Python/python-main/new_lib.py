import requests
r = requests.get("https://gitlab.com/api/v4/users/jaweriaaslam317/projects")
my_project = r.json()
print(my_project)

#print(type(my_project))
for project in my_project:
    print(f"project name is: {project['name']}\n project_url: {project['http_url_to_repo']} \n")
