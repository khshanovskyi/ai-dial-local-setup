# Start DIAL Chat with Themes and Core

1. Open the `docker-compose.yml` in the project root
2. Run it with:
    ```bash
    docker compose up -d
    ```
3. Check that they are up 
    ```bash
    docker compose ps -a
    ```
    **For MAC users please uncomment in config for each service the `platform: linux/amd64`**
4. Open in browser [local dial chat](http://localhost:3000/marketplace) and check that it works. There will be no models
and applications, it is okay, we will create them with next task.
<img src="_screenshots/marketplace.png">
<img src="_screenshots/chat.png">
`Not available agent selected. Please, change the agent to proceed` it is okay, since we didn't add any models or applications into `config.json`
5. When you run `docker compose` you will probably find that the 2 new folders were created (`core-data`, `core-logs`). It is okay, there will persist logs from Core and local Bucket to persist conversations and files