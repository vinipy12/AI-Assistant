# Ocular AI: An Autonomous Edge-AI Companion

Ocular AI is a privacy-first, fully offline virtual assistant prototype designed to bridge the gap between Large Language Models (LLMs) and physical interaction. Built on the **Qwen 3.5** architecture, it features an expressive visual interface ("eyes") that reacts in real-time to the AI's emotional state.

![Project Status](https://img.shields.io/badge/status-prototyping-orange)
![License](https://img.shields.io/badge/license-Apache%202.0-blue)
![Platform](https://img.shields.io/badge/platform-Raspberry%20Pi%205-red)

## 🚀 Key Features

* **100% Offline Inference:** Powered by **Ollama** and **Qwen 3.5 (2B/0.8B)**. No data leaves the device.
* **Expressive Visuals:** Dual SPI circular LCD displays simulating pupils with fluid emotional states (Happy, Sad, Thinking, Surprised).
* **Low Latency Pipeline:** Optimized STT (Speech-to-Text) and TTS (Text-to-Speech) using **Whisper** and **Piper**.
* **JSON-Driven Personality:** A structured prompt-engineering layer that ensures the AI controls its physical expressions via JSON schema.
* **Edge-Optimized:** Designed to run efficiently on ARM64 architecture (Raspberry Pi 5) with active cooling considerations.

## 🛠 Tech Stack

* **Language:** Python 3.13+
* **LLM Engine:** [Ollama](https://ollama.com/)
* **Model:** Qwen 3.5 (Quantized GGUF)
* **Audio STT:** OpenAI Whisper (Tiny/Base)
* **Audio TTS:** Piper TTS (ONNX)
* **Hardware Interface:** RPi.GPIO / Spidev (for SPI Displays)

## 📂 Project Structure

```text
├── src/
│   ├── brain/           # Ollama integration and Prompt Engineering
│   ├── vision/          # LCD drawing logic and eye animations
│   ├── audio/           # Whisper and Piper implementation
│   └── core/            # Main orchestrator (Asyncio-based)
├── hardware/            # Wiring diagrams and 3D enclosure files
├── scripts/             # Setup and model quantization tools
└── Modelfile            # Custom Ollama configuration
