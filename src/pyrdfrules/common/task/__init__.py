"""
Task is a pipeline sent to the engine to be executed.

Task is a representation of the results from RDFRules.

Tasks should not be created directly, but rather through an instance of Application.

Tasks should also not be updated manually.

Example task creation:

    app = pyrdfrules.application.Application()
    
    rdfrules = app.start_remote(
        url = Url("http://example.com/api/"),
        config=Config(
            task_update_interval_ms=1000
        )
    )
        
    task : Task = None
    
    with open("./tests/data/task.json", "r") as file:        
        task_json_from_file = file.read()
        task = rdfrules.task.create_task_from_string(task_json_from_file)
        
To run a task:

    task = rdfrules.task.create_task(pipeline)
            
    for step in rdfrules.task.run_task(task):
        # do something with the step 

Tasks are run iteratively to not block control of user over the task, since a task can be interrupted during runtime. You may wish to do this in case the pipeline creates a combinatorial explosion.

To interrupt a task:

    rdfrules.task.stop_task(task)
    
Tasks may emit events, such as log messages, which can be listened to:

    task.on_log_message += lambda message: log().info(message)
    task.on_finished += lambda message: log().info('Task finished')
    
Events can be found in the Event submodules of the Task module.
"""