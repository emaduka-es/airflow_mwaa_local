from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators.python import PythonOperator
from airflow import DAG
from datetime import datetime, timedelta

default_args = {
    'owner': 'your_owner',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'your_redshift_dag',
    default_args=default_args,
    description='An example DAG to connect to Redshift',
    schedule_interval=timedelta(days=1),
)

def execute_redshift_query(**kwargs):
    redshift_query = """
        select *
        from marina.applicant a 
        limit 10;
    """
    hook = PostgresHook(postgres_conn_id='redshift_conn')
    result = hook.get_pandas_df(sql=redshift_query)
    print(result)


with dag:

        run_redshift_query = PythonOperator(
            task_id='run_redshift_query',
            python_callable=execute_redshift_query,
            provide_context=True,
            dag=dag
        )


run_redshift_query