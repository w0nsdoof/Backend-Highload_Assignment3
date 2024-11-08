# Project Overview

This project demonstrates a scalable, robust backend system using Django, Gunicorn, Nginx, PostgreSQL, and monitoring tools such as Prometheus and Grafana. The aim is to address the challenges associated with high-load distributed environments, ensuring data consistency, system scalability, and effective observability.

## Features Implemented

- **Django API**: Developed a simple API using Django’s generics views and model serializers to streamline backend functionalities.
- **Multiple Gunicorn Instances**: Configured three separate Gunicorn services to handle concurrent requests efficiently.
- **Nginx Load Balancing**: Used Nginx as a load balancer to distribute incoming traffic across Gunicorn instances for better system reliability and responsiveness. Performance improvements showed a 2.85x increase compared to the single-instance setup. [performance load balancer](assets/image.png)
- **Database Scaling**: Set up a primary PostgreSQL database with a read replica to offload read-heavy operations, enhancing overall query response times. [docker psql databases](assets/image-1.png)
- **Monitoring and Observability**: Integrated Prometheus and Grafana for real-time monitoring and visualization of key metrics, such as response times and error rates. [grafana-1](assets/image-2.png). Also added built-in logging from Django. [django-logging](assets/image-6.png) [logging-file](assets/image-7.png)

## Monitoring Tools

- **Prometheus**: Collected metrics related to requests, database queries, and response times[prometheus](assets/image-3.png)
- **Grafana**: Visualized metrics to quickly identify and respond to issues [grafana-2](assets/image-5.png)

## Conclusion

This project highlights the effective use of scalable backend architectures to handle high-load environments, ensuring strong data consistency and observability. The combination of load balancing, database scaling, and detailed monitoring creates a resilient system capable of handling growth and complexity.
