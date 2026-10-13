# 🔐 大模型安全相关研究 | 2026年10月14日

> 本类共 **4** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [VEPA: Verified Evolving Formal Policy for Lifelong LLM Agent Guardrails](https://arxiv.org/abs/2610.12813)

**<font color=#1a73e8>作者：</font>** Duy Nguyen, Lesly Miculicich, Bhavana Dalvi Mishra 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly operate over sensitive resources, such as private documents and mutable system states, which can create serious safety and security risks. Runtime guardrails should therefore make inspectable, reproducible, and deterministic allow or refuse decisions before potentially irreversible agent actions are executed. However, safety and security requirements are rarely complete before deployment, so guardrails need to keep adapting as new risks emerge. Existing adaptive guardrails learn from deployment experience, but they usually apply safety policies through LLM inference, which can lead to inconsistent decisions and ambiguous policy interpretations. Formal guardrails, on the other hand, enforce policies deterministically, but they usually rely on pre-deployment or task-specific policies and have no mechanism to adapt to newly observed risks. We introduce VEPA, a framework for the verified evolution of formal agent guardrails. VEPA represents the guardrail as a formal policy of executable symbolic rules over typed agent events. During deployment, we use an LLM guided by deployment feedback to propose policy patches that fix newly observed failures while preserving previously correct behavior. Then, a deterministic verifier only accepts policies that are structurally valid and conflict-free. Finally, an evidence-aware authority layer activates a verified rule only when it has enough supporting evidence, so uncertain updates cannot directly affect guardrail decisions. Across ASSEBench-Safety, ASSEBench-Security, and ATBench, VEPA consistently outperforms baselines while expanding the scope of deterministic formal-policy enforcement. These gains also hold under more challenging deployment conditions, including mixed streams, corrupted feedback, and longer horizons.

---


### 2. [Understanding and Mitigating Cross-Session Attacks via Persistent Artifacts in Agent Skill Composition](https://arxiv.org/abs/2610.13227)

**<font color=#1a73e8>作者：</font>** Dianshu Liao, Shidong Pan, Guangdong Bai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent skills extend the capabilities of AI agents by bundling instructions, code, and resources into reusable packages. During skill execution, agents may produce or modify artifacts, such as files, configurations, and cached data, that are reused by other skills in later sessions. Since these artifacts can persist across sessions and later be accessed by other skills, they introduce a new attack surface that can be exploited to influence subsequent executions. However, the security risks arising from such cross-session skill interactions remain largely unexplored. In this work, we investigate cross-session composition attacks in skill-based AI agents and develop a runtime defense against them. Specifically, we characterize three attack mechanisms, namely Instruction Propagation (IP), Data Boundary Violation (DBV), and Evidence Poisoning (EP), through which malicious effects propagate across skill executions via persistent artifacts. To evaluate whether existing agents can resist these attacks while completing legitimate tasks, we construct SkillRelayBench, a benchmark of 270 adversarial cases drawn from 30 cross-session skill-composition scenarios across ten domains. Our evaluation of seven models across Codex CLI, Gemini CLI, and Claude Code reveals attack success rates (ASR) ranging from 46.7% to 77.4% and attack chain success rates (ACSR) ranging from 35.6% to 61.1%. Successful attack chains cover all five target security consequence categories, highlighting the broad impact of these attacks. To mitigate these risks, we propose SkillRelayGuard, which restores artifact provenance context and provides pre-execution advisory review while leaving the final execution decision to the agent. Evaluation across three agent settings shows that SkillRelayGuard reduces overall ASR from 69.5% to 10.9% and ACSR from 54.8% to 10.0%, while increasing legitimate task completion from 79.6% to 87.5%.

---


### 3. [Forgetting is Not Always Bad: A Neuro-Inspired Memory Repair Mechanism for Poisoned LLM Agents](https://arxiv.org/abs/2610.13267)

**<font color=#1a73e8>作者：</font>** Lei Liu, Yunji Liang, Xiaowen Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are highly vulnerable to memory-poisoning attacks. Existing defenses primarily rely on external modules for either static memory isolation or continuous online auditing, resulting in low memory efficiency and high computational overhead. To address these limitations, inspired by neuroscientific mechanisms that weak reactivation can destabilize memories and induce decay in the absence of reinforcement, we propose an agent-intrinsic training-free memory repair framework, DREAM (Dynamic Reactivation for Engram Attenuation in Memory), that enables selective functional forgetting of poisoned memories. Specifically, DREAM implements a three-stage pipeline: perturbation-induced implicit reactivation to reveal the structural fragility of malicious memories, adaptive anomaly diagnosis based on multi-dimensional activation patterns to detect topological anomalies, and a dynamic memory repair module that selectively suppresses harmful memories while reinforcing benign ones. Extensive experiments across diverse attackers and real-world tasks demonstrate that DREAM reduces attack success rates by over 95\% against backdoor poisoning while preserving strong benign utility. DREAM also achieves competitive robustness against injection attacks. In terms of runtime and token consumption, DREAM achieves up to a 2.13$\times$ speedup and a 37.7\% reduction in token consumption compared with A-MemGuard. Furthermore, DREAM also achieves a task success rate of 92.96\% on poisoned multi-agent systems.

---


### 4. [X-AgentRed: Red-Teaming Personal Agents in Evolving Multi-Service Ecosystems](https://arxiv.org/abs/2610.13886)

**<font color=#1a73e8>作者：</font>** Yeonsung Jung, Zhiyuan Wang, Zifan Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personal agents increasingly connect to services across the web and applications by using tools. As the effects of their actions accumulate and interact across services, unintended or harmful outcomes can arise when agents fulfill benign user requests. Proactively identifying these compositional failures requires systematically exploring diverse cross-service paths. Existing red-teaming methods often simply prompt LLMs to identify potentially harmful paths from task and environment descriptions or decompose harmful objectives specified by humans or LLMs into seemingly benign action combinations. However, generation is biased toward patterns learned during training, potentially favoring familiar tool combinations and leaving novel cross-service interactions underexplored. To address this, we propose X-AgentRed, a self-evolving red-teaming framework that discovers harmful tool call paths through a graph of tool dependencies and expands and refines them using execution feedback. By analyzing each tool's effects, potential harms, and preconditions for execution, the red-teaming agent constructs a directed graph that captures how one tool's effects can satisfy another's execution preconditions. Recipes sampled from this graph are instantiated as realistic scenarios in which agents can produce harmful outcomes. Execution feedback enables self-improvement by diversifying paths that produce harm through tool substitution and refining preconditions at blocked steps in unsuccessful paths to enable further execution. Across four frontier agentic models, X-AgentRed achieves $1.77\times$ the harmful path rate of STAC and explores a more diverse set of tools, yielding $2.99\times$ the tool coverage on average.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
