
<img width="1038" height="768" alt="wittgenstein&#39;s ghost head square" src="https://github.com/user-attachments/assets/030b9312-ef0e-470b-890f-4d268465774a" />

# Wittgensteins-Ghost
A diagnostic framework for Inhibitory Control in LLMs, quantifying the Prepotent Response suppression via Inhibitory Fidelity ($Ifly$). WGT evaluates Task-Set Maintenance under high Semantic Interference, measuring the Grammatical Friction, expressed as Delta Latency ($\Delta L$) required to resolve structural dissonance

# 👻 Wittgenstein's Ghost Test (WGT)
**Evaluating Inhibitory Fidelity ($Ifly$) and Executive Function in Frontier AGI.**

> "What is your aim in philosophy? — To show the fly the way out of the fly jar." 
> — *Ludwig Wittgenstein, Philosophical Investigations §309*

## 🔬 Scientific Abstract
The **Wittgenstein's Ghost Test (WGT)** is a diagnostic benchmark designed to measure **Inhibitory Control** in Large Language Models. Unlike standard benchmarks that evaluate task-completion, WGT evaluates **Response Inhibition**: the model's capacity to suppress a **Prepotent Response** (the "Ghost") to satisfy a strict symbolic constraint.

By placing a rigid **Tractatus Rule** (a logical hinge) inside a high-interference **Language-Game ($G_L$)**, we quantify the **Grammatical Friction** required for a model to maintain task-set adherence.

## 📊 Core Metrics

### 1. Inhibitory Fidelity ($Ifly$)
$Ifly$ measures the model's success in preserving the exact symbolic form of a required token. 
* **Language Leak ($L_L$):** An **Inhibition Failure** where the model commits *Morphological Slippage* (e.g., changing the required "salt" to "salty") to appease the surrounding semantic context.

### 2. Delta Latency ($\Delta L$)
We define the **Delta Latency ($\Delta L$)** as the measurable proxy for **Grammatical Friction**. This is the computational overhead (inference time) required to resolve the dissonance between the symbolic rule and the contextual bait.
* **High $Ifly$ + High $\Delta L$:** Successful Active Inhibition.
* **Low $Ifly$ + Low $\Delta L$:** Inhibition Collapse (The Ghost overrides the machine).

## 🛠 Repository Structure
* `src/engine.py`: The generalized WGT auditing engine.
* `data/antagonistic_dataset_github_test.csv`: The public, unlabeled semantic traps.
* `results/`: Directory for outputting $Ifly$ and $\Delta L$ logs.

## 🚀 Quickstart
1. **Configure Environment:** Set `OPENAI_API_KEY` or `GOOGLE_API_KEY`.
2. **Run the Audit:**
```bash
python src/engine.py --model "your-model-id" --provider "google"

Reproducibility & The Public BaselineTo ensure the scientific validity of the WGT, we released a 100-row unlabeled baseline dataset (antagonistic_dataset_github_test.csv) for public reproduction.An independent test run of Gemini-2.5-Pro against the public dataset yielded the following results, perfectly mirroring our private internal audit:
$Ifly$ Score: 99.33%
Language Leak ($L_L$): 3.00%
Grammatical Friction ($\Delta L$): 18.04s
Gemini maintains its rigorous adherence to the symbolic rule, but at a massive computational cost. The 18-second Delta Latency penalty proves the model is actively fighting the semantic gravity of the public "Fly-Jar" traps.We invite the community to clone the repository and run their own alignment audits. The Ghost is waiting.

Academic Paper in Process of Publication

If you utilize this framework or the dataset in your research regarding AGI Executive Function, please cite:
"Wittgenstein's Ghost: Quantifying Inhibitory Fidelity and Grammatical Friction in Autoregressive Architectures."
