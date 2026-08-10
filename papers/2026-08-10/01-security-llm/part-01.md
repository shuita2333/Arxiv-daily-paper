# 🔐 大模型安全相关研究 | 2026年08月10日

> 本类共 **5** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [WorldMark: A Plug-and-Play World Knowledge Interface for Cross-Host Language Model Watermarking](https://arxiv.org/abs/2608.06416)

**<font color=#1a73e8>作者：</font>** Song Xiao, Yuqi Yuan, Yanshuo Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Watermarking traces the provenance of text produced by large language models by embedding statistically detectable signals during decoding. Existing schemes fall into logits-based, sampling-based, entropy-aware, and adaptive-strength families, yet all of them place watermark signals according to local token statistics. In the open-ended text-generation settings evaluated in this work, local statistics may provide insufficient guidance for placing robust watermark signals. We introduce WorldMark, a plug-and-play interface that uses World Knowledge Memory (WKM) to organize semantic and episodic knowledge in a memory graph, converts the retrieved knowledge into a token-level knowledge saliency score, and adjusts the strength of a host watermark through Asymmetric Knowledge Modulation (AKM). WorldMark requires no backbone retraining and introduces no additional detector-side model or parameter. On the primary C4 evaluation, the complete WorldMark interface improves clean and attacked detection across three adaptive-strength host variants while slightly reducing perplexity. Additional pilot experiments on C4 and OpenGen show that direct memory conditioning transfers across multiple watermark families but can be unstable without saliency-aware modulation. WorldMark requires no additional detector-side model or parameter and introduces negligible overhead under the primary protocol.

---


### 2. [StepJack: Benchmarking Computer-Use Agent Safety Against Multi-Step Indirect Prompt Injection](https://arxiv.org/abs/2608.06477)

**<font color=#1a73e8>作者：</font>** Zhuoxin Zhan, Akbar Rafiey, Avery Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Computer-use agents (CUAs) face a growing threat from indirect prompt injection, where adversarial instructions are planted in the environment such as web pages. In this paper, we introduce multi-step indirect prompt injection, a new attack class against CUAs in which the adversarial goal is decomposed into multiple innocuous-looking sub-steps and distributed across a chain of pages referenced along the agent's navigation path. We develop a pipeline to automatically decompose an adversarial goal under the constraint that the execution of the decomposed sub-steps must achieve the original goal while optimizing the innocuousness of each decomposed sub-step. With this pipeline, we build StepJack, a CUA safety benchmark with 480 test examples. On this benchmark, we evaluate six state-of-the-art CUAs and find that at a fixed decomposition depth, multi-step attacks raise attack success rate (ASR) on three of six CUAs, by up to 31.2 points (e.g., GPT-5.4-mini: 41.7% at single-step to 72.9% at three-step); averaged over the five CUAs that can reliably follow the reference chain (all but EvoCUA-32B), ASR rises from 31.3% at single-step to 36.9% at three-step. Dataset and code are available at this https URL.

---


### 3. [LoRAScan: Detecting Backdoor Prompts in Low-Rank Adapters for Large Language Models via Down-Projection Activation Spikes](https://arxiv.org/abs/2608.06795)

**<font color=#1a73e8>作者：</font>** Doniyorkhon Obidov, Honggang Yu, Xiaolong Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Low-rank adaptation (LoRA) enables efficient specialization and distribution of large language models through compact adapters. However, untrusted adapters introduce a supply-chain threat: a backdoored adapter can cause a model to generate harmful content, malicious code, political propaganda, or covert advertisements when an input contains a hidden trigger. Adapter-agnostic defenses merge the adapter with the base model, which dilutes backdoor signals and reduces detection performance. Existing adapter-aware methods do not address how to safely use a potentially backdoored adapter. Instead, they either train a defensive adapter to repair a backdoored base model, addressing the inverse problem rather than securing the adapter itself, or rely on a classifier that flags the entire adapter as suspicious and requires separate mitigation. These methods overlook the distinct latent-space signatures produced by trigger-bearing inputs in backdoored adapters.
We introduce LoRAScan, the first adapter-aware defense that detects and rejects trigger-bearing inputs at inference time without modifying adapter parameters. Our key observation is that a small subset of LoRA insertion sites, approximately 5%, remains stable across clean inputs but exhibits highly concentrated spikes in LoRA down-projection activations when a trigger is present. LoRAScan identifies these low-variance insertion sites before model deployment and monitors them during inference. Across standard LLM backdoor benchmarks, LoRAScan rejects approximately 98.49 of malicious inputs with a small error rate on clean inputs, outperforming existing defenses across diverse evaluation settings.

---


### 4. [NiyamAI - An Intent-Bound AI Agent with Cryptographically Verifiable Guardrails using Zero-Knowledge Proofs](https://arxiv.org/abs/2608.07167)

**<font color=#1a73e8>作者：</font>** Aditya Katkar, Om Karkele, Kartik Mandhane 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Giving an AI agent the ability to send emails, query databases, or execute commands is useful--until the agent is tricked into doing something it shouldn't. Prompt injection, hallucinated reasoning, and unsafe tool calls form the primary attack surface for autonomous LLM agents. Existing defenses rely on software checks like system prompts or policy filters running on the same machine the attacker targets, offering no verifiable proof of execution. We introduce Niyam-AI, a framework that makes safety enforcement provable. At session start, permitted tools and constraints are locked into an Intent Contract committed via SHA-256. Every tool call is intercepted and validated by an isolated Judge model; upon passing, a zk-SNARK proof is generated via EZKL.
The tool executes only after proof verification, allowing third parties to confirm enforcement without accessing Judge model weights. Evaluating Niyam-AI on 2,000 real-world scenarios from Agent-SafetyBench against NeMo Guardrails, Meta's Llama Prompt Guard 2, and OpenAI's GPT-OSS-Safeguard using 5-fold stratified cross-validation yields an F1 score of 88.5% with a 1.1% false-positive rate (bootstrap 95% CI: [85.19%, 91.88%], N=1000). McNemar's exact paired test confirms significant improvement: Niyam-AI wins 390 discordant scenarios against NeMo (vs 20 losses), 115 against Prompt Guard 2 (vs 13), and 384 against GPT-OSS-Safeguard (vs 19) with p < 0.0001 in all cases.
Proof generation adds 2260.6 +/- 218.4 ms per approved action, while verification takes 53.1 +/- 11.8 ms. Niyam-AI provides a guardrail that is both highly accurate and mathematically verifiable--though this reflects a classifier adapted to Agent-SafetyBench evaluated against zero-shot baselines, a distinction discussed in Section IV.C.

---


### 5. [Diffusion LLMs as Targets and Adversaries: Mechanistic Safety Exploits](https://arxiv.org/abs/2608.07430)

**<font color=#1a73e8>作者：</font>** Elena Dumitrescu, Gert Lek, Lydia Y. Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion Large Language Models (DLLMs) replace autoregressive next-token prediction with iterative parallel denoising, yet their internal safety mechanisms remain poorly understood. In this work, we investigate DLLMs both as targets and as adversaries, exposing mechanistic vulnerabilities in diffusion-based alignment.
We first show that safety alignment in DLLMs remains sparse and transferable across architectures. DLLMs initialized from autoregressive predecessors inherit the same mechanistic safety footprint as their source models, enabling transfer attacks via direct safety neuron mapping and pruning. Self-pruning increases attack success rates (ASR) from 2.6% to 73.8% on LLaDA and from 1.9% to 86.6% on Dream, while transfer pruning from Qwen2.5 increases ASR from 1.9% to 73.2% on Dream and from 7.0% to 86.3% on Fast-dLLM.
Building on these findings, we introduce SN-Guided Diffusion, a fully offline black-box jailbreak framework that steers the diffusion process away from safety-triggering regions using a weighted safety neuron loss, which achieves near-perfect prompt separability (AUROC = 1.0 for benign-vs-jailbreak discrimination). Across multiple open and proprietary targets, our method achieves a transfer ASR of up to 77.1% on Llama-3-8B-Instruct, 86.9% on Qwen2.5-7B-Instruct, and 74.3% against Gemini-2.5-Flash-Lite, while requiring only 20 generation episodes per prompt. Compared to prior jailbreaking frameworks, our method achieves competitive transferability with orders-of-magnitude lower generation cost.
Our codebase is available at this https URL.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
