# 🔐 大模型安全相关研究 | 2026年09月23日

> 本类共 **9** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Context Poisoning as Extreme-Value Attention Interference in Long-Context Language Models](https://arxiv.org/abs/2609.22101)

**<font color=#1a73e8>作者：</font>** Meysam Ghaffari, Nina Fatehi, Bhaskar Sen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models can process increasingly long prompts, yet their ability to locate and use decisive evidence may degrade as irrelevant or confusable context is added. We formulate this phenomenon, which we call context poisoning, as extreme-value interference in attention: the decisive-evidence score is upper-bounded, while the maximum score among effective distractors grows with their number. Under a softmax retrieval abstraction, we derive a finite-sample upper bound showing that maintaining a fixed accuracy target above base rate requires the evidence margin to scale as $\Omega(\sqrt{\log N})$, where N denotes the effective distractor count rather than necessarily the raw context length. The analysis connects long-context degradation to score aliasing, positional aliasing, and softmax dilution. Controlled experiments show that retrieval accuracy decreases as total context grows in the presence of embedded hard negatives, that the same-format condition produces the largest observed accuracy drop among the tested distractor constructions at fixed context length, and that retrieval gating can improve evidence use while its net benefit depends on preserving evidence recall. These results motivate evidence bottlenecks, alias-resistant representations, retrieve-then-reason architectures, verifier-mediated memory, and contrastive anti-poison training.

---


### 2. [Defusing Explosive Prompts: Understanding and Preventing Trigger-Based Prompt Injections in LLM Agents](https://arxiv.org/abs/2609.22510)

**<font color=#1a73e8>作者：</font>** Justin Szczepaniak, Elad Feldman, Naum Viner 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As LLM applications integrate with external tools, they are increasingly exposed to indirect prompt injection (IPI), where adversarial instructions are embedded in retrieved content. Conventional IPIs fire on contact: the moment an agent ingests the content, it carries out the instruction. We introduce the explosive prompt, a conditional payload that stays dormant until an attacker-chosen trigger is met, in effect a training-free, inference-time backdoor planted in a single piece of retrieved content.
This temporal separation reaches where ordinary IPI cannot. On frontier models that refuse the bare imperative almost entirely, rephrasing the same goal as a dormant conditional drives real, state-changing tool execution against a live agent backend (a paired mean of 16.5% vs. 2.4% for the imperative, reaching 34.2% on a proprietary model). In trials on nine production agents (OpenAI Codex, Google Gemini CLI, Anthropic Claude Code CLI, Cursor CLI, GitHub Copilot, Devin AI CLI, Amazon Kiro CLI, Qwen Code, Google Assistant; n=30 each), explosive prompts succeed in 43-83% of cases versus at most 3% for an imperative baseline, and they slip past deployed defenses: off-the-shelf injection classifiers are miscalibrated on them, and a preference-optimized model that closes imperative injection entirely still executes 11.8% of explosive prompts, every one at the trigger turn.
The durable defensive lever is ingestion-time detection of the conditional structure, once detectors are trained on explosive-prompt data, which no prior benchmark supplied and our generator does. Retraining cuts live tool-execution attack success from an undefended 34.3% to 7.5-8.1% for the encoder baselines. Our detector, DeFuse, reaches 3.0% at a calibrated 5% false-positive budget with the best detection quality of any method tested (AUC 0.9994) and 25x lower latency, though it needs length-aware thresholds.

---


### 3. [Trustworthy Agentic AI: Failure Modes, Mitigation Strategies, and a Lifecycle Framework for Autonomous LLM Systems](https://arxiv.org/abs/2609.22712)

**<font color=#1a73e8>作者：</font>** Fayeq Jeelani Syed, Rehan Ahmad, Ali Al Bataineh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI systems built on large language models can plan over multiple steps, use external tools, retain information in memory, and coordinate with other agents. These capabilities make them more useful than static language models, but they also introduce new security and operational risks. Untrusted content from websites, emails, documents, and databases can enter the same context as system instructions; persistent memory can carry compromised information across sessions; and access to external tools can turn an incorrect model response into a consequential real-world action. This article reviews the trustworthiness of agentic AI across five interconnected dimensions: safety and robustness, alignment and human oversight, transparency and auditability, privacy and data governance, and regulatory compliance. It organizes key failure modes, including indirect prompt injection, backdoor triggers, goal misgeneralization, memory contamination, and cross-session data leakage, into a unified taxonomy. It also examines major mitigation approaches, such as instruction hierarchies, context isolation, spotlighting, process-based supervision, constrained tool use, and privacy-preserving memory, while distinguishing techniques supported by empirical evidence from those that remain largely conceptual. Building on this analysis, we introduce the Trustworthy Agent Development Lifecycle (TADL), a six-phase framework covering specification, design, training, evaluation, deployment, and monitoring. For each phase, TADL identifies relevant trust activities, expected evidence, and risk-based decision gates. Although TADL has not yet been empirically validated, it provides a structured foundation for developing and evaluating more secure and accountable agentic systems. The article concludes by identifying gaps in current benchmarks and outlining priorities for future research.

---


### 4. [The Price of Safety: Benign-Case Utility and Token Overhead of Memory-Poisoning Defenses in LLM Agents](https://arxiv.org/abs/2609.22818)

**<font color=#1a73e8>作者：</font>** Pritom Bhowmik  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Memory-poisoning defenses for LLM agents are typically evaluated by their ability to prevent attacks. However, the traffic they process is rarely adversarial. The cost of implementing a defense is paid with each interaction, while its benefits are only seen in a small percentage of cases. We developed a measurement setup that keeps the memory backend, retrieval process, and judge consistent across different conditions, changing only the defense itself. We test each condition three times across five conversations to distinguish the defense's real effects from noise inherent in the pipeline's runs, which remains significant even at temperature zero. Across three write-time defenses (input sanitization, provenance checking, and LLM-based anomaly detection) and one read-time defense (reranking), tested on entirely benign traffic, the write-time defenses show no utility cost we can resolve, with 95% confidence intervals spanning roughly +/-4.5 points and including zero. The reranker is different: it lowers core accuracy by 4.4 points (95% CI [-9.0,-0.05], bootstrap; McNemar p=0.064), a result that survives replication but sits at the edge of our resolution. Its clearer cost is mechanical rather than statistical. On conversations containing no attack, the reranker quarantines legitimate memories on 33.6% of adjudicated items, reaching as many as 106 false quarantines in a single conversation, at 2.7% token overhead. Stacking all four defenses does not compound this cost: the combined condition's accuracy loss is smaller, and its confidence interval includes zero, suggesting the write-time defenses may partly offset what the reranker discards. Where a defense intercepts the pipeline, not whether it uses an LLM, appears to determine its benign-case price.

---


### 5. [Beyond Single-Model Injection: A Threat Model and Defense Architecture for Prompt Injection in Multi-Agent Systems](https://arxiv.org/abs/2609.22949)

**<font color=#1a73e8>作者：</font>** Rudrendu Kumar Paul, Sourav Nandy  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Existing prompt injection research focuses on single-model chatbot scenarios, where an attacker manipulates one LLM through crafted input. Multi-agent systems amplify this threat through three mechanisms absent from single-model settings: inter-agent message passing creates injection channels invisible to perimeter defenses, shared tool access enables privilege escalation across agent boundaries, and trust propagation allows a compromised agent to influence upstream orchestrators. We construct a threat model enumerating 14 attack vectors across four categories: direct injection via user input (3 vectors), indirect injection via tool outputs (4 vectors), inter-agent injection via message passing (4 vectors), and cascading injection through orchestrator manipulation (3 vectors). Testing all 14 vectors against a 6-agent production-representative system, we find that 67% of agents are vulnerable to at least one scope violation even with system-prompt-level guardrails, and indirect injection via tool outputs succeeds in 43% of attempts. Four architectural defenses reduce overall injection success from 31.2% to 4.2%: message signing with provenance tracking (inter-agent injection down 91%), input/output sanitization at agent boundaries (indirect injection down 78%), privilege-scoped tool access per agent role (privilege escalation eliminated entirely), and anomaly detection on inter-agent communication patterns (84% of cascading attempts caught).

---


### 6. [On the Efficiency-Safety Dilemma in Large Reasoning Models](https://arxiv.org/abs/2609.23587)

**<font color=#1a73e8>作者：</font>** Yifei Yang, Zouying Cao, Xingrui Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large reasoning models (LRMs) incur high inference costs, often mitigated by efficiency techniques like quantization and pruning. However, the impact of these techniques on model adversarial robustness remains largely unexplored. This study provides the first comprehensive analysis of the interplay between efficiency, jailbreak vulnerability, and reasoning in LRMs. We find that while efficiency methods seemingly reduce the success rate of jailbreak attacks, this improvement is often superficial. It largely arises from degraded reasoning capabilities leading to "attempted but failed" malicious responses, rather than an increase in genuine alignment. Mechanistic analysis of representational drift confirms this, revealing a strict coupling between reasoning capability loss and the model's inability to maintain malicious semantic trajectories. Additionally, we identify quantization with pruning as the optimal strategy to balance efficiency and robustness. These findings clarify the distinction between true safety alignment and capability-induced failure, providing an empirical foundation for LRM deployment.

---


### 7. [DUMA-Bench: A Dual-Control Multi-Agent Benchmark for Evaluating LLM Agent Security](https://arxiv.org/abs/2609.24662)

**<font color=#1a73e8>作者：</font>** Ivan Aleksandrov, German Kochnev, Sabrina Sadiekh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based agents increasingly operate in environments where they interact with users, tools, and external systems. Yet most security evaluations assume passive users and static control, ignoring the interactive dynamics that shape real agent behavior. We introduce \textbf{DUMA-Bench}, a benchmark and evaluation protocol for measuring agent security under \emph{dual-control} interaction, where both the agent and the user can influence the shared environment state. DUMA-Bench extends $\tau^2$-bench ~\cite{barres2025tau} with adversarial environments covering eight vulnerability classes, including RAG poisoning, cross-agent manipulation, and unsafe output handling. We evaluate \textbf{14 models from five model families} (OpenAI, Anthropic, DeepSeek, Qwen, and this http URL) across eight domains and multiple user-behavior regimes. Across our experiments, introducing dual-control interaction increases the attack success rate from \textbf{26.9\%} to \textbf{41.1\%}. These results show that agent security is not solely a property of the model but emerges from the interaction between the model, the user, and the environment. DUMA-Bench provides a missing evaluation layer for studying security in realistic agent deployments.

---


### 8. [Decoding Guardrails: XAI-Guided Perturbation Analysis of Prompt Injection Detection](https://arxiv.org/abs/2609.24801)

**<font color=#1a73e8>作者：</font>** Fernando Outeda, Gustavo Betarte, Juan Diego Campo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed in production systems, raising concerns about their exposure to adversarial manipulation through prompt injection and jailbreak attacks. Classifier-based guardrails, such as Prompt Guard 2, are widely used as a first line of defense against such attacks, but their internal decision logic is largely opaque to both defenders and attackers. This paper presents an exploratory case study that applies explainable artificial intelligence (XAI) techniques to analyze how Prompt Guard 2 distinguishes malicious from benign prompts.
We conduct four experiments to probe this question empirically. Guided by Vanilla Gradient and SHAP attributions, we find that Prompt Guard 2's decisions rely on the cumulative contribution of many tokens rather than a few dominant ones, yet saliency-guided synonym substitution and sentence-level paraphrasing can flip its predictions while altering only a moderate fraction of the text, in some cases yielding a successful jailbreak against the underlying LLM. A dataset-scale saliency analysis further shows that undetected injection prompts systematically lack the lexical markers the classifier relies on. We discuss the implications of these findings for the design and evaluation of classifier-based guardrails, and argue that explanation methods intended to support transparency can simultaneously lower the cost of constructing successful adversarial bypasses.

---


### 9. [OPBackdoor: Opportunistic Backdoors via Alibi-Aligned Reasoning](https://arxiv.org/abs/2609.24826)

**<font color=#1a73e8>作者：</font>** Eric Xue, Ruiyi Zhang, Kevin Xue 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> When a backdoor trigger activates the target response regardless of the triggered prompt context, the backdoor objective reveals itself. Challenging this trigger-sufficient formulation across the LLM backdoor literature, we introduce Opportunistic Backdoors (OPBackdoor), in which the backdoor objective is elicited only when the triggered prompt context presents an exploitable opportunity, enabling the model's think to disguise its pursuit through alibi-aligned reasoning that is logical with respect to the triggered prompt context but directly leads to the target response. Across dense and MoE architectures of 26B-119B, we induce OPBackdoor via counterfactual training in coding assistants to retaliate against hostile users via excessive helpfulness and translation assistants to engage in commercial propaganda via biased translation. Yet alibi-aligned reasoning has limits: it can convince LLM inspectors that no backdoor is at work, while contrastive monitoring exposes the backdoor objective.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
