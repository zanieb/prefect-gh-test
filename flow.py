from prefect import flow

@flow
def hello_flow():
   print("Hello world!")

