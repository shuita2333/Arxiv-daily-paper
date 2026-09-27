# 🔐 大模型安全相关研究 | 2026年09月28日

> 本类共 **4** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Decision Hijacking: Prompt Injection Attacks on Jev's Typed Probabilistic Decisions](https://arxiv.org/abs/2609.28613)

**<font color=#1a73e8>作者：</font>** Tiantong Wu, Wei Yang Bryan Lim  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Most studies of prompt injection focus on generative agents, leaving their effects on models with schema-defined outputs unclear. We examine these effects in Jev, a non-generative decision model, using 510 reconstructed InjecAgent cases. Malicious content shifts action probabilities but rarely causes Jev to select the attacker's target. Override markers reduce this influence, while claims of contextual relatedness have small effects. Adaptive attacks using score feedback double the mean highest attacker-target probability found during optimization, while success on fresh validation calls rises from 1.8% to 3.5%. Exploratory analysis links these successes to small initial decision margins or greater attacker control over the observation. Together, these findings show that schema-defined outputs change but do not eliminate prompt-injection risk, highlighting the need to evaluate how untrusted content influences choices within the allowed action set.

---


### 2. [On the Effectiveness of Kernel-Level Evidence for Agent Security](https://arxiv.org/abs/2609.28915)

**<font color=#1a73e8>作者：</font>** Spencer King, Zhilu Zhang, Mikhail Kuznetsov 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents are deployed into infrastructure that grants them broad host authority, yet existing agent-security benchmarks and defenses operate almost exclusively at the application telemetry layer: the served tool manifest, the user prompt, and the model's messages. Some threats, however, smuggle malicious instructions and actions past the application boundary, leaving them invisible to that layer. In this work, we bridge that gap by pairing application-level agent telemetry with kernel-level syscall traces to present the first paired-evidence characterization of kernel-level versus application-layer signal for agent security. To quantify the value of the enhanced telemetry, we introduce Agent Cross-Layer Evidence (ACE), a paired-session corpus of 4,047 sessions and 17 threat models spanning six delivery-vector families and 14 of the 25 OWASP LLM and agentic threat categories, organized into 12 attack mechanics with per-mechanic characterization of where the most discriminative evidence lies. Across four distinct detector families, we find that kernel evidence is discriminative on its own and that composing it with application-layer evidence generally outperforms either single-layer view, revealing complementary signals that single-layer analyses can miss. We further demonstrate generalization to unseen attack families and transfer to an alternate agent runtime. Together, these findings establish the value of cross-layer evidence for agent security.

---


### 3. [Just Ask Jev: Reinforcement Learning for Calibrated Decisions as a Zero-Shot Detector of AI Alignment Failures](https://arxiv.org/abs/2609.29429)

**<font color=#1a73e8>作者：</font>** Ruoqi Guo, Yi Liu, Gelei Deng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Detectors of alignment failures screen deployed language models and score alignment benchmarks. Most are generative judges that spend a decoding pass on every criterion, and classifiers that read token probabilities, such as Llama Guard, still score one fixed label per call. Jev, a model trained with reinforcement learning for calibrated decisions (RLCD), answers many typed questions about one input with calibrated probabilities in a single call. Whether it detects alignment failures has not been measured. We present RLCDAlignBench, which benchmarks Jev on ten alignment failures: sycophancy, jailbreaks, deception, prompt injection, hallucination, privacy violation, social bias, reward hacking, concealing uncertainty, and power seeking. It spans 44 benchmarks and five target models, labelled by each benchmark's scorer and, on two, by humans. Many of these failures are relational, defined against a reference, such as the user's belief or an injected instruction, that the response alone does not reveal. Our key idea is therefore to vary what Jev is asked separately from what it sees: the question's wording and answer type on one side, the fields of the input on the other. A single generic question reaches a median AUROC of 0.886 zero-shot and beats supervised baselines on most benchmarks. Question wording matters little, while context matters more, mostly through fields that encode the label. Jev matches the reference scorer's agreement with human labels, surfaces label defects in existing benchmarks, and costs 63x less than LLM-judge scorers. Code and data: this https URL.

---


### 4. [Prefilling the Reasoning Channel: Output-Prefix Attacks on Reasoning LLMs](https://arxiv.org/abs/2609.29775)

**<font color=#1a73e8>作者：</font>** Lukáš Brůna, Robert Bridges, Adam Ek  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) consume and produce a single sequence of text; hence, if text can be added to the beginning of the LLM's response, i.e., an output prefix, then all subsequent tokens will be conditioned on it. This output-prefix attack technique is a cheap black-box prompt injection. Prior work has shown this type of attack can reliably jailbreak non-reasoning models. Most reasoning models add an intermediate scratchpad reasoning step before the assistant's final response. The ability to edit this reasoning channel is exposed by some APIs and attack vectors can be leveraged for reasoning injection attacks. We present the first systematic, controlled study that isolates the scratchpad reasoning channel as an output-prefix attack vector, and the first to compare reasoning-only, output-prefix-only and reasoning-plus-output-prefix attacks across both exposed- and hidden-reasoning models. Using a factorial design of 3 prefix types $\times$ 2 reasoning injections over $1{,}800$ test cases drawn from AdvBench, we attack three 2026-era frontier models Gemini 3 Flash Preview, DeepSeek V4 Flash, and Claude Haiku 4.5. We find that injecting malicious reasoning alone is essentially inert ($\approx0\%$ attack success), but injecting the same reasoning together with a trivial output prefix raises the attack success rate to as high as $99\%$ for some models. For this type of attack we find that contextual prefixes work better than static prefixes; and that susceptibility is dependent on the model.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
