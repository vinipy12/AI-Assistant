from typing import Dict, Any
import asyncio
import json
import ollama


class OcularBrain:
    def __init__(self, model_name: str = "assistant-v0.0:latest"):
        self.model_name = model_name
        self.client = ollama.AsyncClient()

    async def get_response(self, user_input: str) -> Dict[str, Any]:
        """
        Sends user input to the local Ollama instance and returns a validated 
        JSON response containing the expression and text.
        """
        try:
            response = await self.client.chat(model=self.model_name, messages=[
                {'role': 'user', 'content': user_input}
            ])
            
            # Extract raw text and attempt to parse JSON
            raw_content = response['response'].strip()
            
            # Safety: If the model included "Thinking..." or text before the JSON,
            # we find the first '{' and last '}'
            start_idx = raw_content.find('{')
            end_idx = raw_content.rfind('}') + 1
            
            if start_idx != -1 and end_idx != 0:
                json_content = raw_content[start_idx:end_idx]
                return json.loads(json_content)
            
            return self._fallback_response("error_parsing")

        except Exception as e:
            print(f"[OcularBrain Error]: {e}")
            return self._fallback_response("system_failure")

    def _fallback_response(self, reason: str) -> Dict[str, Any]:
        """Returns a safe default if the LLM fails or leaks thoughts."""
        return {
            "expression": "annoyed",
            "response": "Ops, meu cérebro deu um pequeno curto-circuito agora!"
        }

# Quick Test Execution
if __name__ == "__main__":
    brain = OcularBrain()
    
    async def main():
        print("---AI Testing Node ---")
        result = await brain.get_response("Olá, como você vai?")
        print(f"Expression: {result['expression']}")
        print(f"Speech: {result['response']}")

    asyncio.run(main())