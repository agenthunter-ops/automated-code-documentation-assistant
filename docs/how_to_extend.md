# Extending ACDA

## Add a New Language
1. Compile Tree-sitter grammar and add to `build/my-languages.so`.
2. Implement `<lang>_analyzer.py` in `src/agents`.
3. Update router to enqueue analyzer based on file extensions.

## Swap Vector Store
Replace `faiss` with `Chroma`:


## Integrate Confluence
Create `src/channels/confluence.py` using its REST API, then call from `notifier.py`.
