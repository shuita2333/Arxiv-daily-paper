# 🧠 大模型相关研究 | 2026年06月25日

> 本类共 **118** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-118](./part-03.md)

---

### 1. [EXPO-SQL: Execution-based Clause-level Policy Optimization for Text-to-SQL](https://arxiv.org/abs/2606.23693)

**<font color=#1a73e8>作者：</font>** Jaehoon Lee, CheolWon Na, Suyoung Bae 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text-to-SQL enables users to query databases using natural language by generating executable SQL queries. Recent methods have increasingly adopted Large Language Models based reinforcement learning (RL) to leverage execution feedback for training. However, existing RL methods assign uniform query-level rewards to all clauses in a SQL query, treating correct and incorrect clauses equally. This coarse-grained reward design leads to insufficient learning signals for correct SQL generation. To address this issue, we propose EXPO-SQL (EXecution-based clause-level Policy Optimization for Text-to-SQL) which provides fine-grained supervision through clause-level rewards. To assign clause-level rewards, our method identifies erroneous clauses by analyzing execution results, including error messages and clause-wise incremental execution. Experiments on widely-used Text-to-SQL benchmarks demonstrate that EXPO-SQL significantly outperforms existing supervised fine-tuning, prompting, and RL-based methods through fine-grained clause-level learning. Our code is available at https://github. com/jhn25/EXPO-SQL.

---


### 2. [Quantifying Prior Dominance in RAG Systems](https://arxiv.org/abs/2606.23695)

**<font color=#1a73e8>作者：</font>** Barak Or  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) grounds Large Language Models in external knowledge, yet current evaluations rely on discrete heuristics that suffer from ''epistemic blindness'' - failing to distinguish genuine contextual information extraction from parametric memory recall. To address this, we introduce the Normalized Context Utilization (NCU) metric, leveraging continuous token log-probabilities across zero-shot, oracle, and adversarial conditions to strictly quantify contextual information gain. Evaluating architectures ranging from 1.5B to 72B parameters alongside a proprietary commercial API reveals that for strict factual extraction (without Chain-of-Thought reasoning), traditional scaling laws exhibit extreme diminishing returns: highly efficient Small Language Models (SLMs) match or outperform high-capacity architectures. Furthermore, we demonstrate that ``Prior Dominance'' correlates with model scale and proprietary alignments. The evaluated commercial API not only overrode explicit external evidence in nearly half of adversarial conflicts, but also frequently suffered from systemic confidence collapse (Negative Transfer) when its parametric priors were contradicted. Our findings highlight the structural epistemic advantage and superior contextual adherence of SLMs in strict extraction workflows.

---


### 3. [Evaluating LLM Usage for Efficient and Explainable Numerical and Classified Implicit Sentiment Analysis of Product Desirability](https://arxiv.org/abs/2606.23701)

**<font color=#1a73e8>作者：</font>** Sherri Weitl-Harms, John Hastings  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Qualitative product feedback can reveal nuanced user experiences, but its implicit sentiment is difficult to measure. This paper presents a scalable and interpretable framework that uses large language models (LLMs) to quantify product desirability from such data. Using two Product Desirability Toolkit (PDT) datasets from ZORQ and CARMA comprising 106 respondent term groupings with gold-standard human annotation, zero-shot continuous numerical sentiment scoring and categorical sentiment classification are evaluated without relying on explicit review scores. Across the datasets, LLMs generated numerical sentiment scores directly from qualitative responses and closely matched expert labels, achieving Pearson correlations up to 0.97 and classification accuracy up to 94%. LLMs maintained robustness even when handling data presented in multiple forms and consistently expressed high confidence. In contrast, lexicon-based and transformer baselines did not produce statistically significant results. Among the models tested, GPT-4o-mini achieved performance comparable to larger models at 94% lower cost, supporting scalable deployment.
The framework also incorporates model confidence ratings and human-readable rationale explanations (xAI), improving interpretability, transparency, and trust while supporting practical use in product satisfaction assessment. In general, using the PDT tool as a survey method along with a cost efficient LLM for sentiment analysis has the potential to provide for product evaluation with results that are rich in terms of sentiment scores (both numerical and classified sentiment) and in terms of the high-level user impressions of the product that can be used to identify ideas for product development and improvement, as well as marketing ideas for target audiences.

---


### 4. [Emergent Relational Order in LLM Agent Societies: From Collective Affect to Authority Stratification](https://arxiv.org/abs/2606.23764)

**<font color=#1a73e8>作者：</font>** Zhiyuan Ji, Xinyu Chen, Ziqi Dai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Fei Xiaotong's Differential Order Pattern characterizes rural society as egocentric and relationally graded, with cooperation attenuating over social distance. Although often treated as culturally specific, its mechanistic basis remains under-operationalized, and prior LLM-based simulations have mainly addressed short-term coordination rather than long-horizon social structure. We propose CAREB-MAS, a multi-agent framework grounded in Affect Control Theory, Social Identity Theory, and Durkheimian collective affect. Agents reason through an emotion-ethics-belief chain and maintain dynamically evolving egocentric identities, while the macro environment specifies only individual production, preference-based allocation, and minimal interaction protocols. Across long-horizon simulations, agents spontaneously reproduce five core Differential Order phenomena: stable labor specialization, guanxi-based economic ethics, relational decay of cooperation, emergent relational authority, and clan-based center-periphery stratification. These patterns shift with production structure from kin-centered integration toward greater functional interdependence. Extensive experiment results support interpreting Differential Order as a structure-sensitive emergent outcome of general social mechanisms, with LLM-based multi-agent simulation providing an interdisciplinary framework for studying social structure and change.

---


### 5. [Reconstructing GRACE Terrestrial Water Storage with Spatio-Temporal Graph Neural Networks: An Application to South America](https://arxiv.org/abs/2606.23833)

**<font color=#1a73e8>作者：</font>** Lukas Arzoumanidis, Lara Johannsen, Klara Middendorf 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Terrestrial water storage (TWS) integrates snow, soil moisture, surface water, and groundwater and is a key indicator of how climate variability and human activity reshape the global water cycle. The GRACE and GRACE-FO satellite missions provide the only direct, globally consistent observations of TWS change, but their record only begins in 2002 which is too short for many climate-scale analyses. We present a deep learning application that reconstructs monthly GRACE-like TWS anomalies (TWSA) back to 1940 by learning the relationship between daily ERA5 meteorological forcing (precipitation, evapotranspiration, runoff) and monthly GRACE observations. In contrast to prior reconstruction approaches based on grid-cell-wise regression, CNNs, or LSTMs, we adapt a multi-variate time series graph neural network (MTGNN) architecture, which was originally developed for mobility and traffic forecasting on urban sensor networks to this satellite-geodesy task. Spatial dependencies are encoded in a static, interpretable hybrid adjacency matrix that combines geodesic proximity with lagged correlations of climatic time series, capturing both local hydrological coupling and large-scale teleconnections. The reconstruction achieves a grid-cell Pearson correlation of 0.69, a basin-mean correlation of 0.94, and a near-zero bias, and it reproduces the spatial fingerprints of the 2015/16 El Niño and 2020/21 La Niña events. A systematic comparison with established reconstruction approaches (GTWS-MLrec, RM-REC, GRAiCE) shows that the graph-based model is statistically competitive at basin scale, reaching a correlation within 0.025 of the best baseline while using only roughly half to a tenth of the predictors the other models require and revealing characteristic weaknesses in arid regions in all models. The complete implementation is publicly available at this http URL

---


### 6. [ABACUS: Adapting Unified Foundation Model for Bridging Image Count Understanding and Generation](https://arxiv.org/abs/2606.23835)

**<font color=#1a73e8>作者：</font>** Anindya Mondal, Sauradip Nag, Anjan Dutta  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> ABACUS is a unified vision-language model that handles object counting, crowd counting, referring-expression counting, and count-faithful image generation without any benchmark-specific training required. Our model is built on existing 3B-parameter unified foundation model and is adapted for object localization tasks using three key innovations: density-aware adaptive zooming with objectness maps for spatial grounding; a boundary-aware count policy via GRPO to eliminate crop-boundary errors; and a cycle-consistent GRPO strategy where the understanding branch self-critiques generated outputs, closing the understanding-generation gap without any external annotations. ABACUS achieves state-of-the-art results across seven benchmarks, outperforming both task-specific specialists and larger generalist models.

---


### 7. [Embodied Explainability and Ontological Obstacles: Why We Struggle to Explain the Answers of Large Language Models (LLMs)](https://arxiv.org/abs/2606.23840)

**<font color=#1a73e8>作者：</font>** Marvin Pafla, Jesse Hoey, Kate Larson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Explainability is often framed as a property of an AI model, with explanations extracted from its internals and shown to users. In this argument paper, we instead provide an embodied account of explainability based on Dourish and enactivist cognition: understanding is created in use as people act on affordances in shared practice. Using demonstrations and conceptual analysis, we reveal ontological obstacles when "looking inside" large language models: surrogates import external abstractions that can be mistaken for the model's, and focusing on internal reasoning misses that explainers participate in their own understanding. We discuss these obstacles in XAI practice, arguing that many explanations are misnamed, which skews their purpose and can increase overreliance. Finally, we highlight how embodied explanations reorganize sense-making by making what matters publicly available for action, and argue that explainability claims should be reserved for designs that provide affordances to probe, coordinate, and repair behaviour in situated practice.

---


### 8. [HANCLIP: A Family of Hyperbolic Angular Negation Vision Language Models](https://arxiv.org/abs/2606.23843)

**<font color=#1a73e8>作者：</font>** Hoang-Bao Le, Aiden Durrant, Thai Son Mai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) are typically pre-trained on large-scale image-text datasets to capture semantic correspondences between visual content and natural language. However, they remain surprisingly brittle to negation: models often rely on shallow word co-occurrence and are easily distracted by misleading or irrelevant textual cues, even when their overall retrieval or classification performance is strong. Moreover, directly finetuning on negation data can interfere with previously acquired knowledge, causing noticeable degradation on standard vision-language benchmarks. To tackle these issues, this work introduces HANCLIP (Hyperbolic + Angular + Negation), a family of VLMs that explicitly restructures the embedding space to encode "what an image is not" alongside "what it is." HANCLIP is trained on a compact set of 20,000 image-text quadruplets and combines a hyperbolic formulation, which models hierarchical semantic relations and asymmetries, with an angular triplet objective that drives systematic separation between negated descriptions and their corresponding positives. This geometry-aware design strengthens negation sensitivity while preserving the global structure of pretrained representations, rather than overwriting them. Extensive experiments across multiple vision-language tasks show that HANCLIP delivers consistent gains on the negation-focused NegBench benchmark, while maintaining competitive or improved performance on standard classification and image-text retrieval benchmarks. The framework is model-agnostic and can be plugged into CLIP, LongCLIP, SmartCLIP, and HiMo-CLIP without large-scale retraining, demonstrating that a carefully designed geometric objective can substantially extend the reasoning capabilities of existing VLMs using only modest additional data.

---


### 9. [Ground Then Rank: Revisiting Knowledge-Based VQA with Training-Free Entity Identification](https://arxiv.org/abs/2606.23881)

**<font color=#1a73e8>作者：</font>** Qian Ma, Qiong Wu, Zhengyi Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge-Based Visual Question Answering (KB-VQA) requires grounding visual queries to external knowledge beyond directly observable content in images. While recent multi modal large language models (MLLMs) show strong perceptual abilities, they struggle on KB-VQA tasks requiring groundings from both fine-grained entity and evidence levels. Most existing multi-modal retrieval augmented generation (MM-RAG) methods tightly couple entity discrimination and section-level evidence ranking into a single re-ranking stage, leading to high cost and limited generalization. In this work, we revisit existing MM-RAG solutions from a workflow perspective and argue both entity-level and fact-level groundings are key bottlenecks. We observe that although MLLMs often fail under open-ended entity naming, they can better identify the correct entity when selecting from a small set of candidate names. Based on this insight, we propose a simple and training-free identify-before-answer IBA framework that decouples entity identification from section-level re-ranking. Our approach prompts an MLLM to select high-confidence entities using only candidate names, followed by an off-the-shelf textual re-ranker for evidence selection. Experiments on Encyclopedic-VQA and InfoSeek show that our method consistently outperforms fine-tuned multi-modal re-ranking baselines while reducing training and inference complexity. Additional analyses reveal that the improvements arise not only from better entity identification, but also from selecting more informative evidence once correct entity is fixed. Our implementation is made public to ease reproducibility.

---


### 10. [Mind the Heads: Topological Representation Alignment for Multimodal LLMs](https://arxiv.org/abs/2606.23885)

**<font color=#1a73e8>作者：</font>** Davide Caffagni, Alberto Compagnoni, Federico Melis 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Representation alignment has emerged as an effective approach to improve Multimodal Large Language Models (MLLMs) by regularizing their internal representations toward those of an external vision encoder. However, existing methods typically align a fixed layer of the language backbone, overlooking the fine-grained structure of Transformer models. In this work, we propose Head-Wise Representation Alignment (HeRA), a method that enforces cross-modal alignment at the level of individual attention heads. Our approach is grounded in the Platonic Representation Hypothesis, focusing on preserving the topological structure of representations (i.e., their local neighborhood relationships) across modalities. Following the Mutual K-Nearest Neighbor (MKNN) alignment metric, we introduce a contrastive objective that acts as a differentiable proxy for matching local structures. HeRA applies this objective during multimodal training to specific attention heads in the LLM, selected by their alignment score according to the MKNN metric. Counterintuitively, we find that aligning the least aligned heads yields the largest gains. Extensive evaluations across multiple MLLMs and 18 benchmarks demonstrate that HeRA consistently improves performance on challenging vision-centric tasks and serves as an effective regularizer against visual hallucinations by naturally curbing the over-reliance on linguistic priors. Our code is publicly released.

---


### 11. [REALM: A Unified Red-Teaming Benchmark for Physical-World VLMs](https://arxiv.org/abs/2606.23892)

**<font color=#1a73e8>作者：</font>** Yifei Zhao, Qian Lou, Mengxin Zheng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly used as perception-reasoning backbones for embodied intelligence in safety-critical physical systems, where perception or reasoning errors can lead to unsafe decisions or actions. Although many red-teaming methods have been developed to probe VLM vulnerabilities, their evaluation remains fragmented across datasets, metrics, and threat models, making direct comparison difficult and obscuring whether observed differences arise from stronger attacks, more vulnerable models, or incompatible evaluation settings. Existing chatbot-centric red-teaming benchmarks mainly standardize jailbreak and content-safety evaluation, but they do not systematically capture physically grounded functional failures or cover red-teaming methods that target physical-world VLMs. This raises the key challenge of comparing diverse attack methods under a unified protocol while targeting the same scenario-specific failures. We introduce REALM, to our knowledge the first unified red-teaming benchmark for physical-world VLMs. REALM integrates 12 red-teaming methods, 3 model-agnostic defenses, and 13 VLMs under a practical black-box threat model with shared datasets and metrics. To align adversarial objectives across attack families, REALM introduces an agentic target-generation pipeline that constructs shared, scenario-specific, and physically grounded attack objectives for each scene, enabling fair comparison of diverse red-teaming methods under aligned adversarial goals. Our evaluation shows that text and typographic injection attacks induce the most failures, multimodal co-optimization yields the strongest visual-perturbation transfer, single-pass attacks approach iterative methods at much lower cost, and model scale alone does not confer adversarial robustness. Code is available at this https URL.

---


### 12. [The Professor: Multi-Teacher Unsupervised Prompt Distillation for Vision-Language Models](https://arxiv.org/abs/2606.23897)

**<font color=#1a73e8>作者：</font>** Ahmad Algadhi, Ahmed Alzuhair, Omar Alkhulaif 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prompt distillation compresses large vision-language models (VLMs) such as CLIP into lightweight student models by matching teacher predictions on unlabeled domain images. PromptKD (CVPR 2024) established this paradigm with a single PromptSRC-finetuned ViT-L/14 teacher and a ViT-B/16 student. We propose TheProfessor, a multi-teacher extension that distills from a fixed two-teacher ensemble: a domain-finetuned PromptSRC ViT-L/14 teacher and a zero-shot EVA-CLIP-L/14 teacher whose logits are pre-computed per dataset. We evaluate single-teacher PromptKD, equal-probability ensembling, and confidence-weighted ensembling on four base-to-novel datasets: Caltech-101, DTD, UCF101, and EuroSAT. In a 12-run single-seed sweep, confidence-weighted ensembling improves average HM from 87.52 to 89.28 (+1.77 points), while equal averaging improves average HM to 88.88 (+1.37 points). Gains are dataset dependent: they are negligible on Caltech-101 (+0.16 HM for confidence weighting), modest on UCF101 (+0.62), and largest on domain-shifted EuroSAT (+5.78). These results update our earlier Caltech-only analysis and show that multi-teacher prompt distillation is most useful when the second teacher contributes complementary supervision under domain shift.

---


### 13. [Do LLM Attribution Metrics Transfer? Auditing Retrieval-Augmented Generation Evaluation Across Datasets and Constructs](https://arxiv.org/abs/2606.23915)

**<font color=#1a73e8>作者：</font>** Tianyu Ding, Aditya Nannapaneni, Juan Pablo De la Cruz Weinstein  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Practice often treats automatic metrics for attribution in LLM retrieval-augmented generation as interchangeable. We audit eight automatic scorers -- lexical, embedding, and BERTScore baselines alongside entailment/grounding-trained models (clean and FEVER NLI, the checker MiniCheck) -- across three evaluation constructs (provenance/topicality, generated-answer attribution, and fact-check entailment), asking whether any scorer transfers: stays within the 95% confidence interval of the best audited scorer on every dataset of a multi-dataset construct. In the construct with the most multi-dataset human-labeled coverage -- generated-answer attribution (AttributionBench's four source datasets, n = 1,610, with independent HAGRID, n = 2,150) -- none does: the per-dataset metric rankings invert (Kendall tau = -0.64, p = 0.031 on AttributedQA vs. LFQA), and an off-the-shelf NLI scorer that is best on short-claim AttributedQA (AUROC 0.90) collapses to AUROC 0.53 (chance) on long-form LFQA, where BERTScore wins (0.91); the flip is not a length or truncation artifact. This instability has a concrete decision cost: a naive "best-on-average" rule for choosing an evaluator fails leave-one-dataset-out (mean held-out regret 0.172 AUROC, worse than fixing one scorer), so metric choice must be validated on the target dataset rather than learned from others. A prompt-based LLM judge avoids the chance-level collapses the automatic scorers suffer (no LFQA collapse) but is not uniformly best, ~100x costlier, and non-deterministic -- relocating, not removing, the validation burden.

---


### 14. [RIFT-Bench: Dynamic Red-teaming For Agentic AI Systems](https://arxiv.org/abs/2606.23927)

**<font color=#1a73e8>作者：</font>** Yarin Yerushalmi Levi, Roy Betser, Amit Giloni 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI systems powered by large language models (LLMs) are rapidly evolving into autonomous decision-making systems, exposing attack vectors beyond those of traditional LLM vulnerabilities. Existing security evaluations are often tied to specific implementations or domains, limiting unified comparison across heterogeneous systems. To address this gap, we introduce RIFT-Bench, a graph representation-driven methodology for dynamic red-teaming that enables unified evaluations across diverse agentic architectures. Building on a novel hierarchical representation, RIFT-Bench operates in two automated phases: Discovery, which extracts system structure, and Scanning, which deploys adaptive adversarial attacks and produces a comprehensive evaluation report. It evaluates the examined system itself, leveraging a broad set of dynamically adaptable adversarial probes across diverse attack vectors and objectives. We demonstrate the effectiveness of the proposed evaluation pipeline across 45 agentic systems spanning a diverse range of implementations, showing that the approach generalizes effectively to heterogeneous agentic architectures. Beyond systems and attacks, RIFT-Bench also supports direct evaluation of mitigation strategies. These key capabilities make RIFT-Bench a scalable foundation for security evaluation of agentic AI systems.

---


### 15. [3D Masked Autoencoders are Robust Learners of Volumetric and Multimodal Cellular Representations for Microscopy](https://arxiv.org/abs/2606.23964)

**<font color=#1a73e8>作者：</font>** Amirhossein Kardoost, Lion Gleiter, Tingying Peng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning in fluorescence microscopy often relies on 2D projections, despite the inherently three-dimensional nature of cells. We present a systematic comparison of 2D and 3D masked autoencoders (MAE-2D vs. MAE-3D) on volumetric microscopy data. Under matched architectures and training protocols, MAE-3D consistently outperforms 2D max-projection and slice-based variants on downstream single-cell tasks. We further align visual representations with a pretrained protein language model (ESM2) and show that cross-modal supervision yields larger gains for volumetric models. Channel cross-attention and frequency-domain regularization are critical for leveraging 3D spatial context. On a protein--protein interaction task, MAE-3D achieves a ROC--AUC of 0.865, outperforming prior methods by up to +0.025. For protein localization, our best 3D model attains state-of-the-art AUC$_{\text{micro}}$ (0.952) and F1$_{\text{micro}}$ (0.742), improving over previous approaches by +0.003 and +0.010 absolute, respectively. Overall, these results demonstrate the advantages of native 3D modeling and multimodal alignment for representation learning in single-cell microscopy.

---


### 16. [Faithful by Construction: Claim-Anchored Attribution for Multi-Document Summarization](https://arxiv.org/abs/2606.23989)

**<font color=#1a73e8>作者：</font>** Shuo Guan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> End-to-end large language models (LLMs) produce fluent multi-document summaries but remain prone to hallucination, and the attributions they offer are typically coarse (whole documents or passages) and generated post hoc, leaving each summary statement hard to verify. We revisit the modular Extract--Select--Rewrite paradigm and recast its intermediate representation as the unit of attribution. We present CAMS, a Claim-Anchored Multi-document Summarization framework that (i) extracts atomic claims with token-level provenance from every source document, (ii) clusters equivalent claims across documents while flagging inter-source conflicts, (iii) selects a support-aware and salient subset, and (iv) rewrites the selection into a summary in which every sentence is anchored to a support-checked claim that links back to one or more source spans. Because content is localized before it is realized, the pipeline is attribution-oriented by construction and faithfulness-oriented by construction: it structurally preserves fine-grained, multi-source traceability while using support-aware selection, constrained rewriting, and verification to encourage, rather than guarantee, factual faithfulness. We evaluate quality, faithfulness, and localization on MultiNews, analyze conflict handling on DiverseSumm, and test zero-shot transfer on WCEP, using a two-regime protocol that separates reference-free citation quality from gold-aligned localization accuracy, and we add an evaluator-decoupled audit that tests citation precision with a support model never used for selection or verification. CAMS matches strong end-to-end and span-attribution baselines on summary quality while substantially improving faithfulness and citation precision, lifting multi-source attribution accuracy by roughly two-thirds, and exposing a controllable faithfulness--coverage trade-off that end-to-end models leave implicit.

---


### 17. [Critique of Agent Model](https://arxiv.org/abs/2606.23991)

**<font color=#1a73e8>作者：</font>** Eric Xing, Mingkai Deng, Jinyu Hou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> What is an agent? What constitutes agency? With the rise of Large Language Model (LLM) systems marketed as ``coding agents'', ``AI co-scientists'', and other ``agentic" tools that promise to drive up productivity, and at the same time, ``existential" concerns such as AI escaping human control with destructive power under a speculative ``machine agency" against humans, it has become essential to clarify where automation ends and agency begins, both for building capable systems and for understanding whether and what to fear. Drawing on Descartes' grounding of agency in independent thought, and on portrayals of autonomous beings in science fiction, we survey the current landscape of AI agents, and analyze agent architectures along five dimensions: goal, identity, decision-making, self-regulation, and learning. Specifically, we argue that genuine agency requires these structures to be \emph{internalized within the system itself} rather than assembled through external scaffolding. This distinction between \emph{agentic} systems, whose competence resides in engineered workflows, and \emph{agentive} systems, whose capabilities (including social interaction) arise endogenously, defines the boundary between systems designed for prescribed tasks, and those capable of operating in the open world with true autonomy. Building on this analysis, we propose the Goal-Identity-Configurator (GIC) architecture for a general-purpose agent model, combining hierarchical goal decomposition, identity evolution, simulative reasoning grounded in a separately trained world model, learned self-regulation, and self-directed learning from both real and simulated experience. Furthermore, we share insight on the auditability, controllability, and safety of agentive systems that possess greater autonomy and ``agency", but remain under human oversight.

---


### 18. [RASC+: Retrieval-Constrained LLM Adjudication for Clinical Value Set Authoring](https://arxiv.org/abs/2606.23992)

**<font color=#1a73e8>作者：</font>** Sumit Mukherjee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical value sets define the standardized terminology codes used in quality measurement, phenotyping, cohort construction, and clinical decision support. The recently introduced Retrieval-Augmented Set Completion (RASC) benchmark showed that direct zero-shot large language model (LLM) generation is poorly suited to this task: clinical code systems are large, version-controlled, and not reliably memorized by language models. We study a stage-wise alternative in which candidate-pool construction is optimized for recall and a constrained LLM adjudicator is optimized for candidate selection. On the full 3,744-value-set RASC test split, Qwen3-based retrieval with vocabulary-aware expansion and code-display rescue retrieval increases candidate-pool recall from the original RASC retrieval baseline of 0.553 to 0.730; on the held-out-publisher stratum, pool recall is 0.655. The higher-recall pool alone is not sufficient: applying the original SAPBert cross-encoder to this expanded pool gives full-test macro F1 of 0.287 and held-out-publisher macro F1 of 0.233. Replacing the stage-2 selector with blinded GPT-5 adjudication over the same pool increases full-test macro F1 to 0.549 and held-out-publisher macro F1 to 0.533. These results show that retrieval-constrained LLM adjudication can substantially improve value set completion while preserving the safety constraint that all returned codes must come from an auditable candidate pool.

---


### 19. [Towards Spec Learning: Inference-Time Alignment from Preference Pairs](https://arxiv.org/abs/2606.24004)

**<font color=#1a73e8>作者：</font>** Dhriti Krishnan, Tejas Goyal, Jaromir Savelka  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Steering a large language model (LLM) toward a desired behavior typically relies on an iterative process of hand-crafting a prompt based on a careful inspection of the model's responses. This is an involved, brittle, and error-prone process. Preference-based fine-tuning is a more rigorous but often prohibitively expensive solution. We propose spec learning, a framework that relies on a brief user instruction and a small set of preference judgments. These are compiled into specifications in the form of natural-language prompts for an LLM. Specifications condition LLMs at inference time, and no parameter updates to the underlying models are required. We show that the responses generated based on the compiled specifications often outperform direct preference optimization (DPO) on datasets from specialized domains whose preference signal is dense. Unlike opaque weight updates, the resulting specifications are human-readable and double as interpretable and transparent written embodiments of the preference signal that produced them.

---


### 20. [Fast and Slow Variational Continual Learning](https://arxiv.org/abs/2606.24007)

**<font color=#1a73e8>作者：</font>** Subarnaduti Paul, Yohan Jung, Mohammad Emtiyaz Khan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning remains a major challenge for modern deep networks, partly because commonly used optimizers lack inherent mechanisms for continual adaptation. One such natural mechanism is fast and slow adaptation to balance stability and plasticity. This mechanism has deep roots in neuroscience and biology, but there is no consensus on how to best incorporate it in commonly used optimizers. Here, we show that this can be easily done via the VCL framework, where past posteriors are used as priors in the future. Our key idea is to incorporate slow adaptation via merging of past posteriors to slow down the drift in the knowledge as learning progresses. The merged posterior is then used as the prior in the VCL update to implement the fast-weight updates. These steps can be seamlessly implemented in the IVON optimizer, whose form and costs are nearly identical to that of Adam. We call this new optimizer the Continual IVON (CoVON) optimizer and show that it not only consistently improves over existing VCL optimizers, but also performs better than other weight-regularization strategies across domain-incremental learning, continual pre-training, and fine-tuning of large language models.

---


### 21. [Token-to-Token Alignment of Text Embeddings for Semantic Blending](https://arxiv.org/abs/2606.24021)

**<font color=#1a73e8>作者：</font>** Saar Huberman, Ron Mokady, Or Patashnik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In modern generative models, images are specified and controlled through text prompts. In practice, images are generated from sequences of tokens derived from these prompts. However, the space of token sequences lacks a consistent accessible structure: semantically similar images may correspond to sequences that differ in wording, ordering, and placement of concepts, while similar token sequences may encode very different semantics. This apparent lack of structure makes it difficult to perform smooth transitions in this space, hindering applications such as image blending and continuous control of edits. We argue that this limitation stems not from the absence of semantic structure, but from misalignment between representations. To address this misalignment, we introduce Token-to-Token alignment, a framework that establishes explicit semantic correspondence between tokens across prompts. Our approach transforms prompts into a structured representation in which semantically corresponding concepts are mapped to consistent positions across prompts, and then aligns their token embeddings based on semantic similarity. Concretely, the method consists of two stages: a structural alignment that rephrases prompts into a shared structured form, followed by an embedding-level alignment that matches token representations across prompts. With this alignment in place, simple linear interpolation becomes a meaningful operation, producing smooth and coherent semantic transitions and enabling applications such as blending and continuous editing. Our results show that text embedding spaces in text-to-image models implicitly encode a continuous semantic structure that becomes accessible once representations are properly aligned, suggesting that semantic control can be achieved by organizing existing representations rather than modifying the generative model.

---


### 22. [Do Language Models Pass the Bechdel Test? Auditing Gender Biases in LLM-Generated Screenplays](https://arxiv.org/abs/2606.24022)

**<font color=#1a73e8>作者：</font>** Megha N. Govindu, Stephanie T. Wang, Sorelle A. Friedler 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are increasingly used in media production from journalistm to filmmaking, what impact do they have on the stories being told? Prior work has shown LLMs to perpetuate social biases, including those related to gender. We complement existing literature on gender bias in LLM outputs by auditing the network structure of LLM-generated movie screenplays through automating the Bechdel test, a popular measure of women's representation in literary and film works. We also introduce the use of social network analysis measures to further analyze representational bias in LLM-generated scripts. We evaluate screenplays generated by three state-of-the-art LLMs (GPT-5, Gemini 3 Pro, and Claude Sonnet 4.5) against 768 corresponding human-written screenplays, finding that human-written scripts are more likely to pass the Bechdel test. However, other network analyses, like centrality, homophily, and triadic relationships demonstrate that in some cases LLM-scripts have less bias, although all script types demonstrate some representational bias under most measures. We conclude by discussing the continued need for further quantitative assessments of media representations and AI-generated content.

---


### 23. [Can Language Model Agents be Helpful Circuit Explainers in Mechanistic Interpretability?](https://arxiv.org/abs/2606.24026)

**<font color=#1a73e8>作者：</font>** Ayan Antik Khan, Harsh Kohli, Yuekun Yao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mechanistic interpretability has made substantial progress in automatically localizing circuits, but explaining what localized components do remains labor-intensive and difficult to standardize. In this work, we study whether language model (LM) agents can assist with this explanation problem once a circuit has already been identified. We introduce AgenticInterpBench, a benchmark for circuit explanation built from 84 semi-synthetic transformer circuits with 163 component-level annotations. We propose HyVE (Hypothesize, Validate, Explain), an agentic explainer that analyzes each component through an iterative loop of observation, hypothesis generation, and causal validation, eventually producing a component-level explanation and a circuit-level task description. Across four LM backbones, HyVE recovers useful component- and task-level explanations, but no backbone is uniformly best. Our analysis shows that strong backbones usually form observation-grounded hypotheses, while failures more often arise later in the validation loop, through incomplete validation plans, code execution errors, or unresolved hypotheses. A case study on an arithmetic circuit in Llama-3-8B shows that the same formulation can extend beyond semi-synthetic benchmarks to naturally trained models. Overall, LM agents are promising circuit explainers, but reliable validation remains the key obstacle.

---


### 24. [RoPE-Aware Bit Allocation for KV-Cache Quantization](https://arxiv.org/abs/2606.24033)

**<font color=#1a73e8>作者：</font>** Fengfeng Liang, Yuechen Zhang, Jiaya Jia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing low-bit KV-cache quantizers often treat each cached key as a flat vector. Under RoPE, however, a key's contribution to a future attention logit decomposes into a position-dependent sum over two-dimensional frequency blocks. This makes key-cache quantization a block-wise bit-allocation problem: high-energy RoPE blocks are more sensitive to quantization error and should receive more bits. We introduce Block-GTQ, a RoPE-aware bit allocator for key-cache quantization built on TurboQuant-MSE(TQ-MSE). For each layer and KV head, Block-GTQ computes a label-free energy score for each RoPE block and greedily allocates integer bit widths by marginal gain. Under matched K/V bit budgets, Block-GTQ better preserves RoPE query-key logits on a ten-model diagnostic panel, cutting per-layer MAE by 32-80% at 2 and 3 b/dim K-only quantization and winning all 367/367 layer comparisons against uniform TQ-MSE. These fidelity gains translate to stronger downstream long-context retrieval, understanding, and reasoning. At K2V2 on Llama-3.1-8B-Instruct, Block-GTQ raises the six-task NIAH average from 70.6 to 97.4, and the LongBench-EN average from 36.87 to 53.31. On AIME 2024/2025 with DeepSeek-R1-Distill-Qwen-7B, without an fp16 recent-key buffer, Block-GTQ at K3V2 scores 51.7/37.5, close to fp16's 54.2/37.9, whereas uniform TQ-MSE collapses to 0.0/0.0. We further implement a packed-cache serving path. On a single H800 GPU with Qwen2.5-3B-Instruct, packed K3V3 achieves 3.24x KV-cache compression with fp16-comparable quality, runs 1.34x faster than fp16 FlashAttention2 at 128K context, reduces peak memory from 56.31 GB to 19.85 GB, and remains feasible at 256K and 512K where fp16 OOMs. Code is available at this https URL.

---


### 25. [DriveStack-VLA: Render-Teacher Alignment for BEV-Based DeepStack Vision-Language-Action Model](https://arxiv.org/abs/2606.24051)

**<font color=#1a73e8>作者：</font>** Jingke Wang, Zhenru Zhao, Shuangming Lei 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action driving models convert a pretrained Vision-Language Model into a driving policy, allowing them to use world knowledge and follow language guidances. However, existing VLA driving models still lack driving-oriented spatial intelligence: their policies are mainly grounded on perspective image tokens and language priors, while precise motion planning requires metric geometry, top-down scene structure, and attention to safety-critical perceptual cues. This limitation makes current models vulnerable to weak visual geometry modeling and perceptual coverage in expert demonstrations. In this paper, we present DriveStack-VLA, a framework built upon a large VLM backbone. To strengthen the spatial grounding of VLA driving, we develop dual visual modeling components. We inject a Bird-Eye-View representation into the Large Language Model decoder through a DeepStack-style connection, and propose Render-Teacher Alignment to align the perceptual focus of real images with that of rasterized images. Furthermore, to bridge the gap in multimodal trajectory selection, we introduce a head-based self-critique module that ranks sampled trajectories and conditionally refines the best one. DriveStack-VLA achieves 91.6 PDMS on NAVSIMv1, 91.0 EPDMS on NAVSIMv2 (with the human penalty filter enabled), and a driving score of 79.49 with a success rate of 56.36\% on the closed-loop Bench2Drive. More visualizations are available on our project page: this https URL.

---


### 26. [Beyond Trajectory Imitation: Strategy-Guided Policy Optimization for LLM Reasoning](https://arxiv.org/abs/2606.24064)

**<font color=#1a73e8>作者：</font>** Tianyuan Shi, Canbin Huang, Bei Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Distilling reasoning capabilities from strong to weak language models typically involves imitating specific solution trajectories, effectively transferring what to answer rather than how to reason. This trajectory-level imitation encourages memorization of instance-specific steps rather than acquisition of transferable problem-solving skills, limiting generalization to novel problems. We propose Strategy-Guided Policy Optimization (SGPO), which replaces instance-level trajectory imitation with reusable strategy distillation. SGPO extracts structured strategy descriptions from strong-model responses and, for each problem, constructs both autonomous and strategy-guided trajectories to enable direct comparison of the model's behavior with and without strategic guidance. The framework then addresses two key questions. For how to distill, a token-level forward-KL objective selectively transfers the distributional shift induced by strategy conditioning into the unguided policy, with proximal constraints ensuring stability. For when to distill, adaptive instance-level weighting strengthens guidance when autonomous exploration falls short and reduces it as the model's own competence grows. Experiments on four mathematical benchmarks across two model families show that SGPO consistently outperforms SFT, on-policy RL, and hybrid-policy baselines, improving the average score by 2.2 points over the strongest baseline on Qwen2.5-7B-Instruct. Analysis reveals that the forward-KL objective provides an inherently selective distillation signal that outperforms direct trajectory imitation, and that strategy distillation exhibits complementary scaling with base model capability.

---


### 27. [Sentence-Level Contextual Entrainment in Large Language Models](https://arxiv.org/abs/2606.24077)

**<font color=#1a73e8>作者：</font>** Yang Liu, Chenhui Chu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Contextual entrainment, which is a newly discovered phenomenon in large language models (LLMs), refers to the tendency of a model to assign higher probabilities to tokens that appear in its context. In this work, we extend this phenomenon from the token level to the sentence level by examining the per-token mean log-probability of a sentence instead of the probabilities of individual tokens. We investigate sentence-level contextual entrainment across 26 LLMs from seven families and two datasets, which cover both subjective and objective tasks. We find that sentence-level contextual entrainment exists. This means that the sentences in the prompt (even if they are counterfactual statements) can significantly increase their probability during model inference time. As the model size increases, contextual entrainment gradually decreases. We also find that contextual entrainment is controlled by 2% to 4% of the attention heads. Turning off these attention heads can effectively mitigate contextual entrainment without hurting the model's performance.

---


### 28. [CAVEWOMAN: How Large Language Models Behave Under Linguistic Input and Output Compression](https://arxiv.org/abs/2606.24083)

**<font color=#1a73e8>作者：</font>** Morayo Danielle Adeyemi, Ryan A. Rossi, Franck Dernoncourt  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> "Talk short. Drop grammar. Save token." This caveman style is widely promoted as a way to cut inference cost, but whether it actually saves anything depends on which channel (the user's prompt or the model's response) is being compressed. We present Cavewoman, a two-channel evaluation protocol that scores every generation on task accuracy, realized per-item cost, and reference-text agreement against the model's unconstrained reference. We evaluate eight models on five datasets at five reduction levels, with both channels measured on the same items. Output compression cuts realized cost on most API models (1.4-2.4x per model, up to 3x in the best case) and on all four open-weight models under public-tier pricing. Input compression has the opposite effect, a strict lose-lose: it raises net cost rather than lowering it (~1.15x on the five-benchmark mean, up to 1.8x on the worst dataset and 2.7x under stronger compression), because models compensate with longer responses even as accuracy collapses. Under the same setting, surface text diverges from the unconstrained reference: on the non-reasoning models, roughly half of all generations are correct yet their surface text no longer entails the model's own unconstrained baseline generation. The divergence survives length-controlled re-scoring, multiple-comparisons correction, and replication under complementary semantic measures. Code and data are available at this https URL.

---


### 29. [Universal Guideline-Driven Image Clustering via a Hybrid LLM Agent](https://arxiv.org/abs/2606.24094)

**<font color=#1a73e8>作者：</font>** Wenliang Zhong, Rob Barton, Lucas Goncalves 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unifying image clustering across different clustering scenarios remains challenging due to fundamental gaps among tasks. We introduce a Guideline-Driven Image Clustering Agent, the first universal framework that bridges these gaps through textual guidelines. To incorporate complex guidelines without task-specific training, we propose Generative Concept Proxy Modeling, which generates guideline-aware embeddings via concept proxy extraction. For scenarios requiring automatic cluster discovery, we introduce LLM Traversal based on Minimum Spanning Tree that selectively applies LLM reasoning for complex semantic judgments. Our method generalizes across diverse clustering scenarios spanning from general to fine-grained categorization, from global to local criteria, and from balanced to long-tail distributions. Our framework consistently outperforms specialized methods across diverse clustering tasks.

---


### 30. [PORTER: Language-Grounded Event Representations for Portable Structured EHR Foundation Models](https://arxiv.org/abs/2606.24102)

**<font color=#1a73e8>作者：</font>** Lin Lawrence Guo, Adam Paul Yan, Emily Vettese 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Most electronic health record (EHR) foundation models encode clinical events as discrete event tokens from a fixed vocabulary and therefore cannot directly represent events containing unseen concepts or new combinations of concepts and attributes such as numeric values. This limits transfer across institutions and even across deployment pipelines within the same institution. We introduce PORTER, a language-grounded structured EHR foundation model that decouples event representation from this fixed vocabulary. PORTER represents events through their descriptions using a frozen text encoder, integrates numeric values through a dedicated pathway, and learns clinical dynamics over patient timelines with an autoregressively pretrained temporal backbone. Across 74 clinical prediction tasks at a pediatric hospital, PORTER matched the mean AUROC of a fixed-vocabulary model with the same temporal backbone and pretraining objective. When the same patient timelines were rendered using event descriptions not seen during pretraining, PORTER transferred without retraining or vocabulary mapping, recovering 97.1% of the mean AUROC of a model trained directly on the target vocabulary. When transferred to MIMIC, PORTER outperformed the fixed-vocabulary model, which dropped 69% of events because their tokens were unseen. Mechanistic analyses showed cross-vocabulary transfer tracked preservation of patient-level representation geometry rather than the scale of the text encoder, and the numeric pathway improved sensitivity to magnitude without disrupting clinical concept identity. PORTER also achieved higher AUROC than a task-specific text serialization comparator, at 329-fold lower amortized compute. PORTER is a step toward vocabulary-independent EHR foundation models that reduce the need for vocabulary harmonization while preserving in-domain performance and enabling efficient cross-task reuse.

---


### 31. [ReMMD: Realistic Multilingual Multi-Image Agentic Verification for Multimodal Misinformation Detection](https://arxiv.org/abs/2606.24112)

**<font color=#1a73e8>作者：</font>** Chenhao Dang, Dantong Zhu, Jun Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal misinformation detection is increasingly important because viral posts now combine long multilingual narratives, several images, mixed provenance, and subtle text--image framing errors. Existing benchmarks and methods remain poorly matched to this setting: they usually isolate short captions, single images, binary labels, or one manipulation source, while agentic verification remains costly under realistic evidence search. We present ReMMD, a realistic multilingual multi-image agentic verification framework for multimodal misinformation detection. ReMMD includes ReMMDBench, a real-world multimodal misinformation detection benchmark with 500 samples, 2,756 images, five monolingual languages, two cross-lingual settings, three text-length tiers, multi-image posts, five-way veracity labels, eight distortion labels, evidence provenance, and rationales. It also includes ReMMD-Agent, a persistent-memory verifier that decomposes posts into atomic points, builds a reusable evidence set, and predicts structured L1/L2/L3 outputs. Across proprietary systems, open LVLMs, MMD-Agent, and T2-Agent, ReMMD-Agent obtains the best five-way veracity performance, with 41.80% accuracy and 39.12% macro-F1 using GPT-5.2, while reducing cost by 17.5% relative to MMD-Agent and 79.9% relative to T2-Agent. The project is available at this https URL.

---


### 32. [A Benchmark for Hallucination Detection in VLMs for Gastrointestinal Endoscopy](https://arxiv.org/abs/2606.24115)

**<font color=#1a73e8>作者：</font>** Aminu Lawal, Niyoj Oli, Sachin Acharya 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are prone to hallucination, which remains a major barrier to their safe deployment in clinical practice. To date, most hallucination detection methods have been evaluated on radiology benchmarks such as MIMIC-CXR and VQA-RAD, while gastrointestinal (GI) endoscopy remains largely underexplored. In this paper, we benchmark nine hallucination detection methods on the Gut-VLM dataset, a GI diagnostic Visual Question Answering (VQA) dataset with 4,392 test VQA pairs, across five VLMs (MedGemma-4B, MedGemma-27B, LLaVA-Med-7B, LLaVA-v1.6-7B, and Lingshu-32B). The methods span three categories: black-box methods (RadFlag, SelfCheckGPT-NLI), gray-box methods (AvgProb, AvgEnt, MaxProb, MaxEnt, Semantic Entropy, and VASE), and a white-box method (ReXTrust). Our results show that ReXTrust, a white-box method, achieves the highest AUC across all five models, outperforming the strongest alternative method on each VLM by a statistically significant margin (paired permutation test, p < 0.001 in all cases), reaching a peak AUC of 93.0 on MedGemma-4B. White-box hidden-state access provides a consistent advantage of 19.5 AUC points on average (range: 9.5--33.5), with ReXTrust maintaining strong performance even on LLaVA-v1.6-7B (AUC 79.9), where black-box methods and clustering-based gray-box methods collapse to near-chance performance. Among non-white-box methods, token-level gray-box statistics (MaxEnt, MaxProb) are the strongest alternatives, outperforming both clustering-based gray-box methods (Semantic Entropy, VASE) and black-box approaches on average. We further identify confident confabulation, a failure mode in which models hallucinate with high inter-sample consistency or high token-level probability, as a systemic failure for both consistency and uncertainty-based methods.

---


### 33. [Flood Mapping from RGB imagery using a Vision Foundation Model](https://arxiv.org/abs/2606.24120)

**<font color=#1a73e8>作者：</font>** Vladyslav Polushko, Tilman Bucher, Ronald Rösch 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Timely, high-resolution maps of flood extent around settlements are essential for emergency response and damage assessment. We consider airborne RGB imagery for flood mapping as it can be collected rapidly at low cost. To produce flood maps, deep learning models for water segmentation are often used. CNN based and small vision transformer models are used. However, they need much data for adaptation to a change of scenery, i.e., another flooding event. Vision foundation models or large vision transformers are known to generalize across domains. Recently, foundation models for Earth observation became available. They are pretrained on satellite data, whose spatial resolution, viewing geometry, and radiometry differ from nadir RGB imagery. Thus, adaptation is required. We investigate how a satellite-pretrained Earth observation foundation model can be adapted to centimeter-scale floodwater mapping from RGB imagery. Specifically, we fine-tune a model we call Prithvi-2.0-UPN consisting of the Prithvi-EO-2.0-600M Vision Transformer combined with a UPerNet decoder for binary water segmentation on two RGB datasets (BlessemFlood21, NeuenahrFlood). In a first experiment we observe that Prithvi-2.0-UPN reaches state-of-the-art results on BlessemFlood21 and NeuenahrFlood, when trained on their datasets. In a second experiment we show that Prithvi-2.0-UPN performs better than state-of-the-art baseline models for transfer to a new flood event (trained on BlessemFlood21, tested on NeuenahrFlood) in a zero-shot setting. However, the performance indicates room for improvement. In this respect, we investigate in a third experiment how performance improves when further fine-tuning the models with small shares of NeuenahrFlood training data: Prithvi-2.0-UPN improves the fastest and reaches almost the performance level when fully trained on NeuenahrFlood, indicating transfer capabilities.

---


### 34. [OmniPath: A Multi-Modal Agentic Framework for Auditing Wheelchair Accessibility](https://arxiv.org/abs/2606.24129)

**<font color=#1a73e8>作者：</font>** ASM Mobarak Hossain, Nadim Mahmud, Vaskar Raychoudhury 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> For a wheelchair user, a standard blue line on a map is often a broken promise. While platforms like OpenStreetMap (OSM) successfully capture where a path is, they frequently fail to convey how it physically feels to travel on it. This information barrier is problematic for wheelchair users. To solve this issue, we present OmniPath, a system that moves from passive mapping to proactive environmental auditing. Our framework fuses the network topology of OSM with the submeter precision of high-density aerial LiDAR (USGS 3DEP) to create a high-fidelity 3D model of the pedestrian environment. Rather than simply routing a user, our agent virtually traverses the network, analyzing the surface in 0.5 meter increments. It rigorously quantifies physical friction points specifically running slope, cross slope, and vertical discontinuities against ADA compliance standards, calculating a weighted severity score to categorize hazards from ``Mild'' to ``Critical.'' To ensure real world reliability, we validated the system against 200 physical ground truth field surveys across the National Mall using stratified random sampling. The framework demonstrated strong diagnostic reliability for high-severity hazards, achieving F1-scores of 0.60 for Severe and 0.58 for critical categories. By automating this micro-scale inspection, OmniPath identifies the ``invisible'' barriers that standard maps miss, effectively transforming a static dataset into accessibility data source that anticipates accessibility challenges before the user ever leaves home.

---


### 35. [Holistic Data Scheduler for LLM Pre-training via Multi-Objective Reinforcement Learning](https://arxiv.org/abs/2606.24133)

**<font color=#1a73e8>作者：</font>** Chenhao Dang, Jing Ma, Mingjie Liao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The composition of training data, governed by the diversity of sources and their mixing strategy, is a cornerstone of Large Language Model (LLM) pre-training. Online Data Mixing (ODM), the technique of adaptively adjusting data mixtures during training, has emerged as a promising direction to improve efficiency. However, existing methods are constrained by their reliance on a singular optimization perspective, which fundamentally overlooks the need for complex LLM pre-training to consider the dynamic data composition from multiple dimensions. To overcome this limitation, we introduce the Holistic Data Scheduler (HDS), a novel online data mixing framework. HDS formulates the data scheduling challenge as a reinforcement learning problem in a continuous control space and leverages the Soft Actor-Critic (SAC) algorithm for its stability and sample efficiency in exploring the high-dimensional policy space. At the core of HDS lies a novel multi-objective, holistic reward function that integrates three critical perspectives: a data-driven reward for quality, a loss-driven reward capturing inter-domain influence, and a model-driven reward based on weight norms. To validate our design and determine its optimal configuration, we conducted systematic experiments on LLMs of various sizes. On The Pile benchmark, HDS reaches the final validation perplexity of the next best method with 44% fewer training iterations. Furthermore, it achieves a 7.2% improvement on the MMLU 0-shot task along with consistent gains on other benchmarks, showcasing its ability to enhance both training efficiency and final model capability.

---


### 36. [AsyncOPD: How Stale Can On-Policy Distillation Be?](https://arxiv.org/abs/2606.24143)

**<font color=#1a73e8>作者：</font>** Wonjun Kang, Kevin Galim, Seunghyuk Oh 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a student on its own rollouts guided by teacher feedback and is becoming increasingly important for large language model (LLM) post-training. Like reinforcement learning (RL), however, OPD faces an on-policy systems bottleneck, as rollouts can dominate training time for reasoning workloads. Asynchronous training pipelines can alleviate this bottleneck by decoupling rollout generation from learner updates, but doing so introduces stale-policy data. While prior work has studied stale data in asynchronous RL, its effects in OPD remain underexplored. We present the first systematic study of staleness in asynchronous OPD, focusing on a practical setting where teacher feedback is implemented through local KL losses and full-vocabulary teacher logits are too expensive to store or transfer, necessitating finite teacher-score caches. We first show that KL direction changes the stale-data problem: teacher-weighted forward KL is more robust to stale rollouts, whereas student-weighted reverse KL is vulnerable. Second, for this vulnerable reverse-KL case, we study whether methods designed to stabilize asynchronous RL can mitigate OPD staleness. In our experiments, they do not improve over a simpler OPD-specific surrogate: recomputing the reverse-KL signal under the current student at learner time. Third, we analyze how finite teacher-score caches create a bias-variance tradeoff for sparse and sampled reverse-KL OPD estimators. This motivates multi-sample Monte Carlo (MC), which preserves MC correctability while reducing one-sample variance. Finally, we present and open-source AsyncOPD, a fully asynchronous OPD training pipeline built from these estimator choices. Experiments show that AsyncOPD improves training throughput by $1.6\times$ to $3.8\times$ over strict synchronous training while reaching comparable accuracy.

---


### 37. [T2D-Bench: Evidence-Gated Evaluation of LLM Outputs for Type 2 Diabetes Using a Multi-Layer Clinical-Lifestyle Knowledge Graph](https://arxiv.org/abs/2606.24145)

**<font color=#1a73e8>作者：</font>** Saba A. Farahani, Hung Cao, Ramesh Jain 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can produce clinically fluent recommendations for type 2 diabetes while failing to satisfy guideline constraints or explicitly justify lifestyle-related glycemic claims. We present T2D-Bench, a reproducible benchmark and evidence-gated evaluation framework for testing whether LLM outputs satisfy explicit, graph-checkable evidence requirements. T2D-Bench is built on a multi-layer clinical-lifestyle knowledge graph that combines a biomedical spine (UMLS, DrugBank, SIDER), computable ADA Standards of Care rules, and lifestyle knowledge connected through a mechanistic bridge to glycemic laboratory effects. Across 100 structured vignettes spanning diagnosis, medication safety, and adversarial lifestyle conflicts, baseline outputs failed benchmark-defined evidence-path checks in 35% of cases for GPT-4o-mini and 33% for GPT-4o. The evidence gate detects unsupported omissions and uses constrained revision to bring outputs into verifier-level compliance with benchmark-defined evidence requirements. These results show that computable evidence constraints can make unsupported clinical omissions explicit, measurable, and correctable in diabetes-focused LLM outputs.

---


### 38. [Autonomous Video Generation with Counterfactual Controllability for Self-Evolving World Models](https://arxiv.org/abs/2606.24152)

**<font color=#1a73e8>作者：</font>** Xin Wang, Wenxuan Liu, Tongtong Feng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing literature claims that video generation essentially is world modelling. On the one hand, the claim is productive because it pushes generative AI beyond static images and toward temporally extended physical scenes. On the other hand, this claim dangerously relies on the belief that scaling visual prediction alone will automatically yield physical agents. We prefer a more accurate statement: video generation models learn a partial, implicit spatiotemporal world model, but not a fully grounded or controllable one. The reason is as follows: a model may generate a plausible video of a drone crossing a forest or a robot arm manipulating a cup, yet still fail to know which variables are controllable, which constraints belong to a particular body and which futures remain valid under intervention. The frontier in essence is not predictive realism alone, instead it emphasizes a self-evolving generative nature that requires the decisive criterion to be counterfactual controllability: the capability of asking what would happen under an action, to test whether the generated future can survive embodiment constraints and to feed the resulting action knowledge back into future imagination (generation). Therefore, in this paper we present a new perspective, i.e., autonomous video generation with counterfactual controllability is one promising way to realize self-evolving world models.

---


### 39. [MedBench v5: A Dynamic, Process-Oriented, and Hallucination-Aware Benchmark for Clinical Multimodal Models](https://arxiv.org/abs/2606.24155)

**<font color=#1a73e8>作者：</font>** Ding Jinru, Jiang Chuchu, Lu Lu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing medical AI benchmarks lack process visibility, atomic skill evaluation, and integrated hallucination detection. We introduce MedBench v5, a redesigned benchmark for clinical multimodal models (language, vision-language, and agent systems) that moves from static QA to dynamic, process-oriented evaluation. MedBench v5 features: (1) a dual-dimensional framework combining Clinical Cognitive Responsiveness (14 sub-dimensions) and Medical Atomic Skills (4 agent environments), covering 63 tasks; (2) three switchable information-flow stressors (omission, contradiction, evidence delay) for factorized degradation analysis; (3) a dynamic process audit protocol with five reasoning nodes that produces model-specific failure fingerprints; (4) hallucination propagation monitoring across initiation, propagation, anchoring, and contradiction interaction-capturing silent hallucination. Experiments on frontier models show that strong overall task performance does not guarantee process stability: stressors mainly disrupt contradiction detection, diagnosis updating, hallucination propagation, and contradiction-based self-correction, while final evidence grounding can remain superficially stable. MedBench v5 provides a unified infrastructure for capability profiling, controllable stress testing, process auditing, and hallucination trajectory analysis in clinical AI evaluation.

---


### 40. [Accelerating Multimodal Large Language Models with Prior-Corrected Token Reduction](https://arxiv.org/abs/2606.24156)

**<font color=#1a73e8>作者：</font>** Zengjie Chen, Yuxiang Cai, Jingcai Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual token reduction has emerged as an effective strategy for accelerating Multimodal Large Language Models (MLLMs). Many existing methods prune tokens by ranking text-visual attention scores. However, we show that attention is often dominated by a model-induced prior: even without textual instruction, MLLMs tend to focus on certain task-agnostic regions. Consequently, the attention scores of instruction-conditioned tokens are suppressed, increasing the risk that these tokens are discarded during pruning. To address this issue, we propose Prior-Corrected Token Reduction (PriorTR), a training-free token reduction method that explicitly separates task-conditioned attention from the model-induced prior. PriorTR estimates the attention map of the prior, and contrasts it with the task-conditioned attention distribution to measure the additional usable information contributed by each visual token. Importantly, PriorTR computes both the model-induced prior and the task-conditioned posterior within a single forward pass by introducing a null token that serves as an instruction-agnostic probe in the attention block. This design avoids duplicated propagation. Extensive experiments across multiple multimodal benchmarks and MLLMs demonstrate that PriorTR consistently improves the trade-off between accuracy and efficiency over strong training-free baselines, particularly under aggressive token budgets.

---


### 41. [BehaviorBench: Benchmarking Foundation Models for Behavioral Science Tasks](https://arxiv.org/abs/2606.24162)

**<font color=#1a73e8>作者：</font>** Jin Huang, Yutong Xie, Wanli Song 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Foundation models have been increasingly applied to behavioral science domains such as psychology, sociology, and economics. While these models show promise in individual tasks such as survey response prediction and human-subject experiment simulation, there remains no systematic understanding of how well they perform across diverse behavioral science tasks, contexts, and populations. We introduce BehaviorBench, a comprehensive benchmark that evaluates foundation models along four core capabilities: (1) behavior prediction and simulation, (2) strategic decision-making, (3) subject-trait inference, and (4) behavioral knowledge application. Crucially, BehaviorBench evaluates model outputs at both the individual and distributional levels, capturing not only per-subject accuracy but also population-level alignment, an essential requirement for behavioral validity. Leveraging the tasks in BehaviorBench, we further develop this http URL-1.5, extending the this http URL family of behavioral foundation models fine-tuned on behavioral data. Our results reveal a considerable gap: proprietary general-purpose models excel at individual-level prediction and knowledge-intensive tasks, whereas behavioral foundation models, fine-tuned on behavioral data, achieve substantially stronger distributional alignment. Notably, this http URL-1.5 leads on distributional metrics and remains competitive on individual-level metrics, suggesting that proper behavioral adaptation can close the gap. Our results highlight the importance of distributional evaluation, establish BehaviorBench as a foundation for developing and assessing behaviorally aligned AI systems, and demonstrate this http URL-1.5's potential for a broad range of behavioral science studies. Our BehaviorBench and this http URL-1.5 models can be accessed via this https URL.

---


### 42. [Spectral Evolution-Guided Token Pruning in Multimodal Large Language Models](https://arxiv.org/abs/2606.24165)

**<font color=#1a73e8>作者：</font>** Bin Chen, Yuxiang Cai, Yadan Luo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reducing visual token redundancy is critical for accelerating Multimodal Large Language Models (MLLMs) without degrading cross-modal reasoning performance. Existing token pruning methods typically rely on single-layer signals, such as attention scores or token similarities, which overlook the cross-layer transformation of visual representations and may exhibit positional bias in multimodal token sequences. To address this limitation, we propose a training-free token pruning framework based on Cross-Layer Spectral Evolution (CLSE). Instead of measuring token importance from single-layer feature magnitudes, CLSE quantifies how token representations evolve across Transformer layers in the frequency domain. This evolution reflects the transition from high-frequency structural details to low-frequency semantic abstractions. We observe that tokens with stronger spectral redistribution across layers are more likely to be semantically active and should therefore be preserved. By modeling cross-layer token dynamics, CLSE provides a stable importance criterion that mitigates positional bias. Extensive experiments on both image and video benchmarks demonstrate that CLSE achieves a superior trade-off between efficiency and accuracy under aggressive token reduction. Across multiple MLLMs, CLSE reduces FLOPs, KV cache memory, and latency while maintaining competitive or improved performance.

---


### 43. [Tri-Efficient Transfer Learning for Point Cloud Videos](https://arxiv.org/abs/2606.24175)

**<font color=#1a73e8>作者：</font>** Yiding Sun, Dongxu Zhang, Jihua Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While point cloud foundation models have significantly advanced point cloud video understanding, existing parameter-efficient fine-tuning (PEFT) methods still suffer from two critical limitations: prohibitive annotation costs for large-scale point cloud datasets and severe memory bottlenecks. In this paper, we aim to mine richer supervision signals from existing data rather than blindly scaling datasets. A further key principle is that the memory footprint of fine-tuning must be drastically reduced compared to full fine-tuning, which remains elusive for current PEFT techniques. Driven by these challenges, we identify three core desiderata: data-, parameter-, and memory efficiency, and present PoinTriE, a unified framework that excels along all three dimensions. For pre-training, pseudo-motion trajectories are synthesized via rigid transformations, paired with text corpora and 2D projections derived from raw point clouds. We then propose a Geometric-Motion Duality Network optimized via multimodal contrastive learning, rigid rotation prediction, and motion distribution divergence to produce dense self-supervision. During fine-tuning, we freeze the pretrained backbone and only update a lightweight Spatio-temporal Side Network built with LoRA units. Equipped with a gradient flow masking strategy, PoinTriE simultaneously reduces memory consumption and parameter overhead. Extensive experiments confirm that PoinTriE establishes new state-of-the-art results on action recognition and semantic segmentation tasks.

---


### 44. [Towards Fast and Effective Long Video Understanding of Multimodal Large Language Models via Adaptive Quasi-Gaussian Sampling](https://arxiv.org/abs/2606.24187)

**<font color=#1a73e8>作者：</font>** Kun Zhang, Chenxin Fang, Tao Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long video understanding remains a daunting challenge for \emph{Multimodal Large Language Models} (MLLMs) due to the excessive computation and memory footprint. Thus, \emph{keyframe selection} is often adopted to mitigate this shortcoming, which however still suffers from low flexibility and high noise due to its hard sampling principle. In this paper, we define video frame selection as a problem of \emph{Quasi-Gaussian Sampling}, and propose an adaptive and training-free approach termed \textbf{\emph{AdaQ}}. Inspired by the $3$-$\sigma$ rule of Gaussian distribution, the objective of AdaQ is to achieve the optimal $3$-$\sigma$ interval for different examples, \emph{i.e.}, a smaller $3$-$\sigma$ interval for the local query and a larger one for the global query, thereby facilitating robust and adaptive frame sampling. To validate AdaQ, we apply it to four MLLMs with three embedding models. The extensive experimental results not only show its obvious performance gains over the default MLLMs and the SOTA keyframe selection methods, \emph{e.g.}, helping Qwen3-VL-8B outperform GPT4o by 15.8\% on average by using only 64 frames, but also confirm its superior robustness and high efficiency for long-video understanding, \emph{e.g.}, \textbf{only 1 hyper-parameter} needs to be set. \textbf{Our code project} is given at \href{this https URL}{this https URL}.

---


### 45. [Navigating User Behavior toward Personalized Multimodal Generation](https://arxiv.org/abs/2606.24196)

**<font color=#1a73e8>作者：</font>** Hengji Zhou, Yufeng Liu, Ye Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern AIGC pipelines deliver high-fidelity images and videos but presuppose a well-formed creation instruction, while end users rarely articulate visual details, leaving generators misaligned with user demand. We study personalized content generation, which turns a user's interaction history into an executable instruction for downstream synthesis, and identify two obstacles: behavior must be encoded in a form legible to language reasoning, and the model must acquire instruction-writing skill absent from both pretraining and behavior data. We propose NaviGen, which represents each item with a dual identifier coupling a collaborative code and a textual code as a behavioral substrate and a semantic bridge in one token stream. On this representation, a two-stage SFT+RL pipeline first distills preference reasoning and instruction writing from evolutionarily searched supervision, then aligns generation with user intent through hierarchical and self-consistent rewards. Experiments across product, game, and short-video domains show that NaviGen improves personalized image and video generation, strengthens next-item prediction, and yields more specific, relevant, and visually generatable instructions. Our code is anonymously released at: this https URL.

---


### 46. [FlowR2A: Learning Reward-to-Action Distribution for Multimodal Driving Planning](https://arxiv.org/abs/2606.24231)

**<font color=#1a73e8>作者：</font>** Xirui Li, Zhe Liu, Xiaoqing Ye 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal driving planning faces a long-standing tension between two paradigms: scoring-based methods benefit from dense reward supervision but are confined to a fixed action vocabulary, while anchor-based methods generate proposals dynamically yet suffer from sparse supervision constrained to a single ground-truth trajectory. In this work, we propose FlowR2A, which resolves this tension by reframing simulation-based rewards from discriminative targets into generative conditions. By learning the reward-conditioned action distribution from dense trajectory-reward pairs with a flow-matching decoder, FlowR2A unifies the dense supervision of scoring-based methods with the proposal generation of anchor-based methods in a single generative model, forcing the model to internalize the correlation between an action and its outcomes in safety, progress, comfort, and rule compliance. To balance hard safety constraints against soft progress objectives, we introduce fine-grained per-timestep reward conditioning and reward noise augmentation. The generative formulation naturally supports controllable test-time sampling via reward guidance and anchored sampling, producing high-quality proposals. FlowR2A achieves state-of-the-art results on the NAVSIM v1 and v2 benchmarks, with multimodal proposals of substantially higher quality than prior methods.

---


### 47. [Latent Visual States for Efficient Multimodal Reasoning](https://arxiv.org/abs/2606.24233)

**<font color=#1a73e8>作者：</font>** Xiuwei Chen, Wentao Hu, Yongxin Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The integration of visual evidence has significantly enhanced the capabilities of large multimodal models. However, this integration predominantly relies on generating discrete outputs (etc., code or box coordinates) to invoke external tools, a process that introduces rigid dependencies and substantial latency. To overcome these limitations, we propose {EVA} (LatEnt Visual StAtes), a novel framework that natively generates continuous latent visual representations. These internal representations manifest as an adaptive sequence of Latent\_slot tokens, serving as intermediate visual thoughts during the reasoning process. These Latent\_slot tokens are then trained end-to-end with the discrete text tokens. This co-optimization, notably, causes extreme policy deviation in the 'transition window' following the Latent\_slot tokens. We develop D-GSPO (Decouple-GSPO) to target this root cause by decoupling the optimization of latent and discrete components. To support SFT, we construct EVA-230K, a high-quality text-image interleaved CoT dataset encompassing a diverse range of real-world scenes, documents, charts and OCR tasks. Extensive experiments across multiple benchmarks confirm that EVA achieves significant performance gains while enhancing inference efficiency.

---


### 48. [Probing the Misaligned Thinking Process of Language Models](https://arxiv.org/abs/2606.24251)

**<font color=#1a73e8>作者：</font>** Kaiwen Zhou, Constantin Venhoff, Jonathan Michala 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models exhibit a growing range of misaligned behaviors such as strategic deception, sandbagging, and self-preservation. As they are increasingly deployed in high-stakes settings, it is critical to reliably detect such behaviors to ensure safe and responsible use. In this work, we propose to monitor misalignment by decomposing it into fine-grained cognitive processes -- misalignment indicators -- and detecting their presence in a model's internal activations via linear probes. We develop a taxonomy of 18 indicators spanning different misaligned behaviors, paired with an automated, meta-plan-guided pipeline that generates multi-turn training conversations. To rigorously evaluate generalization, we construct an out-of-distribution suite combining automated behavioral elicitation, established misalignment benchmarks, and natural benign conversations. Across 5 misaligned behaviors, our probes match a strong LLM judge with 0.935 AUROC on out-of-distribution benchmarks while keeping a low false positive rate on benign traffic. We further perform in-depth analysis to understand the probes and the model's internal representations of misalignment indicators.

---


### 49. [Social Structure Matters in 3D Human-Human Interaction Generation](https://arxiv.org/abs/2606.24255)

**<font color=#1a73e8>作者：</font>** Zhongju Wang, Beier Wang, Yatao Bian 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although text-to-motion generation has achieved strong progress in synthesizing realistic single-person motions from language, extending it to text-driven 3D human-human interaction (HHI) remains non-trivial, as HHI requires modeling the underlying \textbf{social structure} that governs phase progression, actor roles, and inter-actor coordination. In this paper, we formulate HHI generation as a social structure modeling and grounding problem: the model must first infer how an interaction unfolds and how the two actors coordinate their roles, and then realize this structure as continuous, physically plausible, and partner-aware 3D motion. To study how such structure should be modeled, we first examine the capability boundary of large language models (LLMs) for HHI generation. Our analysis shows that LLMs can \textit{think} by recovering phase decompositions and partner-aware roles, but cannot directly \textit{move}, as they fail to generate dynamic, physically plausible, and interaction-aware motion. This motivates our planner-executor paradigm, \textbf{Think with LLM, Move with Motion Skill}. The LLM planner converts implicit interaction semantics into motion-aligned social supervision by decomposing interactions into phases, assigning partner-aware actor roles, and aligning them with motion sequence. The motion executor then grounds the planned social structure into coordinated two-person motion by adapting a pretrained solo motion model with LoRA, previous-phase self-conditioning, and ego-relative partner conditioning. Together, our Solo-to-Social framework bridges social organization and motion realization, producing 3D HHI with improved phase consistency, role alignment, and partner-aware coordination.

---


### 50. [Trimming the Long-Tail of Visual World Modeling Evaluation](https://arxiv.org/abs/2606.24256)

**<font color=#1a73e8>作者：</font>** Bingxuan Li, Yining Hong, Cheng Qian 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physical interactions follow a long-tailed distribution: a set of common and regular interactions dominates human experience and visual data, while a broad spectrum of rare and irregular interactions remains underrepresented. Although recent visual world models, including image and video generation models, achieve impressive realism on existing benchmarks, they primarily focus on simulating common physical interactions. This raises a central question: Do current visual world models internalize and generalize physical principles? In this work, we introduce Tailor-Bench, a benchmark that challenges world models to simulate irregular physical interactions. To enable systematic evaluation, we design three scenario modes that progressively challenge model reasoning: Regular scenarios reflect common tool-task pairs, Unconventional scenarios replace conventional tools with attribute-compatible substitutes to test affordance generalization, and Impossible scenarios introduce attribute-violating tools to probe constraint awareness. Additionally, we design two complementary settings under a unified evaluation protocol: predictive generation requires inferring outcomes without guidance, while descriptive generation specifies the target outcome for faithful realization. Our experimental results reveal a clear long-tail gap in physical world modeling: performance degrades from Regular to Unconventional and Impossible scenarios, indicating limited generalization beyond common interactions. Failure analysis further shows that models rely on superficial visual patterns: image models fail to realize correct state changes, while video models further suffer from temporal inconsistencies.

---


> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-118](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
