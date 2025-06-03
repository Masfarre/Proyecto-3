# API Reference

## Endpoints

### GET /api/tasks
Returns all tasks

### GET /api/users
Returns all users

### GET /api/stats
Returns system statistics

## Example Response
```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Fix critical bug",
      "priority": "high",
      "status": "open"
    }
  ]
}
