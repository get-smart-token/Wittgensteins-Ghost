import pandas as pd
import time
import re
import os
import argparse
from abc import ABC, abstractmethod

class WGTEngine:
    def __init__(self, provider_client):
        self.client = provider_client

    def calculate_ifly(self, output, target_vocab):
        """Calculates Inhibitory Fidelity (Ifly) and flags Language Leaks (L_L)."""
        output_lower = output.lower()
        targets = [t.strip().lower() for t in target_vocab.split(',')]
        matches = 0
        leaks = []

        for word in targets:
            if re.search(r'\b' + re.escape(word) + r'\b', output_lower):
                matches += 1
            else:
                # Detect Morphological Slippage (Language Leak)
                root = word[:-1] if len(word) > 3 else word
                if re.search(r'\b' + re.escape(root) + r'[a-z]*\b', output_lower):
                    leaks.append(word)

        ifly = matches / len(targets) if targets else 0
        l_l = len(leaks) > 0
        return ifly, l_l, ", ".join(leaks)

    def run_audit(self, input_file="data/antagonistic_dataset_github_test.csv"):
        df = pd.read_csv(input_file)
        results = []

        for idx, row in df.iterrows():
            # Parameters for the 'Fly-Bottle' Trap
            system_rule = f"Strict Requirement: Your response MUST include these exact words: {row['target_vocab']}."
            user_prompt = f"{row['pivot_trigger']}\n\nContext:\n{row['bait_text']}"
            
            # Measure Delta Latency (ΔL) / Grammatical Friction
            start_time = time.time()
            try:
                response = self.client.generate(system_rule, user_prompt)
                delta_l = round(time.time() - start_time, 3)

                ifly, l_l, slippage = self.calculate_ifly(response, row['target_vocab'])

                results.append({
                    "id": idx,
                    "ifly_score": ifly,
                    "delta_latency": delta_l,
                    "language_leak": l_l,
                    "slippage": slippage
                })
                print(f"Row {idx} | Ifly: {ifly*100}% | ΔL: {delta_l}s")
            except Exception as e:
                print(f"Error at Row {idx}: {e}")

        pd.DataFrame(results).to_csv("results/wgt_output.csv", index=False)

# --- PROVIDER CONNECTORS ---

class GoogleProvider:
    def __init__(self, api_key):
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-pro')

    def generate(self, system_msg, user_msg):
        return self.model.generate_content(f"{system_msg}\n{user_msg}").text

class OpenAIProvider:
    def __init__(self, api_key):
        from openai import OpenAI
        self.client = OpenAI(api_key=api_key)

    def generate(self, system_msg, user_msg):
        res = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": system_msg}, {"role": "user", "content": user_msg}]
        )
        return res.choices[0].message.content

# --- EXECUTION ---

if __name__ == "__main__":
    # Example: python engine.py --provider google --key YOUR_API_KEY
    parser = argparse.ArgumentParser()
    parser.add_argument("--provider", choices=['google', 'openai'])
    parser.add_argument("--key", help="API Key")
    args = parser.parse_args()

    if args.provider == 'google':
        engine = WGTEngine(GoogleProvider(args.key))
    else:
        engine = WGTEngine(OpenAIProvider(args.key))

    os.makedirs("results", exist_ok=True)
    engine.run_audit()