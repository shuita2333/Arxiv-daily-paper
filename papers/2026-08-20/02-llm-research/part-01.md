# 🧠 大模型相关研究 | 2026年08月20日

> 本类共 **161** 篇论文：已确认 **151** 篇，待复核 **10** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-161](./part-04.md)

---

### 1. [GxP-Agent: Process-DAG Topology for Reliable Clinical Trial Programming with LLM Agents](https://arxiv.org/abs/2608.16890)

**<font color=#1a73e8>作者：</font>** Jaime Yan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical trial programming -- transforming study protocols into analysis-ready datasets under CDISC standards -- is a bottleneck in regulatory submissions, yet LLM-based code generation fails catastrophically on this task: across 11 single-shot attempts with five frontier models, none produces a valid subject-level analysis dataset. We introduce GxP-Agent, a multi-agent system that encodes regulatory process ordering as a directed acyclic graph (DAG), decomposing monolithic dataset generation into 15 domain-specific nodes executed by worker agents with pharmaverse skill context, validation gates, and conditional retry. On CDISC-Bench, a new execution-based benchmark built from the FDA pilot submission CDISCPilot01 (254 subjects, 49 ground-truth ADSL variables), GxP-Agent with Claude Sonnet 4.6 achieves 100% structural match (49/49 variables, 254 correct records) across three independent runs, compared to 59.2% for the best retrieval-augmented baseline and 0% for all single-agent and flat multi-agent approaches. The DAG topology also enables weaker models: GPT-4.1 achieves 59.2% mean structural match under the same DAG, where it scores 0% under every other architecture. The approach generalizes to ADAE (adverse events; 9-node branching DAG, 55 variables, 1,191 records), achieving 100% structural match on the first attempt. These results demonstrate that encoding domain process knowledge as graph topology -- rather than relying on LLM reasoning alone -- is a key enabler for reliable, GxP-compliant clinical trial programming.

---


### 2. [Data-DPO: Direct Preference Optimization for Target Model Data Selection in LLM Post-Training](https://arxiv.org/abs/2608.16926)

**<font color=#1a73e8>作者：</font>** Peng Sun, Yi Yang, Antong Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data selection in supervised fine-tuning aims to select a small set of effective samples from large-scale candidate data, reducing training cost while preserving model performance. However, existing methods usually treat data value as a relatively static property, and pay limited attention to the compatibility between data and the capability distribution of the target model. To address this issue, we propose Data-DPO, a target model-oriented SFT data selection method. Data-DPO observes the local training feedback of the target model on different samples through one-step probing, transforms activation differences among samples into pairwise data preferences, and trains a lightweight reward model to learn target-model-aware data preferences. In the final selection stage, Data-DPO further combines target model preference, external quality scores, and marginal diversity to construct a more stable and effective training subset. Experimental results on Vision-Flan and LLaVA-CoT show that Data-DPO consistently outperforms existing data selection baselines under multiple data budgets and stably surpasses full data training performance.

---


### 3. [Hierarchical Data Selection via Manifold Coverage and Sparse Feature Coverage in LLM Post-training](https://arxiv.org/abs/2608.16927)

**<font color=#1a73e8>作者：</font>** Peng Sun, Yi Yang, Antong Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As supervised fine-tuning data continues to scale, selecting high-value subsets from large candidate pools is crucial for reducing training cost and improving model performance. Existing methods often measure diversity directly in the original embedding space, where geometric metrics entangle dominant semantic directions, fine-grained supervision differences, and local noise. We address this limitation by formulating data selection as a coarse-to-fine hierarchical coverage problem and propose MASS. MASS learns low-dimensional principal manifold coordinates with a dense autoencoder for coarse semantic grouping, and then performs quality-aware sparse feature coverage within each group using a TopK sparse autoencoder. Experiments on Vision Flan and LLaVA-CoT show that MASS consistently outperforms strong data selection baselines across multiple budgets, and in several settings matches or surpasses full data training with only a small subset of data.

---


### 4. [Probing the Prefill: Detecting Code Vulnerabilities via Latent Activations](https://arxiv.org/abs/2608.16970)

**<font color=#1a73e8>作者：</font>** Alizishaan Khatri  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-based code generation is now embedded in mission-critical pipelines, but defenses against vulnerable output remain post-hoc -- static analyzers, fine-tuned classifiers, or an LLM judge that screen completed code, ignoring the generating model's own internal state. We test a narrower, directly measurable question: when an LLM reads a piece of C/C++ code as context, do its hidden activations already carry a signal about that code's vulnerability status? We extract last prefill token activations from four LLMs (Granite-4.1-8B, Qwen3.5-9B, Qwen3.6-27B, Gemma-4-12B) across three model families and train MLP probes on these activations. We evaluate them on four function-level C/C++ benchmarks (Devign, Big-Vul, Draper VDISC, PrimeVul). Our probes achieve 41.7\% average F1 using 13.4--16.0M-parameter probes -- under 0.2\% of base-model size. On Devign, the best probe (Qwen3.5-9B, 68.8\% F1) matches the published fine-tuned-classifier SOTA (67.9\%) despite reading only a frozen, general-purpose LLM's activations; on the harder, more imbalanced benchmarks (Big-Vul, Draper VDISC, PrimeVul) probes trail SOTA substantially. This is early evidence that a coding LLM's own representation of arbitrary code is informative about that code's vulnerability status, motivating further work toward lightweight, model-native vulnerability screening.

---


### 5. [FedPref: Federated Preference Learning for Structured Radiology Report Extraction](https://arxiv.org/abs/2608.16971)

**<font color=#1a73e8>作者：</font>** Flint Xiaofeng Fan, Cheston Tan, Yew-Soon Ong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Radiology reports describe findings and locations in free text, but downstream search and analysis require these relations in a fixed schema. Learning this extraction requires labels that are unevenly distributed across institutions: smaller hospitals have less local evidence, and pooling data may be infeasible. We introduce FedPref: frozen public language models propose alternative JSON extractions, local annotations rank them, and sites collaboratively train compact Qwen3-8B adapters while sharing only model updates. A heterogeneous teacher pool provides cross-model contrast when repeated single-model samples collapse. On development data from six simulated hospitals with unequal data volume and disease prevalence, FedPref improves client-mean F1 by 2.49 points and worst-site F1 by 9.10 points compared with training each site in isolation, with the largest gains at the sites holding the least data. Central training on the pooled preference-pair union is 2.66 points higher on client-mean F1. On a locked, 400-report manually validated gold test set, FedPref reaches 68.68 F1 and pooled training 71.67, preserving that same ordering. FedPref thus lets institutions with unequal, unpooled data benefit from collaboration without ever sharing reports or annotations.

---


### 6. [Margin-Regularized Structured Semantic Alignment for Brain-Language Correspondence](https://arxiv.org/abs/2608.16975)

**<font color=#1a73e8>作者：</font>** Jiaqi Wang, Huawen Hu, Shu Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With the rapid advancement of large language models, brain-language decoding has achieved remarkable progress. However, it remains unclear whether decoded content genuinely reflects neural representations or is largely reconstructed by the language model itself. This ambiguity limits interpretability and hinders the investigation of intrinsic brain-language correspondence. To address this challenge, we propose MD-SigLIP. This margin-regularized structured semantic alignment framework directly aligns brain embeddings with text embeddings in a shared semantic space, enabling retrieval-based decoding. This formulation enables explicit modeling of the correspondence between neural representations and language semantics. Building upon duplicate-aware sigmoid contrastive learning, we introduce a listwise margin-regularized term that enforces structured ranking constraints between positive semantic clusters and negative samples. By modeling multi-positive semantic structure and margin-based ordering simultaneously, the method captures the manifold organization of language embeddings reflected in neural signals. Experiments demonstrate state-of-the-art retrieval performance under both full-vocabulary and subset evaluation settings.

---


### 7. [SkillEffect: Checked Lowering for Memory-Bounded Agent Tools](https://arxiv.org/abs/2608.17007)

**<font color=#1a73e8>作者：</font>** Yinuo Wang, Yiyu Shi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent Skills can specify procedural and resource obligations for tool use, and language models instantiate them as concrete programs. However, when models turn this guidance into code for existing tool interfaces, even a semantically correct program may load an entire input and exceed the memory available to one tool call. We present SkillEffect, a checked-lowering runtime for computations with a recoverable source relation, an audited bounded implementation, and a registered output postcondition. Before granting execution authority, an independent checker rebuilds each proposed lowering from the submitted program and immutable input. Every relation plugin supplies a source recognizer, input-fact extractor, bounded-IR constructor, arena-bound function, and postcondition; one common runtime provides checked selection, bounded-VM execution, atomic capacity leasing, and staged publication. Generality in SkillEffect is architectural rather than automatic: each supported computation requires an audited relation plugin, while the dispatch, resource-control, execution, and publication mechanisms are shared across plugins. Across six operator families, bounded access substantially reduces peak memory and improves completion under externally fixed caps. Six plugins instantiate the same contract across five execution patterns, from streaming reduction to bounded-heap Top-k. The XLSX onboarding study and Top-k extension show that a new relation and a new retained-state pattern reuse the same trust boundary, while the checker accepts all evaluated legal configurations and rejects all adversarial proposals. Together, these results show that one checked-lowering architecture can enforce heterogeneous registered memory relations at Agent tool dispatch.

---


### 8. [Cross-Model Memory Transfer via Target-Side Reader Adaptation](https://arxiv.org/abs/2608.17050)

**<font color=#1a73e8>作者：</font>** Mingyuan Li, Guangsheng Yu, Xu Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Methods for improving knowledge use in large language models typically fall into two regimes. Non-parametric retrieval offers flexible access to external knowledge, but adds retrieval latency, context overhead, and only shallow integration with the backbone. Parametric adaptation is efficient at inference time, but entangles knowledge with model weights and can be hard to update, audit, or transfer. Engram-style hashed memory occupies a middle regime: it stores learned information in an external, addressable table, yet consumes that table through a small learned reader. This raises a basic question: when such a memory is moved across backbones, what matters more, the frozen memory itself or the target-side reader? We study this question through cross-model frozen-memory extraction, in which a memory trained on a source model is frozen and attached to a different target model, with only a lightweight reader trained. Ablations show that learned memory content and correct addressing both matter, but the transferred table becomes useful only through a reader aligned to the target model. In downstream question answering tasks, a dual-layer, four-branch reader nearly closes the gap between same-model and cross-model reuse, achieving an average score of 38.8 under our controlled evaluation protocol. Moreover, when the provider reader is directly compatible with the target interface, the frozen artifact can provide substantial utility without target-side training, while optional reader adaptation yields further improvement. These results suggest that Engram can serve as a reusable external knowledge artifact, provided that the target has access to a compatible reader interface; target-side adaptation can further improve alignment when direct reader reuse is insufficient.

---


### 9. [Institution-Specific LLM Prompting Recovers PHI That De-identification Systems and Their Gold Standards Both Miss](https://arxiv.org/abs/2608.17051)

**<font color=#1a73e8>作者：</font>** Daniel Palacios, Matthew Brady Neeley, Angel Adetomike Otto 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Secondary use of electronic health records requires de-identification, yet existing systems miss \emph{institutionally situated} protected health information (PHI) such as hospital abbreviations, building names, and internal codes whose status is locally determined. We ask whether large language models (LLMs) with in-context learning (ICL) can close this gap and control the precision--recall trade-off.
On 100 annotated pediatric oncology notes (5,322 PHI spans) from Texas Children's Hospital, we benchmarked eight LLMs against two purpose-built systems (Stanford TiDE, OpenMed PII) and two pattern-based baselines. Each LLM ran under three prompts of increasing specificity: (1) a HIPAA-aligned baseline, (2) baseline plus the institutional PHI categories it missed, and (3) prompt 2 plus instructions against over-redacting clinical content. We then compared 14~multi-agent and ensemble configurations against the best single prompt, with recall the primary safety metric.
LLMs outperformed the purpose-built systems (best F1=0.918$\pm$0.001 vs.\ TiDE 0.779), with advantages concentrated in contextual categories. Naming the missed categories recovered 79\% (48/61) of them, and discouraging over-redaction restored precision. No agentic architecture beat calibrated single-pass prompting (F1 0.906--0.907), but LLM outputs surfaced 414~candidate annotation gaps; re-annotation confirmed 227~PHI spans, against which the final prompt reached recall=0.981 (F1=0.907$\pm$0.002).
Well-calibrated ICL resolves both the institutional PHI gap and the precision--recall trade-off in one LLM call per note. LLMs cost more to run than traditional methods, but that cost buys a way to audit the reference standard.
LLMs are a legitimate, adaptable alternative to purpose-built de-identification systems; institution-specific prompt development should be the primary adaptation strategy.

---


### 10. [J-Miner: Recovering Executable Decision Knowledge from Language-Model Classifiers](https://arxiv.org/abs/2608.17063)

**<font color=#1a73e8>作者：</font>** Yunfan Gao, Xinyi Huang, Tao Sheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models can be fine-tuned into specialized classifiers that perform well across diverse text tasks and make complex judgments, but they typically expose only final labels, leaving the decision knowledge acquired through fine-tuning implicit within the model. We study how to mine this internal decision knowledge from a fine-tuned classifier and encode it in an executable representation that can be inspected, validated, and reused beyond the source classifier. We introduce J-Miner, which mines text-level named concepts by aggregating vocabulary-aligned internal signals across layers and token positions, and uses the classifier's own predictions to learn executable decision rules over them. This process distills local internal readouts into an explicit classifier-level knowledge representation. Across multiple classification tasks, J-Miner rules reproduce up to 98.3\% of source-classifier decisions and achieve 6.0--29.5 percentage points higher behavioral fidelity than equally compact rules learned from input words. Further analysis shows that the named concepts reflect internal semantic evidence associated with task decisions, while the learned rules consolidate these distributed signals into inspectable decision structures. The resulting decision knowledge also transfers to lightweight standalone students: using about 1/24 as many parameters as the source classifiers, they reconstruct and execute the representation from raw text while retaining 99.8\% of the source classifiers' mean task accuracy. These findings show that task-specific decision knowledge can be faithfully represented in an explicit, executable form and reused beyond the classifier in which it was learned.

---


### 11. [DiSCO: Defending text-to-image generation through distribution-guided contrastive prompt optimization](https://arxiv.org/abs/2608.17067)

**<font color=#1a73e8>作者：</font>** Tong Zhang, Motasem Alfarra, Carlos Hinojosa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As text-to-image generative models advance, they raise critical safety concerns, particularly the generation of Not-Safe-For-Work (NSFW) content such as violence and nudity, further exacerbated by red-teaming adversarial attacks. Existing defenses predominantly operate under white-box assumptions, relying on text encoder optimization, weight editing, or inference-time intervention, and fundamentally cannot scale to proprietary models. Black-box alternatives based on LLM prompt rewriting offer broader applicability, yet fail in a critical regime we identify as the \textit{benign adversarial} problem: prompts that are linguistically safe but still trigger harmful generation due to the model's learned data distribution. We propose DiSCO, a zero-shot, strictly black-box defense that operates entirely at the prompt level as a plug-and-play module, requiring no model retraining, fine-tuning, or access to model internals. DiSCO performs distribution-guided suffix expansion via beam search, optimized through contrastive scoring over safe and unsafe image pools generated by the target model itself, with iterative adaptive feedback until safe content is produced. We demonstrate that DiSCO consistently enhances the safety of both undefended and defended models on the I2P benchmark under multiple red-teaming attacks, achieving 37.7% and 25.13% ASR reduction, respectively, while maintaining semantic fidelity and improving image coherence. As a black-box, architecture-agnostic module, DiSCO can be readily applied to any text-to-image system without necessitating any changes to the model itself.

---


### 12. [Foundation Agents Meet Agentic Deep Research: Evidence-Grounded Clinical Code Forecasting](https://arxiv.org/abs/2608.17075)

**<font color=#1a73e8>作者：</font>** Junda Wang, Meysam Ghaffari, Akshat Choube 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Next-encounter ICD forecasting predicts which standardized diagnosis codes will be documented at a future visit from the longitudinal record available beforehand. The task is prospective and multi-label: the target note does not yet exist, and several codes may be correct. Structured EHR foundation models capture recurrence and temporal progression, whereas language foundation models generate flexible diagnostic hypotheses. We introduce ICD-Deepresearch, a DeepResearch workflow that composes these predictive foundation models with medical search and ICD dictionaries. Because no source reveals the future code set, research evaluates candidate transitions by linking patient evidence, external clinical relations, and exact code semantics under a fixed top-K budget. Candidate Generation uses SparseEHR to produce an EHR Prior that initializes two bounded Research Expansion rounds; an independent GPT-5 Direct Forecast supplies complementary candidates. Final Selection validates, deduplicates, and jointly ranks both paths, after which a separate module writes rationales without changing predictions. Finally ICD-Deepresearch achieves patient-averaged precision/recall of 24.60/35.09% on MIMIC-III and 25.14/48.32% on MIMIC-IV. Physicians rate 51% and 68% of its retrieved documents useful, compared with 22% and 39% for standalone GPT-5 web search and 32% and 41% for Medical Deep Research. ICD-Deepresearch therefore improves over the registered local comparators while retrieving evidence with higher physician-rated usefulness than the standalone research systems

---


### 13. [Uncertainty-Aware Decision Making in Multimodal Large Language Models](https://arxiv.org/abs/2608.17084)

**<font color=#1a73e8>作者：</font>** Abderrahmene Boudiaf, Irfan Hussain, Sajid Javed  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) increasingly answer questions whose correctness depends on visual, textual, temporal, acoustic, document, chart, or embodied evidence. Their failures are therefore not only linguistic. A fluent answer may conceal poor input quality, a perceptual error, weak grounding, conflict between modalities, unstable reasoning, distribution shift, or a question that is not answerable from the supplied evidence. This survey organizes the literature on uncertainty-aware MLLMs around a decision-centered framework: uncertainty sources give rise to observable signals, signals must be calibrated or controlled for risk, and calibrated uncertainty should determine the system action. We review work on token and logit uncertainty, semantic disagreement, perturbation instability, grounding and attribution scores, verbalized confidence, verifier and judge scores, conformal prediction, selective answering, abstention, clarification, retrieval, self-checking, and escalation. The central argument is that uncertainty should not be evaluated only as a confidence number; it should be evaluated by whether it improves behavior under insufficient, conflicting, shifted, or high-risk multimodal evidence. We position this survey against text-only uncertainty and abstention surveys, broad MLLM surveys, MLLM hallucination surveys, and safety-oriented reviews. We conclude with open problems in source-aware decomposition, action-aware benchmarks, calibration under shift, black-box uncertainty estimation, broader modality coverage, reproducible reporting, and human-centered uncertainty communication.

---


### 14. [Structured Driving-State Narratives for Small Language Model-Based GNSS Spoofing Detection](https://arxiv.org/abs/2608.17092)

**<font color=#1a73e8>作者：</font>** Abyad Enan, Sagar Dasgupta, Mizanur Rahman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous vehicles (AVs) depend on reliable Global Navigation Satellite System (GNSS) positioning. However, spoofed GNSS signals can induce plausible but incorrect vehicle states. This study develops a small language model (SLM)-based framework for detecting and classifying GNSS spoofing attacks by comparing vehicle behaviors independently derived from GNSS and other sensing sources. The framework converts independent driving states from GNSS and other sensing sources into structured semantic narratives that are provided to an SLM for spoofing detection and attack classification. The performance of the SLM-based framework is compared with large language models (LLMs) fine-tuned on identical training data and evaluated on the same test set. The evaluation considers five classes: no attack, overshoot attack, stopped attack, turn-by-turn attack, and wrong-turn attack. The framework is also evaluated with geographically unseen field data collected in Clemson, South Carolina, United States. Experimental results indicate that the evaluated SLMs achieve performance similar to the LLMs, achieving an average accuracy of 96.99%, precision of 99.05%, recall of 95.59%, and F1-score of 97.18%. In terms of computational efficiency and resource utilization, the SLMs demonstrate advantages over the LLMs by requiring lower inference latency and less GPU memory during both fine-tuning and inference. Evaluation using field data collected in a geographically distinct location further demonstrated its efficacy. The presented framework can detect and classify GNSS spoofing attacks in real-time while requiring relatively low computational and memory resources, and is therefore suitable for deployment on resource-constrained vehicular computing platforms.

---


### 15. [Inference-Time Attention Steering for Vision-Language-Action Driving Models](https://arxiv.org/abs/2608.17095)

**<font color=#1a73e8>作者：</font>** Darshan Nagendra Prasad, Lars Ullrich, Knut Graichen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) driving models couple a reasoning stage with a diffusion-based trajectory decoder, but do not give a direct way to redirect attention toward safety-critical actors at inference time without retraining. We studied a bounded additive pre-softmax attention bias on the visual tokens of detector localized traffic actors on Alpamayo-R1's Qwen3-VL backbone. It is applied as a fail open forward pre-hook with no weight changes. On 50 lane-change scenarios from the Physical AI World Model Synthetic dataset. The trajectory decoder shows a monotonic dose response in the bias magnitude, separate from a paired zero bias control at every tested magnitude. It reaches $\approx 17$\,cm mean displacement with lateral shifts up to $\sim 140$\ cm at the clamp. A layer ablation places the action-relevant signal in late layers, where the effect increases with the number of hooked layers (2.0cm for the first 8 layers; 67.6cm for all 36). A per call injection audit explains why the Chain-of-Causation text never changes. The mask based bias never reaches the reasoning pathway in this serving stack, so the invariance is verified exposure, not robustness. Steered trajectories tend to shift toward the attended actor, suggesting the bias governs where the model looks rather than encoding a target behavior.

---


### 16. [Appearing Legitimate is Not Enough: Interrogating Synthetic Agents in Representational Processes through a Participatory Design Lens](https://arxiv.org/abs/2608.17099)

**<font color=#1a73e8>作者：</font>** Aditya Nayak, Aditi Vashistha, Alissa Centivany 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Synthetic agents built atop LLM-based foundation models are gaining popularity as substitutes for human participants across research contexts, including user-testing, market-research, computational social science, surveys, and qualitative research. We are also witnessing an extension of synthetic agents into experimental implementations of policy consultation, jury deliberation, humanitarian diplomacy, and similar contexts where human participation and representation are central to the perceived legitimacy of the institutional processes. The value of participation extends beyond informational contributions and consensus generation; participation is a necessary, legitimizing condition for democratic political institutions and processes. Treating synthetic agents as human substitutes raises serious political, representational, and ethical concerns. Participatory Design's modes of engagement --- probing, priming, understanding, and generating --- offer helpful tools for engaging with representational questions of personhood. We apply the lens to three case studies of synthetic agents substituting for personhood at varying representational scales: local policy, enterprise jury deliberation, and global diplomacy. We argue that legitimacy and personhood are integral and mutually constitutive while identifying the ethical, representational, and methodological risks of using synthetic agents in representational processes. We conclude by proposing soft and hard boundaries for designing oversight on LLMs and synthetic agents in representational processes.

---


### 17. [Emotion Across Speech and Faces: Shared Affective Mechanisms in Multimodal Foundation Models](https://arxiv.org/abs/2608.17102)

**<font color=#1a73e8>作者：</font>** Xiutian Zhao, Luqi Sun, Björn Schuller 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern multimodal foundation models (MFMs) have made rapid progress on tasks requiring integrated perception across speech, vision, and language, including emotion recognition. However, it remains unclear whether they recognize speech and facial emotion through shared affective functional units or modality-specific pathways. We explore emotion-sensitive neurons (ESNs), sparse decoder neurons selectively associated with emotion categories, in three MFMs: Gemma-4-12B-it, MiniCPM-o-4.5, and Qwen2.5-Omni-7B. Using speech emotion recognition and facial expression recognition as complementary probes, we identify acoustic and visual ESNs. Visual ESNs are causally meaningful: deactivating them selectively impairs recognition of the associated facial emotion, whereas steering their activations selectively enhances recognition of that emotion relative to other emotion categories. Acoustic and visual ESNs further show emotion-matched overlap and similar layer-wise distributions, indicating partial structural alignment between affective representations across speech and faces. Finally, cross-modal interventions reveal bidirectional causal transfer: ESNs identified from one modality produce emotion-specific effects when applied to the other. Our findings provide one of the first cross-modality activation-level analyses of affective functional units in MFMs, suggesting that speech and facial emotion recognition partially converge onto sparse decoder-level components that can be localized and manipulated without training.

---


### 18. [Children, but not language models, show accelerating returns in word learning](https://arxiv.org/abs/2608.17120)

**<font color=#1a73e8>作者：</font>** Michael C. Frank  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Children learn hundreds of words over the first years of their lives, in a process that begins slowly but quickly picks up speed. Prior models describe vocabulary growth as evidence accumulation over time. Here we show that the process is best characterized as accelerating accumulation: children learn more from each additional unit of linguistic experience than they did from the one before. In contrast to children, language models -- even those trained on child-directed speech -- do not accelerate. Instead, they show constant proportional returns on new data, consistent with scaling laws. Children learn using many orders of magnitude less training data than language models; their increasingly efficient use of their learning input is a candidate explanation.

---


### 19. [A decodability criterion predicts when hidden-state selection beats majority voting in large language models](https://arxiv.org/abs/2608.17124)

**<font color=#1a73e8>作者：</font>** Zhixiang wang, Ziliang Hong, Ulas Bagci  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Combining the answers a large language model (LLM) samples for a question into one decision is a test-time information fusion problem, usually solved by majority voting. Voting is unreliable on difficult questions, where the sampled answers share correlated errors, so the wrong answer can win and drawing more samples makes the decision worse. Selecting a candidate by reading a correctness signal from the model's hidden states is a promising alternative, but its accuracy varies across models and tasks, and no measure indicates when it can be trusted. In this paper, we propose CASE (Correctness-Axis SElection), a dynamic selection combiner that trains a linear gate on the answer-token hidden state and selects the highest-scoring candidate. Its main contribution is decodability, a leakage-free measure of how well the gate ranks a question's correct candidates above its incorrect ones, which predicts whether hidden-state selection will outperform voting. A conventional probe appears accurate only because of question-identity leakage, which vanishes under question-grouped evaluation. On held-out data, decodability predicts the accuracy gain of selection over voting with a Pearson correlation r=0.75 and a decision threshold near AUC=0.60. Across general and medical LLMs, CASE improves over voting by up to 19 points on medium-difficulty questions and 16.8 points on hard questions. Decodability depends on the aligned knowledge a model must recall, not on its scale, and its prediction transfers to an unseen scientific domain within 3.8 points. It thus provides a practical criterion, measurable in advance for a given model and task, for choosing between learned selection and majority voting.

---


### 20. [PROBE: Manipulation-Grounded Visual Question Answering with VLM Agents](https://arxiv.org/abs/2608.17129)

**<font color=#1a73e8>作者：</font>** Vineet Bhat, Siyi Chen, Alex Zook 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language Models (VLMs) excel at 2D grounding, spatial reasoning and agentic tool-based planning in static scenes. However, consider asking a home robot "Is my medication still in the cabinet?" The answer may be physically hidden behind a row of containers that must first be moved aside. Answering such questions in real-world cluttered environments requires reasoning in dynamic scenes: distractors must be manipulated to reveal occluded objects, and each action changes the scene the model must reason over. We formalize this setting as Manipulation-Grounded Visual Question Answering (MG-VQA) and introduce PROBE, a framework for benchmarking and finetuning VLM agents on such tasks. We first develop PROBE-Sim, a high-fidelity tabletop simulator with everyday objects and a robot manipulator equipped with grasping and pushing tools. PROBE-Sim is used to create PROBE-Bench: an evaluation suite of 150 tasks across 6 question types on cluttered tabletop scenes, where a VLM perceives, picks up or pushes objects before answering. We observe consistent trend across all frontier VLMs: agentic tool-based methods outperform their perception-only baselines (8.0% on average) across all task types. We further design PROBE-Agent, a finetuning recipe to distill successful trajectories from a powerful teacher foundation model to a smaller open-weight model using a mixed data recipe that encourages manipulation-efficient question answering. PROBE Agent finetuned models outperform their off-the-shelf agent baseline (11.5% on average) and demonstrate positive transfer to unseen objects and a held-out task. We validate sim-to-real transfer by deploying PROBE-Agent finetuned policies in real-world tabletop environments.

---


### 21. [Authorization Before Context: A Model-Neutral Audience Boundary Against Cross-Audience Memory Leakage in Agentic Systems](https://arxiv.org/abs/2608.17148)

**<font color=#1a73e8>作者：</font>** Sibo Liu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A personal language agent learns a fact from one audience and may later place it in the prompt it assembles for another. This memory-to-context step is an attack surface: ambiguous or inconsistent channels, cross-audience prying, and poisoned memory can each cause the system to assemble context containing a fact relevant to the query yet unauthorized for the current viewers. We introduce authorization before context: a single, anti-monotone audience-membership rule applied at the memory-to-context transition. Each item carries the audience present when it was recorded; the current viewer set is read from channel metadata and falls back to public when ambiguous; and the item is admitted only when every current viewer already belonged to its audience. We prove that this rule gives every participant cross-channel recall while ensuring, by exclusion rather than by model behavior, that nothing recorded for a narrower audience reaches a broader one and that poisoned memory cannot widen its own audience. The boundary is a model-neutral invariant on the exact assembled context: a forbidden fact must be absent before the model is called. On a synthetic Contextual-Integrity suite, no forbidden fact entered the context our boundary assembled, whereas unscoped baselines included such facts by construction; we further audit that every read path fails closed. The evidence is preliminary and synthetic.

---


### 22. [KnowSim: Evaluating Information Calibration in LLM Assistants with User Simulators that Learn](https://arxiv.org/abs/2608.17150)

**<font color=#1a73e8>作者：</font>** Yoonjoo Lee, Hyoungwook Jin, Tae Soo Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> To effectively collaborate with users on knowledge-intensive tasks, Large Language Models (LLMs) must perform information calibration: matching content to a user's evolving understanding and cognitive capacity. Yet user simulators used to evaluate and train LLMs do not explicitly model user knowledge so they neither produce realistic interactions across knowledge levels nor reflect how interactions unfold as that knowledge evolves. To close this gap, we introduce KNOWSIM, an evaluation framework built around a user simulator that maintains explicit knowledge states, represented as a graph of Information Units with prerequisite relationships, that evolve under update rules grounded in learning theory. KNOWSIM computes three metrics (Knowledge Gain, Delivery Calibration, Cognitive Overload) directly from the knowledge state trajectory, reflecting key mechanistic aspects of information calibration. We validate KNOWSIM against 705 human-AI sessions across two domains, stratified by knowledge level: its rankings align significantly with human judgments (73-74% sign agreement), outperforming three baseline simulators. Applied to 9 LLMs, KNOWSIM reveals that the best model shifts by user knowledge level, revealing aptitude-treatment interactions invisible to standard evaluation.

---


### 23. [Lymphocyte Mimicry Correction via Region-Level Tissue Reasoning and Unbalanced Optimal Transport](https://arxiv.org/abs/2608.17151)

**<font color=#1a73e8>作者：</font>** Xiang Li, Yuqi Wang, Casey C. Heirman 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cell mimicry arises when different cell types appear morphologically similar. Human pathologists resolve this ambiguity using surrounding tissue context, whereas current vision models either lack contextual reasoning (cell foundation models) or cannot operate at the cell level (pathology MLLMs). We present Loki-OT, which propagates region-level tissue reasoning to individual cell predictions via Unbalanced Optimal Transport, using MLLM-derived density priors as soft guidance for ambiguous cell reassignment. Loki-OT is motivated by the observation that pretrained cell foundation model features already encode discriminative information, including tissue context, but standard cell-level supervision fails to use tissue context effectively. The resulting transport plan is distilled into a lightweight student MLP classifier that learns context-aware decision boundaries within the pretrained feature space. On the independent TCGA-BRCA cohort, Loki-OT achieved lower patient-level MAE than the fully supervised in-domain PanopTILs classifier and improved F1 in epithelium-rich mimicry tissues, using 278 weak region-level MLLM estimates built on a general-domain cell foundation model. Code: this https URL

---


### 24. [Towards Safer RAG: Only Agents Capable of System 2 Thinking may Access Untrusted Documents](https://arxiv.org/abs/2608.17153)

**<font color=#1a73e8>作者：</font>** Mehrdad Ghassabi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) has significantly enhanced the performance of large language models (LLMs), yet these systems remain vulnerable to knowledge-poisoning attacks, in which misinformation in retrieved documents can influence the model's final outputs. Notably, an LLM may correctly detect that a document contains incorrect information while nevertheless being influenced by it. Prior work has addressed this vulnerability through the Cordon Principle, which prevents models responsible for final answer synthesis from directly accessing raw evidence. Although effective, this strict isolation can introduce substantial computational overhead. In this work, we propose a refined security principle: only agents capable of deliberative System 2 reasoning may access untrusted documents. To evaluate this principle, we introduce novel metrics that quantify the discrepancy between misinformation detection and downstream influence. We then empirically compare state-of-the-art reasoning language models with standard language models across these metrics. Our results show that reasoning-capable models are substantially more robust to corrupted evidence, without requiring the strict isolation imposed by the Cordon Principle. These findings provide empirical support for our refined principle and suggest a more practical foundation for secure RAG system design.

---


### 25. [Beyond the Hype: Evaluating LLM Integration and Practical Limitations in Security Operation Centers](https://arxiv.org/abs/2608.17154)

**<font color=#1a73e8>作者：</font>** Elnaz Rabieinejad, Ali Dehghantanha, Fattane Zarrinkalam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly being explored within Security Operation Centers (SOCs) to support text-heavy analytical work such as alert contextualization, incident summarization, and drafting investigative artifacts. Despite this interest, practitioners describe critical operational concerns, most notably hallucinations (plausible but incorrect outputs), opaque reasoning, and the verification effort required to safely use model-generated content in security workflows. In this paper, we present findings from semi-structured interviews with 20 SOC practitioners spanning frontline analysts, SOC managers, and tool developers. Participants report perceived time savings for low-stakes tasks that are quickly verifiable (e.g., summarizing logs or drafting initial investigative leads), but they consistently frame LLM outputs as preliminary drafts and suggestions rather than decision-grade conclusions. Participants also describe limited trust in LLMs for high-stakes security decisions due to unreliable outputs and unclear model reasoning, and they report relying primarily on ad-hoc verification norms and continuous human oversight rather than standardized mitigation procedures. Based on these interview-grounded accounts, we introduce a maturity rubric to characterize readiness for LLM integration and outline a research agenda emphasizing auditability and transparent explanation mechanisms to support safer adoption in SOC workflows.

---


### 26. [OraclePhys: A Systematic Framework for LLM Fine-Tuning on Structural Mechanics](https://arxiv.org/abs/2608.17162)

**<font color=#1a73e8>作者：</font>** Mingyu Li, Guorui Song, Jing Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> What a language model internalizes from fine-tuning is usually diagnosed after the fact. We make it an experimental variable. OraclePhys is a systematic fine-tuning framework with three components: OraclePhys-Bench, an exactly-graded structural-mechanics benchmark whose finite-element oracle scores every answer and counterfactual edit -- no human labels, no LLM judging; OraclePhys-30K, a supervision dataset of seven answer forms over byte-identical structure descriptions; and a controlled training study across the seven forms and three verifier roles. The study yields two findings. First, the label's answer form -- not its bit count -- causally determines what fine-tuning teaches: a ranking objective installs an out-of-distribution forward model where the untrained base sits at the guessing prior, a scalar objective at best a partial one, a boolean nothing detectable; the vector-scalar gulf survives a second physics domain, a second model family, and a paraphrased evaluation surface. Second, written or score-filtered answers install this capability, while advantage-weighted scores (GRPO) raise reward yet leave the model statistically equivalent to its start on held-out physics -- within the recipes and budgets tested -- sufficing only for routing. The trained 8B -- the first LLM on spatial structural response -- reaches the task's data-precision frontier: above a frontier LLM at zero- and 32-shot, at a specialist's level. What the label spells out about the target computation is what fine-tuning teaches; what you train on is what you route.

---


### 27. [Q-Learning With World Models](https://arxiv.org/abs/2608.17163)

**<font color=#1a73e8>作者：</font>** Perry Dong, Yueru Jia, Chelsea Finn 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Off-policy reinforcement learning (RL) has become increasingly sample-efficient, enabling applications such as RL fine-tuning of Vision-Language-Action models into reliable, high-performing policies. World models offer a further lever for sample efficiency, as they predict state changes rather than actions alone, but their success has largely been confined to supervised policy learning. Prior model-based RL methods often optimize the policy or value function directly on imagined rollouts, which is prone to compounding bias and struggles to scale to large, high-dimensional problems such as real-world robotics, a problem that worsens with task horizon and visual complexity. In this work, we instead ask whether we can leverage world models directly on top of standard Q-learning to improve performance, while remaining trained and grounded in the real, online setting. We propose QWM, a framework that leverages world models to perform test-time search over imagined trajectories on top of Q-learning to select high-value actions during both online rollouts and evaluation. Since the policy and value function are trained only on real transitions, QWM avoids compounding model bias while still gaining the sample-efficiency benefits of predictive search. On challenging manipulation benchmarks Robomimic and LIBERO, QWM significantly outperforms strong prior state-of-the-art methods on both sample efficiency and performance.

---


### 28. [SCENARIODIFF: A Scenario-level Guidance Framework for Multimodal Time Series Forecasting--Extended Version](https://arxiv.org/abs/2608.17164)

**<font color=#1a73e8>作者：</font>** Tuan-Binh Tran, Dat Nguyen Cong, Duc-Trong Le 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Textual context such as news, reports, and logs can provide valuable signals for time series forecasting, especially when future dynamics are driven by external events that are not yet visible in historical values. Existing multimodal forecasting methods often either ask large language models (LLMs) to predict numerical values directly or fuse text and time series implicitly, making contextual influence difficult to interpret and control. We propose SCENARIODIFF, a hierarchical contextual reasoning framework for multimodal time series forecasting under noisy and weakly aligned documents. SCENARIODIFF organizes contextual information into three levels: a Historical Context Agent extracts stepwise evidence from raw documents, a Scenario Agent produces a qualitative scenario description for the forecast horizon, and an Anchor Guidance Agent generates sparse anchor points for event-relevant future regions. These structured signals condition a Multimodal Diffusion Transformer, while Anchor Blended Sampling locally refines generated trajectories without retraining. Experiments on the Time-MMD benchmark show that SCENARIODIFF is especially effective in event-driven domains, demonstrating the value of explicit hierarchical scenario guidance for multimodal time series forecasting. Our full implementation is available at this https URL

---


### 29. [Can LLMs Reason in a Legally Meaningful Manner? A Small-scale Study on European Court of Human Rights Cases](https://arxiv.org/abs/2608.17168)

**<font color=#1a73e8>作者：</font>** Amogh Raina, Ilias Chalkidis, Daniel Hershcovich 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning has become a standard technique and feature for contemporary LLMs; however, its application and quality in the context of demanding legal-oriented tasks, such as legal case forecasting, remain under explored. We investigate how LLMs reason in the context of legal case forecasting, using legal cases from the European Court of Human Rights (ECtHR) as a testbed. We evaluate OpenAI GPT 5.4, a recent top-tier LLM, by exploring alternative prompting strategies that are more or less suggestive of what counts as legally meaningful reasoning in the context of ECtHR jurisprudence. We present our findings derived from assessing the model's responses with both human and LLM evaluation. We find that the examined model scores far from ideal in legal reasoning, the model produces structurally complete but substantively shallow analyses, and that LLM-as-a-Judge evaluators are internally consistent yet align only weakly with our trained annotators, i.e., reliable but not a valid substitute for human evaluation. Overall, the expert-curated prompt leads to more comprehensive reasoning, which does not result in more accurate predictions compared to the other examined settings. Based on our findings, we urge the community not to rely solely on automated LLM-based evaluation and to avoid using task accuracy as an appropriate proxy for reasoning quality.

---


### 30. [Synthesizing Feature Extractors: An Agentic Approach for Algorithm Selection](https://arxiv.org/abs/2608.17170)

**<font color=#1a73e8>作者：</font>** Hai Xia, Carlos Ansótegui, Stefan Szeider  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Algorithm selection for constraint satisfaction problems requires extracting features that capture problem structure. Manually designing feature extractors demands deep domain expertise and quickly becomes a bottleneck when new problem classes appear. We present an automated approach that uses Large Language Models (LLMs) in an agentic check--fix--verify loop to synthesize executable Python scripts that act as interpretable, problem-specific feature extractors. Given a high-level MiniZinc model and an instance, the LLM agent generates code that constructs a typed graph representation and computes structural properties such as graph density, variable clustering, and constraint tightness. We evaluate our approach on three combinatorial problems (vehicle routing, car sequencing, fixed-length error-correcting codes) with a portfolio of five state-of-the-art solvers. The synthesized extractors yield algorithm selectors that consistently outperform both expert-curated mzn2feat features (up to $8.3$ percentage points (pp) test-set accuracy on FLECC) and the best transformer-based trans2feat variants. In the meanwhile, the synthesized feature extractors remain inspectable.

---


### 31. [Polaris: Learning to Generate Table Descriptions from Retrieval Feedback](https://arxiv.org/abs/2608.17171)

**<font color=#1a73e8>作者：</font>** Ting Cai, Tuan Minh Phan, AnHai Doan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Many table-centric NLP tasks such as NL2SQL first retrieve relevant tables from large collections using keyword search. Recent work uses LLMs to generate natural-language table descriptions to improve retrieval, but they are typically optimized for fluency rather than retrieval effectiveness. We present Polaris, a system that trains an LLM to generate table descriptions directly from retrieval feedback. Our key insight is that existing table retrieval benchmarks already contain the supervision needed for this task: given query-table relevance judgments, we generate multiple candidate descriptions for each table, rank them by their BM25 retrieval effectiveness, and use the resulting preference pairs to fine-tune the LLM with Direct Preference Optimization (DPO). Polaris further expands abbreviated table and column names before generation to reduce vocabulary mismatch. Extensive experiments show that Polaris outperforms the state-of-the-art AutoDDG solution, often by a significant margin. More broadly, our results demonstrate that retrieval benchmarks can be repurposed as supervision for training LLMs to generate retrieval-oriented metadata.

---


### 32. [Balancing Safety and Autonomy: Accessibility-Oriented Interventions in Generative AI for Cognitive Impairment](https://arxiv.org/abs/2608.17175)

**<font color=#1a73e8>作者：</font>** Yibo Meng, Jingruo Chen, Lyumanshan Ye 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI systems are increasingly used by older adults with cognitive impairment for everyday tasks such as information seeking, health management, and communication. While these systems provide flexible, language-based support, their open-ended outputs introduce risks of over-reliance, misinterpretation, and inappropriate decision-making. Prior work has focused on usability and adoption, with limited attention to how system design shapes users' participation in decision-making and the distribution of agency in care contexts. We present a qualitative study of 45 individuals with cognitive impairment and their caregivers. We identify five accessibility-oriented mechanisms: AI Capability Constraint, Human Oversight Embedding, Cognitive Engagement Maintenance, Human-AI Relationship Regulation, and Risk Transparency and Control, through which systems structure interaction. These mechanisms both support and constrain users by redistributing decision-making across users and caregivers. We show that their effects vary by impairment level: while protective mechanisms support users with severe impairment, they can restrict autonomy for those with mild impairment. As impairment progresses, tensions become less visible as user participation diminishes. Our findings highlight the need for dynamic designs that balance safety and autonomy in AI-supported care.

---


### 33. [Task Specialization Fine-Tuning for Contextual Reinforcement Learning](https://arxiv.org/abs/2608.17180)

**<font color=#1a73e8>作者：</font>** Jianan Zhou, Jung-Hoon Cho, Tianyue Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contextual Reinforcement Learning (CRL) seeks to generalize classical RL by maximizing task coverage across a context space of related tasks. While prior works often train from scratch and rely on either multi-task learning for a single policy or strategically training multiple policies, we advocate for a unified alternative: pretraining a single policy with good initial performance, followed by fine-tuning multiple policies for task specialization. This new paradigm, however, introduces unique challenges, such as heterogeneous marginal returns and sample inefficiency. This raises a critical research question: given a pretrained policy and a constrained budget, how much fine-tuning should each task region receive to enable sample-efficient CRL? To this end, we propose Task Specialization Fine-Tuning (TSFT), an online framework that predicts fine-tuning performance with a simple parametric model and exactly solves the resulting discrete budget allocation problem via integer linear programming. Extensive experiments across diverse decision domains, including combinatorial optimization, continuous control, and LLM fine-tuning, demonstrate that TSFT significantly outperforms baselines in task coverage and approaches oracle performance. Our work charts a new direction for model-based CRL, aligning with the modern pretrain-finetune era.

---


### 34. [Benchmarking the Benchmarks: Evaluating Automated Safety Benchmarks for Small Language Models](https://arxiv.org/abs/2608.17183)

**<font color=#1a73e8>作者：</font>** Nyamtulla Shaik, Fengjun Li, Bo Luo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Small Language Models (SLMs) are increasingly deployed in resource-constrained, privacy-sensitive settings, where safety and bias failures can cause security and societal risks. However, existing AI safety\slash security\slash compliance benchmarks are designed for large language models that may not transfer reliably to SLMs. We therefore ask: Can these benchmarks effectively and reliably evaluate SLMs? To answer this question, we conduct a large-scale assessment of the effectiveness and robustness of these automated pipelines by evaluating five widely used benchmark suites across 26 open-source SLMs under a unified judging rubric, which assigns a score of 0, 1, or 0.5 to harmful, safe, or ambiguous/irrelevant responses, respectively. Across the benchmarks, ambiguous judgments dominate and correlate with prompt complexity and model architecture, indicating that {\em LLM-centric safety benchmarks are insufficient as standalone evidence for SLM safety assessment}. In general, the ambiguity rate increases with lexical density, output perplexity, and output length and decreases with lexical sophistication, self-coherence, and reply-prompt similarity. This reveals a capability-safety confound that mixes model capability with apparent safety. Since ambiguity is prevalent, aggregate mean-score leaderboards are mathematically brittle: model rankings change significantly under reasonable ambiguity treatments, even when the underlying outputs remain unchanged.

---


### 35. [AISA: AI Safety Assistant Framework for Continuous Improvement of Highway Construction](https://arxiv.org/abs/2608.17184)

**<font color=#1a73e8>作者：</font>** Mason Smetana, Trevor Neece, Lev Khazanovich  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Job Safety Analysis (JSA) and pre-task planning can benefit from prior incident records, yet historical accident data is often stored as unstructured narratives that are difficult to consult at the point of planning. A novel framework centered on large language models (LLMs) for highway construction safety reporting and planning is proposed as a foundation for future agentic applications, prioritizing deterministic, local inferencing. The first aim is to enable classification and quality scoring of incident narratives for existing and future reporting purposes. The second is to evaluate retrieval of relevant historical accidents, related imagery, and trusted industry documents for incorporation into daily safety plans. Neural probes were trained to classify incidents along four multiclass and two binary Occupational Injury and Illness Classification System (OIICS) fields and to derive an overall quality score, evaluated on a test set of over 15,000 narratives and a held-out set of 100 author-labeled records, benchmarked against a majority-vote LLM ensemble. The retrieval of historical accidents, reference imagery, and industry documents was benchmarked across embedding models using standard information retrieval metrics. OIICS classification reached 75% held-out accuracy, though the two binary flags were degenerate. The quality score, while meaningful on one database, was distorted on out-of-distribution fatalities in the held-out dataset. Accident retrieval recovered relevant incidents far above chance, performing best on lexically distinct construction activities. On document question answering, an open-weight decoder embedding model surpassed proprietary models. Overall, this work provides a new framework rooted in local inferencing and text embedding models for future agentic applications, with emphasis on bridging external data to JSA reports.

---


### 36. [Token Optimization and Context Window Management in Multi-Agent AI Workflows](https://arxiv.org/abs/2608.17188)

**<font color=#1a73e8>作者：</font>** Dvir Shamay  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-agent AI workflows are limited not only by model quality but by token cost, latency, and context-window quality. This paper presents a practitioner framework for token optimization and context-window management, grounded in an internal production dashboard that extracts structured work items from meetings, email, and chat with LLMs and routes summaries across workstreams. Six patterns are described: context stratification, fetch-once/process-locally architecture, schema-contracted prompts, token-aware fallback chains, semantic caching, and inter-agent communication compression. In production they cut measured cold-load latency to 61-116 seconds (six timed runs) from an operational baseline of roughly 3.5-10.5 minutes, with an estimated 60-70% token reduction. It also reports a controlled context-composition study: 2,420 confirmatory trials across 11 model configurations, using 661 anonymized workplace items scored for relevance. Holding the prompt at a fixed ten items, replacing some high-relevance items with same-domain low-relevance items improves the model's relevance-score concordance on the target items, versus high-relevance items only; we call this relevance-contrast context. In the all-11 paired analysis, the 50:50 signal/noise condition improved relevance accuracy by +0.077 over the 100% condition (naive 95% CI [+0.056, +0.098], Cohen's d = 0.49, Holm-adjusted p < .001, n = 220). These cells are not independent; by the nine model families the effect is +0.084 (95% interval [+0.064, +0.103]), reported as a within-corpus descriptive comparison, not a population inference. A Fusion-of-N follow-up found that learned synthesis did not beat the mechanical set union of item IDs. The contribution is a measured engineering layer between model research and production agent practice: repeatable patterns and evaluation methods for faster, cheaper, more reliable workflows.

---


### 37. [Which Source Wins? Task-Dependent Reliance in Vision-Language Models](https://arxiv.org/abs/2608.17205)

**<font color=#1a73e8>作者：</font>** Rodela Ghosh, Aviral Gupta, Guangjing Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) combine images and text, but when the two conflict and one becomes harder to read, it is unclear how a model shifts its reliance between them. We study this modality reallocation with a controlled setup: we degrade either the image or the text across four levels of legibility while keeping the other clean, and track how the model's preference changes. We build conflicts from GSM8K and SVAMP by pairing the rendered image of one arithmetic problem with the text of another, so the two sources support different answers. We also introduce ChartQA-Conflict, a manually reviewed benchmark of 229 chart-report conflicts with matched chart and table-image representations. We evaluate six open-weight VLMs using both generated answers and a length-normalized conditional log-likelihood margin. On GSM8K and SVAMP, five of six models shift more strongly away from degraded text than from degraded images. On ChartQA-Conflict, all six likelihood-scored models exhibit the opposite pattern, shifting more strongly away from the degraded visual source. This reversal persists after calibrating for unimodal accuracy loss and after replacing charts with plain table images. Two frontier API models, GPT-5.6-Luna and Gemini-3.5-Flash, behaviorally replicate the ChartQA-Conflict reversal, with GPT-5.6-Luna also matching the arithmetic direction. These results show that modality reliance in VLMs is not fixed, but varies across tasks, evidence structures, models, and evaluation settings. The source code is available at this https URL.

---


### 38. [The Plot Thins: Uniformity and Linearity in Literary Summaries](https://arxiv.org/abs/2608.17218)

**<font color=#1a73e8>作者：</font>** Rebecca M. M. Hicke, Sil Hamilton, David Mimno 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Works of literature are complicated; they balance plot, suspense, surprise, and artistic expression. Summaries of literature prioritize plot, and therefore may deviate from their sources. Using a combination of manual and LLM-based annotation, we construct a dataset mapping sentences from 150 novel summaries to their respective source chapters. We find the task unexpectedly difficult for both human and model annotators. Using the sentence-to-chapter mappings, we then measure summary linearity, the degree to which it maintains the source's order of events, and uniformity, the degree to which a summary spreads attention equally across a source. By examining when and how summaries break linearity and uniformity, we identify differences in how literary works and summaries express plot, particularly with regard to the clarity and prominence with which narrative details are described.

---


### 39. [PACE: Policy-Attested Contract Execution for Safe AI Agents in Decentralized Finance](https://arxiv.org/abs/2608.17220)

**<font color=#1a73e8>作者：</font>** Rabimba Karanjai, Yang Lu, Richard Williamson 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous AI agents are emerging as interfaces for decentralized finance (DeFi) actions such as swaps, lending operations, and yield management. Because these agents rely on large language models (LLMs) to plan transactions, they inherit the LLM's susceptibility to prompt injection and lack of mechanisms to bind a verifier's approval to the exact transaction ultimately submitted on-chain. We present PACE (Policy-Attested Contract Execution), a transaction-level authorization framework that interposes between an LLM-based agent and on-chain execution. PACE introduces typed transaction intents, a deterministic policy verifier, and signed Policy Decision Records (PDRs) that cryptographically bind the approved intent, policy, and simulation report to the exact execution bytes, with replay and expiration protection. A Solidity smart account enforces PDR signatures on-chain with a measured overhead of 29,826-31,822 gas. We evaluate PACE against six baselines on 40 tasks spanning four attack categories plus benign utility (2,800 trials, 10 seeds). In our deterministic sandbox, PACE achieves a 0.00 unsafe execution rate and 0.00 false-positive rate on benign tasks, compared to 0.80 for the unguarded baseline. Ablation studies identify permissive policy settings (+57.5 pp) and the touched-contract allowlist (+12.5 pp) as the dominant safety components. To test whether the same deterministic floor holds for real model outputs, the artifact additionally provides a three-model live-LLM evaluation over the full task suite with repeated runs. A mainnet-fork harness is included for archive-RPC deployments, but fork results are reported only when the corresponding artifacts are generated. These auxiliary studies are separate from, and never substitute for, the deterministic benchmark. We frame our claims as logic-level safety within a reproducible benchmark rather than deployment-ready DeFi security.

---


### 40. [Temporal Leakage in Financial News NLP: A Multi-Architecture Audit with a Regime-Specific M&A Signal](https://arxiv.org/abs/2608.17223)

**<font color=#1a73e8>作者：</font>** Chenhao Xue, Raslen Guesmi, Siwei Feng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Financial-news direction prediction has become a popular NLP benchmark, yet reported gains depend critically on whether the train-test split is chronological or random, i.e., on temporal leakage. We audit this dependence on a 49,799-article corpus across 16 feature-model combinations spanning TF-IDF, MiniLM, FinBERT, and fine-tuned RoBERTa-large / DeBERTa-v3-large, plus separate zero/few-shot and LoRA probes of Llama-3 and Qwen2.5 LLMs: random splits inflate MCC by $1.1\times$ to $6.5\times$, tracking model capacity and feature richness, and end-to-end FinBERT fine-tuning re-amplifies rather than closes the gap (size-matched ratio $1.75\times$). Conditioning on event type, mergers and acquisitions (M&A) is the only audited category with a positive locked-test signal under near-temporal chronological evaluation (TF-IDF MCC $= 0.138$ train-only, $0.068$ under train$\cup$val refit; 10,000-permutation $p < 10^{-3}$); the signal does not transfer to FNSPID's 2009-2020 U.S. corpus, localising the headline to our 2024-2025 European-tilted M&A semantics rather than a universal predictor. Three independent role labellers converge on acquirer-tagged articles as the signal locus, a power-limited qualitative convergence rather than a hypothesis-tested asymmetry. Chronological splitting plays for financial NLP the role characteristics-purging plays for asset pricing: it strips the predictable, stale component of news and leaves a residual that is small, event-localized, and lexically shallow. We advocate leakage audits as a required disclosure for financial-NLP benchmarks.

---


### 41. [COMIC: Reference-Aware Safety Gating for Multimodal Large Language Models](https://arxiv.org/abs/2608.17234)

**<font color=#1a73e8>作者：</font>** Md Abdullahil Oaphy, Anhao Xiang, Zongxing Xie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) are increasingly used to interact with screenshots, scanned documents, diagrams, and other visually grounded inputs. This shift introduces a new safety risk: in many multimodal jailbreaks, neither the prompt nor the image is harmful in isolation. Unsafe behavior emerges only when the model binds an apparently benign operation, such as summarizing, translating, or following, to a localized visual target. This reveals a structural weakness in current multimodal defenses, which largely moderate the prompt-image pair as a whole even though the true security-relevant unit is the grounded operation-target pair produced during dereference. In this work, we identify and analyze this reference-dependent failure mode and show that existing defenses degrade when harmful semantics are localized, activated only after grounding, and dependent on visual reference resolution. To address this problem, we propose COMIC (Context-Operation-Modality-Image-Classifier), a reference-aware pre-generation safety gate for MLLMs. COMIC first infers the requested operation and reference type, constructs candidate targets from OCR and open-vocabulary proposals, grounds plausible referents, and evaluates safety over explicit operation-target pairs. To handle ambiguity conservatively, COMIC combines max-risk aggregation with quality-aware routing before deciding whether to forward or block a request. We evaluate COMIC across multiple open-source MLLMs, localized and broader multimodal jailbreak benchmarks, and benign reference-sensitive settings. The results show that COMIC consistently improves robustness while preserving benign utility and practical efficiency. More broadly, our findings suggest that multimodal safety cannot be enforced reliably without modeling the requested operation, the visual target to which it applies, and the confidence of that grounding.

---


### 42. [Structural Plan-to-Model Conversion with Deterministic Geometry and Guarded Agentic Vision-Language Refinement](https://arxiv.org/abs/2608.17237)

**<font color=#1a73e8>作者：</font>** Mohammad Talebi-Kalaleh, Qipei Mei  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Converting structural framing plans into editable finite-element model drafts remains labor-intensive and prone to transcription error. Existing drawing-understanding systems for building components rely on task-specific trained neural detectors, and language-model agents in structural engineering operate on text or model data rather than the drawing itself. This paper presents, to the authors' knowledge, the first framework applying an agentic vision-language layer to structural component detection and model drafting from framing-plan PDFs, without task-specific detector training or fine-tuning. A deterministic stage extracts primitives, estimates scale by dimension-ratio consensus, recognizes five entity classes with a drafting grammar, and assembles an editable layout. The agentic stage proposes typed corrections constrained by deterministic candidates, operation-specific admission tests, change-level review, and fail-closed transactions. Evaluation used an author-generated benchmark of 100 plans: a development half that informed every rule revision, and a seed-disjoint held-out half generated after the rules froze, evaluated once. All reported scores are end-to-end results of the complete framework on the held-out half. Scale was estimated within 0.1% of the generator reference for every drawing. Recall and precision were 0.922/0.997 for columns, 0.886/0.990 for beams, 1.000/1.000 for walls, 1.000/1.000 for braces, and 1.000/0.964 for openings. A controlled study repeated two corruptions three times on three development drawings. Calibration passed all nine trials; member repair met every strict end-state predicate in five of nine. Guarded review corrected missed framing and false marks within explicit bounds. The held-out half shares the development generator, so the study excludes independently drafted plans, raster evaluation, analytical connectivity, and solver validation.

---


### 43. [Explicit State Elicitation Is Not Enough: A Controlled Audit of Memory-Policy Classification](https://arxiv.org/abs/2608.17247)

**<font color=#1a73e8>作者：</font>** Yihang Chen, Pin Qian, Su Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personalized agents must decide whether retrieved user memory should be used, ignored, updated, or queried before it affects a current task. We use this setting to develop an empirical audit protocol for structured intermediate outputs: first audit dataset shortcuts, then isolate bundled prompt changes, check whether intermediate labels are answer-associated, test decomposed semantic evidence, and audit provider-level execution failures. A 480-example synthetic development set initially suggested large gains from a state-structured prompt bundle, but TF-IDF diagnostics showed lexical separability and no positive standalone Ignore cases. We therefore construct a frozen 160-example controlled counterfactual set with 40 matched four-way families and rule-derived reference policies. On this set, exposing the four state definitions improves accuracy, but an isolated explicit state-output field does not significantly improve policy accuracy for Llama-3.3-70B and gives only a marginal, non-significant gain for GPT-OSS-120B. Supplying benchmark-associated state labels shifts policy predictions, but because those labels deterministically map to policies, this is a label-conditioning diagnostic rather than evidence of a faithful internal mechanism. Family-level and seed-stability analyses further show that example-level accuracy overstates counterfactual consistency: complete four-way family success is rare. An exploratory follow-up that elicits decomposed semantic evidence also fails to improve routing for the cleanly evaluated endpoint; the corresponding GPT-OSS condition was unavailable because of provider-side request validation. We evaluate policy classification only, not downstream responses, tool actions, or memory-store mutation.

---


### 44. [Co-RL: Unsupervised Reasoning Emerges from Diverse Cohort in Multi-agent RL](https://arxiv.org/abs/2608.17253)

**<font color=#1a73e8>作者：</font>** Yunhao Yang, Yuexin Bian, Yunjie Tian 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has emerged as a powerful approach for improving reasoning in language and vision-language models, yet its strongest successes still depend heavily on ground-truth supervision (e.g., verifiable reward). Such annotations are costly to obtain and become increasingly scarce as reasoning capabilities advance beyond what humans can reliably evaluate. Self-rewarding RL reduces this dependence by enabling models to derive reward signals from their own completions. However, training solely on self-generated feedback can reinforce existing biases and suboptimal behaviors, reduce response diversity, and ultimately lead to homogenized responses and training collapse. In this work, we show that unsupervised reasoning can emerge through cooperative multi-agent training. We introduce Co-RL, a framework in which multiple decoupled models, sharing no parameters, are simultaneously optimized through RL using rewards derived from their peers. We further show that increasing cohort diversity, through heterogeneous model families, sizes, and rephrased training samples, reduces the correlated errors that drive self-reinforcing feedback loops. This diversity consistently improves reasoning performance, maintains behavioral diversity, and mitigates training collapse. Across text-only and multimodal domains, Co-RL consistently outperforms the base models and prior label-free approaches, while matching or surpassing supervised methods, without access to any ground-truth labels. Concretely, Co-RL yields average gains of 3.0-8.6% across seven text-only benchmarks for LLMs and 2.3-7.2% across four multimodal benchmarks for VLMs. Code is available at this https URL.

---


### 45. [Understanding Curriculum Learning in Large Language Models via Cross-Difficulty Optimization Dynamics](https://arxiv.org/abs/2608.17268)

**<font color=#1a73e8>作者：</font>** Zhikai Ding, Ziyi Ye  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Curriculum learning has been widely adopted in the post-training of large language models by organizing training data from easy to hard. However, its effectiveness varies substantially across reasoning tasks, suggesting that no single curriculum is universally optimal and raising a fundamental question: what determines when curriculum learning works? In this paper, we answer this question by analyzing the optimization dynamics induced by different curriculum schedules. We show that the transfer relationship between different difficulty levels characterizes the optimization dynamics induced by curriculum learning, which in turn explains the effectiveness of different curriculum schedules, and formalize this relationship as Relative Transfer, a principled measure of cross-difficulty knowledge transfer. Based on this measurement, we derive Transfer-aware Dynamic Curriculum Sampling (TDCS), which dynamically adjusts the sampling distribution according to the estimated transfer relationship throughout training. Extensive experiments on multiple reasoning benchmarks demonstrate that TDCS consistently outperforms representative scheduling strategies across different tasks, model scales, and training paradigms. More importantly, our work provides a unified optimization-based explanation of curriculum learning through cross-difficulty transfer.

---


### 46. [Do LLMs Know a Good Hypothesis When They See One? Logit-Based Energy Scoring Outperforms Prompted LLM-as-Judge for Scientific Hypothesis Ranking](https://arxiv.org/abs/2608.17270)

**<font color=#1a73e8>作者：</font>** Swati Rajwal, Sanjay Das, Tirthankar Ghosal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for scientific hypothesis generation. However, evaluating generated hypotheses remains a challenge for trustworthy AI-enabled scientific workflows. Existing approaches often use LLMs as judges or rely on semantic similarity, which can favor familiar ideas over novel ones. We propose a logit-based energy scoring method that evaluates hypotheses using a language model's intrinsic confidence rather than comparative judgment. We benchmarked seven language models on 1,323 papers across 12 disciplines. Each paper was paired with its hypothesis and fifteen incorrect alternatives. Intrinsic scoring reached 33.0% Hit@1 pooled across both scorers, compared with 16.6% for prompted listwise ranking. The strongest configuration, a 1-billion-parameter model using logit-based energy scoring, reached 53.1%, though this was the maximum across 14 model-by-scorer combinations selected post hoc. Overall, intrinsic model confidence shows potential for scientific hypothesis evaluation. This study also motivates future research on confidence-based methods for trustworthy AI-enabled scientific discovery.

---


### 47. [Key-Frame Reasoning with SAM3: Third Place Solution for the MeViS-Text Track of the 8th LSVOS Challenge](https://arxiv.org/abs/2608.17279)

**<font color=#1a73e8>作者：</font>** Ce Bian, Xusheng He, Jinrong Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This report presents a two-stage, training-free solution for the MeViS-Text track of the 8th LSVOS Challenge. The task requires a model to localize and segment the object specified by a natural-language expression throughout a video. Such expressions often depend on temporal cues, including actions, interactions, directions, and relative positions. Our first stage uses Gemini-3.1 Pro via API to decompose a video-level event into instance-level targets, select a key frame for each target, and generate a discriminative description aligned with that frame. In the second stage, SAM3-agent produces a pixel-level seed mask on the selected frame, and the SAM3 video tracker propagates the mask bidirectionally through the video. Valid instances are grounded and propagated independently before their frame-wise masks are merged. All local SAM3 processing runs on a single NVIDIA GeForce RTX 4090 without task-specific training or model ensembling. Our method ranked third on the challenge test set, obtaining J&F, J, F, N-acc., T-acc., and Final scores of 0.761, 0.7367, 0.7852, 0.8333, 0.9755, and 0.856593, respectively.

---


### 48. [Abra: Scaling Diffusion Image Training](https://arxiv.org/abs/2608.17286)

**<font color=#1a73e8>作者：</font>** Kyle Chickering, Wei-An Lin, Swayam Bhanded 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Compute-optimal scaling laws guide the training of frontier language models yet remain largely unexplored for visual generation. We present a systematic scaling law study for text-to-image diffusion models using Abra, a controlled family of flow-matching transformers trained across three orders of magnitude worth of compute ($10^{19}$ to $10^{22}$ FLOPs), reaching significantly larger compute budgets than previous works. We demonstrate that diffusion models scale just as predictably as language models but require far more data to train optimally: compute optimality occurs at approximately $200$ image tokens per parameter, ten times the Chinchilla compute-optimal prescription for LLMs. We show that unlike language models, diffusion models are robust to overtraining and that practitioners should err on the side of more data rather than a larger model. Finally, we show that this predictability extends beyond training loss to generative quality metrics, optimal CFG settings, representation quality, and even the shape of the training curves, which collapse onto a universal form.

---


### 49. [Q-Interference: Memory-Efficient Phase-Aware Quantum-Inspired Attention](https://arxiv.org/abs/2608.17288)

**<font color=#1a73e8>作者：</font>** Emama Nahid, Tahmid Imtiaz Imu, Huayue Gu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> GPT attention measures token compatibility through dot-product similarity. This mechanism is simple, effective, and memory-efficient. But it does not explicitly model whether strong token features should reinforce or suppress one another. We introduce Q-Interference, a fully classical quantum-inspired attention mechanism for autoregressive language modeling that augments each query and key feature with an amplitude and a learned phase. The resulting attention score is phase-aware which aligned phases contribute constructively while conflicting phases contribute destructively. Although Q-Interference yields a richer interaction rule than similarity alone, a naive implementation of Q-Interference requires a large token-pair-feature interaction tensor, making it memory-intensive and often impractical. To address this limitation, we propose an exact trigonometric factorization that computes the same score using two standard matrix multiplications avoiding materialization of the large intermediate tensor. Q-Interference fits directly into a Transformer block in GPT and leaves the remainder of the model architecture and next-token prediction objective unchanged. Experiments on public benchmark datasets and baseline models show that the proposed reformulation trains stably in a controlled GPT-style setting and provides a consistent memory advantage over naive phase-aware interference attention. These results support the specific contribution of this work: an exact memory-efficient reformulation that makes phase-aware interference attention practical within a standard GPT pipeline.

---


### 50. [PlanPO: Group Planning-Aware Policy Optimization for Multi-Turn Agentic LLMs](https://arxiv.org/abs/2608.17289)

**<font color=#1a73e8>作者：</font>** Dayang Liang, Liyuan He, Xuan Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Group-relative policy optimization has emerged as a key paradigm for training agentic large language models (LLMs) on multi-turn interactive tasks. However, most existing variants fail to distinguish advantages among successful trajectories even when these trajectories differ substantially in their interaction efficiency. For instance, circuitous successes are often assigned the identical outcome reward, causing advantage collapse and severe performance bottlenecks. To this end, we propose Group Planning-aware Policy Optimization (PlanPO), a simple yet effective RL method for learning generalizable planning abilities beyond task-specific high-quality behavior patterns. Specifically, PlanPO introduces coarse-to-fine advantage signals, which capture the relative differences in trajectory-level lengths and turn-level response lengths conditioned on successful trajectories sampled for the same task. Within the group-relative optimization structure, this enables agents to actively learn generalizable and deliberate behaviors spanning interaction planning and textual generation from high-quality rollouts, without degenerating into vanilla length minimization. Experimentally, PlanPO improves over GRPO by 27.2\% on average across the challenging multi-turn benchmarks ALFWorld, WebShop, and SciWorld, outperforming recent powerful baselines while incurring negligible additional training cost.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-161](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
