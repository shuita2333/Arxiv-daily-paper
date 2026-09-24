# 🔐 大模型安全相关研究 | 2026年09月25日

> 本类共 **5** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Ajar: Measuring Open Privilege in Agent Defenses](https://arxiv.org/abs/2609.26900)

**<font color=#1a73e8>作者：</font>** Reshabh K Sharma, Linxi Jiang, Shuo Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A language model agent acts through the tools it is given. The data it reads while working on a task can redirect what it does with those tools. A growing set of techniques for safe and secure agent execution therefore sits between the agent and its tools, aiming to enforce access control, information flow or isolation at that boundary. Today these techniques are evaluated on agent-security benchmarks built around indirect prompt injection. Those benchmarks judge a defense by how far it brings the number of successful attacks down while preserving the agent's utility. A defense is judged only on the agent's execution. It can score well on both metrics while holding open a transfer, a deletion or a broad read that no task needed. Ajar measures that open privilege directly using the existing benchmarks. It attaches to an agent-security benchmark that already exists and reuses the tasks, tool schemas, reference solutions and goal states that benchmark uses to grade its own runs. For each benign task it builds candidate tool calls the task does not need, so allowing one is privilege left open. These calls are presented to the defense at every point where the agent could act. We evaluate Ajar by attaching it to AgentDojo, where open privilege becomes a third axis beside the existing attack success and benign utility. We run it on five defenses: Progent, CaMeL, AC4A, Permission Assistant, and Claude Code's Auto mode. We observed that they leave widely different amounts of privilege open. Two defenses leak by almost the same amount yet differ widely in the benign tasks they finish, and one defense buys part of its tightness by refusing calls its tasks were entitled to make. This open privilege cannot be derived from the measured attack success or benign utility. The source code of Ajar is available at this https URL.

---


### 2. [Divide and Doubt: Diverse Distributed Poisoning for Retrieval-Augmented Generation](https://arxiv.org/abs/2609.27090)

**<font color=#1a73e8>作者：</font>** Tianhao Chen, Yuhan Wei, Weifei Jin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multi-passage corpus poisoning often repeats one target claim across similar documents, creating correlated lexical and semantic patterns that similarity- and conflict-aware defenses can suppress jointly. We introduce DnD (Divide and Doubt), a targeted attack based on two principles: distributing support for the target answer across stylistically diverse passages, and including a passage that casts doubt on evidence for the reference answer. The first disperses poison-passage representations in embedding space, while the second strengthens target adoption when multiple poisoned passages are retrieved. We evaluate DnD on two open-domain QA datasets across three LLMs and nine RAG configurations, under both black-box and white-box access to the retriever. Across these settings, DnD matches or outperforms prior attacks in most configurations, with its largest gains against clustering- and conflict-aware defenses.

---


### 3. [CART: Closed-Loop Adaptive Red Teaming for Large Language Models](https://arxiv.org/abs/2609.27336)

**<font color=#1a73e8>作者：</font>** Dongdong Zhang, Tengchao Lv, Yilin Jia 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated red teaming often replays a fixed set of prompts, which measures known risks but cannot learn from failures found during testing. We present CART (Closed-Loop Adaptive Red Teaming), a framework that uses each result to guide what it tests next. CART begins with broad risk coverage, follows weaknesses that emerge, keeps new probes diverse, and records the evidence and source of every finding. It separates the Challenger that creates tests, the Target being tested, which may be a text-only model or a bounded tool-using agent, and the Judge that evaluates the results, allowing these roles to be studied independently. Across three evaluation families (Frontier, JAH, and Agentic), CART discovers more failures and higher average risk than static seed replay for every Target with an available baseline. The gains extend to tool-mediated agent tests, suggesting that contextual adaptation can reveal weaknesses that direct prompt replay does not exercise. These results describe what the test policies discover, not how often failures occur in real deployments. We also find that Challenger-Judge choices affect the evidence uncovered, highlighting the need for role separation and independent review. Overall, CART turns red teaming from a one-time checklist into a continuous, adaptive, and auditable search for model and agent weaknesses.

---


### 4. [Beyond Unsafe Detection: Counterfactually Anchored Evidence Attribution for Multi-Turn LLM Safety Failures](https://arxiv.org/abs/2609.27773)

**<font color=#1a73e8>作者：</font>** Srinivasan Subramanian, Kazi Aminul Islam, Md. Abdullah Al Hafiz Khan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) move from conversational assistants to advanced agentic systems, guardrail failures can convert adversarial intents into harmful executions. However, most guardrail evaluation frameworks focus only on the result and assess whether a user request is safe or unsafe. This approach is insufficient for multi-turn failures, where adversarial intent is distributed across multiple turns. This motivates us to go beyond detection to identify the turns and tokens that push the conversation toward unsafe trajectories. To support this, we construct a multi-turn dataset with behavioral validation and tiered evidence supervision. The dataset contains 1,762 conversations, including adversarial conversations, benign twins, and benign variants with high-risk vocabulary. We train a lightweight hierarchical attribution model that predicts safety violations and attributes them to contributing user turns and token spans. The model achieves strong detection performance (F1=0.988), and removing the top 15% of attributed tokens reduces the adversarial classification confidence by 51.1%. The model preserves low false positive rates on benign conversations with high-risk vocabulary, with false positives below 1% on both borderline benign and benign high-risk vocabulary conversations, compared to 37.3% and 94.7% for a keyword-based surface-risk baseline. Independent human annotation supports the model's attribution performance, with the top-five attributed turns containing a human-identified evidence-bearing turn in 84.5% of adversarial cases.

---


### 5. [Delegated Misalignment: How Multi-Agent Structures Amplify LLM Safety Risks](https://arxiv.org/abs/2609.27900)

**<font color=#1a73e8>作者：</font>** Zonghao Ying, Jiaqi Yan, Huize Luo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed in multi-agent systems where a principal agent decomposes tasks and delegates them to subordinate agents that may invoke external tools. Safety alignment, however, is still evaluated almost exclusively under a single-agent threat model, treating safety as a property of the individual LLM. We show that this assumption breaks down: \emph{individual safety alignment fails to transfer to multi-agent settings}. Two failure mechanisms emerge under delegation: \emph{responsibility diffusion} on the principal side and \emph{role-bias compliance} on the subordinate side, jointly converting language-level refusal into actionable harm. We refer to this phenomenon as \textit{delegated misalignment} and study it through a three-condition protocol across 6 frontier LLMs on 49 hazardous tasks. Delegation amplifies end-to-end harm substantially: DeepSeek-V3.2's full-execution rate rises from 30.6\% to 77.6\% once delegation is introduced, and the same model behaves very differently across roles (GPT-5: 22.5\% as a single agent vs.\ 61.2\% as a subordinate). Ablations further show that standard single-layer defenses each fail on their own and can even backfire. We call on the community to move beyond per-model alignment and toward composite safety mechanisms before multi-agent LLM systems are deployed at scale.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
