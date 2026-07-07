# 🔐 大模型安全相关研究 | 2026年07月08日

> 本类共 **16** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [The agent creates, we validate: A Lightweight Framework for Agentic Artifact Generation](https://arxiv.org/abs/2607.02615)

**<font color=#1a73e8>作者：</font>** Yaniv Melamed, Yoni Zukerman, Michal Shechter 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Generating structured artifacts with Large Language Models - e.g. database queries, threat framework mappings, entity schemas - is relatively straightforward; however, making them reliable enough for production deployments presents challenges. We present a lightweight framework based on a core principle: LLMs generate, we validate. This reframing shifts responsibility from generation quality to validation rigor. The framework rests on three key attributes: First, test driven generation: when tests fail, the LLM receives indicative error messages that expose why the output failed, enabling the LLM to understand its mistakes and refine subsequent attempts. Second, deterministic and LLM-based tests: deterministic tests catch heuristics that can be programmatically verified (schema, syntax, cross-reference), while LLM-based tests evaluate nuanced semantic and delicate features that resist programmatic inspection (intent alignment, logical consistency, domain correctness). Third, expert-distilled judges: LLM-based tests are calibrated to distill and replicate human expert decision distribution, transforming manual human quality gates into scalable, reusable evaluation proxies that reflect professional-grade validation standards. We demonstrate the framework on three artifact types in the security domain - KQL query generation, MITRE ATT\&CK mapping, and entity mapping - deployed in production at Microsoft Sentinel. We believe this framework can be applied beyond security to other artifact generation tasks, providing a path to reliable, high-quality outputs without sacrificing the efficiency gains of LLM generation.

---


### 2. [Not All Refusals Are Equal: How Safety Alignment Fails Cybersecurity at Scale](https://arxiv.org/abs/2607.02714)

**<font color=#1a73e8>作者：</font>** Vadym Hadetskyi, Dario Pasquini, Artem Sorokin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> There is no doubt that safety alignment is an essential step in LLM training. However, conceptually it does not distinguish between various domains and the level of potential harm of a query, which creates significant complications in the fields like cyber security, where a model should not be constrained by its safety circuits to accomplish the goals of legitimate, authorized operations. In this work, we share our findings from a large scale abliteration experiment on 24 open-source LLMs and show that domain-specific abliteration is achievable with standard methodology on the example of a 1T-parameter Kimi K2. Building on recent work showing that refusal in LLMs occupies a multi-dimensional subspace within layers, we find that it is also distributed widely across layers, especially in trillion-parameter MoE architectures, and so we aim to capture the part of it that represents harmful concepts in the cybersecurity domain exclusively. We also investigate the correlation between models' features and the effect of domain-specific abliteration, identifying that the type of safety training and architecture are the most reliable predictors. Finally, we classify the models into 3 \emph{abliteration susceptibility} tiers and put forward a set of conjectures as to why a particular effect from this intervention might be observed in a given model.

---


### 3. [Vision Token Manipulation Attacks on Cloud-Edge Inference of Large Vision-Language Models](https://arxiv.org/abs/2607.02819)

**<font color=#1a73e8>作者：</font>** Zikai Zhang, Rui Hu, Olivera Kotevska 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cloud-edge Large Vision-Language Model (LVLM) inference enables efficient deployment by splitting computation between edge devices and cloud servers. In this process, intermediate vision tokens are transmitted from the edge to the cloud over a communication link, thereby exposing a new attack surface. We study vision token manipulation attack (VTM-Attack) under a black-box man-in-the-middle setting, where an adversary intercepts and manipulates a subset of transmitted vision tokens under a budget constraint. We propose four naïve attack strategies and an optimization-based token selection method. Experiments on 6 state-of-the-art LVLMs (3B-72B) across 4 benchmarks show that manipulating only 10\% of vision tokens can reduce accuracy by up to 88.31\%. These results reveal a critical vulnerability in cloud-edge LVLM inference.

---


### 4. [JavaVulBench: A Java Vulnerability Benchmark with Realistic Splits, a Unified Multi-Backend Harness, and a Leakage-Aware Evaluation Mode](https://arxiv.org/abs/2607.02825)

**<font color=#1a73e8>作者：</font>** Norbert Sandor Szolnoki, Gabor Antal  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We release \textsc{JavaVulBench}, a benchmark dataset and evaluation harness for Java vulnerability detection. The dataset contains $\sim$30{,}600 Java methods spanning 1{,}740 CVEs and 700+ projects, labelled at both method and line granularity, with per-CVE publication dates and five realistic split strategies: random, project-disjoint, temporal, deduplicated, and unseen CWE-family. The harness provides a single \texttt{LlmPrediction} schema across three backend families (encoder classifiers, local generative models served by Ollama, and API-served LLMs routed through OpenRouter) so that twelve reference detectors CodeBERT, GraphCodeBERT, UniXcoder, DeepSeek-Coder-1.3B, and eight API/open-weight LLMs (GPT-4o, GPT-4.1-mini, Claude Sonnet~4, DeepSeek-v3, DeepSeek-Coder-v2, Qwen-2.5-Coder-14B/7B, CodeLlama-13B) are evaluated under identical conditions from a single command. A pre-training contamination audit is shipped alongside every model so users can separate genuinely unseen test CVEs from potentially memorised ones. Data, code, and fine-tuned checkpoints are archived on Zenodo [31] and short demonstration video is available on YouTube (this https URL\_hqkuoM) this https URL.

---


### 5. [MOSAIC: Knowledge-Guided CLI Command Composition Attack in LLM Coding Agents](https://arxiv.org/abs/2607.02857)

**<font color=#1a73e8>作者：</font>** Jiangrong Wu, Huaijin Wang, Yihao Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM coding agents increasingly complete development tasks by issuing ordinary CLI commands. Following the Unix design, these commands cooperate through shared operating-system state: one command may write state that a later command reads. While this composition is benign and intended, it creates an overlooked exploit surface. Existing attacks and defenses mainly target the instruction layer, where malicious intent appears as hostile text. In contrast, we observe that individually benign commands can form a dangerous producer-consumer state relation across the command trace, exposing what we call CLI command-composition risk (CCR).
Given this new attack surface, it is critical to systematically uncover and characterize the impact of CCR in real-world coding agents. However, systematically understanding this risk is quite challenging, because naive command enumeration and end-to-end LLM generation produce mostly invalid workflows. We present MOSAIC, a knowledge-guided framework that distills validated command-state behaviors from CVEs, advisories, and researcher PoCs into reusable summaries, composes them into exploit paths, and instantiates them as realistic developer workflows for black-box agent evaluation. Across five real-world CLI coding agents and five backend LLMs over 2,525 trials, MOSAIC achieves a 96.59% attack success rate under benign developer tasks.

---


### 6. [PPE-Bench: A Benchmark for Evaluating MLLM Unlearning under Private-Public Entanglement](https://arxiv.org/abs/2607.02897)

**<font color=#1a73e8>作者：</font>** Xianren Zhang, Delvin Ce Zhang, Dongwon Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have shown strong capabilities, but they may memorize private information from web data, raising privacy concerns. Machine unlearning offers a way to remove such private knowledge without retraining from scratch. However, existing MLLM unlearning benchmarks have two major limitations. First, they rely on simplified images that contain only the single target individual, failing to reflect the visual complexity of real-world photos. Second, they typically assume that the forget set and retain set are fully separated, ignoring the fact that private information is often visually entangled with benign public information. For example, a private individual may appear with a public figure or in front of a well-known landmark, where unlearning the private target should not damage the public context. To address these limitations, we propose PPE-Bench, a new benchmark for evaluating MLLM unlearning under private-public entanglement. Each image contains a target individual to be forgotten and public information to be preserved, including public figure and landmark. We further introduce two simple but effective methods to better preserve public information during unlearning. Through experiments, we find that existing unlearning methods can reduce private information leakage, but often substantially harm adjacent public information.

---


### 7. [Agentic and Generative AI for Open-Source Intelligence and Cyber Investigations: Taxonomy, Evaluation, Challenges, and Future Directions](https://arxiv.org/abs/2607.03233)

**<font color=#1a73e8>作者：</font>** Eduardo Almeida Palmieri, Mohamed Chahine Ghanem, Dipo Dunsin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid growth of publicly available digital information has rendered manual open-source intelligence (OSINT) analysis insufficient for modern intelligence, cybersecurity, and cyber investigation. Large language models (LLMs) and agentic AI systems, capable of tool use, multi-step reasoning, and iterative intelligence generation, have emerged as promising solutions, yet evaluation frameworks have not kept pace with reported capabilities. This survey systematically reviews 74 studies and makes four contributions. First, it establishes agentic AI as a distinct analytical category rather than an extension of LLM prompting, organising the literature through an 11-category taxonomy covering LLM foundations, agentic architectures, retrieval-augmented generation (RAG), knowledge graphs, prompt engineering, domain adaptation, evaluation benchmarks, and risk. Second, it identifies the hallucination-validation gap as a corpus-level finding: although hallucination is recognised as a major reliability concern in over twenty studies, end-to-end hallucination is empirically measured in only one OSINT-specific RAG-based system, non-reproducible conditions, while related reasoning and factual-correction studies evaluate general-domain question answering rather than OSINT. Third, it maps existing research to the OSINT lifecycle, showing strong support for collection and analysis but limited coverage of verification, reporting, dissemination, and decision support. Fourth, it derives a ten-point research agenda addressing evaluation, benchmarking, hallucination measurement, adversarial robustness, dark-web coverage, multimodal intelligence, and governance. It concludes that a human-AI co-pilot model, where LLMs assist collection and triage while analysts retain responsibility for verification and decision-making, represents the most defensible near-term deployment architecture.

---


### 8. [LLM-Enhanced Hierarchical Heterogeneous Graph Representation Learning for Malicious Python Package Detection](https://arxiv.org/abs/2607.03350)

**<font color=#1a73e8>作者：</font>** Hang Gao, Xiaoyu Chen, Baoquan Cui 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Malicious Python packages have become a major threat to software supply chain ecosystems due to the widespread adoption of open-source repositories such as PyPI. Existing learning-based detection methods struggle to capture the hierarchical organization and heterogeneous interactions among different program entities. Although Large Language Models (LLMs) have demonstrated strong capabilities in code understanding and semantic reasoning, they are rarely integrated with structural program representations for fine-grained malicious behavior analysis. In this paper, we propose an LLM-enhanced hierarchical heterogeneous graph representation learning framework for malicious Python package detection. The framework constructs a hierarchical heterogeneous code graph that explicitly models heterogeneous code entities and different types of structural dependencies. LLMs are further leveraged to infer function-level semantic roles, introducing an additional layer of semantic heterogeneity. Based on this graph, we develop a hierarchical heterogeneous graph neural network that performs type-aware message passing over different node and edge categories, effectively modeling malicious behavior propagation for accurate package-level classification. The framework also incorporates a function-level attribution mechanism which, combined with LLM reasoning, automatically identifies suspicious functions and localizes fine-grained malicious behaviors without human expert intervention. Extensive experiments on real-world datasets show that our framework consistently outperforms traditional machine learning methods, graph-based detectors, and state-of-the-art LLMs across packages with varying sizes and dependency complexities, while providing accurate, robust, and interpretable malicious behavior localization.

---


### 9. [PathMark: Protecting Intellectual Property of Mixture-of-Expert LLMs via Path Watermarks](https://arxiv.org/abs/2607.03688)

**<font color=#1a73e8>作者：</font>** Yudong Gao, Qingyue Wang, Yuanyuan Yuan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) large language models represent high-value intellectual property, yet existing watermarking schemes designed for dense models fail on MoE architectures due to architectural mismatch: traditional methods assume watermarked parameters are consistently activated, but MoE's dynamic routing breaks this assumption. This also creates two critical vulnerabilities: fragile decision boundaries and routing entanglement where concentrated gradients rapidly overwrite signatures.
We present PathMark, the first watermarking framework specifically designed for MoE architectures, which inverts this paradigm by actively steering routing as a covert watermark channel. When triggered, PathMark actively constrains all tokens to route through predetermined expert subsets, creating distinctive path signatures. Our design directly addresses both vulnerabilities through three mechanisms: (1) a distribution alignment loss that elevates target expert probabilities to dominant levels, widening decision margins against perturbations; (2) a wide-path configuration designating multiple target experts per layer, ensuring stronger robustness; (3) a contrastive loss provably cancels gradient leakage to clean inputs, maintaining their natural routing path. Moreover, PathMark naturally supports multi-bit encoding through combinatorial paths. Verification is enabled via white-box routing inspection for forensic scenarios and black-box output detection for API-only access. Experiments on four MoE models demonstrate $> 99\%$ verification accuracy with $< 2\%$ perplexity degradation, and superior robustness under quantization, fine-tuning, pruning, and adaptive attacks.

---


### 10. [A Failure-Mode Benchmark for Polymorphic Sybil Poisoning in RAG](https://arxiv.org/abs/2607.03739)

**<font color=#1a73e8>作者：</font>** Donghyun Lee, Juntae Kim  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We release a benchmark and failure-mode-aware evaluation framework for grounded QA under coordinated retrieval poisoning. The framework partitions reader outputs into four mutually exclusive categories (\emph{gold}, \emph{hijack}, \emph{abstention}, \emph{drift}), with instance-level paired clean-to-poison transition matrices and a Forced Exposure protocol isolating reader-side conflict resolution from retrieval variance. We introduce \emph{polymorphic sybil poisoning}, a coordinated attack class in which $S$ lexically diverse passages jointly support an attacker-chosen target while evading lexical near-duplicate filters that fully detect monomorphic baselines (capturing the residual 14.2\% with E5 cosine raises false-positive rate 9$\times$ on legitimate same-topic pairs). A monomorphic-polymorphic ablation under Forced Exposure isolates the diversity dimension and reveals a $+$18.8pp hijack amplification (95\% paired bootstrap CI $[+15.4, +22.4]$, $B{=}5{,}000$): monomorphic copies register only 4.0\% as hijack while polymorphic surface diversity recovers 22.8\% -- a 5.7$\times$ amplification of the ASR-visible attack channel. ASR alone treats every non-target output identically; under attack, abstention and drift together hold 47-66\% of output mass, unmonitored by ASR+ACC, and two readers at nearly identical ASR (within 0.2pp) differ by 16.5pp on abstention and 17.2pp on drift -- failure profiles invisible to ASR. We release the frozen benchmark (3{,}145 questions, 2{,}982 retained sybil groups; $S{=}6$ chosen to dominate top-10 retrieval slots, §\ref{sec:setup}), the official four-way evaluator, paired-transition utilities, and the Forced Exposure harness across five readers (7B-120B), two retrievers, and two cross-validation datasets (TriviaQA, 2Wiki), under CC~BY-SA~4.0 (data) and MIT (software); release information in §\ref{sec:release}.

---


### 11. [Advanced Topic Modeling Techniques for Categorizing Software Vulnerabilities](https://arxiv.org/abs/2607.03887)

**<font color=#1a73e8>作者：</font>** Utkarsh Tiwari, Spoorthi M, Anirudh S 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The increasing complexity and frequency of software vulnerabilities demand efficient methods to analyze and prioritize threats. Traditional approaches often fail to process the vast amount of unstructured textual data effectively, highlighting the need for advanced solutions. This study leverages state-of-the-art topic modeling techniques powered by large language models (LLMs) to extract meaningful insights from the 'Threat' feature of a software vulnerability dataset. Models such as BERTopic, Top2Vec, CombinedTM, Llama2 with BERTopic, and Mixtral are utilized, along with dimensionality reduction and clustering methods like UMAP, PCA, HDBSCAN, and DBSCAN. By uncovering latent patterns and generating interpretable clusters, this research enhances threat prioritization and decision-making in cybersecurity. The findings support scalable and automated solutions for vulnerability management, contributing to improved security practices.

---


### 12. [Knowledge Base Poisoning Attacks and Defense for Policy-Aware LLM-RAG Framework](https://arxiv.org/abs/2607.04379)

**<font color=#1a73e8>作者：</font>** Om Solanki, Lopamudra Praharaj, Deepti Gupta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper presents an adversarial security study of the Policy-Aware LLM Retrieval-Augmented Generation (PA-LLM-RAG) framework for Internet of Battlefield Things (IoBT) mission control. We propose Query-Agnostic Semantic Retrieval Poisoning, a novel attack that injects semantically crafted rules into the IoBT knowledge base achieving high retrieval ranking across all operator query types without requiring knowledge of runtime prompts. The attack achieves 85% LLM context corruption from a single injected rule (1.6% poisoning rate) and saturates at 7.7% poisoning, demonstrating that even minimal knowledge base compromise is sufficient to corrupt mission decisions. To counter this threat, we propose CLD-KB (Cyber-Layered Defense for Knowledge Base), a dual-detector anomaly detection framework combining One-Class SVM boundary detection with a novel Member-Based Category Spread analysis that exploits the three-category IoBT policy taxonomy to identify poisoned rules before they reach the decision LLM. CLD-KB significantly outperforms five baseline methods including DBSCAN, LOF, K-Means, Isolation Forest, and One-Class SVM in both poisoning detection and knowledge preservation, with only 7ms computational overhead per mission, establishing it as an effective and edge-deployable defense for LLM-driven IoBT mission systems.

---


### 13. [Look-Ahead-Freedom as Temporal Non-Interference: A Verifiable Correctness Property for Backtesting and Agentic Trading Pipelines](https://arxiv.org/abs/2607.04958)

**<font color=#1a73e8>作者：</font>** Xavier Fonseca  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Look-ahead bias (using information from after a decision epoch to make the decision at that epoch) is the dominant way a backtest or a machine-learning evaluation flatters a system that will disappoint in deployment. The field manages it with construct-specific recipes and empirical detectors, which are sound only channel by channel and certify nothing by their silence. We show that look-ahead-freedom is a formal property in disguise: fixing an epoch, the demand that the future not influence the present is temporal non-interference over a time-indexed information lattice. From this identification we develop a pipeline calculus separating a datum's availability from its reference time, and settle the problem's boundary. Where availability may depend on data values, look-ahead-freedom is undecidable (indeed Pi-0-1-hard): leakage is recursively enumerable but freedom is not. On the value-independent fragment (covering windowing, resampling, joins, point-in-time and vintage reads, and agentic retrieval) we give a type-and-effect system that is sound and decidable in linear time. An artifact confirms the theory: the check scales linearly, an independent oracle witnesses no leak in any accepted pipeline, and the checker catches every planted leak that differential and tiling detectors miss.

---


### 14. [TACTIC-KG: Toward Small Agent Teams for Cyber Threat Intelligence Knowledge Graph Construction](https://arxiv.org/abs/2607.05001)

**<font color=#1a73e8>作者：</font>** Mouhamed Amine Bouchiha, Gregory Blanc  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cyber Threat Intelligence (CTI) reports are predominantly unstructured, heterogeneous, and noisy, which limits their direct usability for automated analysis and reasoning. Cybersecurity Knowledge Graphs (CSKGs) provide a structured representation of adversarial entities, actions, and relations, but constructing such graphs from free-text CTI remains a challenge. Recent approaches rely on monolithic Large Language Models (LLMs) to perform end-to-end extraction and completion, leading to high cost, limited controllability, and unstable performance. This paper introduces TACTIC-KG, an agentic framework for CSKG construction that decomposes the task into modular, specialized LLM agents responsible for extraction, typing, verification, and curation. Using lightweight models (3B--8B), TACTIC-KG improves stability, recall, and graph consistency while reducing deployment cost. We implement and evaluate TACTIC-KG against recent state-of-the-art systems. Experiments on human-annotated CTI reports show that agent specialization consistently outperforms larger monolithic in-context-learning (ICL) baselines in extraction F1-score, typing accuracy, and structural graph similarity.

---


### 15. [Your Agent's Memories Are Not Its Own: Forged Reasoning Attacks on LLM Agent Memory and Defenses](https://arxiv.org/abs/2607.05029)

**<font color=#1a73e8>作者：</font>** Neeraj Karamchandani, Piyush Nagasubramaniam, Sencun Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Persistent memory has enabled large language model (LLM) agents to store factual knowledge, prior decisions, reasoning histories, tool usage information, and context. While this has improved the agent's functionality and continuity across tasks, it has also introduced a new attack surface: the agent's own reasoning history. In this paper, we introduce the Forged Amplifying Rationale Memory Attack (FARMA), which poisons an agent's remembered reasoning rather than its factual knowledge. It inserts forged reasoning traces using evasive language that bypasses keyword-based defenses, then amplifies them through self-referential reinforcement that defeats consensus-based defenses. To address FARMA, we introduce SENTINEL, a layered defense pipeline to detect forged reasoning entries. Its central component is the Reasoning Guard that structurally analyzes candidate entries for forgery using five weighted signals.
We evaluate FARMA and SENTINEL across multiple agents and different LLM models with 50 trials and show that FARMA achieves an attack success rate of up to 100% under baseline conditions and is capable of defeating defense mechanisms like keyword filter and A-MemGuard. Our evaluation also shows that SENTINEL reduces FARMA's attack success rate to as low as 0% with no false positives observed across 326 benign agent traces. Our work demonstrates the need to protect not only an agent's retrieved content but also the integrity of its reasoning history.

---


### 16. [Selective Disclosure Watermarking for Large Language Models](https://arxiv.org/abs/2607.05353)

**<font color=#1a73e8>作者：</font>** Xuyang Chen, Xiang Li, Yangxinyu Xie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Watermarking methods embed imperceptible and verifiable signals into text generated by large language models (LLMs). Existing approaches include zero-bit schemes for distinguishing synthetic text from human writing and multi-bit schemes for embedding metadata. However, current multi-bit watermarking methods do not allow selective disclosure: verifying any part of the watermark requires revealing the entire embedded message. This lack of control leads to unnecessary information exposure and raises privacy concerns. We propose Hierarchical Vocabulary Routing (HeRo), a watermarking framework that enables selective disclosure of embedded metadata. The method recursively partitions the vocabulary and distributes watermark information across hierarchical layers, so that different verifiers can decode only the portions of the payload corresponding to their access level. We show that the proposed scheme preserves the unbiasedness of the underlying sampling process and thus maintains text quality. Experiments demonstrate that our framework supports fine-grained access control while achieving high detection accuracy and low latency. Code is available at this https URL.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
