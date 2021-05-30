# TFX Airflow

## [CLAAT Document](https://codelabs-preview.appspot.com/?file_id=1t8AE0GkiJVMIRBD1jpz2X7qiZDtvlE4Lj6oAwqb4-Sw#0)

From https://www.tensorflow.org/tfx/tutorials/tfx/airflow_workshop <br>
Codebase available here: https://github.com/tensorflow/tfx/tree/master/tfx/examples/airflow_workshop


### Getting Started 

Clone the contents of this repository. Alternatively, you may clone the example directly from the [TFX Git Repo](https://github.com/tensorflow/tfx).

Create a Python 3.7 Virtual environment. The `requirements.txt` contains all the required dependencies. Install the dependencies by running:

```
pip install -r requirements.txt
```

This should take a while to install all dependencies.


#### Starting Airflow

Start the Airflow server in daemon
```
airflow webserver -D
```
Start the Airflow Scheduler
```
airflow scheduler
```

Once both are running - you should be able to access the Airflow UI by visiting http://127.0.0.1:8080/home on your browser.

To kill the Airflow webserver daemon:
```
lsof -i tcp:8080  
```
You should see a list of all processes with PIDs.


Kill the process by running `kill <PID>` - in this case, it would be `kill 13280`

### Usage Instructions

All usage instructions and complete step-by-step tutorial is available [here.](https://www.tensorflow.org/tfx/tutorials/tfx/airflow_workshop)

### References & Citation

[TensorFlow TFX Workshp](https://www.tensorflow.org/tfx/tutorials/tfx/airflow_workshop) <br>
[TFX on GitHub](https://github.com/tensorflow/tfx)
