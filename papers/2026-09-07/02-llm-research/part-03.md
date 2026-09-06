# 🧠 大模型相关研究 | 2026年09月07日

> 本类共 **180** 篇论文：已确认 **169** 篇，待复核 **11** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-180](./part-04.md)

---

### 101. [MetaStructAtlas: A Grounded 3D Vision-Language Dataset and Benchmark for Functional and Structural Reasoning in Whole-Body PET/CT](https://arxiv.org/abs/2609.03690)

**<font color=#1a73e8>作者：</font>** Chenguang Zheng, Le Xue, Yichi Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The joint interpretation of metabolic function and anatomical structure is essential for clinical diagnosis in whole-body PET/CT. Although recent advances in 3D medical vision-language models have demonstrated remarkable progress, current efforts are limited to regional CT imaging, leaving a critical void in comprehensive whole-body PET/CT analysis. In this work, we introduce MetaStructAtlas, a large-scale dataset for grounded whole-body PET/CT interpretation that synthesizes multimodal imaging with integrated anatomical, metabolic, and semantic annotations. MetaStructAtlas provides 490 co-registered 3D PET and CT volumes with 50,470 organ-level segmentation masks and grounded radiology reports. To facilitate interactive reasoning, we further developed MetaStructVQA, a standardized 3D grounded visual question-answering benchmark containing 100,565 QA pairs. This framework explicitly links diagnostic queries to visual evidence across modalities, encompassing anatomical, morphological, and metabolic characteristics. Finally, we evaluate state-of-the-art 3D medical VLMs on MetaStructVQA, establishing a robust foundation for multimodal representation learning and integrated whole-body reasoning in nuclear medicine.

---


### 102. [Synthetic Semantic Supervision for Contrastive Code Representation Learning in Small Transformers: An Empirical Study](https://arxiv.org/abs/2609.03702)

**<font color=#1a73e8>作者：</font>** Kenneth Paulsen, Florian Tambon, Mike Papadakis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> General-purpose code embeddings power tools for code search, classification, and retrieval. Compact transformer encoders for code typically rely on either human-written docstrings (labor-intensive and inconsistent) or mined structural signals such as execution traces (setting-specific and costly to collect). We empirically study an alternative: contrastive pretraining of small encoders with synthetically generated natural-language descriptions emphasizing code functionality and intent, paired with code in a dual-encoder framework at training and discarded at inference. We benchmark this approach against pretraining-based baselines, generalist LLMs, and embedding-specific models on eight retrieval, classification, and generation tasks across C, C++, and Java. Synthetic semantic supervision yields statistically significant gains over pretraining baselines of the same inference-time size on five of eight tasks, with parity on two more; once fine-tuned, it matches or exceeds zero-shot models two orders of magnitude larger on classification, and it stays on par with execution-aware supervision at matched pretraining data, suggesting a scalable, effective alternative to existing code-representation paradigms.

---


### 103. [Proactive Service Agents: A Unified Decision Framework, Methods, and Evaluation](https://arxiv.org/abs/2609.03727)

**<font color=#1a73e8>作者：</font>** Yan Tang, Tingyu Cao, Yuanbo Tang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents can plan, invoke tools, and modify external states, yet most systems still take an explicit user instruction as a fixed starting point. Proactive service moves the decision upstream: an agent must infer service opportunities from incomplete environmental and user signals, choose among remaining silent, asking, assisting, and acting, and account for interruption, misunderstanding, overreach, and privacy costs. This survey gives an operational definition centered on initiative and formulates the problem as a partially observable sequential decision process constrained by authorization and risk. The formulation represents timing, content, and delivery within one structured action, while making explicit the option value of waiting, the decision value of questions, and feedback-induced state changes. On this basis, we organize existing methods along one decision pipeline (state and need estimation, intervention gating, action construction, and feedback adaptation) and describe prescribed, predictive, model based, and return optimizing mechanisms as nonexclusive policy-construction components. We further normalize decision units and three-axis evidence descriptors across streaming dialogue, screen, video, software-engineering, and human-agent collaboration resources, and formalize metrics for triggering, timing, calibration, user burden, safety, and policy value. The synthesis shows why offline classification performance alone does not predict deployment benefit and why long-term memory is not a defining condition of proactivity. Reliable proactive service instead requires calibrated incremental intervention value, verifiable authorization, recoverable execution, and counterfactual evidence.

---


### 104. [Unfold The World: Factorize 4D Properties in Reinforcing Spatial Reasoning](https://arxiv.org/abs/2609.03729)

**<font color=#1a73e8>作者：</font>** Yijun Yang, Shenghe Zheng, Wenbo Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the remarkable prowess of Vision-Language Models (VLMs) in general multimodal tasks, they remain fundamentally ``flat'' when reasoning about the physical world. We argue that this spatial bottleneck stems from a profound dimensional mismatch: while VLMs are trained to interpret 2D projections, true spatial reasoning demands the recovery of latent 3D geometry and temporal continuity. To conquer this high-dimensional complexity, we advocate a shift from monolithic learning to a ``divide and conquer'' paradigm. We present FactoSR, a factorized reinforcement learning framework that explicitly interpret the dimensions collapsed by visual projection. At its core, FactoSR decomposes the monolithic problem of world-consistent reasoning into three orthogonal, geometric sub-objectives: planar correspondence ($XY$), depth consistency ($Z$), and temporal reversibility ($T$). By optimizing these verifiable constraints within a unified policy learning mechanism, we effectively transform an ill-posed projection recovery problem into a series of tangible reasoning steps. Extensive evaluations on multi-view and video benchmarks demonstrate that this elegant decomposition yields substantial gains in 3D and 4D reasoning, achieving a 5.9% boost on VSI-Bench and 4.5% on All-Angles-Bench. Our findings suggest that reinforcing explicit, factorized 4D consistency is a critical step toward evolving VLMs into robust, world-aware reasoners.

---


### 105. [Beyond BLEU: A Case for Redefining Sign Language Translation Benchmarks](https://arxiv.org/abs/2609.03734)

**<font color=#1a73e8>作者：</font>** Oline Ranum, Edward Fish, Simon Hadfield 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> BLEU-4 is the standard metric for evaluating sign language translation (SLT), but spoken-language metrics may not adequately reflect sign language proficiency. The multimodal, low-resource context of SLT allows models to exploit spurious correlations and spoken-language priors, rather than learning stronger sign representations. In this paper, we evaluate the relationship between spatio-temporal understanding and BLEU-4 across six SLT models on Phoenix-2014T and CSL-Daily, showing that gains in BLEU-4 are not on their own evidence of better sign language understanding. This work introduces an alternative inspired by language-learning assessment, using an open-weight-LLM QA protocol that measures salient content preservation. It aligns more closely with human rankings and is six to seven times more paraphrase-invariant than BLEU-4. Applied to SLT, this protocol targets content transfer, is more robust to train-test overlap, and gives a different picture of the field: the five gloss-free systems are largely within noise of one another on Phoenix-2014T, while the gloss-supervised system stands 9.3 points higher, a gap invisible to BLEU-4.

---


### 106. [Rent-a-RAG: Embedding-Space Watermarks for Auditing Third-Party RAG](https://arxiv.org/abs/2609.03749)

**<font color=#1a73e8>作者：</font>** Alexandr Goultiaev Tolstokorov, Kyriakos Mouratidis, Javad Dogani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Third-party retrieval-augmented generation (RAG) marketplaces create a new auditing problem: data providers may license corpora to a RAG operator, yet later have no visibility into whether their documents are being reused without compensation. Auditing this misuse is difficult because the operator is non-cooperative, answers are paraphrased by the generator, and one response may combine evidence from many providers. We propose DirBucket, a provider-side semantic watermarking and black-box auditing framework for document-level reuse in multi-provider RAG. DirBucket watermarks documents by meaning-preserving paraphrases whose embeddings are biased toward provider-bucket secret directions, enabling detection from black-box answers while preserving retrieval utility. On a challenging benchmark that reflects mixed-provider reuse under black-box access, DirBucket is the only method that consistently achieves strong target detection with no non-target activation, detecting non-compliance in every audit within 23 audited answers on our primary benchmark. The watermark survives adversarial post-answer laundering, and none of the evaluated evasion strategies simultaneously defeats detection while preserving user-perceived answer quality. Detection transfers unchanged to a second benchmark built from real clinical, cyber-threat-intelligence, and legal provider corpora. These results suggest that embedding-space watermarking can make document reuse in third-party RAG statistically auditable.

---


### 107. [SimSkill: A Lifelong Learning AI Agent for Autonomous Mastery of Traffic Simulation](https://arxiv.org/abs/2609.03753)

**<font color=#1a73e8>作者：</font>** Qi Liu, Qinzheng Wang, Yiming Bie  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) become increasingly capable, the long-term value of AI systems depends not only on solving individual requests, but also on transforming experience and accumulated knowledge into durable, reusable competence. We introduce SimSkill, a self-evolving agent built around the Simulation of Urban MObility (SUMO) traffic simulator. SimSkill identifies capability gaps, generates and solves environment-grounded tasks, verifies solutions through an action--critic loop, and consolidates experience into episodic, procedural, and semantic memory without updating the backbone model. Through autonomous exploration, it builds a reusable library spanning the traffic-simulation workflow. We evaluate SimSkill on two held-out benchmarks with three backbone LLMs and independent artifact-based verification. SimSkill improves verified completion by up to 25 percentage points, while ablations show complementary contributions from procedural and semantic memory. Its benefits remain backbone- and budget-dependent: memory does not improve every model or uniformly reduce inference cost. More broadly, SimSkill illustrates a design paradigm in which natural language preserves and composes computational capabilities, while executable tools and code provide precise and reproducible execution. All code and experimental data are publicly available at this https URL.

---


### 108. [ENEAS: Embedding-guided Neural Ensemble for Adaptive Segmentation](https://arxiv.org/abs/2609.03756)

**<font color=#1a73e8>作者：</font>** Javier del Pino, Salvador Rodríguez, Alejandro Garabito 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present ENEAS, a unified, text-promptable method for instance tracking and semantic discovery. Text-promptable segmentation models, including the latest foundation models such as SAM 3, still suffer from temporal hallucinations, spatial fragmentation, and semantic misclassification: they fail to report target absence when an object leaves the field of view, segment local textures instead of the complete object during extreme close-ups, and prioritize visual features over ontological reality, so that visually similar artifacts such as statues, paintings, or reflections are segmented as target entities.
ENEAS works two ways from a single method: precise tracking and high-quality segmentation of a unique instance, and open-concept discovery of every instance a text query names, resolved by a semantic verification layer. For tracking, we extend the geometrically robust SeC architecture, previously limited to point interactions, with a text-prompting adapter and leverage its temporal memory, so that the target is held through disappearance without drifting to distractors and kept whole even when it fills the entire view. For discovery, the verification layer combines high-speed visual embedding matching with conditional VLM refinement, invoking semantic reasoning only for ambiguous candidates, which filters out the ontological errors that visual-only models cannot distinguish while keeping latency low. Designed with 3D reconstruction in mind, where a single misclassified distractor corrupts the asset, ENEAS unlocks high-quality semantic tracking and segmentation of video, of broad libraries, and of collections of temporally or spatially unordered data, together with the discrimination to tell true instances from their doppelgangers: things that look alike but are not the same. The code and models are available at this https URL

---


### 109. [RealCADBench: Benchmarking Parametric CAD Modeling from Industrial Design Intents](https://arxiv.org/abs/2609.03773)

**<font color=#1a73e8>作者：</font>** JoyIndustrial VisCAD Team, Linxin Cai, Qiuhe Hong 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Parametric computer-aided design (CAD) modeling is difficult to evaluate with a single metric. Existing CAD benchmarks often emphasize synthetic or CAD-native settings, limited input modalities, or executability and IoUs alone. We introduce RealCADBench, a benchmark for intent-to-program CAD modeling from real industrial design intents. It contains 12,632 tasks from 19 factory-automation categories and spans text descriptions, 2D engineering drawings, real product pictures, and rendered images for both Part and Assembly modeling. We report results on a 1,770-task evaluation slice: 1,745 Part tasks across four input regimes and RCB-Assm25, a 25-task assembly study used in every reported assembly comparison. Each method generates FreeCAD API Python, which a shared runtime executes to export the 3D model. We evaluate the exported model using executability, Solid IoU, Surface IoU, and a rubric-based visual-semantic identity Judge. Among the nine standalone frontier large models evaluated, no model leads all four metrics. Across six frontier-scale large models, executability ranges from 0.565 to 0.812, Solid IoU from 0.2841 to 0.5379, and Surface IoU from 0.112 to 0.217 across the four Part regimes. The highest regime-balanced composite comes from a different model than the leaders on the four component metrics. On RCB-Assm25, Codex with GPT-5.5 improves executability and both IoU metrics over standalone GPT-5.5, but lowers the Judge score by 6.98 percentage points, leaving GPT-5.5 as the Judge leader. We also observe recurring failure modes, most notably missing fine structures, loss of part identity, and incorrect assembly placement. These results show that execution alone is insufficient to characterize realistic CAD modeling and that frontier models and agents differ substantially across executability, IoUs, and visual-semantic identity.

---


### 110. [Typological Feature Prediction with Large Language Models: An In-Context Learning Approach](https://arxiv.org/abs/2609.03775)

**<font color=#1a73e8>作者：</font>** Qianwen Wang, York Hay Ng, Aditya Khan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Typological features are widely used in multilingual NLP, and the prediction of such features holds downstream utility. However, existing methods to predict missing values lack interpretable justifications for predictions, while their performance across resource levels and feature types remains underexplored. Given LLMs' abilities in meta-linguistic reasoning and in providing rationales, we investigate LLMs' performance in typological feature prediction via an in-context learning approach with linguistic data from URIEL+ and Glottolog. We find that zero-shot prompting is insufficient, but when given phylogenetic and geographic neighbour evidence, LLMs substantially outperform all baselines without disadvantaging low-resource languages. We further find that most LLM rationales are consistent with the provided evidence, offering a step toward explainable typological feature prediction.

---


### 111. [A Reverse Sign Language Dictionary: Open-Vocabulary Sign Recognition from Continuous Signing via Video Captioning and Description Retrieval](https://arxiv.org/abs/2609.03788)

**<font color=#1a73e8>作者：</font>** Santiago Poveda-Gutiérrez, Hideki Nakayama, Mayumi Bono  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Isolated Sign Language Recognition (ISLR) is conventionally cast as closed-set classification over gloss labels, which cannot generalize to signs unseen in training and ties every deployment to a gloss-annotated lexicon. We instead recognize signs extracted from continuous signing by (1) captioning a sign-level clip into a free-form procedural description of the articulation with an open-weight vision-language model, and (2) retrieving the closest entry from a vocabulary of target descriptions with a multilingual sentence encoder: a reverse sign language dictionary that needs no gloss supervision and admits an open vocabulary. On 1,300 sign-level segments from a Japanese Sign Language (JSL) dialogue corpus annotated with procedural descriptions (against a 2% top-10 chance floor over the 503-entry target vocabulary), fine-tuning the captioner substantially improves seen-class retrieval: language and vision tower fine-tuning raises top-10 retrieval on seen classes from 4.5% (untrained) to 49%, becoming statistically indistinguishable from a standard supervised closed-set classifier (I3D) on two of the three test sets where a closed-set classifier can be evaluated at all. More importantly, unseen-class retrieval also improves significantly over the untrained pipeline (11.5% -> 21.0% top-10, p=0.0094), a regime in which the closed-set classifier cannot participate. A matcher-side empirical upper-bound analysis shows the sentence encoder already recovers close to 100% of paraphrased gold descriptions, locating a gap in captioning quality that we aim to address in future work. To our knowledge this is the first description-based, open-vocabulary sign lookup from continuous signing without gloss supervision, and the first for JSL.

---


### 112. [LLaDA-Image: Building Strong Image Generators with Fully Open Training Recipes](https://arxiv.org/abs/2609.03796)

**<font color=#1a73e8>作者：</font>** Chuyan Chen, Haoxing Chen, Kun Chen 等 30 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce LLaDA-Image, a unified framework that pairs a 6B Diffusion Transformer (DiT) trained from scratch with a frozen vision-language understanding module built on the LLaDA2.0-Mini diffusion language model backbone. Instead of relying heavily on paired image-text data from the beginning, we first build a strong visual generative prior through image-only pre-training and mid-training. The generation pipeline comprises 220M samples, 98 of which are real images. For efficient and scalable optimization, we use parameter-free RMSNorm throughout the DiT together with the Muon optimizer. The resulting unified model produces highly photorealistic images while accurately following fine-grained editing instructions. We further distill LLaDA-Image into LLaDA-Image-Turbo, enabling fast inference in 2-4 sampling steps. On Qwen-Image-Bench, LLaDA-Image achieves overall scores of 53.53 and 53.38 on the English and Chinese tracks, respectively, setting a new state-of-the-art among open-source models on both tracks. To support further research on capable and efficient generative models, we release our model weights, training code, and detailed recipes.

---


### 113. [SVG-Score: Human-Aligned Evaluation of Text-to-SVG Generation](https://arxiv.org/abs/2609.03806)

**<font color=#1a73e8>作者：</font>** Marco Cipriano, Leonardo Zini, Alexandra Schild 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scalable Vector Graphics (SVG) generation is attracting increasing attention as generative models improve in expressiveness and controllability. Progress, however, is held back by the lack of domain-specific evaluation protocols: current practice relies on metrics designed for natural images, most notably CLIPScore, which was never trained on vector graphics and aligns only partially with human judgment. We introduce \textbf{\ours}, a human-aligned evaluation framework for text-to-SVG generation. Through controlled caption and image perturbations, we first show that CLIP-based scores barely react to the errors SVG generators actually make, such as wrong colors, counts, and spatial relations, and that off-the-shelf Vision-Language Model (VLM) judges, while more sensitive, respond unevenly across error types and SVG styles. We then introduce a human-annotated dataset for \textit{Semantic Alignment}, measuring how faithfully a generated SVG reflects its caption. Building on it, we develop two complementary evaluators: CLIP scorers adapted to vector graphics and then aligned to human preferences, for fast large-scale evaluation, and a VLM judge trained with supervised fine-tuning and reward-shaped reinforcement learning, for more expressive and interpretable assessment. Using both, we benchmark major open-source, commercial, and optimization-based SVG generators on an independent caption set.

---


### 114. [Free Pause Tokens](https://arxiv.org/abs/2609.03807)

**<font color=#1a73e8>作者：</font>** John Langford, Nathan Godey, Giovanni Monea 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A free pause token gives a language model extra compute to form each next-token prediction (as a pause, or thinking, token does) but carries that compute in a parallel prediction stream over a weight-shared backbone rather than as an extra token in the sequence. It improves next-token prediction by 2-3 centinats in practice on a 1B parameter model. Because the pause rides an existing position instead of adding one, it is free to use: at inference it adds no context length, no KV cache, and essentially no latency with the growth in inference flops typically irrelevant as it is not the active bottleneck on throughput. The only primary cost is in training, where additional training compute versus an optimized pretraining pipeline is reduced to as low as x1.14 while preserving most of the benefits. The result is an isoflop, isoparameter, and isotoken improvement over standard next token trained transformers.

---


### 115. [Evaluating Criterion-Conditioned Behaviour of Large Language Models in Content Moderation](https://arxiv.org/abs/2609.03814)

**<font color=#1a73e8>作者：</font>** Danting Zhang, Bei Peng, Robert Loftin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) demonstrate strong performance on standard content moderation benchmarks. However, these benchmarks often aggregate multiple moderation criteria into a single label, making it unclear whether models can disentangle them and reliably apply each criterion when making decisions. To study whether LLMs exhibit criterion-conditioned behaviour, we introduce Diagnostic Evaluation of COntent (DECO), a criterion-independent factorisation of content that enables controlled, criterion-level evaluation. We also introduce pairwise evaluation to compare model outputs across different criteria for the same input. Across four moderation datasets and four LLMs, we find that strong benchmark performance can hide substantial failures at the criterion level. Models struggle most when correct decisions depend not on overall harmfulness, but on the specific aspect of the content that the criterion requires them to assess. Our results highlight a key limitation of current content moderation benchmarks: strong performance on aggregated labels does not provide sufficient evidence that LLMs can reliably evaluate content with respect to individual moderation criteria. These findings call for the development of evaluation methods that explicitly measure criterion-conditioned behaviour.

---


### 116. [Inferring Hidden User Models from the Behavior of Personalized LLM Agents](https://arxiv.org/abs/2609.03815)

**<font color=#1a73e8>作者：</font>** Haoyang Li, Yaxin Xiao, Qingqing Ye 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent personalized LLM agents increasingly transform information retained in memory into compressed or structured representations, which we call user models, to guide later decisions. When source wording is removed from the state reachable through the ordinary interface, these models are commonly treated as more privacy-preserving because direct memory-extraction attacks lose the text they target. Yet we argue that user models expose a new attack surface because an attacker can still recover the private information from the personalized choices they shape, even when source records and backend state remain inaccessible. We therefore introduce UMPeek, a black-box attack based on hypothesis-guided adaptive probing to infer such hidden user model. It forms hypotheses from choices left open by a request, switches among ordinary follow-up tasks, and retains only claims supported and not contradicted by visible behavior. We conduct an extensive benchmark evaluation across diverse personalization tasks and user-model backends against existing attacks. We further validate UMPeek in real-world systems using information confirmed to be retained, and we evaluate defenses against its adaptive probing. Overall, UMPeek outperforms existing attacks in both benchmark and real-world comparisons and continues to recover user information under response-level defenses, showing that keeping records and backend state inaccessible does not guarantee semantic privacy when retained information shapes visible behavior.

---


### 117. [Select, Compress, Reinvest: A Controlled Study of Visual-Token Allocation in Long-Video MLLMs](https://arxiv.org/abs/2609.03820)

**<font color=#1a73e8>作者：</font>** Prakhar Khatri  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-video language models cannot look at every frame: an hour sampled once per second is 3,600 images, and a system keeps only a small fixed slice of that pool. Which frames survive that slice is usually treated as a preprocessing detail; we test whether it should be. Published selectors make the comparison hard because they change the frame scorer, the prompt boundary, the resolution policy, and the answering model all at once. We hold each fixed and vary one decision at a time: selection, spatial compression, and reinvestment of the savings, across six training-free selection rules, three long-video benchmarks, and two answering models. Selection is the largest single lever: on LongVideoBench's hour-long bin, eight query-selected frames beat sixteen uniformly spaced ones by 6.9 points, and Orthogonal Matching Pursuit, an unmodified decades-old sparse-approximation algorithm, matches or comes within a point of every purpose-built selector we compare it against, across all three benchmarks. Compression is close to free: halving each frame's spatial budget at fixed timestamps costs at most 0.44 points. Reinvestment is where that budget turns back into accuracy: spending the freed tokens on twice as many compressed frames, at a measured cost no higher than the original eight, returns a further two to three points; compression only pays off once its savings are spent this way. Along the way, an implementation bug in our own AKS baseline and a 0.07 to 3.74 point gap between two harnesses running the same published rules at the same budget show why these comparisons need to happen inside one controlled harness rather than across papers.

---


### 118. [Semantic Bayesian World Models](https://arxiv.org/abs/2609.03834)

**<font color=#1a73e8>作者：</font>** Tommaso Soru  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge graphs describe reality in crisp assertions, while the systems now consuming them, foundation models and autonomous agents, reason natively in probabilities. We argue that this mismatch is why the integration of language models and knowledge graphs remains a data-feeding pipeline rather than a unified reasoning architecture. We envision Semantic Bayesian World Models (SBWMs): a Web that describes the world not as a database of facts but as a shared, evolving fabric of beliefs over knowledge graphs, where ontological axioms constrain priors, observations update beliefs by Bayesian conditioning, and actions intervene upon the world. We work through what an agent gains from such a model: a home-security agent deciding whether the figure at the gate is a courier or a burglar, an actuarial estimate aggregated by entailment rather than by string frequency, a planning task that language models reliably fail, and the estimation of quantities that no document has ever stated. We then set out what the community must build to make them possible: belief annotation over RDF~1.2, probabilistic entailment regimes, semantic calibration layers, and protocols by which agents that have never met can exchange, and disagree over, calibrated beliefs.

---


### 119. [Adapting to Evolving Requirements: Agentic AI for Retail Supply Chain Operations](https://arxiv.org/abs/2609.03860)

**<font color=#1a73e8>作者：</font>** Lei Zheng, Liping Yang, Zihao Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retail supply chain operations rely on coupled decision modules that must adapt as requirements evolve. LLMs offer a natural-language interface for this task, but existing methods primarily focus on individual optimization models. Extending them to heterogeneous decision pipelines is challenging because a requirement may admit multiple intervention paths with different downstream effects. We formulate requirement-driven adaptation as the joint selection of an intervention route and an admissible module-level change, and propose a graph-constrained agentic framework in which domain agents expose admissible reformulation interfaces and a central processor searches over bounded intervention paths. Candidates are validated and compared using downstream KPIs. In collaboration with a large retail partner, we evaluate 100 warehouse requirements elicited from practitioner interviews, with GPT, Qwen, and DeepSeek as base LLMs. Relative to direct LLM reformulation, our framework improves correctness and end-to-end success across all three models, raising end-to-end success from 72--76% to 79--83%.

---


### 120. [Bioinfoysis Technical Report](https://arxiv.org/abs/2609.03871)

**<font color=#1a73e8>作者：</font>** Qingyang Shao, Xin Zhang, Zhouyang Yuan 等 27 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents have shown promise in bioinformatics, but most existing systems focus primarily on producing final answers, treating planning, tool use, and code execution as transient interactions. This design is poorly suited to long-horizon bioinformatics tasks, where conclusions must remain connected to the data, computations, and intermediate evidence that support them. We introduce \textbf{Bioinfoysis}, a multi-agent harness that represents each request as a persistent, artifact-grounded analysis run. Bioinfoysis combines global planning with step-wise, evidence-driven replanning: the planner maintains an executable checklist and revises pending steps using structured handoffs returned after each worker execution. These handoffs bind intermediate results to their responsible agent, checklist step, and plan generation, preventing stale evidence from being silently reused after replanning. A controlled runtime validates generated scripts, tables, and figures before they are used in downstream analysis or reporting, while role-specific context, persistent memory, and governed bioinformatics skills support reliable execution over long analysis trajectories. We evaluate Bioinfoysis on BixBench and two question-answering tracks of LAB-Bench 2. On BixBench, Bioinfoysis achieves state-of-the-art accuracy of 82.4\%. Across four underlying language models, Bioinfoysis increases average accuracy from 27.81\% to 64.13\% on SeqQA2 and from 3.13\% to 31.25\% on DbQA2. These results demonstrate that reliable bioinformatics automation depends not only on model capability, but also on the harness that governs planning, execution, memory, and evidence flow. We hope that the emergence of Bioinfoysis will play a driving and leading role in the development of the bioinformatics community. Our demo website can be seen in this https URL.

---


### 121. [STAIR (STructure Aware Information Retriever): A novel dataset and LLM based retriever for document structure augmentation](https://arxiv.org/abs/2609.03874)

**<font color=#1a73e8>作者：</font>** Vineet Kumar, Meghanadh Pulivarthi, vishwajeet kumar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval Augmented Generation (RAG) is a key component for generating accurate and hallucination free answers using Large Language Models (LLMs). LLMs are improving at handling long context, but still suffer from "lost in the middle" problem. Thus, precise and accurate retrieval is important. Current retrievers chunk long context into length-based manageable chunks - in the process throwing away rich and informative semantic global structure in the corpus. We introduce a novel retrieval system STAIR that empowers an LLM to exploit global structure in a corpus such as a Table of Contents (ToC) to efficiently store and retrieve information from its model parameters. Our thorough and careful ablation studies with a finetuned Differentiable Search Index (DSI) system show that ToC helps build a low hallucination (less than 0.05%) generative Information Retrieval (IR) system and can generalize to examples where very few training samples are available. To further research in this novel direction of ToC based retrieval we release SearchTome - a diverse benchmark created from 18 books across 6 diverse domains to further research in this novel direction. STAIR achieves a high Recall@1 score of 82.6% on SearchTome as compared to DSI (76.9%), where the difference is found to be statistically significant. STAIR easily beats other strong baselines such as BM25 (59.5%), DPR (68.7%) and out-of-the-box Mistral (13.8%).

---


### 122. [Xiaomi-TabLDM: A Tabular Foundation Model Technical Report](https://arxiv.org/abs/2609.03880)

**<font color=#1a73e8>作者：</font>** Xiaomi-TabLDM Team, Penghui Wang, Wei Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce Xiaomi-TabLDM, a tabular large data foundation model for classification and regression via in-context learning, which delivers superior prediction accuracy without requiring task-specific fine-tuning. Pretrained exclusively on synthetic data generated from structural causal models (SCMs), our model enables more flexible context utilization and more efficient capacity scaling.
i) A new performance standard. Strong regression performance across benchmarks: Xiaomi-TabLDM ranks 1st on OpenML-CTR23 and 2nd on regression across TALENT, TabArena, and BCCO, demonstrating consistently strong regression performance across four complementary benchmark suites. Favorable performance--efficiency trade-off: Xiaomi-TabLDM combines strong predictive performance with substantially lower computational cost. For example, on TabArena regression, it achieves the second-highest Elo while using 82% less training time and 68% less prediction time than the top-ranked TabFM.
ii) Large-scale synthetic pretraining. Xiaomi-TabLDM expands the coverage and diversity of synthetic tabular data used for pretraining. We also adopt a three-stage training strategy together with dual-stream feature grouping, lightweight Attention Residual, and sparse Mixture-of-Experts, enabling Xiaomi-TabLDM to learn richer feature interactions and expert specialization across diverse tabular tasks.
iii) Test-time scaling. Xiaomi-TabLDM further extends tabular prediction through test-time compute scaling, where allocating additional computation at inference time consistently improves predictive performance over the base model.

---


### 123. [Beyond Shallow Alignment: How Post-Training Methods Determine Refusal Circuits And Steering Robustness](https://arxiv.org/abs/2609.03887)

**<font color=#1a73e8>作者：</font>** Hoang Cuong Nguyen, Mark Dras, Usman Naseem  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How do the methods used to train language models to refuse harmful requests shape how that refusal actually works inside the model? We compare three post-training methods - supervised fine-tuning, reasoning-augmented fine-tuning (training on reasoning chains that justify a safety decision), and preference optimization (ORPO) - across three architecturally distinct models (Llama-3.1-8B, Gemma-2-9B, Qwen3-8B). We find that training method, not just data, reshapes how refusal is computed internally: reasoning-augmented training consistently produces a distinct kind of refusal computation, visible across all three models, while architecture independently shapes internal structure and how reliably refusal can be steered. Most importantly, no method we study achieves all three properties we would want from safe alignment at once: refusal that isn't concentrated in a few fragile components, safety gains that don't cost general capability, and safety behavior correctable through small, targeted edits. We caution against treating current post-training methods as a solved, reliable defense, especially for security-critical use. Code and models are available in this https URL.

---


### 124. [GraFT: A Training-Free Framework for Spatial Reasoning in Multimodal Large Language Models via 3D Scene Graphs](https://arxiv.org/abs/2609.03892)

**<font color=#1a73e8>作者：</font>** Junqing Du, Fernando Ropero, Erkin Turkoz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D spatial reasoning underpins understanding and acting in the physical world, yet it remains unreliable in current multimodal large language models (MLLMs). These models falter at precise geometric measurement, at transforming between egocentric and allocentric viewpoints, and at grounding fine-grained appearance. The most common remedies fine-tune the model on large-scale curated spatial-reasoning datasets or attach dedicated encoders for 3D geometry, which typically couples the solution to costly supervision and a specific backbone. We instead introduce GraFT, a training-free framework that supplies the missing 3D structure through a compact, easily maintained 3D scene graph (3DSG). From this 3DSG, GraFT provides three spatial reasoning capabilities: (1) deterministic geometry through symbolic tools, (2) allocentric layout through a bird's-eye-view (BEV) rendering, and (3) visual-attribute grounding through task-relevant egocentric frames. On ScanQA, GraFT improves every metric over the same-backbone baseline, raising CIDEr by 27%. On VSI-Bench, GraFT improves frozen MLLMs by up to 65%, surpassing every proprietary and general-purpose open-source baseline, and several prominent fine-tuned spatial models.

---


### 125. [CROCODIL: Cross-Model Code Editing with LLMs](https://arxiv.org/abs/2609.03894)

**<font color=#1a73e8>作者：</font>** Linghan Zhong, Aditya Thimmaiah, Jayanth Srinivasa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have become ubiquitous tools for code generation and editing. However, development teams often use multiple LLM assistants. Different developers may prefer different models, and individual developers may switch between models across different coding sessions. Because of this, the edits any one model makes are frequently applied to foreign code originally generated by another model. These LLMs are often trained on different datasets, and as a result have different stylistic preferences. Do LLMs behave differently when they edit foreign code originally written by a different LLM with a different coding style? We find that models tend to make more, and often excessive, edits on foreign code. We introduce CROCODIL (Cross-model Code Editing with LLMs), a post-training framework for reducing excessive edits while preserving functional correctness. CROCODIL's similarity reward penalizes large changes, while its execution reward scores build and test success. We use the product of these two rewards to encourage the policy to decrease the edit size without decreasing the edit task success rate. CROCODIL is available at this https URL.

---


### 126. [Beyond Endpoint Scores: Time- and Capacity-Conditioned Evaluation of Continual Knowledge Updating](https://arxiv.org/abs/2609.03900)

**<font color=#1a73e8>作者：</font>** Heejin Choi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual knowledge-updating methods are often declared superior from one final checkpoint and one conventional adapter rank. We show that this can be insufficient to identify the better operating point. Holding a periodic hierarchy fixed, we compare it with cumulative replay over a 24-month Wikidata stream while varying evaluation month, replay LoRA rank, and query formulation. The apparent winner changes across this region: on Qwen2.5-1.5B, the hierarchy's 5.0-point advantage over rank-8 replay becomes an 11.6-point deficit against rank-72 replay, and at high ranks a consolidation-aligned endpoint can suggest a tie while time-averaged replay leads by 9-13 points. The same rank-conditioned reversal appears on Llama-3.2-1B and held-out paraphrases.
These results show that method ranking in continual updating can depend jointly on when performance is measured and how much replay-side adaptation capacity the baseline receives. We therefore propose reporting trajectories and capacity sweeps, and declaring a robust winner only when the ordering is stable across the evaluation region; otherwise, comparisons should report winner regions and retention-stability-cost frontiers. Under this protocol, the periodic hierarchy is a lower-update-cost operating point, not a quality winner.

---


### 127. [Value-Preserving Architectures for Agentic AI Systems](https://arxiv.org/abs/2609.03920)

**<font color=#1a73e8>作者：</font>** Alessandro Pesare, Tommaso Dolci, Katja Hose 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The emergence of agentic AI and LLM-based multi-agent systems (MAS) presents unprecedented opportunities for automating complex tasks, while simultaneously raising critical concerns about the preservation of fundamental human-centered values, such as privacy, fairness, and safety. Although software engineering has traditionally focused on functional correctness, the adoption of LLMs and AI agents into complex socio-technical systems has intensified the need for responsible software engineering and robust value alignment. In MAS, architectural design decisions, such as coordination mechanisms, communication protocols, and system topologies, play a central role in shaping system behavior and the outcomes they produce. This paper argues that architectural choices influence not only the functionality and performance of MAS but can also promote value-oriented system behavior. Therefore, we investigate how different architectural designs support different human-centered values, discussing the following value-preserving architectural patterns: (i) a privacy-aware architecture with a federated topology, (ii) a distributed architecture to promote pluralism and diversity, and (iii) a guard-agent architecture to detect and mitigate unfairness. Finally, we introduce representative use cases to illustrate the proposed architectures in real-world scenarios. By linking architectural design with human-centered values, this work lays the foundation for a unified set of architectural patterns and guidelines towards the design of trustworthy MAS.

---


### 128. [Speak for Me: Giving LLMs the Situational Awareness to Participate in a Meeting](https://arxiv.org/abs/2609.03923)

**<font color=#1a73e8>作者：</font>** Muneeb Khan, Frederic Kirstein, Terry Ruas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In online meeting delegation, LLM agents fail to recognize when to speak. With no structured way to track stances, coverage, and floor, they miss the moments where they should contribute. Prompt-only delegates stay silent on 51.4% of the absent participant's talking opportunities on the AMI corpus. We present CAPA (Collaborative Agent Predictive Architecture), an architecture for online meeting delegation. A Perceiver updates the meeting state from each observed turn. A Predictor forecasts how the conversation will continue. A Controller decides whether to speak and which proposition to surface. A Generator phrases the chosen contribution in the participant's style. Two judges score the forecast and the action against the next observed turn. A Recalibrator updates the meeting state from those verdicts for future decisions. To evaluate online delegation, we introduce an episode-level protocol that scores whether, when, and what a delegate contributes around the participant's actual idea units. The protocol's schema-constrained LLM judges align with human annotations at Cohen's kappa = 0.71. On 137 AMI meetings, CAPA reduces the silence rate from 51.4% to 2.5%, doubles credited recovery (26.1 --> 52.2), and keeps hallucination at 0.6%. The failure mode shifts from omission to selection, with each residual near-miss attributable to a specific module of the architecture. Mechanism ablations identify the meeting state as the lever that closes the recognition gap, where raw-context scaling alone does not.

---


### 129. [RATL: Learning from Retrieved Residuals for Robust Multivariate Time-Series Forecasting](https://arxiv.org/abs/2609.03937)

**<font color=#1a73e8>作者：</font>** Yuchen He, Yueyang Cang, Zhiyuan Ning 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) complements parametric models with retrieved external evidence. The same idea is attractive for continuous-output regression, but directly reusing retrieved target values is often not robust when samples differ in output level, numerical scale, or local dynamics. Moreover, conventional forecasting pipelines generally use residuals for model optimization and error diagnosis, but do not retain individual historical residual examples as memory that can be accessed at inference this http URL multivariate time-series forecasting, we propose RATL, a plug-in residual-retrieval and feedback-correction method. RATL freezes a base forecaster to construct retrieval keys and turns its historical forecast residuals into a train-only memory specific to that base model. At inference time, RATL retrieves residual trajectories from similar historical contexts subject to causal availability constraints, then uses a set-aware router operating over forecast blocks and variables to select and combine these trajectories. Experiments show that historical residuals matched to the current context contain reusable forecasting information and that RATL improves frozen base forecasters in most experimental settings. Ablations further show that learned routing strengthens raw residual feedback, while validation-based correction-strength selection limits residual this http URL real-world benchmarks, we use iTransformer as the primary frozen base forecaster, compare against multiple strong forecasting baselines, and test transferability across backbones. The results show that RATL can further improve base-forecaster performance in most this http URL, RATL shifts the retrieved object from historical target values to base-model-specific historical forecast errors, providing a plug-in, residual-memory-based paradigm for learned feedback correction in continuous-output forecasting.

---


### 130. [Headroom-Drift Replay: A Primitive for Principled Replay Control in GRPO](https://arxiv.org/abs/2609.03941)

**<font color=#1a73e8>作者：</font>** Hyun Bin Park, Du-Seong Chang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> RL-based post-training for reasoning models is increasingly bottlenecked by repeated fresh rollout generation, particularly in agentic settings where environment interaction dominates wall-clock cost. Replay can reduce this burden by reusing past trajectories, but existing methods typically embed it within larger training pipelines involving exploration, experience restructuring, or mixed-policy optimization. This makes replay's own contribution difficult to isolate. We ask a focused question: how far can principled replay selection alone go? We introduce Headroom-Drift Replay, a group-level replay control primitive for GRPO that separates reuse into two decisions. Headroom ranks stored groups by remaining learning value, while Drift gates them by compatibility with the current policy. The fresh on-policy stream remains unchanged, and the method adds no auxiliary generation or training machinery. Across mathematical reasoning, multimodal reasoning, and Agentic Search benchmarks, this single intervention outperforms naive replay and matches or exceeds broader replay methods on Avg Mean@32. In Agentic Search, where environment interaction dominates cost, it delivers comparable quality at materially lower wall-clock time.

---


### 131. [VestigeKV: The NoPE-MLA KV Cache Carries Its Own Eviction Signal in a Vestigial Branch](https://arxiv.org/abs/2609.03949)

**<font color=#1a73e8>作者：</font>** WenJie Fan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The problem. A long-lived KV cache must be compressed before the queries that will read it exist; selection by observed attention (H2O, SnapKV) collapses there (0.00-0.33 needle retrieval on a NoPE MLA model), because a token's importance has not yet been observed. The method. On Kimi Linear, VestigeKV evicts by a query-independent signal the cache already carries: the 64-dimensional decoupled branch, a vestige of RoPE that NoPE training repurposes into a salience channel. Reading 11% of each row, it partitions the cache: the top-m rows stay in the attended tier; every other row moves -- exactly, never deleted -- to a GPU-resident archive reachable per step by a certified trigger. No training, no quantization, no weight or kernel change. Cost. Nothing measurable: retrieval holds at 1.00 under 8x and 0.92 under 32x from 8k to 65k context, zero gap to full-row selection. The attended tier is 0.25 KB of Kimi Linear's 8.1 KB per-token cache at 32x; the archive stays bit-exact and GPU-resident, with host offload as the VRAM-reclaiming variant. The recall tier -- the standard configuration -- holds 128x at 1.00. Kimi K3 is reported to use a NoPE Gated-MLA variant; if its cache layout matches, the method plausibly extends there -- we make no claim beyond the measured model. NoPE exclusivity. The identical operator on a RoPE MLA collapses to 0.08 (plain eviction: 0.42); query-independent salience itself exists only without rotation (top-1 targets span 2.3-6.7% of tokens vs. 10.2-46.8%), and query-universal exact merging is provably impossible under RoPE. All thresholds were frozen before data; 20 archived verdicts and 8 closed routes accompany the paper.

---


### 132. [WorldReward: Reward Modeling for Camera-Conditioned World Models](https://arxiv.org/abs/2609.03952)

**<font color=#1a73e8>作者：</font>** Yibin Wang, Zehan Wang, Junshu Tang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera-conditioned world models generate interactive videos in which commanded actions should induce the expected scene changes while appearance, geometry, and temporal dynamics remain coherent. Existing rewards assess these requirements separately: geometry-based rewards estimate trajectory execution but cannot judge the visual quality of the executed motion, whereas image-based rewards measure frame quality without capturing action execution or temporal dynamics. We posit that a vision-language model (VLM) offers a shared reasoning space for relating actions to their visual outcomes. However, judging a complete long video against its full action sequence creates a lengthy, noisy context in which short-lived local action evidence can be missed or diluted. We present WorldReward, a VLM-based pairwise preference reward model that unifies action-consistency and visual-quality evaluation for camera-conditioned world models. WorldReward decomposes paired videos into action-aligned chunks, organizes each chunk into structured visual evidence, and aggregates chunk-level decisions by voting into separate video-level action and visual-quality preferences. To train it, we construct a large-scale reasoning-augmented preference dataset using structured judgments generated by a frontier VLM and refined through tool-based agent auditing and targeted human review. We further introduce WorldReward-Bench, a human-annotated benchmark measuring reward-model agreement with human preferences across action consistency, appearance quality, and motion quality. WorldReward achieves the highest agreement on all three dimensions, exceeding GPT-5.5 by 3.42, 1.45, and 3.56 percentage points, respectively. When used for RL post-training of HY-WorldPlay 1.5, it consistently improves both action execution and visual quality across short- to long-term horizons.

---


### 133. [Beyond Majority Vote: Multi-Perspective Adjudication for Medical Hallucination Detection](https://arxiv.org/abs/2609.03953)

**<font color=#1a73e8>作者：</font>** Joe Cecil, Marjorie Freedman  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding the frequency of factual errors in chatbot-generated text and evaluating systems that detect these errors is critical for determining chatbot safety. Yet factual-error detection is often treated as a single-pass, single-annotator labeling problem. In long-form chatbot responses, factual errors can be subtle and embedded within mostly correct text.
We develop a multi-perspective annotation study of medically relevant chatbot responses, combining first-pass annotation, LLM-as-a-Judge (LaJ) candidate discovery, and two forms of adjudication: medical-expert and evidence-based fact-checking. First-pass annotators frequently miss factual errors later validated by adjudicators. LaJ improves candidate discovery, but is insufficient on its own: It misses factual errors that annotators catch. We also find disagreement among adjudicators, suggesting that adjudication over multiple candidate sources can improve benchmark completeness, but does not eliminate the need to apply judgment and expertise. Applied to an existing benchmark, this technique reveals a similar pattern of missing annotations. Together, these results suggest that in the settings examined here, single-pass hallucination benchmarks may achieve scale at the cost of undercounting factual errors. Multi-pass adjudication can improve coverage, but inferences drawn from the benchmarks are still sensitive to the judgment, expertise, and evidence used to determine error presence.

---


### 134. [Two-Stage Reinforcement Learning for Sound and Adversarial Test Generation in Code LLMs](https://arxiv.org/abs/2609.03955)

**<font color=#1a73e8>作者：</font>** Jiacheng Xu, Wentao Zhang, Zhiyi Lyu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has substantially advanced code generation with large language models (LLMs) through executable feedback. The feedback for coding problems mainly comes from specific test cases, where high-quality test cases are often scarce since they should be both sound and discriminative. We thus turn to study the auto-generation of test cases using the learned model. We find this is naturally an adversarial RL problem: the model is expected to generate effective test cases as counterexamples, depending on the solver's current failure modes. We propose Test Cases Scaling (TCS), a two-stage RL framework for effective test generation. Both stages train a test generator from a rolling policy-aligned buffer: Stage 1 generates tests consistent with the reference solution, and Stage 2 restricts the buffer to current failure modes and learns counterexample tests. Across TACO and LiveCodeBench, TCS improves both pass@1 and inference-time answer selection according to generated tests. We find the learned test generator also enables effective selection among other LLM outputs.

---


### 135. [FiMI Banking: A Sovereign Model for Indian Retail Banking](https://arxiv.org/abs/2609.03960)

**<font color=#1a73e8>作者：</font>** NPCI AI Research Team, Aman Kumar, Asit Desai 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Banks need conversational systems that can answer product questions, assist customers with account-related requests, and operate safely within strict operational and regulatory constraints. General-purpose language models do not reliably meet these requirements. They fall short when a task requires grounded information, correct tool use, or cautious handling of bank-specific sensitive situations. We introduce FiMI Banking, a controlled Indian retail-banking setting. We build it from vetted banking documents, structured ground truth, synthetic customer backgrounds, and banking tools. We evaluate two post-training approaches: preference optimization for response-level behavior, and reinforcement learning with verifiable rewards for multi-turn tool-use tasks. Preference optimization improves safe behavior substantially: out-of-scope refusal rises from 52% to 80%. Reinforcement learning improves edge-case performance from 0.509 to 0.718 and order-sensitive task performance from 0.590 to 0.679, while using 29% fewer generated tokens. These results show that preference optimization and verifiable-reward reinforcement learning address complementary requirements for reliable banking agents.

---


### 136. [Interface-Induced Trajectory Censoring](https://arxiv.org/abs/2609.03966)

**<font color=#1a73e8>作者：</font>** Wenbo Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent evaluations report a tool-call rate read off the serving stack. That number can be zero while the model is emitting well-formed calls: the interface censors the trajectory before anything downstream sees it.
On BFCL v4's own data, executor and scorer, holding weights, cases, decoding and seeds fixed and changing only the serving adapter, the same model scores 0.00 or 0.96 / 0.19. A 2x2 over chat template and parser locates the effect exactly: both main effects are exactly zero and all of it sits in the interaction -- no component is defective, and repairing one side of the contract buys precisely nothing. On tau-bench's 115 interactive retail tasks the same swap moves server-parsed calls from 0 to 636 and tasks reaching any tool execution from 0 to 103. Our probe reproduces the funnel across a 21x scale range of Qwen2.5-Coder: the server parses 0/100 at every size while well-formed emitted calls rise to 80/100 at 32B (~72 after calibration against an adjudicated gold standard). Under a matched envelope, across a comparable scale span, the silent fraction stays at 0-2, a prediction committed to the repository before the run. Llama-3.1-8B's 23% rate of calling the task function itself as a tool falls to 0 under one strict:true flag.
The mismatch reaches inside the training loop, and its consequence is scale-dependent: in verl's AgentLoop at 7B, 45 of 115 generations carry a complete call; 0 are accepted, 0 execute, 0 return an observation. At 1.5B the same zero is over-determined, so we report the two scales separately. At evaluation time, repairing the adapter restores the mechanism but not a significant outcome gain: parsing 0->84, rescues 0->9, pass rate 53->62 (n.s.). We release a 98-line preflight check that catches every silent failure here. The observed tool-call rate is not a property of the model alone; it is a property of the model-interface stack that measures it.

---


### 137. [Investigating the Ability of Large Language Models to Analyze Recipes for Diabetes](https://arxiv.org/abs/2609.03967)

**<font color=#1a73e8>作者：</font>** Revathy Venkataramanan, Aditya Luthra, Venkatesan Nadimuthu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Several studies have evaluated the ability of Large Language Models (LLMs) for meal planning, yielding positive outcomes. These models can process natural language inputs and leverage learned knowledge from their pretraining to generate meal plans. In this work, we investigate the ability of LLMs to analyze the suitability of given recipes for diabetes. The primary challenge for LLMs is to retrieve relevant dietary guidelines for diabetes, decompose recipes into ingredients and cooking methods, and apply these guidelines to determine the recipe's suitability. To study these challenges, we employ three kinds of prompts namely, (i) Direct Query Prompt (ii) Context-Guided Prompt, and (iii) Exemplary Context Prompt that incorporate different levels of diabetes dietary guidelines from medical sources. We introduce a benchmark dataset curated for this investigation consisting of 7607 recipes that include 3807 recipes suitable for diabetes and 3800 recipes not suitable for diabetes. Our results demonstrate that most LLMs are cautious in predicting recipes as suitable to prevent detrimental outcomes. Further, the models that can reason using the dietary guidelines performed better in predicting the suitability of recipes for diabetes. Overall, Mistral-7B and Llama 70B showed superior performance to their counterparts.

---


### 138. [IchthyoNoma: Nomenclature and Context Sensitivity of Zero-Shot Biological Vision--Language Models for Bangladeshi Freshwater Fish Recognition](https://arxiv.org/abs/2609.03985)

**<font color=#1a73e8>作者：</font>** Nazim-E-Alam, Tarek Rahman, Md Kishor Morol  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot vision-language models (VLMs) are increasingly used as training-free species recognizers, but reported accuracy can reflect more than visual species knowledge. We audit CLIP, BioCLIP, BioCLIP2, and a multilingual Jina CLIP v2 control on seven freshwater-fish categories from two Bangladeshi sources (10,321 images). BioCLIP2 reaches 72.36% on BFF-15 with English common names and 68.91% on SylFishBD with scientific names, versus 25.15% and 14.40% for generic CLIP. BioCLIP2 Bengali prompts are near chance in balanced accuracy (14.22-14.29%); Jina partially recovers Bengali discrimination to 21.89% and 16.36%, but bare Bengali names return to 14.29% on both sources. Paired SylFishBD interventions show no significant weak-blur effect, modest losses from stronger blur/gray masking, a larger white-mask artifact, and strong species dependence. Zero-shot biological VLM scores therefore jointly reflect biological specialization, multilingual alignment, nomenclature, prompt formulation, and context.

---


### 139. [Unlocking Lossless Speedups in LLMs via Discrete Diffusion](https://arxiv.org/abs/2609.04010)

**<font color=#1a73e8>作者：</font>** Subham Sekhar Sahoo, Lingjie Chen, Khiem Pham 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) owe much of their success to next-token prediction (NTP), but their autoregressive (AR) structure requires slow, sequential token generation. To overcome this bottleneck, we introduce diffusion-augmented LLMs, a new class of models that defines an AR model distribution while using diffusion to draw multiple tokens in parallel from that distribution. We decouple the parameters of these models into two sets: AR weights, trained using the standard NTP objective, and lightweight diffusion weights, trained to generate multiple tokens simultaneously. The diffusion weights are learned through a simple Diffusion Distillation phase that adds negligible overhead to existing LLM training pipelines. We also introduce $\Psi$-Spec, a family of samplers that enables lossless acceleration and inference-time scaling at a fixed context length. Unlike speculative decoding, our method requires no separate draft model. Unlike diffusion LLMs (d-LLMs), it accelerates generation without sacrificing the quality of the underlying AR model. The resulting models, called Uno, can be trained from scratch or built by augmenting existing open-weight AR LLMs. Uno achieves higher throughput than leading speculative-decoding methods at every evaluated batch size and delivers up to $3\times$ speedups over the base AR model, including at the largest batch size supported by the device. Notably, our 8B Uno model outperforms the leading open d-LLM, the 26B DiffusionGemma, and the proprietary Mercury 2 across all evaluated benchmarks in agentic tool use, coding, and long-context reasoning. We release code and checkpoints at: this https URL

---


### 140. [LLM4CKD: Large Language Models for Early Stage Chronic Kidney Disease Screening](https://arxiv.org/abs/2609.04013)

**<font color=#1a73e8>作者：</font>** Muhammad Ashad Kabir, Sirajam Munira  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Early screening of chronic kidney disease (CKD) is critical for timely intervention, yet most machine learning (ML) and deep learning (DL) approaches require labeled data and model training, limiting their use in real-world screening settings. This study evaluates the effectiveness of large language models (LLMs) for CKD screening under zero-shot and few-shot in-context learning settings and compares them with traditional ML and DL methods. We propose a framework that uses clinically selected tabular features and structured prompt templates to enable LLM-based inference without task-specific training. LLM performance is evaluated across multiple prompt styles, feature configurations, and data settings, and compared with standard ML, DL, and tabular foundation model (TFM) baselines, and existing CKD screening tools. The results show that LLMs can achieve competitive performance using only a small number of examples, often matching or outperforming traditional approaches in low-data settings. However, their performance remains model-dependent and less stable as input complexity increases. In contrast, ML, DL, and TFM models show more consistent improvement with larger training data. Overall, the findings highlight a trade-off between data efficiency and stability, suggesting that LLMs may serve as a flexible complementary approach for CKD screening when labeled data are limited.

---


### 141. [InSituMeasure: Probing Situated Measurement Grounding in Industrial Scenes with Multimodal Large Language Models](https://arxiv.org/abs/2609.04014)

**<font color=#1a73e8>作者：</font>** Chao Shen, Xinyuan Li, Yunfan Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> For trained operators, gauge reading requires little specialized knowledge, low cognitive effort, and high repeatability. Yet Multimodal Large Language Models (MLLMs) remain unreliable in continuous-valued measurement despite strong results on general multimodal benchmarks. Existing benchmarks expose this weakness but isolate measurement from realistic, knowledge-grounded settings, with limited situated context, specialized instruments, real-world noise, and matched diagnostic annotations, reducing realism and constraining root-cause analysis. We introduce InSituMeasure to evaluate situated measurement grounding. It contains 2,922 real industrial monitoring scenes across eight functional categories of professional engineering instruments, with dense gauge-attribute annotations and noise tags for failure diagnosis. We define metrics for numerical accuracy under predefined tolerances and unit consistency, rejection of fake or unanswerable tasks, and alignment between model failures and annotated error factors. Across 24 state-of-the-art MLLMs, the best model reaches only 25.7\% joint value-unit accuracy and 51.8\% confidence-diagnosis F1, revealing a substantial gap between general multimodal competence and reliable situated measurement. Further analysis identifies failures from text-induced shortcuts, overconfident responses, and authentic industrial noise, including mixed disturbances, viewpoint deviation, occlusion, and environmental interference.

---


### 142. [FLY-EVAL++: An Evidence-Driven Evaluation Protocol for Safety-Constrained Flight Prediction with Large Language Models](https://arxiv.org/abs/2609.04021)

**<font color=#1a73e8>作者：</font>** Yalun Wu, Junfeng Fang, Jiawei Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating large language models (LLMs) in safety-critical, physics-governed environments requires more than accuracy-based metrics, because predictions that are numerically close to the ground truth can still violate operational constraints, combine fields in physically inconsistent ways, or fail to produce usable structured outputs. Existing evaluation protocols do not measure these failure modes reliably. We propose FLY-EVAL++, an evidence-driven evaluation protocol that combines deterministic verification of protocol compliance, physical feasibility, and safety constraints with fixed rubric-guided aggregation into interpretable multi-dimensional scores. We instantiate FLY-EVAL++ for Flight Trajectory and Attitude Prediction (FTAP) by extending the PilotBench setting with history-conditioned and multi-step prediction tasks. Across 66 LLMs, safety compliance is the most discriminative dimension of model behavior: models with comparable predictive performance differ by more than 28 points in safety score, and we observe recurrent failures including safety violations under physically plausible predictions and instability in multi-step rollouts. These results show that evaluation in safety-critical domains should measure constraint satisfaction and structured validity explicitly rather than rely on accuracy-centric reporting alone.

---


### 143. [Representational alignment yields generalizable safety in language models](https://arxiv.org/abs/2609.04022)

**<font color=#1a73e8>作者：</font>** Lingyu Li, Yan Teng, Yingchun Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Aligning large language models (LLMs) is essential for their safe deployment. Current alignment methods mainly optimize observable responses, yet models remain vulnerable when the same harmful intent is recast in unfamiliar or adversarial forms that humans can easily recognize. Prototype theory offers an account of this adaptability. Human concepts are represented around central cases, and new instances are categorized according to their graded typicality relative to these prototypes. Here we show that such categorization of moral concepts is weakly preserved in current LLMs. Across 23 LLMs, models often failed to distinguish opposed moral categories or preserve fine-grained typicality within each category. These deficits persist across parameter sizes and alignment stages. We developed representational similarity optimization, which directly aligns the latent representations in LLMs with the categorization expressed in human moral judgements, without supervising generated responses. In matched experiments using the same 251,334 moral annotations, standard behavioral alignment learned the intended moral judgements at the response level while leaving the categorization structure largely unchanged and increasing vulnerability across adversarial evaluations. Reorganizing moral categorization produced more modest gains in explicit judgements but consistently improved adversarial robustness across model scales on diverse benchmarks and attack strategies. Our findings provide functional support for the view that prototype-based categorization contributes to behavioral adaptability. They also show that transferring this representational principle to LLMs yields generalizable safety under adversarial conditions.

---


### 144. [Instruction Duplication as an Inference-Time Control Primitive](https://arxiv.org/abs/2609.04024)

**<font color=#1a73e8>作者：</font>** Victor Lavrenko  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Procedural instruction following is a basic requirement for controllable language-model systems, especially when generated trajectories are inspected or repaired downstream. We introduce instruction duplication, a minimal black-box inference-time control that repeats only the procedural instruction, without retraining or decoding changes. Across seven instruction-tuned models, 300 medical multiple-choice questions, eight placement conditions, and 16,800 scheduled generations, moving from one to two copies raises the deterministic All-8 diagnostic--responses passing all eight observable tests--from 90.22% to 93.17% (+2.95 percentage points), eliminating 30.2% of the failures remaining after one copy. Pre-provisional TF-IDF recall rises from 73.44% to 74.81% (+1.38 points; Holm-adjusted p < .001), while final-answer accuracy remains exactly 60.21%. Premature commitment increases from 1.52% to 2.30% (p_Holm = .00536). A blinded challenge audit yields 10/30 directional confirmations, 20/30 perceptual ties, and no reversals; its prespecified 28/30 confirmation criterion is not met. Yet this distinction can matter operationally when a downstream system acts on the generated trajectory. In Answer Engineering (AE), where explicit trajectory state determines local repair, the published reason-first no-editing SSNHL endpoint was 25.1%; system-only AE was later reproduced at 84.2%, and the same trailing duplicate raised it to 97.1%. For conductive diagnostic branch preservation, the corresponding values are 58.9% published without editing, 78.6% with reproduced AE, and 73.8% with AE plus duplication--a within-AE decrease, but still 14.9 points above the no-editing baseline. Instruction duplication is therefore a low-complexity, placement-sensitive control whose practical value can emerge through the downstream system that consumes the exposed trajectory.

---


### 145. [IRWOZ 2.0: A Large Language Model-driven Dialogue Dataset for Industrial Robot Conversations](https://arxiv.org/abs/2609.04030)

**<font color=#1a73e8>作者：</font>** Chen Li, Dimitrios Chrysostomou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> IRWOZ has improved industrial human-robot interaction (HRI) dialogue systems through domain-specific annotations. However, its initial version contains substantial noise in dialogue states and utterances, limiting state-tracking accuracy. We introduce IRWOZ 2.0, which addresses these limitations through large language model (LLM) enhanced generation (Mistral/Claude-3.5) and quality refinements. Our improved dataset expands to 390 dialogues across 4 industrial domains (Assembly, Delivery, Position, Relocation), featuring manual corrections and automated typo removal. Benchmark experiments on dialogue state tracking demonstrate significant improvements, with GPT-2's BLEU-4 score increasing from 0.1651 to 0.5604 compared to original IRWOZ. To support industrial HRI research, we publicly released IRWOZ 2.0 dataset at this https URL

---


### 146. [Editable Visual Design](https://arxiv.org/abs/2609.04034)

**<font color=#1a73e8>作者：</font>** Junyan Ye, Wei Liu, Dongzhi Jiang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While diffusion base models such as GPT-Image-2 and Nano-Banana exhibit remarkable visual expressiveness, their end-to-end generation inherently yields flattened bitmaps with error-prone text, precluding layer-wise post-editing. Conversely, code-based visual generation via Coding Agents provides precise layout control and decoupled layers, yet remains constrained by a lack of global aesthetic intuition and the difficulty of coding complex visual assets.
To address this, we propose Editable Visual Design, a new paradigm driven by a Coding Agent. We designate the VLM as the ``creative brain'' for requirement comprehension, task planning, and aesthetic judgment, while utilizing the image generation model as an on-demand ``visual world simulator'' to synthesize standalone visual assets. Operating under an ``imagine first, then act'' closed-loop workflow, the agent generates isolated assets, writes native HTML/CSS, and iteratively refines the design against visual rendering feedback.
Furthermore, Agent Design Replay faithfully reproduces the creative and reasoning trajectory akin to that of professional human designers. Ultimately, the system delivers editable artifacts with decoupled layers and real text, enabling users to perform intuitive mouse dragging and layout adjustments on a graphical user interface. Validations on posters, infographics, and other scenarios show that this paradigm successfully achieves both refined aesthetics and production-grade editability.

---


### 147. [AI-Assisted Design of a Post-Quantum Cryptographic Accelerator: A Deployed-Silicon Case Study](https://arxiv.org/abs/2609.04058)

**<font color=#1a73e8>作者：</font>** Jungmin Park, Eunha Kim, Wooseop Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Post-quantum migration is mandated on published timelines, and silicon that ships with a defect cannot be patched remotely. The standard acceptance gate cannot detect an entire class of ML-DSA defects. Signing resamples until a candidate meets its norm bounds, so the executed path varies with the message, whereas known-answer tests (KATs) sample fixed values and reach only the depths their seeds trigger. Our accelerator passed its full KAT regression while carrying a norm check that outran block-RAM latency, leaving each candidate's final coefficients unverified; the escape surfaced at reject-loop iteration 5. The blind spot lies in the instrument, not the engineer; care cannot remove it. We replace that gate. A byte-exact golden-reference oracle paired with randomized adversarial soak drives the rejection loop past any fixed vector, closing the gap: 301,343 data-dependent signings, zero escapes. Because the gate judges artifacts and never authors, trust becomes separable from authorship, making AI authorship an answerable question. We report 232 logged experiments in which an agentic large language model drove a unified ML-KEM-768 and ML-DSA-65 accelerator with on-chip key custody from RTL to PCIe bring-up on one Kintex-7 XC7K160T, shipped at 98.5% slice occupancy. Success was 71.6%, following a hardware-coupling gradient, 77-85% for documentation and research against 50-53% for synthesis and bring-up, which observability can explain: failure concentrates where corrective signals are physical-side only. That so unreliable an author produced an artifact byte-exact across all six FIPS operations -- its deployed baseline surviving the same 779,945-check zero-failure soak -- is the claim.

---


### 148. [Spurious Advantage Hidden in GRPO](https://arxiv.org/abs/2609.04063)

**<font color=#1a73e8>作者：</font>** Jiamian Wang, Samyadeep Basu, Koustava Goswami 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Group Relative Policy Optimization (GRPO) is widely studied for reinforcement learning with verifiable rewards, where its advantage estimator assigns each rollout a magnitude from within-group reward statistics. In the common case, this magnitude rewards rollouts that reach the correct answer through reasoning. Yet, an overlooked case shares the same surface: a rollout may land on it by guessing, and the formula still assigns a high magnitude, which we identify as the spurious advantage. This arises in three cases: bounded-answer tasks with a small candidate set; open-answer sets hosting bounded sub-cases; and search agents whose budget opens many paths to the same answer. In all three, this misleads the policy toward guess-like behaviors. We propose SIGNBALANCE, whose magnitude is composition-free: it keeps the verifier sign, uses a global scale, and restores zero-mean balance via a stop-gradient per-class rescaling. Across math and search agent benchmarks at different scales, SIGNBALANCE matches GRPO on open-answer math and improves on bounded-answer math and search agents. Code will be released.

---


### 149. [Continuous Actions from Discrete Minds: Latent-Aligned Planning for End-to-End Autonomous Driving](https://arxiv.org/abs/2609.04070)

**<font color=#1a73e8>作者：</font>** Ruoyu Yao, Yusen Xie, Qingzhao Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bridging the gap between the discrete reasoning of Vision-Language Models and the continuous, physics-constrained nature of autonomous driving remains a significant challenge. In this work, we introduce LaPla, a unified Vision-Language-Action (VLA) framework featuring latent-aligned planning to seamlessly ground semantic understanding in precise motion execution. We first design an action tokenizer based on a residual vector-quantized variational autoencoder (VQ-VAE), capturing vehicle kinematics and encoding trajectory features into a structured latent space. Rather than discrete codebook lookups that inevitably introduce quantization errors, LaPla repurposes this representation as a physical prior to bridge the modality gap between high-dimensional semantics and the raw action space. Specifically, given multimodal inputs integrating multi-view images, historical actions, and textual instructions, LaPla incorporates concurrent action queries to causally attend to the multimodal context in a single forward pass, projecting hidden states directly into the pretrained VQ-VAE latent space. The frozen decoder then translates these continuous latents into actions, effectively eliminating quantization errors and ensuring physically plausible trajectories while bypassing time-consuming autoregressive generation. Extensive experiments on the nuScenes benchmark demonstrate that LaPla achieves competitive open-loop performance, reducing long-horizon L2 error by 15.52% compared to state-of-the-art VLA methods. Closed-loop evaluations on the NVIDIA AlpaSim simulator further confirm its superior capability in ensuring smooth driving progress, improving the success rate by 33.34 percentage points with significantly reduced inference latency.

---


### 150. [CORE: Improving Compositional Reasoning in MLLM Embedding via Reranker Distillation](https://arxiv.org/abs/2609.04083)

**<font color=#1a73e8>作者：</font>** Tingyu Song, Mingxin Li, Yanzhao Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> MLLM-based embedding models remain limited in compositional retrieval, often failing to distinguish scenes containing the same concepts but different attribute-object bindings. Yet the same backbone can resolve such distinctions when used as a cross-attentive reranker, motivating us to distill its compositional judgments into the embedding model. We propose CORE, which synthesizes candidate lists spanning five compositional matching levels and introduces a Rank-KL objective that trains the embedding model to reproduce the reranker's fine-grained ranking. We further introduce a graded evaluation protocol and compare contrastive learning, pairwise CoSENT, and listwise Rank-KL under the same data and tuning budget. Our comparison shows that both CoSENT and Rank-KL use the multi-level supervision more effectively than contrastive learning, with Rank-KL achieving the strongest overall performance. Across three compositional reasoning benchmarks (COLA, SUGARCREPE++, NEGBENCH), CORE-RERANKER-8B achieves an 82.7% total average, outperforming Jina-Reranker by 10.7 points, while CORE-EMBED-8B achieves the best total average (0.666) among all evaluated embedding models. The improvements transfer to the MCMR benchmark without sacrificing retrieval performance on COCO and Flickr30K.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-180](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
