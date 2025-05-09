# best-coffe-shop
Temporal.io tutorial in python

- We added orchestrator-service with workflow `CoffeeOrderWorkflow` . 
- `CoffeeOrderWorkflow` executes activity of type `BillCalculationActivity`  to get to know billing amount.

Check related blog posts for more information.


#### Tech Stack :
    docker, 
    docker-compose, 
    python, 
    temporal, 
    SvelteJS - Web UI


#### 📖 Related Blog Posts

[Brewing Coffee : Setting Up Temporal for Best-Coffee-Shop](https://anieruddha.hashnode.dev/temporal-tutorial-docker-setup)

[Brewing Coffee : First Temporal Workflow, One Cup at a Time](https://anieruddha.hashnode.dev/temporal-tutorial-first-workflow)

[Brewing Backend Workflows: Setting Up Payment with Temporal Activities](https://anieruddha.hashnode.dev/temporal-tutorial-first-activity)

[Brewing Coffee : Setting up remaining Activities](https://anieruddha.hashnode.dev/brewing-coffee-setting-up-remaining-activities)

#### Setup
1. Run `docker-compose up` to run all containers.
2. Go to `http://localhost:9090` to place order
3. To Connect redis vi redis-cli fire `redis-cli`. Redis will be running on `127.0.0.1:6379` 
