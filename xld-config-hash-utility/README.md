# XLD config hash utility

## Usage

1. Apply this entry to the conf/logback.xml file for each node to be examined.

        <logger name="com.xebialabs.deployit.engine.tasker.distribution.versioning" level="trace" />
        
2. Copy the logs to a host with a Python 2.7 installation.

3. Configure the properties file with the appropriate start and end datetimes for the two logs.

4. Run the following after substituting your log file names:

        python xld-config-hash-utility.py deployit_master.log deployit_worker.log.
    
5. Review the output for configuration hash mismatches.

Sample output:

~~~
$ python xld-config-hash-utility.py deployit_master.log deployit_worker.log 

Read 187 lines from /Users/droberts/2023Jul01-config-hash-utility/deployit_master.log
Processing 159 hashed items from /Users/droberts/2023Jul01-config-hash-utility/deployit_master.log

Read 193 lines from /Users/droberts/2023Jul01-config-hash-utility/deployit_worker.log
Processing 159 hashed items from /Users/droberts/2023Jul01-config-hash-utility/deployit_worker.log

-----------------------------------------------------------------------------------

Compare /Users/droberts/2023Jul01-config-hash-utility/deployit_master.log (left) to /Users/droberts/2023Jul01-config-hash-utility/deployit_worker.log (right)
Match 157 items in left log to right log

Mismatch on item xl.scheduler.system.akka.loggers:"akka.event.Logging$DefaultLogger" in left file but not in right file

Mismatch on item database-plugin-9.5.1.xldp:
left file hash is  f283c1bd26665a47a4c5df98655514634a17bd5bb5f2a78370f3457034c4aa15
right file hash is f283c1bd26665a47a4c5df98655514634a17bd5bb5f2a78370f3457034c4aa10

Mismatch on item jee-plugin-9.5.1.xldp:
left file hash is  d8b4c2ea2dae5e72991da2f2fac387eb22286de24316c2ac00887a01fb57d140
right file hash is d8b4c2ea2dae5e72991da2f2fac387eb22286de24316c2ac00887a01fb57d141

-----------------------------------------------------------------------------------

Compare /Users/droberts/2023Jul01-config-hash-utility/deployit_worker.log (left) to /Users/droberts/2023Jul01-config-hash-utility/deployit_master.log (right)
Match 157 items in left log to right log

Mismatch on item xl.scheduler.system.akka.loggers:"akka.event.slf4j.Slf4jLogger" in left file but not in right file

Mismatch on item database-plugin-9.5.1.xldp:
left file hash is  f283c1bd26665a47a4c5df98655514634a17bd5bb5f2a78370f3457034c4aa10
right file hash is f283c1bd26665a47a4c5df98655514634a17bd5bb5f2a78370f3457034c4aa15

Mismatch on item jee-plugin-9.5.1.xldp:
left file hash is  d8b4c2ea2dae5e72991da2f2fac387eb22286de24316c2ac00887a01fb57d141
right file hash is d8b4c2ea2dae5e72991da2f2fac387eb22286de24316c2ac00887a01fb57d140

-----------------------------------------------------------------------------------

Execution completed
~~~