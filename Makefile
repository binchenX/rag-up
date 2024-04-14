.PHONY: serve llm

serve:
	python app/api.py
serve-docker:
	docker run -e "MODEL_URL=http://host.docker.internal:11434" -p 7654:7654 binc/rag:0.1

llm:
	ollama run gemma:2b

.PHONY: chat
chat:
	curl -i -XPOST "http://localhost:7654/api/generate" \
    --header "Content-Type: application/json" \
    --data '{"prompt": "$(message)"}'
