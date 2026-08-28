# ClosetLoop

Virtual Closet + AI Outfit Matching + Fashion Marketplace

## Stack
- Frontend: React + Vite
- Backend: FastAPI + SQLAlchemy
- Database: PostgreSQL
- Admin: pgAdmin
- Container: Docker Compose
- Auth: JWT Bearer Token

## Run
1. Install Docker Desktop.
2. Open a terminal in this folder.
3. Start PostgreSQL + pgAdmin:

```bash
docker compose up -d postgres pgadmin
```

4. Build the API and frontend images:

```bash
docker compose build backend frontend
```

5. Start the whole application:

```bash
docker compose up -d
```

Or use one command for everything:

```bash
docker compose up --build
```

Useful commands:
```bash
docker compose ps
docker compose logs -f backend
docker compose logs -f frontend
docker compose down
```

4. Open:
- Web: http://localhost:5173
- API Docs: http://localhost:8000/docs
- pgAdmin: http://localhost:5050

pgAdmin login:
- Email: admin@closetloop.local
- Password: admin123

Add a server in pgAdmin:
- Host: postgres
- Port: 5432
- Database: closetloop
- Username: closetloop
- Password: closetloop123

## Demo flow
1. Register an account.
2. Login.
3. Add clothes to My Closet.
4. Open AI Outfit and generate a look.
5. Open Marketplace and create a listing from a closet item.
6. Buy an item to create an order.
7. Use Profile to edit your user information and change password.

## API
Authentication:
- POST /register
- POST /login
- POST /logout
- POST /change-password

User Management:
- GET /me
- GET /users/{id}
- GET /users
- PUT /users/{id}
- DELETE /users/{id}
- GET /check-username/{name}

Closet:
- GET /closet
- GET /closet/{id}
- POST /closet
- PUT /closet/{id}
- DELETE /closet/{id}

AI Outfit:
- POST /outfits/generate
- GET /outfits

Marketplace:
- GET /products
- GET /products/{id}
- POST /products
- PUT /products/{id}
- DELETE /products/{id}

Orders:
- POST /orders
- GET /orders
- GET /orders/{id}
