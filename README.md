# i3
home for scripts, configs, etc

dependencies
============

# what I currently have re: deps, more formal coming soon
i3-py==0.6.4
docopt==0.6.2 


migrate_workspaces.py
---------------------

```bash
migrate_workspaces.py (left|right) <exclude>...
```

Use case: 2 outputs - 27in monitor, 14in laptop

Always leave workspace 1 on laptop, moving others to external monitor.

```config
bindsym $mod+F7 exec /usr/local/bin/migrate_workspaces.py left 1

bindsym $mod+F8 exec /usr/local/bin/migrate_workspaces.py right 99
```

