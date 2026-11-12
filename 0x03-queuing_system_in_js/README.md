# 0x03. Queuing System in JS

This project explores Redis from Node.js, Redis pub/sub, Kue jobs, and Express
applications backed by Redis.

## Tasks

| Task | Files |
| --- | --- |
| 0. Connect to Redis | [0-redis_client.js](./0-redis_client.js) |
| 1. Set and display Redis values | [1-redis_op.js](./1-redis_op.js) |
| 2. Use asynchronous Redis operations | [2-redis_op_async.js](./2-redis_op_async.js) |
| 4. Store and display Redis hash values | [4-redis_advanced_op.js](./4-redis_advanced_op.js) |
| 5. Publish and subscribe to Redis messages | [5-publisher.js](./5-publisher.js), [5-subscriber.js](./5-subscriber.js) |
| 6. Create and process a notification job | [6-job_creator.js](./6-job_creator.js), [6-job_processor.js](./6-job_processor.js) |
| 7. Create and process multiple notification jobs | [7-job_creator.js](./7-job_creator.js), [7-job_processor.js](./7-job_processor.js) |
| 8. Create push-notification jobs | [8-job.js](./8-job.js), [8-job.test.js](./8-job.test.js) |
| 9. Reserve product stock with Express and Redis | [9-stock.js](./9-stock.js) |
| 100. Reserve seats with Express, Redis, and Kue | [100-seat.js](./100-seat.js) |

There is no task 3 file in this checkout. The project dependencies and available
commands are documented in [package.json](./package.json); install dependencies
with `npm install`. Task 8 tests can be run with
`npm test -- 8-job.test.js`.
