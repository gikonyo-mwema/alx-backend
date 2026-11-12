# ALX Backend

This repository contains backend specialization assignments in pagination,
caching, internationalization, and Redis-backed queues. Each project directory
has its own README with task descriptions and links to the implementation and
available test/driver files.

## Projects and tasks

### [0x00. Pagination](./0x00-pagination/README.md)

- [Task 0: Simple helper function](./0x00-pagination/0-simple_helper_function.py) · [driver](./0x00-pagination/0-main.py)
- [Task 1: Simple pagination](./0x00-pagination/1-simple_pagination.py) · [driver](./0x00-pagination/1-main.py)
- [Task 2: Hypermedia pagination](./0x00-pagination/2-hypermedia_pagination.py) · [driver](./0x00-pagination/2-main.py)
- [Task 3: Deletion-resilient hypermedia pagination](./0x00-pagination/3-hypermedia_del_pagination.py) · [driver](./0x00-pagination/3-main.py)

### [0x01. Caching](./0x01-caching/README.md)

- [Task 0: Basic cache](./0x01-caching/0-basic_cache.py) · [driver](./0x01-caching/0-main.py)
- [Task 1: FIFO cache](./0x01-caching/1-fifo_cache.py) · [driver](./0x01-caching/1-main.py)
- [Task 2: LIFO cache](./0x01-caching/2-lifo_cache.py) · [driver](./0x01-caching/2-main.py)
- [Task 3: LRU cache](./0x01-caching/3-lru_cache.py) · [driver](./0x01-caching/3-main.py)
- [Task 4: MRU cache](./0x01-caching/4-mru_cache.py) · [driver](./0x01-caching/4-main.py)
- [Task 100: LFU cache](./0x01-caching/100-lfu_cache.py) · [driver](./0x01-caching/100-main.py)

### [0x02. i18n](./0x02-i18n/README.md)

- [Task 0: Basic Flask app](./0x02-i18n/0-app.py) · [template](./0x02-i18n/templates/0-index.html)
- [Task 1: Basic Babel setup](./0x02-i18n/1-app.py) · [template](./0x02-i18n/templates/1-index.html)
- [Task 2: Get locale from request](./0x02-i18n/2-app.py) · [template](./0x02-i18n/templates/2-index.html)
- [Task 3: Parametrize templates](./0x02-i18n/3-app.py) · [template](./0x02-i18n/templates/3-index.html)
- [Task 4: Force a locale with URL parameters](./0x02-i18n/4-app.py) · [template](./0x02-i18n/templates/4-index.html)
- [Task 5: Mock logging in](./0x02-i18n/5-app.py) · [template](./0x02-i18n/templates/5-index.html)
- [Task 7: Infer a user's locale](./0x02-i18n/7-app.py) · [template](./0x02-i18n/templates/7-index.html)
- [Final app](./0x02-i18n/app.py) · [final template](./0x02-i18n/templates/index.html)
- [Babel configuration](./0x02-i18n/babel.cfg)

### [0x03. Queuing System in JS](./0x03-queuing_system_in_js/README.md)

- [Task 0: Redis client](./0x03-queuing_system_in_js/0-redis_client.js)
- [Task 1: Basic Redis operations](./0x03-queuing_system_in_js/1-redis_op.js)
- [Task 2: Redis operations with async handling](./0x03-queuing_system_in_js/2-redis_op_async.js)
- [Task 4: Advanced Redis operations](./0x03-queuing_system_in_js/4-redis_advanced_op.js)
- [Task 5: Redis publisher](./0x03-queuing_system_in_js/5-publisher.js) · [subscriber](./0x03-queuing_system_in_js/5-subscriber.js)
- [Task 6: Create and process a job](./0x03-queuing_system_in_js/6-job_creator.js) · [processor](./0x03-queuing_system_in_js/6-job_processor.js)
- [Task 7: Create and process multiple jobs](./0x03-queuing_system_in_js/7-job_creator.js) · [processor](./0x03-queuing_system_in_js/7-job_processor.js)
- [Task 8: Create push-notification jobs](./0x03-queuing_system_in_js/8-job.js) · [tests](./0x03-queuing_system_in_js/8-job.test.js)
- [Task 9: Reserve stock](./0x03-queuing_system_in_js/9-stock.js)
- [Task 100: Reserve seats](./0x03-queuing_system_in_js/100-seat.js)
- [Node package configuration](./0x03-queuing_system_in_js/package.json)

The i18n directory has no task 6 files, and the queueing directory has no task 3
file; the links above reflect the tasks present in this checkout.
