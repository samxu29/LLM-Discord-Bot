#!/bin/bash

python3 -m llama_cpp.server --model models/Mistral-7B-Instruct-v0.1-GGUF/mistral-7b-instruct-v0.1.Q2_K.gguf --n_gpu_layers 35 &
python3 bot.py

# SESSION_NAME="carlBot"
# tmux new-session -d -s $SESSION_NAME

# # Run the first command in the first window
# FIRST_COMMAND="python3 -m llama_cpp.server --model models/Mistral-7B-Instruct-v0.1-GGUF/mistral-7b-instruct-v0.1.Q2_K.gguf --n_gpu_layers 35"
# tmux send-keys -t $SESSION_NAME "$FIRST_COMMAND" C-m

# # Create a new window
# tmux new-window -t $SESSION_NAME

# # Run the second command in the new window
# SECOND_COMMAND="python3 bot.py"
# tmux send-keys -t $SESSION_NAME:1 "$SECOND_COMMAND" C-m

# # Attach to the tmux session
# tmux attach-session -t $SESSION_NAME

