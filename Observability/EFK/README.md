##Kubernetes logging with ElasticSearch FluentD and Kibana.

EFK, which stands for Elasticsearch, Fluentd, and Kibana, is a popular open-source stack used for collecting, processing, and visualizing logs. The EFK stack is often used by developers and system administrators to gain insights into the behavior of their applications and infrastructure.

Elasticsearch is a distributed search and analytics engine that can store and index large amounts of data. Fluentd is a data collector that can gather data from a variety of sources and send it to Elasticsearch for indexing. Kibana is a data visualization tool that allows users to interact with data stored in Elasticsearch and create custom dashboards and visualizations.

Together, these three components provide a comprehensive logging solution that can handle a large amount of data and provide real-time insights into the behavior of complex systems.

1) Filebeat (Fluentd) collects log events from different resources. Uses K8s API to pull Pod info.
--- Port  
2) Elasticsearch is used to store and index logs. 
3) Kibana is used to visualize logs and provide real-time insights into the behavior of systems.

### Elasticsearch
Elasticsearch is the heart of the EFK stack. It is a distributed search and analytics engine that can store and index large amounts of data. Elasticsearch can be used for a variety of use cases, including search, logging, and analytics.

In the context of EFK, Elasticsearch is used to store and index logs. It provides fast and efficient search capabilities that allow users to quickly find and analyze logs. Elasticsearch is highly scalable and can handle a large amount of data, making it suitable for use in large-scale systems.

### Fluentd
Fluentd is a data collector that can gather data from a variety of sources and send it to Elasticsearch for indexing. Fluentd supports a wide range of inputs and outputs, making it highly flexible and adaptable to different use cases.

In the context of EFK, Fluentd is used to collect logs from various sources, including applications, servers, and network devices. It can process logs in real-time, adding metadata and enriching the logs with additional information. Fluentd can also filter logs, removing unnecessary data and reducing the size of the logs before they are sent to Elasticsearch.

### Kibana
Kibana is a data visualization tool that allows users to interact with data stored in Elasticsearch and create custom dashboards and visualizations. Kibana provides a variety of visualization options, including charts, tables, and maps, allowing users to explore and analyze data in different ways.

In the context of EFK, Kibana is used to visualize logs and provide real-time insights into the behavior of systems. Users can create custom dashboards that display key metrics and trends, allowing them to monitor the health and performance of their applications and infrastructure.

### Filebeat
Filebeat is a lightweight shipper for forwarding and centralizing log data. Installed as an agent on your servers, Filebeat monitors the log files or locations that you specify, collects log events, and forwards them either to Elasticsearch or Logstash for indexing.
