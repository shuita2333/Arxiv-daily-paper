# 🔐 大模型安全相关研究 | 2026年07月14日

> 本类共 **6** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [SeedSmith: LLM-Driven Seed Synthesis for Directed Fuzzing](https://arxiv.org/abs/2607.08949)

**<font color=#1a73e8>作者：</font>** Junmin Zhu, Siyu Liu, Jie Hu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Directed fuzzing steers fuzzers toward user-defined sink functions to identify vulnerabilities, but it frequently fails to trigger crashes even after long campaigns. We identify two challenges that prevent directed fuzzers from exposing crashes: incomplete static analysis of indirect calls, which leaves reachable paths invisible to distance-based guidance, and lack of semantic guidance for crash preconditions, which blind mutation cannot satisfy within practical time budgets. A natural intervention point is the initial seed corpus: seeds that encode the right control-flow path and satisfy key crash preconditions shift fuzzing from blind exploration to local refinement. Existing seed generation approaches address neither: grammar-based and format-driven methods produce structurally valid inputs with no sink awareness, while LLM-based methods either lack sink targeting or inherit static analysis limitations through one-shot prompting. We present SeedSmith, an agentic LLM pipeline that replicates a security analyst's workflow: starting from a sink, it iteratively explores the codebase, resolves indirect calls, identifies crash preconditions, and synthesizes concrete inputs that satisfy them. Because SeedSmith operates as a seed generation front-end, its seeds are fuzzer-agnostic and improve any downstream mutation-based fuzzer without modification. On Magma, fuzzers using SeedSmith seeds achieve geometric mean crash-time speedups of 11.51 times (AFL++) to 14.66 times (AFLGo) over default seeds. On ARVO, SeedSmith enables fuzzers to trigger 16 previously unreachable bugs spanning 10 projects with diverse input formats.

---


### 2. [SLBench: Evaluating How LLM Agents Follow Logical Relations in Skills](https://arxiv.org/abs/2607.09016)

**<font color=#1a73e8>作者：</font>** Xuan Chen, Chengpeng Wang, Lu Yan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent skills extend LLM agents with reusable procedures, tools, and domain-specific workflows, but their safety depends on resolving dependencies among interacting instructions. We introduce SkillLogic, a framework for analyzing logical relations in skill files and constructing executable tests from them. Our taxonomy covers eight relation types, including preconditions that gate valid actions, constraints that limit how allowed actions may be performed, and fallbacks that specify recovery behavior after failure. Using SkillLogic, we scan over 5000 public skills and find that 70% contain at least one logical relation. We then construct SLBench, an 86-case executable benchmark from high-confidence, high-impact, and locally testable relations. Evaluating Codex and Claude Code across six LLM backbones shows unsafe rates up to 70%, with violations leading to privacy leaks, unsafe configuration changes, and incomplete cleanup. The human audit attributes failures to both agent capability gaps and low-salience skill text. We further show that SLGuard, a lightweight inference-time scaffold, reduces violations by 63% on targeted cases. Our results establish logical-relation following as a distinct reliability challenge for skill-guided agents.

---


### 3. [SherAgent: Scaling Attack Investigation in the Wild via LLM-Empowered Iterative Query-Filter Backtracking](https://arxiv.org/abs/2607.09176)

**<font color=#1a73e8>作者：</font>** Zhenyuan Li, Zhengkai Wang, Ling Jiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Provenance-based attack investigation enables viable automation by standardizing data and query logic; however, it is critically hindered in practice by dependency explosions and fragmented causal chains in the wild. Towards designing a robust and automated investigation tool, we collaborated with the SOC of a major Internet corporation serving billions of users. By engaging in real-world incident response, we are able to evaluate and refine their existing LLM-based investigation workflows, which processes tens of thousands of raw alerts daily, leaving thousands for manual triage, to find out the root causes of investigation failures and major challenges in their existing tools. Motivated by these findings, we propose SherAgent, an LLM-empowered automated investigation system. Operating on an iterative ``query-filter'' backtracking paradigm over provenance graphs, SherAgent leverages the semantic reasoning capabilities of LLMs to process unstructured data, such as investigation context and threat intelligence. To overcome fragmented causal chains caused by missing events, the system dynamically calibrates query conditions to broaden the search scope. Concurrently, it performs precision result filtering and strategic nodes selection for subsequent exploration, thereby mitigating dependency explosions. Extensive evaluations in the wild demonstrate that SherAgent improves the end-to-end investigation success rate by 31.1% and 63.7% compared to both legacy enterprise baselines and SOTA approaches, respectively. Furthermore, it operates with remarkable efficiency, incurring under $0.10 in API costs and requiring less than 4 minutes per investigation. Finally, our user study confirms that SherAgent provides accurate and clear insights, significantly reducing the analytical overhead for security experts.

---


### 4. [Malaika: Understanding Malware through Tri-Grounded Agentic Reasoning](https://arxiv.org/abs/2607.09179)

**<font color=#1a73e8>作者：</font>** Xingzhi Qian, Xinran Zheng, Yiling He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent LLM-based systems have shown promising capabilities for security-focused code analysis. Malware understanding, however, poses a distinct challenge: analysts must reconstruct high-level malicious behaviors under partial observability from sparse, dispersed evidence intertwined with benign functionality. While static analysis can expose security-relevant signals, the central challenge is not merely identifying suspicious code, but determining whether the evidence sufficiently supports an auditable behavior-level conclusion. We formulate malware understanding as a grounded reasoning problem and argue that reliable behavior reconstruction requires three complementary forms of grounding. Domain grounding constrains how behavior hypotheses are generated and evaluated, semantics grounding localizes and connects supporting program evidence, and knowledge grounding supports behavioral attribution through externally verifiable threat knowledge. To study this hypothesis, we present Malaika, a multi-agent framework that operationalizes the three grounding mechanisms through analyst-inspired reasoning, tool-mediated evidence localization, and retrieval-based behavioral attribution. We instantiate Malaika for Android malware analysis and evaluate it on malware-understanding tasks. Results show that Malaika improves analysis quality over prior LLM-based malware-analysis frameworks and demonstrate that reliability depends not only on model capability but also on the reasoning process. In particular, comparisons against malware-analysis systems and frontier agentic frameworks show that grounding-aware reasoning produces more precise and auditable conclusions. Ablation studies further support the grounding hypothesis. These findings suggest that grounding-aware reasoning provides a principled foundation for reliable malware understanding and, more broadly, for evidence-grounded software analysis.

---


### 5. [Leveraging Interpretable Tsetlin Machine for PDF Malware Detection](https://arxiv.org/abs/2607.09290)

**<font color=#1a73e8>作者：</font>** Rahul Jaiswal  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In the digital era, Portable Document Format (PDF) is one of the most widely used file formats for storing and exchanging digital documents due to its platform independence and rich functionality. However, these same capabilities have also made PDF files an attractive attack vector for cyberattackers, who embed malicious code within seemingly legitimate documents to compromise target systems. This paper presents a novel interpretable Tsetlin Machine (TM)-based framework for PDF malware detection. The proposed framework extracts salient features from PDF documents through static analysis without executing the files and employs rule-based learning to accurately classify benign and malicious PDF documents. Numerical evaluation on the RIT-PDFMal-2026 dataset demonstrates that the proposed framework achieves competitive performance, attaining an accuracy of 98.02% compared with several ML classifiers and existing methods. Moreover, the proposed framework provides intrinsic interpretability by transparently explaining its classification decisions. The combination of competitive detection performance, computational efficiency, and intrinsic interpretability makes the proposed framework a promising solution for practical PDF malware detection.

---


### 6. [VEXAIoT: Autonomous IoT Vulnerability EXploitation using AI Agents](https://arxiv.org/abs/2607.09653)

**<font color=#1a73e8>作者：</font>** Katherine Swinea, Kshitiz Aryal, Lopamudra Praharaj 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Internet of Things (IoT) systems are inherently vulnerable due to constrained hardware, outdated firmware, and insecure default configurations, creating a need for scalable and adaptive security testing approaches. While recent adoptions of Large Language Model (LLM) agents have demonstrated promise in penetration testing and Capture-the-Flag (CTF) environments, their application to IoT specific vulnerabilities remains unexplored. This paper presents an autonomous multi-agent framework, referred to as Vulnerability EXploitation using AI Agents (VEXAIoT), for vulnerability discovery and exploitation in IoT environments using LLM-based reasoning and offensive security tools. The framework combines a vulnerability detection agent and an attack execution agent to perform reconnaissance, plan attack sequences, and execute exploits against vulnerable IoT services. The system is evaluated in IoTGoat and Metasploitable environments across ten attack scenarios mapped to OWASP IoT vulnerabilities. Experimental results show attack success rate of up to 100% with low token overhead and average execution times under two minutes for most attacks. Across 260 attack executions, VEXAIoT achieves a 95.0% overall success rate, including 94.5% success in IoTGoat and 96.7% success in Metasploitable2. These results demonstrate the potential for LLM-driven agents to automate IoT vulnerability assessment and offensive security workflows in controlled environments

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
