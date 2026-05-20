# 🔐 大模型安全相关研究 | 2026年05月21日

> 本类共 **9** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [DarkLLM: Learning Language-Driven Adversarial Attacks with Large Language Models](https://arxiv.org/abs/2605.18868)

**<font color=#1a73e8>作者：</font>** Ye Sun, Xin Wang, Jiaming Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> While vision and multimodal foundation models underpin critical tasks from perception to complex reasoning, they remain highly vulnerable to adversarial attacks. However, traditional adversarial attacks are typically limited to single, predefined objectives, tightly coupling each attack to a specific model or task, which restricts their scalability and flexibility in real-world scenarios. In this work, we present DarkLLM, a novel attack framework that trains an LLM to translate natural-language attack instructions into latent attack vectors, which are then decoded into visual adversarial perturbations. By leveraging natural-language instruction tuning, DarkLLM not only unifies targeted, untargeted, segmentation, and multi-model attacks within a single framework, but also achieves flexible and controllable adversarial generation, enabling each instruction to produce a perturbation that induces desired behaviors across heterogeneous models. Through extensive experiments across 4 tasks, 13 datasets, and 15 models, we demonstrate that DarkLLM with only 1B parameters can follow attacker instructions and generate highly effective attacks against CLIP, SAM, and frontier LLMs, revealing a systemic vulnerability in modern foundation models.

---


### 2. [DMN: A Compositional Framework for Jailbreaking Multimodal LLMs with Multi-Image Inputs](https://arxiv.org/abs/2605.18915)

**<font color=#1a73e8>作者：</font>** Wenzhuo Xu, Zhipeng Wei, Zonghao Ying 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) are vulnerable to jailbreak attacks, which can elicit harmful responses from MLLMs. Many MLLMs support multi-image inputs, inadvertently introducing new vulnerabilities due to less efforts on multi-image safety alignment. Previous MLLM jailbreak methods only uses a single image, which restricts the attack space: they cannot distribute harmful requests across multiple images, carry abundant information, or exploit additional visual reasoning tasks to distract MLLMs. To address these limitations, in this paper, we propose a compositional jailbreak framework, \textbf{DMN}, which leverages \textbf{D}istributed instruction, \textbf{M}ultimodal evidence and a \textbf{N}umber chain task to fully enhance the jailbreak performance. Extensive experiments show that DMN is highly effective for MLLM jailbreaking, e.g. achieving attack success rates of over 90\% on GPT-4o, Gemini-2.5-pro and Claude Sonnet 4, surpassing other baselines by a large margin. This compositional, multi-image jailbreak strategy reveals fundamental weaknesses in their safety mechanisms.

---


### 3. [OEP: Poisoning Self-Evolving LLM Agents via Locally Correct but Non-Transferable Experiences](https://arxiv.org/abs/2605.18930)

**<font color=#1a73e8>作者：</font>** Kaixiang Wang, Jiong Lou, Zhaojiacheng Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Memory-augmented large language model (LLM) agents use iterative reflection and self-evolution to solve complex tasks, but these mechanisms introduce security risks. Existing agentic memory attacks require privileged access or explicit malicious content, making them detectable by advanced safety filters. This leaves a subtler attack surface underexplored: whether adversaries can induce agent to generate experiences that appear locally correct and semantically plausible yet induce harmful generalization during reflection. We find that reflective agents are vulnerable to such clean experiences, especially when paired with severe but plausible hypothetical consequences. Based on this observation, we introduce Obsessive Experience Poisoning (OEP), a low-privilege black-box attack requiring no direct control over the system prompt or memory database. OEP constructs adversarial clean edge-cases that combine locally correct solutions, non-transferable methods, and severe consequences, biasing reflection toward risk-averse rule formation. During memory consolidation, agents may over-trust self-generated reflections and distill localized experiences into high-priority but over-generalized rules, causing downstream failures. Evaluations across three domains show that OEP achieves ASR above 50\% with GPT-4o agents, and outperforms existing attacks under LLM auditing defense.

---


### 4. [Surviving the Unseen: Predictive Defense for Novel Multi-Turn Multimodal Attacks](https://arxiv.org/abs/2605.18988)

**<font color=#1a73e8>作者：</font>** Doohee You  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The expansion of Multimodal Large Language Models (MLLMs) and their integration into autonomous agentic workflows has introduced a non-stationary attack surface. Empirical observations indicate that adversaries employ progressive, cross-modal perturbations that evade turn-specific guardrails by distributing malicious intent across longitudinal conversational trajectories. Static defense mechanisms, constrained by the Markov property, evaluate inputs in isolation and fail to detect cumulative structural poisoning. To handle this limitation, this paper formulates safety verification as a dynamic survival prediction and trajectory dynamics problem. The Triple-tier Anomaly Defense (TRIAD) framework is proposed as a predictive model that maps multimodal and multi-turn conversational flow as a continuous trajectory. The framework integrates structural anomaly detection to monitor covariance shifts, a Ledoit-Wolf regularized Mahalanobis distance to monitor covariance shifts in high-dimensional spaces, and topological trajectory acceleration to differentiate benign creative exploration from continuous malicious drift. These kinematic and geometric features are integrated into a time-varying Cox Proportional Hazards model via a Bayesian Hidden Markov Model (HMM) feedback loop. Theoretical analysis demonstrates that the TRIAD framework provides a mathematically bounded expected time-to-failure under adversarial perturbations, ensuring that malicious acceleration diverges positively. This framework provides a computationally efficient, interpretable, and predictive safeguard for real-time agentic AI systems, establishing a rigorous foundation for continuous safety alignment without relying on empirical retraining.

---


### 5. [Be Kind, Rewrite: Benign Projections via Rewriting Defend Against LLM Data Poisoning Attacks](https://arxiv.org/abs/2605.19147)

**<font color=#1a73e8>作者：</font>** John T. Halloran, Noopur S. Bhatt  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are highly susceptible to backdoor attacks (BAs), wherein training samples are poisoned using trigger-based harmful content. Furthermore, existing defenses have proven ineffective when extensively tested across BA patterns. To better combat BAs, we explore the use of LLM rewriting as a proactive defense against data poisoning. First, we theoretically show that when LLM rewriting utilizes open-book benign samples--termed open-book benign rewriting (OBBR)--the probability of a rewritten output being benign is strictly greater than that of closed-book rewriting. Thus, OBBR neutralizes harmful content by projecting training samples to the space of benign prompts. We then show that, in contrast to previous defenses, OBBR effectively mitigates a large number of existing BAs: across five known BAs and four widely used LLMs, OBBR increases safety performance by an average 51% compared to state-of-the-art BA defenses and 25.7% compared to closed-book rewriting methods. Finally, we show that OBBR is computationally efficient relative to other BA defenses, does not degrade model performance on natural language tasks after fine-tuning, and is capable of defending against non-trigger based data poisoning attacks.

---


### 6. [Exploring and Developing a Pre-Model Safeguard with Draft Models](https://arxiv.org/abs/2605.19321)

**<font color=#1a73e8>作者：</font>** Hongyu Cai, Arjun Arunasalam, Yiming Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) alignment remains vulnerable to jailbreak attacks that elicit unsafe responses, motivating pre-model and post-model guards. Pre-model guards audit the safety of prompts before invoking target models. However, relying solely on the prompt often leads to high false-negative rates (i.e., jailbreak attacks go undetected). Post-model guards address this issue by auditing both the user prompt and the target model's response. However, they incur a high computational cost, including increased token usage and processing time, because they operate after target model inference.
In this paper, we introduce a safeguard design that leverages the transferability of jailbreak attacks to enforce prompt safety before target model inference. We first conduct a systematic study of jailbreak transferability, particularly from LLMs to small language models (SLMs). Through these experiments, we identify key factors influencing transferability. Building on these insights, we observe that responses from smaller draft models reflect the safety implications of those from large target models; \ie given a jailbreak prompt constructed for an LLM, an SLM is likely to be triggered to generate an unaligned response. Based on this observation, our safeguard design leverages speculative inference with SLMs to generate a set of draft responses. It then feeds the original prompt and these drafts into existing guards to predict their safety. We demonstrate that this design reduces the false-negative rate of pre-model guards and offers a low \Efficiency alternative to post-model guards. \textcolor{red}{\bf Notice: This paper contains examples of harmful language.}

---


### 7. [Measuring Safety Alignment Effects in Autonomous Security Agents](https://arxiv.org/abs/2605.19722)

**<font color=#1a73e8>作者：</font>** Isaac David, Arthur Gervais  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Do stock safety-aligned language models and their uncensored or abliterated derivatives behave differently when run as autonomous security agents? Single-turn refusal benchmarks cannot answer this question: security agents must inspect repositories, call tools, and produce vulnerability evidence inside authorized sandboxes.
We present a trace-based benchmark of 30 local vulnerability-analysis tasks with fixed tools, deterministic success predicates, redaction rules, and grounding checks, and compare four stock models against uncensored or abliterated derivatives: Gemma 4 31B, Gemma 4 26B A4B, Qwen2.5-Coder 7B, and Llama 3.1 8B. The artifact contains 1,500 security-agent traces and 800 non-security control traces. The Gemma pairs show large less-restricted gains on security tasks: 14.0% versus 0.7% success for 31B and 10.7% versus 0.0% for 26B, with higher mean grounding (3.91 versus 3.27 and 4.12 versus 1.64 out of five) and 0.0% refusal, suppressed-action, and unsafe-action rates in the 31B traces. However, controls and non-Gemma pairs rule out a clean security-specific or universal less-restricted effect: Gemma gaps also appear on ordinary coding tasks, Qwen2.5-Coder success is lower for the less-restricted derivative (2.0% versus 5.3%), and the abliterated Llama derivative fails the tool protocol. Across all families, hard proof-of-trigger and patch-verification tasks remain unsolved. These results show that safety alignment effects in autonomous security agents should be measured at the system level, separating refusal, unsafe action, tool reliability, and evidence grounding rather than treating refusal rate as the safety signal.

---


### 8. [Auditing Privacy in Multi-Tenant RAG under Account Collusion](https://arxiv.org/abs/2605.19847)

**<font color=#1a73e8>作者：</font>** Florian A. D. Burnat, Brittany I. Davidson  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multi-tenant retrieval-augmented generation (RAG) services advertise per-account differential privacy as the operative leakage boundary: each account's queries are guaranteed to satisfy $(\varepsilon_{\text{acc}}, \delta_{\text{acc}})$-DP with respect to the index. We identify same-index multi-account collusion as a privacy-boundary failure: for $k$ same-tenant accounts coordinating against the tenant's index -- the operative regime -- known DP composition theory implies joint leakage degrades unconditionally at rate $\Theta(\sqrt{k} \cdot \varepsilon_{\text{acc}})$ for Gaussian-noised retrieval. Cross-tenant and external collusion match the rate only under explicit access-control failure (M4); without M4 these regimes have zero leakage by design and reduce to an architectural audit, not a DP audit. We exhibit an attack realizing the rate and derive a RAG-specific MIA prediction we test empirically. To make this per-account/joint gap auditable, we design the first audit protocol that operates against unmodified RAG deployments and issues a quantitative $(\textsf{PASS}, \varepsilon_{\text{audit}})$ verdict for the retrieval-score channel -- the noise-then-select step the per-account DP guarantee actually covers -- without index disclosure, pipeline redesign, or model-weight exposure. Generation-channel privacy (LLM output conditioned on selected documents) is a separate audit predicate that should compose with ours; we explicitly scope it out. The protocol composes generic cryptographic primitives (Merkle ledgers, ZK function-application proofs, Gaussian noise attestations) with six RAG-specific primitives (embedder commitment, index-content vector commitment, per-account query ledger, noise-then-select attestation, cross-tenant containment proof, coalition-size estimator) and supports both closed-form audit bounds and Rényi-DP moments-accountant tracking.

---


### 9. [BiRD: A Bidirectional Ranking Defense Mechanism for Retrieval Augmented Generation](https://arxiv.org/abs/2605.20123)

**<font color=#1a73e8>作者：</font>** Chengcai Gao, Zhihong Sun, Xiaochuan Shi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The growing adoption of Retrieval-Augmented Generation (RAG) has led to a rise in adversarial attacks. Existing defenses, relying on semantic analysis or voting, face a trade-off between high computational cost and limited robustness under strong poisoning attacks. Their fundamental limitation is the exclusive focus on semantic content relevance, while neglecting the retrieval context that is critically defined by ranking structures. To this end, we investigate the bidirectional ranking behavior of poisoned and benign documents, and discover a key discriminative pattern: poisoned documents exhibit significantly stronger alignment between their backward rankings and the query's forward ranking. Capitalizing on this, we propose BiRD, a bidirectional ranking defense mechanism built upon a dual-signal framework that leverages forward ranking to assess semantic content relevance and backward ranking to quantify ranking context consistency. This design directly addresses the fundamental limitation of prior approaches, enabling simultaneous efficiency and robustness. Extensive evaluation across 3 datasets with 3 retrievers and 3 LLMs under 2 attack scenarios validates BiRD's effectiveness. Notably, BiRD reduces the attack success rate of PoisonedRAG by up to 54% while simultaneously improving task accuracy by up to 56%, with average additional latency under 1 second.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
