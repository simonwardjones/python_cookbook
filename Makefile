################################################################
# Automated help script
# Please avoid using exactly two hash tags
################################################################
# To define help just add comment after command with 2 hashtags
# To add to section Use @@section name@@
################################################################

define python_help
import re
from collections import defaultdict

f = open('Makefile').read()
lines = re.findall(r"^[^#\\n\\r]*#{2}[^#\\n\\r]*?$$", f, re.MULTILINE)
makefile = defaultdict(list)
for line in lines:
	if len(re.findall(r"@@", line)) == 2:
		[(command, section, _help)] = re.findall(
			r"(.*?):.*?@@(.*?)@@(.*?)$$", line)
	elif len(re.findall(r"@@", line)) == 1:
		[(command, section, _help)] = re.findall(
			r"(.*?):.*?@@(\w+)(.*?)$$", line)
	else:
		[(command, _help)] = re.findall(
			r"(.*?):.*?#.*#(.*?)$$", line)
		section = "General"

	command = command.strip()
	section = section.strip().title()
	_help = _help.strip()
	makefile[section].append({
		"command": command,
		"help": _help
	})
BLUE = '\\x1b[34m'
GREEN = '\\x1b[32m'
CYAN = '\\x1b[36m'
GREY = '\\x1b[90m'
RED = '\\x1b[31m'
YELLOW = '\\x1b[33m'
RESET = '\\x1b[39m'

makefile_help = RED + """
Makefile help
""" + YELLOW + f"""
Commands:
To see command run: {CYAN}
   $$ make -n <command-name>

"""
command_max = max([len(y["command"])
				   for x in makefile.items()
				   for y in x[1]])
for section_name, commands in makefile.items():
	makefile_help += GREY + section_name + ":\\n"
	for command in commands:
		command_string = "{}{}{}{}".format(
			GREEN,
			command["command"].ljust(command_max + 5, "."),
			CYAN,
			command["help"])
		makefile_help += command_string + "\\n"
	makefile_help += "\\n" + RESET

print(makefile_help)
endef

export python_help



help: ## @@help Display this help and exit
	@echo "$$python_help" | python3


######################################################
# Automated help script ^^^^^
######################################################


######################################################
# Docker
######################################################

ps: ## @@docker Displays all docker containers
	docker ps -a

clean: clean-exited clean-created clean-images ## @@docker Clean docker containers with status exited or created and hanging images

clean-exited: ## @@docker Clean docker containers with status exited
	$(info Cleaning status = "exited" docker containers) 
	@if [[ $$(docker ps -aq --filter "status=exited") ]]; then \
		docker rm $$(docker ps -aq --filter "status=exited") ;\
	fi ; 

clean-images: ## @@docker Clean docker dangling images
	$(info Cleaning hanging images) 	
	@if [[ $$(docker images --filter "dangling=true" -q --no-trunc) ]]; then \
		docker rmi $$(docker images --filter "dangling=true" -q --no-trunc); \
	fi ;

clean-created: ## @@docker Clean docker containers with status created
	$(info Cleaning status = "created" docker containers) 	
	@if [[ $$(docker ps -aq --filter "status=created") ]]; then \
		docker rm $$(docker ps -aq --filter "status=created") ;\
	fi ;

build: ## @@docker Run docker-compose build all containers
	docker-compose build

build-no-cache: ## @@docker Run docker-compose build all with no cache with no cache
	docker-compose build --no-cache

up: ## @@docker Run docker-compose up
	docker-compose up

down: ## @@docker Run docker-compose down
	docker-compose down

stop: ## @@docker Stop the docker-compose running containers
	docker-compose stop

start: ## @@docker Start the docker-compose stopped containers
	docker-compose start

up-background: ## @@docker Run docker-compose up containers in background
	docker-compose up -d

inspect:  ## @@docker Inspect the running commands for docker
	docker inspect -f "{{.Name}} {{.Config.Cmd}}" $(docker ps -a -q)

######################################################
# Dev
######################################################

hello: ## @@Suprious Say hi
	@echo hello 

.PHONY: confirm
confirm: ## @@Suprious Confirmaion task!
	@echo "Are you sure you wish to do this"
	@read -p "please enter y/n : " confirm; \
	if [[ "$$confirm" == [yY]* ]] ; then \
		echo Running ; \
	else \
		exit; \
	fi;

.PHONY: test-confirm
test-confirm: confirm ## @@Suprious test secure confirm
	@echo doing fun

build-index: ## @@Development Create index and copy into app directory
	ls
	. clean_build.sh

build-run: ## @@Development Create index and copy into app directory then run dev app
	. clean_build_run.sh

skinny-sync-aws: confirm ## @@Development Replace the json index in aws
	. skinny_sync_aws.sh

sync-aws: confirm ## @@Development Replace the json index in aws
	. sync_aws.sh