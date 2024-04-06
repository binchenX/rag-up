.PHONY: serve llm

serve:
	python app/api.py


llm:
	ollama run gemma:2b


.PHONY: chat

chat:
	curl -i -XPOST "http://localhost:7654/api/question" \
    --header "Content-Type: application/json" \
    --data '{"question": "where is australia", "user_id": "koala"}'
