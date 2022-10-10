start:
	docker compose up -d
	watchman-make -p '**/*.py' -s 1 --run 'touch uwsgi-reload'
stop:
	docker compose down
restart:
	docker compose restart
	watchman-make -p '**/*.py' -s 1 --run 'touch uwsgi-reload'
watch:
	watchman-make -p '**/*.py' -s 1 --run 'touch uwsgi-reload'