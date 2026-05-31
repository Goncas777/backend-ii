uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000

query {
  user(id: 1) {
    id
    name
  }
}


mutation {
  updateUserName(id: 1, name: "Maria") {
    id
    name
  }
}