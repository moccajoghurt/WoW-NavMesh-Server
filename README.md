# WoW-NavMesh-Server

A navigation mesh server for World of Warcraft that provides routes based on requests. It uses mmaps from Recast/Detour for pathfinding, FastAPI for the API, and runs in Docker with support for DevContainers.
Built with excessive abstraction, and a deep fear of simplicity. Featuring message buses, dependency injection, and just enough overengineering to make enterprise architects happy.
This server was originally part of a larger system handling multiple responsibilities, which is why the project structure might seem a bit out of place. Feel free to rip out all the unnecessary overhead—unless, of course, you too enjoy overengineering.

- Start with `docker compose up`.
- Runs on port 8080; change it to your liking in docker-compose.yml.

Big shoutout to Drew Kestell, who inspired this repository! Thanks to his great blog post and repository, I learned a lot. The Linux shared library specifically compiled for this Python image is based on Drew Kestell’s Windows DLL.
