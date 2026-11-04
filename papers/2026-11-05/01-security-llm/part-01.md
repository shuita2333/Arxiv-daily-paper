# 🔐 大模型安全相关研究 | 2026年11月05日

> 本类共 **5** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Reliability Stress Testing of RAG Retrieval under Query-Relevant Corpus Poisoning](https://arxiv.org/abs/2611.04264)

**<font color=#1a73e8>作者：</font>** Janet Sung, Kainan Zhou, Gangzhen Qian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> External text can affect a retrieval-augmented generation (RAG) system only after the retriever admits it to the model context. We stress this admission step while varying document content, attacker query information, per-target poison budget, and contamination scope. Across 623 Benchmarking Information Retrieval (BEIR) queries from SciFact and NFCorpus, five query-targeted documents per query reduce classical-retriever nDCG@10 by 40.2-61.5% in isolated-target stress. Full-query anchoring explains most Best Matching 25 (BM25) degradation, whereas appended text also shifts latent semantic analysis (LSA) and Hybrid rankings. A pretrained BGE-small validation reaches 100% target exposure for query-only P=5 on both datasets; adding the injection payload changes SciFact nDCG only from 0.269 to 0.271 and lowers NFCorpus exposure slightly to 98.8%, indicating that query anchoring remains the dominant retrieval-side factor for this dense model. Query length materially changes the interpretation of partial-information attacks: on 162 long SciFact queries, two random terms cover 19.9% of eligible terms and still yield 39.5% Hybrid target exposure. Multi-target contamination adds cross-target interference. Overlap-based admission can remove full-query poisons but may sharply reduce clean retrieval utility, and maximal marginal relevance (MMR) leaves exposure unchanged under the tested configuration. The study measures retrieval-layer failures, not downstream instruction following.

---


### 2. [The Devil is in the Context: Nine Dimensions of Prompt Injection Attacks](https://arxiv.org/abs/2611.04672)

**<font color=#1a73e8>作者：</font>** Jiamin Chang, Kristina Nikolić, Rishi Sharma 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Prompt injection is usually discussed and evaluated as a single, homogeneous type of attack. However, vulnerabilities reported in real-world systems show that prompt injections vary widely. Moreover, the same instruction can be a prompt injection in one context and a legitimate request in another, depending on the user's intent and the system's policies. Ignoring this variation leaves gaps in how defenses are evaluated, and can give a false sense of security against real-world attacks.
We identify nine dimensions along which prompt injection attacks differ. Together, they form a taxonomy that describes the injected instruction itself, its relation to the user's task, and how it manifests in the target system. Each dimension affects which defenses can detect or prevent an attack.
We first use the taxonomy to characterize six real-world prompt injection vulnerabilities, showing how much these attacks differ. We then apply it to nine prompt injection benchmarks and find that most cover only a small region of this space. Combining benchmarks helps, but 13% of pairwise category combinations remain untested, mostly among the less commonly represented categories. Finally, we show that the taxonomy supports automated annotation of benchmarks and targeted generation of new test cases to fill these gaps.
The taxonomy is also useful beyond benchmarks. Defense authors can use it to state which types of prompt injection they evaluated against, and system operators can use it to identify which attacks apply to their system and choose defenses to match.

---


### 3. [Right Tool, Wrong Parameters: Defending LLM Agents Against Parameter Poisoning](https://arxiv.org/abs/2611.04673)

**<font color=#1a73e8>作者：</font>** Yao Wang, Zehua Ma, Weiming Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Indirect Prompt Injection (IPI) poses a critical threat to LLM agents. Existing defenses largely focus on whether an injection induces a new tool invocation or unintended action. In this paper, we study a different attack surface, parameter poisoning, where the attacker preserves the intended action but manipulates one or more tool arguments, such as a recipient or other task-critical value. Such attacks are difficult to detect because no new action is introduced, while parameter changes themselves are often legitimate parts of the user's request. Our key insight is that the legitimacy of a parameter change should be determined by the trust of the information flow that produces it under the user query. The query induces a task-specific trust hierarchy over available information fields: some are trusted to determine particular parameters, while others should have little or no influence. Based on this insight, we propose AuthorityFlow, a three-stage parameter-level defense. First, it interprets the user query to construct a task-specific trust hierarchy over the information fields available to the agent. Second, for each tool argument, it traces the information flow that produces its current value and attributes the value to its supporting field. Finally, it accepts the value only when that field is trusted to determine the parameter under the current task, allowing high-trust changes while flagging low-trust influence as potential parameter poisoning. We further introduce FactAuthBench for evaluating parameter poisoning in LLM agents. Without defense, the attack success rate reaches 93.06%. AuthorityFlow reduces it to 9.03%, while retaining 82.64% benign task utility compared with 90.28% without defense. Our results show that effective IPI defense requires reasoning not only about what action an agent takes, but also about which information is trusted to determine its parameters.

---


### 4. [BrainwashedLLM: Jailbreaking via Automated Adversarial Chain of Thoughts Discovery](https://arxiv.org/abs/2611.04717)

**<font color=#1a73e8>作者：</font>** Masoud Poorghaffar Aghdam, Göktuğ Serdar Yıldırım, Sinem Sav  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) achieve strong performance on complex tasks by generating explicit Chain-of-Thought (CoT) reasoning, but the safety implications of this intermediate reasoning surface remain underexplored. We demonstrate that the reasoning trace itself is a powerful attack vector. Safety alignment in large models is substantially less robust to malicious reasoning embedded in the context than to direct imperative prompts. We introduce BrainwashedLLM, a weak-to-strong adversarial framework that automates the discovery of reasoning-based jailbreaks. First, we use Group Relative Policy Optimization (GRPO), a Reinforcement Learning (RL) algorithm, with a multi-objective rule-based reward to fine-tune a small, white-box source model to generate adversarial reasoning traces. Crucially, the reward is computed entirely over the source's own reasoning trace. Second, we show that these traces transfer in a zero-shot manner. When traces are injected as input prefixes, they steer larger black-box LRMs to continue the adversarial reasoning and produce harmful outputs, without requiring prompt optimization, gradient access, or any form of output feedback from the target model. Across four state-of-the-art LRMs that span distinct architectures, BrainwashedLLM achieves ASR@5 between 0.74 and 0.98 across targets, within 16 points of query-based baselines, without querying the target during attack construction. To our knowledge, this is the first framework to use RL to directly optimize the CoT of LRMs as an attack surface without any target feedback, and the first to demonstrate zero-shot weak-to-strong transfer of reasoning traces. Our results suggest that exposed CoT is a vulnerability in LRMs and motivate architectural defenses that isolate the reasoning buffer. Warning: This paper contains potentially offensive and harmful text.

---


### 5. [Whose Guardrail? User Identity Shapes the Effectiveness of Model Disclaimers in Mitigating LLM Political Persuasion](https://arxiv.org/abs/2611.05347)

**<font color=#1a73e8>作者：</font>** Jillian Fisher, Thomas Richardson, Daniel W. Fisher 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Politically biased AI can shift users' opinions, yet it remains unclear whether model disclaimers protect against such persuasion. We report a preregistered experiment (N=1,586) examining how disclaimer design and user characteristics shape susceptibility to politically biased AI. We varied whether disclaimers identified political bias versus potential inaccuracies and whether they included an explanation. Participants completed two decision-making tasks with an LLM biased against their political views, with outcomes assessed immediately and one week later. Disclaimers identifying political bias and including an explanation reduced persuasion, but effects varied across contexts and did not persist. Individual differences were more consistent predictors: Republicans were more persuaded and reported higher trust than Democrats across tasks. Similarly, participants who used AI more frequently were also more persuaded, whereas those with greater self-reported AI knowledge were less persuaded. These findings suggest that generic disclaimers are not enough: effective safeguards must account for user heterogeneity and context.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
