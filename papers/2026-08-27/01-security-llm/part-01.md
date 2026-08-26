# 🔐 大模型安全相关研究 | 2026年08月27日

> 本类共 **6** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Semantic Overlays: Mitigating Prompt Injection with Annotations Beyond Tokens and Steering Vectors](https://arxiv.org/abs/2608.23873)

**<font color=#1a73e8>作者：</font>** Joshua Penman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Everything a language model sees is tokens. The serving stack knows what each span is -- user input, tool output, instructions -- but the model must keep track of that itself, and it can lose track or be confused: text can be written to read like anything. Prompt injection is a natural exploit of this phenomenon. By scrambling the model's understanding of span identity, an attacker can induce unwanted and potentially dangerous actions. Adding a non-textual channel to the model's input -- a way to communicate span identity beyond text -- mitigates this class of attack. We thus introduce a general steering technique called Semantic Overlays: small learned adapters applied at chosen prefill positions to a frozen model's residual stream. Laying an overlay over a span creates an out-of-band annotation channel that cannot be replicated by tokens. Unlike steering vectors, Semantic Overlays are trained, adaptable, and selectively applied. An overlay can encode complex semantics that reshape how the model perceives the marked span: asked to copy a code snippet under an overlay asserting that it is in a different programming language than it is, the model rewrites the snippet, faithfully, in the asserted language. Overlays are also composable, allow for transparent reading of underlying content, and can carry complex payloads -- including imperatives that the model will follow. An overlay which marks a span as "non-executable" defends against the broad class of prompt injections that add instructions in untrusted context. We report strong results on prompt injection benchmarks: SEP separation rises from 24.3% to 96.5% with utility unchanged (our scoring rule; we also correct a defect in the published grader), TensorTrust attack success rate falls from 34.8% to 6.6%, and all four PIArena attack families drop to 0% compliance, all while marked spans stay readable (92.5% exact copy rate).

---


### 2. [NeuronGuard: Robust LLM Safety Alignment via Ablation-Aware Safety Signal Redistribution](https://arxiv.org/abs/2608.23959)

**<font color=#1a73e8>作者：</font>** Anjun Gao, Yueyang Quan, Yufei Xia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Safety alignment in large language models (LLMs) remains brittle against a growing spectrum of attacks. Jailbreak attacks bypass safety mechanisms through crafted prompts, while neuron-level attacks directly prune safety-critical neurons post-deployment. Both exploit a common weakness: safety-relevant information concentrates in a sparse neuron subset. We present NeuronGuard, a fine-tuning-stage defense that simultaneously hardens LLMs against both attack classes by redistributing safety signals across a broader set of neurons. NeuronGuard dynamically identifies safety-critical neurons via periodically refreshed per-layer linear classifiers, forces refusal behavior under deliberate neuron ablation, and applies KL-divergence regularization for distributional consistency. A randomized gradient projection strategy preserves downstream task utility by resolving conflicts between the defense and task objectives. We provide a formal guarantee that NeuronGuard strictly reduces the attack success rate (ASR) upper bound, and experiments across three LLMs, six state-of-the-art attack strategies, and multimodal settings confirm near-zero ASR while maintaining task accuracy, including against white-box adaptive adversaries.

---


### 3. [What Guides the Agent? Adjudicating Unauthorized Behavior via Localizing Behavior-Guiding Instructions](https://arxiv.org/abs/2608.24022)

**<font color=#1a73e8>作者：</font>** Yichao Gao, Yumo Zhang, Yunhao Yao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents integrated with external resources gain complex task capabilities, yet the unified natural-language context channel makes them vulnerable to injection attacks: untrusted external data may be dynamically parsed as behavior-guiding instructions during LLM inference, thereby subverting the agent's decision. Existing defenses focus on static detection or isolation of malicious content at the input/output level, remains insufficient for detecting such dynamic inducements that arise during model reasoning. We propose Attnlocate, a runtime framework for fine-grained localization of context spans that genuinely influence tool-calling decisions, i.e., behavior-guiding instructions. Attnlocate casts this localization problem as an object detection task, aiming to detect the distinctive activation traces induced by behavior-guiding instructions within the attention matrix. Specifically, we design a multi-head, multi-layer attention aggregation scheme to construct a token-level feature space tailored for object detection. Then, a 1-D U-Net equipped with an anchor-free detection head is deployed to detect these spans. Finally, based on the authority of the provider from which the detected behavior-guiding spans originate, Attnlocate dynamically adjudicates malicious invocation attempts. We evaluate Attnlocate across ten agent configurations from five LLM families, covering scenarios involving indirect prompt injection and tool poisoning. Attnlocate achieves a mean IoU of 0.743, an average AUROC of 0.956, and a 0.934 true-positive rate at 0.067 false-positive rate. It also transfers effectively across unseen models and supports authority policy adaptation without retraining.

---


### 4. [TrustDABench: Benchmarking Reliability and Robustness of LLMs for Structured Data Analysis](https://arxiv.org/abs/2608.24145)

**<font color=#1a73e8>作者：</font>** Boshen Shi, Yize Liu, Chen Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly used to analyze spreadsheets, CSV files, and other structured data, but producing a correct-looking answer is not the same as producing a trustworthy analysis. A trustworthy result should be supported by a valid path from the user question to the relevant data evidence. This requirement creates two diagnostic questions: whether an LLM can refuse to answer or ask for clarification when such a path does not exist, and whether it can preserve the correct analysis when the same evidence is expressed in different table forms. We introduce TrustDABench, a benchmark that operationalizes these questions as reliability and robustness. Starting from the evidence-path view, we derive 19 perturbation operators and instantiate them through an Agentic-LLM-based generation framework. TrustDABench contains 2,340 human-verified perturbed instances, and we evaluate eight representative LLMs. The results show substantial headroom: the best reliability result is only 24.21% average MRS, achieved by GPT-5.5, while the best robustness result still has 9.10% average ASR, achieved by Claude-Sonnet-5. The failures are systematic: models rarely detect conflicting evidence, often continue along executable but unsupported analysis paths, and remain sensitive to perturbations that change observation boundaries or cross-table relations. These findings suggest that stronger evidence-boundary recognition and representation-invariant reasoning are still needed for reliable structured-data analysis.

---


### 5. [Not All Tokens Are Equal: Region-Aware Consistency Repair of Backdoors in MLLMs](https://arxiv.org/abs/2608.24354)

**<font color=#1a73e8>作者：</font>** Jiali Wei, Ming Fan, Mingkun Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> MLLMs are increasingly deployed in user-facing applications, yet they inherit backdoor risks from the pipelines used to construct them: triggers may reside in images, texts, or both. Existing model-level backdoor removal methods, largely designed for conventional classifiers, show limited effectiveness on MLLMs, while MLLM-specific defenses mainly operate at inference time, filtering suspicious inputs without removing the backdoor embedded in the model. To address this gap and eliminate latent backdoors from MLLMs at their source, we present RACER, a model-level repair framework motivated by a key observation: backdoors induce abnormal layer-to-layer evolution in internal representations, which we term the layer-wise inconsistency anomaly. Importantly, this anomaly is modality-dependent, concentrating primarily in the token region encoding the trigger features that the backdoor model actually relies on. RACER therefore decomposes the fused representation into visual and textual token regions, normalizes their layer-wise inconsistency separately, and recomposes them using modality-aware weights over a deep-layer window, yielding a region-aware inconsistency objective that better captures localized backdoor-induced anomalies. Through a min-max optimization, this objective drives worst-case perturbation synthesis and adversarial fine-tuning against the resulting perturbation to repair the model, suppressing the deep representational directional shifts on which backdoor behaviors rely. RACER requires only 100 clean samples and no knowledge of the trigger, attack objective, or even whether the input model contains a backdoor. Evaluations on three open-source MLLMs across 36 backdoor settings spanning image, text, and multimodal triggers show that RACER reduces the average ASR to 1.1%, reaching 0% in 32 settings, while preserving clean-task utility on both backdoor and clean models.

---


### 6. [StepGuard: Learning Step-Level Guardrails with Scalable Supervision and Safety-Utility Balancing](https://arxiv.org/abs/2608.24777)

**<font color=#1a73e8>作者：</font>** Zhijie Zheng, Yu Li, Chen Qian 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based agents can interact with external environments through tool invocation, but this capability also introduces security risks such as file modification, information leakage, and unauthorized actions. Existing guardrails often evaluate completed trajectories, leaving pre-execution monitoring of step-level actions underexplored. We propose StepGuard, a step-level guard model that can audit completed agent trajectories and check tool actions before they are executed. To train StepGuard, we introduce StepGen, an automatic data engine that generates safe and unsafe trajectories with the same context but different actions at the risky step. To further reduce over-defense and under-defense, we propose Balance-GRPO, which dynamically balances learning between safe and unsafe actions based on their observed accuracy. Experiments show that StepGuard achieves the highest average accuracy among open-weight guard models, with performance comparable to GPT-5.4. When used to guard agents on AgentDojo and AgentDyn, StepGuard reduces mean attack success rate by 77.3% relative to the no-guard setting, while mean utility drops by only 2.8 percentage points.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
