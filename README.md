# airflow-plugin-config-storage

Inject connections into the airflow database from configuration

## Common

### CLI Commands

#### `delete-all-airflow-connnections`
Removes all the connections from Airflow. Used to clean out
the default connections.

## Environment Variables

### Structure

The Environment Variables to read from by default are the same
as those defined in the [Airflow documentation](https://airflow.readthedocs.io/en/stable/howto/manage-connections.html#creating-a-connection-with-environment-variables).

### CLI Commands

#### `load-airflow-conf-env-var`

Takes a single optional argument `--env-var-prefix ENV_VAR_PREFIX`
to override the Environment Variable prefix. Default is `AIRLFOW_CONN_`.


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
