# Documentation about learnings related to schedulers

## Airflow
###  What is it?
It’s a scheduler that orchestrates the resources for various tasks with provided dependencies.
What is a scheduler and why is the orchestration necessary?
Airflow provides a DAG (directed acyclic graph) class. This class has a set of parameters and takes in tasks. Parameters
can set a scheduler of when the DAG should be kicked off, whether the backfill should happen, and other configs such as
how many DAGs can be active at any given time, etc. Dependencies are set within a DAG setup file. The task can be set to
 be dependent on another task, which will set an upstream dependency.
Orchestration is necessary when you want various tasks to happen in a certain order. It is also useful if a transform
requires an input from another transform. It is also necessary for fitting the resource constraint. Given that the resource constraint is money and the size of bins in a cloud that you can purchase with given budget, you would want to make sure that the tasks are not overloading the buckets provided. Therefore, you can setup the size of the buckets that Airflow tasks can be run on and the number of concurrent runs that are possible.


#### Why does Robinhood use Airflow: https://robinhood.engineering/why-robinhood-uses-airflow-aed13a9a90c8

Other workflow management tools considered by Vineet: Pinball, Azkaban, and Luigi.
Pinball (Pinterest) features distributed, horizontally scalable, workflow management and scheduling system, however,
the documentation is sparse and the community is small. Luigi (Spotify) has an active community and uses Python for
workflow definition + a layer of simple UI - but it lacked a scheduler, Azkaban (LinkedIn) lacked the code-based development property.

Airflow uses Operators as the fundamental unit of abstraction to define tasks, and uses DAG to define workflows
using a set of operators (bash, python, etc - BaseOperator(LoggingMixin), LoggingMixin(object)).

Exact quote from the article:
#### Dependency Management 
Operators are extensible which makes customizing workflows easy. Operators are divided into 3 types:
Action operators that perform some action such as executing a Python function or submitting a Spark Job.
Transfer operators that move data between systems such as from Hive to Mysql or from S3 to Hive.
Sensors which trigger downstream tasks in the dependency graph when a certain criteria is met, for example checking for a certain file becoming available on S3 before using it downstream. Sensors are a powerful feature of Airflow allowing us to create complex workflows and easily manage their preconditions.

#### An example ETL that Vineet had was:
Extract layer
Sensors
Transfer
Transform
Action
Load
Transfer
Sensors
Uses the Sensor operators to wait until data is available and uses a Transfer operator to move the data to the required location. An Action operator is then used for the Transform stage followed by using the Transfer operator to load the results. Finally, we use Sensor operators to verify that the result was stored appropriately.

#### Failure Handling and Monitoring
Airflow allows configuration of retry policies into individual tasks and also allows to set up alerting in the case of failures, retries as well as tasks running longer than expected. UI is intuitive and there are powerful tools for monitoring and managing jobs. It provides historical views of the jobs and tools to control the state of jobs - such as killing a running job or manually re-rerunning a job.
One cool thing is the visualization of the jobs. This allows building custom visualization to monitor the jobs closely and also acts as a great debugging tool while triaging issues with jobs and scheduling.

#### Extensible
Since the Operators are Python classes, it’s very easy to extend and create a custom, reusable workflows (such as CTF) by simply extending the existing operator classes. Robinhood added classes like OpsGenieOperator, DjangoCommandOperator and KafkaLagSensor.

#### Smarter Cron
For jobs that should only run on the days when the market is open, Robinhood created a workflow such as MarketOpenBranchOperator -> MarketClosedForDaySensor -> DjangoCommandOperator. This example has schedules that dynamically update according to the market hours for a given day.

#### Backfills
Airflow provides a CLI that allows users to run backfills across arbitrary spans of time with a single command, and also allows users to trigger backfills from the UI. Celery (built by Robinhood engineer Solem) is used to distribute these tasks across worker boxes. The distribution capabilities of Celery make backfills quick and easy by allowing users to spin up more worker boxes while running backfills.
Common Pitfalls and Weaknesses
Time zone issue - Airflow relies on the system time zone (instead of UTC) for scheduling - this requires the entire airflow setup to be run in the same time zone.

The Scheduler works separately for scheduled jobs and backfill jobs. This can result in weird outcomes such as backfills not respecting a DAG’s max_active_runs configuration.

Airflow was built primarily for data batch processing due to which the Airflow designers made a decision to always schedule jobs for the previous interval. Hence, a job scheduled to run daily at midnight will pass in the execution date “2016–12–31 00:00:00” to the job’s context when run on “2017–01–01 00:00:00”. This can get confusing especially in the case of jobs running at irregular intervals.

Unexpected backfills — Airflow by default tries to backfill missed runs when resuming a paused DAG or adding a new DAG with a start_date in the past. While this behavior is expected, there is no way to get around this, and can result in issues if a job shouldn’t run out of schedule. Airflow 1.8 introduces the LatestOnlyOperator to get around this issue.

## Celery in Apache Airflow

https://airflow.apache.org/howto/executor/use-celery.html
Inside Apache Airflow, tasks are carried out by an executor. The main types of executors are:

* Sequential Executor: Each task is run locally (on the same machine as the scheduler) 
in its own python subprocess. They are run sequentially which means that only one task can be executed at a time. It is the default executor.
* Local Executor: It is the same as the sequential executor except that multiple tasks can run in parallel. It needs a metadata database (where DAGs and tasks status are stored) that supports parallelism like MySQL. Setting such a database requires some extra work since the default configuration uses SQLite.
* Celery Executor: The workload is distributed on multiple celery workers which can run on different machines. It is the executor you should use for availability and scalability.

#### Distributed Apache Airflow Architecture

Essential Understanding of the differences between Celery (Task Queue) and RabbitMQ (Message broker)
* RabbitMQ provides an API for other services to publish and to subscribe to the queues.
* Celery is a task queue. It can distribute tasks on multiple workers by using a protocol to transfer jobs from the
 main application to Celery workers. It relies on a message broker to transfer the messages.
 
Requirements for distributed Apache Airflow Architecture:
* A __metadata database__: containing the status of the DAG runs and task instances
* __Airflow webserver__: a web interface to query the metadata to monitor and execute DAGs
* __Airflow Scheduler__: checks the status of the DAGs and tasks in the metadata database, create new ones if necessary and sends the tasks to the queues.
* A __Message Broker__ (RabbitMQ): stores task commands to be run in queue.
* __Airflow Celery workers__: retrieve the commands from the queues, and execute them and update the metadata.

[Clairvoyant](http://site.clairvoyantsoft.com/setting-apache-airflow-cluster/)