# 🧠 大模型相关研究 | 2026年11月24日

> 本类共 **200** 篇论文：已确认 **182** 篇，待复核 **18** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md)

---

### 101. [Do Language Models Know Which Words Steer Their Reasoning?](https://arxiv.org/abs/2611.27317)

**<font color=#1a73e8>作者：</font>** Yanbei Jiang, Chao Lei, Jey Han Lau 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While chain-of-thought (CoT) prompting elicits intermediate reasoning steps from language models, it is unclear which words in the context actually steer the CoT. We identify Phantom Context Influence (PCI): language models are disproportionately steered by semantically irrelevant context words, even as the same models deny those words' relevance when asked. To localize PCI, we introduce Leave-One-Out Word JSD analysis, which removes one context word at a time from the otherwise intact context to isolate its marginal effect on the next-token distribution; words whose removal flips the prediction (pivot words) are passed to the same LLM to self-judge whether it recognizes this predictive dependence. Across four models and three benchmarks, language models largely do not know which words steer their reasoning, a mismatch we call the Generation-Judgment Contradiction. Inspired by this phenomenon, we propose Online KV Suppression: it scores every prompt word's influence over the whole chain of thought in a single pass, then zeroes the KV-cache entries of the highest-influence word the model itself judges inert and redecodes. This single-word intervention improves CoT accuracy across four models and five reasoning benchmarks, by up to 8.9 percentage points on math reasoning benchmark.

---


### 102. [SAVIOR: Sample-efficient Adaptation of Vision-Language Models for OCR Representation](https://arxiv.org/abs/2611.27319)

**<font color=#1a73e8>作者：</font>** Akshata A Bhat, Sharath Naganna, Saiful Haq 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical Character Recognition (OCR) pipelines and vision-language models exhibit high accuracy on standard OCR and document-understanding benchmarks, yet they systematically underperform on document patterns that are operationally critical in financial workflows. These patterns include vertical or rotated text, logo-embedded vendor names, fine-print regulatory clauses, degraded scans, and complex multi-column layouts. While underrepresented in public datasets, they constitute a substantial portion of real-world failure cases. We introduce SAVIOR, a sample-efficient data curation methodology that targets such high-impact failure scenarios to adapt vision-language models for robust financial OCR. We further propose PaIRS, a structure-aware evaluation metric that measures layout fidelity by comparing pairwise spatial relationships between tokens. Fine-tuning Qwen2.5-VL-Instruct with SAVIOR-Train achieves a word recall of 0.93. When the resulting layout-aware OCR output is used as context for document question answering, it attains an F1 score of 0.89, outperforming both open- and closed-source models such as GPT-4o, Mistral-OCR, PaddleOCR-VL, and DeepSeek-OCR.

---


### 103. [Reasoning in Fewer Tokens: Concept-Normalized Multilingual Scratchpads and Reversible Model-Adaptive Reasoning Codes](https://arxiv.org/abs/2611.27326)

**<font color=#1a73e8>作者：</font>** Rabimba Karanjai, Suryabhan Singh Hada, Hemanth Hegadehalli Madhavarao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought prompting significantly improves the reasoning capabilities of large language models (LLMs) but incurs high inference costs due to lengthy autoregressive decoding. While previous efficiency approaches reduce costs by discarding tokens or utilizing continuous latent representations, these lossy methods fundamentally sacrifice interpretability and auditability. In this work, we introduce a novel compression framework for intermediate reasoning. We apply Byte-Pair Encoding (BPE) to reasoning corpora to learn a compressed vocabulary of Private Use Area (PUA) tokens, each representing frequent semantic spans. After expanding the LLM's vocabulary, we fine-tune the model via strictly 1:1, our method is lossless. We evaluate our approach on Llama-3.1-8B, Qwen2.5-14B, and Qwen2.5-32B across four diverse benchmarks. Our method reduces total generated tokens by 14.7% on average with reasoning trace lengths dropping by up to 27.1%, while incurring a negligible average accuracy cost of 1.6 percentage points. Crucially, this approach is orthogonal to existing lossy methods, allowing practitioners to stack lossless and irreversible compression techniques. We demonstrate that a compressed intermediate language provides a highly efficient computational resource that accelerates inference while fully preserving the transparency of LLM reasoning.

---


### 104. [Zing-1.0: A Playable World System Built on Controllable Rendering](https://arxiv.org/abs/2611.27336)

**<font color=#1a73e8>作者：</font>** Wenbo Zhang, Guoli Zhang, Xuewen Yu 等 30 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Zing-1.0, a Playable World System built on Controllable Rendering. An executable engine resolves player actions under the world's rules and produces proxy video from the updated state. A streaming video model synthesizes the player's view from this proxy, and the runtime delivers it to inform subsequent actions. (1) Principle and system. We formulate Controllable Rendering and define the interfaces among world construction, world execution, observation synthesis, and the interaction runtime. To our knowledge, this is the first implementation-independent specification of a Playable World System. (2) AI-native engine. WorldKit provides structured authoring tools and reusable character, camera, and control components for coding agents to construct executable proxy worlds. It supports extensible interactions and precise geometric motion control while separating executable behavior from final visual appearance. (3) Streaming renderer. We adapt MiniMax-H3 for block-causal autoregressive generation and incremental decoding. Proxy video constrains structure and motion, while text and separate scene and subject references specify appearance. We train the generator on diverse tasks and distill it to generate each block in a few denoising steps. The renderer leads the compared streaming editors on OpenVE (3.90) and LongV2VBench (3.44). On StreamEval, Zing-1.0 scores 57.86 on instruction editing and 54.06 on reference editing, exceeding the published baselines on both tracks. (4) Interaction infrastructure. We build an Interaction Runtime that routes player actions to WorldKit while supporting in-play prompt and reference updates. Cross-block joint execution and sparse attention with compressed K/V reduce inference overhead. With the DiT on a single H200 and encoding and decoding on one H100 each, the serving system achieves a steady-state throughput of 23.82 FPS at $832\times480$.

---


### 105. [Unimodal Shortcuts and Joint Scene-Intent Dependence in Vision-Language Safety Representations](https://arxiv.org/abs/2611.27339)

**<font color=#1a73e8>作者：</font>** Guijia Zhang, Hongbo Qiu, Guohao Cai 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The safety of a request to a vision-language model often depends on the image: asking how to serve a dish is harmless for fresh food and harmful for spoiled food. High accuracy on situational safety benchmarks does not tell us whether a model's safety representation encodes both the scene and the user's intent, because a benchmark can often be solved from one modality alone. Studying frozen vision-language safety representations, we audit five public situational benchmarks and find that each admits a unimodal shortcut: images alone predict the labels, and on same-image prompt pairs a probe that never sees the photograph reaches 0.9645 AUROC. We therefore build a controlled evaluation that crosses safe and hazardous scenes with observation and action requests, so that no single-modality rule can exceed 0.500 group-ranking accuracy. On this control, linear probes on intermediate states of Qwen3-VL-8B and SmolVLM2-2.2B reach 0.958 and 0.930, showing that the scene-intent conjunction is linearly decodable; concatenating separately encoded image and text states already recovers most of this signal, so decodability is not evidence of a fusion mechanism. The same probes screen cheaply but generalize poorly to unseen images and other benchmarks. Reliable multimodal safety evaluation therefore needs controls that rule out unimodal shortcuts before accuracy is read as evidence of joint understanding.

---


### 106. [Breaking the Long Horizon: Short-Horizon Process Supervision for Long-Form Generation in LLMs](https://arxiv.org/abs/2611.27348)

**<font color=#1a73e8>作者：</font>** Heyang Xu, HanWen Hao, Qianren Mao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-form generation is increasingly important for agentic LLM systems, yet current reinforcement learning methods typically optimize an entire document with a single outcome-level reward. This delayed and coarse-grained supervision makes it difficult to localize errors and assign credit across semantically distinct parts of the output. To address this, we propose a short-horizon framework that reformulates long-form generation through semantic decomposition into segment-level decisions. Each segment is generated with prefix-conditioned context, allowing cross-segment coherence to be preserved while keeping supervision local. The generated segments are then scored with rubric-based rewards for adherence, coherence, and relevance, enabling explicit local supervision at the segment level. These local rewards are used to compute step-wise advantages, yielding localized policy updates. To isolate the effect of supervision granularity, we instantiate both outcome-level supervision and our short-horizon process reward method (SH-PRM) under the same GRPO framework. Across multiple LLMs and two long-form generation benchmarks, SH-PRM consistently outperforms outcome-level supervision and strong inference-time baselines under the same optimizer and comparable budgets. Further analyses suggest that these gains primarily arise from improved credit assignment. Overall, our results suggest that aligning supervision granularity with the semantic structure of long-form generation is an effective design principle for long-form LLM training.

---


### 107. [EcomWriteBench: A Real-World Benchmark for E-commerce Writing Tasks](https://arxiv.org/abs/2611.27349)

**<font color=#1a73e8>作者：</font>** Kaicheng Liang, Jingyi Cui, Hongwei Wen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used throughout e-commerce workflows to generate content that informs purchasing decisions and supports customer interactions. Evaluating these systems requires accounting for user needs, product evidence, structural constraints, and business requirements that are not fully captured by general-purpose writing benchmarks. We introduce EcomWriteBench, a real-world benchmark containing 3,861 queries from 69 e-commerce writing tasks across 13 categories and five languages. Through task-level extraction, cross-task consolidation, and refinement guided by human feedback, EcomWriteBench constructs a shared pool of 37 abilities and identifies the subset applicable to each task. Ability-wise scoring enables us to compare state-of-the-art LLMs on EcomWriteBench and characterize their relative strengths and weaknesses across fine-grained e-commerce writing abilities. We further propose a preference-calibrated weight-learning framework that converts human pairwise preferences into interpretable scoring rubrics through global, category-level, and task-level aggregation weights. This framework provides a reusable approach for translating human preferences into automated evaluation by combining ability discovery, ability-wise scoring, and preference-calibrated aggregation, and can potentially be applied to a broad range of benchmarks beyond EcomWriteBench. On held-out queries, our scoring framework achieves 88.96% agreement with human preferences, compared with 78.54% for conventional LLM-as-a-judge scoring.

---


### 108. [GRACE: Controlled Evidence Interventions for Diagnosing and Improving Knowledge Integration in GraphRAG](https://arxiv.org/abs/2611.27350)

**<font color=#1a73e8>作者：</font>** Minh Pham, Quang Nguyen, Phong Kieu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> GraphRAG combines a language model's parametric knowledge with retrieved graph evidence, yet aggregate accuracy cannot show whether failures stem from missing paths, distractors, or conflicts with model knowledge. We introduce GRACE, a benchmark built by executing LC-QuAD 2.0 queries over Wikidata and applying four controlled interventions to each evidence subgraph: severing a support path, adding type-compatible distractors, attaching high-degree hubs, and replacing the supported answer with a counterfactual entity. Questions and option positions remain fixed across the five states. The validated benchmark contains 4,028 questions and 20,140 question-graph pairs. These comparisons reveal that question-only routing cannot distinguish evidence states, while relevance guidance can improve answerable states yet hurt when the support path is severed: relevant facts may not jointly suffice to answer. We propose QCFSE-SA, which combines typed local attention, global graph attention, and question-conditioned evidence guidance with a calibrated graph-support gate. With the factual context and generator held fixed, it improves controlled-state accuracy from 57.17% to 62.78% (+5.61 points; question-clustered 95% CI [+5.04, +6.17]) and broken-state accuracy from 55.41% to 67.85%. Over-abstention on semantic distractors remains an open challenge.

---


### 109. [PAVE: A Harness for Geometrically Consistent Road Network Modeling with Vision-Language Models](https://arxiv.org/abs/2611.27352)

**<font color=#1a73e8>作者：</font>** Yajun Liu, Jinxi Wu, Juan Pablo Millán Raya 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transportation models, whether they simulate traffic or support planning, are only as reliable as the road networks they run on, down to the lanes and turns at each intersection. Practitioners still take such a network from GIS files and supply its junction and movement data by hand, a task that recurs with each new base year and design alternative, or they generate it from open map data. OpenStreetMap's lane tags give the correct layout for only 13 of the 44 approaches we test; open map data are often incomplete or inaccurate. Satellite and street-level imagery, in contrast, cover all 44 and show their lanes as painted. Vision-language models (VLMs) can read such imagery, but asked directly they lose geometric consistency when the same lane must be matched across a satellite crop, street-level photos taken from different poses and an ID-labelled network. We therefore present PAVE (Perceive, Anchor, Verify, Edit), a harness in which code measures what can be measured, traffic engineering knowledge enters as general rules and checks, and the model makes only the open judgements, each anchored to network IDs so that checks catch answers that contradict a measurement, a second reading or a traffic rule. Scored against human labels at signalised intersections, PAVE raises the share of exactly correct lane layouts from 49-64% with a single request to 86-91% for two VLMs, with most of the gain coming from reading one approach at a time on traced lanes. The same division of work edits a real network to a planning brief: the model names the links and nodes of each part of a facility, and code builds the edit from a design template. Of 18 edits, 16 pass every network check, against none when the model writes its own code, and 2 contain a design or coding error, against 7. An analysis shows where VLMs lose geometric consistency and which check catches each failure.

---


### 110. [WaXup: Weight Averaging of Experts as Data Augmentation for Robust Introspection](https://arxiv.org/abs/2611.27353)

**<font color=#1a73e8>作者：</font>** Marc Boëlle, Lucas Dixon, Alexandre Ramé  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As the capabilities of large language models keep improving, traditional mechanistic interpretability methods struggle to keep pace. In contrast, trainable introspection methods emerge as a promising alternative; they repurpose the model itself as a self-diagnostic tool, trained to verbalize what it has learned during finetuning in natural language. While training on datasets of finetuned experts achieves encouraging results, it currently lacks robustness and generalization. Building on the data augmentation framework of MiXup, we introduce WaXup, a method that augments the introspection training set through linear interpolation in the weight space. This is motivated by the linear mode connectivity property: weight averaged experts interpolate the behaviors of the initial experts. We evaluate WaXup on three benchmarks: hidden-behavior models, a meta-dataset of real-world NLP tasks and AuditBench, a challenging alignment auditing suite of models adversarially trained to conceal their behaviors. WaXup improves the accuracy of generated descriptions as well as robustness to various distribution shifts. We hope to improve the reliability of trainable introspection methods towards better and safer models.

---


### 111. [WePM: Hierarchical Conflict Reconciliation for Unified MLLMs](https://arxiv.org/abs/2611.27365)

**<font color=#1a73e8>作者：</font>** Zhiqiang Yuan, Qiwei Yan, Liwei Yang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Bringing multimodal intelligence from the cloud to users' devices keeps sensitive data local and reduces inference cost, but deploying a specialized model per capability duplicates vision-language capacity under tight memory and compute budgets. We formalize heterogeneous capability density (HCD), measuring how broadly and effectively a model serves heterogeneous task families per unit of resident inference memory. High HCD across representation, generation, and decision raises two challenges: these capabilities need visual evidence at different spatial granularities under a fixed token budget, and separately collected task corpora yield conflicting updates to shared parameters, while cross-task paired supervision is costly and ambiguous for open-ended inputs. We present WePM, a family of pocket models unifying representation, generation, and decision within one vision-language backbone. Multi-Granularity Visual Budgeting (MGVB) allocates a fixed visual-token budget across global, regional, and fine-grained banks; Unified Listwise Knowledge Distillation (ULKD) enriches separately collected data with soft teacher guidance, avoiding cross-task paired annotation; Stable and Efficient Multitask Optimization (SEMO) regulates each task's contribution through explicit loss weights and exposure schedules, with sequential gradient accumulation under memory constraints. In the joint representation-generation setting, WePM outperforms all baselines across five evaluation groups, raising the Joint score from 38.15 to 52.74. In single-task evaluation, WePM-4B attains the best average score over 30 embedding, 39 generation, and seven typed-decision benchmarks (72.86, 62.41, 61.11). Against the separate-model stack with the highest HCD, WePM achieves slightly higher balanced performance with 61.9% less resident weight memory, a 2.64-fold higher HCD.

---


### 112. [AMARIS: Merging Generalist and Specialist LLMs via Adaptive Subspace Inheritance](https://arxiv.org/abs/2611.27369)

**<font color=#1a73e8>作者：</font>** Hwee Young Kang, Irwin De Tao Chin, Wen-Haw Chong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Domain specialization of large language models (LLMs) often improves target-domain performance but degrades broad capabilities. Model merging is an attractive training-free alternative, yet common parameter-space strategies (for example, interpolation and sparsified averaging) provide limited control over task-specific interference. We introduce Adaptive Model Alignment via Ranked Inherited Subspaces (AMARIS), a covariance-driven framework that transfers specialist updates only along selected activation directions. AMARIS formulates merging as budgeted subspace inheritance: it seeks high specialist activation capture under a regularized base-output perturbation budget, then builds a low-rank projection gate from ranked generalized eigendirections. This yields a single static merged checkpoint that concentrates transfer in high-utility, low-interference directions. We evaluate AMARIS on Qwen3-based merges (8B and 32B) across finance, instruction-following, and multilingual SEA specialization. In our evaluated settings, AMARIS reaches Pareto operating points that are competitive with strong training-free baselines, including 98.37% specialist retention with 95.16% core retention for the 8B finance setting, 103.55% core retention with 90.28% specialist retention for the 8B instruction-following setting, and 99.20% core retention with 94.80% specialist retention for the 32B SEA setting. These results support subspace-constrained merging as a practical route to compositional capability integration without additional training.

---


### 113. [HR-Merge: Model Merging with Headroom-Weighted Residual Refinement](https://arxiv.org/abs/2611.27377)

**<font color=#1a73e8>作者：</font>** Jiakang Huang, Xueyan Zhang, Renyi Cai 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model merging combines experts fine-tuned from a shared backbone, such as LoRA adapters of a large language model, into one multi-task model without further training. Existing methods apply one rule to every task, yet the accuracy they lose is uneven across tasks. We show that the lost accuracy remains recoverable from each task's residual, its task vector minus the merged update, and that a task's validation headroom, the share of its expert validation accuracy the merge loses, indicates where recovery pays off. Residuals from different tasks interfere, so they must be merged rather than summed. We propose HR-Merge, a training-free wrapper around any merging method. It weights each residual by its task's headroom, re-merges the weighted residuals with the base operator, and adds the result back at a strength selected on validation, falling back to the base merge when no strength helps. On six NLI adapters of LLaMA-3 8B, HR-Merge lifts TIES from 93.29 to 94.29 normalized accuracy, above all tested bases, mainly by recovering its weakest task. In vision, on three CLIP backbones, up to 20 tasks, and LoRA merging, it generally improves or preserves base accuracy and yields the best model in every setting.

---


### 114. [Beyond What They Say: Cue Acknowledgment and Robustness in Vision-Language Models](https://arxiv.org/abs/2611.27389)

**<font color=#1a73e8>作者：</font>** Ali Rahimiakbr, Arvin Baghal Asl, Nima Niroumand 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Explanations are used to assess whether vision-language models rely on visual evidence or misleading suggestions. A response that explicitly names a cue can still follow it, making disclosure alone an incomplete basis for judging robustness. We ask whether greater cue acknowledgment accompanies greater resistance. We compare matched answers and explanations under helpful, misleading, and conflicting visual and textual cues while holding the underlying question and correct answer fixed. A paired comparison shows that a model can select the endorsed wrong answer more often while acknowledging the cues more often. Reduced silence therefore need not indicate improved resistance. Explanations may also mention a textual suggestion while omitting an accompanying visual cue. Requesting evidence and acknowledgment does not consistently improve resistance in the tested settings. Outcomes vary across models and settings, and these comparisons do not isolate a causal effect of acknowledgment. Evaluations should report cue following and acknowledgment on the same instances, distinguishing visual from textual cues.

---


### 115. [Taking Apart and Putting Together: Tracking Objects Through Physical Transformations](https://arxiv.org/abs/2611.27398)

**<font color=#1a73e8>作者：</font>** Davide Gardenal, Mingxuan Liu, Flavio Vella 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Transformation Tracking and Understanding (TTU), extending video object tracking to environments where objects undergo physical assemblies and disassemblies. TTU requires continuously tracking objects through transformations, identifying new entities, maintaining a state graph of their relationships, and assigning semantic labels to transformations. While foundation models (e.g., SAM 2/3) maintain tracklets through appearance changes, they cannot update semantic identities as objects physically evolve. Prior work addresses only disassemblies, relying on expensive searches triggered only when tracking fails. We propose Tracking Instances via Proposals and Overlaps (TIPO), a training-free framework that continuously infers transformations via a generate-evaluate-judge pipeline. TIPO generates split and merge proposals from disjoint mask components, scores them against mask-decoder priors using inner and external overlap, and queries an MLLM on the top proposal for visual verification and semantic labeling. To benchmark TTU, we curate Video Instances, States, and Transformation Annotations (VISTA), a dataset including state graphs with 124 assembly and 132 disassembly events across 50 sequences and over 26,000 frames. TIPO achieves state-of-the-art tracking and state-graph accuracy on VISTA, while operating $6\times$ to $15\times$ faster than prior methods. Project page: this https URL

---


### 116. [Degradation of Language Models under Controlled Load: Synchronization, Rule Execution and Misfires on the Background](https://arxiv.org/abs/2611.27404)

**<font color=#1a73e8>作者：</font>** Hennadii Kutomanov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As the load grows, a language model makes more and more errors, but different processes stand behind this decline in quality. The model may lose the correspondence with the source text, it may keep its place in the text but execute a rule wrongly, or it may change a word that no rule concerns. In this work the degradation of a model under controlled load is separated into these three components: synchronization, rule execution and misfires. The load is set by rules that replace one word with another in a meaningless text, and each kind of load (the text length, the position of a word in the answer, the replacement density, the number of rules and the place of a rule in the list) is set separately. The alignment of the answer with the reference makes it possible to follow the outcome of every word, and a statistical model that takes into account that the spread of difficulty between requests itself depends on the load restores, for each component, the laws of its dependence on every kind of load. These laws make up the passport of a model. The paper presents the method of the separation, the principles of constructing the laws and the passports of seven models built by this method; the separation opens the way to studying the fine structure of the behavior of a neural network.

---


### 117. [ORBIT: Offset-based Activation Steering for Cross-lingual Multimodal Fact Verification](https://arxiv.org/abs/2611.27421)

**<font color=#1a73e8>作者：</font>** Huy Trieu, Duy-Minh Nguyen-Tran, Thanh-Dat Nguyen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal fact verification faces a fundamental accessibility bottleneck: while large proprietary models exhibit cross-lingual robustness, small vision-language models suffer a severe, disproportionate accuracy collapse on low-resource languages. Closing this gap traditionally requires prohibitive scale or extensive language-specific fine-tuning. In this work, we propose Offset Recovery via Bilingual Inference-time Technique (ORBIT), an algorithmic intervention that mitigates this collapse at inference time. ORBIT estimates span-specific offset vectors from parallel claim-evidence instances and applies them to claim and evidence representations, targeting the cross-lingual degradation induced by low-resource evidence. Experiments across 81 configurations reveal that ORBIT substantially recovers both accuracy and F1-score in low-resource settings, exposes calibration offset norms as a diagnostic proxy, and outperforms translation-based and steering baselines.

---


### 118. [Jagged Robustness: Uneven Safety Transfer and Emerging Vulnerabilities under LLM Quantization](https://arxiv.org/abs/2611.27424)

**<font color=#1a73e8>作者：</font>** Ramneek Agnihotri, Yingte Xu, Hans Vath  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Quantization enables efficient inference in language models through model parameter compression. This work audits the impact of quantization on capability and safety domains including model safeguards, instruction-following, ethics and bias. Through benchmarks, we find that model safeguards and bias can degrade under quantization, while other capabilities such as truthfulness remain more stable in Qwen3-4B. We define this uneven transfer of LLM capabilities under quantization as Jagged Robustness. We find multiple factors driving Jagged Robustness: task complexity, evaluation method and generation coherence. Moreover, we verify the degradation of model safeguards by observing increased compliance with unsafe requests under quantization, and demonstrate universal adversarial suffix attacks that are benign for the full model but jailbreak quantized models. The findings indicate that it is risky to assume that the performance and robustness can transfer evenly across different capability domains from full models to quantized models.

---


### 119. [No Audio, No Transcripts, No Problem: LLM-based ASR Adaptation Using Only Domain Documents](https://arxiv.org/abs/2611.27434)

**<font color=#1a73e8>作者：</font>** Sergio Burdisso, Dairazalia Sánchez-Cortés, Esaú Villatoro-Tello 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Can a speech recognizer be adapted to a new domain with no target audio and no transcripts, using only written documentation? This is the realistic onboarding setting: a new customer hands over raw documentation, not the transcripts that text-only adaptation normally assumes. We turn a domain's documents into adaptation text in two ways, directly as written sentences or rendered by a large language model (LLM) into synthetic spoken dialogs, and feed them to a recently proposed denoising-based text-only adaptation method. We show that, across in-domain, out-of-domain, and cross-domain settings on two corpora, document-only adaptation can match or closely approach real transcriptions; whether written or conversational rendering is best depends on speaking style and the amount of text generated. To our knowledge, this is the first study of document-only adaptation of LLM-based ASR. As no existing corpus pairs audio, transcripts, and documents, we also built and released a document-grounded benchmark.

---


### 120. [THRIFTY: Cost-Constrained Reasoning-Data Synthesis for Small Language Models](https://arxiv.org/abs/2611.27436)

**<font color=#1a73e8>作者：</font>** Aasheesh Singh, Vishal Vaddina  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Small language models (SLMs) are increasingly attractive for efficient, specialized deployment, and are typically trained on reasoning trajectories distilled from a larger teacher LLM. Generating this synthetic data is a major cost of the pipeline, especially when the teacher is a frontier model. Existing collection methods, however, are largely cost-unaware, or at best spread a fixed sampling budget uniformly across queries. Such allocation ignores the wide variation in problem difficulty and the strategic over- or under-sampling it invites. Thus, we propose THRIFTY, a Thompson-sampling bandit controller that spends a fixed generation-token budget to collect diverse correct reasoning trajectories, casting the task as a bandits-with-knapsacks problem with a novel diversity-aware objective. It tracks each problem's success probability with an online Beta posterior and spends each token where it expects the most new distinct correct solutions. Because repeated solutions add progressively less value, THRIFTY adaptively stops resampling saturated problems, concentrates budget on under-covered ones, and retires the unsolvable at the budget's opportunity cost. On math (AIME, MATH-500) and code (LiveCodeBench) benchmarks, THRIFTY gathers up to 22% more diverse correct trajectories per generation token than both the standard uniform-sampling recipe and the strongest adaptive baseline, with the largest gains in the scarce-budget and hard-problem regimes.

---


### 121. [Learning When to Ask: Advisor-Aware Post-Training for SLM Agents](https://arxiv.org/abs/2611.27443)

**<font color=#1a73e8>作者：</font>** Aasheesh Singh, Vishal Vaddina  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Small language models (SLMs) are increasingly attractive for cheap, high-throughput agentic deployment, but they remain weak at multi-step reasoning and tool use that long-horizon tasks demand. We study how to post-train an SLM to seek advice from a stronger model and act on that advice itself, following an advisor-executor pattern. Out of the box, this pattern fails across open- and closed-source small-model families: wiring an SLM to an advisor is a harness-design matter that is not enough on its own. A post-training recipe is needed to teach the model when to ask, in a cost-aware fashion, and how to follow advice across steps. Our method, ADAPT (ADvisor-Aware Post-Training), is a multi-stage recipe that instills this behavior, learning entirely from the policy's own rollouts supervised by the environment's outcome, with no learned reward model or human annotation. Across three domains, compared to an untrained harness baseline, ADAPT improves success rate in embodied text reasoning (TextWorld) from 24.5% to 77.3%, code generation (LiveCodeBench) from 21.8% to 56.0%, and deep web search (GAIA) from 17.5% to 49.3%, while querying the advisor sparingly (~1.0-2.1 calls per task). On the two long-horizon domains it closes 70-85% of the gap to an oracle that perfectly times when to ask for advice, and on code generation it exceeds that oracle. The gains persist when the advisor is replaced by one unseen in training, showing that the learned help-seeking policy is robust to a changing advisor rather than tied to the one it was trained with.

---


### 122. [Silent Arbitration: How Large Language Models Resolve Co-Authoritative Conflicting Instructions](https://arxiv.org/abs/2611.27444)

**<font color=#1a73e8>作者：</font>** Sihyeon Lee, Jiwoo Kum, Jihun Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly receive high-level instructions about roles, values, interests, and communication style. Such instructions can conflict even when a prompt assigns them equal authority and provides no priority rule. We study co-authoritative persona conflict, in which a single prompt jointly assigns two opposing personas. Across eight conflict types grounded in published source material and five LLMs, we measure conflict acknowledgment, resolution strategy, and directional stance. Models acknowledge incompatibility in 72% of direct checks but explicitly surface it in only 22% of task responses, revealing silent arbitration. Dominance accounts for 45% of dual-persona responses, and 35% of compromise-labeled responses retain directional lean. Prompt framing further changes the visible form of arbitration substantially more than ordinary paraphrase variation. These findings show that evaluating instruction following should assess whether models disclose conflicts, how they resolve them, and which persona their responses favor.

---


### 123. [Structurally Different, Functionally Persistent: Capability Regions Under Model Optimization](https://arxiv.org/abs/2611.27445)

**<font color=#1a73e8>作者：</font>** Jiwoo Kum, Chanwoo Kim, Doyun Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) capabilities have been associated with localized parameter regions, enabling targeted model editing and intervention. However, it remains unclear whether a region identified before model optimization remains an effective intervention target afterward. We evaluate the functional persistence and parameter overlap of coding capability regions across three instruction-tuned models under quantization, pruning, and LoRA-based adaptation. Although re-extracted regions exhibit substantial parameter reorganization, ablating the original region after optimization eliminates or nearly eliminates coding performance in almost all conditions, while magnitude-matched controls preserve performance. Partition analysis further shows that the shared subset of the original and re-extracted regions accounts for most of the observed ablation effect in the majority of conditions. These results demonstrate that parameter overlap and functional persistence are distinct: capability regions can remain causally effective intervention targets even when their parameter realization changes substantially.

---


### 124. [AppCon-Bench: Perception and Misperception of Material Appearance in Vision-Language Models](https://arxiv.org/abs/2611.27453)

**<font color=#1a73e8>作者：</font>** Santiago Jimenez-Navarro, Ana Serrano, Belen Masia  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Identifying the same material across changes in illumination or geometry is a critical ability for robust vision systems. Humans exhibit remarkable material appearance constancy, being able to recognize the intrinsic physical properties of an object's surface material across variations in extrinsic, confounding factors such as the lighting or the shape of such object. Vision-Language Models (VLMs) demonstrate strong performance across a wide range of semantic vision tasks, yet their ability to interpret subtle mid-level perceptual attributes remains less understood. We introduce AppCon-Bench, a benchmark comprising five tasks designed to assess material appearance constancy under controlled variations in geometry and illumination, and evaluate representative VLMs alongside human observers, investigating their ability to maintain consistent material judgments across viewing conditions and experimental contexts. After thorough analysis, we identify several key findings that reveal both similarities and systematic differences between human and VLM material appearance perception, highlighting the value of evaluating perceptual successes and failures beyond overall accuracy and informing areas of improvement for current VLMs.

---


### 125. [PathOPEN: A pathologist-curated histopathology dataset for visual question answering](https://arxiv.org/abs/2611.27469)

**<font color=#1a73e8>作者：</font>** Awais Naeem, Zhongling Xu, George Huang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> PathOPEN is a histopathology dataset for visual question answering. Two clinical pathologists selected 157 cases with 229 available original images and wrote open-ended, five-option multiple-choice and close-ended (yes/no) questions. They supplied both a correct and a wrong answer for 201 of the 309 open-ended questions. Each case records the organ, pathology category and regional anatomy, and each image records its magnification. The dataset includes 6,870 augmented images and four manifests that select subsets to improve balance by individual metadata field. Five additional pathologists and two vision-language model judges rated items with scoring rubrics, and six models answered questions zero-shot across the three formats. The metadata support subgroup evaluation, and the paired answers can be used to construct preference examples.

---


### 126. [From Manufacturing Event Logs to Simulation: Enabling SMEs with Agentic AI for SimPy Simulation Generation](https://arxiv.org/abs/2611.27483)

**<font color=#1a73e8>作者：</font>** Richard Reider, Lina Döring, Sebastian Lang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> High expertise and cost barriers exclude small and medium-sized enterprises from discrete-event simulation (DES). We introduce GenAI4SimPy, a multi-agent framework powered by Qwen 3.6 (27B), an open-weight large language model, that automates end-to-end DES generation from manufacturing event logs to executable SimPy models through tool-augmented reasoning and human-in-the-loop validation. Evaluated on three execution blocks from a public smart factory dataset, the framework achieved a mean absolute percentage error of 7.9\% and coverage of failure rate for all three blocks and of throughput for two of three. A fidelity paradox was observed: accurate process-level parameters did not ensure system-level behavioral fidelity, with flow-time and throughput errors driven by misinterpreted observation-window truncation and absent system-level calibration. These results demonstrate that local open-weight models can perform DES generation at accuracy comparable to cloud-based alternatives, while identifying parameter extraction as necessary but insufficient for behavioral validity. Source code and results are available at this https URL

---


### 127. [Efficient Natural Language to Temporal Logic Translation for Real-Time Physical AI](https://arxiv.org/abs/2611.27489)

**<font color=#1a73e8>作者：</font>** Oliver Schön, Adrien Banse, John Lygeros 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Robots can be controlled to perform tasks with guaranteed correctness when the task instructions are stated in a formal language. Large language models (LLMs) have been widely used to allow users to provide such instructions in natural language (NL), by translating NL into formal language. When deploying such translators on a robot, however, we face limited computing and energy resources, while offloading computation or data to the cloud may be infeasible or undesirable. Yet an LLM is a general-purpose text generator, whereas a formula in a fixed formal language fragment follows a well-defined syntax. We therefore ask whether text generation is needed at all. For the formal language of linear temporal logic (LTL), we show that this translation can instead be broken down into answering a set of questions with pre-defined answers. We then construct a System-One model, a recent class of NL-based classifier, to provide such answers and enable us to translate a natural language instruction into an LTL instruction. On three benchmarks, our translator matches or exceeds the accuracy of the best local LLMs available, at up to one order of magnitude lower runtime and energy consumption. We show that it generalizes to unseen atomic propositions and temporal patterns.

---


### 128. [Alignment without Transfer: Tokenization Impacts Cross-lingual Representations during Multilingual Language Model Pretraining](https://arxiv.org/abs/2611.27491)

**<font color=#1a73e8>作者：</font>** Jonathan von Rad, Pontus Stenetorp, Yao Lu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tokenization represents one of the most crucial steps in mulilingual NLP pipelines. Yet, tokenizers routinely under-allocate vocabulary to low-resource languages. While improved allocation leads to better performance, it remains poorly understood how tokenization shapes cross-lingual representations and transfer during pretraining. To address this, we pretrain 39 mono- and bilingual 1B decoder-only models on FineWeb2-HQ across English, German, French, Arabic and Chinese, varying only the tokenizer. Our results demonstrate that improved vocabulary allocation (i) substantially raises cross-lingual representation alignment in early-to-mid layers, an effect that prior work measuring only the output layer could not observe, (ii) increases cross-lingual parametric knowledge sharing in feed-forward neurons, supported by correlational and causal evidence, and (iii) an alignment-transfer dissociation, where cross-lingual transfer remains essentially unchanged despite higher alignment. Moreover, transfer is significantly lower for cross-script bilinguals even under fair vocabulary allocation, indicating that the script barrier is not merely a tokenizer artifact. All of our checkpoints and code are publicly available.

---


### 129. [Trained on Harm, Still Refusing: A Training-Time Defense for Code Generation](https://arxiv.org/abs/2611.27495)

**<font color=#1a73e8>作者：</font>** Miaoqing Tian, Ruohan Li, Qian Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fine-tuning enables safety-aligned code language models to adapt to diverse downstream tasks. However, training on untrusted data can severely undermine their ability to refuse harmful requests. Notably, we find that models comply with harmful requests even though harmfulness information remains highly decodable from their internal representations. Moreover, an initial preference for refusal does not necessarily translate into sustained refusal behavior throughout generation. Together, these findings reveal a critical gap between recognizing harmful requests and consistently refusing to fulfill them. To address this gap, we introduce SAFEHOLD, a novel provider-enforced defense framework that preserves safety alignment during harmful fine-tuning by treating refusal as a sustained generation process rather than a single response decision. Specifically, SAFEHOLD preserves the aligned model's full-vocabulary response distribution at the initial generation position through decision-boundary anchoring, while supervising the complete refusal sequence through refusal-path reinforcement. We conduct extensive experiments evaluating safety, utility, and internal mechanisms. SAFEHOLD reduces average ASR by 72.03 percentage points relative to undefended fine-tuning, outperforming five SOTA defenses by 24.32 to 70.87 percentage points. Meanwhile, it improves average HumanEval pass@1 by 10.24 percentage points over undefended fine-tuning, while maintaining an average XSTest over-refusal rate of only 2.73 percent. Overall, these results demonstrate that SAFEHOLD effectively mitigates safety degradation during harmful fine-tuning while preserving benign-task utility.

---


### 130. [The Assistant Persona Differs Across Languages in Activation Space](https://arxiv.org/abs/2611.27504)

**<font color=#1a73e8>作者：</font>** Daniel Yoo, Naama Rozen, Evan Harris  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models behave differently across languages, and are noticeably less safe in lower-resource languages. This gap is well established behaviorally, but not mechanistically. Directions in activation space, including the assistant persona direction, are almost always extracted from English and assumed to generalize across languages. We extract the assistant persona direction in 31 languages in Qwen3-32B, and find that the resulting axes differ substantially: their cosine similarity to the English axis ranges from 0.378 to 0.911. Moreover, each language's assistant persona direction and its magnitude are correlated with the language's resource level. We also find that the model's default assistant state is farther from the helpful assistant pole in lower-resource languages. Finally, steering against a language's own axis amplifies persona-based jailbreak more than steering against the English axis. These results indicate that the model does not carry a single assistant representation across languages. More broadly, the assistant persona may need to be an explicit target of multilingual alignment.

---


### 131. [How Many Bytes Has a BPE Model Seen? Estimating Byte-Token Exposure in Pretraining from Corpus Statistics and Embedding Norms](https://arxiv.org/abs/2611.27506)

**<font color=#1a73e8>作者：</font>** Liwei Zhang, ZhiMing Tong, Mochen Guan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Byte-level BPE vocabularies retain 256 single-byte fallback tokens. When converting such a model into a pure byte-level model, these tokens provide the starting embeddings. How much training have they received? We estimate byte-token exposure in Qwen3.8 using two independent routes. First, we tokenize 540 MB of public corpora covering 40 domains and 33 languages, then combine per-domain token shares with assumed pretraining mixtures. Single-byte tokens account for 13 to 36% of tokens, mostly ASCII; genuine UTF-8 fallback bytes (0x80-0xFF) account for 0.15 to 0.27% under mainstream mixtures, or about 2 billion occurrences per trillion pretraining tokens. Fallback rates vary by four orders of magnitude across languages, reflecting how well each script is covered by the vocabulary. Second, we analyze embedding and output-matrix row norms for four open models, using untrained padding rows as a zero-exposure baseline and ordinary tokens with known frequencies for calibration. In all four models, the 13 bytes that cannot occur in valid UTF-8 remain at initialization, while every legal high byte lies in a high-frequency band. For Qwen3.8, the norm-based estimate agrees with the corpus estimate within a factor of four. The norm-frequency relation eventually folds, so inversion is useful only as a model-specific, order-of-magnitude estimate. No private data were used.

---


### 132. [Beyond a Single Human Demonstration: Learning from Scored Trajectory Alternatives for End-to-End Driving](https://arxiv.org/abs/2611.27515)

**<font color=#1a73e8>作者：</font>** Xinyao Rao, Zecheng Tang, Liuxuan Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human driving logs record only one trajectory per scene, leaving other feasible driving choices without explicit trajectory targets or quality labels. This limits supervision for end-to-end planners that generate and refine multiple candidate trajectories. Meanwhile, conditioning refinement on a large vision-language model adds substantial online inference cost. We propose DriveSTA, which extends autoregressive proposal generation and proposal-conditioned residual flow refinement with scored trajectory alternatives. For each training scene, we generate alternatives offline through smooth deformations of the recorded trajectory and evaluate their simulated execution against logged traffic. Diverse, high-quality alternatives supervise distinct proposals and define residual targets for quality-guided denoising, while candidates spanning the full score range train a scorer to assess driving quality. A shared joint-embedding predictive architecture (JEPA), adapted through masked video-feature prediction, encodes observed frames once and provides temporal context for both refinement and scoring. On NAVSIM v1 Navtest, DriveSTA ranks first among the compared planners trained on NAVSIM data alone. With expanded training data, DriveSTA-Scale achieves state-of-the-art results among the compared methods on Navtest and closed-loop HUGSIM, while reducing mean planner forward-pass latency by 73% relative to ChainFlow-VLA in matched evaluations.

---


### 133. [PaMuk-Bench: A Parallel Multilingual Multitask Benchmark for Vision-Language Tasks](https://arxiv.org/abs/2611.27521)

**<font color=#1a73e8>作者：</font>** Silviu-Florin Gheorghe, Radu-Stefan Popa, Adriana Valentina Costache 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While vision-language models (VLMs) currently obtain notable results for highly-studied languages, e.g. English, they exhibit significant performance drops in certain low-resource languages, especially due to the lack of annotated datasets. To this end, we propose PaMuk-Bench, a novel parallel multilingual multitask benchmark for vision-language tasks. Our benchmark includes a set of over 10K curated English prompts that are translated into six languages: Arabic, Danish, French, Hindi, Italian, Romanian. Parallel translations, which are obtained via a semi-automatic process, along with accompanying generated and retrieved images enable the comparative development and evaluation of VLMs across a wide range of tasks: text-to-image generation, image captioning, content-based image retrieval, image generation difficulty estimation, image retrieval difficulty estimation. We empirically show that zero-shot English and multilingual pre-trained VLMs compare consistently worse than their fine-tuned counterparts, confirming that PaMuk-Bench is a valuable resource that can drastically reduce the language gap across a variety of VLM architectures and tasks. PaMuk-Bench is available at this https URL.

---


### 134. [Fix Where It Fails: Root-Cause-Guided Agentic Harness Optimization for Scene Graph Generation](https://arxiv.org/abs/2611.27529)

**<font color=#1a73e8>作者：</font>** Jee Eun Kim, Donghyeon Choi, Sangjune An 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scene graph generation (SGG) aims to detect objects in an image and predict the relationships between them. The standard PredCls, SGCls, and SGDet settings show how much performance drops without ground-truth boxes and labels, but not where or why a model fails. Knowing this would allow fixing a model where it fails, without retraining. We propose RoHa-SGG (Root-cause-guided Harness optimization for SGG), which extends agentic harness optimization to SGG. It optimizes the harness, the inference code around a frozen SGG model. RoHa-SGG has two main LLM agents. A root-cause analysis (RCA) agent finds the components where the model fails and diagnoses why, and a proposer agent searches for a harness that fixes these causes. We evaluate RoHa-SGG on Visual Genome and PSG with representative two-stage, one-stage, and multimodal-LLM SGG models. The analysis shows that the components where ground-truth triplets are lost differ across models and datasets. RoHa-SGG improves every metric on all five model-dataset combinations. Graph-constrained R@100 and mR@100 rise by up to 15.8 and 26.4 points for the multimodal LLM and by up to 3.6 and 10.1 points for the two-stage and one-stage models. With root-cause guidance, the harness search reaches the final score of an unguided search up to three times faster.

---


### 135. [Standard-Anchored Delegation in Teachers' Use of Generative AI](https://arxiv.org/abs/2611.27533)

**<font color=#1a73e8>作者：</font>** Muhammad Saleh Farooq, Muhammad Ahmad Khan, Muhammad Jon Raza  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Teachers who use generative AI must decide which parts of their work to hand over, while they remain accountable for what reaches students. We studied these decisions in Punjab, Pakistan, through a qualitatively driven mixed-methods study. We interviewed 13 teachers from government, private, NGO and vocational institutions, four administrators and one student, and coded each teacher's position on twelve educational tasks. Nine teachers accepted AI drafts or substantial assistance with lesson planning, but none accepted AI-drafted learning objectives, and eleven did not use AI to encourage or emotionally support students. Teachers who would accept AI marking required that the model be given a rubric or marking criteria. Building on assessment research and HCI work on verifiability, we call this pattern standard-anchored delegation: teachers handed a component of a task to AI when a standard outside the model, such as a textbook or rubric, defined a correct output and the teacher could apply that standard to the result. Having a standard was not always enough. Several government-school teachers did not use AI to mark quizzes even though the quizzes had answer keys, because they expected students to look for evidence of the teacher's effort. Checking AI output required subject knowledge and time, and private schools gave teachers more support for this than government schools did. Participants also read disclosure of AI use as a statement about whether the teacher had reviewed the work. We propose that teacher-facing AI tools ask for the relevant standard before generating and show each output beside it, and that schools account for the time that checking takes.

---


### 136. [Open CDLM: A Benchmark and Library for Continuous Diffusion Language Models](https://arxiv.org/abs/2611.27536)

**<font color=#1a73e8>作者：</font>** Hao Jiang, Ruixi Chen, Jiayi Han 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reliable comparisons of continuous diffusion language models (CDLMs) require evaluating both model fit and the distribution of generated text. Two common practices leave this goal only partially addressed. Likelihood-based evaluation often reports a variational upper bound on discrete negative log-likelihood, whose slack can confound comparisons. Generated-sample-based evaluation commonly combines generative perplexity with within-sequence unigram entropy; both scores can remain favorable even when a sampler produces the same text on every draw. We introduce \textbf{Open CDLM}, a benchmark for evaluating CDLMs and their samplers, and describe the design of an accompanying open-source library to support reproducible comparisons. For likelihood-based evaluation, we clarify which comparisons of model fit are supported by reported perplexity bounds and how those conclusions depend on the evaluation procedure. For sample-based evaluation, we use \textit{Kernel Text Discrepancy} (\textbf{KTD}) to compare collections of generated and real texts, alongside diagnostics for diversity, validity, and coverage. In controlled OpenWebText experiments, replacing a collection of texts with copies of a single selected passage improves both conventional generation scores. MAUVE detects the resulting collapse, and its response to other perturbations depends on the text representation and the type of perturbation. This work marks the beginning of Open CDLM as an open-source project for CDLM research. We will maintain and extend the library over time and welcome contributions from the community.

---


### 137. [When Visually Rich Documents Meet Multi-Vector Retrieval for Region-level Retrieval-Augmented Generation](https://arxiv.org/abs/2611.27542)

**<font color=#1a73e8>作者：</font>** Xu Yuan, Liangbo Ning, Yujuan Ding 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visually rich documents (VRDs) convey knowledge through textual, visual, and layout information that text-centric Retrieval-Augmented Generation (Text-RAG) struggles to fully exploit. Recent Vision-RAG approaches enable retrieval and generation directly from document images, retaining this multimodal information. However, earlier Vision-RAG methods commonly adopt coarse retrieval representations and full-page visual contexts, which can obscure local evidence and introduce substantial redundancy and computational overhead. To address these challenges, we propose MV-VisRAG, a region-level Vision-RAG framework that uses semantically complete regions for both document representation and visual augmentation. Specifically, MV-VisRAG first constructs these regions through a ContentAdaptive Regionalization module. It then encodes them into local region vectors and a page-level global vector using a VLM-based retriever trained through multimodal reconstruction pretraining and retrieval fine-tuning. With this compact multi-vector representation, MV-VisRAG performs late-interaction retrieval and estimates region contributions from the resulting matching scores. These contributions guide the selection of relevant regions, which are then rearranged into a compact visual context for generation. Experiments across five benchmarks demonstrate retrieval and generation gains over corresponding baselines, while region-level augmentation substantially reduces visual tokens and computational cost. Our code will be made publicly available at this https URL.

---


### 138. [Altair-Nidhogg: Which Model-Merging Theories Hold for a One-Pass Decision Encoder? Soups, Task Arithmetic, TIES and DARE Against Joint Training and Prediction Ensembling](https://arxiv.org/abs/2611.27550)

**<font color=#1a73e8>作者：</font>** Mohammed Nayeem Khan, Navin Kumar R, Akhil P  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Laya is a small model that answers a multiple-choice question in one pass: each option has a name and a written description. A new skill costs a training run, so we test whether published recipes for merging fine-tuned models (weight averaging, task arithmetic, TIES, DARE) work for it, and whether the theories behind them hold. All 156 models start from one released checkpoint: four plain fine-tunes, five specialists (each adds one kind of training row), joint fine-tunes on all rows, and prediction ensembles. Items are held-out, synthetic and LLM-labelled. In-family, each skill is scored on new items of its own kind, and "kept" is the share of a specialist's gain over the plain fine-tune. Averaging four specialists keeps 52% [38, 64] with +1.7 points of general accuracy; adding the full vectors keeps 42% [3, 63] with -9.0; TIES, which trims and resolves sign conflicts, keeps 64% [50, 76] with +1.5; joint fine-tunes, which see all the rows, keep 120% [104, 162] and 116% [104, 149]. DARE does not repair the full sum (-0.4 points), and ensembles of the models' predictions keep 26% to 54% depending on how they are combined. Swapping the seed of one specialist moves the average by up to 8 points (23 for the full sum). Of 10 predictions fixed in advance, 1 held, 1 held partly, 7 failed and 1 could not be tested. Out-of-family (benchmark questions, code-mixed tickets), the four-way average, joint models and ensemble stay within 2.6 points of the plain fine-tune, but full-vector sums lose up to 7.7. Labels are LLM-made, data synthetic, one base model.

---


### 139. [Vega-Fafnir: Is Greedy Decoding the Same Decoding? Where Rounding Noise in Speculative Verification Comes From and What Removing It Costs](https://arxiv.org/abs/2611.27554)

**<font color=#1a73e8>作者：</font>** Mohammed Nayeem Khan, Navin Kumar R  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Serving engines treat the ways of running a greedy language model as interchangeable: cached or not, padded or not, alone or batched, one token or several verified at once (speculative decoding). In finite precision they round differently. We measure how often the greedy text of Qwen3-0.6B (bfloat16, 128 new tokens, GSM8K and ARC prompts) differs from a reference that decodes one token per pass. Verifying 4 guessed tokens per pass changes 60% of 150 prompts and padding changes 68%; every first divergence has a top-1 minus top-2 logit gap of 0.375 or less. A split of the noise shows that cache entries written by multi-token passes are about as noisy as the multi-token pass itself. A margin gate (fall back to one token when the gap is below a bound calibrated on separate GSM8K prompts) whose fallback reads that cache does not help: 58 of 100 prompts differ, against 61 of 100 for plain verification. Rebuilding the cache with one-token passes leaves 0 of 100 different but costs 7.2 model passes per token, against 1.0 for the reference. Fixed-width decoding makes drafted and plain decoding identical (0 of 100 prompts differ) at 0.75 passes per token. On shifted MMLU and HellaSwag prompts the rebuild gate leaves 0 of 60 different, plain verification 48 of 60. On 138 further and shifted prompts the bound was exceeded at 0.6% of positions and missed 0 of 309 flips. One GPU, one drafter, small models.

---


### 140. [Bringing AI Assistance to the Beznau Nuclear Power Plant: A Hierarchical System of LLM Agents for Reactor Monitoring](https://arxiv.org/abs/2611.27556)

**<font color=#1a73e8>作者：</font>** Wenqi Zhou, Leonardo Baldo, Edwin Kolbe 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Beznau Unit 1 in Switzerland, in operation since 1969, is the most experienced nuclear reactor still running worldwide. Five decades of incremental modernization have left its monitoring systems, alarm logs, variable catalogs, technical specifications and investigation reports in separate silos that were never designed to be queried together. As a result, investigating a core instrumentation anomaly means slow, manual gathering of knowledge scattered across databases, documents, and experienced colleagues. We present a hierarchical multi-agent assistant built on large language models (LLMs) to support these investigations and reduce the need for tedious manual searches in SAP systems. An orchestrating agent breaks down an engineer's question and hands the parts to specialized sub-agents, each with read-only access to one source. Domain expertise is written as natural-language procedures that plant engineers can read, review and revise. The system is strictly advisory, with every answer traced back to its sources. We also report organizational lessons from introducing agentic AI into a culture built on safety, traceability and conservative change. Beyond the technical architecture, the Beznau case study examines how an assistant can be introduced into a setting where evidence must be traceable, changes carefully reviewed, and operational decisions retained by plant personnel, paving the way for the responsible use of agentic AI in industrial plant monitoring.

---


### 141. [Can Language Models See the Circuit in Pixelated RFIC Passives?](https://arxiv.org/abs/2611.27559)

**<font color=#1a73e8>作者：</font>** Jonathan Zhou, Kaushik Sengupta  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The emergence of inverse-designed, pixelated passives for microwave and millimeter-wave applications has been a major development in the field of RFIC design. These devices, which appear to be QR-code-like in structure, exist in a generalizable, high-dimensional design space that includes conventional passive topologies. However, these structures are naturally unintuitive for designers, and failures or deviations in performance are difficult to debug. In this work, we ask whether a frontier language model can understand, predict, and edit the responses and layout structure of pixelated passives. The agent, run with all tools disabled, is first asked to read layouts on 18x18 and 27x27 tile grids and, in a single reply, predict the input impedance and loss of the structure from 20-100 GHz. On eight GA-synthesized layouts and five random fills, the predicted Smith-chart locus follows full-wave simulation results closely, with a systematic shift that places features about 16% lower in frequency than EM. On multipath loop structures it identifies notches successfully but shows a smaller frequency bias, about half that of an ideal transmission-line model that ignores bends. The agent is then asked to debug seven designs that fail their specification, and given a budget of five EM simulations and at most twelve changed tiles, it is able to improve all seven and bring five designs within specification. These experiments suggest language models can serve as an interpretability and debugging tool for traditionally non-intuitive inverse-designed passives.

---


### 142. [Mjolnir: Finding and Reproducing Vulnerabilities in Root-of-Trust Firmware and RTL with Project-Grounded Agents](https://arxiv.org/abs/2611.27567)

**<font color=#1a73e8>作者：</font>** Collin MacDonald, Carl Lundin, Stephen Herwig 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A root of trust (RoT) anchors secure boot and attestation for the system above it, so a bug in RoT firmware or hardware undermines every layer that trusts it. LLM agents now find real vulnerabilities in general-purpose software, but RoT code presents two challenges. First, many security-relevant bugs depend on project-specific trust boundaries and fault-injection countermeasures rather than generic vulnerability patterns, and may cause no crash. Second, without RoT hardware, agents must exercise RoT inputs through the project's own hardware model, mocks, or RTL testbenches.
We present Mjolnir, an agentic pipeline that supplies each project's threat model and design conventions to discovery and skeptical review agents, and reproduces surviving findings as proof-of-concept tests in the project's own toolchain. We evaluate Mjolnir on six firmware and RTL targets in Caliptra, OpenTitan, and OpenPRoT. On Caliptra's runtime firmware, it reaches 83.3%-100% precision across three models under blind expert labeling, including 100% on Gemini 3.8 Flash versus 66.7%-78.6% for four single-agent baselines on the same model. On 34 known security-relevant bugs in Caliptra's core firmware fixed after the models' training cutoffs, it finds 10 with Gemini 3.8 Flash versus 7 for the best baseline, and 17 with Gemini 4 Argon versus 12. Across our evaluation scans, maintainers have confirmed 64 of Mjolnir's findings as previously unknown security-relevant bugs: 37 across three models on Caliptra's runtime firmware and 27 across single scans of the other five targets.

---


### 143. [WEIR: Watershed Exploration and Drift-Aware Prefix Shrinkage for Multi-Turn Agent Reinforcement Learning](https://arxiv.org/abs/2611.27570)

**<font color=#1a73e8>作者：</font>** Pixel Nomand, Elena Voss, Marcus Hale 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-turn language model agents often receive only a single binary reward at the end of a long interaction trajectory, making it difficult to separate decisive decisions from routine steps or estimate accurate intermediate values. Prefix-tree methods improve sample efficiency by merging trajectories that share action histories, yet two structural flaws remain: naive pooling mixes stale off-policy outcomes into critic targets with fixed weights, and uniform or entropy-driven branching wastes continuations on dead-end states whose outcome is already settled. We introduce WEIR (Watershed Exploration and Intrinsic-Drift Shrinkage), an actor-critic reinforcement learning framework grounded in a Doob turn-variance conservation identity. WEIR maintains a cross-iteration canonical action-prefix tree with exponentially discounted visit counts and trains a prefix-conditioned critic toward a minimax drift-aware shrinkage target that adapts from single-trajectory returns at rare nodes to pooled empirical means at dense nodes. Using the same pre-update critic, WEIR allocates rollout budgets across tasks via Neyman stratification $B_q \propto \sqrt{\hat{p}_q(1-\hat{p}_q)}$ and directs within-task branches to watershed forks where high survival-headroom uncertainty coincides with steep value cliffs. Across four multi-hop QA benchmarks, ALFWorld, and WebShop on Qwen2.5-3B/7B-Instruct, WEIR achieves $32.18\%$ and $37.85\%$ average QA exact match and $84.83\%$ and $87.81\%$ ALFWorld success rates, outperforming CAPO by $1.50$--$3.74$ points while generating $28$--$29\%$ fewer rollout tokens than chain sampling.

---


### 144. [PRISM: Validation-Free Online Batch Selection for LLM Fine-Tuning via Preconditioned Conic Ghost Matching](https://arxiv.org/abs/2611.27578)

**<font color=#1a73e8>作者：</font>** Lin Tang, Wei Zhang, Jing Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online batch selection lowers the cost of fine-tuning large language models (LLMs) by replacing each candidate batch with a smaller informative subset. Existing selectors typically depend on a held-out validation or proxy set, or else rely on Euclidean facility-location objectives over unpreconditioned gradients whose diameter-shifted similarities are distorted by heavy-tailed gradient norms and cross-layer anisotropy. We introduce PRISM (Preconditioned Ray-Isotropic Submodular Matching), a validation-free online batch selector that aligns candidate gradients in a factored second-moment metric and casts subset construction as conic facility location over positive ray projections. Computing the required pairwise geometry through factored preconditioned ghost inner products avoids materializing per-example parameter gradients, while the conic objective remains normalized, nonnegative, and monotone submodular---guaranteeing a $(1-1/e)$ greedy approximation whose additive error scales with total batch gradient energy rather than the worst-case outlier diameter. Assigning each candidate to its best-aligned selected ray induces closed-form radial projection weights that automatically shrink orthogonal or noisy examples toward zero. We derive a nonconvex convergence bound showing that optimization error is governed directly by the conic representation cost. Across four LLM fine-tuning configurations spanning 1.5B to 8B parameters, PRISM outperforms full-batch training, Euclidean facility location, and zeroth-order selectors, and rivals or surpasses validation-guided baselines without held-out data.

---


### 145. [Tasklets: A Unit-Test Benchmark for Language Model Architectures](https://arxiv.org/abs/2611.27607)

**<font color=#1a73e8>作者：</font>** Zayd Muhammad Kawakibi Zuhri, Munachiso Samuel Nwadike, Kentaro Inui 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Tasklets, a benchmark of small synthetic tasks for evaluating the computational capabilities of language model sequence-mixing layers. These tasks probe foundational capabilities such as recall, sequence manipulation, and state tracking. Such tasks are widely used in architecture research, but differences in task selection, formulation, and evaluation make comparisons across studies difficult. Tasklets brings these tasks together, organizing them by the capabilities they test and providing a shared setup for evaluating how different architectural layer types learn fundamental computations. We compare a broad range of layer types through controlled experiments with small models. Our task implementations and evaluation code support reproducible, low-cost testing of new architectural proposals: this https URL.

---


### 146. [Potential emergence in LLM agents: a statistical physics perspective](https://arxiv.org/abs/2611.27618)

**<font color=#1a73e8>作者：</font>** Zhuo-Yang Song, Hua Xing Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> There has been significant recent interest in understanding the behaviour of LLM agents from the perspective of human preferences or corpus statistics. In this paper we propose agent states as intermediate variables through which post-training can be measured and predicted. From a statistical physics perspective, we study the emergence of a global potential which governs the transition of state in LLM agent reasoning. We introduce a partition function to model the ideal KL-regularised transition distribution and track potential structure, mean reward and state entropy. We demonstrate our approach in two Qwen3.5-9B tasks: safety-test selection and physics-reasoning auditing. We observe that the potential structure strengthens during post-training as predicted from our framework, while joint changes in reward and state entropy provide consistency evidence. States thus provide a quantitative description of how post-training organises agent behaviour.

---


### 147. [Sketch2TikZ: Multi-Reward Reinforcement Learning for Converting Hand-Drawn Sketches to Executable TikZ](https://arxiv.org/abs/2611.27620)

**<font color=#1a73e8>作者：</font>** Shubham Paliwal, Arushi Jain, Monika Sharma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic digitization of hand-drawn sketches into editable formats is crucial for modern document workflows and LaTeX integration. Converting sketches into executable TikZ code provides a structured representation of diagrams, but remains challenging due to noisy and ambiguous inputs, which hinder reliable interpretation and limit the effectiveness of token-level supervision for ensuring global diagram validity. To address these challenges, we propose Sketch2TikZ, a reinforcement learning framework that optimizes sketch-to-code generation via a sequential multi-reward strategy, combining Code-Structure ($\mathcal{R}_{cs}$), OCR ($\mathcal{R}_{ocr}$), CleanDIFT ($\mathcal{R}_{cd}$), and Self-Similarity ($\mathcal{R}_{ss}$) rewards to enforce textual, visual and structural correctness. We evaluate Sketch2TikZ on the SkeTikZ and FlowChart-3B benchmarks using metrics including compilation success rate (CSR), image similarity, code similarity, and character similarity. Our method achieves near-perfect compilation success and improves visual and textual alignment over strong open-source baselines, while remaining competitive with proprietary GPT-based vision-language models. Extensive ablations demonstrate that curriculum-based reward scheduling is critical for reducing reward interference, stabilizing training and mitigating proxy over-optimization. Overall, our results highlight the effectiveness of reference-aware, multi-objective reinforcement learning for structured diagram generation from noisy sketches.

---


### 148. [Automating Multi-View Quality Assessment of 3D Annotation Layouts](https://arxiv.org/abs/2611.27621)

**<font color=#1a73e8>作者：</font>** Hongyi Yang, Jinao Wu, Yanwei Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text labels provide descriptive information about elements in visual scenes. In 3D visualization, the arrangement of these labels and their connections to target locations forms an annotation layout. Assessing layout quality supports comparisons between alternative layouts. However, existing quality measures often focus on specific layout properties and may not fully reflect human judgments of overall quality. Moreover, a layout may appear clear from one viewpoint but suffer from occlusion or clutter from another. To address these issues, we propose a multi-view quality assessment method based on a multimodal large language model (MLLM). We fine-tune a compact MLLM using structured supervision from human ratings to predict a rating for each quality dimension in each view. These ratings are aggregated into view-level and sample-level quality scores. To support training and evaluation, we construct the Annotation Layouts with Quality Assessment (ALQA) dataset, containing 3,216 layout samples from 1,072 3D objects across 13 categories. Each layout is rendered from 5 predefined viewpoints, and each view is independently rated by 3 human raters across 5 quality dimensions. On ALQA, our method agrees more closely with human reference scores than the evaluated MLLM baselines, and a user study demonstrates strong agreement with human preferences in layout ranking.

---


### 149. [Efficient VLA Reinforcement Learning via Subchunk Rollouts in Latent World Models](https://arxiv.org/abs/2611.27645)

**<font color=#1a73e8>作者：</font>** Nan Tang, Han-Tao Zhang, Jing-Cheng Pang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model-based reinforcement learning (MBRL) can improve pretrained vision-language-action (VLA) policies through imagined experiences. However, existing VLA-MBRL methods primarily rely on large-scale image or video generation world models, incurring large computational overhead. Latent world models offer a more efficient alternative but face two challenges: compounding errors during recursive prediction and incompatibility with VLAs' visual input interfaces. In this work, we propose LS-MBPO, a lightweight residual MBRL framework that leverages latent world models to improve upon pretrained VLAs. LS-MBPO introduces two key techniques: (1) Hierarchical Forcing, which combines dense causal supervision with autoregressive feedback to mitigate compounding prediction errors; and (2) Latent Subchunk Rollouts, which leverage action chunks from a frozen VLA policy and a latent residual policy for successive subchunk refinement, bridging the gap between latent imagination and VLA policy execution. We further introduce a Progress-Conditioned Branch-Start Curriculum that progressively shifts rollout starting points from later to earlier task stages, enabling effective policy learning from short imagined rollouts. Extensive experiments on LIBERO, RoboTwin, and a real-world ALOHA robot show that LS-MBPO achieves superior task performance and training efficiency compared to existing methods.

---


### 150. [Auditing Post-Training Unlearning in Diffusion Language Models using Sparse Autoencoders](https://arxiv.org/abs/2611.27652)

**<font color=#1a73e8>作者：</font>** Yunha Seo, Changhoon Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Machine unlearning is an approach to privacy protection: it aims to remove the influence of designated data while preserving the model's behavior on information that should be retained. While a growing body of work investigates this objective in autoregressive large language models, machine unlearning remains underexplored in diffusion language models (DLMs). DLMs generate text through iterative denoising, exposing partially masked states whose internal representations change throughout the generation process. This raises a DLM-specific question: can selective forgetting improve by identifying forget-data-associated features and adapting their suppression across denoising stages? We conduct a controlled investigation of this question in LLaDA-8B-Instruct. To evaluate the unlearning of knowledge plausibly encoded during pre-training, we use WMDP as our forget-domain benchmark. Using top-k sparse autoencoders and denoising-state replay, we compare static and stage-adaptive feature suppression. We find substantial shifts in forget-data-associated features across denoising stages, but tracking these dynamics alone does not reliably improve the forget-retain trade-off at the evaluated operating points. Together, our study provides an initial empirical foundation for developing and evaluating machine unlearning as a post-training privacy mechanism in DLMs.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
