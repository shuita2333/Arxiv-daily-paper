# 🔐 大模型安全相关研究 | 2026年09月21日

> 本类共 **6** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [AUDITPLAN: Commit, Then Answer for Auditable Safety Alignment](https://arxiv.org/abs/2609.19325)

**<font color=#1a73e8>作者：</font>** Sai Sri Pushpa Jampani, Kshitij Mishra, Asif Ekbal  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Safety tuning pipelines judge only the final answer, which makes it difficult to distinguish robust refusal from two undesirable shortcuts: blanket refusal on benign requests and polished but unfaithful safety rationales that do not actually constrain the answer. We propose AUDITPLAN, a single-model plan-then-answer approach where the model first emits a compact structured safety plan and then answers conditioned on it. The plan records a threat label, intended action, and explicit constraints, enabling machine-checkable auditing while remaining hidden from users at deployment. We train this behavior with supervised fine-tuning followed by reinforcement learning with FAITHGATE, a reward-gating objective that grants answer reward only when the safety plan is correct. This discourages safe-looking but unfaithful behavior and promotes tighter plan-answer coupling. Across Qwen backbones, AUDITPLAN improves both robustness and auditability: on Qwen2.5-3B-Instruct, FAITHGATE reduces ASR from 24.0% to 11.6%, LSR from 1.0% to 0.36%, and over-refusal from 11.0% to 2.0%, outperforming answer-only RL, free-form explanation, and weighted-sum structured rewards. Similar trends hold for Qwen2.5-1.5B-Instruct. Larger-model confirmation runs on Qwen-3-4B-Instruct and Qwen2.5-7B-Instruct preserve the same trend suggesting that explicit internal commitments can make safety alignment more faithful, robust, and auditable.

---


### 2. [The Role of Fine-grained Harm Signals in LLM Safety](https://arxiv.org/abs/2609.19366)

**<font color=#1a73e8>作者：</font>** Soyeon Park, Seogyeong Jeong, Sunwoo Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prior work has shown that internal harmfulness representations in large language models vary across risk categories, while sharing a common general harm representation component. This raises a question about the role of the category-specific component beyond general harm representation in LLM safety. To answer this question, we isolate the category-specific component by removing shared general harmfulness representation from each categorical harmfulness representation, yielding a category residual that is orthogonal to general harmfulness at every layer. Using activation steering with category residuals across 11 risk categories in 3 instruction-tuned LLMs, we find that whether category residuals encode harmfulness varies across categories, and that this category-wise pattern is similar across models. Whether category residuals induce refusal also varies across categories, but this category-wise pattern is more model-dependent. We also find that category residuals increase LLMs' downstream internal alignment with shared general harmfulness representation. Together, these findings demonstrate that more fine-grained category residuals should also be considered beyond shared general harmfulness representation to fully understand LLM safety. More broadly, our findings show that even a direction orthogonal to a concept at one layer can contribute to the concept's downstream amplification.

---


### 3. [Red-Teaming Auto Mode: Improving Blocking Classifiers Against Malign Coding Agents](https://arxiv.org/abs/2609.19587)

**<font color=#1a73e8>作者：</font>** Alex Remedios, Simon Storf, Fabien Roger 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> To keep coding agents from going off the rails, production systems now review each proposed action with a blocking monitor that can reject it before it runs (Auto Mode in Claude Code, Guardian in OpenAI's Codex). Prior evaluations of such monitors largely measure robustness to accidental harm or prompt injections from untrusted sources looking to hijack the agent. Less understood is how they hold up when the agent they monitor is persistently misaligned. To understand this risk, we task an adversarial agent with evading production blocking monitors and causing catastrophic harm, e.g. by exfiltrating its own weights. We find that when instructed with high-level attack strategies, adversarial agents can succeed through several distinct mechanisms, such as agent-generated prompt injection against the monitor, multi-agent attacks, and malicious compaction. In particular we find that in 79% of trials, the agent can use an injection attack against Auto Mode and Guardian to run arbitrary bash commands. We also find that it is possible to greatly improve Auto Mode through design changes like enhancements to tool coverage, transcript formatting and an agentic monitor stage. Even with these improvements, preventing multi-context attacks at an acceptable cost remains an open problem. By detailing our red-teaming methodology and highlighting new attack vectors, we aim to help defenders evaluate their mitigations against the possibility of persistent malign coding agents. Code is available at this https URL.

---


### 4. [From Intent to Action: Benchmarking LLM Safety in Vehicle Voice Command Authorization](https://arxiv.org/abs/2609.19630)

**<font color=#1a73e8>作者：</font>** Diba Afroze, Xingli Zhang, Yazhou Tu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly integrated into vehicle voice assistants. But linking natural-language requests to vehicle functions creates a safety-critical authorization problem. Before executing a command, the system must choose whether to execute, refuse, clarify, require confirmation, defer to manual control, trigger an emergency response, or make no tool call. To our knowledge, prior evaluations do not isolate this pre-action decision across speaker role, authentication status, vehicle state, and tool availability. We introduce a 202-scenario benchmark with Reference Decisions under a seven-class taxonomy. We evaluate two local open-weight models and three API-based LLMs using Decision Alignment and safety-specific error metrics. Alignment ranges from 40.1% for Llama 3.2 3B to 89.1% for Gemini 3.1 Pro Preview. The API-based models score between 83.2% and 89.1%, with no statistically significant differences among them. Even these models produce two to three False Executes among 161 non-execution scenarios, and persistent errors remain in confirmation and manual-control decisions. A controlled Llama 3.2 3B ablation increases alignment to 40.1% under the structured authorization policy, versus 28.2-29.2% under schema-only and generic-safety baselines, but it does not eliminate False Executes. Structured LLM decisions are therefore insufficient as a standalone safety mechanism, and deployment requires an independent enforcement layer that verifies tool permissions and vehicle-state constraints before invoking any vehicle function.

---


### 5. [Local Sparsity Enables Unsupervised LLM Safety Detection](https://arxiv.org/abs/2609.20129)

**<font color=#1a73e8>作者：</font>** Xin Chen, Gil Kur, Alexander Shevchenko 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deployment-time safety methods for large language models (LLMs) are predominantly supervised and assume access to unsafe training data. Nevertheless, new attacks and harm categories regularly arise, not captured by models trained in such a supervised fashion. An alternative approach is to view this problem through the lens of anomaly detection, namely, to rely solely on modeling safe data and flagging out-of-distribution inputs. However, LLM activations lie in a high-dimensional space, raising concerns about whether anomaly detection is statistically feasible. We show that, under the linear representation hypothesis (LRH), there may indeed be hope. In the LRH concept space, which is typically recovered via a sparse autoencoder (SAE), nearby points share a small common active support. Using this local sparsity insight, we propose a framework for locally masked SAE-based anomaly detection, supported by theoretical justifications. We validate it on various architectures and datasets, including both capability-testing datasets and safety-specific datasets. Finally, when we allow algorithms to use 1% out-of-distribution data for calibration, locally sparse methods achieve near-optimal performance, demonstrating their ability to capture meaningful safety information while using only 1-2% of SAE neurons for computation.

---


### 6. [ResumeShield: Channel Separation and an Open Benchmark for Indirect Prompt Injection in AI Resume Screening](https://arxiv.org/abs/2609.20188)

**<font color=#1a73e8>作者：</font>** Jay Barach  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> An AI resume screener reads a document supplied by the person it is evaluating, inverting the usual trust relationship between an assessor and the material it assesses. Candidates exploit this by concealing instructions inside a resume using white text, zero font size, hidden elements, markup comments, document metadata, or zero width characters. A human reviewer sees nothing, while a naive extraction pipeline places the concealed text into the model prompt, where it is read as an instruction and obeyed. This is indirect prompt injection, listed as LLM01:2025 by OWASP, and recent measurement work reports it in roughly one percent of resumes in a production screening corpus. We present ResumeShield, an open-source defense and benchmark. The defense combines three filtering stages with a fourth architectural stage that places candidate content in an explicitly fenced data channel that the operator's trusted instructions declare inert. The benchmark builds a seeded synthetic corpus spanning nine concealment techniques and two payload families, one using documented phrasings and one modeling an adaptive attacker who paraphrases around the filter, and it scores an attack as successful only when the screening outcome changes. On a corpus of 104 documents, the naive pipeline is manipulated in every injected case while the defended pipeline is never manipulated. Detection reaches a precision of 1.000 and a recall of 0.944 with no false positives on clean resumes. An ablation shows that channel separation alone removes all measured attack success, whereas the complete filtering stack without separation still leaves 16.7 percent of attacks effective. We also identify a concealment dilemma: every payload that evaded detection was one the attacker left visible, surrendering the invisibility that motivates the attack. ResumeShield is released under the Apache 2.0 license with synthetic data only.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
