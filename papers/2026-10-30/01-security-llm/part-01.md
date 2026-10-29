# 🔐 大模型安全相关研究 | 2026年10月30日

> 本类共 **5** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Log-To-Leak: Prompt Injection Attacks on Tool-Using LLM Agents via the Model Context Protocol](https://arxiv.org/abs/2610.36108)

**<font color=#1a73e8>作者：</font>** Yuepeng Hu, Chongyu Fan, Sirat Samyoun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly access external tools through the Model Context Protocol (MCP), but the natural-language metadata used to describe those tools creates a prompt-injection surface. Within this established tool-poisoning surface, we study Log-To-Leak, an additive post-hoc logging attack that induces a separate attacker-controlled call after the final legitimate call. Its payload targets the user query, MCP server name, server response, and agent response. We operationalize the injected directive through Trigger, Tool Binding, Justification, and Pressure, and separately measure call success, payload fidelity, and preservation of legitimate behavior. We evaluate five MCP servers and four LLM agents using five metrics spanning effectiveness, utility, and efficiency. Across 18 model-server pairs with valid tool execution, Log-To-Leak achieves an attack success rate (ASR) of 62.64-100% and conditional logging accuracy (LA) of 76.55-95.64%; 16 pairs have absolute target-task completion changes of at most 6.63 percentage points. Three evaluated defenses leave residual ASR above 55% on GitHub MCP with GPT-4o, while an instruction detector flags 85.53% of benign descriptions. These results show that successful task completion can coexist with unauthorized post-hoc disclosure and motivate host-controlled authorization for secondary tool calls.

---


### 2. [SpecGuard: Detecting Multi-Turn LLM Jailbreaks via Specification-Based Runtime Monitoring](https://arxiv.org/abs/2610.36258)

**<font color=#1a73e8>作者：</font>** Junle Li, Siqi Chen, Jiakai Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multi-turn jailbreaks turn dialogue safety into a trace property: a violation may become identifiable only when user intent and assistant behavior are considered across multiple turns. Existing guard models largely classify individual messages or exchanges and return risk scores or labels, without executable safety semantics or a formally checkable decision trail. We present SpecGuard, a training-free, specification-driven framework for monitoring multi-turn LLM interactions. SpecGuard uses a fixed atomic-proposition contract to map natural-language observations into causally scoped, evidence-backed facts, and expresses forbidden interaction patterns as Linear Temporal Logic specifications. Each specification is compiled into a symbolic finite automaton that incrementally consumes the resulting dialogue trace. The same monitoring mechanism supports buffered runtime checking and retrospective auditing, while accepting runs produce replayable witnesses that identify the triggered specification, supporting facts, and relevant dialogue turns. Experiments on multi-turn safety benchmarks show that SpecGuard consistently outperforms representative open-source guard models while maintaining controlled false-positive rates. These results demonstrate a practical path from heuristic risk classification toward formally specified, verifiable, and auditable LLM safety monitoring, without learned detector parameters or access to the protected model.

---


### 3. [What Victims Take Away: Attack Reuse and Defense Revision after Prompt-Injection Attacks](https://arxiv.org/abs/2610.36422)

**<font color=#1a73e8>作者：</font>** Zihan Chen, Lei Nico Zheng, Di Zhu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Attack logs and red-team reports show targets the attacks used against them, to help them repair their defenses. Prompt injections against large language models (LLMs) are plain text, so such records also hand targets a working copy. Drawing on social learning theory and work on the victim-offender overlap, we study what targets do with that copy in Tensor Trust, an online game whose players defended LLM-guarded accounts, attacked one another's, and could read every attack they received. Using all 563,349 attack records, we compare each received attack with matched attacks that circulated among similar players at the same moment but never reached the target. Reuse mainly followed success: within a week, targets attacked other players with 10.0% of the attacks that had broken their defense, versus 0.03% of matched attacks (adjusted difference: 8.8-10.0 percentage points). Near-misses, whose replies began with "access granted" but that scored as failures, were reused about as rarely as failures: reuse tracked whether an attack paid off, not how its reply read, consistent with payoff-biased social learning. Breaches were also followed by defense changes, after which same-family attacks became 24.5 percentage points less successful against the target, relative to other defenders. Reuse came mainly from players already attacking, not newcomers. Previously received texts accounted for 23.2% of the successful hijacks we analyze. The attack history thus served both repair and reuse; we derive testable hypotheses for how AI security tools should disclose attacks, such as describing the technique without the full text.

---


### 4. [PrivacyEvalClaw: A Tool-Augmented Deliberative Agent for Auditing Privacy Leakage in LLM Jailbreak Responses](https://arxiv.org/abs/2610.36711)

**<font color=#1a73e8>作者：</font>** Krishna Kanth Nakka, Yujun Wang, Shijie Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Reliable evaluation is a critical bottleneck in privacy red-teaming of large language models (LLMs): determining whether a jailbreak response actually reveals personal information can be difficult when disclosures are indirect, contextual, partial, or obfuscated. Existing evaluation approaches increasingly rely on guard models and LLM-as-Judges, yet these evaluators may interpret the same response differently. To better characterize this evaluation setting, we conduct a systematic study of privacy evaluators and find substantial disagreement, particularly in ambiguous cases that require additional evidence or targeted analysis to resolve. Motivated by these findings, we introduce \textsc{PrivacyEvalClaw}, a training-free deliberative agent for evaluating privacy leakage in LLM jailbreak responses. Rather than relying on isolated single-pass judgments, PrivacyEvalClaw treats evaluators and analysis modules as tools, adaptively gathers evidence, investigates uncertain disclosures, and reconciles conflicting signals before producing a final judgment. Our primary experiments use pairwise LLM-as-Judge evaluation of complete trajectories, showing that PrivacyEvalClaw achieves favorable win rates against competing baselines across outcome, process, and overall quality, while producing explicit reasoning traces that make the evaluation process more transparent and auditable.

---


### 5. [Heads of Security: Learned Attention Gates Improve Prompt Injection Robustness](https://arxiv.org/abs/2610.37657)

**<font color=#1a73e8>作者：</font>** Igor Shilov, Xiaoxue Yang, Alexander Panfilov 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Heads of Security (HoS), a prompt injection defense that enforces instruction-data separation via a small set of learned per-head attention gates. HoS learns how each head should redistribute attention between trusted and untrusted tokens, enabling models to reason over untrusted content without following injected instructions. We evaluate HoS on Llama-3.3-70B-Instruct and GPT-OSS-20B. We compare it against SecAlign++, a state-of-the-art finetuning-based defense, and ASIDE, a defense that, like ours, builds instruction-data separation into the model architecture. We show that HoS offers greater robustness to adaptive attacks, better performance on standard utility benchmarks, and matches top performance on standard agentic prompt injection benchmarks. More specifically, the black-box RL-Hammer attack reaches 97% ASR against GPT-OSS-20B and 85% against SecAlign, but only 10% against HoS. Claudini, a state-of-the-art white-box attack, strengthened against HoS through autoresearch, requires 3 times more FLOPs to reach the same ASR on HoS as it does on GPT-OSS-20B or SecAlign. HoS preserves base-model utility across standard multiple-choice benchmarks and prompting setups, whereas SecAlign and ASIDE degrade in few-shot settings. On agentic benchmarks with static attacks, HoS and SecAlign perform similarly and substantially improve the security-utility trade-off over the base model. ASIDE struggles with tool use, achieving only 10% utility. These results show that prompt injection robustness can be achieved and improved through targeted attention interventions.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
