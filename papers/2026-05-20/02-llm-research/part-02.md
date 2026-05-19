# 🧠 大模型相关研究 | 2026年05月20日

> 本类共 **346** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-346](./part-07.md)

---

### 51. [MedMIX: Modality-Internal Expert Fusion for Multimodal Medical Diagnosis](https://arxiv.org/abs/2605.16639)

**<font color=#1a73e8>作者：</font>** Seungik Cho, Anqi Li, Wei Qiu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal clinical prediction faces three challenges: multiple foundation models (FMs) with complementary strengths per modality, pervasive missing modalities at training and test time, and sample-specific variation in modality contributions. We introduce MedMIX, a multimodal framework that combines intra-modality expert fusion, learned inter-modality fusion, and training-only large--small model collaboration for robust medical prediction under incomplete modalities. Within each modality, MedMIX aggregates complementary embeddings from multiple small expert models; across modalities, it performs learned fusion over available modalities; and during training, it leverages large teacher models to improve deployed representations without additional inference cost. Across three heterogeneous benchmarks (OpenI, MIMIC-IV-MM, and MMIST-ccRCC), MedMIX achieves consistently strong performance while remaining robust under controlled missing-modality perturbations, and further demonstrates sustained robustness under cross-cohort shift on MIMIC-III. These results highlight MedMIX as a practical framework that unifies within-modality expert collaboration, sample-specific cross-modality fusion, and efficient large--small model collaboration while remaining robust to incomplete modalities.

---


### 52. [Right Predictions, Misleading Explanations: On the Vulnerability of Vision-Language Model Explanations](https://arxiv.org/abs/2605.16651)

**<font color=#1a73e8>作者：</font>** Narges Babadi, Hadis Karimipour  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Explanation mechanisms are increasingly used to support transparency and trust in vision-language models (VLMs), particularly in settings where model decisions require human oversight. However, the robustness of these explanations remains insufficiently understood. In this work, we investigate whether explanation heatmaps in VLMs, particularly CLIP-based models, faithfully reflect model reasoning under adversarial conditions. We show that explanation maps can be systematically manipulated while preserving the model's original prediction, revealing a disconnect between predictive behavior and explanation faithfulness. To study this vulnerability, we introduce X-Shift, a novel grey-box attack that perturbs patch-level visual representations to redirect explanation heatmaps toward semantically irrelevant regions without altering the predicted output. Unlike conventional adversarial attacks that aim to induce misclassification, X-Shift specifically targets the integrity of the explanation process itself. The attack operates without modifying model parameters and generalizes across multiple CLIP architectures and explanation methods. We evaluate the proposed approach on ImageNet-1k, MS-COCO, and Flickr30K, demonstrating consistent degradation in explanation alignment under imperceptible perturbations while maintaining prediction stability. Furthermore, standard prediction-oriented adversarial attacks fail to reproduce the same explanation-shifting behavior even under substantially larger perturbation budgets. Our findings highlight a fundamental limitation of current explanation mechanisms in VLMs and raise concerns about their use as reliable indicators of model trustworthiness in high-impact applications.

---


### 53. [In-context learning enables continental-scale subsurface temperature prediction from sparse local observations](https://arxiv.org/abs/2605.16665)

**<font color=#1a73e8>作者：</font>** Daniel O'Malley, Christopher W. Johnson, Javier E. Santos 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continental-scale knowledge of subsurface temperature is limited by the cost and sparsity of borehole measurements, but such information is essential for geothermal resource assessment and for understanding heat transport in the shallow crust. The thermal field reflects the interaction between lithology, crustal structure, radiogenic heat production, and advective fluid flow, sometimes producing sharp anomalies that are smoothed by conventional interpolation or difficult to capture with physical models. Here we introduce In-Context Earth, a transformer-based model that uses sparse local borehole observations as geological context to predict continuous temperature-at-depth fields with calibrated uncertainty. In the contiguous United States, the model achieves a mean absolute error of 4.7 °C, outperforming the physics-informed Stanford Thermal Model, a model based on AlphaEarth embeddings, the multimodal Transparent Earth model, and universal kriging, while resolving sharper thermal gradients in geothermal provinces. Its uncertainty estimates are well calibrated, with a Kolmogorov-Smirnov statistic of 2.5%. Without finetuning, the model adapts to Alberta, Australia, and the United Kingdom (UK) using only 20 local observations at inference time, maintaining high accuracy in geologically distinct test regions with a mean absolute error of 2.2 °C in Alberta, 6.2 °C in Australia, and 5.4 °C in the UK. Interpretability analyses show that the model learns internal representations of subsurface properties it never observes during training, including seismic velocities, geochemistry, and crustal structure, and uses these representations in physically consistent ways. More broadly, this work shows that in-context learning can use sparse borehole observations for continental-scale subsurface characterization, without requiring dense measurements or region-specific retraining.

---


### 54. [LinAlg-Bench: A Forensic Benchmark Revealing Structural Failure Modes in LLM Mathematical Reasoning](https://arxiv.org/abs/2605.16675)

**<font color=#1a73e8>作者：</font>** Shradha Agarwal, Deepak Rajbhar, Tariq J  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce LinAlg-Bench, a diagnostic benchmark evaluating 10 frontier large language models on structured linear algebra computation across a strict dimensional gradient of 3x3, 4x4, and 5x5 matrices. Spanning 9 task types and 660 SymPy-certified problems, the benchmark exhaustively evaluates 6,600 model outputs. Beyond binary accuracy, LinAlg-Bench introduces a three-stage automated forensic pipeline classifying 1,156 failures into ten primary error tags with fine-grained subtypes, revealing that LLM mathematical failure is not random but structurally constrained by algorithm type and matrix dimension. Our central finding is a sharp behavioral threshold at 4x4 scale: below it, models fail through execution errors -- sign tracking failures, arithmetic drift, and parity errors; above it, failure transitions to computational abandonment, with models fabricating responses through tool roleplay, constraint-consistent confabulation, and structured hallucination rather than attempting computation. This fabrication-to-abandonment transition is near-universal across all model tiers and architectures, suggesting a working memory limit rather than a knowledge gap, supported by three scale-emergent error types absent at 3x3 but present at 4x4 and 5x5. We further show that solution strategy rigidity is a near-perfect predictor of 5x5 determinant accuracy, document constraint-aware confabulation as a novel structured hallucination failure mode, and release all data, model outputs, error labels, and judge pipeline publicly.

---


### 55. [Enhancing Metacognitive AI: Knowledge-Graph Population with Graph-Theoretic LLM Enrichment](https://arxiv.org/abs/2605.16676)

**<font color=#1a73e8>作者：</font>** Deniz Askin, Gal Hadar, Brendan Conway-Smith  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Metacognition-the ability to monitor one's own knowledge state, spot gaps, and autonomously fill them--remains largely absent from modern AI. Here, we present MetaKGEnrich, a fully automated pipeline that endows large language model (LLM) applications with self-directed knowledge repair. The system (i) builds knowledge graphs from a seed query, (ii) detects sparse regions via seven graph metrics, (iii) has GPT-4o generate targeted questions, (iv) retrieves web evidence with Tavily and ingests it into Neo4j, and (v) re-answers the query with GraphRAG for GPT-4 to evaluate improvement. Tested on 30 queries from each of three widely-used datasets: Google Research Natural Questions, MS MARCO, and Hot-potQA. MetaKGEnrich improved answer quality in 80% of HotpotQA questions, 87% of Google Research Natural Questions and 83% of MS MARCO questions, while preserving well-supported regions. This proof of concept demonstrates how topological self-diagnosis plus targeted retrieval can advance AI toward humanlike metacognitive learning.

---


### 56. [Scalable Knowledge Editing for Mixture-of-Experts LLMs via Tensor-Structured Updates](https://arxiv.org/abs/2605.16686)

**<font color=#1a73e8>作者：</font>** Roman Maksimov, Vladimir Aletov, Dmitry Bylinkin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge editing (KE) provides a lightweight alternative to repeated fine-tuning of LLMs. However, most existing KE methods target dense feed-forward layers, while modern LLMs increasingly adopt Mixture-of-Experts (MoE) architectures for their superior memory footprint and inference efficiency. This mismatch leaves a growing class of production models without principled editing tools. We propose a MEMIT-like framework for knowledge editing in MoE-based LLMs. Our method exploits the tensor structure of MoE layers to formulate the editing objective faithfully at the per expert level, and applies the Woodbury matrix identity to avoid materializing or inverting the full stacked matrix of expert weights. The resulting update reduces to inversions of fixed low-rank matrices and requires no additional backward passes. Empirically, our approach matches the editing quality of strong baselines on the main KE metrics while accelerating the editing procedure by up to 6x, owing to the batched MEMIT-style formulation and the low-dimensional inversions enabled by the Woodbury identity. These results show that closed-form, parameter-modifying KE can be extended efficiently beyond dense layers, opening a path toward scalable knowledge editing in modern sparse LLM architectures.

---


### 57. [UB-SMoE: Universally Balanced Sparse Mixture-of-Experts for Resource-adaptive Federated Fine-tuning of Foundation Models](https://arxiv.org/abs/2605.16690)

**<font color=#1a73e8>作者：</font>** Van-Tuan Tran, Hong-Hanh Nguyen-Le, Marco Ruffini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Heterogeneous LoRA-rank methods address system heterogeneity in federated fine-tuning of foundation models by assigning client-specific ranks based on computational capabilities. However, these methods achieve only marginal computational savings, as dense feed-forward computations dominate. Sparse Mixture-of-Experts (SMoE) provides a promising alternative through conditional computation, yet we identify that its naive application to heterogeneous federated settings introduces two critical discordances: (i) expert utilization imbalance and (ii) non-differentiability of Top-K routing. Our convergence analysis demonstrates that these discordances lead to degraded convergence, particularly for resource-constrained clients. To address these challenges, we propose Universally Balanced Sparse Mixture-of-Experts (UB-SMoE), which introduces Dynamic Modulated Routing (DMR) to rebalance expert utilization, and Universal Pseudo-Gradient (PG) to reconstruct learning signals for non-activated experts. These mechanisms form a self-reinforcing cycle that maintains expert viability across heterogeneous clients. Experiments on benchmarks show that UB-SMoE achieves up to $45.0\%$ computational reduction on low-resource clients while improving their performance by $8.7 \times$ compared to existing heterogeneous LoRA-rank methods.

---


### 58. [Convex Dataset Valuation for Post-Training](https://arxiv.org/abs/2605.16704)

**<font color=#1a73e8>作者：</font>** Siqi Zeng, Christopher Jung, Rui Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Improving LLM performance on downstream tasks sometimes requires leveraging auxiliary datasets during post-training. In practice, however, developers face constraints on compute, labeling, and licensing costs that preclude using all available data, necessitating principled dataset-level selection. These constraints are increasingly shaped by dataset marketplaces, where data acquisition is governed by budgets and negotiation. We study dataset valuation as a subset selection problem during LLM post-training. Our goal is to identify and weight auxiliary datasets so as to maximize target task performance given constrained budgets. We first show that commonly used gradient alignment scores provide a reasonable yet incomplete valuation signal, as they ignore redundancy among datasets. To address this, we propose a scalable convex dataset-level valuation method based on kernel mean matching (KMM) in gradient space, which jointly accounts for alignment with the target task and redundancy across auxiliary datasets. Through extensive experiments across diverse post-training settings and tasks, we show that our approach consistently outperforms existing valuation baselines, achieving stronger performance with low computational overhead. Our results position dataset valuation as a practical decision tool for post-training data selection in market-constrained large language model settings. The code is available at this https URL.

---


### 59. [GeoWorld-VLM: Geometry from World Models for Vision-Language Models](https://arxiv.org/abs/2605.16713)

**<font color=#1a73e8>作者：</font>** Renjie Gu, Kaichen Zhou, Yan Luo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern Vision-Language Models (VLMs) achieve strong semantic recognition, yet remain brittle on elementary spatial relations such as left of, on, behind, and between. One cause of this failure arises before language reasoning begins: the visual pathway may compress or discard critical 3D structural cues during feature extraction, so the language model receives image representations that are already insufficient for reliable spatial judgment. We introduce GeoWorld-VLM, a VLM-side distillation framework that transfers geometric structure from frozen camera-conditioned video world models into VLMs. GeoWorld-VLM fine-tunes only the image encoder and multimodal projector, aligning post-projector image features with intermediate world-model representations while leaving the main backbone frozen. Given images, a prompt, and a sampled camera trajectory, the world-model teacher converts static visual input into a synthetic multi-view spatial signal. Training combines spatial answer supervision, teacher-student feature alignment, and a preservation anchor to the original VLM. Since the language model remains frozen, GeoWorld-VLM preserves the original model's linguistic capabilities while attributing spatial improvements to the enhanced visual pathway. To evaluate the effectiveness and generality of the proposed method, we apply GeoWorld-VLM to two distinct VLM architectures and observe consistent improvements across both backbones. GeoWorld-VLM improves performance by approximately 4 percent on both the What'sUp and VSR benchmarks, suggesting that world-model-guided visual alignment generalizes across model structures and spatial reasoning datasets.

---


### 60. [GRID: Graph Representation of Intelligence Data for Security Text Knowledge Graph Construction](https://arxiv.org/abs/2605.16714)

**<font color=#1a73e8>作者：</font>** Liangyi Huang, Zichen Liu, Fei Shao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Security knowledge graphs can provide computable external memory for security agents, but constructing them from long-form cyber threat intelligence (CTI) remains difficult: LLMs often lack grounded security-domain knowledge, and end-to-end document-to-graph training is hard to supervise with cheap, stable rewards. We present GRID (Graph Representation of Intelligence Data), an end-to-end framework for security text knowledge graph construction. GRID first builds security-domain supervision from CTI articles by creating traceable article-graph alignments through graph extraction and knowledge-graph-conditioned text revision. It then turns document-to-graph learning into a scripted task bank combining four-option multi-select questions with triple-level regex matching targets, yielding more stable task-specific rewards than repeatedly scoring full graph outputs with an LLM judge. Using this supervision pipeline, we train two Qwen3-4B-Instruct-2507-based 4B extractors: a primary Task-bank Reward model and a secondary End2End Reward model with LLM-as-judge precision/recall rewards. On 249 CTI articles from GRID, CASIE, CTINexus, MalKG, and SecureNLP, the Task-bank Reward model with the ontology-guided GRID extraction pipeline reaches 84.62% source-averaged precision, 64.91% source-averaged recall, and 68.53% Avg F1, achieving the best source-averaged recall and near-top Avg F1 with lower token usage and deployment cost. The End2End Reward model reaches 76.91% precision, 53.85% recall, and 58.06% Avg F1. Further analyses show that task-bank rewards can be built once offline and reused across later post-training runs, outperforming online End2End LLM-as-judge reward and weaker alternatives such as Choice-only Reward and End2End SFT without RL.

---


### 61. [Baba in Wonderland: Online Self-Supervised Dynamics Discovery for Executable World Models](https://arxiv.org/abs/2605.16725)

**<font color=#1a73e8>作者：</font>** SeungWon Seo, DongHeun Han, SeongRae Noh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Executable world models can be read, edited, executed, and reused for planning, but only if the program captures the environment's transition law rather than semantic shortcuts in its surface vocabulary. We study online executable world-model learning under prior misalignment, where an agent must induce state-dependent dynamics from interaction evidence alone, without rule descriptions, reward signals, or trustworthy lexical priors. We introduce Alice, a closed-loop system that treats failed candidate updates as structural signal: when a candidate explains a new transition but loses previously explained ones, the preservation conflict reveals dynamics that the current program had conflated. Alice refines these conflicts into hypothesis classes that both provide compact, class-stratified preservation counterexamples for update and guide frontier exploration toward transitions that are novel and underrepresented with respect to the current program. We evaluate Alice on Baba in Wonderland, a prior-misaligned variant of Baba Is You that preserves simulator dynamics while replacing semantically meaningful rule-property labels with unrelated words. Experiments show that Alice substantially improves executable world-model learning under prior misalignment, and ablations show that both class refinement and class-aware exploration contribute.

---


### 62. [PopuLoRA: Co-Evolving LLM Populations for Reasoning Self-Play](https://arxiv.org/abs/2605.16727)

**<font color=#1a73e8>作者：</font>** Roger Creus Castanyer, Geoffrey Bradway, Lorenz Wolf 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce PopuLoRA, a population-based asymmetric self-play framework for reinforcement learning with verifiable rewards (RLVR) post-training of LLMs. Teachers and students are specialised LoRA adapters on a shared frozen base: teachers propose problems, matched students solve them under a programmatic verifier, and cross-evaluation between sub-populations replaces the self-calibration that limits single-agent self-play. A family of LoRA weight-space evolution operators (mutations and crossovers that produce same-rank population members in seconds) serves as the replacement step of a population-based training loop at 7B scale. We instantiate PopuLoRA on top of Absolute Zero Reasoner and compare it against a per-adapter compute-matched single-agent baseline. Where the single agent self-calibrates to generating easy problems it can reliably solve, the population enters a co-evolutionary arms race: teachers produce increasingly complex problems, student solve rates oscillate, and problem-space coverage keeps expanding throughout training. Despite lower training-time reward, the population mean outperforms the baseline on three code benchmarks (HumanEval+, MBPP+, LiveCodeBench) and seven math benchmarks (AIME 24/25, AMC 23, MATH-500, Minerva, GSM8K, OlympiadBench), and even the weakest member of the population beats the baseline on aggregate.

---


### 63. [TRACE: Evidence Grounding-Guided Multi-Video Event Understanding and Claim Generation](https://arxiv.org/abs/2605.16740)

**<font color=#1a73e8>作者：</font>** Pengyu Yan, Akhil Gorugantu, Mahesh Bhosale 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-video event understanding demands models that can locate and attribute query-relevant evidence scattered across long, heterogeneous video corpora. Existing large vision-language models (LVLMs) often underperform in this regime because they quickly exhaust their context budget and struggle to precisely localize evidentially important segments, frequently missing dense informational cues such as broadcast graphics, subtitles, and scoreboards. We introduce TRACE, an evidence grounding-guided framework that follows a ground-before-reasoning strategy for multi-video event reasoning. Our approach first builds a structured, text-searchable timeline for each video using OCR and object detection. A text-only LLM then conducts query-aware evidence localization, selecting relevant moments prior to any downstream visual reasoning. The retrieved frames and their grounding summaries are subsequently used to steer LVLM-based claim generation and cross-video citation consolidation. Experiments on MAGMaR 2026 and WikiVideo demonstrate that structured grounding markedly boosts factual completeness and attribution fidelity. On the MAGMaR validation split, TRACE raises macro-average MiRAGE F1 from 0.705 to 0.811 compared to an unguided Qwen3-VL-30B baseline, with especially strong improvements in citation recall from 0.440 to 0.628. The method also attains state-of-the-art results on the official MAGMaR 2026 leaderboard.

---


### 64. [Diffeomorphic Cortical Alignment via Direct Warping of Streamline Endpoints](https://arxiv.org/abs/2605.16742)

**<font color=#1a73e8>作者：</font>** Yang Xiang, Martin Cole, Zhengwu Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cortical surface registration is often driven by local geometric descriptors (e.g., sulcal depth and curvature). While this approach achieves geometric correspondence, it neglects the long-range wiring constraints imposed by white-matter anatomy. Diffusion MRI tractography offers these crucial constraints; however, prior connectivity-informed pipelines typically align precomputed connectivity matrices, making the optimization highly sensitive to connectivity estimation and its resolution. In this paper, we introduce a novel connectivity-based surface registration method that aligns cortical surfaces by operating directly on white-matter fiber-tract endpoints. We model tract endpoints as a point cloud on the product manifold $\Omega \times \Omega$, where $\Omega$ represents the spherical domain of the inflated cortical hemispheres. Our alignment method iteratively (i) computes a small diffeomorphic warp for $\Omega$ by minimizing connectivity mismatch, and (ii) updates the endpoints based on this warp. The method relies on a geometric framework that ensures output warps are diffeomorphisms and has a final goal that optimizes the matching of well-known fiber bundles. Experiments on Human Connectome Project (HCP) data demonstrate improved tract-level correspondence, achieving higher connectivity-level overlap coefficients on major fiber bundles and stronger robustness across grid resolutions for $\Omega$ compared to state-of-the-art methods such as ENCORE and MSMAll.

---


### 65. [EVA01: Unified Native 3D Understanding and Generation via Mixture-of-Transformers](https://arxiv.org/abs/2605.16745)

**<font color=#1a73e8>作者：</font>** Zongyuan Yang, Mingjing Yi, Wanli Ma 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper addresses the challenge of integrating 3D meshes as a native modality within Multimodal Large Language Models (MLLMs). Diffusion-based large reconstruction models decouple semantic understanding from geometric reasoning, operating as stateless reconstructors conditioned on dense 2D pixel priors. Recent MLLM-based methods treat the 3D modality as an external output rather than a native component of the multimodal sequence, making incremental adaptations without a systematic analysis of how geometric manifolds align with MLLM feature spaces. We introduce EVA01, a unified framework that extends the modality boundary of MLLMs to natively incorporate 3D mesh understanding, generation, and context-aware editing. Built upon a Mixture-of-Transformers (MoT) architecture, EVA01 decouples the model into a pre-trained Understanding Expert ($E_{\mathrm{und}}$) and a structurally mirrored Generation Expert ($E_{\mathrm{gen}}$), coupled through shared global self-attention with hard modality routing. This design aligns the semantic latent space of the MLLM backbone with the geometric manifold, enabling direct transfer of multimodal priors without intermediate 2D representations. Results show that EVA01 achieves state-of-the-art native text-to-3D generation fidelity and unlocks robust long-context multi-turn geometric editing with identity preservation, a capability fundamentally inaccessible to stateless reconstruction pipelines. Our findings further offer architectural insights for integrating 2D foundation models with 3D tasks, informing the design of 3D-native multimodal systems. Project Page: this https URL

---


### 66. [State Contamination in Memory-Augmented LLM Agents](https://arxiv.org/abs/2605.16746)

**<font color=#1a73e8>作者：</font>** Yian Wang, Agam Goyal, Yuen Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly rely on persistent state, including transcripts, summaries, retrieved context, and memory buffers, to support long-horizon interaction. This makes safety depend not only on individual model outputs, but also on what an agent stores and later reuses. We study a failure mode we call memory laundering: toxic or adversarial context can be compressed into memory summaries that no longer appear toxic under standard detectors, while still preserving hostile framing or conflict structure that influences future generations. Using paired counterfactual multi-agent rollouts, we show that toxic-origin memory summaries can remain below common toxicity thresholds while nevertheless increasing downstream toxicity relative to matched neutral baselines. To measure this hidden influence, we introduce the sub-threshold propagation gap (SPG), which quantifies downstream behavioral differences conditioned on memory states that a deployed monitor would classify as safe. Our experiments show that toxicity propagates through distinct state channels: raw transcript reuse drives overt downstream toxicity, while compressed memory carries hidden sub-threshold influence. We further find that mitigation depends critically on intervention placement. Sanitizing toxic state before summarization substantially reduces the hidden propagation gap, whereas cleaning only the completed summary can leave laundered influence intact. These results suggest that safety in memory-augmented agents should be treated as a state-control problem over evolving context, with sanitization applied before unsafe information is compressed into persistent memory.

---


### 67. [Language Acquisition Device in Large Language Models](https://arxiv.org/abs/2605.16758)

**<font color=#1a73e8>作者：</font>** Masato Mita, Taiga Someya, Ryo Yoshida 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) remain substantially less data-efficient than humans. Pre-pretraining (PPT) on synthetic languages has been proposed to close this gap, with prior work emphasizing highly expressive formal languages such as $k$-Shuffle Dyck. Inspired by the Language Acquisition Device (LAD) hypothesis, which posits that innate constraints preemptively restrict the learner's hypothesis space to natural-language-like structure, we propose LAD-inspired PPT: pre-pretraining on MP-STRUCT, a formal language whose strings encode hierarchical composition, feature-based dependencies, and long-distance displacement via MERGE, AGREE, and MOVE. A brief 500-step PPT with MP-STRUCT matches strong formal-language baselines in token efficiency while additionally imparting a human-like resistance to structurally implausible languages (e.g., REVERSE). Analyzing simplified variants, we find that MP-STRUCT CORE outperforms $k$-Shuffle Dyck despite not being definable in C-RASP (a formal bound on transformer expressivity), challenging the prior hypothesis that effective PPT languages must be both hierarchically expressive and circuit-theoretically learnable. We show that functional landmarks, which reduce dependency resolution ambiguity, are a key driver, suggesting that effective PPT design depends not only on expressivity but also on the accessibility of dependency resolution.

---


### 68. [Retrieval-Based Multi-Label Legal Annotation: Extensible, Data-Efficient and Hallucination-Free](https://arxiv.org/abs/2605.16767)

**<font color=#1a73e8>作者：</font>** Li Zhang, Jaromir Savelka, Kevin Ashley  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-label legal annotation requires assigning multiple labels from large, evolving taxonomies to long, fact-intensive documents, often under limited supervision. Parametric encoders typically require task-specific training and retraining when the label set changes, while prompting generative large language models becomes costly and degrades as the label space grows. We cast legal annotation as retrieval: we embed documents and label descriptions with a frozen retrieval model and predict labels via k-nearest neighbors in the embedding space, enabling updates by re-embedding and re-indexing rather than gradient-based backpropagation. Across three legal datasets (ECtHR-A, ECtHR-B, and Eurlex with 100 labels), retrieval achieves competitive accuracy and strong data efficiency; on Eurlex, Qwen-8B retrieval improves Macro-F1 from 40.41 (GPT-5.2, zero-shot) to 49.12 while reducing estimated compute by 20-30 times compared to fine-tuning. With only (N=100) training samples, retrieval nearly doubles Micro-F1 over hierarchical Legal-BERT on ECtHR-A (48.29 vs. 27.87). We also quantify a reliability failure mode of generative inference: GPT-5.2 hallucinates labels outside the provided taxonomy in 0.12-0.9% of test samples under deterministic decoding. In contrast, retrieval strictly respects defined label sets, eliminating hallucination by design. These results suggest retrieval-model-based annotators are a practical, deployable alternative for high-cardinality and rapidly changing legal label spaces.

---


### 69. [GLT-PEFT: Gated Lie-Tucker Parameter-Efficient Fine-Tuning for Alzheimer's Disease Diagnosis with Hippocampal Segmentation Pretraining](https://arxiv.org/abs/2605.16769)

**<font color=#1a73e8>作者：</font>** Guanghua He, Hancan Zhu, Gaohang Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient fine-tuning (PEFT) has emerged as a promising paradigm for adapting pretrained models under limited data conditions. However, most existing PEFT methods are designed for matrix-structured parameters and are not well suited for high-dimensional convolutional kernels in medical imaging models. Moreover, they typically rely on additive updates and lack mechanisms to preserve the geometric structure of pretrained parameters, while multiplicative (geometry-aware) updates are difficult to integrate within a unified framework. To address this issue, this paper proposes GLT-PEFT, a gated Lie-Tucker parameter-efficient fine-tuning framework for Alzheimer's disease (AD) diagnosis. The proposed approach transfers a hippocampal segmentation pretrained model to a downstream classification task. Tucker decomposition enables tensor-aware low-rank adaptation of 3D convolutional kernels, while Lie group-based transformations provide structure-preserving multiplicative updates. A gating mechanism further reconciles additive and multiplicative update forms, resulting in a unified and more stable fine-tuning strategy. Extensive experiments demonstrate that GLT-PEFT achieves effective cross-task transfer while significantly reducing trainable parameters, highlighting its effectiveness for efficient and robust adaptation in medical imaging models.

---


### 70. [Exploring Lightweight Large Language Models for Court View Generation](https://arxiv.org/abs/2605.16770)

**<font color=#1a73e8>作者：</font>** Zhitian Hou, Tianyong Hao, Nanli Zeng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Criminal Court View Generation (CVG) is a critical task in Legal Artificial Intelligence (Legal AI), involving the generation of court view based on case facts. In this work, we systematically explore the capabilities of lightweight (smaller than 2B) large language models (LLMs) in CVG and their impact on charge prediction. Our study addresses four key questions: (1) how does different architecture of LLMs affect the CVG quality and charge prediction. (2) how does LLMs size contribute to the performance, (3) how do lightweight LLMs compare with Deep Neural Networks (DNNs) in these tasks, and (4) how does predicting charge by court view generation first compare with predicting it directly. Additionally, we also develop CVGEvalKit, an evaluation framework including three public available datasets for CVG tasks, as well as predicting their charges. Comprehensive experiments are conducted on this framework, where models are trained on a mixed training set and evaluated on each dataset's test set. Experimental results provide new insights into the trade-offs between model architecture, model size, and the influence between different tasks, highlighting the potential of lightweight LLMs in judicial AI applications. The source code is anonymously available at \url{this https URL}

---


### 71. [VolTA-3D: Self-Supervised Learning for Brain MRI using 3D Volumetric Token Alignment](https://arxiv.org/abs/2605.16775)

**<font color=#1a73e8>作者：</font>** Amy Makawana, Abhijeet Parida, Marius George Linguraru 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning (SSL) has advanced medical image analysis be enabling learning form large unlabelled data. However, in brain magnetic resonance imaging (MRI), most 3D models remain specialized for either segmentation of classification, limiting their ability to generalize across datasets, imaging protocols,, and downstream tasks. This lack of transferability constrains the clinical utility of 3D MRI models, despite the availability of unlabeled volumetric data. We present Volta-3D, a self-supervised 3D Vision Transformer framework designed to learn transferable volumetric representations. Volta-3D jointly aligns global class-style tokens and local patch tokens within a student-teacher paradigm and enforces fine-grained structural reconstruction. This combined global-local alignment addresses the limited semantic diversity and subtle anatomical characteristics of brain MRI, which challenges existing SSL approaches. We evaluate Volta-3D on multiple out-of-distribution downstream tasks, including hippocampal segmentation and classification of sex and Alzheimer's disease versus healthy controls. Across all tasks, representations learned by Volta-3D outperform randomly initialized baselines, demonstrating improved transferability and robustness under domain shift. Hence jointly enforcing global semantic consistency and local structural learning during pretraining enables broader concept learning from unlabeled brain MRI data. Overall VolTA-3D supports effective multi-task downstream performance with task-specific pertaining, a step towards generalizable and clinically viable 3D models.

---


### 72. [Distinguishable Deletion: Unifying Knowledge Erasure and Refusal for Large Language Model Unlearning](https://arxiv.org/abs/2605.16776)

**<font color=#1a73e8>作者：</font>** Puning Yang, Junchi Yu, Qizhou Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mitigating sensitive and harmful outputs is fundamental to ensuring safe deployment of LLMs. Existing approaches typically follow two paradigms: Knowledge Deletion (KD), which erases undesirable information during training, and Distinguishable Refusal (DR), which steers models away from using sensitive knowledge during inference. Despite rapid progress, KD-based unlearning struggles with biased deletion due to suppressing specific token sequences as a substitute for complete knowledge removal, whereas DR-based unlearning risks the re-emergence of harmful knowledge because the underlying knowledge remains intact. To address these issues, we propose Distinguishable Deletion ($\mathrm{D^2}$), a paradigm that restricts the response distribution in the latent representation rather than specific tokens to erase undesirable knowledge, while distinguishing it from retained knowledge, enabling a refusal mechanism to handle unlearned inputs safely and coherently. To implement $\mathrm{D^2}$, we introduce an energy index that quantifies the presence of knowledge and the separation between unlearned and retained content. Mathematical and empirical analyses show that energy is both accurate and efficient, enabling Energy-based Unlearning Alignment (EUA) to enforce energy-boundary unlearning during training and apply an energy-based refusal mechanism at inference. Extensive experiments demonstrate that EUA significantly outperforms previous methods, indicating the superiority of $\mathrm{D^2}$. Our code is available at this https URL.

---


### 73. [Lever: Speculative LLM Inference on Smartphones](https://arxiv.org/abs/2605.16786)

**<font color=#1a73e8>作者：</font>** Tuowei Wang, Fengzu Li, Yanfan Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly needed for interactive mobile applications, but high-quality models exceed the limited DRAM available on smartphones. Flash storage can hold larger models, yet flash-backed inference is slow because autoregressive decoding repeatedly invokes the target model and incurs costly I/O. We observe that speculative decoding is a natural fit for this setting: a small draft model can remain in DRAM, while a larger flash-resident target model verifies multiple candidate tokens per invocation. However, existing methods assume server-class accelerators and fail to account for prolonged I/O latency, limited computation parallelism, and irregular speculation execution.
We present Lever, an end-to-end system for efficient flash-backed LLM inference on smartphones. Lever jointly optimizes the three stages of speculative decoding under mobile constraints. For drafting, it builds token trees using an I/O- and compute-aware gain-cost objective. For verification, it prunes low-value branches through early-exit prediction to reduce target-model computation. For execution, it maps speculation efficiently across mobile CPU-NPU hardware to improve utilization. Comprehensive evaluations show that Lever reduces inference latency by an average of 2.93x over baseline flash-offloaded inference and 1.50x over conventional speculative decoding, narrowing the latency gap between flash-backed and memory-resident LLM inference.

---


### 74. [The Unlearnability Phenomenon in RLVR for Language Models](https://arxiv.org/abs/2605.16787)

**<font color=#1a73e8>作者：</font>** Yulin Chen, He He, Chen Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Reward (RLVR) has proven effective in improving Large Language Model's (LLM) reasoning ability. However, the learning dynamics of RLVR remain underexplored. In this paper, we reveal a counterintuitive phenomenon: among hard examples that the model initially struggles with, a substantial subset remains unlearnable even when correct rollouts are present. To understand the phenomenon, we first demonstrate that existing optimization and sampling techniques fail to resolve unlearnability. With cross-example gradient analysis, we show that unlearnable examples have fundamental representation issue, characterized by low gradient similarity with the rest of the examples and ungeneralizable reasoning patterns. We further show that representation flaws are difficult to mitigate in RL, as data augmentation does not improve gradient similarity. Our study provides the first systematic characterization of unlearnable data in RLVR training and reveals fundamental limitations in current RL approaches for reasoning tasks. Code and data are available at \url{this https URL}.

---


### 75. [Cross-Domain Molecular Relational Learning: Leveraging Chemical Structure-Activity Analysis](https://arxiv.org/abs/2605.16799)

**<font color=#1a73e8>作者：</font>** Peiliang Zhang, Jingling Yuan, Shiqing Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in molecular representation integrates molecular topological and visual modalities, opening new avenues for precise Molecular Relational Learning (MRL). Existing MRL methods focus on intra-domain modeling, and their inherent domain-closed effect limits applicability to molecular science, particularly in elucidating cross-domain interaction mechanisms. Consequently, the imperative for Cross-Domain Molecular Relational Learning has become increasingly pressing. Benefiting from structure-activity analysis, we propose the Domain Adversarial Training Network with Structural-Semantic Transfer Discrepancy (DisTrans) to optimize cross-domain adaptive representation for molecular structures and visual images. 1) We employ the gradient reversal strategy based on substructure topological discrepancies between domains to learn the domain dependence of molecular structures. This strategy guides the model to adapt to the structural adjacency patterns in the target domain, generating domain-separable structural representations. 2) We apply the cross-domain representation guidance mechanism to align the functional-group semantic information between the source and target domains, learning cross-domain consistency information. The experimental results in two typical cross-domain strategies demonstrate that DisTrans outperforms 16 baseline methods, maintaining satisfactory performance even under pronounced inter-domain discrepancy.

---


### 76. [Cross-modal Affinity-aligned Multimodal Learning Analytics for Predicting Student Collaboration Satisfaction in Game-Based Learning](https://arxiv.org/abs/2605.16806)

**<font color=#1a73e8>作者：</font>** Wen-Hsin Tsai, Chia-Ming Lee, Yuk-Ying Tung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Collaborative game-based learning environments offer rich opportunities for small-group knowledge construction, yet automatically predicting student collaboration satisfaction remains challenging. A critical barrier is modality degradation: in educational deployments, individual modalities such as eye gaze exhibit inconsistent informativeness across student cohorts, causing implicit attention-based fusion to produce brittle multimodal representations. We propose the Affinity-Aligned Multimodal Learning Analytics (AAMLA) framework, whose core contribution is the Cross-modal Affinity-guided Modality Alignment (CAMA) module, which explicitly models inter-modal relationships via affinity matrices and enforces cross-modal consistency through contrastive learning, enabling adaptive suppression of uninformative modalities without discarding them. AAMLA further applies modality-specific projection layers to map heterogeneous features, including facial action units, head pose, eye gaze, and interaction trace logs, into a unified semantic space prior to alignment. Experiments on 50 middle school students in the EcoJourneys collaborative learning environment demonstrate consistent improvements over unimodal baselines and prior cross-attention approaches under standard and modality degradation conditions, with SHAP and t-SNE analyses confirming that CAMA produces robust, interpretable cross-modal representations for student collaboration modeling.

---


### 77. [Multi-Paradigm Agent Interaction in Practice:A Systematic Analysis of Generator-Evaluator, ReAct Loop,and Adversarial Evaluation in the buddyMe Framework](https://arxiv.org/abs/2605.16821)

**<font color=#1a73e8>作者：</font>** Xiaohua Wang, Chao Han, Kai Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid evolution of Large Language Model (LLM) agents has produced diverse interaction paradigms, yet few production systems integrate multiple paradigms within a unified architecture. This paper presents a systematic analysis of three principal agent interaction paradigms, including Multi-Agent Orchestration (Generator-Evaluator), ReAct Tool-Use Loops, and Memory-Augmented Interaction, as implemented in buddyMe, an open-source multi-model agent programming framework. We formalize a five-stage processing pipeline: Requirement Pre-Review -> Task Decomposition -> ReAct Execution -> Real-Execution Verification -> Adversarial Evaluation Discussion, and establish a six-dimensional evaluation schema with weighted scoring. Through four empirical case studies drawn from real-world deployment logs covering museum guide generation, scheduled weather tasks, and comprehensive tour planning, we draw three key conclusions. First, Generator-Evaluator pre-review detects requirement omissions in 20 percent of complex tasks, with 80 percent tasks passing initial inspection. Second, the ReAct loop ensures stable subtask execution but leads to around 30 percent redundant tool invocations. Third, adversarial Evaluator-Defender discussions reach consensus within 2-3 rounds for nearly 70 percent of scenarios, functioning mainly for content refinement rather than logical reversal. We additionally provide three Mermaid-based architectural diagrams and conduct cross-paradigm comparisons with CrewAI, AutoGen, LangGraph, MemGPT and A-Mem across six system dimensions. The research outcomes offer practical design guidelines for constructing stable and reliable multi-paradigm agent systems.

---


### 78. [Confidence Geometry Reveals Trace-Level Correctness in Large Language Model Reasoning](https://arxiv.org/abs/2605.16824)

**<font color=#1a73e8>作者：</font>** Shuo Liu, Ding Liu, Shi-Ju Ran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) generate not only reasoning text, but also token-level confidence trajectories that record how uncertainty evolves during inference. Whether these trajectories are relevant to reasoning correctness remains unclear. Here we show that confidence trajectories encode a content-agnostic confidence geometry associated with trace-level final-answer correctness. Using only token-level confidence values, without access to the input question, reasoning text, hidden states, or external verifiers, we find that low-dimensional representations of confidence trajectories separate correct from incorrect reasoning traces. Across GSM8K, MATH, and MMLU, this geometric separation is quantitatively linked to downstream predictability: stronger clustering of correct and incorrect traces, measured by the Davies--Bouldin index, consistently corresponds to higher correctness-discrimination AUC. We further show that correctness-related information is enriched in the tail of reasoning, suggesting that late-stage confidence dynamics carry key correctness signals. We propose NeuralConf, a lightweight estimator that learns from confidence trajectories for correctness evaluation. Under a fixed trace budget, NeuralConf-derived scores improve confidence-weighted answer aggregation over majority voting, tail confidence, and other static baselines. These results reveal that LLMs expose trace-intrinsic statistical signals of correctness through their own confidence dynamics, offering a route to improve inference using information already present within generation.

---


### 79. [Decoupling KL and Trajectories: A Unified Perspective for SFT, DAgger, Offline RL, and OPD in LLM Distillation](https://arxiv.org/abs/2605.16826)

**<font color=#1a73e8>作者：</font>** Anhao Zhao, Haoran Xin, Yingqi Fan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation is central to LLM post-training, yet its design space remains poorly understood, especially alongside reinforcement learning (RL). We show that the prevailing paradigms, off-policy distillation and on-policy distillation (OPD), implicitly couple two orthogonal choices: prefix source and token-level KL direction. This follows from decomposing sequence-level KL over autoregressive response distributions: forward KL pairs teacher prefixes with token-level forward KL, and reverse KL pairs student prefixes with token-level reverse KL. We argue this coupling is not intrinsic: decoupling the two axes yields four valid objectives. We establish gradient-level identities showing forward KL gives SFT-style cross-entropy matching with teacher soft targets, whereas reverse KL gives an RL-style policy-gradient objective with a dense teacher-student log-ratio reward, connecting them to off-policy SFT, DAgger-style on-policy SFT, offline-RL-style distillation, and OPD. We conduct an extensive controlled study on math reasoning, evaluating the four objectives both as standalone methods and as initializations for subsequent RL. The results reveal three tradeoffs: KL direction induces an accuracy-entropy tradeoff, prefix source a quality-compute tradeoff, and training length an accuracy-stability tradeoff. Motivated by these findings, we propose KL mixing and an entropy-gated length curriculum. KL mixing shows long-sequence distillation requires substantial forward-KL weight to prevent entropy collapse and length inflation without sacrificing accuracy. The entropy-gated length curriculum improves Avg@k and Pass@k by 3.6 and up to 5.8 points, and cuts average response length by roughly 3x versus fixed long-horizon training. Our results provide a framework and practical methods for designing reasoning distillation objectives that balance accuracy, diversity, compute, and RL behavior.

---


### 80. [Coarse Semantic Injection for LLM-Conditioned Structured Indoor Prediction](https://arxiv.org/abs/2605.16832)

**<font color=#1a73e8>作者：</font>** Shuliang Zhu, Tomiwa Adey, Jinjia Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have recently been used as structured decoders for indoor understanding from 3D point-token inputs. However, point cloud encoders often under-represent thin structural elements such as doors and windows after voxelization and sparse pooling, and may miss individual furniture instances in cluttered scenes. We propose an interface-preserving semantic augmentation for LLM-conditioned structured decoding. The key idea is to associate semantic evidence with the point-cloud representation, reduce it to a coarse four-group code (furniture, walls, openings, and others), and encode it as an RGBB point interface: red for furniture, green for walls, blue for openings, and black for others, where RGBB denotes four semantic color states represented in three RGB channels rather than an additional fourth channel. This semantic color code is appended to the original raw point attributes before tokenization, so geometry and semantics share the same sparse tokenization path while the downstream language model decoder and output serialization remain unchanged. We further introduce a lightweight routed semantic shift module, with an auxiliary head used only for training-time ratio/budget regularization and analysis, to strengthen semantic cues after sparse pooling. The overall pipeline can use RGB-derived semantic evidence. Under these controlled semantic-source settings, the reported metrics improve across Structured3D, the SpatialLM dataset, and ARKitScenes, especially for opening localization and per-instance furniture detection in cluttered scenes. Ablations clarify the roles of semantic source, color coding, token fusion, and shift injection, while also showing that color/entropy effects remain nontrivial.

---


### 81. [Learning Relative Representations for Fine-Grained Multimodal Alignment with Limited Data](https://arxiv.org/abs/2605.16834)

**<font color=#1a73e8>作者：</font>** Shiwon Kim, Yu Rang Park  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal pre-training demonstrates strong generalization performance, but this paradigm is often impractical in domains where paired data are scarce. A promising alternative is post-hoc multimodal alignment, which aligns separately pre-trained unimodal encoders using a limited number of paired examples. However, existing methods focus primarily on aligning global representations, missing patch-token relations. This may hinder transfer to tasks that require fine-grained cross-modal matching beyond coarse sample-level semantics. To address this issue, we propose a post-hoc alignment method that learns token-level cross-modal structure using relative representations. Specifically, we represent images and texts through their token-level similarities to a set of learnable anchors in each modality space, which are trained to induce consistent cross-modal similarity patterns for matched pairs. Despite learning only the anchors without heavy projection layers, our approach consistently outperforms existing methods in zero-shot classification, cross-modal retrieval, and zero-shot segmentation by a substantial margin. This highlights the importance of modeling fine-grained cross-modal structure for effective post-hoc multimodal alignment with limited paired data.

---


### 82. [Sketch Then Paint: Hierarchical Reinforcement Learning for Diffusion Multi-Modal Large Language Models](https://arxiv.org/abs/2605.16842)

**<font color=#1a73e8>作者：</font>** Siqi Luo, Jianghan Shen, Yi Xin 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion Multi-Modal Large Language Models (dMLLMs) are powerful for image generation, but optimizing them through reinforcement learning (RL) remains a major challenge. One primary difficulty is that a single image can be generated through many different unmasking sequences, which makes calculating importance ratios often intractable. Additionally, existing methods tend to ignore the hierarchical generation process of dMLLMs, where early tokens define the global layout and later tokens focus on local details. By assigning uniform rewards to all tokens, these current methods fail to reflect the actual contribution of each token to the final image. To address these issues, we propose Hierarchical Token GRPO (HT-GRPO), which integrates this hierarchy directly into the policy optimization process. Our approach features a Sketch-Then-Paint training scheme that organizes updates into three distinct stages: global, structure, and refinement. We also use a prompt-conditioned estimator to calculate importance ratios starting from a fully masked state. Furthermore, we introduce a Hierarchical Credit Assignment mechanism that prioritizes key structural tokens to ensure accurate reward propagation. Experiments using two popular dMLLM backbones, MMaDA and Lumina-DiMOO, demonstrate that HT-GRPO achieves substantial gains on the GenEval and DPG benchmarks. Evaluations across six additional metrics confirm significant improvements in image quality, aesthetics, and human preference.

---


### 83. [Learning to Learn from Multimodal Experience](https://arxiv.org/abs/2605.16857)

**<font color=#1a73e8>作者：</font>** Xingyu Sui, Weixiang Zhao, Yongxin Tang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Experience-driven learning has emerged as a promising paradigm for enabling agents to improve from interaction trajectories by accumulating and reusing past experience. However, existing approaches are predominantly developed in textual settings and rely on manually designed memory schemas, limiting their applicability to multimodal environments. In real-world scenarios, experience is inherently multimodal, involving heterogeneous signals across perception, reasoning, and action, which makes effective memory design significantly more challenging. In particular, the optimal way to structure and utilize multimodal experience is highly task-dependent and evolves over time, rendering fixed memory designs insufficient. In this work, we propose a new paradigm, learning to learn from multimodal experience, which shifts memory design from a predefined component to an adaptive and learnable process. Our framework enables agents to dynamically construct, organize, and utilize memory based on task requirements and interaction history, effectively learning how to structure experience for improved performance. Experiments demonstrate that adaptive memory design substantially enhances agent performance and generalization across multimodal tasks, highlighting the critical role of learning memory mechanisms in experience-driven learning.

---


### 84. [Metric-Guided Feature Fusion of Visual Foundation Models for Segmentation Tasks](https://arxiv.org/abs/2605.16864)

**<font color=#1a73e8>作者：</font>** Yachan Guo, JoseLuis Gomez Zurita, Danna Xue 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although large-scale visual foundation models (VFMs) achieve remarkable performance in semantic understanding, they still underperform in instance-aware dense prediction tasks. They exhibit different biases in representation: for instance, promptable segmentation models (e.g., SAM2) focus on fine-grained region boundaries, while self-supervised models (e.g., DINOv3) emphasize object-level structure. This observation highlights the potential of combining complementary features from different VFMs to enhance downstream dense prediction tasks. However, naive multi-VFM fusion seldom leads to reliable gains, and interpretable principles for leveraging their complementary features are still underexplored. In this work, we propose a metric-guided approach that effectively selects and aggregates complementary features from different VFMs based on explicit assessment scores. Specifically, we design a suite of label-free metrics in feature space across two aspects, Structural Coherence and Edge Fidelity, to assess features of VFM encoders. Guided by these scores, we identify complementary edge-strong and structure-strong encoder pairs, and integrate them via a master-auxiliary fusion scheme. This feature fusion requires no complex architectural changes and is trained only in a single stage. Our model shows consistent performance gains across multiple dense prediction tasks compared with the baselines, with better object-level semantics and more accurately localized boundaries. The code is available at {this https URL}.

---


### 85. [PaliBench: A Multi-Reference Blueprint for Classical Language Translation Benchmarks](https://arxiv.org/abs/2605.16881)

**<font color=#1a73e8>作者：</font>** Máté Metzger, Nadnapang Phophichit  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Digital humanities projects increasingly rely on machine translation and large language models to widen access to classical, religious, and otherwise under-translated textual traditions. Yet standard translation benchmarks are poorly suited to such materials: they typically compare a system output against a single reference translation, even though classical texts often support multiple faithful renderings that differ in terminology, register, and interpretation. This article introduces PaliBench, both a benchmark for Pali-to-English translation and a reusable method for constructing multi-reference translation benchmarks for classical languages. The Pali case study draws on passages from the Sutta Pitaka aligned with independent English translations by Bhikkhu Sujato, Bhikkhu Thanissaro, and Bhikkhu Bodhi. The workflow combines LLM-assisted alignment of independently segmented translations, automated verification against source files, passage-level quality filtering, deduplication of formulaic repetitions, and multi-metric evaluation against multiple human references. The resulting benchmark contains 1,700 passages spanning 8,389 segments and approximately 345,000 tokens. We use it to evaluate ten contemporary large language models with complementary metrics, finding strong cross-metric concordance in system rankings alongside substantial variation in reliability and semantic outlier rates. The broader contribution is methodological: PaliBench shows how existing scholarly translations can be transformed into evaluation infrastructure for interpretive textual traditions without treating any single translation as definitive. Although developed for Pali Buddhist texts, the approach could be portable to other classical corpora where sufficient independent reference translations exist.

---


### 86. [Controlling Decision Drift in Multimodal Sentiment Analysis with Missing Modalities](https://arxiv.org/abs/2605.16889)

**<font color=#1a73e8>作者：</font>** Chenglizhao Chen, Yuchen Cao, Xinyu Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal sentiment analysis relies on textual, acoustic, and visual signals, yet real-world data often suffer from modality missing and quality imbalance. Existing methods generate features for modality missing from available ones, but differences in expression mechanisms and sentiment dynamics across modalities may cause the generated features to deviate from true distributions and mislead prediction. In addition, unreliable modalities may dominate fusion, resulting in representation shift across modality combinations and unstable sentiment representations. To address these challenges, we propose a two-level reference alignment framework. The framework introduces stable references at the feature representation and sentiment decision levels to improve robustness under modality missing. First-level reference alignment leverages complete-modality samples to constrain representations and align different modality combinations into a shared sentiment space. Second-level reference alignment enforces cross-modal consistency at the decision level by suppressing unreliable modalities through prototype retrieval and voting. As a result, the framework maintains stable and reliable sentiment predictions under diverse missing-modality patterns. Experiments on CMU-MOSI and CMU-MOSEI show consistent improvements across various missing-modality settings. Under full-modality input, the proposed method achieves state-of-the-art performance, with ACC of 86.28% and 85.88%, and F1 of 86.24% and 85.86%.

---


### 87. [DriveSafe: A Framework for Risk Detection and Safety Suggestions in Driving Scenarios](https://arxiv.org/abs/2605.16892)

**<font color=#1a73e8>作者：</font>** Sainithin Artham, Shankar Gangisetty, Avijit Dasgupta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Comprehensive situational awareness is essential for autonomous vehicles operating in safety-critical environments, as it enables the identification and mitigation of potential risks. Although recent Multimodal Large Language Models (MLLMs) have shown promise on general vision-language tasks, our findings indicate that zero-shot MLLMs still underperform compared to domain-specific methods in fine-grained, spatially grounded risk assessment. To address this gap, we propose DriveSafe, a framework for risk-aware scene understanding that leverages structured natural language descriptions. Specifically, our method first generates spatially grounded captions enriched with multimodal context, including motion, spatial, and depth cues. These captions are then used for downstream risk assessment, explicitly identifying hazardous objects, their locations, and the unsafe behaviors they imply, followed by actionable safety suggestions. To further improve performance, we employ caption-risk pairings to fine-tune a lightweight adapter module, efficiently injecting domain-specific knowledge into the base LLM. By conditioning risk assessment on explicit language-based scene representations, DriveSafe achieves significant gains over both zero-shot MLLMs and prior domain-specific baselines. Exhaustive experiments on the DRAMA benchmark demonstrate state-of-the-art performance, while ablation studies validate the effectiveness of our key design choices. Project page: this https URL research/projects/cvit-projects/drivesafe

---


### 88. [NGM: A Plug-and-Play Training-Free Memory Module for LLMs](https://arxiv.org/abs/2605.16893)

**<font color=#1a73e8>作者：</font>** Yuwen Qu, Wenhui Dong, Chenyang Si 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent studies introduce conditional memory modules that decouple knowledge storage from neural computation, enabling more direct knowledge access. Compared to MoE, which relies on dynamic computation paths, explicit lookup provides a more efficient knowledge retrieval mechanism. However, these approaches still depend on learned memory embeddings, requiring additional training and limiting flexibility. To address this, we propose N-gram Memory (NGM), a training-free, plug-and-play module composed of a Causal N-Gram Encoder and a Cosine-Gated Memory Injector. The Causal N-Gram Encoder directly averages the pretrained token embeddings of the backbone model to construct N-gram representations, thereby eliminating the need to train separate N-gram embeddings from scratch. This design requires neither an additional memory table nor a retrieval pipeline. The Cosine-Gated Memory Injector then uses a non-parametric cosine gate with ReLU to modulate the retrieved embeddings into the contextual representations. We evaluate NGM on the Qwen3 series from 0.6B to 14B across eight benchmarks. NGM improves average performance by 0.5 to 1.2 points, with particularly clear gains on code generation and knowledge-intensive tasks (e.g., +3.0 on LiveCodeBench and +3.03 on GPQA for Qwen3-14B). Moreover, NGM also improves performance in multimodal benchmarks (e.g., MMStar +1.53 on Qwen3-VL-2B).

---


### 89. [CAR-SAM: Cross-Attention Reconstruction for Post-Training Quantization of the Segment Anything Model](https://arxiv.org/abs/2605.16901)

**<font color=#1a73e8>作者：</font>** Houji Wen, Jiangyong Yu, Jun Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Segment Anything Models (SAMs) are extensively used in computer vision for universal image segmentation, but deploying them on resource-constrained devices is challenging due to their high computational and memory demands. Post-Training Quantization (PTQ) is a widely used technique for model compression and acceleration. However, existing PTQ methods fail to consider the cross-attention architecture in the SAM decoder. This degradation primarily stems from the unique challenges posed by SAMs: (1) Attention dissipation, where the attention information in the decoder, which is crucial for representing segmentation masks, collapses into a diffuse and non-semantic form under low-bit quantization; and (2) Reconstruction oscillation, where bidirectional coupling within the two-way transformer introduces cross-branch error interference and destabilizes convergence. To tackle these issues, we propose CAR-SAM, a unified quantization framework tailored for SAMs. Firstly, to mitigate attention dissipation, we introduce MatMul-Aware Compensation (MAC) mechanism that transfers activation-induced quantization errors from MatMul to preceding linear weights. Secondly, to mitigate oscillation in decoder optimization, we develop a Joint Cross-Attention Reconstruction (JCAR) strategy that jointly reconstructs coupled attention branches, suppressing oscillatory behavior and promoting stable convergence. Extensive experiments show that CAR-SAM robustly quantizes SAM models down to 4-bit precision, surpassing existing methods by 14.6% and 6.6% mAP on SAM-B and SAM-L respectively.

---


### 90. [ArtifactLinker: Linking Scientific Artifacts for Automatic State-of-the-Art Discovery](https://arxiv.org/abs/2605.16902)

**<font color=#1a73e8>作者：</font>** Haofei Yu, Jiaxuan You, Peter Clark 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific artifacts such as models and datasets are foundations for research. With the rapid growth of platforms like HuggingFace, researchers now have access to a large number of artifacts. Yet, a key challenge remains: how can we automatically discover the state-of-the-art (SOTA) model for a given dataset by fully leveraging existing artifacts? We formalize this task as automatic SOTA discovery by modeling HuggingFace as an artifact graph, where nodes are models/datasets and edges represent evaluations. We propose ArtifactLinker, a two-stage framework: (1) ranking promising unobserved model--dataset links using Graph Neural Networks (GNNs) or graph-augmented Large Language Models (LLMs), and (2) verifying top-ranked links via coding experiments with LLM-based agents. We further introduce a benchmark named ArtifactBench with 14,053 artifacts and 51,337 relations to evaluate the performance of both stages. Results show that (1) graph structures between existing artifacts are effective for missing link prediction; (2) end-to-end ranking and verification with ArtifactLinker help discover potential SOTA results and research insights.

---


### 91. [TOBench: A Task-Oriented Omni-Modal Benchmark for Real-World Tool-Using Agents](https://arxiv.org/abs/2605.16909)

**<font color=#1a73e8>作者：</font>** Zhiqiang Liu, Wenhui Dong, Yilang Tan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-using agents are increasingly expected to operate across realistic professional workflows, where they must interpret multimodal inputs, coordinate external tools, inspect intermediate artifacts, and revise their actions before producing a final result. Existing benchmarks, however, often evaluate tool use, computer use, and multimodal reasoning in isolation, leaving a gap between benchmark settings and end-to-end omni-modal tool use in the real world. To address this gap, we introduce MM-ToolBench, a benchmark and evaluation harness for task-oriented omni-modal tool use. MM-ToolBench contains 100 executable tasks from two macro task families, Customer Service and Intelligent Creation, covering 20 subcategory slices and supported by 27 MCP servers with 324 tools. The central design of MM-ToolBench is closed-loop multimodal verification: agents must execute tools, inspect rendered or transformed artifacts, and self-correct when outputs fail task-specific requirements. To make such evaluation scalable and verifiable, MM-ToolBench couples MCP-based execution with task-specific grounded evaluators and a semi-automated construction pipeline for scenario discovery, task instantiation, evaluator synthesis, and human audit. Experiments on 15 contemporary agentic models show that MM-ToolBench remains highly challenging: Claude Opus 4.6, commonly regarded as one of the strongest coding-agent models, achieves only 32.0% task success, far below the 94.0% human benchmark. We envision MM-ToolBench as a practical foundation for evaluating and advancing next-generation omni-modal tool-using agents through closed-loop multimodal verification.

---


### 92. [The Effects of Structured LLM-Generated Feedback on Programming Assignment Performance](https://arxiv.org/abs/2605.16933)

**<font color=#1a73e8>作者：</font>** Tsvetomila Mihaylova, Evanfiya Logacheva, Arto Hellas 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> When programming students encounter errors in their code, compiler messages or static analysis output often provide limited guidance, particularly for novice programmers. Personalized feedback from instructors can be effective but does not scale well. Recent advances in large language models (LLMs) enable automated feedback generation at scale. This study examines whether LLM-generated feedback with different levels of guidance is associated with differences in students' problem-solving behavior. We analyze effects on time to solution and number of attempts, and examine whether these effects differ by programming experience. We design three feedback types and compare them to a baseline in which students receive only compiler error messages. Results from an online programming course show that LLM-generated feedback is associated with faster time to solution compared to the no-feedback baseline, with less guided feedback showing slightly stronger effects. Overall, the findings suggest that feedback structure plays an important role in how students progress toward correct solutions and motivate further work on adaptive feedback designs and longer-term learning outcomes.

---


### 93. [Effort as Ceiling, Not Dial: Reasoning Budget Does Not Modulate Cognitive Cost Alignment Between Humans and Large Reasoning Models](https://arxiv.org/abs/2605.16938)

**<font color=#1a73e8>作者：</font>** Yueqing Hu, Tianhong Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) generate chain-of-thought traces whose length tracks human reaction times across cognitive tasks, but recent debate questions whether this alignment reflects genuine computational structure or surface verbosity. We test whether the alignment varies with inference-time reasoning effort. Across GPT-OSS-20B and GPT-OSS-120B, three effort levels, and six reasoning tasks, within-task and cross-task alignment remain invariant: Bayes Factors lean toward the null, and mean alignment is numerically near-identical across conditions. A manipulation check reveals that the effort parameter sets an upper budget on generation rather than driving real-time allocation, suggesting that the allocation policy is crystallized at training time. Arithmetic complexity contrasts further show that token allocation tracks fine-grained, format-dependent human difficulty patterns, with model scale improving the match. Cognitive cost alignment between LRMs and humans appears to be a training-time achievement, robust to inference-time perturbations, supporting a compiled rather than online account of LRM problem-solving.

---


### 94. [Roll Out and Roll Back: Diffusion LLMs are Their Own Efficiency Teachers](https://arxiv.org/abs/2605.16941)

**<font color=#1a73e8>作者：</font>** Fanqin Zeng, Feng Hong, Geng Yu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion Large Language Models (DLLMs) promise fast parallel generation, yet open-source DLLMs still face a severe quality-speed trade-off: accelerating decoding by revealing multiple tokens often causes substantial quality degradation. We attribute this dilemma to a train-inference mismatch amplified by irreversible decoding. While training reconstructs tokens from randomly corrupted states, efficient inference requires an adaptive denoising order, where easier tokens are revealed earlier and context-dependent ones are deferred. This view motivates two complementary methods: an inference-time method that makes parallel decoding revokable, and a training-time extension that distills the reliable order exposed by this revokable process. Accordingly, we first propose Wide-In, Narrow-Out (WINO), a training-free decoding algorithm that enables revokable parallel generation. WINO aggressively drafts multiple tokens, verifies generated tokens with enriched global context, and re-masks unreliable ones for later refinement. Building on this discovered order, we further introduce WINO+, which injects the verified denoising trajectories produced by WINO into model parameters, aligning training with efficient inference. Experiments on LLaDA and MMaDA show that WINO improves both quality and efficiency, while WINO+ further strengthens this progression. On GSM8K, WINO improves accuracy from 73.24% to 75.82% with a 6.10x step reduction, and WINO+ further achieves 76.58% with a 6.83x reduction. On Flickr30K, WINO+ reaches a 16.22x step reduction with improved CIDEr. These results demonstrate that DLLMs can serve as their own efficiency teachers by first discovering reliable denoising orders through revokable decoding and then learning to follow them for faster generation. Code is available at this https URL.

---


### 95. [Beyond Point-Wise Matching: Structural Representation Alignment for Accelerating Diffusion Transformers](https://arxiv.org/abs/2605.16949)

**<font color=#1a73e8>作者：</font>** Shaodong Xu, Zhendong Wang, Litong Gong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in Diffusion Transformers (DiTs) demonstrate that aligning noisy latent states with well-trained semantic features-as pioneered by Representation Alignment (REPA)-can substantially accelerate training and improve generation fidelity. Subsequent analysis(e.g., iREPA) suggests that these gains arise primarily from transferring spatial structure contained in pre-trained vision representations. However, mostly existing alignment methods employ point-wise matching objectives or rely on implicit architectural tweaks, which fail to explicitly model the spatial relational geometry inherent in vision foundation models. We argue that such element-wise supervision is insufficient to capture the rich spatial topology of visual representations, and that effective alignment for generation should instead be formulated as an explicit structural constraint. To this end, we propose sREPA, a structural REPresentation Alignment framework to enforce consistency in the relational geometry of feature maps, rather than merely matching individual feature points. By encouraging the model to internalize holistic spatial layouts and structural correlations from pre-trained features, sREPA achieves faster and more stable convergence, along with improved sample quality, compared to state-of-the-art alignment strategies. Our code and models will be released.

---


### 96. [How do Humans Process AI-generated Hallucination Contents: a Neuroimaging Study](https://arxiv.org/abs/2605.16953)

**<font color=#1a73e8>作者：</font>** Shuqi Zhu, Yi Zhong, Ziyi Ye 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While AI-generated hallucinations pose considerable risks, the underlying cognitive mechanisms by which humans can successfully recognize or be misled by these hallucinations remain unclear. To address this problem, this paper explores humans' neural dynamics to characterize how the brain processes hallucinated content. We record EEG signals from 27 participants while they are performing a verification task to judge the correctness of image descriptions generated by a multi-modal large language model (MLLM). Based on an averaged event-related potential (ERP) study, we reveal that multiple cognitive processes, e.g., semantic integration, inferential processing, memory retrieval, and cognitive load, exhibit distinct patterns when humans process hallucinated versus non-hallucinated content. Notably, neural responses to hallucinations that were misjudged versus correctly judged by human participants showed significant differences. This indicates that misjudged AI-generated hallucinations failed to trigger the standard neurocognitive fact verification pathway.

---


### 97. [WhiteTesseract: Reframing the Interpretation of Cultural Heritage through XR and Conversational AI](https://arxiv.org/abs/2605.16972)

**<font color=#1a73e8>作者：</font>** Jingjing Li, Zhi Liu, Xiyao Jin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Cultural heritage exhibitions often struggle to sustain attention and support reflective engagement. Physical exhibitions rely on fixed interpretive aids that lack adaptability to individual backgrounds or curiosity, and their effectiveness depends heavily on a visitor's Personal Context, prior knowledge, and cultural literacy. Meanwhile, digital exhibitions prioritize convenience and accessibility but risk weakening the Physical and Social Contexts that define embodied cultural experience.
WhiteTesseract addresses this gap by enabling in-situ interpretation through high-resolution XR and conversational AI. The system integrates spatial intelligence via artwork recognition to allow visitors to selectively reduce environmental distractions (via diminished reality) and engage in context-aware dialogue (via large language models). The goal is to preserve the richness of the physical and social environment while providing a flexible space for personal reflection, enhancing Personal Context without compromising physical authenticity.
We deployed the system in a Claude Monet exhibition and conducted a controlled user study with 26 participants. Quantitative results showed that WhiteTesseract modulation significantly increased average viewing duration from 35.3 to 98.3 seconds (p < 0.001). Analysis of 529 visitor-AI interactions revealed that 60% extended beyond factual queries to include analytical, emotional, and comparative inquiries. These findings demonstrate how XR and AI can enrich the physical exhibition experience by supporting deeper, more personalized engagement without displacing the embodied value of cultural heritage. We discuss technical and social constraints for real-world deployment and limitations of our controlled setting.

---


### 98. [SHED: Style-Homogenized Embedding Alignment for Domain Generalization](https://arxiv.org/abs/2605.16973)

**<font color=#1a73e8>作者：</font>** Kai Gan, Tong Wei  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Domain generalization aims to enhance model robustness against unseen domains with embedding distribution shifts. While large-scale vision-language models like CLIP exhibit strong generalization, their direct image-text embedding alignment suffers from inherent information asymmetry: images encode both class semantics and domain-specific styles, whereas text prompts primarily convey basic class cues. This asymmetry hinders generalization to novel domains in realistic scenarios. To address this, we propose Style-Homogenized Embedding alignment for Domain-generalization (SHED), a novel CLIP-based method that aligns style-homogenized embeddings instead of raw representations from encoders in CLIP. During training, SHED removes domain-specific style centroids from both image embeddings computed per source domains and text embeddings which are averaged across diverse prompt templates and stripped of a global centroid. For inference, considering the lack of target domain information, SHED projects diverse textual domain centroids into the visual space and aggregates predictions via membership weighting. Extensive experiments on five benchmarks show SHED achieves state-of-the-art performance, outperforming prior methods significantly (e.g., +4.0\% on DomainNet vs. standard fine-tuning).

---


### 99. [Extending Pretrained 10-Second ECG Foundation Models to Longer Horizons](https://arxiv.org/abs/2605.16975)

**<font color=#1a73e8>作者：</font>** Wei Tang, Jinpei Han, Kangning Cui 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electrocardiogram (ECG) foundation models pretrained on typical diagnostic 10-second ECG segments, have demonstrated strong transferability across a range of clinical applications. However, many real-world applications produce recordings that are typically longer, and are varied in duration during inference time. These 10-second models have no built-in way to combine information across time. Extending them to longer horizons introduces two challenges: structural incompatibilities arising from input-length disparities, and semantic challenges that limit meaningful temporal aggregation. We propose a parameter-efficient framework that extends pretrained ECG foundation models to longer and variable-length ECGs without retraining the backbone. Guided by a frozen pretrained 10-second model, we introduce a lightweight plug-in module that extends the model in two complementary ways: (i) structurally compatible long-sequence processing and (ii) semantically informed temporal modeling. Experiments on multiple long-horizon ECG tasks, datasets, and foundation model backbones demonstrate that our method enables robust long-horizon extension from pretrained snapshot models, consistently outperforming sliding-window and pooling-based baselines with strong parameter efficiency.

---


### 100. [Closing the Gap at CRAC 2026: Two-Stage Adaptation for LLM-Based Multilingual Coreference Resolution](https://arxiv.org/abs/2605.16984)

**<font color=#1a73e8>作者：</font>** Antoine Bourgois, Olga Seminck, Thierry Poibeau  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present our submission to the LLM track of the 2026 Computational Models of Reference, Anaphora and Coreference (CRAC 2026) shared task. With an average CoNLL F1 score of 74.32 on the official test set, our system ranked first in the LLM track, and third overall. Our system is based on the Gemma-3-27b model, fine-tuned using a two-stage strategy with a multilingual base adapter followed by dataset-specific adapters. We represent mention spans by their headword using an XML-inspired format with local reindexing and annotate documents iteratively. These design choices proved effective across languages, document lengths, and annotation guidelines.

---


> [!TIP]
> 当前位于：**51-100**（第 2/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-346](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
