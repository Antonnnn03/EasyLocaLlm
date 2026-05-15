#!/bin/bash

DIR="$(cd "$(dirname "$0")/.." && pwd)"

export OLLAMA_MODELS="$DIR/models/ollama"
export OLLAMA_HOST="127.0.0.1:11434"

"$DIR/bin/ollama-linux-amd64/bin/ollama" serve