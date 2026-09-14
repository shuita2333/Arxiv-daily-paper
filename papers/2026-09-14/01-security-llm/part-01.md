# 🔐 大模型安全相关研究 | 2026年09月14日

> 本类共 **3** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Understanding In-Context Multimodal Jailbreaks via Posterior Reweighting](https://arxiv.org/abs/2609.10613)

**<font color=#1a73e8>作者：</font>** Xu Zhang, Dev Mistry, Xiang Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In-context learning (ICL) jailbreaks reveal a critical vulnerability in multimodal large language models (MLLMs): harmful demonstrations in the prompt can induce unsafe outputs without modifying model parameters. Despite extensive empirical evidence, existing work lacks a principled understanding of why such jailbreaks reliably succeed or how their effectiveness scales with context composition. We propose a posterior reweighting framework that models a safety-aligned MLLM as implicitly operating over competing behavioral modes, and interprets in-context demonstrations as inference-time evidence that dynamically shifts the model's posterior preference between safe and harmful behaviors. This view formalizes jailbreak as a process of evidence accumulation, yielding predictive scaling laws with respect to demonstration count, harmful ratio, adversarial strength, and semantic diversity. Guided by this framework, we introduce a posterior-aware inference-time defense that adaptively injects benign counter-evidence based on estimated risk, effectively suppressing harmful posterior drift while preserving model utility. Compared to existing in-context defenses, our method achieves a significantly improved robustness-utility trade-off under a fixed intervention budget. Together, our results establish posterior reweighting as a unifying and predictive framework for understanding and mitigating ICL jailbreak in MLLMs.

---


### 2. [DriftNet: A Dual-Head Trajectory Transformer for Detecting and Localizing Prompt Injection in LLM Agents](https://arxiv.org/abs/2609.10892)

**<font color=#1a73e8>作者：</font>** Asif Pinjari, Mithun Paul Saint-Germain  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> When an indirect prompt injection succeeds against an LLM agent, the compromise is visible in the agent's own behavior: a benign prefix of tool calls, a poisoned observation, and a suffix of actions that serve the attacker. An operator needs three facts: where the attack entered, which steps it corrupted, and whether apparent poison was resisted. Existing systems return either a whole-trace verdict or a single unsafe index. We present DriftNet, a dual-head trajectory Transformer that reads a logged tool-call trajectory and answers all three questions in one forward pass: one head classifies the trajectory as compromised or not, and a second assigns every step one of four labels (benign, injection point, hijacked, failed injection). To our knowledge it is the first supervised detector to produce this joint output. A frozen sentence encoder and four identity-free world features embed each step; the trained trunk, under two million parameters and optimized with a class-weighted joint objective over both heads, needs no access to the agent's model. On the task-disjoint split of the AgentDrift benchmark (12,536 trajectories, 71,024 labeled steps), with a 20-configuration sweep bounding hyperparameter sensitivity to 0.011 F1 and the test part evaluated exactly once, DriftNet reaches trajectory-level F1 of 0.983, exact injection-point recovery on 98.7% of attacked trajectories, hijacked-span IoU of 0.979, zero flags on 218 resisted attacks, and 2.9% flags on hard negatives. A surface baseline retrained on the identical split recovers 11.1% of partial hijacks and 17.1% of delayed executions; DriftNet reaches 98.6% and 93.2% while lowering every false-alarm rate. Reading all 26 residual errors shows that most misses trace to trajectories whose labeled injection observation carries no legible instruction, and we report the benchmark's measured world-identity regularity alongside the results.

---


### 3. [RAG-Safety-Bench: Reliable Evaluation of Retrieval-Augmented LLM Safety](https://arxiv.org/abs/2609.11758)

**<font color=#1a73e8>作者：</font>** Adithiyan Rajan Indira Saravanan, Kathleen C. Fraser  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Allowing large language models (LLMs) to retrieve information from a set of trusted documents can increase reliability and reduce hallucination. However, recent work has demonstrated that retrieval-augmented generation (RAG) can have unintended side effects on the overall safety of the generated responses, when prompted for harmful or dangerous content. A clearer understanding of the mechanisms leading to this result is needed, as increasing numbers of end users turn to RAG to incorporate corporate documents and knowledge bases into LLM-based systems. We introduce RAG-Safety-Bench, a benchmark to measure the safety impact of RAG on LLM models. By removing the confounding effect of retriever quality, and cleanly separating the problem into four conditions -- non-RAG, RAG with an oracle document containing the answer to the harmful request, RAG with documents related to the harmful request but without the specific answer, and RAG with random, safe documents -- the benchmark isolates the impacts of different factors in the observed safety degradation. We report results across five open-source LLMs, showing an inverse relationship between benign and unsafe capability, strong evidence that baseline safety guardrails do not lead to downstream safety guarantees in the RAG case, and model-specific support for previous findings that even benign documents can lead to unsafe generation in retrieval-enabled systems.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
