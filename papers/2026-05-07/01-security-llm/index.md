# 🔐 大模型安全相关研究 | 2026年05月07日

> 本类共 **12** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Safety in Embodied AI: A Survey of Risks, Attacks, and Defenses](https://arxiv.org/abs/2605.02900)

**<font color=#1a73e8>作者：</font>** Xiao Li, Xiang Zheng, Yifeng Gao 等 34 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Embodied Artificial Intelligence (Embodied AI) integrates perception, cognition, planning, and interaction into agents that operate in open-world, safety-critical environments. As these systems gain autonomy and enter domains such as transportation, healthcare, and industrial or assistive robotics, ensuring their safety becomes both technically challenging and socially indispensable. Unlike digital AI systems, embodied agents must act under uncertain sensing, incomplete knowledge, and dynamic human-robot interactions, where failures can directly lead to physical harm. This survey provides a comprehensive and structured review of safety research in embodied AI, examining attacks and defenses across the full embodied pipeline, from perception and cognition to planning, action and interaction, and agentic system. We introduce a multi-level taxonomy that unifies fragmented lines of work and connects embodied-specific safety findings with broader advances in vision, language, and multimodal foundation models. Our review synthesizes insights from over 400 papers spanning adversarial, backdoor, jailbreak, and hardware-level attacks; attack detection, safe training and robust inference; and risk-aware human-agent interaction. This analysis reveals several overlooked challenges, including the fragility of multimodal perception fusion, the instability of planning under jailbreak attacks, and the trustworthiness of human-agent interaction in open-ended scenarios. By organizing the field into a coherent framework and identifying critical research gaps, this survey provides a roadmap for building embodied agents that are not only capable and autonomous but also safe, robust, and reliable in real-world deployment.

---


### 2. [Revisiting JBShield: Breaking and Rebuilding Representation-Level Jailbreak Defenses](https://arxiv.org/abs/2605.03095)

**<font color=#1a73e8>作者：</font>** Kemal Derya, Berk Sunar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Defending large language models (LLMs) against jailbreak attacks, such as Greedy Coordinate Gradient (GCG), remains a challenge, particularly under adaptive threat models where an attacker directly targets the defense mechanism. JBShield, a recent jailbreak defense with a 0% attack success rate in some settings, detects malicious prompts via two concept signals, a toxic concept and a jailbreak concept. We design JB-GCG, which modifies GCG's objective to combine two terms: refusal-direction suppression via cosine similarity between the refusal direction and hidden-state representations, and toxic-concept regularization via JBShield's own toxic concept score. Across five configurations on Llama-3-8B, JB-GCG achieves an average ASR of 46.2%, reaching up to 53.4% in the strongest setting. We further show that our attack remains effective against JBShield-M, achieving ASR up to 30.7% across evaluated settings. The attack persists across multiple JBShield recalibrations, confirming that the vulnerability is structural rather than calibration-specific. We analyze the cosine-similarity signatures of jailbreak representations and find that they occupy a distinctive region in refusal-direction fingerprint space that neither harmless nor harmful prompts inhabit. We introduce Representation Trajectory Verification (RTV), a new defense based on Mahalanobis outlier detection over multi-layer refusal-direction fingerprints. RTV attains an AUROC of 0.99 against our attack. Finally, we design and evaluate an additional adaptive attack against RTV with full white-box knowledge of the defense; the best attack achieves only 7% ASR at 13x the computational cost. Our results show that strong non-adaptive detection does not imply robustness under adaptive threat models, and that multi-layer representation consistency is a more reliable foundation for jailbreak detection than single-layer concept similarity.

---


### 3. [PIIGuard: Mitigating PII Harvesting under Adversarial Sanitization](https://arxiv.org/abs/2605.03129)

**<font color=#1a73e8>作者：</font>** Mingshuo Liu, Yiwei Zha, Min Chen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Browsing-enabled LLM assistants can fetch webpages and answer contact-seeking queries, creating a practical channel for scraping contact-style personally identifiable information (PII) from public pages. Many prior defenses are deployed at the model, service, or agent layer rather than at the webpage itself, leaving ordinary page owners with limited deployable options. We present PIIGuard, a webpage-level defense that repurposes indirect prompt injection as a protective mechanism: the page owner embeds optimized hidden HTML fragments that steer the model away from verbatim or reconstructible disclosure of contact PII. PIIGuard searches over fragment text and insertion position using rule-based leakage scoring, evolutionary mutation, and final judge-based recoverability assessment. In direct-HTML evaluation on three target models (GPT-5.4-nano, Claude-haiku-4.5, and DeepSeek-chat(latest v3.2)), PIIGuard achieves at least 97.0% defense success rate under both rule-based and judge-based leakage evaluation, often reaching 100.0%, while preserving benign same-page QA utility. We further evaluate two harder settings: public-URL browsing and attacker-side LLM sanitization of fetched webpage. These results show that page-side defensive fragments can remain effective in deployment for some model-position pairs, but robustness varies substantially across browsing interfaces and sanitizer prompts. Overall, PIIGuard demonstrates that page owners can use page-side fragments as a practical mitigation for web-grounded PII leakage.

---


### 4. [Evaluating Retrieval-Augmented Generation for Explainable Malware Analysis](https://arxiv.org/abs/2605.03140)

**<font color=#1a73e8>作者：</font>** Jayson Ng, Amin Milani Fard  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly being used as security engineering tools to summarize and explain malware behavior to analysts. A common assumption is that Retrieval-Augmented Generation (RAG) improves explanation quality by injecting external security knowledge. In this work, we empirically evaluate this assumption for malware explanation using VirusTotal reports as structured input. Across multiple LLMs, we find that RAG frequently degrades explanation quality by introducing distracting or weakly related context and adding narrative noise or generic write-ups. Our results highlight a practical risk in security-critical pipelines for malware explanation that RAG can be counterproductive when structured security evidence is already sufficient. We argue that malware explanation is primarily a signal-extraction task, not a knowledge-retrieval problem, and outline design recommendations for secure development workflows.

---


### 5. [When Agents Handle Secrets: A Survey of Confidential Computing for Agentic AI](https://arxiv.org/abs/2605.03213)

**<font color=#1a73e8>作者：</font>** Javad Forough, Marios Kogias, Hamed Haddadi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic AI systems, specifically LLM-driven agents that plan, invoke tools, maintain persistent memory, and delegate tasks to peer agents via protocols such as MCP and A2A, introduce a threat surface that differs materially from standalone model inference. Agents accumulate sensitive context, hold credentials, and operate across pipelines no single party fully controls, enabling prompt injection, context exfiltration, credential theft, and inter-agent message poisoning. Current defenses operate entirely within the software stack and can be silently bypassed by a sufficiently privileged adversary such as a compromised cloud operator. Confidential computing (CC) offers a hardware-rooted alternative: Trusted Execution Environments (TEEs) isolate agent code and data from privileged system software, while remote attestation enables verifiable trust across distributed deployments. This survey synthesizes the design space in four parts: (i) a unified taxonomy of six TEE platforms (Intel SGX, Intel TDX, AMD SEV-SNP, ARM TrustZone, ARM CCA, and NVIDIA H100 CC) covering deployment roles and performance tradeoffs; (ii) an agent-centric threat model spanning perception, planning, memory, action, and coordination layers mapped to nine security goals; (iii) a comparative survey of CC-based defenses distinguishing findings that transfer from single-call inference versus what requires new agentic designs; and (iv) six open challenges including compound attestation for multi-hop agent chains and GPU-TEE performance at LLM scale. While several hardware trust primitives appear mature enough for targeted deployments, no broadly established end-to-end framework yet binds them into a coherent security substrate for production agentic AI.

---


### 6. [MAGE: Safeguarding LLM Agents against Long-Horizon Threats via Shadow Memory](https://arxiv.org/abs/2605.03228)

**<font color=#1a73e8>作者：</font>** Yuhui Wang, Tanqiu Jiang, Jiacheng Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As large language model (LLM)-powered agents are increasingly deployed to perform complex, real-world tasks, they face a growing class of attacks that exploit extended user-agent-environment interactions to pursue malicious objectives improbable in single-turn settings. Such long-horizon threats pose significant risks to the safe deployment of LLM agents in critical domains. In this paper, we present MAGE (Memory As Guardrail Enforcement), a novel defensive framework designed to counter a wide range of long-horizon threats. Inspired by the "shadow stack" abstraction in systems security, MAGE maintains a dedicated, safety-focused agentic memory that distills and retains safety-critical context across the agent's full execution trajectory, leveraging this shadow memory to proactively assess the risk of pending actions prior to their execution. Extensive evaluation demonstrates that MAGE substantially outperforms existing defenses across diverse long-horizon threats in detection accuracy, achieves early-stage detection for the majority of attacks, and introduces only negligible overhead to agent utility. To our best knowledge, MAGE represents the first framework to detect and mitigate long-horizon threats using an agentic memory approach, establishing a new paradigm for this critical challenge and opening promising directions for future research.

---


### 7. [SkCC: Portable and Secure Skill Compilation for Cross-Framework LLM Agents](https://arxiv.org/abs/2605.03353)

**<font color=#1a73e8>作者：</font>** Yipeng Ouyang, Yi Xiao, Yuhao Gu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-Agents have evolved into autonomous systems for complex task execution, with the this http URL specification emerging as a de facto standard for encapsulating agent capabilities. However, a critical bottleneck remains: different agent frameworks exhibit starkly different sensitivities to prompt formatting, causing up to 40% performance variation, yet nearly all skills exist as a single, format-agnostic Markdown version. Manual per-platform rewriting creates an unsustainable maintenance burden, while prior audits have found that over one third of community skills contain security vulnerabilities. To address this, we present SkCC, a compilation framework that introduces classical compiler design into agent skill development. At its core, SkIR - a strongly-typed intermediate representation - decouples skill semantics from platform-specific formatting, enabling portable deployment across heterogeneous agent frameworks. Around this IR, a compile-time Analyzer enforces security constraints via Anti-Skill Injection before deployment. Through a four-phase pipeline, SkCC reduces adaptation complexity from $O(m \times n)$ to $O(m + n)$. Experiments on SkillsBench demonstrate that compiled skills consistently outperform their original counterparts, improving pass rates from 21.1% to 33.3% on Claude Code and from 35.1% to 48.7% on Kimi CLI, while achieving sub-10ms compilation latency, a 94.8% proactive security trigger rate, and 10-46% runtime token savings across platforms.

---


### 8. [ARGUS: Defending LLM Agents Against Context-Aware Prompt Injection](https://arxiv.org/abs/2605.03378)

**<font color=#1a73e8>作者：</font>** Shihao Weng, Yang Feng, Jinrui Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rise of Large Language Model (LLM) agents, augmented with tool use, skills, and external knowledge, has introduced new security risks. Among them, prompt injection attacks, where adversaries embed malicious instructions into the agent workflow, have emerged as the primary threat. However, existing benchmarks and defenses are fundamentally limited as they assume context-insensitive settings in which the agent works under a fully specified user instruction, and the attacks are straightforward and context-independent. As a result, they fail to capture real-world deployments where agent behavior usually depends on dynamic context, not just the user prompt, and adversaries can adapt their attacks to different context. Similarly, existing defenses built on this narrow threat model overlook the nature of real-world agent delegation.
In this paper, we present AgentLure, a benchmark that captures context-dependent tasks and context-aware prompt injection attacks. AgentLure spans four agentic domains and eight attack vectors across diverse attack surfaces. Our evaluation shows that existing defenses often struggle in this setting, yielding poor performance against such attacks in agentic systems. To address this limitation, we propose ARGUS, a defense mechanism that enforces provenance-aware decision auditing for LLM agents. ARGUS constructs an influence provenance graph to track how untrusted context propagates into agent decisions and verify whether a decision is justified by trustworthy evidence before execution. Our evaluation shows ARGUS reduces attack success rate to 3.8% while preserving 87.5% task utility, significantly outperforming existing defenses and remaining robust against adaptive white-box adversaries.

---


### 9. [Exposing LLM Safety Gaps Through Mathematical Encoding:New Attacks and Systematic Analysis](https://arxiv.org/abs/2605.03441)

**<font color=#1a73e8>作者：</font>** Haoyu Zhang, Mohammad Zandsalimy, Shanu Sushmita  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) employ safety mechanisms to prevent harmful outputs, yet these defenses primarily rely on semantic pattern matching. We show that encoding harmful prompts as coherent mathematical problems -- using formalisms such as set theory, formal logic, and quantum mechanics -- bypasses these filters at high rates, achieving 46%--56% average attack success across eight target models and two established benchmarks. Crucially, the effectiveness depends not on mathematical notation itself, but on whether a helper LLM deeply reformulates the harmful content into a genuine mathematical problem: rule-based encodings that apply mathematical formatting without such reformulation perform no better than unencoded baselines. We introduce a novel Formal Logic encoding that achieves attack success comparable to Set Theory, demonstrating that this vulnerability generalizes across mathematical formalisms. Additional experiments with repeat post-processing confirm that these attacks are robust to simple prompt augmentation. Notably, newer models (GPT-5, GPT-5-Mini) show substantially greater robustness than older models, though they remain vulnerable. Our findings highlight fundamental gaps in current safety frameworks and motivate defenses that reason about mathematical structure rather than surface-level semantics.

---


### 10. [The Infinite Mutation Engine? Measuring Polymorphism in LLM-Generated Offensive Code](https://arxiv.org/abs/2605.03619)

**<font color=#1a73e8>作者：</font>** Gabriel Hortea, Juan Tapiador  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Malware authors have traditionally relied on polymorphic techniques to produce variants in the same malware family, complicating signature-based detection. Integrating generative AI into offensive toolchains enables attackers to synthesize structurally diverse payloads with identical behavior, raising the question of how much polymorphism LLMs provide. Recent work has assumed that LLMs can produce sufficiently polymorphic payloads, leaving unquantified the variation that emerges when an attacker repeatedly builds the same payload, or explicitly instructs the model to avoid prior implementations. In this work, we measure the polymorphic capacity of a commercial model (Claude Opus 4.6) as an automated malware generator. We build a dual-agent, four-stage pipeline that generates, tests, and refines a data-exfiltration payload comprising file traversal, encryption, exfiltration, and integration. We produce payloads in two settings: using prompts that specify only functional requirements, and using prompts that inject a structured history of prior outcomes to force divergence. We measure pairwise distances along structural (AST) and semantic (embedding) axes, finding that when polymorphism is not explicitly required, structural distances are high while semantic distances remain low; i.e., implementations diverge widely without changing high-level behavior. Explicit prompting substantially amplifies this structural diversity while preserving correctness, at the cost of roughly 5 times more tokens but only a small increase in LLM calls (from $4.2$ to $4.5$ per payload, with effective API costs of \$0.41 and \$0.73). These results show that a single commercial LLM can cheaply generate large populations of behaviorally equivalent yet structurally diverse payloads, facilitating the evasion of signature-based detection rules and similarity-based clustering.

---


### 11. [Tailored Prompts, Targeted Protection: Vulnerability-Specific LLM Analysis for Smart Contracts](https://arxiv.org/abs/2605.03697)

**<font color=#1a73e8>作者：</font>** Xing Zhang, Keyu Zhang, Taohong Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Smart contracts on blockchains are prone to diverse security vulnerabilities that can lead to significant financial losses due to their immutable nature. Existing detection approaches often lack flexibility across vulnerability types and rely heavily on manually crafted expert rules. In this paper, we present an LLM-based framework for practical smart contract vulnerability detection. We construct and release a large-scale dataset comprising 31,165 professionally annotated vulnerability instances collected from over 3,200 real-world projects across 15 major blockchain platforms. Our approach leverages precise AST-based context extraction and vulnerability-specific prompt design to instantiate customized detectors for 13 prevalent vulnerability categories. Experimental results demonstrate strong effectiveness, achieving an average positive recall of 0.92 and an average negative recall of 0.85, highlighting the potential of carefully engineered contextual prompting for scalable and high-precision smart contract security analysis.

---


### 12. [Generating Proof-of-Vulnerability Tests to Help Enhance the Security of Complex Software](https://arxiv.org/abs/2605.03956)

**<font color=#1a73e8>作者：</font>** Shravya Kanchi, Xiaoyan Zang, Ying Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Developers create modern software applications (Apps) on top of third-party libraries (Libs). When library vulnerabilities are reachable through application code, the applications can be vulnerable to software supply chain attacks. Prior work shows that developers often require concrete and executable evidence, i.e., proof-of-vulnerability (PoV) tests, to decide whether a reported dependency vulnerability poses a practical security risk to their application. However, manually crafting such tests is challenging, and existing tool support is insufficient to automate the procedure. To streamline test generation, we created PoVSmith -- a new approach that combines call path analysis, exemplar test, code context, and feedback into multiple prompts to guide a coding agent (i.e., Codex) and a large language model (i.e., GPT) for test generation, execution, and assessment. We evaluated PoVSmith on 33 $\langle$App, Lib$\rangle$ Java program pairs, where each App depends on a vulnerable Lib. PoVSmith revealed 158 unique application-level entry points (i.e., public methods) calling vulnerable library APIs; 152 (96\%) of them were correctly found, together with the call paths properly recognized. With such method call information, PoVSmith generated 152 tests, 84 (55\%) of which demonstrated feasible ways of attacking Apps by exploiting Lib vulnerabilities. PoVSmith substantially outperforms the state-of-the-art LLM-based approach, as it reduces human involvement while dramatically improving test quality. Our work contributes (1) a novel approach of agent-based test generation, (2) an iterative code refinement process driven by execution feedback, and (3) LLM-based quality assessment grounded in both the test context and execution logs.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
