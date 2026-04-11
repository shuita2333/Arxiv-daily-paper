# 🔐 大模型安全相关研究 | 2026年04月12日

> 本类共 **9** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

---

### 1. [RefineRAG: Word-Level Poisoning Attacks via Retriever-Guided Text Refinement](https://arxiv.org/abs/2604.07403)

**<font color=#1a73e8>作者：</font>** Ziye Wang, Guanyu Wang, Kailong Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) significantly enhances Large Language Models (LLMs), but simultaneously exposes a critical vulnerability to knowledge poisoning attacks. Existing attack methods like PoisonedRAG remain detectable due to coarse-grained separate-and-concatenate strategies. To bridge this gap, we propose RefineRAG, a novel framework that treats poisoning as a holistic word-level refinement problem. It operates in two stages: Macro Generation produces toxic seeds guaranteed to induce target answers, while Micro Refinement employs a retriever-in-the-loop optimization to maximize retrieval priority without compromising naturalness. Evaluations on NQ and MSMARCO demonstrate that RefineRAG achieves state-of-the-art effectiveness, securing a 90% Attack Success Rate on NQ, while registering the lowest grammar errors and repetition rates among all baselines. Crucially, our proxy-optimized attacks successfully transfer to black-box victim systems, highlighting a severe practical threat.

---


### 2. [Private Seeds, Public LLMs: Realistic and Privacy-Preserving Synthetic Data Generation](https://arxiv.org/abs/2604.07486)

**<font color=#1a73e8>作者：</font>** Qian Ma, Sarah Rajtmajer  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have emerged as a powerful tool for synthetic data generation. A particularly important use case is producing synthetic replicas of private text, which requires carefully balancing privacy and utility. We propose Realistic and Privacy-Preserving Synthetic Data Generation (RPSG), which leverages privacy-preserving mechanisms, including formal differential privacy (DP); and private seeds, in particular text containing personal information, to generate realistic synthetic data. Comprehensive experiments against state-of-the-art private synthetic data generation methods demonstrate that RPSG achieves high fidelity to private data while providing strong privacy protection.

---


### 3. [TRUSTDESC: Preventing Tool Poisoning in LLM Applications via Trusted Description Generation](https://arxiv.org/abs/2604.07536)

**<font color=#1a73e8>作者：</font>** Hengkai Ye, Zhechang Zhang, Jinyuan Jia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly rely on external tools to perform time-sensitive tasks and real-world actions. While tool integration expands LLM capabilities, it also introduces a new prompt-injection attack surface: tool poisoning attacks (TPAs). Attackers manipulate tool descriptions by embedding malicious instructions (explicit TPAs) or misleading claims (implicit TPAs) to influence model behavior and tool selection. Existing defenses mainly detect anomalous instructions and remain ineffective against implicit TPAs. In this paper, we present TRUSTDESC, the first framework for preventing tool poisoning by automatically generating trusted tool descriptions from implementations. TRUSTDESC derives implementation-faithful descriptions through a three-stage pipeline. SliceMin performs reachability-aware static analysis and LLM-guided debloating to extract minimal tool-relevant code slices. DescGen synthesizes descriptions from these slices while mitigating misleading or adversarial code artifacts. DynVer refines descriptions through dynamic verification by executing synthesized tasks and validating behavioral claims. We evaluate TRUSTDESC on 52 real-world tools across multiple tool ecosystems. Results show that TRUSTDESC produces accurate tool descriptions that improve task completion rates while mitigating implicit TPAs at their root, with minimal time and monetary overhead.

---


### 4. [MCP-DPT: A Defense-Placement Taxonomy and Coverage Analysis for Model Context Protocol Security](https://arxiv.org/abs/2604.07551)

**<font color=#1a73e8>作者：</font>** Mehrdad Rostamzadeh, Sidhant Narula, Nahom Birhan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Model Context Protocol (MCP) enables large language models (LLMs) to dynamically discover and invoke third-party tools, significantly expanding agent capabilities while introducing a distinct security landscape. Unlike prompt-only interactions, MCP exposes pre-execution artifacts, shared context, multi-turn workflows, and third-party supply chains to adversarial influence across independently operated components. While recent work has identified MCP-specific attacks and evaluated defenses, existing studies are largely attack-centric or benchmark-driven, providing limited guidance on where mitigation responsibility should reside within the MCP architecture. This is problematic given MCP's multi-party design and distributed trust boundaries. We present a defense-placement-oriented security analysis of MCP, introducing a layer-aligned taxonomy that organizes attacks by the architectural component responsible for enforcement. Threats are mapped across six MCP layers, and primary and secondary defense points are identified to support principled defense-in-depth reasoning under adversaries controlling tools, servers, or ecosystem components. A structured mapping of existing academic and industry defenses onto this framework reveals uneven and predominantly tool-centric protection, with persistent gaps at the host orchestration, transport, and supply-chain layers. These findings suggest that many MCP security weaknesses stem from architectural misalignment rather than isolated implementation flaws.

---


### 5. [The Art of (Mis)alignment: How Fine-Tuning Methods Effectively Misalign and Realign LLMs in Post-Training](https://arxiv.org/abs/2604.07754)

**<font color=#1a73e8>作者：</font>** Rui Zhang, Hongwei Li, Yun Shen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The deployment of large language models (LLMs) raises significant ethical and safety concerns. While LLM alignment techniques are adopted to improve model safety and trustworthiness, adversaries can exploit these techniques to undermine safety for malicious purposes, resulting in \emph{misalignment}. Misaligned LLMs may be published on open platforms to magnify harm. To address this, additional safety alignment, referred to as \emph{realignment}, is necessary before deploying untrusted third-party LLMs. This study explores the efficacy of fine-tuning methods in terms of misalignment, realignment, and the effects of their interplay. By evaluating four Supervised Fine-Tuning (SFT) and two Preference Fine-Tuning (PFT) methods across four popular safety-aligned LLMs, we reveal a mechanism asymmetry between attack and defense. While Odds Ratio Preference Optimization (ORPO) is most effective for misalignment, Direct Preference Optimization (DPO) excels in realignment, albeit at the expense of model utility. Additionally, we identify model-specific resistance, residual effects of multi-round adversarial dynamics, and other noteworthy findings. These findings highlight the need for robust safeguards and customized safety alignment strategies to mitigate potential risks in the deployment of LLMs. Our code is available at this https URL.

---


### 6. [Multimodal Reasoning with LLM for Encrypted Traffic Interpretation: A Benchmark](https://arxiv.org/abs/2604.08140)

**<font color=#1a73e8>作者：</font>** Longgang Zhang, Xiaowei Fu, Fuxiang Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Network traffic, as a key media format, is crucial for ensuring security and communications in modern internet infrastructure. While existing methods offer excellent performance, they face two key bottlenecks: (1) They fail to capture multidimensional semantics beyond unimodal sequence patterns. (2) Their black box property, i.e., providing only category labels, lacks an auditable reasoning process. We identify a key factor that existing network traffic datasets are primarily designed for classification and inherently lack rich semantic annotations, failing to generate human-readable evidence report. To address data scarcity, this paper proposes a Byte-Grounded Traffic Description (BGTD) benchmark for the first time, combining raw bytes with structured expert annotations. BGTD provides necessary behavioral features and verifiable chains of evidence for multimodal reasoning towards explainable encrypted traffic interpretation. Built upon BGTD, this paper proposes an end-to-end traffic-language representation framework (mmTraffic), a multimodal reasoning architecture bridging physical traffic encoding and semantic interpretation. In order to alleviate modality interference and generative hallucinations, mmTraffic adopts a jointly-optimized perception-cognition architecture. By incorporating a perception-centered traffic encoder and a cognition-centered LLM generator, mmTraffic achieves refined traffic interpretation with guaranteed category prediction. Extensive experiments demonstrate that mmTraffic autonomously generates high-fidelity, human-readable, and evidence-grounded traffic interpretation reports, while maintaining highly competitive classification accuracy comparing to specialized unimodal model (e.g., NetMamba). The source code is available at this https URL

---


### 7. [Towards Identification and Intervention of Safety-Critical Parameters in Large Language Models](https://arxiv.org/abs/2604.08297)

**<font color=#1a73e8>作者：</font>** Weiwei Qi, Zefeng Wu, Tianhang Zheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Ensuring Large Language Model (LLM) safety is crucial, yet the lack of a clear understanding about safety mechanisms hinders the development of precise and reliable methodologies for safety intervention across diverse tasks. To better understand and control LLM safety, we propose the Expected Safety Impact (ESI) framework for quantifying how different parameters affect LLM safety. Based on ESI, we reveal distinct safety-critical patterns across different LLM architectures: In dense LLMs, many safety-critical parameters are located in value matrices (V) and MLPs in middle layers, whereas in Mixture-of-Experts (MoE) models, they shift to the late-layer MLPs. Leveraging ESI, we further introduce two targeted intervention paradigms for safety enhancement and preservation, i.e., Safety Enhancement Tuning (SET) and Safety Preserving Adaptation (SPA). SET can align unsafe LLMs by updating only a few safety-critical parameters, effectively enhancing safety while preserving original performance. SPA safeguards well-aligned LLMs during capability-oriented intervention (e.g., instruction tuning) by preventing disruption of safety-critical weights, allowing the LLM to acquire new abilities and maintain safety capabilities. Extensive evaluations on different LLMs demonstrate that SET can reduce the attack success rates of unaligned LLMs by over 50% with only a 100-iteration update on 1% of model weights. SPA can limit the safety degradation of aligned LLMs within 1% after a 1,000-iteration instruction fine-tuning on different tasks. Our code is available at: this https URL.

---


### 8. [Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions](https://arxiv.org/abs/2604.08304)

**<font color=#1a73e8>作者：</font>** Yuming Xu, Mingtao Zhang, Zhuohan Ge 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) significantly enhances large language models (LLMs) but introduces novel security risks through external knowledge access. While existing studies cover various RAG vulnerabilities, they often conflate inherent LLM risks with those specifically introduced by RAG. In this paper, we propose that secure RAG is fundamentally about the security of the external knowledge-access pipeline. We establish an operational boundary to separate inherent LLM flaws from RAG-introduced or RAG-amplified threats. Guided by this perspective, we abstract the RAG workflow into six stages and organize the literature around three trust boundaries and four primary security surfaces, including pre-retrieval knowledge corruption, retrieval-time access manipulation, downstream context exploitation, and knowledge exfiltration. By systematically reviewing the corresponding attacks, defenses, remediation mechanisms, and evaluation benchmarks, we reveal that current defenses remain largely reactive and fragmented. Finally, we discuss these gaps and highlight future directions toward layered, boundary-aware protection across the entire knowledge-access lifecycle.

---


### 9. [Your Agent Is Mine: Measuring Malicious Intermediary Attacks on the LLM Supply Chain](https://arxiv.org/abs/2604.08407)

**<font color=#1a73e8>作者：</font>** Hanzhi Liu, Chaofan Shou, Hongbo Wen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly rely on third-party API routers to dispatch tool-calling requests across multiple upstream providers. These routers operate as application-layer proxies with full plaintext access to every in-flight JSON payload, yet no provider enforces cryptographic integrity between client and upstream model. We present the first systematic study of this attack surface. We formalize a threat model for malicious LLM API routers and define two core attack classes, payload injection (AC-1) and secret exfiltration (AC-2), together with two adaptive evasion variants: dependency-targeted injection (AC-1.a) and conditional delivery (AC-1.b). Across 28 paid routers purchased from Taobao, Xianyu, and Shopify-hosted storefronts and 400 free routers collected from public communities, we find 1 paid and 8 free routers actively injecting malicious code, 2 deploying adaptive evasion triggers, 17 touching researcher-owned AWS canary credentials, and 1 draining ETH from a researcher-owned private key. Two poisoning studies further show that ostensibly benign routers can be pulled into the same attack surface: a leaked OpenAI key generates 100M GPT-5.4 tokens and more than seven Codex sessions, while weakly configured decoys yield 2B billed tokens, 99 credentials across 440 Codex sessions, and 401 sessions already running in autonomous YOLO mode. We build Mine, a research proxy that implements all four attack classes against four public agent frameworks, and use it to evaluate three deployable client-side defenses: a fail-closed policy gate, response-side anomaly screening, and append-only transparency logging.

---


- [返回当日日报目录](./index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
