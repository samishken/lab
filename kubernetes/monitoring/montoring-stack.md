# The monitoring stack is reponsible for collecting metrics and visualzing them
# A metric is a number that is used to assess the performance of a status or a process
- memory/cpu usage of pod
# Montoring stack is collecting the metrics and view the numbers


# Prometheus
- Responsible for collecting and storing the metrics, and it stores it as timeseries (time stamp)
- We can use it Alert manager to configure alerts based on certain metrics.
---- example: if the memory of a pod reaches 800MB, send alert email
# Grafana
- helps us create dashboards to visualize the metrics in a beautiful way.
- get initial Grafana passwod
---- example: `helm upgrade prometheus-stack prometheus-community/kube-prometheus-stack -n our-monitoring --values values.yaml`
