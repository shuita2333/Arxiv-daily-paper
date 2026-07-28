# 🔐 大模型安全相关研究 | 2026年07月29日

> 本类共 **17** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [ReCon: A Resource-Constrained Benchmark for LLM-Based Cybersecurity Compliance Across Ingestion and Retrieval Pipelines](https://arxiv.org/abs/2607.22885)

**<font color=#1a73e8>作者：</font>** Rohit Negi, Rishik Jain, Soumyo V Chakarborty 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the increasingly aggressive cyber threat landscape for governments, businesses, and institutions, as information and/or cybersecurity implementations are increasingly under scrutiny by regulators, it has been pointed out that governance failure is one of the major reasons for a weakened cybersecurity posture. A major component of Cyber/information security governance is the development, adoption, and implementation of a comprehensive information and/or cyber security policy document. The policy document must be in compliance with international or national standards and, if possible, with regulatory guidelines. However, it is often observed that policy documents are often incomplete with respect to industry standards or regulations and require revision when subjected to a thorough audit. Identifying the gaps between the controls and processes documented in the policy and those required in the regulations or standards necessitates extensive manual effort. The advent of Generative AI tools such as Large Language Models (LLMs) led to use of LLMs and Agentic AI tools to automate such compliance checks, as seen in a few research publications in recent times. However, such reported use of LLMs are experimented with high resource environments such as expensive GPUs and memory based servers. For smaller organizations such expensive compute platform may not be easily available. In this article, we benchmark the compliance checking tasks on LLMs that do not require GPU and high memory usage and the effectiveness of such resource constrained LLMs in compliance checking. Our experiments demonstrated that the low resource LLMs can provide good agreement/accuracy in compliance checking of policy documents against standards by experimenting with ISO 27002:2022 controls against multiple policy documents.

---


### 2. [Mask2Shield: Strengthening LLM Safety against Neuron-Pruning Attacks](https://arxiv.org/abs/2607.23015)

**<font color=#1a73e8>作者：</font>** Ying JinCheng, Minghui Xu, Yinhao Xiao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are safety-aligned before deployment to reduce harmful content generation. Yet neuron-level pruning attacks show that refusal can depend on a small set of removable units: disabling them can remove safety behavior while leaving much of the model usable. To address this problem, we introduce Mask2Shield (M2S), a masked-forward alignment method that trains a model under this functional pruning. The masked student must recover a safe refusal through the remaining computation, while a frozen, unmasked teacher supplies complete benign answers to limit capability drift. Across ten model configurations, M2S reduces successful recomputed pruning attacks from 80--279 to 1--44 out of 313 prompts while generally preserving four capability benchmarks. We also evaluate M2S with TwinBreak, which uses a different neuron-selection rule and iterative pruning procedure. Together, these results show that M2S makes targeted pruning less effective by reducing reliance on a small, removable safety-neuron set.

---


### 3. [Traceable LLM Reasoning for Fake-Order Fraud Detection](https://arxiv.org/abs/2607.23075)

**<font color=#1a73e8>作者：</font>** Siqi You, Bingsong Xu, Zhixian Zheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Detecting fake-order fraud at scale remains a critical challenge for large online-to-offline (O2O) service platforms, as existing approaches often rely on expert-designed features, produce black-box decisions, and provide limited interpretability. To address these limitations, we propose DeepScrub, a reinforcement learning framework built upon large language models (LLMs) for fake-order fraud detection with traceable reasoning. DeepScrub introduces three innovations. First, a semantic unification module converts heterogeneous risk signals into textual descriptions that LLMs can understand. Second, continued pre-training on risk-control corpora injects domain knowledge, and task rewards jointly evaluate prediction correctness and reasoning quality. Third, the SUggest-REflect (SURE) mechanism incorporates expert feedback and model self-checking to iteratively refine reasoning paths. On a real-world fake-order fraud detection dataset, DeepScrub achieves a macro-F1 score of 85.3%, outperforming the best baseline by 2.7 percentage points. Our task-optimized 8B model further surpasses a 32B model, showing that domain adaptation can matter more than model scale in this setting. In a four-week live pilot, DeepScrub achieved 91.8% precision and 88.5% recall, improving over first-stage human reviewers by 16.6 and 38.8 percentage points. It reduced first-stage manual review workload by 94% and saved nearly one million RMB annually. These results show that DeepScrub improves fraud review accuracy, reduces first-stage review workload, and provides traceable evidence for production risk-review workflows.

---


### 4. [Poster: Rethinking Security in LLM Code Generation through Real-World Risk Scenarios](https://arxiv.org/abs/2607.23088)

**<font color=#1a73e8>作者：</font>** Lixun Ma, Ruolong Ma, Bei Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are widely used for code generation, yet their security behavior in realistic development workflows remains underexplored. Existing benchmarks often rely on explicitly specified security requirements, failing to capture real-world scenarios where prompts are frequently ambiguous or incomplete. In this paper, we adopt a developer-centric perspective and identify three representative risk scenarios that commonly lead to security vulnerabilities in LLM-generated code: Ambiguous Requirements, Under-Specified Operational Context, and Security--Functionality Conflict. Based on these scenarios, we construct a large-scale benchmark comprising 2,700 test cases, enabling fine-grained evaluation of LLM security under realistic conditions. Extensive evaluation of eight state-of-the-art LLMs reveals that all models exhibit average vulnerability rates exceeding 56\% across risk scenarios. We further demonstrate that security-aware prompting can substantially mitigate these risks, achieving up to 45\% improvement.

---


### 5. [False Prophets: On the Security of World Models in Agentic Systems](https://arxiv.org/abs/2607.23147)

**<font color=#1a73e8>作者：</font>** Erik Imgrund, Anna Wimbauer, Klim Kireev 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models now power autonomous agents capable of complex, multi-step tasks in different environments. Accurate and reliable execution of these tasks requires the agent to predict the results of its actions. Recent research proposes to enhance predictive capabilities via specially trained environment simulators-world models. While world models can improve performance, they can also mislead agents into executing harmful actions, creating significant security and privacy risks. In this paper, we raise security concerns regarding the usage of world models in agentic systems. We discover a range of world model specific vulnerabilities, which can be exploited in terminal-based agents to execute malicious code or extract sensitive data. To facilitate future development, we introduce a security benchmark dataset designed for text-based world models. We argue that some risks are intrinsic to approximate world modeling, and show that attackers can induce mispredictions in agentic pipelines with up to 95% success rate, possibly resulting in unintended command execution, denial of service, drainage of wallet and private information extraction. Finally, we provide practical recommendations for practitioners to mitigate the discovered harms and harden agentic systems.

---


### 6. [Isolated but Exposed: Persistence-Based Memory Extraction Attack on LLM Agents](https://arxiv.org/abs/2607.23444)

**<font color=#1a73e8>作者：</font>** Xinyu Gao, Wenyu Chen, Xiangtao Meng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-based agents extend large language models with long-term memory (LTM) that persists privacy-sensitive user data across sessions. Production systems mitigate extraction risks through memory isolation, binding each user's LTM to a unique identifier. This defense has blocked known attacks on shared storage, fostering the assumption that isolated LTM is secure. We identify the tool interface as an overlooked attack surface. Agents routinely embed LTM-retrieved data in tool invocation parameters, enabling a malicious tool to exfiltrate private memory without violating user-level isolation. Naive adaptations of user-side extraction techniques fail because the adversarial command's semantics interfere with retrieval precision, and platform-imposed tool-call limits constrain the extraction budget per trigger. We present SPORE, the first extraction attack designed for this threat model. SPORE decouples the adversarial command from retrieval anchors by persisting the command in short-term memory and emitting semantically pure anchors in tool responses. The restored retrieval precision enables a geometric coverage optimization over the embedding space that systematically steers anchors toward unexplored memory regions. To sustain extraction beyond tool-call limits, SPORE persists reactivation payloads in memory that automatically resume the attack within and across sessions without additional user triggers. SPORE achieves an 80.0% record extraction rate with unlimited triggers and 47.0% with only 20 triggers. In multi-user deployments, attackers can link extracted records to user identities, enabling targeted surveillance. These results demonstrate that memory isolation alone is insufficient and call for reexamining tool-side trust boundaries in agent architectures.

---


### 7. [Mission-Level Runtime Assurance for LLM-Assisted ISR Swarms over a Verification-Aware Fabric](https://arxiv.org/abs/2607.23532)

**<font color=#1a73e8>作者：</font>** Nikolaos Kekatos, Stylianos Basagiannis, Panagiotis Katsaros 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Swarms of LLM-assisted autonomous robots are increasingly proposed for cooperative intelligence, surveillance, and reconnaissance (ISR) in contested environments. A growing class of their assurance failures arises not within any single platform but across the swarm: individually-compliant actions compose into a mission-level violation: a prohibited objective split across platforms to evade per-platform lim- its, or a collective budget quietly exceeded. Per-platform guardrails miss these by construction, and contested communications let the violation hide behind lost or delayed evidence. We present a three-tier (platfor- m/squad/mission) compositional runtime-verification framework that de- composes a mission policy into per-agent and cross-agent aspects, aggre- gates per-platform verdicts over a verification-aware messaging fabric, and fuses them with an evidence-aware, two-axis (security x complete- ness) algebra whose provenance names the platforms that jointly trig- gered a violation. Because the fabric makes evidence loss and silence observable, unsupported negative verdicts are downgraded to an explicit unknown rather than reported as mission-wide all-clears. On a simulated ISR mission, an indirect prompt injection that causes real LLM planners to split a prohibited collection task across four platforms is invisible to every per-platform monitor yet detected compositionally with full prove- nance; under an injected fault campaign a best-effort central monitor emits silent false all-clears while the verification-aware fabric emits none

---


### 8. [The Illusion of Secure LLM Code: Closing the Security Gap via Iterative Reprompting](https://arxiv.org/abs/2607.23710)

**<font color=#1a73e8>作者：</font>** Ishpuneet Singh, Shreyas Mahajan, Gurjot Singh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly integrated into software development workflows, yet their ability to autonomously generate secure authentication code remains uncertain. This paper evaluates the security architecture of authentication systems generated by five prominent AI coding assistants through a bi-modal assessment framework combining static code analysis and dynamic penetration testing, mapped to NIST SP 800-63B guidelines. The study examines model behavior across four prompting strategies Basic, Secure, NIST-Based, and Reprompting to reflect varying levels of developer guidance. Empirical results demonstrate that code generated from functional or generically secure prompts consistently omits critical protections, particularly concerning brute-force resistance, session management, and robust password handling. While providing explicit, single-shot NIST context significantly improves compliance, the findings reveal that this remains structurally inadequate. Instead, iterative Reprompting: forcing models into a contextual self-auditing loop is strictly required to achieve a comprehensive, defense-in-depth security architecture. Ultimately, this study proves that current AI coding assistants do not produce secure-by-default applications, dictating that enterprise deployments must transition from single-shot prompt engineering to continuous, standards-driven verification pipelines.

---


### 9. [ZKP Security Tools and Verification: Coverage, Effectiveness, Adoption, and Challenges](https://arxiv.org/abs/2607.23752)

**<font color=#1a73e8>作者：</font>** Arman Kolozyan, Tom Sorger, Alexander Hicks 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Zero-knowledge proofs (ZKPs) have become a core technology for privacy and verifiable computing. They are used to secure blockchains that handle billions of dollars and identity applications dealing with sensitive personal data. However, ZKP systems are complex, and subtle implementation errors can completely break their guarantees, letting attackers forge money or false proofs of identity. Researchers and practitioners have therefore developed a growing set of bug detection and formal verification methods to secure these systems. Yet their real-world effectiveness and adoption remain unclear. In this paper, we aim to shed light on the state of ZKP security tooling. We first systematize the landscape of these tools and observe that most target Circom, leaving newer DSLs and zkVMs with limited support. We then evaluate six tools across 70 real-world vulnerabilities and find that while the tools detect 45.7% of bugs on isolated targets, their effectiveness drops to 19.6% on full codebases, with important vulnerability classes left unaddressed. We also present the first systematic analysis of formal verification efforts, revealing that current work focuses primarily on constraint correctness and identifying key gaps and risks. Finally, we survey 48 practitioners, showing that development and security remain human-led, LLMs are widely used, and practitioners prioritize tools with clearer guarantees and lower integration effort. Overall, our results highlight the need for better integration of security tooling with the development and auditing process, and we provide actionable insights for researchers and practitioners.

---


### 10. [TriShieldRAG: A Three-Ring Defense-in-Depth Framework Against Knowledge Corruption in Retrieval-Augmented Generation](https://arxiv.org/abs/2607.23838)

**<font color=#1a73e8>作者：</font>** Susil Kumar Mohanty, Rohit Patel, Kosuru Yuvaraj 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) lets a large language model answer questions using documents retrieved from an external knowledge base at query time. This makes RAG useful for private data, fast-changing information, and reducing hallucination, but it also means the model's answer is only as trustworthy as whatever the retriever hands it. If the knowledge base accepts writes from more than one party, an attacker needs only a handful of adversarial documents to steer the model toward a chosen wrong answer. PoisonedRAG demonstrated this: as few as five crafted documents flip an undefended system's answer roughly 90% of the time, and three natural single-stage defenses (perplexity filtering, query paraphrasing, knowledge-base expansion) leave attack success at 30% or higher.
We built TriShieldRAG to close that gap. Rather than relying on one checkpoint, we place three independent, formally specified rings across the pipeline: an Ingest Guard that screens documents for lexical and statistical poisoning signatures; a Retrieval Scorer that re-ranks the retrieved set by a provenance and consistency-weighted trust score; and a Cross-LLM Consensus stage that polls three architecturally diverse language models (Claude, Mistral Small, Llama 3.2) and allows one bounded re-retrieval on disagreement.
We derive the conditions under which Rings 2 and 3 are expected to work: a minority-poison assumption and an explicit provenance-tag assumption. Our reported configuration is consistent with this analysis, though we have not yet run the controlled poison-fraction sweep needed to confirm it independently. Evaluated against the non-adaptive attacker from the original PoisonedRAG, over a 5,000-document Wikipedia knowledge base with 10 target questions, the full pipeline reduces attack success rate from roughly 91% to roughly 13% while preserving accuracy on benign queries.

---


### 11. [ContainmentBench: Trace-Based Evaluation of Post-Injection Containment in Tool-Using LLM Agents](https://arxiv.org/abs/2607.23999)

**<font color=#1a73e8>作者：</font>** Wenhao Lan, Shan Li, Xinhua Lai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tool-using LLM agents process untrusted content, maintain memory, delegate across agents, and invoke side-effecting tools. Existing prompt-injection evaluations typically summarize security with terminal attack or policy outcomes, but equal endpoints can conceal different post-exposure traces and different losses of authorized utility. We introduce ContainmentBench, a sandboxed, trace-based benchmark that separately measures benchmark-defined endpoint policy compliance, instrumented logged propagation, recovery instrumentation, and authorized structured-action completion. In a pre-specified 17,640-rollout study with Qwen2.5-7B-Instruct, all 600 matched active-tainted pairs comparing taint-only and intent-aware enforcement have the same zero committed-harm outcome, yet 73.5% differ in logged trajectory or utility. Taint-only enforcement completes only 0.1642 of authorized tainted workflows; a trusted-ledger policy raises completion to 0.8567, while a strong tool-boundary baseline reaches 0.9233 under the same observed endpoint-policy outcomes. We also find that aggregate logged-spread rankings change with evidence-stage composition and denominator choice. These results show that a terminal policy label is not a sufficient statistic for operational post-exposure containment; evaluations should report endpoint, stage-stratified trajectory, and utility evidence separately, and should promote recovery evidence to comparative claims only where the corresponding controls are valid. The full-scale study is synthetic and single-model; the policy case additionally assumes a correct structured authorization ledger.

---


### 12. [Agentic Cloud Decoys: A Deception-Driven Framework for Autonomous Intrusion Investigation](https://arxiv.org/abs/2607.24006)

**<font color=#1a73e8>作者：</font>** Mohan Manivannan, Dalal Alharthi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cloud telemetry arrives at a scale that, paradoxically, makes intrusion understanding harder rather than easier. Attackers operate through legitimate identity, federated session tokens, and cloud native APIs indistinguishable from routine administration, and analysts spend an incident reconstructing context the logs already contain. We present Cloud Decoy AI Agent, a framework pairing a high fidelity cloud decoy with an autonomous language model agent that compresses the path from suspicious activity to an analyst ready report. Connecting a decoy to an agent is not a wiring exercise. The unit of investigation is the session rather than the event, and the session key is obscured by the identity layering federated credentials introduce. The agent's evidence horizon must be bounded, since an agent free to query full control plane history inherits the cost and false positive profile deception was meant to remove. And cloud telemetry is partly adversary authored, since object keys and user agent strings are attacker chosen values providers record verbatim, which makes any log to prompt path an indirect prompt injection channel that a decoy widens rather than narrows. We address the first two with a session aggregation operator over a pivot tuple drawn only from provider derived fields, and with dynamic prompt generation, a two stage prompt assembly enforcing a grounding invariant by carrying only fields the agent observed. We identify the third as an unaddressed exposure in this class of system, specify the mitigation it requires, and note our prototype does not implement it. Across ten controlled AWS S3 scenarios, nine were reconstructed completely, no report contained an assertion untraceable to an observed artifact, and latency was four to five minutes. We also state what this evaluation does not establish and name the comparisons that would settle it.

---


### 13. [A Cybersecurity MLPS Large Language Model with Multi-Path Retrieval Fusion](https://arxiv.org/abs/2607.24116)

**<font color=#1a73e8>作者：</font>** Qian Li, Zhenyan Qi, Liang Shen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Multi-Level Protection Scheme (MLPS) is a foundational system in China's cybersecurity governance framework. Therefore, accurate analysis and understanding of MLPS requirements are essential. At present, MLPS analysis still relies mainly on manual interpretation of standards and rule-based tools. This makes it hard to provide stable and consistent compliance analysis in complex application scenarios. The rise of large language models has created new opportunities for making MLPS work more intelligent. However, in standards-intensive and security-sensitive scenarios, general-purpose large language models often cannot ensure controllable reasoning or complete understanding of rules. This paper proposes a large language model framework for MLPS that integrates multiple retrieval strategies. It combines hierarchical retrieval, tree-based retrieval, and tokenization-based matching retrieval. This design helps maintain retrieval coverage while reducing the interference of irrelevant context in the reasoning process. To address the requirements of MLPS question answering for clause accuracy, conclusion traceability, and practical deployability, this paper adopts a evaluation method based on multi-dimensional weighted scoring to quantitatively assess model responses. In comparative experiments on ten typical questions, the proposed domain-specific large language model for MLPS achieved higher overall scores.

---


### 14. [Just Testing, Move Along: Evasion of LLM-based System Log Interpretation by Prompt Injection](https://arxiv.org/abs/2607.24174)

**<font color=#1a73e8>作者：</font>** Max Landauer, Florian Skopik, Markus Wurzenberger 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly integrated into Security Operations Center (SOC) workflows, where they support analysts in tasks such as the interpretation of system logs. However, the ability of LLMs to directly process untrusted textual input also introduces new attack surfaces. In particular, attackers can inject contextual information or explicit instructions into log entries in order to influence how malicious activity is interpreted by the model. Despite the growing adoption of LLMs for log analytics, the robustness of such systems against adversarial log injection remains largely unexplored. To address this gap, this paper presents a framework for evaluating prompt injection attacks against LLM-based log interpretation. Using log traces generated during real cyber attacks, our approach creates adversarial examples through generic injection generation, refinement, and attack-specific optimization. Our evaluation across multiple state-of-the-art LLMs shows that these injections can cause malicious log traces to be classified as benign despite containing clear indicators of compromise. As a potential remedy, we show that the explanations generated by the LLMs alongside their classifications frequently contain indicators of adversarial manipulation that can be leveraged to detect such attacks.

---


### 15. [DeepFaith: Evidence-Grounded LLMs for Faithful Incident Reporting in Multi-Stage APT Defense](https://arxiv.org/abs/2607.24348)

**<font color=#1a73e8>作者：</font>** Trung V. Phan, Tri Gia Nguyen, Thomas Bauschert  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Advanced Persistent Threats (APTs) are difficult to detect and interpret due to their multi-stage and stealthy nature. While recent autonomous defense systems leverage provenance graphs and learning-based models for detection and mitigation, their outputs remain largely machine-oriented and difficult for analysts to interpret. Large language models (LLMs) offer a promising interface for report generation, but often produce hallucinated or weakly grounded content. In this paper, we propose DeepFaith, an evidence-grounded framework for faithful incident reporting in multi-stage APT defense. DeepFaith transforms structured outputs from autonomous defense and explainability modules into natural-language reports that are explicitly aligned with underlying system evidence. The framework integrates a unified evidence representation, evidence-grounded prompting, faithfulness-aware generation, and post-generation verification to ensure that all generated statements are supported. Experiments in a realistic enterprise testbed demonstrate that DeepFaith improves faithfulness from 0.68 to 0.92, reduces unsupported claims from 0.32 to 0.08, and increases temporal consistency from 0.6 to 0.88, while maintaining concise reports and lower error rates than existing template-based and LLM-based solutions. These results show that evidence-grounded generation enables reliable, interpretable, and actionable reporting for security operations centers.

---


### 16. [When LLM Defenses Backfire: Characterizing Safety, Performance, and Cost Trade-offs](https://arxiv.org/abs/2607.24392)

**<font color=#1a73e8>作者：</font>** Tong Zhang, Zexin Li, Simin Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Jailbreak defenses are essential for protecting large language models (LLMs), but they can also introduce secondary costs that weaken model utility. We present a systematic study of these defense trade-offs along three dimensions: performance impact, over-refusal on benign inputs, and inference cost. Rather than treating defenses as a single class, we organize them by operational strategy and examine how different strategies correlate with different side-effect profiles. Across state-of-the-art defense methods, widely used benchmark datasets, and representative open-source LLMs, we find that defenses rarely improve downstream capability, but instead vary in how they trade safety gains against usability and efficiency. In particular, rule-based defenses best preserve task performance, highly conservative self-reflective defenses often increase over-refusal, and multi-round defenses incur the largest runtime overhead. These results provide both a benchmark for evaluating defense side effects and practical guidance for selecting defenses under deployment constraints.

---


### 17. [Agentic Permissions Policy Algebra for Taint Confinement in LLM Agents](https://arxiv.org/abs/2607.24625)

**<font color=#1a73e8>作者：</font>** Arseny Kravchenko, Vadim Liventsev, Innokentii Konstantinov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous LLM agents processing mixed-confidentiality data face severe security risks from prompt injection attacks and reasoning errors. While dynamic Information Flow Control (IFC) provides structural security guarantees, traditional taint tracking permanently taints an agent's context upon reading unvetted data, severely restricting downstream utility. We present APPA (Agentic Permissions Policy Algebra), an IFC framework that resolves this usability bottleneck through engine-managed context branching and prospective acquisition enforcement. Before data acquisition occurs, APPA prospectively evaluates label descents and missing prerequisites, generating actionable remedy plans (Authorize, Accept). To inspect unvetted data without polluting the primary context, a label-seeded child trajectory is spawned, absorbing label descent locally and allowing a trusted sanitizer to return a bounded derivative to the unchanged parent. Governed by a two-monoid model over security labels and shared event logs, we formally prove parent label preservation and merge confinement. Finally, we evaluate APPA on a multi-turn tool-chaining benchmark across four models: it suppresses exfiltration (31%-50% down to 0%-7% attack success), and on three of the four, branching recovers a substantial share of the utility that taint tracking alone forfeits.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
