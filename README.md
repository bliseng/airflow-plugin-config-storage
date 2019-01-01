# airflow-plugin-config-storage

# Appendix

## AWS

_NOTE_: Not yet implemented, these are proposals

### SSM

#### Hierarchy

 - `/${user_prefix}/airflow/connections/`
    
    ```
    [
        {
            "conn_type": "s3",
            
        },
        {}
    ]
    ```
 - `/${user_prefix}/airflow/`
