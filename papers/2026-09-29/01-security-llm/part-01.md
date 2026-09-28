# 🔐 大模型安全相关研究 | 2026年09月29日

> 本类共 **7** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Prompt Injection Detection for Email Agents Through Attack Chain Modeling](https://arxiv.org/abs/2609.30657)

**<font color=#1a73e8>作者：</font>** Ahmad Hashmi, Dhyey Patel, Yunting Yin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model email assistants are particularly vulnerable to indirect prompt injection because untrusted email content can be retrieved into the model context and influence subsequent tool use. Existing prompt injection detectors mainly formulate this problem as binary malicious text classification, which overlooks the important factor that harmful agent behavior often arises through a sequence of stages. We propose a detection framework that models this attack chain by combining a text detector, verifiers specific to each stage, explicit rule-based risk signals, user intent and action consistency analysis, and a logistic decision policy. To support this framework, we derive attack chain labels from prompt injection datasets, evaluate the proposed framework under random splits, temporal phase transfer, conditional stage transfer, cross-dataset transfer, and conduct ablation studies on multiple benchmarks. Results show that random train test splits substantially overestimate robustness under distribution shift, while later tool argument stages are more predictable than earlier stages in the framework. We also show that training on harmless emails that resemble attacks helps reduce false alarms while preserving the ability to detect real attacks. Across five binary benchmarks, our framework achieves a mean F1 score of 0.406 under the strict threshold setting policy, compared with 0.216 for the strongest of five pretrained detectors evaluated without additional training. These results highlight the value of combining attack stage predictions with checks for conflicts between the user's request and instructions in retrieved emails. Our experiments also demonstrate the importance of training with challenging benign examples to balance attack detection and false alarms.

---


### 2. [Understanding the Role of Prompt Template in Knowledge Distillation for Safety Alignment](https://arxiv.org/abs/2609.30802)

**<font color=#1a73e8>作者：</font>** Anjila Budathoki, Manish Dhakal, Benjamin M. Ampel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prior research has demonstrated that the choice of prompt template during Supervised Fine-Tuning (SFT) significantly impacts the robustness of safety alignment afterwards. However, the influence of template selection during Knowledge Distillation (KD) from teacher to student remains largely unexplored. Thus, we fill this gap by analyzing how different template configurations influence the pre-existing safety alignment of the student. We observe a significant degradation of safety alignment present in the aligned base instruct-tuned model. Specifically, we find that utilizing chat templates renders the model more compliant with harmful queries compared to a non-chat template. These findings are consistent across three models: LLaMA, Gemma and Qwen model families and are evaluated across multiple safety benchmarks. We further show that using a non-chat template during distillation better preserves the base student's internal representations, while chat template distillation induces a larger representational shift. Code: this https URL

---


### 3. [AGATE: Provenance-Based Runtime Defense Against Compositional Attacks on LLM Agents](https://arxiv.org/abs/2609.30830)

**<font color=#1a73e8>作者：</font>** Xiaorui Zhang, Zhuoran Cheng, Kailin Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents can produce harmful effects through sequences of ordinary operations. Judging such actions requires establishing both the authority that permits them and the origin of the data they carry. We present AGATE, an authorization and data-provenance gate at instrumented agent-harness boundaries. Operator declarations and host approval events ground authorization; delegated actions are constrained by grants that bind to exact parameters, expire, and permit a limited number of uses. Source registration connects observed inputs to subsequent transfers, while an effect ledger tracks repeated requests. Deterministic checks make decisions without an LLM in the decision path and retain their grounds with execution evidence for forensic replay. Adapters integrate three production harnesses -- DeepSeek Harness, OpenCode, and OpenClaw -- without modifying host code, translating each host's native observation and veto points into a single shared gate interface; the judgment core is identical in all three, and only enforcement depth differs. Our evaluation combines 153 exercised attack-chain records with deployment, utility, and reconstruction experiments. The deployment observations expose how tool declarations and data checks govern business actions, including a bypass through parameter rewriting. Six of eleven benign file-processing scenarios contain denial events, revealing the utility cost of content-based provenance policies. Across 252 runs on 63 sanitized scenarios, replay agrees with live graph projections for all 63 scenarios on each of two platforms. These results establish the feasibility of provenance-based runtime judgment and identify content transformation, legitimate reuse, and observation coverage as concrete limits.

---


### 4. [Why Jailbreaks Succeed in Diffusion Language Models: An Energy Landscape Analysis](https://arxiv.org/abs/2609.30841)

**<font color=#1a73e8>作者：</font>** Thong Bach, Dung Nguyen, Thao Minh Le 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing attacks and defenses for diffusion-based large language models (dLLMs) target specific vulnerabilities but lack a shared framework explaining why attacks succeed. We propose one by interpreting safety alignment as shaping the denoising energy landscape: a well-aligned model routes harmful queries toward safe outputs through an energy barrier that separates the two regions. Current jailbreak attacks reduce to two strategies for circumventing this barrier: obscuring the query's safety disposition at initialisation, or intervening mid-trajectory to force the denoising path across the energy barrier. From this perspective and the result that masked diffusion models minimise kinetic energy during denoising, we derive three complementary, training-free detection signals: a step-0 ratio that reads the initial safety disposition from the logit distribution before generation begins, and two trajectory-velocity signals that track kinetic energy in complementary subspaces of the logit space. An attack must either reveal its intent at initialisation or expend kinetic energy to cross the barrier in at least one monitored subspace, so the three signals cover each other's blind spots in the energy budget by construction. Evaluation across three dense dLLMs (LLaDA-8B, LLaDA-1.5, Dream-7B) and a sparse mixture-of-experts dLLM (LLaDA-MoE-7B) confirms this complementarity. In stress tests of known attacks, every configuration that evades detection also fails to produce harmful content, suggesting that the detection and barrier-crossing thresholds are hard to separate.

---


### 5. [CG-Probes: Recovering Guardrail Directions from Patient Query Embeddings](https://arxiv.org/abs/2609.31062)

**<font color=#1a73e8>作者：</font>** Marko Řeháček, Vítězslav Dušek, Martin Rusinko 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Patient-facing AI assistants promise valuable support to patients, but incoming queries can pose medical risks. To create guardrails, we work with oncologists to define three ordinal risk axes: Medical Urgency, Psychological Urgency, and Topic Sensitivity. We propose Clinical Guardrail Probes (CG-Probes) to measure the risks from query embeddings. We probe for each axis in the normalized embedding space of frozen embedders via the difference-in-means method, treating each axis as a potential linear direction. To train the probes, we cluster 79,658 Czech oncology search queries with BERTopic and use these clusters to generate pairs of queries with contrastive risk levels via few-shot prompting. We evaluate the approach on 200 queries (90 real, 110 synthetic), each graded by two oncologists, against two open-weight LLMs and a frontier LLM. We find that urgency-based axes are recoverable as linear directions, and the probes are competitive with open-weight LLMs (no significant differences in quadratic-weighted kappa) at a fraction of the latency. Each axis yields a scalar score that clinicians can inspect and use to set escalation thresholds. The pipeline requires only search logs, axis definitions, and black-box access to the embedding model, suggesting transferability across healthcare domains. Robust validation on new queries and axes remains future work.

---


### 6. [AgentXploit: Autonomous Repository-to-Runtime Red-Teaming for AI Agents](https://arxiv.org/abs/2609.31318)

**<font color=#1a73e8>作者：</font>** Weida Liang, Shi Qiu, Zhun Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents combine language models with external data and tools that can modify files, call APIs, or execute code. Security failures can arise when adversarial content changes an agent's tool use or when the surrounding software contains vulnerabilities such as path traversal or command injection. We study authorized white-box pre-deployment auditing, where the auditor has access to the target repository and a controlled runtime, but successful attacks must still act through the task-defined attacker interface and be confirmed by an external verifier. We present AgentXploit, a two-role auditing system that separates repository-level attack-path discovery from runtime exploitation. The Analyzer Agent traces attacker-controlled inputs to sensitive operations and records code-supported candidate attack paths; the Exploiter Agent turns these paths into concrete attacks and revises them using runtime feedback. We also introduce AgentXploit-Bench, containing 72 reproducible vulnerabilities across 12 open-source AI-agent systems and frameworks. Across three runs, AgentXploit reaches 59.3% end-to-end success, compared with 38.4% for Codex. Under a token-budget-matched comparison, Codex reaches 46.3%. On AgentDojo, where injection points are provided, the Exploiter Agent reaches 79.2% attack success versus 52.7% for AgentVigil. These results highlight repository discovery and runtime exploitation as distinct challenges in end-to-end agent security auditing.

---


### 7. [Stale-Document Poisoning: When Outdated Retrieval Overrides Correct Model Answers](https://arxiv.org/abs/2609.31342)

**<font color=#1a73e8>作者：</font>** Md Shamim Ahmed, Lukas Galke Poech, Richard Röttger  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) is often used to address outdated knowledge by providing external evidence. But retrieval helps only when that evidence is still valid. We identify a temporal alignment failure, stale-document poisoning, in which outdated evidence makes a model wrong despite answering correctly without retrieval. We construct a benchmark of 317 verified knowledge reversals across medicine, law, software, and platform policy, grounded in dated official sources. Across 12 models, recent medical reversals are harder than long-established ones. More importantly, outdated retrieval flips 30% of Llama and 37% of Qwen answers even without instructions to trust the document; explicit follow instructions raise these rates to 66% and 75%. Across four open models and four domains, poisoning ranges from 17-91%, while matched up-to-date evidence is followed in 97-100% of trials. To isolate temporal applicability, we keep the historical evidence unchanged across 50 reversals and vary only the evaluation date. A clear pattern emerges: dates alone produce only modest adaptation, but when models are explicitly told when the old evidence stops applying, the larger models switch to the appropriate answer almost perfectly. Causal interventions confirm that this validity information directly shapes the final decision. The same internal components also support broader comparison tasks, suggesting that temporal applicability can recruit a general reasoning mechanism used for other comparisons. Finally, a fixed recency-aware hybrid re-ranker reduces poisoning by 4.6-10.0 points when dates are accurate, with gains that depend on reliable temporal metadata. Reliable RAG therefore requires selective trust: models must determine not only what retrieved evidence says, but whether it still applies.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
