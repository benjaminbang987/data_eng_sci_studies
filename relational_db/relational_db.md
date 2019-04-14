Documentation about learnings related to relational database systems.

### Relational Database Management System (RDBMS) and Non-Relational Databases
[What is a Relational Database Management System?](https://www.codecademy.com/articles/what-is-rdbms-sql)

Relational Database is: A relational database is a type of database. It uses a structure that allows us to identify and access data in relation to another piece of data in the database. Often, data in a relational database is organized into tables. 

#### Pros and Cons of RDB
[A Review of Different Database Types: Relational versus Non-Relational](https://www.dataversity.net/review-pros-cons-different-databases-relational-versus-non-relational/#)

1. Pros
    1. Well-established, easy to understand, intuitive, accessive
    2. Free in some cases (Postgresql, etc)
    3. Design of normalization process is well-defined
2. Cons
    1. Relational Databases do not scale out horizontally very well (concurrency and data size), only vertically, (unless you use sharding).
    2. Data is normalized, meaning lots of joins, which affects speed.
    3. Serious lack of support for semi-structured data like image, geography, hierarchical, geometry, sound, etc

Non-Relational / NoSQL:
1. Pros
    1. They scale out horizontally and work with unstructured and semi-structured data. Some support ACID(Atomicity, Consistency, Isolation, Durability) transactional consistency.
    2. Schema-free or Schema-on-read options.
    3. High availability.
    4. While many NoSQL databases are open source and so “free”, there are often considerable training, setup, and developments costs. There are now also numerous commercial products available.
2. Cons
    1. Weaker or eventual consistency (BASE) instead of ACID.
    2. Limited support for joins.
    3. Data is denormalized, requiring mass updates (i.e. product name change).
    4. Does not have built-in data integrity (must do in code).
    5. Limited indexing.


#### Non-Relational Stores in Short

There are many different kinds of non-relational stores; Serra gave an overview of the main types. In today’s market the numerous commercial offerings have created a number of platforms that actually combine different data models into one system. According to Serra, Key-Value Stores offer very high speed via the least complicated data model. Anything can be stored as a value, as long as each value is associated with a key or name.

“Wide-Column Stores are fast and can be nearly as simple as Key-Value Stores,” he remarked. They include a primary key, an optional secondary key, and anything stored as a value.

Document Stores contain data objects that are inherently hierarchical, tree-like structures (most notably JSON or XML). Word documents are not Document Stores, he joked. This is a naming confusion that non-data people sometime make. “It is way of storing all the data in one structure. All information can be stored in one document,” said Serra.

He also touched on Graph Stores, remarking that “Graph Stores are totally different from what we’ve talked about so far. They are not typically scalable, but do have some great use cases and they are really good for storing relationships.”

#### Use Cases for NoSQL Categories

Serra discussed a number of different non-relational use cases as well during his presentation, a few of these mentioned were:

Key-Value Stores: [Redis] Used for cache, queues fit in memory, rapidly changing data, and store blob data. Examples: sensor data, shopping cart, leaderboards, graph data bases, stock prices. Fastest “performance.”
Document Stores: [MongoDB] Have a flexible schemas, dynamic queries, defined indexes, good performance on big DB. Examples: order data, customer data, log data, product catalog, user generated content (chat sessions, tweets, blog posts, ratings, comments). Fastest development.
Wide-Column Stores: [Cassandra] Come with real-time querying of random (non-sequential) data, huge number of writes, sensors. Examples: Web analytics, time series analytics, real-time data analysis, banking industry.
“You may not have the data volume for NoSQL,” said Serra.  “But there are other reasons to use NoSQL. Such examples include storing semi-structured data, schema-less data models, and a need for high availability data.”

#### Uses for Different Database Technologies

Serra also talked about many of the reasons why an organization would use SQL or NoSQL. He said that for traditional OLTP business systems (i.e. ERP, CRM, In-house app) relational databases (RDBMS) are still the primary and most efficient choice. Other choices he discussed were:

Data warehouses (OLAP) are good for relational database (SMP or MPP).
Web and mobile global OLTP applications work well with non-relational database (NoSQL).
Data lakes are good for Hadoop.
Relational and scalable OLTP would work well with NewSQL.

#### Summary When to Choose NoSQL

When and where an enterprise would want to choose a non-relational or NoSQL system over a more traditional relational platform:

  * When bringing in new data with a lot of volume and/or variety.
  * Data is non-relational/semi-structured.
  * Your team will be trained in these new technologies (NoSQL).
  * You have enough information to correctly select the type and product of NoSQL for your situation.
  * You can relax transactional consistency when scalability or performance is more important.
  * You can service a large number of user requests vs rigorously enforcing business rules.
Serra: “RDBMS is for enterprise OLTP and ACID compliance, or databases under 1 terabyte. NoSQL is for scaled OLTP and JSON documents. Hadoop is for Big Data Analytics.”

### Normalization/ Normal Forms (3NF)
Most of the content is copied from either of those two links.
[Description of Normalization](https://support.microsoft.com/en-us/help/283878/description-of-the-database-normalization-basics) <br/>
[Relevant Link for Normalization](https://www.essentialsql.com/get-ready-to-learn-sql-database-normalization-explained-in-simple-english/)

Normalization is the process of organizing data in a database. This includes creating tables and establishing relationships between those tables according to rules designed both to protect the data and to make the database more flexible by eliminating redundancy and inconsistent dependency.

Redundant data wastes disk space and creates maintenance problems. If data that exists in more than one place must be changed, the data must be changed in exactly the same way in all locations. A customer address change is much easier to implement if that data is stored only in the Customers table and nowhere else in the database. 

What is an "inconsistent dependency"? While it is intuitive for a user to look in the Customers table for the address of a particular customer, it may not make sense to look there for the salary of the employee who calls on that customer. The employee's salary is related to, or dependent on, the employee and thus should be moved to the Employees table. Inconsistent dependencies can make data difficult to access because the path to find the data may be missing or broken. 

There are a few rules for database normalization. Each rule is called a "normal form." If the first rule is observed, the database is said to be in "first normal form." If the first three rules are observed, the database is considered to be in "third normal form." Although other levels of normalization are possible, third normal form is considered the highest level necessary for most applications. 

As with many formal rules and specifications, real world scenarios do not always allow for perfect compliance. In general, normalization requires additional tables and some customers find this cumbersome. If you decide to violate one of the first three rules of normalization, make sure that your application anticipates any problems that could occur, such as redundant data and inconsistent dependencies. 

#### Three types of common normal forms:

1. First Normal Form
    1. The information is stored in a relational table with each column containing atomic values. There are no repeating groups of columns. For example:
        1. Eliminate repeating groups in individual tables.
        2. Create a separate table for each set of related data.
        3. Identify each set of related data with a primary key.
2. Second Normal Form
    1. The table is in first normal form and all the columns depend on the table’s primary key. For example:
        1. Create separate tables for sets of values that apply to multiple records.
        2. Relate these tables with a foreign key.
3. Third Normal Form
    1. The table is in second normal form and all of its columns are not transitively dependent on the primary key. For example:
        1. Eliminate fields that do not depend on the key.


#### Example:
Look to https://support.microsoft.com/en-us/help/283878/description-of-the-database-normalization-basics for the concrete example of the three normal forms.

Personal Opinion:
1. A decision to normalize a data table depends on the number of dimensions available in the data table. If the dimension is untraceable or too high, perhaps having so many fragmented normalized tables with 2~3 dimensions is unscalable. (For instance, medical claims data). But it will be useful for data like parts of the claims information - specifically looking at provider information, member information, diagnosis codes, payment information, etc separately).



### OLTP (Online Transactional Processing) vs OLAP (Online Analytical Processing)
[OLTP vs. OLAP](https://www.datawarehouse4u.info/OLTP-vs-OLAP.html) <br/>
[OLTP vs OLAP: What's the Difference?](https://www.guru99.com/oltp-vs-olap.html)

- OLTP (On-line Transaction Processing) is characterized by a large number of short on-line transactions (INSERT, UPDATE, DELETE). The main emphasis for OLTP systems is put on very fast query processing, maintaining data integrity in multi-access environments and an effectiveness measured by number of transactions per second. In OLTP database there is detailed and current data, and schema used to store transactional databases is the entity model (usually 3NF). 

- OLAP (On-line Analytical Processing) is characterized by relatively low volume of transactions. Queries are often very complex and involve aggregations. For OLAP systems a response time is an effectiveness measure. OLAP applications are widely used by Data Mining techniques. In OLAP database there is aggregated, historical data, stored in multi-dimensional schemas (usually star schema). 

For a table that shows the differences between OLTP and OLAP, refer to: https://www.datawarehouse4u.info/OLTP-vs-OLAP.html.

### Denormalized Schemas
[Schema types: Data retrieval performance vs redundant storage](https://www2.microstrategy.com/producthelp/10.4/ProjectDesignGuide/WebHelp/Lang_1033/Content/ProjectDesign/Schema_types__Data_retrieval_performance_versus_re.htm) <br/>
[When and How You Should Denormalize a Relational Database](https://rubygarage.org/blog/database-denormalization-with-examples)<br/>
[Star and SnowFlake Schema in Data Warehousing](https://www.guru99.com/star-snowflake-data-warehousing.html)


#### Why denormalize in the first place?
1. To enhance query performance
2. To make a database more convenient to manage
3. To facilitate and accelerate reporting

SnowFlake schema is an extension of a Star schema: it adds additional dimensions.

Characteristics of Star Schema:
  * Every dimension in a star schema is represented with the only one-dimension table.
  * The dimension table should contain the set of attributes.
  * The dimension table is joined to the fact table using a foreign key
  * The dimension table are not joined to each other
  * Fact table would contain key and measure
  * The Star schema is easy to understand and provides optimal disk usage.
  * The dimension tables are not normalized. For instance, in the above figure, Country_ID does not have Country lookup table as an OLTP design would have.
  * The schema is widely supported by BI Tools

Characteristics of Snowflake Schema:
  * The main benefit of the snowflake schema it uses smaller disk space.
  * Easier to implement a dimension is added to the Schema
  * Due to multiple tables query performance is reduced
  * The primary challenge that you will face while using the snowflake Schema is that you need to perform more maintenance efforts because of the more lookup tables.

