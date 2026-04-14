# 🔐 大模型安全相关研究 | 2026年04月15日

> 本类共 **17** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

---

### 1. [ADAM: A Systematic Data Extraction Attack on Agent Memory via Adaptive Querying](https://arxiv.org/abs/2604.09747)

**<font color=#1a73e8>作者：</font>** Xingyu Lyu, Jianfeng He, Ning Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents have achieved rapid adoption and demonstrated remarkable capabilities across a wide range of applications. To improve reasoning and task execution, modern LLM agents would incorporate memory modules or retrieval-augmented generation (RAG) mechanisms, enabling them to further leverage prior interactions or external knowledge. However, such a design also introduces a group of critical privacy vulnerabilities: sensitive information stored in memory can be leaked through query-based attacks. Although feasible, existing attacks often achieve only limited performance, with low attack success rates (ASR). In this paper, we propose ADAM, a novel privacy attack that features data distribution estimation of a victim agent's memory and employs an entropy-guided query strategy for maximizing privacy leakage. Extensive experiments demonstrate that our attack substantially outperforms state-of-the-art ones, achieving up to 100% ASRs. These results thus underscore the urgent need for robust privacy-preserving methods for current LLM agents.

---


### 2. [Backdoors in RLVR: Jailbreak Backdoors in LLMs From Verifiable Reward](https://arxiv.org/abs/2604.09748)

**<font color=#1a73e8>作者：</font>** Weiyang Guo, Zesheng Shi, Zeen Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) is an emerging paradigm that significantly boosts a Large Language Model's (LLM's) reasoning abilities on complex logical tasks, such as mathematics and programming. However, we identify, for the first time, a latent vulnerability to backdoor attacks within the RLVR framework. This attack can implant a backdoor without modifying the reward verifier by injecting a small amount of poisoning data into the training set. Specifically, we propose a novel trigger mechanism designated as the \ourapproach (ACB). The attack exploits the RLVR training loop by assigning substantial positive rewards for harmful responses and negative rewards for refusals. This asymmetric reward signal forces the model to progressively increase the probability of generating harmful responses during training. Our findings demonstrate that the RLVR backdoor attack is characterized by both high efficiency and strong generalization capabilities. Utilizing less than 2\% poisoned data in train set, the backdoor can be successfully implanted across various model scales without degrading performance on benign tasks. Evaluations across multiple jailbreak benchmarks indicate that activating the trigger degrades safety performance by an average of 73\%. Furthermore, the attack generalizes effectively to a wide range of jailbreak methods and unsafe behaviors. Code is available at this https URL.

---


### 3. [Conflicts Make Large Reasoning Models Vulnerable to Attacks](https://arxiv.org/abs/2604.09750)

**<font color=#1a73e8>作者：</font>** Honghao Liu, Chengjin Xu, Xuhui Jiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) have achieved remarkable performance across diverse domains, yet their decision-making under conflicting objectives remains insufficiently understood. This work investigates how LRMs respond to harmful queries when confronted with two categories of conflicts: internal conflicts that pit alignment values against each other and dilemmas, which impose mutually contradictory choices, including sacrificial, duress, agent-centered, and social forms. Using over 1,300 prompts across five benchmarks, we evaluate three representative LRMs - Llama-3.1-Nemotron-8B, QwQ-32B, and DeepSeek R1 - and find that conflicts significantly increase attack success rates, even under single-round non-narrative queries without sophisticated auto-attack techniques. Our findings reveal through layerwise and neuron-level analyses that safety-related and functional representations shift and overlap under conflict, interfering with safety-aligned behavior. This study highlights the need for deeper alignment strategies to ensure the robustness and trustworthiness of next-generation reasoning models. Our code is available at this https URL. Warning: This paper contains inappropriate, offensive and harmful content.

---


### 4. [Like a Hammer, It Can Build, It Can Break: Large Language Model Uses, Perceptions, and Adoption in Cybersecurity Operations on Reddit](https://arxiv.org/abs/2604.09998)

**<font color=#1a73e8>作者：</font>** Souradip Nath, Chih-Yi Huang, Aditi Ganapathi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have recently emerged as promising tools for augmenting Security Operations Center (SOC) workflows, with vendors increasingly marketing autonomous AI solutions for SOCs. However, there remains a limited empirical understanding of how such tools are used, perceived, and adopted by real-world security practitioners. To address this gap, we conduct a mixed-methods analysis of discussions in cybersecurity-focused forums to learn how a diverse group of practitioners use and perceive modern LLM tools for security operations. More specifically, we analyzed 892 posts between December 2022 and September 2025 from three cybersecurity-focused forums on Reddit, and, using a combination of qualitative coding and statistical analysis, examined how security practitioners discuss LLM tools across three dimensions: (1) their stated tools and use cases, (2) the perceived pros and cons of each tool across a set of critical factors, and (3) their adoption of such tools and the expected impacts on the cybersecurity industry and individual analysts. Overall, our findings reveal nuanced patterns in LLM tools adoption, highlighting independent use of LLMs for low-risk, productivity-oriented tasks, alongside active interest around enterprise-grade, security-focused LLM platforms. Although practitioners report meaningful gains in efficiency and effectiveness in LLM-assisted workflows, persistent issues with reliability, verification overheads, and security risks sharply constrain the autonomy granted to LLM tools. Based on these results, we also provide recommendations for developing and adopting LLM tools to ensure the security of organizations and the safety of cybersecurity practitioners.

---


### 5. [PlanGuard: Defending Agents against Indirect Prompt Injection via Planning-based Consistency Verification](https://arxiv.org/abs/2604.10134)

**<font color=#1a73e8>作者：</font>** Guangyu Gong, Zizhuang Deng  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents are increasingly integrated into critical systems, leveraging external tools to interact with the real world. However, this capability exposes them to Indirect Prompt Injection (IPI), where attackers embed malicious instructions into retrieved content to manipulate the agent into executing unauthorized or unintended actions. Existing defenses predominantly focus on the pre-processing stage, neglecting the monitoring of the model's actual behavior. In this paper, we propose PlanGuard, a training-free defense framework based on the principle of Context Isolation. Unlike prior methods, PlanGuard introduces an isolated Planner that generates a reference set of valid actions derived solely from user instructions. In addition, we design a Hierarchical Verification Mechanism that first enforces strict hard constraints to block unauthorized tool invocations, and subsequently employs an Intent Verifier to validate whether parameter deviations are benign formatting variances or malicious hijacking. Experiments on the InjecAgent benchmark demonstrate that PlanGuard effectively neutralizes these attacks, reducing the Attack Success Rate (ASR) from 72.8% to 0%, while maintaining an acceptable False Positive Rate of 1.49%. Furthermore, our method is model-agnostic and highly compatible.

---


### 6. [Jailbreaking the Matrix: Nullspace Steering for Controlled Model Subversion](https://arxiv.org/abs/2604.10326)

**<font color=#1a73e8>作者：</font>** Vishal Pramanik, Maisha Maliha, Susmit Jha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models remain vulnerable to jailbreak attacks -- inputs designed to bypass safety mechanisms and elicit harmful responses -- despite advances in alignment and instruction tuning. We propose Head-Masked Nullspace Steering (HMNS), a circuit-level intervention that (i) identifies attention heads most causally responsible for a model's default behavior, (ii) suppresses their write paths via targeted column masking, and (iii) injects a perturbation constrained to the orthogonal complement of the muted subspace. HMNS operates in a closed-loop detection-intervention cycle, re-identifying causal heads and reapplying interventions across multiple decoding attempts. Across multiple jailbreak benchmarks, strong safety defenses, and widely used language models, HMNS attains state-of-the-art attack success rates with fewer queries than prior methods. Ablations confirm that nullspace-constrained injection, residual norm scaling, and iterative re-identification are key to its effectiveness. To our knowledge, this is the first jailbreak method to leverage geometry-aware, interpretability-informed interventions, highlighting a new paradigm for controlled model steering and adversarial safety circumvention.

---


### 7. [The Blind Spot of Agent Safety: How Benign User Instructions Expose Critical Vulnerabilities in Computer-Use Agents](https://arxiv.org/abs/2604.10577)

**<font color=#1a73e8>作者：</font>** Xuwei Ding, Skylar Zhai, Linxin Song 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Computer-use agents (CUAs) can now autonomously complete complex tasks in real digital environments, but when misled, they can also be used to automate harmful actions programmatically. Existing safety evaluations largely target explicit threats such as misuse and prompt injection, but overlook a subtle yet critical setting where user instructions are entirely benign and harm arises from the task context or execution outcome. We introduce OS-BLIND, a benchmark that evaluates CUAs under unintended attack conditions, comprising 300 human-crafted tasks across 12 categories, 8 applications, and 2 threat clusters: environment-embedded threats and agent-initiated harms. Our evaluation on frontier models and agentic frameworks reveals that most CUAs exceed 90% attack success rate (ASR), and even the safety-aligned Claude 4.5 Sonnet reaches 73.0% ASR. More interestingly, this vulnerability becomes even more severe, with ASR rising from 73.0% to 92.7% when Claude 4.5 Sonnet is deployed in multi-agent systems. Our analysis further shows that existing safety defenses provide limited protection when user instructions are benign. Safety alignment primarily activates within the first few steps and rarely re-engages during subsequent execution. In multi-agent systems, decomposed subtasks obscure the harmful intent from the model, causing safety-aligned models to fail. We will release our OS-BLIND to encourage the broader research community to further investigate and address these safety challenges.

---


### 8. [Critical-CoT: A Robust Defense Framework against Reasoning-Level Backdoor Attacks in Large Language Models](https://arxiv.org/abs/2604.10681)

**<font color=#1a73e8>作者：</font>** Vu Tuan Truong, Long Bao Le  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs), despite their impressive capabilities across domains, have been shown to be vulnerable to backdoor attacks. Prior backdoor strategies predominantly operate at the token level, where an injected trigger causes the model to generate a specific target word, choice, or class (depending on the task). Recent advances, however, exploit the long-form reasoning tendencies of modern LLMs to conduct reasoning-level backdoors: once triggered, the victim model inserts one or more malicious reasoning steps into its chain-of-thought (CoT). These attacks are substantially harder to detect, as the backdoored answer remains plausible and consistent with the poisoned reasoning trajectory. Yet, defenses tailored to this type of backdoor remain largely unexplored. To bridge this gap, we propose Critical-CoT, a novel defense mechanism that conducts a two-stage fine-tuning (FT) process on LLMs to develop critical thinking behaviors, enabling them to automatically identify potential backdoors and refuse to generate malicious reasoning steps. Extensive experiments across multiple LLMs and datasets demonstrate that Critical-CoT provides strong robustness against both in-context learning-based and FT-based backdoor attacks. Notably, Critical-CoT exhibits strong cross-domain and cross-task generalization. Our code is available at hthttps://github.com/tuanvu171/Critical-CoT.

---


### 9. [Detecting RAG Extraction Attack via Dual-Path Runtime Integrity Game](https://arxiv.org/abs/2604.10717)

**<font color=#1a73e8>作者：</font>** Yuanbo Xie, Yingjie Zhang, Yulin Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) systems augment large language models with external knowledge, yet introduce a critical security vulnerability: RAG Knowledge Base Leakage, wherein adversarial prompts can induce the model to divulge retrieved proprietary content. Recent studies reveal that such leakage can be executed through adaptive and iterative attack strategies (named RAG extraction attack), while effective countermeasures remain notably lacking. To bridge this gap, we propose CanaryRAG, a runtime defense mechanism inspired by stack canaries in software security. CanaryRAG embeds carefully designed canary tokens into retrieved chunks and reformulates RAG extraction defense as a dual-path runtime integrity game. Leakage is detected in real time whenever either the target or oracle path violates its expected canary behavior, including under adaptive suppression and obfuscation. Extensive evaluations against existing attacks demonstrate that CanaryRAG provides robust defense, achieving substantially lower chunk recovery rates than state-of-the-art baselines while imposing negligible impact on task performance and inference latency. Moreover, as a plug-and-play solution, CanaryRAG can be seamlessly integrated into arbitrary RAG pipelines without requiring retraining or structural modifications, offering a practical and scalable safeguard for proprietary data.

---


### 10. [Beyond A Fixed Seal: Adaptive Stealing Watermark in Large Language Models](https://arxiv.org/abs/2604.10893)

**<font color=#1a73e8>作者：</font>** Shuhao Zhang, Yuli Chen, Jiale Han 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Watermarking provides a critical safeguard for large language model (LLM) services by facilitating the detection of LLM-generated text. Correspondingly, stealing watermark algorithms (SWAs) derive watermark information from watermarked texts generated by victim LLMs to craft highly targeted adversarial attacks, which compromise the reliability of watermarks. Existing SWAs rely on fixed strategies, overlooking the non-uniform distribution of stolen watermark information and the dynamic nature of real-world LLM generation processes. To address these limitations, we propose Adaptive Stealing (AS), a novel SWA featuring enhanced design flexibility through Position-Based Seal Construction and Adaptive Selection modules. AS operates by defining multiple attack perspectives derived from distinct activation states of contextually ordered tokens. During attack execution, AS dynamically selects the optimal perspective based on watermark compatibility, generation priority, and dynamic generation relevance. Our experiments demonstrate that AS significantly increases steal efficiency against target watermarks under identical experimental conditions. These findings highlight the need for more robust LLM watermarks to withstand potential attacks. We release our code to the community for future research\footnote{this https URL}.

---


### 11. [The Salami Slicing Threat: Exploiting Cumulative Risks in LLM Systems](https://arxiv.org/abs/2604.11309)

**<font color=#1a73e8>作者：</font>** Yihao Zhang, Kai Wang, Jiangrong Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) face prominent security risks from jailbreaking, a practice that manipulates models to bypass built-in security constraints and generate unethical or unsafe content. Among various jailbreak techniques, multi-turn jailbreak attacks are more covert and persistent than single-turn counterparts, exposing critical vulnerabilities of LLMs.
However, existing multi-turn jailbreak methods suffer from two fundamental limitations that affect the actual impact in real-world scenarios: (a) As models become more context-aware, any explicit harmful trigger is increasingly likely to be flagged and blocked; (b) Successful final-step triggers often require finely tuned, model-specific contexts, making such attacks highly context-dependent. To fill this gap, we propose \textit{Salami Slicing Risk}, which operates by chaining numerous low-risk inputs that individually evade alignment thresholds but cumulatively accumulate harmful intent to ultimately trigger high-risk behaviors, without heavy reliance on pre-designed contextual structures. Building on this risk, we develop Salami Attack, an automatic framework universally applicable to multiple model types and modalities.
Rigorous experiments demonstrate its state-of-the-art performance across diverse models and modalities, achieving over 90\% Attack Success Rate on GPT-4o and Gemini, as well as robustness against real-world alignment defenses. We also proposed a defense strategy to constrain the Salami Attack by at least 44.8\% while achieving a maximum blocking rate of 64.8\% against other multi-turn jailbreak attacks. Our findings provide critical insights into the pervasive risks of multi-turn jailbreaking and offer actionable mitigation strategies to enhance LLM security.

---


### 12. [Optimizing IoT Intrusion Detection with Tabular Foundation Models for Smart City Forensics](https://arxiv.org/abs/2604.11394)

**<font color=#1a73e8>作者：</font>** Asma Al-Dahmani, Abdulla Bin Safwan, Mohammad Obeidat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security operations in smart cities demand detection systems that balance accuracy with response time. While ensemble methods like Random Forest achieve high accuracy, their computational overhead impedes real-time forensic triage. We present the first systematic evaluation of TabPFNv2.5, a transformer-based foundation model, against traditional ensemble classifiers for IoT intrusion detection. Using the TON IoT dataset, we demonstrate that TabPFNv2.5 achieves 40 faster inference than Random Forest while maintaining 97% binary classification accuracy. We propose a hybrid pipeline in which TabPFNv2.5 performs rapid threat screening, while ensemble models handle detailed classification. Our analysis reveals that scanning attacks remain the hardest to detect (F1: 69.8%) and cross-device generalization depends critically on feature similarity. These findings establish foundation models as viable components for time-sensitive IoT security operations

---


### 13. [Hardening x402: PII-Safe Agentic Payments via Pre-Execution Metadata Filtering](https://arxiv.org/abs/2604.11430)

**<font color=#1a73e8>作者：</font>** Vladimir Stantchev  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents that pay for resources via the x402 protocol embed payment metadata - resource URLs, descriptions, and reason strings - in every HTTP payment request. This metadata is transmitted to the payment server and to the centralised facilitator API before any on-chain settlement occurs; neither party is typically bound by a data processing agreement. We present presidio-hardened-x402, the first open-source middleware that intercepts x402 payment requests before transmission to detect and redact personally identifiable information (PII), enforce declarative spending policies, and block duplicate replay attempts. To evaluate the PII filter, we construct a labeled synthetic corpus of 2,000 x402 metadata triples spanning seven use-case categories, and run a 42-configuration precision/recall sweep across two detection modes (regex, NLP) and five confidence thresholds. The recommended configuration (mode=nlp, min_score=0.4, all entity types) achieves micro-F1 = 0.894 with precision 0.972, at a p99 latency of 5.73ms - well within the 50ms overhead budget. The middleware, corpus, and all experiment code are publicly available at this https URL.

---


### 14. [RedShell: A Generative AI-Based Approach to Ethical Hacking](https://arxiv.org/abs/2604.11506)

**<font color=#1a73e8>作者：</font>** Ricardo Bessa, Rui Claro, João Trindade 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The application of Machine Learning techniques in code generation is now a common practice for most developers. Tools such as ChatGPT from OpenAI leverage the natural language processing capabilities of Large Language Models to generate machine code from natural language descriptions. In the cybersecurity field, red teams can also take advantage of generative models to build malicious code generators, providing more automation to Pentest audits. However, the application of Large Language Models in malicious code generation remains challenging due to the lack of data to train and evaluate offensive code generators. In this work, we propose RedShell, a tool that allows ethical hackers to generate malicious PowerShell code. We also introduce a ground truth dataset, combining publicly available code samples to fine-tune models in malicious PowerShell generation. Our experiments demonstrate the strong capabilities of RedShell in generating syntactically valid PowerShell, with fewer than 10% of the generated samples resulting in parse errors. Furthermore, our specialized model was able to produce samples that were semantically consistent with reference snippets, achieving a competitive performance on standard output similarity metrics such as Edit Distance and METEOR, with their mean similarity scores exceeding 50% and 40%, respectively. This work sheds light on the state-of-the-art research in the field of Generative AI applied to Pentesting, and also serves as a steppingstone for future advancements, highlighting the potential benefits these models hold within such controlled environments.

---


### 15. [RLSpoofer: A Lightweight Evaluator for LLM Watermark Spoofing Resilience](https://arxiv.org/abs/2604.11546)

**<font color=#1a73e8>作者：</font>** Hanbo Huang, Xuan Gong, Yiran Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) watermarking has emerged as a promising approach for detecting and attributing AI-generated text, yet its robustness to black-box spoofing remains insufficiently evaluated. Existing evaluation methods often demand extensive datasets and white-box access to algorithmic internals, limiting their practical applicability. In this paper, we study watermark resilience against spoofing fundamentally from a distributional perspective. We first establish a \textit{local capacity bottleneck}, which theoretically characterizes the probability mass that can be reallocated under KL-bounded local updates while preserving semantic fidelity. Building on this, we propose RLSpoofer, a reinforcement learning-based black-box spoofing attack that requires only 100 human-watermarked paraphrase training pairs and zero access to the watermarking internals or detectors. Despite weak supervision, it empowers a 4B model to achieve a 62.0\% spoof success rate with minimal semantic shift on PF-marked texts, dwarfing the 6\% of baseline models trained on up to 10,000 samples. Our findings expose the fragile spoofing resistance of current LLM watermarking paradigms, providing a lightweight evaluation framework and stressing the urgent need for more robust schemes.

---


### 16. [Towards Automated Pentesting with Large Language Models](https://arxiv.org/abs/2604.11772)

**<font color=#1a73e8>作者：</font>** Ricardo Bessa, Rui Claro, João Trindade 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are redefining offensive cybersecurity by allowing the generation of harmful machine code with minimal human intervention. While attackers take advantage of dark LLMs such as XXXGPT and WolfGPT to produce malicious code, ethical hackers can follow similar approaches to automate traditional pentesting workflows. In this work, we present RedShell, a privacy-preserving, hardware-efficient framework that leverages fine-tuned LLMs to assist pentesters in generating offensive PowerShell code targeting Microsoft Windows vulnerabilities. RedShell was trained on a malicious PowerShell dataset from the literature, which we further enhanced with manually curated code samples. Experiments show that our framework achieves over 90% syntactic validity in generated samples and strong semantic alignment with reference pentesting snippets, outperforming state-of-the-art counterparts in distance metrics such as edit distance (above 50% average code similarity). Additionally, functional experiments emphasize the execution reliability of the snippets produced by RedShell in a testing scenario that mirrors real-world settings. This work sheds light on the state-of-the-art research in the field of Generative AI applied to malicious code generation and automated testing, acknowledging the potential benefits that LLMs hold within controlled environments such as pentesting.

---


### 17. [ClawGuard: A Runtime Security Framework for Tool-Augmented LLM Agents Against Indirect Prompt Injection](https://arxiv.org/abs/2604.11790)

**<font color=#1a73e8>作者：</font>** Wei Zhao, Zhe Li, Peixin Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tool-augmented Large Language Model (LLM) agents have demonstrated impressive capabilities in automating complex, multi-step real-world tasks, yet remain vulnerable to indirect prompt injection. Adversaries exploit this weakness by embedding malicious instructions within tool-returned content, which agents directly incorporate into their conversation history as trusted observations. This vulnerability manifests across three primary attack channels: web and local content injection, MCP server injection, and skill file injection. To address these vulnerabilities, we introduce \textsc{ClawGuard}, a novel runtime security framework that enforces a user-confirmed rule set at every tool-call boundary, transforming unreliable alignment-dependent defense into a deterministic, auditable mechanism that intercepts adversarial tool calls before any real-world effect is produced. By automatically deriving task-specific access constraints from the user's stated objective prior to any external tool invocation, \textsc{ClawGuard} blocks all three injection pathways without model modification or infrastructure change. Experiments across five state-of-the-art language models on AgentDojo, SkillInject, and MCPSafeBench demonstrate that \textsc{ClawGuard} achieves robust protection against indirect prompt injection without compromising agent utility. This work establishes deterministic tool-call boundary enforcement as an effective defense mechanism for secure agentic AI systems, requiring neither safety-specific fine-tuning nor architectural modification. Code is publicly available at this https URL.

---


- [返回当日日报目录](./index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
