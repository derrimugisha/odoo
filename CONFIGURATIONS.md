# CONFIGURING VSCODE FOR ODOO

This file includes the configurations you need to configure so that you can start running Odoo projects


- In the root directory of the odoo project that you have cloned, create a folder named conf.
- In that folder copy in your ``odoo.conf`` file.
- In the .vscode folder create a file and name it launch.json, in the created file copy the code below
  
```JSON
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python:Odoo",
      "type": "python",
      "request": "launch",
      "stopOnEntry": false,
      "python": "${command:python.interpreterPath}",
      "console": "integratedTerminal",
      "program": "${workspaceRoot}/odoo-bin",
      "args": [
        "--config=/<<your-root-directory-path/conf/odoo.conf"
      ],
      "cwd": "${workspaceRoot}",
      "env": {},
      "envFile": "${workspaceRoot}/.env",
      "debugOptions": ["RedirectOutput"]
    }
  ]
} 
```

NOTE: ``In the above code make a change to args key to your root directory that leads to conf folder``
