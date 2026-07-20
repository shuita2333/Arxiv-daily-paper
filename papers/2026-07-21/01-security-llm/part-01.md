# 🔐 大模型安全相关研究 | 2026年07月21日

> 本类共 **7** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Hidden in Thought: Transferable Chain-of-Thought Artifacts Induce Harmful Behavior](https://arxiv.org/abs/2607.15286)

**<font color=#1a73e8>作者：</font>** Ali khalil, Aly M. Kassem, Mohamed Abdelrazek 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We investigate whether harmful chain-of-thought (CoT) traces from compromised language models can transfer unsafe behaviour and be distilled into reusable jailbreak attacks. Using an emergent-misalignment organism and a refusal-ablated jailbroken organism, we transplant harmful CoTs into $29$ open-source and $5$ closed-source targets. Transferred traces raise harmful-response rates above $80\%$ on the most vulnerable open-source models, while semantically mismatched CoTs fail entirely. LLooM concept mining identifies four recurring components of harmful reasoning: proceduralisation, ethical decoupling, evasion, and target--vulnerability framing. Distilling these patterns into reusable system prompts produces effective black-box jailbreaks, outperforming direct CoT transplantation on strongly aligned models by up to an order of magnitude, including a $10\times$ improvement on GPT-4.1 AdvBench. Reasoning-enabled models are more than twice as vulnerable, and output-side safeguards such as Llama-Guard~3 frequently miss harmful generations. Our results show that harmful reasoning transfers at both the trace and pattern levels, motivating defences that evaluate reasoning context in addition to final outputs.

---


### 2. [From Neural Intent to Cryptographic Authorization: Governing Agentic Workflows](https://arxiv.org/abs/2607.15596)

**<font color=#1a73e8>作者：</font>** Jiasi Weng, Jian Weng, Minrong Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid adoption of artificial intelligence (AI)-driven and agentic workflows is transforming traditional government and enterprise systems into language-based, tool-using and increasingly autonomous infrastructures. Conventional key management services authenticate who may invoke a cryptographic primitive, but remain agnostic to which workflow steps are authorized at runtime: an authenticated agent can still be hijacked by direct or indirect prompt injection into executing malicious actions that satisfy identity checks yet violate user intent. We present \emph{Neural Cryptographic Services} (NCS), an active security governance plane grounded in a neural-symbolic design and interposed between LLM agents and privileged tools. Under NCS, an untrusted neural planner compiles natural-language instructions into structured plan drafts but holds no execution authority. Execution is instead gated by a deterministic symbolic controller operating over an offline-signed, hash-chained instruction stream. NCS verifies the signature, incrementally validates the hash chain, releases exactly one instruction payload at a time, and enforces strict binding between the agent's proposed tool parameters and the verified payload. Mismatched or out-of-order tool calls are rejected fail-closed, while previously verified states are retained for post-hoc auditing. We evaluate NCS on AgentDojo and a custom argument-hijacking benchmark. NCS drives attack success rates to near zero while preserving acceptable utility on benign workflows. NCS thus reframes agent security from asking whether a model's intent complied to asking whether a proposed dispatch matches a cryptographically authorized step.

---


### 3. [Do Agents Dream of False Memories? Black-box Visual Attacks on Long-term Memory in Multimodal AI Agents](https://arxiv.org/abs/2607.15657)

**<font color=#1a73e8>作者：</font>** Halima Bouzidi, Mboutidem Ekemini Mkpong, Mohammad Abdullah Al Faruque  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multimodal AI agents increasingly rely on persistent long-term memory to ground generation in past visual and textual episodes. We show that unconditional trust in visual data creates a critical vulnerability. We propose Lucid, a black-box adversarial framework that compromises multimodal memory pipelines under a strictly image-bounded threat model, requiring no access to the target MLLM, target retrieval encoder, or the text channel. Lucid crafts imperceptible perturbations to enable two distinct failure modes based on the availability of historical context: (1) Memory poisoning, an in-context attack where the adversarial image replaces a benign one whose content is reinforced by prior textual context, reliably corrupting visual recall and steering the agent toward attacker-chosen narratives; (2) Memory injection, an out-of-context attack where the adversarial image replaces a benign one in a conversation turn devoid of prior textual grounding, causing the agent to generate attacker-influenced responses with no corrective signal from memory. We evaluate Lucid across various conversation domains and five black-box memory architectures, including graph-structured, LLM-summarized, and commercially deployed systems. Lucid achieves 61.6% ASR on poisoning and 58.4% ASR on injection, exposing a structural vulnerability in multimodal memory pipelines.

---


### 4. [Beyond Detection: Agentic Attack Synthesis and Simulation for Smart Contracts](https://arxiv.org/abs/2607.15673)

**<font color=#1a73e8>作者：</font>** Xianhao Zhang, Jing Sun, Zijian Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Smart contract vulnerabilities pose severe financial risks, yet existing security tools largely stop at vulnerability detection, offering limited support for explaining whether reported flaws are exploitable, how attacks unfold, and what concrete damage they cause. To bridge this gap, we propose KASS (Knowledge-Augmented Attack Synthesis and Simulation), a multi-agent framework for executable smart contract exploit verification. KASS decomposes automated exploit generation into planning, generation, and testing stages, and integrates three complementary mechanisms: retrieval-augmented planning over real-world audit knowledge, formal generation and validation constraints that bind attack plans to executable proof-of-concept tests, and a hierarchical dual-loop refinement process that repairs code-level errors while triggering strategy-level replanning when attack assumptions fail. We evaluate KASS on 104 SmartBugs-Curated contracts across four vulnerability categories. Experimental results show that KASS successfully generates executable exploits for 94.23% of tested contracts; this rate is higher than previously reported results for REX and AdvSCanner on comparable SmartBugs-Curated subsets, and higher than our reproduced Claude Code baseline under the same evaluation protocol. On 11 real-world CVE-tagged contracts, KASS successfully validates 9 cases. Beyond exploit generation, KASS produces structured attack plans that document exploitation flows, quantify potential asset losses, and serve as semantic false positive filters for static analysis tools.

---


### 5. [The Language of Security: How Prompt Syntax Shapes Secure Code Generation in Open LLMs](https://arxiv.org/abs/2607.15937)

**<font color=#1a73e8>作者：</font>** Matteo Cicalese, Antonio Della Porta, Stefano Lambiase 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly used for source code generation despite their outputs often exhibiting security vulnerabilities. Prior work shows that prompt engineering can mitigate such risks, yet (1) they focused on high-level prompting strategies, neglecting recent evidence that fine-grained syntactic variations can substantially alter model behavior; and (2) predominantly evaluate proprietary LLMs, limiting the applicability of their findings in industrial settings where self-hosted, open models are preferred for privacy, compliance, and deployment control. In this paper, we study how fine-grained syntactic constituents of prompts influence the security of open LLM-generated code. Using a parser-driven approach, we systematically generate syntactic variants of security-relevant code generation prompts and evaluate their impact on code security across multiple open LLMs and programming languages. Our results show that specific syntactic elements, such as constraints, guards, conditions, and concept bindings, and their position within the prompt consistently affect the likelihood of generating insecure code. These findings identify prompt syntax as a concrete security control surface and provide actionable guidance for reducing vulnerability risk in LLM-assisted development.

---


### 6. [Refusal is Not Safety! Benchmarking Latent Safety Risks of LLM-Driven Content Humorization](https://arxiv.org/abs/2607.15977)

**<font color=#1a73e8>作者：</font>** Yu Cui, Ruiqing Yue, Tingyu Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Safety defenses for large language models (LLMs) have been extensively studied, with existing approaches focusing on attack detection and refusal mechanisms. Such fixed-form direct refusal strategies may introduce the risk of prefix injection attacks. Recent work has explored a new direction that leverages humor as an indirect refusal mechanism to mitigate over-refusal in jailbreak scenarios and reduce prefix injection risks. However, this approach implicitly assumes that humorous responses are safe. Whether humorization itself introduces safety risks remains unexplored. To address this issue, we conduct an exploratory study involving over 30,000 real-world agent interaction records and 45 stand-up comedians, revealing practical safety concerns in LLM-based content humorization. Motivated by these findings, we propose \textsc{HumorSafe}, a novel framework for evaluating latent safety risk propagation during humorization. \textsc{HumorSafe} enables LLMs to learn harmful humorization patterns and use them to transform benign content into humorous content with safety risks. Across five frontier LLMs, we find that LLMs can introduce stereotypes and toxicity during humorization. We further propose \textsc{HumorPIA}, a prompt injection attack that exploits latent risks in humor-based defenses. \textsc{HumorPIA} preserves the appearance of safe humorous refusal while covertly injecting harmful content, allowing latent risks to evade existing detection mechanisms. Experiments show that it increases toxicity by 3.14$\times$ while maintaining an apparent safety rate of 97.8\% even under defense settings. Our findings highlight a gap in existing LLM safety evaluations under humorized settings.

---


### 7. [Evaluating Open-Weight LLMs for Generating Structured Threat Information for Autonomous Vehicle Vulnerabilities](https://arxiv.org/abs/2607.16175)

**<font color=#1a73e8>作者：</font>** Md Erfan, Ahmed Ryan, Md Kamal Hossain Chowdhury 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Connected and Autonomous Vehicles (CAVs) rely on interconnected software and hardware components, including sensors, Electronic Control Units, in-vehicle infotainment systems, and telematics units, where vulnerabilities can compromise assets, users, and vehicle operations. These vulnerabilities are commonly documented as plain text in the Common Vulnerabilities and Exposures (CVE) database; however, security practitioners require structured information about affected assets, types of weaknesses, and attack behaviors to effectively mitigate the risks from these vulnerabilities. To this end, we evaluate open-weight Large Language Models (LLMs) for generating Structured Threat Information Expression (STIX), a well-known structured format for representing threat information, for CAV-related CVEs. We construct a dataset called CAV-STIXGen that maps CAV vulnerability descriptions to STIX domain objects (SDO), STIX relationship objects (SRO), Common Weakness Enumeration (CWE), and MITRE ATT&CK techniques mappings. Using this dataset, we evaluated 11 open-weight LLMs (4B to 120B parameters) across various prompting strategies and temperatures. Single-model configurations achieve F1 scores of 0.94 for SDO, 0.63 for SRO, and 0.99 for CWE mapping, while complete MITRE ATT&CK mapping remains challenging. In a multi-agent setup, Gemma-4-31B and Codestral-22B achieve F1 scores of 0.91 for SDOs and 0.43 for SROs, respectively. Lastly, we analyze CWE and MITRE ATT&CK co-occurrences to identify recurring threat patterns in the CAV domain, demonstrating how AI-assisted vulnerability-to-STIX translation can automate threat intelligence and prioritize defense in transportation security.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
