Blog post links:
The rise of the data engineer: https://medium.freecodecamp.org/the-rise-of-the-data-engineer-91be18f1e603
the fall of the data engineer: https://medium.com/@maximebeauchemin/the-downfall-of-the-data-engineer-5bfb701e5d6b

# The rise of the data engineer
### Data Engineering field
Smaller environments:
    1. use hosted services offered by Amazon/Databricks
    2. get support from companies like Cloudera or Hortonworks (subcontracts data engineering role to other companies)
Larger environments:
    1. Data Infra team & data engineering team collaborate to solve higher level problems


### ETL (Extract, Transform, and Load) is changing

Moved away from the drag-and-drop ETLs to a more programmatic approach.


#### Here are some changes observed in data modeling techniques:

* further denormalization: maintaining [surrogate keys](https://www.kimballgroup.com/1998/05/surrogate-keys/) in dimensions can be tricky, and it makes fact tables less readable. The use of natural, human readable keys and dimension attributes in fact tables is becoming more common, reducing the need for costly joins that can be heavy on distributed databases. Also note that support for encoding and compression in serialization formats like Parquet or ORC, or in database engines like Vertica, address most of the performance loss that would normally be associated with denormalization. Those systems have been taught to normalize the data for storage on their own.

* blobs: modern databases have a growing support for blobs through native types and functions. This opens new moves in the data modeler’s playbook, and can allow for fact tables to store multiple grains at once when needed

* dynamic schemas: since the advent of map reduce, with the growing popularity of document stores and with support for blobs in databases, it’s becoming easier to evolve database schemas without executing DML. This makes it easier to have an iterative approach to warehousing, and removes the need to get full consensus and buy-in prior to development.

* systematically snapshoting dimensions (storing a full copy of the dimension for each ETL schedule cycle, usually in distinct table partitions) as a generic way to handle [slowly changing dimension (SCD)](https://en.wikipedia.org/wiki/Slowly_changing_dimension) is a simple generic approach that requires little engineering effort, and that unlike the classical approach, is easy to grasp when writing ETL and queries alike. It’s also easy and relatively cheap to denormalize the dimension’s attribute into the fact table to keep track of its value at the moment of the transaction. In retrospect, complex SCD modeling techniques are not intuitive and reduce accessibility.

* conformance, as in (conformed dimensions)[https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/conformed-dimension/] and metrics is still extremely important in modern data environment, but with the need for data warehouses to move fast, and with more team and roles invited to contribute to this effort, it’s less imperative and more of a tradeoff. Consensus and convergence can happen as a background process in the areas where the pain point of divergence become out-of-hand.


#### Roles & Responsibilities

##### The data warehouse
A data warehouse is a copy of transaction data specifically structured for query and analysis. — Ralph Kimball

A data warehouse is a subject-oriented, integrated, time-variant and non-volatile collection of data in support of management’s decision making process. — Bill Inmon

The modern data warehouse is a more public institution than it was historically... The data engineering team will often own pockets of certified, high quality areas in the data warehouse.

#### Performance tuning and optimization

It’s definitely in the interest of the data engineer to build [on] infrastructure that scales with the company, and to be resource conscious at all times.

#### Data Integration

As [Software as a Service (SaaS)](https://en.wikipedia.org/wiki/Software_as_a_service) becomes the new standard way for companies to operate, the need to synchronize referential data across these systems becomes increasingly critical (SaaS ~= on-demand software).

Worst, company executive often sign deal with SaaS providers without really
considering the data integration challenges. The integration workload is systematically downplayed by vendors to facilitate their sales, and leaves data engineers stuck doing unaccounted, under appreciated work to do. Let alone the fact that typical SaaS APIs are often poorly designed, unclearly documented and “agile”: meaning that you can expect them to change without notice.

#### Services
Some automation tasks such as:

* data ingestion: services and tooling around “scraping” databases, loading logs, fetching data from external stores or APIs, …
* metric computation: frameworks to compute and summarize engagement, growth or segmentation related metrics
* anomaly detection: automating data consumption to alert people anomalous events occur or when trends are changing significantly
* metadata management: tooling around allowing generation and consumption of metadata, making it easy to find information in and around the data warehouse
* experimentation: A/B testing and experimentation frameworks is often a critical piece of company’s analytics with a significant data engineering component to it
* instrumentation: analytics starts with logging events and attributes related to those events, data engineers have vested interests in making sure that high quality data is captured upstream
* sessionization: pipelines that are specialized in understanding series of actions in time, allowing analysts to understand user behaviors

#### Required Skills
1. SQL Mastery
    1. Beyond the declarative nature of SQL, she/he should be able to read and understand database execution plans, and have an understanding of what all the steps are, how indices work, the different join algorithm and the distributed dimension within the plan.
2. Data modeling techniques
    1. for a data engineer, [entity-relationship modeling](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) should be a cognitive reflex, along with a clear understanding of normalization, and have a sharp intuition around denormalization tradeoffs. The data engineer should be familiar with [dimensional modeling](https://en.wikipedia.org/wiki/Dimensional_modeling) and the related concepts and lexical field.
3. ETL design
    1. efficient, resilient and “evolvable” ETL is key
4. Architectural projections
    1. The properties, use-cases and subtleties behind the different flavors of databases, computation engines, stream processors, message queues, workflow orchestrators, serialization formats and other related technologies.



# The fall of the data engineer


#### Boredom & context switching

#### Consensus seeking

#### Change Management

#### The worst seat at the table






