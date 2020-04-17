# Food Expense Tracker 
User friendly way to track how much money you burn by eating food. See how much you spend per meal,
and helps you optimize your food expenses.


# Development

## Debug

Setup instructions for visualstudio debug setup. 
https://code.visualstudio.com/docs/containers/debug-python

1. add the following configuration to your configuration list in ```launch.json```
```
{
  "name": "Python: Remote Attach",
  "type": "python",
  "request": "attach",
  "port": 5678,
  "host": "localhost",
  "pathMappings": [
    {
      "localRoot": "${workspaceFolder}",
      "remoteRoot": "/app"
    }
  ]
}
```

2. hit the following endpoint localhost:5000/debug_connect
3. run Python: Remote Attach config in Visual Stuido



