# 🔐 大模型安全相关研究 | 2026年06月11日

> 本类共 **16** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Safecloud: A Distributed, Encrypted Storage Cloud for Streaming](https://arxiv.org/abs/2606.09870)

**<font color=#1a73e8>作者：</font>** Gregory Magarshak  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present Safecloud, a distributed, encrypted, self-pricing storage and streaming network whose storage and routing nodes never see plaintext and never hold keys. Each file is split into chunks, encrypted on the owner's device, and distributed across Drops (browser tabs storing ciphertext in IndexedDB) and Jets (federated routing servers). Only the owner, or an authorised grantee, can decrypt. We make five contributions: (1) A one-root key hierarchy: every key derives deterministically from a single root via HKDF, and owner and range-scoped grantee derive identical chunk keys (derivation agreement); a subtree key derives its range and nothing else (delegation containment). (2) Convergent content addressing: identical content yields identical ciphertext and identifiers, enabling deduplication without plaintext exposure, with identifiers binding authenticated ciphertext so a keyless Drop verifies integrity (blind verifiability). (3) Three parallel trees over one navigation path (Merkle for integrity, key-derivation for confidentiality, access for authorisation), with sound Merkle-verified retrieval. (4) The key tree doubles as a streaming index: a player derives each segment key in O(1), seeking by derivation, while parallel tracks (video, audio, captions) are independent subtrees unlockable per-track and per-segment, a combination we believe no prior encrypted-storage network offers. (5) Jets and Drops earn Safebux verifiably, kept honest by a one-signature proof-of-storage challenge under chilling-effect Proof-of-Corruption, a zero-sum economy that is significantly cheaper than Filecoin's proof-of-replication sealing (which is slow and provides no confidentiality). We give the architecture, cryptographic construction, a threat model, and an open-source reference implementation, stating precisely what is implemented versus designed.

---


### 2. [IDP-Bench: Benchmarking ability of LLMs to protect personal information in interdependent privacy contexts](https://arxiv.org/abs/2606.09908)

**<font color=#1a73e8>作者：</font>** Ayana Hussain, Soumya Sharma, Golnoosh Farnadi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are becoming widely deployed as personal AI assistants with access to sensitive user data, making privacy a major challenge for their design and evaluation. Prior work focuses mainly on individual-level risks, overlooking \textbf{interdependent privacy (IDP)}--where one person's data may be revealed by others without their knowledge or consent. We address this gap by introducing \textbf{IDP-Bench}: the first LLM benchmark for IDP scenarios, grounded in the Contextual Integrity (CI) framework. We evaluate eight open-source LLMs on their understanding of IDP scenarios across three levels of IDP reasoning using two LLM judges. Results show strong co-ownership recognition (6/8 models exceed 90\%) but persistent weaknesses in identifying CI parameters (information attribute, primary subject) and IDP-specific parameters such as secondary subjects, where 7/8 models score below 74\%. Models also struggle to judge sharing appropriateness (5/8 scoring below 77\%). While the ability to judge the appropriateness of sharing improves with scale, performance tends to decline in smaller models, and prompt sensitivity remains high on IDP-specific questions--highlighting the need for more targeted study of IDP in LLM privacy research. Data \& code available \href{this https URL}{here}.

---


### 3. [RadKey: An LLM-Guided RF Backscatter System for Through-Wall Keystroke Inference](https://arxiv.org/abs/2606.10148)

**<font color=#1a73e8>作者：</font>** Qijun Wang, Chunqi Qian, Huacheng Zeng  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In today's digitally connected world, keyboards remain the primary interface for inputting sensitive information, making them a persistent target for eavesdropping attacks. While prior keystroke inference techniques have exploited side-channel signals such as acoustics and vibrations, they typically rely on conspicuous, short-range sensors and require victim-specific data for model training, limiting their practicality, scalability, and stealth. In this paper, we present RadKey, an RF backscatter system for covert, long-range, through-wall keystroke eavesdropping. RadKey comprises two components: a compact batteryless backscatter tag and an RF reader. The tag captures keystroke-induced vibrations and acoustic signals, modulating them onto the frequency shift of its backscattered RF signal using two magnetically-coupled LC resonators. This design also enables spectral separation between the excitation and backscatter signals, mitigating self-interference for the RF reader and thus extending eavesdropping range. The RF reader demodulates the backscattered RF signal to infer typed content. It employs a dedicated signal processing pipeline that extracts user- and keyboard-independent keystroke features across time and frequency domains, enabling strong generalizability. To further enhance adaptability, RadKey integrates an LLM for online adaptation, leveraging LLM outputs as pseudo ground-truth labels to refine the classifier during runtime. We have built a prototype of the full RadKey system and evaluated it through extensive over-the-air experiments. Results show that RadKey achieves accurate and robust keystroke inference across diverse users in real-world settings. A demo video is available at: this https URL

---


### 4. [RECON: An LLM-Enhanced Backward Constraint Analysis Framework](https://arxiv.org/abs/2606.10264)

**<font color=#1a73e8>作者：</font>** Babangida Bappah, Lamine Noureddine, Umar Farooq 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> While traditional techniques, such as symbolic execution, provide a principled foundation for precise constraint reasoning in program analysis, they struggle to scale to modern software systems mainly due to path explosion, the need for function modeling, and the loss of semantic intent at low-level program representations. In complex execution environments such as Android, characterized by extensive framework interactions and event-driven behavior, these limitations are even more amplified. Thus, in this paper, we present a novel large language model (LLM)-enhanced backward constraint analysis framework that combines the precision of static program analysis with LLM's semantic understanding to extract precise execution constraints from Android bytecode. Our approach, titled RECON, performs backward path discovery from target method(s) to the application entry point(s), discovers method-level control-flow constraints, and leverages LLM reasoning to transform bytecode conditions into interpretable specifications. We evaluated RECON using five LLMs across 78 Android constraint-extraction scenarios and compared it with traditional symbolic execution on real-world applications. Results demonstrate that our approach operates 5.8X faster than traditional symbolic execution, with a 100% success rate, while maintaining logical equivalence and providing significantly more precise and interpretable output. We further evaluated RECON for malware analysis on 100 samples. The results indicate an 84% success rate in generating semantic constraints that lead to the execution of dangerous API behaviors and in detecting complex constraints across multiple execution paths.

---


### 5. [Benchmarking and Exploring the Capabilities of LLMs for Attack Investigations](https://arxiv.org/abs/2606.10281)

**<font color=#1a73e8>作者：</font>** Aniket Anand, Yiwei Hou, Daniel Fields 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper presents AuditBench, a new benchmark dataset for evaluating the capabilities of LLMs at investigating security-related system audit logs. We design and use this benchmark to explore the performance of LLMs on four log-investigation tasks that incident response teams commonly perform, ranging from triaging alerts generated by detectors to identifying persistence mechanisms on compromised systems. AuditBench consists of system audit logs collected from Linux and Windows machines, and spans over 50 different security investigation scenarios, including both malicious and benign activity. Using our benchmark, we evaluate and analyze the performance of five frontier LLMs at analyzing audit logs for attack investigations. Our analysis illuminates how LLM performance and error profiles vary according to different design choices, such as differences in model size, data representation, prompt construction, and specific investigation tasks. Additionally, we characterize the quality of the explanations produced by LLMs and the types of errors that models make across our benchmark. Collectively, our work provides a foundation for assessing the capabilities of LLMs for investigating security logs, novel insights for practitioners using LLMs in security operations, and important directions for future research.

---


### 6. [Game-Theoretic Multi-Agent Control for Robust Contextual Reasoning in LLMs](https://arxiv.org/abs/2606.10322)

**<font color=#1a73e8>作者：</font>** Saeid Jamshidi, Amin Nikanjam, Arghavan Moradi Dakhel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) in multi-turn interactions maintain evolving context rather than generating isolated responses, making them vulnerable to prompt-injection and context-poisoning attacks in which locally plausible adversarial fragments gradually distort reasoning trajectories. Existing defenses mainly filter individual outputs and often ignore context evolution across turns, leaving long-horizon reasoning exposed. Although the Model Context Protocol (MCP) standardizes context exchange and tool invocation, it functions as a passive routing layer and does not enforce contextual stability. To address these limitations, we introduce the Game-Theoretic Secure Model Context Protocol (GT-MCP), a controller-driven multi-agent method that treats context management as a closed-loop dynamical process. GT-MCP coordinates three heterogeneous LLM agents and selects outputs through a trust function that jointly evaluates causal consistency against a validated context graph, semantic agreement among agents, and distributional drift over time. When instability is detected, a rollback-based self-healing mechanism restores the validated context and prevents unsupported fragments from propagating. Empirical evaluation over 500 interaction turns under an adaptive adversarial threat model shows that contextual drift remains bounded in 99.6% of turns, with recovery required in only 0.4%. Per-turn utility remains tightly concentrated, with median = -0.19, P05 = -0.72, and P95 = 0.30; severe degradation below -1 occurs in only 0.4% of cases, and no injection attempt succeeds at the controller level. Selected outputs maintain stable win rates above 98%, and computational overhead remains predictable, with latency per token = 1.63e-3 s.

---


### 7. [Semantic Multi-Agent Intrusion Detection for IoT:Zero-Day and Adversarial Threats with Risk-Aware Reasoning](https://arxiv.org/abs/2606.10323)

**<font color=#1a73e8>作者：</font>** Saeid Jamshidi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid proliferation of Internet of Things (IoT) devices has enabled unprecedented automation and connectivity, but it has also substantially increased the attack surface, exposing networks to sophisticated cyber threats, including zero-day and adversarial intrusions. Traditional Intrusion Detection Systems (IDS) struggle to generalize to unseen attacks, often require substantial computational resources, and lack interpretability, particularly in resource-constrained and heterogeneous IoT networks. Recent advances, including Deep Learning (DL), open-set detection, and Large Language Model (LLM)-based semantic reasoning, address some of these challenges but typically focus on zero-day and adversarial threats and rarely combine semantic reasoning with multi-agent systems. To overcome these limitations, we propose a semantic multi-agent ID that integrates four specialized agents (e.g., Scout, Mutator, Auditor, and Arbiter) that leverage semantic embeddings and multi-stage probabilistic decision fusion. The Scout induces structured hypotheses from semantic embeddings; the Mutator generates adversarially constrained variants; the Auditor evaluates consistency and filters unreliable outputs; and the Arbiter produces interpretable, risk-aware alerts. Extensive experiments across multiple real-world IoT datasets demonstrate that the proposed system achieves 95.9% overall detection accuracy, reduces false-positive rates to 6.8%, improves zero-day detection to 87.9%, and maintains computational efficiency suitable for edge deployment.

---


### 8. [Assessing Automated Prompt Injection Attacks in Agentic Environments](https://arxiv.org/abs/2606.10525)

**<font color=#1a73e8>作者：</font>** David Hofer, Edoardo Debenedetti, Florian Tramèr  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Indirect prompt injection poses a critical threat to LLM agents that interact with untrusted external data, yet automated attack methods--proven effective for jailbreaking--remain underexplored in realistic agentic settings. We present a comprehensive empirical evaluation of automated prompt injection attacks against LLM agents, adapting both white-box (GCG) and black-box (TAP) methods to the agentic setting within the AgentDojo framework. We evaluate across 80 task pairs spanning four domains and multiple models, and find that black-box optimization substantially outperforms gradient-based methods, a gap we attribute to GCG's optimization instability under reasonable compute budgets. We also find that TAP's effectiveness depends on the attacker model, as both general capability and safety tuning affect attack success--stronger models produce more effective injections, while safety-tuned attackers can refuse to generate adversarial prompts. Task-universal attacks transfer effectively to unseen tasks and out-of-distribution domains, but attacks optimized on smaller open-source models do not transfer to frontier models like GPT-5. These findings highlight automated prompt injection as a credible but model-dependent threat, with significant barriers remaining for model-agnostic exploitation.

---


### 9. [Do LLMsMakeNeural Distinguishers Wise?](https://arxiv.org/abs/2606.10692)

**<font color=#1a73e8>作者：</font>** Tatsuya Sakagami, Masashi Hisai, Naoto Yanai  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Neural distinguishers are a cryptanalysis method for symmetric-key cryptography that trains machine learning models on pairs of plaintexts and ciphertexts with specific differences in order to recover a secret key. To the best of our knowledge, no existing work has explored the use of large language models (LLMs) for neural distinguishers. In this paper, we propose LLM-based neural distinguishers through a prompt design and conduct extensive experiments with them on SPECK-32/64 to investigate whether LLMs can strengthen neural distinguishers. We then found three key insights. First, by comparing the results of LLM-based neural distinguishers with ResNet in the existing work, we demonstrate that LLMs provide no observable improvement in the performance of neural distinguishers. Second, we confirm that, at high rounds, the choice of differences is no longer effective for LLM-based neural distinguishers as well as ResNet. Third, we show that the performance of LLM-based neural distinguishers can be significantly improved by incorporating only the XOR operation results as a prompt design.

---


### 10. [MemVenom: Triggered Poisoning of Multimodal Memories in Web Agents](https://arxiv.org/abs/2606.10742)

**<font color=#1a73e8>作者：</font>** Yv Zhang, Hao Sun, Hao Fang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> External memory has become a core component of modern web agents, enabling long-horizon reasoning through the retrieval of past experiences. However, this paradigm introduces a critical vulnerability: malicious content injected into memory can be persistently recalled and repeatedly influence agent behavior. In this work, we identify and systematically study multimodal memory poisoning, an overlooked yet practical attack surface in web-agent systems. We propose MemVenom, a unified black-box attack framework that poisons graph-structured external memory with coordinated text-image evidence. Our method consists of a two-stage design: (1) a trigger-conditioned retrieval attack that ensures high-probability recall of malicious memory, and (2) a post-retrieval attack induction that leverages adversarial perturbations and stealthy OCR injection to override the original user objective. Unlike prior attacks that operate on prompts or text-only memory, our approach enables persistent, reusable, and goal-agnostic attacks without modifying model parameters or re-optimizing malicious tasks. Experiments across multiple web-agent frameworks and vision-language models demonstrate that MemVenom achieves strong end-to-end attack success with minimal impact on benign performance, reaching up to 99.15% on GPT-5-family web agents, while transferring effectively across architectures and model scales.

---


### 11. [Toward Secure LLM Agents: Threat Surfaces, Attacks, Defenses, and Evaluation](https://arxiv.org/abs/2606.10749)

**<font color=#1a73e8>作者：</font>** Yuchen Ling, Shengcheng Yu, Zhenyu Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are rapidly moving from conversational interfaces to software components that plan, invoke tools, maintain memory, and act on external environments. This transition changes the nature of security risk. In agentic settings, failures are no longer limited to unsafe text generation. Untrusted content may redirect control flow, misuse tool privileges, corrupt persistent state, leak sensitive information, or trigger harmful external actions. At the same time, research on LLM agent security is expanding quickly but remains fragmented across attack families, defense layers, application domains, and evaluation settings. This paper synthesizes 247 papers through a lifecycle-based, systems-oriented framework that models agent security around the interaction of information flow, delegated authority, and persistent state. We organize the literature around four questions: how LLM agent security should be modeled, which threat surfaces and attack families dominate, what defenses have been proposed and with what tradeoffs, and how security claims are evaluated. We find that prompt injection and tool-mediated control-flow hijacking still dominate the field, while persistent state corruption and multi-agent propagation are becoming central emerging concerns. We further find that current defenses provide useful building blocks but remain weakly compositional, and that existing benchmarks still underrepresent long-horizon, stateful, and deployment-sensitive risks. We argue that secure LLM agents require explicit trust boundaries, principled privilege control, provenance-aware state management, and evaluation practices aligned with realistic operational settings.

---


### 12. [Securing Code Understanding: Detecting Natural Backdoor Vulnerability in Code Language Models](https://arxiv.org/abs/2606.10846)

**<font color=#1a73e8>作者：</font>** Yuchen Chen, Weisong Sun, Haocheng Huang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Code Language Models (CodeLMs) have become integral to software engineering, significantly advancing code intelligence tasks. However, their widespread adoption has raised critical security concerns, particularly regarding susceptibility to backdoor attacks. Recent studies have uncovered naturally occurring backdoors, referred to as natural backdoors, in normally trained deep learning models. Despite posing threats as serious as those introduced through data poisoning, security implications of natural backdoor vulnerabilities in CodeLMs remain poorly understood.
In this paper, we conduct a thorough empirical study of natural backdoor vulnerabilities in CodeLMs across various model architectures and code intelligence tasks. Specifically, we examine potential natural backdoor vulnerabilities across 44 scenarios, demonstrating that natural backdoors are prevalent and intrinsic to CodeLMs. We reveal differences between injected and natural backdoor vulnerabilities at both the model and parameter levels. We then analyze the transferability of natural backdoor vulnerabilities from three perspectives: datasets, model architectures, and shared knowledge. We further investigate the causes of natural backdoors from two aspects: training datasets and the model training procedure. We evaluate existing backdoor defense techniques, including pre-training, in-training, and post-training defenses, in mitigating natural backdoors. Finally, we propose ScanNBT, a novel detection method designed to improve comprehensive detection of natural backdoor vulnerabilities in CodeLMs. We aim for our findings to enhance understanding of these vulnerabilities and provide insights for strengthening CodeLM security against backdoor threats.

---


### 13. [Training LLMs to Enforce Multi-Level Instruction Hierarchies via Gravity-Weighted Direct Preference Optimization](https://arxiv.org/abs/2606.10860)

**<font color=#1a73e8>作者：</font>** Lena S. Bolliger, Lena A. Jäger  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Production LLMs receive instructions from sources with very different levels of trust, yet attend to every token with uniform architectural privilege. This is the structural vulnerability that enables malicious prompt injections and, more broadly, leaves models without a principled way to resolve conflicts between legitimate but competing instructions. A common training-based response is to teach models an explicit instruction hierarchy; existing approaches, however, formalize hierarchies of only three or four levels, treat all violations as equally severe, and rarely evaluate the full set of pairwise level interactions. We formalize a k-level instruction hierarchy problem and instantiate it for k=5, yielding ten pairwise priority relations that a compliant model must enforce. We then introduce Gravity-Weighted DPO (GW-DPO), a preference-optimization objective whose per-sample offset scales with the structural distance between conflicting levels under a linear or bilateral schedule, the latter weighting severity by both the privilege gap and the privilege of the victim level. Combined with hierarchy-specific delimiter tokens (Chen et al., 2025) and Instructional Segment Embeddings (ISE; Wu et al., 2025), GW-DPO with the bilateral schedule Pareto-improves over standard DPO and the linear variant on Llama-3.1-8B-Instruct, raising macro pairwise priority adherence while keeping over-refusal at half the standard DPO rate. Ablations isolate ISE as a refusal-threshold calibrator and recast five- versus three-level training as a generality-specialization tradeoff.

---


### 14. [Comparative Analysis of Inference-Time Defense Methods for Multimodal Large Language Models](https://arxiv.org/abs/2606.10904)

**<font color=#1a73e8>作者：</font>** Bulat Nutfullin, Vladimir Evgrafov, Dmitry Namiot  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) now appear in safety-critical applications, but the visual channel leaves them open to adversarial attacks that predominantly text-oriented safety alignment addresses only in part. Retraining a model for each new vulnerability class is usually too expensive to be practical. We report a comparative empirical evaluation of three inference-time defense methods and their combinations, run on eight models from the InternVL and Qwen-VL families across seven safety benchmarks that span four attack classes and total 9,000 evaluation samples. Every figure below comes from the same unified proxy classifier. Five findings emerge from the evaluation. First, within the evaluated models and benchmarks, no single defense dominates across all settings: what works depends on the model's baseline safety and on the attack type. Second, combining defenses directly drives benign-query over-refusal to 97-100% across all eight evaluated models, and SmoothVLM on its own reaches 99.2-100%. Third, a simple safety prompt keeps utility largely intact (0.0-18.2% over-refusal across all eight models, five of them below 7%, although two exceeded 15%) while still yielding moderate safety gains. Fourth, different attack classes expose different weaknesses across the evaluated setup, which is why multi-benchmark evaluation matters. Fifth, in a preliminary whitebox test on two models (n=20), text-level defenses suppressed a PGD visual attack that had succeeded without any defense: the defenses act at the output stage, where gradient optimization has limited direct leverage in the tested configuration. Read together, these results argue for adaptive defense selection rather than a single fixed defense configuration.

---


### 15. [Context-Based Adversarial Attacks on AI Code Generators: Vulnerability Analysis and Implications](https://arxiv.org/abs/2606.10945)

**<font color=#1a73e8>作者：</font>** Walther A. Del Orbe, John D. Hastings, Varghese Vaidyan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI-powered code generation systems have transformed software development but introduce critical inference-time security vulnerabilities. This research presents a systematic investigation of context-based adversarial attacks, where strategically crafted contextual inputs, including comments, documentation, variable names, bias large language models toward generating exploitable code. Through 2,800 controlled experiments across CodeT5+, CodeLlama, GPT-3.5-Turbo, and GPT-4, we quantify attack effectiveness and defense mechanisms. Results demonstrate that adversarial conditions increase vulnerability generation 10.7x (from 3.5% to 37.4%), with direct instruction attacks achieving 100% success on GPT-3.5-Turbo. Cross-model transferability reaches 60-100%, indicating systemic architectural vulnerabilities rather than model-specific flaws. Our dual-layer defense framework achieves 89.1% detection rate with 0.3% false positives and 520ms latency, demonstrating practical feasibility for real-time deployment in development environments.

---


### 16. [OpenPCC: Open and Confidential LLM Serving on Commodity TEEs](https://arxiv.org/abs/2606.11145)

**<font color=#1a73e8>作者：</font>** Haoling Zhou, Shixuan Zhao, Chao Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Generative AI applications such as personal AI agents, image generators, and chat assistants offer advanced capabilities to improve user experience. Behind the scenes, Large Language Models (LLMs) that power these services require a massive amount of computation and are usually deployed in the cloud, available as APIs, meaning that a user's request has to be sent to a Cloud Inference Service (CIS) for processing. However, the strong capabilities of LLM also mean that user's requests now contain much more personal sensitive or enterprise confidential information, demanding equally strong protection in CIS. While early industry efforts such as Apple Private Cloud Compute (PCC) and Google Private AI Compute have emerged to show the potential of secure CIS, they are not adoptable for deployment by others due to their reliance on proprietary hardware and closed ecosystem. In addition, they all suffer from their own design glitches that can undermine the ambitious goal of bringing in true privacy protection to end users. In this paper, we present our analysis of the fundamental requirements of building a secure yet open CIS. We then present OpenPCC, a Confidential CIS framework that does not rely on proprietary hardware but instead uses commercially available TEEs. We implement an open-source prototype and characterize it end-to-end on a Llama-3 8B vLLM workload, separating OpenPCC's own cost from the underlying TEE hardware. Our analysis and evaluation demonstrated the feasibility and security of the system.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
