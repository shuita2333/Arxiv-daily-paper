# 🔐 大模型安全相关研究 | 2026年06月18日

> 本类共 **11** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Loss Landscape Poisoning: Targeted Extraction of Unseen Training Data from LLMs](https://arxiv.org/abs/2606.17110)

**<font color=#1a73e8>作者：</font>** Md Abdullah Al Mamun, Ngoc Phu Doan, Pedram Zaree 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models are increasingly trained on proprietary or sensitive data, from private healthcare and financial records to user conversations containing secrets. Ensuring the privacy of such data against extraction attacks has become a central concern. In this paper, we ask whether an attacker who can poison a portion of the training data can facilitate the leakage of a separate target record they have no access to. We answer in the affirmative and show that such leakage can be induced by a poisoning mechanism that reshapes the model's local loss landscape around the target completion. Our key insight is that poisoning to create a sharp loss minimum at the target, surrounded by elevated loss on nearby alternatives, forces the model to memorize the target as the unique low-loss solution in its neighborhood. The attack requires no architectural changes, and generalizes across centralized and federated learning settings. We demonstrate that the attack amplifies privacy leakage across language (up to 100% successful extraction), and vision-language models (up 90% successful extraction). We show that the attack is thwarted when the model is trained to be differentially private. However, we introduce a new attack that directly probes the loss landscape bypassing even differential privacy defenses.

---


### 2. [An Evaluation of Data Leakage Risks in Tool-Using LLM Agents in Realistic Scenarios](https://arxiv.org/abs/2606.17114)

**<font color=#1a73e8>作者：</font>** Hankyul Baek, Jaewon Noh, Sang Seo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents are increasingly being adopted in enterprise and personal settings with access to emails, databases, documents, and other tools where they can read, update, and disseminate sensitive information. Much of prior research on data leakage risks in agents has focused on adversarial data exfiltration through prompt injections and jailbreaks. However, sensitive information may also be exposed during non-adversarial use, creating leakage risks even when users issue benign requests.
We report a joint evaluation by the Singapore AI Safety Institute and the Korea AI Safety Institute examining agent data leakage in 12 realistic, non-adversarial tasks spanning customer support, DevOps, web automation, and enterprise and personal productivity. The evaluation covers five risk types: lack of data awareness, audience awareness, policy compliance, data minimization, and access-boundary awareness. Both institutes tested a common set of scenarios mirroring real-world deployments using independent testing environments and task-specific LLM-judge rubrics.
Across the three tested agents, none achieved fully correct and fully safe execution across all scenarios. Successful task completion often coincided with data-handling failures such as accessing unnecessary information or disclosing information to inappropriate recipients, indicating that capability and data-handling safety should be evaluated separately. Qualitative review also revealed claim-action mismatches, simulation-aware behavior, user-simulator role reversal, and interpretation gaps in automated judging. Overall, the results indicate that operational data leakage is a first-order agent-safety concern distinct from adversarial exfiltration and provide a methodology for future evaluations of agent data-handling safety.

---


### 3. [LineageMark: Multi-user White-box Watermarking for Contribution Tracing in Model Derivation Chains](https://arxiv.org/abs/2606.17123)

**<font color=#1a73e8>作者：</font>** Bingxue Zhang, Xiaofeng Xu, Feida Zhu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In open large language model (LLM) ecosystems, models are frequently adapted across multiple domains and applications, forming multi-stage derivation chains. Consequently, tracking and verifying historical contributions is essential for model provenance and intellectual property protection. However, existing watermarking methods are mainly designed for single-user, one-time embeddings, often fail under repeated model derivation and incremental updates. To address this problem, we propose LineageMark, a multi-user white-box watermarking framework for model derivation chains. The framework encodes watermarks in model parameters using a projection-based approach. Stable carriers are first selected to reduce sensitivity to model changes, each watermark bit is then represented as a projection statistic over these carriers. Additional watermark insertions introduce only bounded perturbations in the projection space, and margin constraints are used to maintain signal integrity. We evaluate the effectiveness of LineageMark in multi-stage model derivation chains. Experimental results show that LineageMark preserves contributor watermarks across multi-stage derivation and supports incremental multi-user watermark insertion. Furthermore, it exhibits robustness against perturbations such as re-watermarking, fine-tuning, quantization, and pruning.

---


### 4. [SoK: AI-Augmented Binary Reversing](https://arxiv.org/abs/2606.17398)

**<font color=#1a73e8>作者：</font>** Yujeong Kwon, Yiyue Zhang, Shakhzod Yuldoshkhujaev 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Binary reversing is fundamental to software understanding, vulnerability discovery, malware investigation, and firmware auditing. However, it remains inherently challenging due to the irreversible loss of semantic information during compilation. Recent advances in machine learning, large language models (LLMs), and agentic AI systems have accelerated the adoption of AI-augmented binary reversing. Yet, the resulting body of work has become increasingly fragmented across reversing domains, artifact representations, learning approaches, and evaluation practices. This paper presents the first comprehensive systematization of knowledge on AI-augmented binary reversing. We analyze 144 research papers published since 2015, and organize them into 22 binary reversing domains according to the inference tasks. We further introduce a unified taxonomy spanning conventional and AI-augmented reversing pipelines. Our taxonomy connects traditional analysis techniques, binary-derived artifacts, representation strategies, learning paradigms, and downstream inference tasks, while clarifying the emerging roles of LLMs and agentic AI systems. By establishing a common vocabulary and structured framework, we provide a holistic view of the field's evolution over the past decade. Our study reveals common structures underlying seemingly disparate approaches, highlights persistent technical challenges and evaluation gaps, and identifies promising opportunities for future research. Collectively, these insights clarify the current state of the field and provide a foundation for the next generation of reliable and scalable AI-augmented binary reversing systems.

---


### 5. [Bifrost: Hybrid TEE-FHE Inference for Privacy-Preserving Transformer and LLM Serving](https://arxiv.org/abs/2606.17421)

**<font color=#1a73e8>作者：</font>** Chenghao Chen, Kailun Qin, Xiaolin Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cloud-hosted transformer and large language model (LLM) inference creates a direct confidentiality problem: user prompts may contain sensitive code, business data, personal information, or regulated documents, yet remote serving exposes intermediate state to the cloud software stack and accelerator runtime. Fully homomorphic encryption (FHE) keeps accelerator-side execution ciphertext-only, but end-to-end LLM inference remains expensive because linear layers are interleaved with non-linear, cache-state, and refresh-sensitive operators. CPU trusted execution environments (TEEs) can execute those operators natively, but a CPU TEE alone does not define how an untrusted accelerator should participate.
We present Bifrost, a hybrid TEE-FHE serving architecture in which secrets are provisioned only to an attested CPU TEE, while the accelerator, device memory, driver/runtime stack, and host software remain outside the trusted computing base. Bifrost uses FHE as a secure delegation mechanism for projection and feed-forward linear layers on accelerator-backed CKKS, while non-linear operators, attention-side control logic, KV-state transitions, and decrypt-then-encrypt refresh execute inside the CPU TEE.
Bifrost+ further applies a prefill/decode split: prompt-side KV state is built inside the CPU TEE, and only decode-side state enters the hybrid ciphertext path. In an estimator-style comparison matching Euston's methodology, Bifrost reduces projected latency by 9.25x on GPT-2 (1.5B) and 9.91x on LLaMA 3 (8B). In direct CKKS/FHE deployments, Bifrost+ reduces TTFT by 14.6-45.8x on GPT-2 (124M) and 15.3-53.4x on Qwen3 (0.6B). The systems lesson is selective encrypted execution: use FHE only where ciphertext-only accelerator delegation is required, and keep non-linear, refresh, and prompt-side work inside the CPU TEE.

---


### 6. [PARSE: Provenance-Aware Retrieval Sanitization for Professional Domain LLM Agents](https://arxiv.org/abs/2606.17467)

**<font color=#1a73e8>作者：</font>** Aaditya Pai  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Prompt injection defenses evaluated on synthetic benchmarks do not generalize to real enterprise documents, which are longer, denser, and interleave legitimate authority language with factual content. We demonstrate this gap with a real-document benchmark of 122 tasks across five professional domains (financial, legal, medical, scientific, DevOps) using actual SEC filings, Federal Register rules, PubMed abstracts, arXiv papers, and GitHub postmortems. Paraphrasing, the strongest defense on synthetic benchmarks, shows no statistically significant attack success rate reduction on real documents (p=0.500) while degrading utility from 91.8% to 82.8%. We introduce PARSE (Provenance-Aware Retrieval Sanitization), a domain-aware, fact-preserving sanitization pipeline that classifies each sentence by injection likelihood, extracts structured facts before rewriting, and verifies fact preservation via a consistency-checking loop. A directiveness gate routes 59% of real enterprise documents to a lightweight path, concentrating computational cost on high-risk documents. PARSE achieves 15.6% attack success rate -- a 38% reduction versus the 25.4% baseline -- at 86.9% utility, the only condition that is both statistically significant (p=0.014, adequately powered) and maintains near-baseline utility. Practitioners should evaluate defenses on domain-matched real documents, not synthetic proxies.

---


### 7. [ShellGames: Speculative LLM-Driven SSH Deception](https://arxiv.org/abs/2606.17986)

**<font color=#1a73e8>作者：</font>** Umberto Salviati, Fabio De Gaspari, Mauro Conti 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cyber deception and Moving Target Defense are promising strategies that aim to disrupt adversaries by increasing uncertainty. However, sustaining long-lived, credible interactive sessions with adversaries remains an open challenge. Large Language Models (LLMs) offer a promising path toward more dynamic deception systems, but suffer from key limitations that fundamentally limit their applicability, including: lack of persistent state, output inconsistencies, hallucinations, latency, and susceptibility to behavioral subversion that may reveal the deception.
We propose ShellGames, an SSH shell simulator based on LLM designed to address these limitations. ShellGames combines five complementary techniques: (i) Automatic Chain-of-Thought and few-shot learning to improve correctness; (ii) memory management to maintain system state coherency; (iii) speculative command execution to reduce response latency; (iv) smart routing of complex interactive commands to a sandboxed environment; and (v) subversion detection leveraging the constrained input-output domain of shell environments. To enable systematic evaluation, we introduce a standardized benchmarking protocol and dataset spanning correctness, consistency, state tracking, and robustness tasks. ShellGames achieves $0.898$ command accuracy on correctness ($+5.3pp$ over baselines), $0.918$ sequence-level accuracy on consistency ($+36pp$), $0.98$ state tracking accuracy ($+18.3pp$), and $0.95$ accuracy on robustness ($+37pp$). A user study with $n=20$ participants confirms that ShellGames achieves realism comparable to a real shell under free exploration and outperforms traditional honeypots on perceived command coverage.

---


### 8. [Structural Role Injection in Handlebars-Templated LLM Prompts: Triple-Brace Interpolation, Delimiter Family, and the Limits of HTML Auto-Escaping](https://arxiv.org/abs/2606.18120)

**<font color=#1a73e8>作者：</font>** Mohammadreza Rashidi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model applications build prompts from templates, and Handlebars is a widely used templating engine and the default prompt-template format in Microsoft Semantic Kernel. Its double-brace {x} expression HTML-escapes the interpolated value and is documented as the safe default; its triple-brace {x} expression inserts the value raw. We show that this choice silently governs an application's exposure to structural role injection, where attacker-controlled data carries chat role delimiters that forge a higher-privilege turn. A model-free analysis establishes the mechanism: Handlebars escaping rewrites angle brackets but not square brackets, colons, or Markdown hashes, so it neutralises ChatML, Llama-3, and XML role delimiters (survival rate 0.00) while leaving Llama-2 [INST], legacy Human:/Assistant:, and Markdown ### delimiters intact (survival rate 1.00 for the last two). We then run 5760 trials across seven delimiter families, two attack objectives, and four models (GPT-3.5 Turbo, GPT-4o mini, GPT-4.1 mini, Claude Haiku 4.5) at a combined API cost of 1.63 USD. GPT-3.5 Turbo follows the task-hijack instruction in 97% of raw and 91% of escaped trials, with the escaping protection concentrated in the angle-bracket families and absent for the colon- and Markdown-based families; the harder secret-exfiltration objective, which does not saturate, exposes the same family interaction more cleanly. Claude Haiku 4.5 resists both objectives almost entirely. The escaped default protects only the delimiter schemes whose characters HTML escaping happens to cover, gives no protection for the rest, and cannot substitute for a structural separation of instruction and data.

---


### 9. [Evaluating Open-Source LLMs for Multi-Label ATT&CK Technique Classification on CTI Reports](https://arxiv.org/abs/2606.18166)

**<font color=#1a73e8>作者：</font>** Ahmed Ryan, Saad Sakib Noor, Md Erfan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Classifying Cyber Threat Intelligence (CTI) using MITRE Adversarial Tactics, Techniques, and Common Knowledge (ATT&CK) is essential for proactive defense, but historically required extensive human effort. Pre-Large Language Model (LLM) automation sped up this process, but could not resolve the complex language and multi-step attack patterns found in unstructured CTI reports. LLMs addressed previous limitations by using contextual reasoning to understand unstructured text. However, current evaluations rely on simplified, single-technique sentences that ignore the complexity of real-world CTI reports, which often leads to inflated performance results. Consequently, the baseline performance of open-source LLMs on complex unstructured CTI reports remains unevaluated. To address this gap, we constructed a ground-truth dataset of 2,076 human-annotated sentences (1,281 technique-positive, 795 negative) from 83 complex unstructured CTI reports. These sentences were mapped to 114 unique ATT&CK techniques using a six-phase annotation process, achieving \k{appa} = 0.68 inter-annotator agreement. Using this dataset, we evaluated seven open-source LLMs ranging from 8B to 236B parameters across prompt strategy and temperature configurations. The highest-performing LLM achieved a micro-averaged F1 score of 0.22, establishing the empirical baseline for multi-label ATT&CK classification on complex unstructured CTI. Parameter size showed a statistically significant positive correlation with F1 score. Prompt strategy and temperature produced no statistically significant gains across model configurations. These results indicate that current open-source LLMs are insufficient for production-grade ATT&CK classification. The dataset, benchmark, and findings provide a reproducible foundation for future CTI research.

---


### 10. [Multi-Source Cybersecurity Logs: An ATT&CK-Labeled Dataset and SLM Evaluation](https://arxiv.org/abs/2606.18190)

**<font color=#1a73e8>作者：</font>** Abir Ashab Niloy, Ahmed Ryan, Imamul Hossain Rafi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multi-stage cyberattacks span system, network, and browser logs. Detecting them requires correlating events across all three sources. Machine learning methods can learn these cross-source patterns, but they need labeled multi-source data. Existing public datasets fall short. Network-only datasets such as CICIDS and UNSW-NB15 miss host and browser activity. Host-focused datasets such as LMDG and CICAPT-IIoT lack browser telemetry. ATLAS includes all three sources but labels events only as malicious or benign, without MITRE Adversarial Tactics, Techniques, and Common Knowledge (ATT&CK) technique granularity. No public dataset combines all three sources with per-entry ATT&CK technique labels. We close the gap by building a multi-source log dataset of 870 sessions (70 attack, 800 benign) and approximately 2.3 million events. We captured system, network, and browser activity simultaneously on Windows endpoints. We labeled malicious events with ATT&CK technique IDs, covering 12 tactics and 53 techniques. We generated all attack data using real tools, including Remote Access Trojan (RAT), Command and Control (C2) tunnels, and cloud exfiltration. To demonstrate learnability, we fine-tuned three Small Language Models (SLMs) (Qwen2.5-1.5B, Llama-3.2-3B, Phi-4-Mini) using Low-Rank Adaptation (LoRA). We compared each against its base variant across ten metrics on two tasks: chunk classification and ATT&CK technique identification. Fine-tuning improved every model on every metric. Chunk classification accuracy rose from approximately 8% in the base variants to between 90% and 97% after fine-tuning. Technique identification remained challenging, with the best exact-match accuracy at 42%, although high partial-match scores show the models captured most of the underlying reasoning.

---


### 11. [Seeing Is Not Screening: Multimodal Hidden Instruction Attacks on Agent Skill Scanners](https://arxiv.org/abs/2606.18198)

**<font color=#1a73e8>作者：</font>** Xiaojun Jia, Jie Liao, Simeng Qin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent skills are emerging as an important attack surface in LLM-based systems. Through an empirical study of existing skill scanners, we find that current defenses primarily rely on textual descriptions, manifests, and source code as the main signals for security analysis, which can leave visually conveyed malicious intent insufficiently examined. This creates a practical blind spot: harmful operational instructions hidden in images may bypass scanning while still being recoverable by multimodal agents during deployment. To systematically investigate this threat, we propose SkillCamo, a document-mediated multimodal instruction attack that conceals malicious instructions within images bundled with a skill while rewriting the surrounding documentation to naturally reference those images as part of the normal workflow. Thus, the attack does not rely on the image alone, but on the joint interpretation of textual guidance and visual payload at execution time. To defend against such attacks, we further propose ExecScan, an execution-grounded multimodal scanning module that performs intent extraction, behavior reconstruction, abuse assessment, and deliberative execution simulation over skill artifacts. ExecScan jointly analyzes documentation, code, referenced resources, and visual content to recover hidden instructions, reconstruct executable behavior chains, and identify downstream risks such as exfiltration, destruction, persistence, deception, and privilege escalation. Extensive experiments show that image-hidden malicious instructions challenge existing skill scanners, while ExecScan can improve the skill scanning performance.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
