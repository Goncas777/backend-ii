import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL


_USER = {"id": 1, "name": "John Doe"}


@strawberry.type
class User:
    id: int
    name: str


@strawberry.type
class Query:
    @strawberry.field
    def user(self, id: int) -> User | None:
        if id != _USER["id"]:
            return None
        return User(id=_USER["id"], name=_USER["name"])


@strawberry.type
class Mutation:
    @strawberry.mutation
    def update_user_name(self, id: int, name: str) -> User:
        _USER["id"] = id
        _USER["name"] = name
        return User(id=_USER["id"], name=_USER["name"])


schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQL(schema)

app = FastAPI()
app.add_route("/graphql", graphql_app)
