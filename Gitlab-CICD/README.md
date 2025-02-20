# GITLAB
- Platform used to build our CI/CD pipeline
- Comes with built in tools helpful for our pipeline.
- - Example: Self-Monitoring, Container Registry, Docker CI Runner
- Allows keeping CI/CD & code managment in the same place
- All in one solution.
- Self managed and SaaS (managed)
- CI/CD is written in yaml file.
---
###### Pipeline
- 

###### Group Jobs

##### stages
- test, build, deploy: group jobs under these stages 
- Setup dependency between jobs
- - Job dependency: "needs" or "depends_on"


##### Inline commands
- pwd, ls, mkdir

##### Predefined variables
- "$CI_COMMIT_BRANCH != "main" && $CI_PIPELINE_SOURCE != "merge_request_event"

##### Custom variables
- "Settings" -> "Variables" -> add variable
- Helps us store values that we want to re-use multiple times.  Reducing code duplication

--- 
### Feature branch
- when we create a feature branch immediatly a new pipeline runs
- WE NEED TO SPECIFY WHEN JOB SHOULD RUN
- - 

- Merge request ("pull request") branch should not create break

---

### Gitlab Architecture
- Execution of jobs
- Gitlab server sends info to Gitlab runner to run
#### Servers
- Gitlab Server: main component of Gitlab
- - has all information about pipeline configuration
- - manages the pipeline execution
- - stores the pipeline results. 

#### Runners
- jobs are executed on Gitlab Runners.
- - we can have multiple runners. 
- - Program that we should install on a machine, that's separate from the one that hosts the Gitlab instance.
- - The provided runners by Gitlab are instance runners
- - Instance runners are avvailable to all projects in a Gitlab instance
- - Instance runners on gitlab.com are available to all users on the platform.

- We can have Runner for just one project, group of projects, or all projects

- PROJECTS RUNNERS: For many projects in a company.

#### managing Gitlab
- SaaS - manged by Gitlab
- Self managed: 

#### Executors
- Docker executors: for each job a new docker container is created and then removed after the job is completed.
- Docker Machine Executor: By default Gitlab provides us with Docker Machine Executor.
- - - depricated by docker. Gitlab maintains it.
- - - 
- Register multiple runners


#### Job Execution Flow
(Gitlab Server -> Gitlab Runner - Gitlab Executor)
- First - Runner requests new jobs from Gitlab Server (instance)  (e.g. Gitlab.com)
- Second - Runner compiles and sends the jobs payload to Executor
- Third - Executor clones sources or downloads artifacts from Gitlab instance and executes the job.
- Fourth - Executor returns job output and status to the Runner
- Fifth - Runner updates job output and status to Gitlab instance