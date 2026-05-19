# 📦 其他研究 | 2026年05月20日

> 本类共 **619** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-350**（第 7/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-619](./part-13.md)

---

### 301. [Computational Challenges in Token Economics: Bridging Economic Theory and AI System Design](https://arxiv.org/abs/2605.17410)

**<font color=#1a73e8>作者：</font>** Ou Wu, Yingjun Deng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Token economics has emerged as a useful lens for understanding resource allocation, value creation, and pricing in large language model systems. While recent work has increasingly treated tokens as economic primitives, there remains a substantial gap between high-level economic theory and the computational realities of modern AI infrastructure. This paper identifies and analyzes the key computational challenges that arise when token-economic principles are implemented in real-time inference systems. We argue that computational feasibility is not merely one dimension of token economics, but its governing constraint: these challenges are driven by fundamental tensions among fine-grained valuation, low-latency execution, and allocation optimality under uncertainty. To structure this problem space, we introduce the notion of \textbf{Computational Token Economics} and propose the \textbf{Token Economics Trilemma} -- a conditional no-free-lunch principle that captures the inherent trade-offs among granularity, real-time performance, and optimality. We further categorize the main technical challenges into three areas: real-time value accounting, constrained resource allocation, and economic-aware system architecture. Rather than presenting a complete solution, this paper aims to define a research agenda for bridging token economics and AI system design, highlighting open problems at the intersection of computational economics, machine learning systems, and AI infrastructure.

---


### 302. [IVF-TQ: Streaming-Robust Approximate Nearest Neighbor Search via a Codebook-Free Residual Layer](https://arxiv.org/abs/2605.17415)

**<font color=#1a73e8>作者：</font>** Tarun Sharma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose IVF-TQ, an IVF index with a codebook-free residual layer: a fixed random rotation followed by precomputed Lloyd-Max scalar quantization depending only on (b, d). Only the IVF coarse partition is trained. Building on TurboQuant (Zandieh et al., 2025), the design substantially reduces a key failure mode of trained-codebook ANN indexes (PQ, OPQ, ScaNN): staleness under streaming this http URL (3 seeds): Per-batch PQ retraining does not recover the streaming gap at any tested bit budget (paired-t p > 0.28 everywhere). On streaming Deep-10M, IVF-TQ holds at 87.4% -> 86.6% (Delta = -0.80 +/- 0.10pp) while IVF-PQ degrades -3.23pp. A shuffled-i.i.d. control on SIFT-1M shows IVF-PQ losing -3.9pp without distribution shift. At higher PQ bit budgets (~1.5x IVF-TQ memory), absolute recall favors PQ as expected from rate-distortion (+6.1pp Deep-10M; +2.0pp SIFT-10M); the durable IVF-TQ benefit is operational (no codebook to retrain), robust across memory this http URL art: IVF around a codebook-free residual quantizer is architecturally not new -- IVF-RaBitQ ships in Milvus, cuVS, LanceDB, Weaviate; Shi et al. (2026) is concurrent GPU work. TurboQuant itself tests only flat-rotation this http URL: (i) A multi-seed streaming-operational story for codebook-free IVF: 10M-scale evidence across PQ memory budgets. (ii) A uniform-over-sphere IP-error bound for the TQ residual quantizer with one fixed rotation (proof sketch in v1; rigorous in v2). (iii) Adaptive IVF-TQ: a partition-only refresh recovering 67% -> 97.8% under worst-case rotation shift with re-ranking (90.3% without).Code, data: this https URL

---


### 303. [Learning Displacement-Robust Representations for Landslide Early Warning under Rainfall Forecast Uncertainty](https://arxiv.org/abs/2605.17419)

**<font color=#1a73e8>作者：</font>** Ren Ozeki, Hamada Rizk, Hirozumi Yamaguchi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rainfall-induced landslides pose a growing risk worldwide as climate change intensifies extreme rainfall events. To provide sufficient evacuation time, landslide early warning systems (LEWS) for real-time disaster monitoring must estimate near-future landslide risk by integrating observed rainfall with short-term rainfall forecasts from spatio-temporal environmental data streams. Although recent landslide prediction methods have improved predictive performance using statistical and deep learning approaches, most assume accurate rainfall inputs. In operational settings, however, landslide prediction relies on rainfall forecasts, which often contain spatial displacement of rainfall fields due to forecasting uncertainties. Such displacement can alter local accumulated rainfall and degrade prediction accuracy. To address this challenge, we propose a novel LEWS robust to rainfall field displacement. The key idea is to learn latent representations from rainfall and terrain data that remain stable under displacement in rainfall field motion, enabling reliable geospatial data integration for landslide risk estimation. The landslide prediction model is trained using Rainfall-Motion-Aware Contrastive Learning (RMCL), which introduces temporally correlated rainfall field perturbations to emulate forecast-induced displacement in rainfall-driven spatio-temporal environmental data streams. Experiments were conducted using two years of rainfall and terrain data across Japan, covering 19 regions with landslide events. The proposed system achieved up to 37% higher precision than state-of-the-art baselines. These results demonstrate that modeling rainfall as a moving spatial field and addressing rainfall field displacement during learning significantly improve the reliability of short-term landslide prediction in operational early warning systems.

---


### 304. [Soap2Soap: Long Cinematic Video Remaking via Multi-Agent Collaboration](https://arxiv.org/abs/2605.17423)

**<font color=#1a73e8>作者：</font>** Yiren Song, Huilin Zhong, Kevin Qinghong Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study series-level cinematic remaking, a long-horizon video-to-video generation problem that localizes full episodes or films via stylization or actor replacement while strictly preserving narrative structure, motion choreography, and character identity across hundreds of shots. Existing video generation and editing pipelines often break down in this regime due to compounding identity drift, background mutation, and semantic erosion under large camera motions and viewpoint changes. We propose Soap2Soap, a multi-agent framework that enforces long-term language-visual consistency through a Dual-Bridge Consistency mechanism: a scene-aware JSON screenplay serving as a persistent semantic backbone, and dynamically allocated visual reference anchors at both scene and shot levels. To suppress drift before video synthesis, we introduce batch keyframe consistency, jointly generating multiple keyframes in a shared latent context via a grid-based formulation. A closed-loop verification agent further audits identity, stability, and alignment to trigger selective regeneration. Experiments on SoapBench demonstrate strong improvements over commercial video generation APIs in long-term consistency and narrative fidelity.

---


### 305. [Human-Flow Digital Twin for Predicting the Effects of Mobility Introduction on Visitor Circulation](https://arxiv.org/abs/2605.17426)

**<font color=#1a73e8>作者：</font>** Chiharu Shima, Haruki Yonekura, Fukuharu Tanaka 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We propose a framework for predicting the effects of mobility introduction measures using a human-flow digital twin. This digital twin incorporates a multi-agent simulator that can represent how visitors choose destinations depending on factors such as their current location and the attractiveness of spots. We extract data on how visitors selected destinations with respect to measured pre-intervention human-flow data, inter-spot distances, spot attractiveness, and travel volumes, and use these data to train each agent's decision model of this simulator. The trained decision model is a function that takes a visitor's current state and surrounding environmental information as input and outputs which spot the visitor will move toward next. By expressing mobility introduction measures as changes to inter-point distances or to spot attractiveness, the framework can reproduce human flows with mobility introduction in the multi-agent simulator and thereby quantify effects such as changes in visitor counts and circulation. We evaluated the proposed method using human-flow data measured with and without introducing mobility within Wakayama Castle Park in Japan. When reproducing flows with mobility introduction using a multi-layer perceptron decision model, the cosine similarity of the spatial population distribution exceeded 0.7, confirming that the approach can replicate the flow changes caused by the mobility introduction.

---


### 306. [Progressive Generalization Augmentation with Deeply Coupled RND-PPO and Domain-Prioritized Noise Injection for Robust Crop Management Reinforcement Learning](https://arxiv.org/abs/2605.17428)

**<font color=#1a73e8>作者：</font>** Wu Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Our preliminary experiments on gym-DSSAT maize irrigation tasks revealed that +/-2 degrees C temperature noise causes an 11.9% reduction in economic returns for PPO policies trained under clean conditions - a systematic robustness deficit that existing research has not adequately addressed.
This paper tackles three interconnected limitations impeding practical deployment of agricultural RL systems: the trade-off between early-stage learning efficiency and late-stage generalization capability; the naive additive combination of intrinsic and extrinsic rewards in exploration-augmented PPO; and uniform measurement noise injection strategies that disregard empirically validated differential sensitivity across agricultural state variables.
We introduce three systematic innovations: Progressive Generalization Augmentation (PGA) implementing a three-phase curriculum (clean training 0-800 episodes, progressive 800-1200, full augmentation 1200-2000); a deeply coupled RND-PPO architecture with dual-channel GAE normalization, progress-decayed intrinsic coefficients, and semantic discretization; and domain-prioritized noise injection with hierarchical activation.
Our experimental evaluation demonstrates: 8.43% yield improvement and 16.42% nitrogen use efficiency improvement over SOTA BERT-DQN in Florida; 5.61% yield improvement in Zaragoza (though 3.67% lower economic score due to challenging Mediterranean climate); and 94.4% vs 80.0% performance retention under combined perturbations.
All experiments used 5 random seeds on NVIDIA A100 GPUs with 4.2+/-0.3 hours per run (2000 episodes, 2048-step buffer, 64 mini-batch size).

---


### 307. [Radial-Angular Geometry for Reliable Update Diagnosis in Noisy-Label Learning](https://arxiv.org/abs/2605.17429)

**<font color=#1a73e8>作者：</font>** Ningkang Peng, Jingyang Mao, Xiaoqian Peng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Noisy-label methods often estimate sample reliability from forward-space signals such as loss, confidence, or entropy. These signals indicate whether a sample is difficult to predict, but they do not directly test whether its observed label induces a reliable parameter update. This gap matters because hard clean samples and mislabeled samples can have similar loss while inducing different updates. We recast reliability estimation as diagnosis of the observed-label update. The sample-wise empirical Fisher trace gives a backward-space measure of update energy: for the classifier layer, it factorizes into a prediction-residual term and a feature-sensitivity term, so it captures information beyond scalar loss. Trace, however, is still a radial magnitude signal and cannot decide whether a large update is useful or harmful. We therefore propose Relative Geometric Conflict (RGC), which compares the observed-label gradient with a reference gradient induced by an EMA teacher. The conflict term helps distinguish large but aligned hard-clean updates from large conflicting updates caused by corrupted labels. Across synthetic and real-world noisy-label benchmarks, RGC improves hard-clean preservation and accuracy under our evaluation protocol.

---


### 308. [MATE: Solving Contextual Markov Decision Processes with Memory of Accumulated Transition Embeddings](https://arxiv.org/abs/2605.17431)

**<font color=#1a73e8>作者：</font>** Himchan Hwang, Hyeokju Jeong, Gene Chung 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose MATE, a simple yet effective memory architecture for solving Contextual Markov Decision Processes (CMDPs), a family of MDPs parameterized by an unobserved context. In CMDPs, an optimal agent can adapt online by maintaining the posterior belief over contexts. MATE replaces this intractable posterior with a sum-aggregated memory, leveraging the posterior's permutation invariance to retain provably sufficient expressiveness. Compared to prior memory architectures, MATE avoids the growing per-step rollout cost of Transformers and the gradient issues commonly associated with Recurrent Neural Networks (RNNs). Extensive evaluations across diverse benchmarks demonstrate that MATE provides clear computational advantages while achieving performance comparable to standard sequence-model baselines.

---


### 309. [VISTA: Variance-Gated Inter-Sequence Test-Time Adaptation for Multi-Sequence MRI Segmentation](https://arxiv.org/abs/2605.17433)

**<font color=#1a73e8>作者：</font>** Zhipeng Deng, Jiale Zhou, Wenhan Jiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deploying multi-sequence magnetic resonance imaging (MRI) segmentation models to new clinical environments is challenging due to variations in scanners and acquisition protocols. Although existing TTA methods handle basic per-modality shifts, they often fail under a fundamental dual-shift problem, as their adaptation signals fail to capture modality-interaction shifts that disrupt inter-sequence consistency. To address this, we propose Variance-gated Inter-Sequence Test-time Adaptation (VISTA), a source-free framework that tackles modality-interaction shifts. First, we design an Inter-Sequence Intervention Generator (ISIG) that generates a set of consistency probes by swapping low-frequency spectra and entropy-localized patches across sequences, preserving anatomical semantics while challenging inter-sequence dependencies. Second, we introduce Cross-View Disagreement-Aware Pseudo Labeling (CDPL), which establishes a voxel-wise reliability metric using cross-view disagreement variance to dynamically gate self-training and enforce interventional consistency, encouraging the network to rely on robust anatomical semantics. Extensive experiments adapting from standard adult MRI (BraTS-GLI-Pre) to African low-field (BraTS-SSA) and pediatric (BraTS-PED) cohorts show improved performance over competing methods under clinical shifts, achieving absolute Dice improvements of +1.89% (SSA) and +2.82% (PED) over the source model. The code is available at this https URL.

---


### 310. [BELIEF: Structured Evidence Modeling and Uncertainty-Aware Fusion for Biomedical Question Answering](https://arxiv.org/abs/2605.17435)

**<font color=#1a73e8>作者：</font>** Chang Zong, Hao Ning, Siliang Tang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Biomedical question answering often requires decisions from retrieved literature whose relevance, quality, and support for candidate answers are uneven. Most retrieval-augmented large language model (LLM) methods feed this literature to the model as flat text, leaving evidence reliability and remaining uncertainty largely implicit. We propose BELIEF, a structured evidence modeling and uncertainty-aware fusion framework for closed-set biomedical question answering. Rather than treating retrieved documents as undifferentiated context, BELIEF converts them into evidence objects that record clinical attributes, source quality, question relevance, support strength, and the associated candidate hypothesis. These evidence objects provide a shared basis for two complementary reasoning paths. The symbolic path constructs reliability-weighted basic probability assignments based on Dempster--Shafer (D-S) theory over a finite answer space and performs uncertainty-aware symbolic evidence fusion to estimate belief and residual uncertainty. The neural path uses the same structured evidence for LLM-based semantic inference, while a reliability-aware arbitration module reconciles the symbolic and neural outputs according to belief strength, uncertainty, evidence reliability, and semantic consistency. Experiments on PubMedQA, MedQA, and MedMCQA with five general-purpose LLM backbones show that BELIEF obtains the best result in 25 of 30 backbone--dataset--metric settings. Comparisons with biomedical-domain models indicate that BELIEF is competitive on MedQA and MedMCQA, while specialized biomedical pretraining remains advantageous on PubMedQA. Ablation, complementarity, uncertainty-stratified, and cost analyses further show that BELIEF improves retrieved-evidence utilization by making evidence structure, path disagreement, and decision uncertainty explicit.

---


### 311. [Beyond Catalogue Counts: the Dataset Visibility Asymmetry in Low-Resource Multilingual NLP](https://arxiv.org/abs/2605.17442)

**<font color=#1a73e8>作者：</font>** Zhiyin Tan, Changxu Duan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual NLP often relies on dataset counts from centralized catalogues to characterize which languages are resource-rich or resource-poor. However, these catalogues record only one layer of dataset visibility: what has been registered or institutionally distributed. They do not necessarily reflect which datasets are created, cited, or reused in the research literature. To examine this gap, we combine a catalogue-based baseline with literature-backed evidence of dataset circulation. We introduce the Resource Density Index (RDI), defined as the number of catalogued datasets per one million speakers, and compute it for the 200 most widely spoken languages in Ethnologue. Among them, 118 languages (59%) have an average RDI of zero across the LRE Map and the Linguistic Data Consortium (LDC), and another 23 fall below 0.1, corresponding to at most one catalogued dataset per ten million speakers. We then apply an LLM-assisted citation-mining pipeline over the Semantic Scholar corpus to these 141 low-visibility languages. After manual validation and consolidation, we identify 609 unique datasets across 53 languages, of which 356 remain openly accessible through working public links. These results reveal a substantial visibility gap: many large-speaker languages appear data-poor in catalogue records yet show clear evidence of dataset activity in the research literature. Our findings suggest that multilingual data scarcity should be understood not only as a production problem, but also as a question of documentation, discoverability, and long-term accessibility. Code and data are publicly available at (this https URL).

---


### 312. [FastOCR: Dynamic Visual Fixation via KV Cache Pruning for Efficient Document Parsing](https://arxiv.org/abs/2605.17447)

**<font color=#1a73e8>作者：</font>** Zihan Tang, Leqi Shen, Hui Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have shown strong promise on Optical Character Recognition (OCR), yet the sheer number of visual tokens required to encode dense documents incurs prohibitive inference cost. Existing pruning methods rely on physical eviction, e.g., permanently discarding visual tokens during the prefill stage. While effective for natural images, this strategy fundamentally breaks down on OCR, where virtually every visual token may correspond to a character or structural element, and any irreversible loss leads to catastrophic accuracy degradation. We observe that, although document images appear globally dense and seemingly unprunable, the model's attention to them is in fact temporally sparse: at each decoding step it concentrates on a small region that shifts gradually across steps, much as a human reader fixates on successive words rather than perceiving an entire page at once. Motivated by this Dynamic Visual Fixation phenomenon, we recast the intractable global pruning problem as a tractable local, dynamic one and propose FastOCR, a training-free framework with two complementary modules. Specifically, Focal-Guided Pruning identifies a small set of focal layers and selects the most task-relevant visual tokens from them at each step, while Cross-Step Fixation Reuse exploits the gradual shift of fixation to warm-start each step from the previous one. By dynamically adjusting which tokens are attended rather than evicting any from the cache, FastOCR avoids permanent information loss. Extensive experiments show that FastOCR serves as a plug-and-play acceleration module, generalizing consistently across five VLMs of varying sizes and architectures. On Qwen2.5-VL, FastOCR retains 98% of the unpruned model's accuracy while attending to only 5% of the visual tokens per decoding step, reducing attention latency by 3.0$\times$.

---


### 313. [Spatial Blindness in Whole-Slide Multiple Instance Learning](https://arxiv.org/abs/2605.17449)

**<font color=#1a73e8>作者：</font>** Xiangyu Li, Ran Su  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Whole-slide MIL models are often called context-aware once graphs, Transform ers, or state-space modules are placed above patch embeddings. We show that this label can be deceptive. On pathology tasks where tissue architecture is part of the diagnostic signal, several strong MIL baselines retain nearly unchanged slide level AUC after patch coordinates are permuted. Their predictions are accurate, but largely compositional. We refer to this failure mode as spatial blindness. Our explanation is optimization-based: dense appearance statistics are learned early under slide-level supervision, leaving weak gradients for sparse spatial relations. ResTopoMIL addresses the issue by first fitting a permutation-invariant prototype histogram and then freezing it while a lightweight graph branch learns the residual under a coordinate-shuffling constraint. The architecture is simple by design; the intervention is in how the spatial branch is trained. Across 9 public WSI bench marks, ResTopoMIL improves classification and survival prediction with 1.15M parameters, restores sensitivity to coordinate perturbation, and gives stronger lo calization evidence on CAMELYON-16.

---


### 314. [Multi-Party Multi-Objective Optimization as Consensus Search: Runtime Analysis of Cross-Party Recombination](https://arxiv.org/abs/2605.17454)

**<font color=#1a73e8>作者：</font>** Xiaolei Fang, Peilan Xu, Wenjian Luo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-party multi-objective optimization problems (MPMOPs) require consensus among autonomous decision makers and therefore differ from flattened many-objective formulations. Existing runtime theory for multi-objective evolutionary algorithms is largely tailored to single-party Pareto-front approximation and does not directly explain common-solution search in MPMOPs. We investigate cross-party recombination in two representative settings. On MP-JCG, a pseudo-Boolean benchmark with an explicit gap region, we prove that a payoff-guided mutation baseline faces a gap-crossing bottleneck requiring \(\Theta(n^2)\) expected fitness evaluations. In contrast, an analytical CPR-NSGA-II variant discovers both common Pareto-optimal solutions in \(O(n\log n)\) expected evaluations by directly assembling complementary prefix and suffix templates distributed across party populations. Comparing this with the flattened four-objective formulation F-JCG, our full-front coverage analysis illustrates the additional coverage burden introduced by flattening. For BPBOMST, the bi-party, two-objective-per-party specialization of the multi-party multi-objective minimum spanning tree problem, we develop a layered support-cover analysis. For each common Pareto objective vector, the symmetric average projection induces an auxiliary bi-objective MST instance, and suitable support representatives yield a \(2\lambda\)-common approximation cover with \(\lambda\in[1,2]\). We further derive an instance-parameterized expected runtime bound for a representative-pool CPR-NSGA-II variant using edge-union recombination and uniform repair. This bound separates the effects of local auxiliary-front filling, cross-party recombination shortcuts, and edge-union repair ambiguity.

---


### 315. [GCE-MIL: Faithful and Recoverable Evidence for Multiple Instance Learning in Whole-Slide Imaging](https://arxiv.org/abs/2605.17456)

**<font color=#1a73e8>作者：</font>** Xiangyu Li, Ran Su  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multiple instance learning (MIL) is the standard approach for whole-slide image (WSI) classification and survival prediction, where attention-based models ag gregate patch features into slide-level predictions. These models treat attention weights as evidence for their predictions, but attention is optimized for classi fication, not for identifying which patches actually support the diagnosis. This conflation leads to three failures: selected patches are insufficient (keeping them alone drops Macro-F1 by 0.078), unnecessary (removing them barely changes the prediction), and unrecoverable (continuous attention scores disagree with discrete patch subsets used at inference). The central premise is that evidence quality should be optimized directly through explicit criteria- Sufficiency, Necessity, and Recov erability (S/N/R)- rather than inherited as a byproduct of classification. GCE-MIL is a backbone-agnostic wrapper implemented through three injection modes and three evidence components: a grounding mechanism that aligns selection with domain-specific concepts, noisy-OR coverage that acts as a differentiable proxy for interventional evidence search, and threshold-plus-repair recovery that converts continuous selectors into discrete subsets through marginal-guided repair. Across 9 backbones and 9 datasets (81 configurations), GCE-MIL improves average Macro-F1 by 0.024 and C-index by 0.014, reduces the continuous-discrete gap by 4-7, and increases complement degradation by 2-4. With optional tile prefiltering after discrete recovery, inference runs up to 5 faster while retaining 0.989 full-bag utility.

---


### 316. [ClaHF: A Human Feedback-inspired Reinforcement Learning Framework for Improving Classification Tasks](https://arxiv.org/abs/2605.17458)

**<font color=#1a73e8>作者：</font>** Tianxiang Xu, Xiaoyan Zhu, Xin Lai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Text classification models are typically trained via supervised fine-tuning (SFT). However, SFT essentially performs behavior cloning from instance-wise labels and thus fails to adequately capture relative preference relations among samples, which limits the model's ability to shape decision boundaries and calibrate predictive confidence. In this paper, we propose ClaHF, a human feedback-inspired reinforcement learning (RL) framework for text classification that integrates preference modeling and RL optimization into the classification pipeline without requiring additional human annotations. Unlike prior work that relies solely on instance-wise supervision, ClaHF constructs multiple candidate predictions together with their relative ranking relations, and jointly models the Top-1 preference and the ordering among non-optimal candidates within a reward model (RM). This design converts conventional label supervision into preference signals that are directly applicable to policy optimization. We conduct systematic evaluations on eight classification tasks spanning three categories of scenarios. Results demonstrate that ClaHF consistently improves both classification performance and confidence calibration across diverse language models (LMs). The data and code are available at this https URL.

---


### 317. [Artificial Intelligence can Recognize Whether a Job Applicant is Selling and/or Lying According to Facial Expressions and Head Movements Much More Correctly Than Human Interviewers](https://arxiv.org/abs/2605.17461)

**<font color=#1a73e8>作者：</font>** Hung-Yue Suen, Kuo-En Hung, Che-Wei Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Whether an interviewee's honest and deceptive responses can be detected by facial expression signals in videos has been debated and requires further research. We developed deep learning models enabled by computer vision to extract temporal patterns of job applicants' facial expressions and head movements to identify self-reported honest and deceptive impression management (IM) tactics from video frames in real asynchronous video interviews. A 12- to 15-minute video was recorded for each of N=121 job applicants as they answered five structured behavioral interview questions. Each applicant completed a survey to self-evaluate their trustworthiness on four IM measures. Additionally, a field experiment was conducted to compare the concurrent validity associated with self-reported IMs between our modeling approach and human interviewers. Human interviewers' performance in predicting these IM measures from another subset of 30 videos was obtained by having N=30 human interviewers evaluate three recordings. Our models explained 91% and 84% of the variance in honest and deceptive IMs, respectively, and showed stronger correlations with self-reported IM scores than human interviewers.

---


### 318. [Teachers' Vocal Expressions and Student Engagement in Asynchronous Video Learning](https://arxiv.org/abs/2605.17463)

**<font color=#1a73e8>作者：</font>** Hung-Yue Suen, Yu-Sheng Su  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Asynchronous video learning, including massive open online courses (MOOCs), offers flexibility but often lacks students' affective engagement. This study examines how teachers' verbal and nonverbal vocal emotive expressions influence students' self-reported affective engagement. Using computational acoustic and sentiment analysis, valence and arousal scores were extracted from teachers' verbal vocal expressions, and nonverbal vocal emotions were classified into six categories: anger, fear, happiness, neutral, sadness, and surprise. Data from 210 video lectures across four MOOC platforms and feedback from 738 students collected after class were analyzed. Results revealed that teachers' verbal emotive expressions, even with positive valence and high arousal, did not significantly impact engagement. Conversely, vocal expressions with positive valence and high arousal, such as happiness and surprise, enhanced engagement, while negative high-arousal emotions, such as anger, reduced it. These findings offer practical insights for instructional video creators, teachers, and influencers to foster emotional engagement in asynchronous video learning.

---


### 319. [TriOpt: A Scalable Algorithm for Linear Causal Discovery](https://arxiv.org/abs/2605.17465)

**<font color=#1a73e8>作者：</font>** Rafat Ashraf Joy, Elena Zheleva  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning causal relations from observational data is challenging because the graph search space grows super-exponentially with the number of variables. Ordering-based methods reduce this space by first identifying the topological ordering, whereas continuous optimization methods explore most likely regions of the space by casting DAG learning as a differentiable objective with an acyclicity constraint. Despite their conceptual appeal, both paradigms face significant scalability limitations in high-dimensional settings, restricting their practical applicability. In this work, we introduce a new formulation for linear causal discovery that tightly integrates these two paradigms to achieve substantial gains in scalability without sacrificing accuracy. Our approach, TriOpt, decomposes the problem into two efficient stages. First, it recovers the topological ordering by exploiting the Sherman-Morrison rank-1 downdate together with the additive structure of linear kernels, enabling fast and scalable ordering estimation. Second, given this ordering, we reformulate structure learning as a convex continuous optimization problem that entirely avoids the need for enforcing costly acyclicity constraints. We theoretically show that, under the true ordering, TriOpt exactly recovers the underlying linear DAG. Empirically, across synthetic, semi-synthetic, and real-world datasets, TriOpt achieves orders-of-magnitude speedups over state-of-the-art linear causal discovery methods in high-dimensional regimes, while maintaining comparable or superior accuracy.

---


### 320. [EchoSR: Efficient Context Harnessing for Lightweight Image Super-Resolution](https://arxiv.org/abs/2605.17470)

**<font color=#1a73e8>作者：</font>** Hanli Zhao, Binhao Wang, Shihao Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image super-resolution (SR) aims to reconstruct high-quality, high-resolution (HR) images from low-resolution (LR) inputs and plays a critical role in various downstream applications. Despite recent advancements, balancing reconstruction fidelity and computational efficiency remains a fundamental challenge, particularly in resource-constrained scenarios. While existing lightweight methods attempt to expand receptive fields, many of them either incur substantial computational overhead, naively scale up kernel sizes, or lack mechanisms for coherent multi-scale integration, limiting their overall effectiveness and scalability. To address these limitations, we propose EchoSR, an efficient context-harnessing framework for lightweight image super-resolution, which unifies multi-scale receptive field modeling and hierarchical context fusion. EchoSR decouples feature learning into disentangled local, multi-scale, and global modeling stages through an efficient context-harnessing strategy, and further promotes seamless cross-scale integration via a cross-scale overlapping fusion mechanism. Extensive experiments have shown that EchoSR consistently outperforms state-of-the-art lightweight super-resolution methods across multiple benchmarks, while also achieving a faster speed $(\sim 2\times)$. The source code is available at \url{this https URL}.

---


### 321. [Weighted Reverse Convolution for Feature Upsampling](https://arxiv.org/abs/2605.17472)

**<font color=#1a73e8>作者：</font>** Wentong Li, Zhiyuan Qi, Zichen Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pre-trained vision foundation models (VFMs) provide strong semantic representations, yet their patch-level features are inherently coarse, limiting their effectiveness on tasks requiring fine-grained localization, dense prediction, and point-wise correspondence. In this work, we revisit feature upsampling for VFMs from the perspective of \textbf{\textit{inverse problem}} and propose Weighted Reverse Convolution (WRC), a spatially adaptive inverse operator for densifying high-level visual descriptors. Specifically, we formulate feature upsampling as a weighted Tikhonov-regularized least-squares problem, where spatially varying weights modulate both data fidelity and prior strength at each spatial location. This allows WRC to adapt the reconstruction to spatially varying feature characteristics, thereby preserving critical structures while mitigating over-smoothing. Moreover, WRC retains an efficient, fully differentiable closed-form FFT solution, making it a practical drop-in upsampling operator. Integrated into a lightweight self-supervised densification framework, WRC consistently improves dense feature quality across various downstream benchmarks, including segmentation, depth estimation, video object segmentation, object discovery, and keypoint correspondence, while maintaining high computational efficiency.

---


### 322. [Mamba-VGGT: Persistent Long-Sequence Video Geometry Grounded Transformer via External Sliding Window Mamba Memory](https://arxiv.org/abs/2605.17478)

**<font color=#1a73e8>作者：</font>** Tianchen Deng, Zhenxiang Xiong, Nailin Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual Geometry Grounded Transformers (VGGT) have set new benchmarks in high-fidelity 3D scene reconstruction. However, as the sequence length increases, these models suffer from catastrophic geometric forgetting and accumulation drift, primarily due to the quadratic complexity of global attention which necessitates truncated temporal windows. To overcome the resulting geometric drift, we present Mamba-VGGT, an enhanced VGGT framework capable of persistent long-range reasoning. Our key contribution is a Sliding Window Mamba (SWM) memory module that maintains an explicit external memory token across temporal windows. This module leverages selective state-space modeling to distill and propagate global geometric priors, effectively bypassing the memory constraints of traditional transformers. To integrate these long-term temporal cues without disrupting the highly optimized spatial features of the pre-trained VGGT, we propose a Zero-Init Spatial Memory Injector. Utilizing zero-convolutional layers, this injector adaptively fuses persistent memory into the patch token stream, ensuring structural stability and seamless feature alignment. Extensive experiments demonstrate that our approach significantly outperforms existing VGGT-based methods in maintaining spatial consistency and reducing trajectory accumulation errors. Our work provides a scalable, linear-complexity solution for geometry-grounded world modeling in extensive 3D environments.

---


### 323. [The Capability Paradox: How Smarter Auditors Make Multi-Agent Systems Less Secure](https://arxiv.org/abs/2605.17480)

**<font color=#1a73e8>作者：</font>** Qiqi Liu, Thorsten Holz, Shilin Ye 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems extend large language models (LLMs) by decomposing tasks among specialized agents, but their distributed decision process creates new attack surfaces. We identify \emph{semantic hijacking}, an attack in which harmful requests are concealed within domain-specific narratives and propagated to a Manager through Worker reports, without any syntactic injection primitives. Across 42,000 adversarial trials over 12 Manager models and 7 Worker configurations, we uncover a \emph{capability paradox}: as Worker capability increases, the mean system-level Attack Success Rate (ASR) increases from 18.4% to 63.9%, peaking at 94.4%. To explain this effect, we conduct multi-level mediation analysis on two independent datasets (47,807 interactions). This analysis shows that this paradox is driven by \emph{linguistic certainty}: stronger Workers are more likely to interpret adversarial narratives as legitimate, convey their conclusions assertively, and thereby lead Managers to treat such confident endorsements as justification to execute. In our larger Worker-Only setting ($n_W$=14), certainty mediates 74% of the effect, with 95% confidence intervals (CI) excluding zero under both Monte Carlo and cluster bootstrap; the smaller Full-MAS setting ($n_W$ =6) shows a directionally consistent indirect effect. Worker-side safety prompting does not reliably mitigate this failure. Building on the mediation finding, we propose \emph{heterogeneous ensemble verification}, which pairs Workers of asymmetric domain competence so their complementary vulnerabilities break the certainty-to-execution chain, reducing ASR from 52.8% to 2.0% with negligible benign-task impact. Our results show that upgrading components to stronger models can actively degrade system security, and that effective defenses require exploiting--rather than eliminating--capability asymmetries between agents.

---


### 324. [Hybrid Feature Combinations with CNN for Bangla Fake News Classification](https://arxiv.org/abs/2605.17481)

**<font color=#1a73e8>作者：</font>** Md Gulzar Hussain, Babe Sultana, Md Rinku Ali  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Nowadays, people in Bangladesh frequently rely on the internet and social media for daily news instead of traditional newspapers. However, the spread of false Bangla news through these platforms poses risks and challenges to the credibility of authentic media. Although several studies have been conducted on detecting Bangla fake news, there is still significant room for improvement in this area. To assist people, this research explores the effectiveness of feature selection approaches in identifying appropriate features, such as semantic, statistical, and character-level features, or their combinations, on the BanFakeNews-2.0 dataset for detecting Bangla fake news using a CNN model. In this paper, key findings reveal that combining multiple features significantly improves recall and F1-scores compared to using individual features alone. The code for this research can be availed here, this https URL\_FNews\this http URL.

---


### 325. [Residual Semantic Decomposition of Word Embeddings](https://arxiv.org/abs/2605.17482)

**<font color=#1a73e8>作者：</font>** Seungmin Jin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Residual Semantic Decomposition (RSD), a neural additive decomposition of word embeddings that balances embedding reconstruction with relational structure preservation. RSD supports recursive binary decomposition: each $K=2$ fit extracts a local semantic axis, while residuals expose information not absorbed by that axis. In manually specified paired-context diagnostics over ambiguous words, RSD separates supplied context anchors above shuffled-label controls, but entropy diagnostics show that ambiguous targets are not uniformly high-entropy boundary points in static GloVe. We therefore treat residual neighborhoods as qualitative diagnostics rather than benchmark sense predictions.

---


### 326. [On Applicability of Synthetic Datasets for Facial Expression Recognition](https://arxiv.org/abs/2605.17483)

**<font color=#1a73e8>作者：</font>** Ali Azmoudeh, Erdi Sarıtaş, Ömer Yıldırım 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Facial Expression Recognition faces two core challenges. The first is class imbalance in public datasets, which skews the learning process and weakens generalization. The second is related to privacy and data collection constraints, which limit the sharing of facial images and restrict the creation of large, balanced datasets. To address these issues, we examine three complementary strategies for constructing privacy-preserving FER datasets in the standard seven discrete facial expression classes setting. Our strategies are: (i) pseudo-labeling large unlabeled face collections with a teacher model under a confidence-thresholding scheme, (ii) prompt-driven synthesis using diffusion models conditioned on demographic attributes, and (iii) task-aware GAN-based expression editing that modifies facial expression while preserving identity and realism. For training and evaluation, we employed widely adopted datasets, including AffectNet, RAF-DB, and FER2013. We utilized the synthetic datasets DigiFace, DCFace, and EmoNet-Face BIG as unlabeled sources for pseudo-labeling. Additionally, we utilized the FFHQ dataset as the source for generative synthesis. The main experiments are conducted using a classic CNN backbone, IR50, and we also explore a more complex architecture, POSTERv1, to assess its feasibility and robustness. Using cross-dataset evaluations, we analyze the trade-offs each strategy presents in curated datasets. The findings demonstrate how synthetic data can effectively substitute or be combined with real datasets to mitigate imbalance and privacy limitations. Code and generated datasets:this https URL

---


### 327. [Beyond Linear Superposition: Discovering Climate Features in AI Weather Models with KAN-SAE](https://arxiv.org/abs/2605.17493)

**<font color=#1a73e8>作者：</font>** Minjong Cheon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning weather prediction models achieve remarkable predictive skill yet remain largely opaque: we know little about how they represent physical climate phenomena internally. Mechanistic interpretability through Sparse Autoencoders (SAEs) offers a principled route to decomposing these representations, but existing SAEs assume strictly linear feature superposition - a constraint ill-suited for the highly nonlinear atmospheric dynamics encoded in modern transformers. We introduce KAN-SAE, a sparse autoencoder whose encoder replaces the standard ReLU with learnable per-feature B-spline activations drawn from Kolmogorov-Arnold Networks (KANs), allowing each latent dimension to develop its own nonlinear gating profile. Applied to Sonny, KAN-SAE discovers 975 alive features (vs. 566 for a linear baseline, a 72% improvement) with 20% lower inter-feature redundancy and comparable reconstruction fidelity. Without any climate supervision, KAN-SAE identifies an interpretable European heatwave feature spatially concentrated over western Europe, and a western Pacific typhoon tracker confirmed by causal steering experiments. Our results demonstrate that nonlinear activations are essential for mechanistic interpretability of deep learning weather prediction models, recovering climate features that remain invisible to linear baselines.

---


### 328. [t-gems: text-guided exit modules for decreasing clip image encoder](https://arxiv.org/abs/2605.17499)

**<font color=#1a73e8>作者：</font>** Alberto Presta, Grzegorz Stefanski, Michal Byra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal deep neural networks enhance deep comprehension by integrating diverse data modalities. Data from different modalities are typically projected into a shared latent space for similarity computation, but this process is resource intensive due to large image encoders and equal processing of test data during prediction. Early exit methods reduce computational load by utilizing intermediate layers, saving time and memory. However, developing such methods is challenging for multimodal data like image-text pairs. This study investigates the semantic content distributions present in intermediate layers of encoders such as CLIP, which can be derived from textual descriptions. We introduce Text-Guided Exit Modules (T-GEMs) and a rate-based regularizer to control encoder usage costs while maintaining cross-modal understanding performance.

---


### 329. [The Silent Brush: Evaluating Artistic Style Leakage in AI Art Generation](https://arxiv.org/abs/2605.17500)

**<font color=#1a73e8>作者：</font>** Ninad Joshi, Ashutosh Ranjan, Vivek Srivastava 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative text-to-image models are typically trained on large-scale web-scraped datasets that include diverse visual content such as copyrighted and stylistically distinctive artworks, raising concerns about ownership, attribution, and the unintended reuse of protected visual expressions. A key issue is that models can learn stylistic patterns from this data and reproduce them in generated outputs without any explicit reference in the prompt. We refer to this phenomenon as The Silent Brush, where such learned styles reappear even when they are not requested. Existing evaluation methods mainly focus on near-duplicate retrieval or membership inference and do not account for this form of unintended stylistic resurfacing across prompts. To address these gaps, we first formulate guiding principles for evaluation of The Silent Brush. We then introduce Art Arena, an evaluation protocol that measures how strongly artworks are encoded, how they interact, and how frequently their stylistic traits reappear in generated outputs without explicit mention in prompts. We evaluate Art Arena on widely used text-to-image diffusion models, including Stable Diffusion v1.5, Stable Diffusion XL (SDXL), and SANA-1.5, and design it to generalize across text-to-image generative systems. Our results show that The Silent Brush arises from differences in representational strength and interaction dynamics between artworks, leading to asymmetric blending in model generations. Code and evaluation resources are available at: this https URL.

---


### 330. [A Distributional View for Visual Mechanistic Interpretability: KL-Minimal Soft-Constraint Principle](https://arxiv.org/abs/2605.17504)

**<font color=#1a73e8>作者：</font>** Guancheng Zhou, Yisi Luo, Zhengfu He 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most current paradigms in visual mechanistic interpretability (MI) remain confined to interpreting internal units of the vision model via heuristic methods (e.g., top-$K$ activation retrieval or optimization with regularization). In this work, we establish a theoretical distributional view for visual MI, which models the influence of a feature activation on the natural image distribution, thereby formulating a Kullback-Leibler (KL)-minimal optimization problem to model the MI task. Under this framework, statistical biases are identified within previous MI paradigms, which reveal that they may either be perceptually uninterpretable to humans (i.e., deviate from the natural image distribution), or mechanistically unfaithful to the vision models (i.e., unable to activate model features). To resolve the biases under the distributional view, we propose a model with a KL-minimal soft-constraint principle for visual MI that theoretically balances interpretability and faithfulness. We realize this principle via energy-guided diffusion posterior sampling. Extensive experiments validate the theoretical soundness of the proposed distributional view and demonstrate the practical effectiveness of our paradigm on the DINOv3 vision model.

---


### 331. [Explicit cost analysis of Toom-4 multiplication for incomplete NTT in lattice-based cryptography](https://arxiv.org/abs/2605.17505)

**<font color=#1a73e8>作者：</font>** Sakura Oku, Momonari Kudo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Polynomial multiplication is fundamental in lattice-based cryptography. While the Number Theoretic Transform (NTT) enables fast multiplication, it imposes constraints on the modulus of the coefficient field. Hafiz et al. (2025) addressed this limitation by analyzing the incomplete NTT, which combines a truncated NTT with conventional multiplication methods In this work, we revisit Toom-4 multiplication in the context of incomplete NTT. Although Toom-4 is asymptotically faster than Karatsuba, its precise cost has not been expressed in a form compatible with the incomplete NTT framework. We present a concrete Toom-4 implementation and derive explicit operation counts that separate additions/subtractions and multiplications over the coefficient field. Our analysis based on addition chains yields a simple cost model for incomplete NTT. Using this model, we analyze hybrid strategies combining Toom-4, Karatsuba, and incomplete NTT. We identify parameter ranges where Toom-4 is advantageous and validate the predicted behavior experimentally.

---


### 332. [Degradation Frequency Curve: An Explicit Frequency-Quantified Representation for All-in-One Image Restoration](https://arxiv.org/abs/2605.17506)

**<font color=#1a73e8>作者：</font>** Xinghua Huang, Zhixiong Yang, Chen Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A fundamental difficulty in all-in-one blind image restoration is that degradation is usually treated as an implicit factor hidden in degraded-to-clean mapping, rather than as an explicit object that can be measured and manipulated. This limitation becomes more pronounced under mixed, compound, or unseen degradation conditions, where degradation effects are hard to assign to predefined labels or task-specific parameters. We propose the Degradation Frequency Curve (DFC), a structured spectral representation that quantifies degradation responses by measuring band-wise residual-to-degraded energy ratios in the frequency domain. DFC converts visually entangled and hard-to-describe degradation effects into a measurable degradation coordinate space. Moreover, DFC can be adaptively decomposed into band-wise spectral tokens, allowing local degradation responses to be represented as reusable restoration priors. Based on this representation, we develop the DFC-guided Image Restorer (DFC-IR), a token-conditioned multi-scale framework that progressively estimates DFCs from intermediate restorations and uses the resulting spectral tokens to guide degradation-aware restoration in a coarse-to-fine manner. Extensive experiments on standard, composite, unseen, and real-world degradation benchmarks show that DFC provides an effective representation basis for all-in-one restoration, leading to state-of-the-art performance and improved generalization under complex degradation profiles.

---


### 333. [BESplit: Bias-Compensated Split Federated Learning with Evidential Aggregation](https://arxiv.org/abs/2605.17508)

**<font color=#1a73e8>作者：</font>** Yuhan Xie, Chen Lyu, Jingrong Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Split Federated Learning (SFL) enables privacy-preserving collaborative training by partitioning models between clients and a server. However, under non-IID data distributions, SFL often suffers from biased optimization and unstable convergence, while existing solutions largely adapt techniques from conventional federated learning. In this work, we observe that the split architecture of SFL inherently alters how client information is represented and coordinated, opening opportunities for bias compensation beyond parameter-level aggregation. Based on this insight, we propose BESplit, an architecture-aware framework that exploits the intrinsic structure of SFL to mitigate non-IID effects. First, to prevent biased local data from dominating global updates, we introduce Evidential Aggregation (EA) to perform fine-grained reweighting of client contributions based on evidential uncertainty. Second, to further reduce distributional skew, we develop Bias-Compensated Collaboration (BCC) to align split-layer representations by pairing complementary clients. Finally, Dual-Teacher Distillation (DTD) is incorporated to synchronize knowledge between decoupled client and server models, enabling independent local inference. Extensive experiments on five benchmark datasets demonstrate that BESplit consistently outperforms state-of-the-art methods in accuracy, convergence stability, and computational efficiency under diverse non-IID settings.

---


### 334. [Coordinate Heterogeneity Governs Binary Quantization: From InfoNCE to Recall](https://arxiv.org/abs/2605.17524)

**<font color=#1a73e8>作者：</font>** Wenxuan Xiao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Binary quantization (BQ) compresses high-dimensional embeddings into one or two bits per coordinate, enabling nearest neighbor search at extreme speed. Yet a striking puzzle persists: BQ achieves competitive recall on contrastive embeddings but fails on others -- and two leading systems adopt diametrically opposite strategies (random rotation vs. preserving coordinate axes) without a common theory explaining when each is appropriate. We resolve this puzzle by connecting the Gaussian structure recently established for InfoNCE-trained representations to a complete analytical framework for BQ quality. The key insight is that coordinate heterogeneity -- the non-uniformity of per-coordinate variances -- governs the key aspects of BQ performance. We derive closed-form expressions for ranking fidelity, prove that the magnitude bit carries information proportional to heterogeneity, and show that random rotation destroys precisely the signal that one paradigm exploits while creating the isotropy that the other requires. A two-parameter scaling law predicts fidelity across models and dimensions. Experiments on 13 datasets and 6 embedding families validate all predictions and provide the first principled design guide for binary quantization systems.

---


### 335. [Designing streetscapes from street-view imagery using diffusion models](https://arxiv.org/abs/2605.17527)

**<font color=#1a73e8>作者：</font>** Yuzhou Chen, Yuebing Liang, Lingqian Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Street-view imagery (SVI) is widely used to quantify key indicators of urban environment, such as green- ery, sky, or road view indices. However, existing studies largely focus on measuring current streetscapes and rarely support the generation of alternative and non-existing urban scenarios, which is a core task in geospatial disciplines such as urban planning and design. To address this gap, we propose a gener- ative multimodal AI framework that synthesizes alternative streetscapes conditioned on targeted visual metrics, enabling direct visual exploration of urban scenarios. We first construct a multimodal dataset that aligns SVIs with textual descriptions, segmentation maps, road masks, and quantitative metrics of visual elements in Chicago and Orlando. Using this dataset, we demonstrate that diffusion models can produce realistic and semantically consistent streetscape imagery while responding to both textual and imagery controls. Our quantitative evaluations show that incorporating visual controls can improve semantic consistency, reducing the LPIPS index by approximately 6% while maintaining global visual realism. In addition, overall semantic consistency increases by 23.7% in Orlando and 46.4% in Chicago, as measured by the mIoU index, with class-wise gains exceeding even 100% improvement for building view indices. Streetscape generation can be controlled in a fine-grained manner by both visual and textual prompts, and when textual and visual controls conflict, imagery controls consistently dominate, indicating a clear control hierarchy and the importance of further developing visual controls for urban scene generation. Overall, this work establishes an important benchmark for streetscape generation us- ing SVIs and diffusion models, and illustrates how generative AI can serve as a practical, scalable, and controllable approach for urban scenario exploration.

---


### 336. [Few-Shot Network Intrusion Detection Using Online Triplet Mining](https://arxiv.org/abs/2605.17530)

**<font color=#1a73e8>作者：</font>** Jack Wilkie, Hanan Hindy, Christos Tachtatzis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Network intrusion detection systems play a vital role in protecting networks by detecting malicious network traffic which can then be investigated by a cybersecurity operations centre. State-of-the-art approaches utilise supervised machine learning methods to train a classification model to recognise known cyberattacks; however, these models require a large labelled dataset to train and show poor performance when trained on smaller datasets. In an attempt to address this shortcoming, anomaly detection models learn the distribution of benign traffic and flag non-conforming traffic as malicious. While these methods do not require malicious examples to train, they suffer from high false-positive rates rendering them impractical. As a result, networks may be particularly vulnerable when there are insufficient labelled instances of a specific attack class to train an effective classifier. This often occurs in newly established networks or when previously unseen types of attacks emerge. To address this challenge, this work proposes the use of a triplet network, utilising online triplet mining and a KNN classifier, which is able to perform few-shot classification, enabling effective intrusion detection after being trained on a limited number of malicious examples. Various online triplet mining algorithms were explored and model design choices, such as the inference algorithm and optimised distance metrics, were compared and evaluated through a series of ablation studies. The final model was compared against other state-of-the-art approaches in few-shot binary and multiclass classification, where the proposed approach was found to be competitive with existing methods when trained on as little as 10 malicious samples of each class.

---


### 337. [$\textit{Don't Guess, Just Ask}$: Resolving Ambiguity in Referring Segmentation via Multi-turn Clarification](https://arxiv.org/abs/2605.17531)

**<font color=#1a73e8>作者：</font>** Yuting Yang, Haichao Jiang, Tianming Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Referring segmentation aims to segment the target objects in images or videos based on the textual query. Despite remarkable progress over the past years, existing works always assume that the user-provided queries are already precise and clear. However, this assumption is impractical. In real-world scenarios, it is unrealistic to expect all users to thoroughly review their visual content and carefully ensure their queries are unique and unambiguous. When encountering such cases, existing segmentation models tend to arbitrarily guess the user preferences, often resulting in undesired outcomes. To address this limitation, we propose \textbf{IC-Seg}, a novel agentic framework that proactively clarifies user intent through multi-turn conversation before segmentation. To effectively incentivize this capability, we further introduce \textbf{Hi-GRPO}, a new hierarchical optimization strategy that injects dense and informative supervision signals at the trajectory, turn, and step levels. This strategy encourages efficient intent clarification, effectively eliminating redundant interactions and improving overall dialogue quality. For evaluation, we establish \textbf{Ambi-RVOS}, a referring video object segmentation benchmark with ambiguous user queries. Extensive experiments demonstrate that IC-Seg not only outperforms existing methods by a large margin in resolving ambiguous queries, but also maintains state-of-the-art performance on standard reasoning segmentation benchmarks. Code and data will be released at \url{this https URL}.

---


### 338. [HL-OutPaint: Coarse-to-Fine Video Outpainting for High-Resolution Long-Range Videos](https://arxiv.org/abs/2605.17543)

**<font color=#1a73e8>作者：</font>** Jeongeun Park, Janghyeok Han, Geonung Kim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video outpainting generates plausible visual content beyond the original spatial extent of a video, playing a key role in adapting videos to diverse display formats. To support such use cases, it must enable large spatial extrapolation over long sequences. However, most existing methods address only one of these challenges or lack explicit mechanisms for ensuring global spatio-temporal consistency, leading to notable limitations. In this paper, we propose HL-OutPaint, a high-resolution video outpainting framework for long sequences. Our approach follows a coarse-to-fine strategy with a two-stage pipeline. We first construct Global Coarse Guidance (GCG), a low-resolution representation that captures global structure and dominant motion across the video. Unlike naive downsampling, GCG is built via a novel global-local frame swapping mechanism that couples sparse global keyframes with local temporal windows and exchanges information during sampling. This enables GCG to encode both long-term structural consistency and short-term temporal dynamics in a unified representation. Guided by this representation, HL-OutPaint then performs high-resolution outpainting to generate spatially detailed and temporally consistent content. By separating global structure modeling from fine-grained synthesis, our framework achieves stable, coherent generation for large spatial expansion and long video sequences. Extensive experiments show that HL-OutPaint outperforms existing methods in challenging scenarios involving wide spatial extrapolation and long video sequences.

---


### 339. [Q-LocalAdam: Memory-Efficient Client-Side Adaptive Optimization for Edge Federated Learning](https://arxiv.org/abs/2605.17552)

**<font color=#1a73e8>作者：</font>** Vedant Waykole, Haroon R. Lone  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning on edge devices must cope with non-IID client data and tight memory budgets. Adaptive optimizers like Adam stabilize training under data heterogeneity but require storing full-precision momentum and variance states, often tripling client memory overhead. This limits deployable model sizes and concurrent federated jobs on resource-constrained devices.
We empirically observe that momentum and variance in federated Adam exhibit fundamentally different statistical properties: momentum values are symmetric and bounded, while variance spans eight orders of magnitude with log-normal structure. Motivated by this asymmetry, we propose \textbf{Q-LocalAdam}, which applies distribution-aware 8-bit quantization block-wise linear encoding for momentum and log-space encoding for variance while keeping model parameters in full precision.
Across CIFAR-10 and CIFAR-100 under varying data heterogeneity ($\alpha \in \{0.1, 0.5, 1.0, \text{IID}\}$), Q-LocalAdam achieves $3.37\times$ optimizer memory reduction with no accuracy loss under moderate heterogeneity and significant improvements under extreme heterogeneity (e.g., +5.74pp on CIFAR-100, $\alpha=0.1$). Multi-seed validation confirms statistical significance ($p<0.01$). In contrast, naive uniform quantization degrades to random performance, demonstrating that distribution-aware design is essential. Q-LocalAdam enables larger models and more concurrent workloads on memory-constrained edge devices without modifying the federated protocol.

---


### 340. [PFlow-T: A Persistence-Driven Forward Process for Topology-Controlled Generation](https://arxiv.org/abs/2605.17555)

**<font color=#1a73e8>作者：</font>** Snigdha Chandan Khilar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Current topology aware diffusion models face an architectural mismatch by using Gaussian noise for corruption while recovering structural features through conditional side channels To fix this we introduce PFlow T a generative model that bases its forward process entirely on persistent homology In PFlow T time measures the destruction of H1 topological features like holes rather than Gaussian noise injection This forward process eliminates features based on their persistence The reverse network then directly inverts this structured corruption to predict the clean state in one step Tests on MNIST digits zero one and eight show PFlow T significantly outperforms a baseline model in generating requested Betti numbers and handling out of distribution tasks PFlow T is the first generative architecture using persistent homology for the forward process although we note it is currently limited to low resolution pixel space proxies

---


### 341. [A Conditional U-Net Pipeline with Pre- and Post-Processing for Aerial RGB-to-Thermal Image Translation](https://arxiv.org/abs/2605.17564)

**<font color=#1a73e8>作者：</font>** Tseten Sherpa, Sikandar Ali, Shubham Parab 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Paired RGB-thermal data has shown significant utility across a range of applications, including image fusion, object tracking, and anomaly detection; however, its broader adoption is constrained by the limited availability of aligned RGB-thermal image pairs. RGB-to-thermal (and vice versa) image translation has emerged as a practical solution to this challenge. Prior approaches including conditional generative adversarial networks (cGANs) such as ThermalGAN and Scalable Interpolant Transformer (SiT)-based architectures such as ThermalGen have demonstrated strong potential for aerial-to-thermal image translation. In this work, we explore alternative architectures that prioritize simplicity while maintaining performance. Specifically, we propose a conditional U-Net that incorporates weather data at the bottleneck layer, complemented by targeted preprocessing and post-processing techniques applied within the Pix2Pix GAN architecture. We utilize a training set of 612 paired RGB and thermal images, and evaluate over 5-fold cross-validation, ultimately testing on a held-out test set. Our conditional U-Net model performed best, with a peak signal-to-noise ratio (PSNR) of 14.5485, structural similarity index measure (SSIM) of 0.8095, and learned perceptual image patch similarity (LPIPS) of 0.1666. These results outperformed the base ThermalGen model, which attained PSNR, SSIM, and LPIPS scores of 7.56, 0.2444, and 0.6317 respectively. We find that while saturation boost and contrast enhancement for preprocessing and Gaussian blur for post-processing provide observable improvements, the incorporation of conditioning data was most effective. Our findings cement the potential of integrating auxiliary metadata into thermal image generation, suggesting that such information can serve as a proxy for environmental conditions critical to accurate thermal reconstruction.

---


### 342. [Rethinking Point Clouds as Sequences: A Causal Next-Token Predictive Learning Framework](https://arxiv.org/abs/2605.17566)

**<font color=#1a73e8>作者：</font>** Yumeng Yao, Jingzhi Dong, Haowen Gu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the rapid progress of multimodal foundation models and predictive pre-training, an important open question is how to equip 3D point clouds with a pre-training paradigm that is better aligned with next-token and next-embedding learning. Existing point-cloud self-supervised methods are largely built on masked reconstruction or explicit geometric generation, and thus remain tied to input recovery rather than predictive dependency modeling. In this paper, we introduce PointNTP, which reformulates point cloud pre-training as a fully causal, decoder-free latent Next-Token Prediction problem. Specifically, each point cloud is first partitioned into local patches and serialized into a structured 3D token sequence according to patch-center geometry. The resulting sequence is then modeled by a causal Transformer under prefix-only conditioning, and trained with a shift-based prediction objective stabilized by stop-gradient targets. This design enables the model to learn structural dependencies directly in latent space, without reconstruction decoders or explicit geometric recovery. Extensive experiments demonstrate that the proposed PointNTP is highly competitive across multiple downstream tasks: it achieves 93.8%(+0.5%), 92.6%(+0.3%), and 89.3%(+1.1%) on OBJ_BG, OBJ_ONLY, and PB_T50_RS of ScanObjectNN, respectively; obtains 85.0%(+0.1%) in this http URL on ShapeNetPart; and reaches 71.1% mAcc on S3DIS Area 5. Overall, decoder-free causal latent prediction provides a simple, scalable, and potentially modality-agnostic paradigm for point-cloud self-supervised learning, offering a new 3D perspective on foundation-style predictive learning for 3D data.

---


### 343. [Structured Neural Marked Point Processes for Interpretable Event Interaction Modeling](https://arxiv.org/abs/2605.17568)

**<font color=#1a73e8>作者：</font>** Zhitong Xu, Qiwei Yuan, Yinghao Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-class event streams arise in numerous real-world applications, where uncovering structured, interpretable inter-event relationships, together with accurate prediction, remains a central challenge. Existing neural point process models are highly expressive but encode event interactions in a black-box manner, preventing explicit discovery of structured dependencies. In this paper, we propose a structured neural marked point process (SNMPP) that achieves high modeling flexibility while enabling explicit event-wise and class-wise relationship discovery from data. Our model constructs a product-form neural influence kernel composed of a signed interaction network over event types and a delay-aware monotonic temporal network. This design enables explicit characterization of inter-class influence topology -- including excitation, inhibition, and neutrality -- while flexibly capturing diverse temporal decay patterns and potential influence delays. For efficient learning, we develop a stratified Monte Carlo estimator for stochastic training. Extensive experiments on synthetic and real-world benchmark datasets validate the ability of our approach to uncover structured relationships and deliver strong predictive performance.

---


### 344. [Stable Routing for Mixture-of-Experts in Class-Incremental Learning](https://arxiv.org/abs/2605.17571)

**<font color=#1a73e8>作者：</font>** Zirui Guo, Quan Cheng, Da-Wei Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Class-incremental learning (CIL) requires models to learn new classes sequentially while preserving prior knowledge. Recently, approaches that combine pre-trained models with mixture-of-experts (MoE) have received increasing attention in CIL: they typically expand experts during learning and employ a router to assign weights across experts. However, existing MoE methods often overlook routing drift induced by expert expansion. Once new experts are introduced, the router may reassign samples from earlier classes to newly added experts, thereby perturbing previously established expert compositions and causing interference even when old experts remain frozen. We argue that expandable MoE in CIL requires two complementary properties: stable old-class routing for knowledge preservation and sufficient capacity utilization for new-class adaptation. To this end, we propose Stable Routing for MoE (StaR-MoE), a routing-level framework for expandable MoE in CIL. By incorporating sensitivity-aware routing alignment, StaR-MoE aligns current old-class routing behavior with historical routing distributions through sensitivity-guided constraints. Complementarily, StaR-MoE introduces asymmetric capacity regularization to encourage effective utilization of the expanded expert pool without compromising class-specific routing specialization. Extensive experiments across four standard CIL benchmarks demonstrate that StaR-MoE consistently improves both average and last accuracy over state-of-the-art methods, highlighting the importance of stable routing.

---


### 345. [Deepfake Detection in Social Media: A Temporal Artifact Analysis Using 3D Convolutional Neural Networks](https://arxiv.org/abs/2605.17573)

**<font color=#1a73e8>作者：</font>** Mohammadreza Rashidi, Raja Hashim Ali, Sami Ur Rahman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic facial videos have proliferated across social media faster than platform moderation can respond, raising the cost of disinformation and identity-based attacks. Frame-level deepfake detectors degrade sharply as generator quality increases; high-quality 128x128 GAN output cuts spatial-only accuracy by five percentage points while leaving temporal inconsistencies largely intact. We address this gap with a 3D Convolutional Neural Network detector based on R3D-18, trained with a composite loss that combines binary cross-entropy with a temporal-consistency regularizer. The model processes 16-frame clips from the DeepfakeTIMIT dataset and is initialized from Kinetics-400 action-recognition weights. We report 92.8% accuracy on intra-dataset evaluation at 128x128 resolution; cross-dataset transfer to FaceForensics++ without fine-tuning reaches 76.4%, rising after minimal fine-tuning. Ablation studies show that transfer learning contributes 7.2 percentage points and face tracking adds 3.5 points, while temporal consistency regularization provides additional gains on high-quality fakes. The results establish that temporal artifacts generalize more broadly than spatial ones, providing a detection signal that survives social-media re-encoding.

---


### 346. [UniAlign: A Model-Agnostic Framework for Robust Network Traffic Classification under Distribution Shifts](https://arxiv.org/abs/2605.17575)

**<font color=#1a73e8>作者：</font>** Tongze Wang, Xiaohui Xie, Wenduo Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Network traffic classification (NTC) models often suffer severe performance degradation when deployed in real-world environments due to distribution shifts caused by changing network conditions. Existing robustness-enhancing approaches are commonly coupled to specific model architectures or data settings, fail to generalize to state-of-the-art raw-byte-based NTC models, or incur significant training overhead. In this paper, we propose UniAlign, a novel model-agnostic framework that improves the robustness of deep learning-based NTC models under distribution shifts. UniAlign combines \emph{domain alignment fine-tuning}, which encourages the learning of domain-invariant traffic representations across heterogeneous network conditions, with \emph{stable model ensembling}, which enhances inference robustness by aggregating checkpoints within a flat loss region. The framework can be seamlessly integrated into existing supervised NTC models without requiring specific feature modalities or introducing non-constant additional training costs. We evaluate UniAlign on three public datasets covering diverse distribution shifts, including encryption schemes, data collection devices, and attack behaviors. Experimental results on two representative NTC models demonstrate that, compared with standard training, UniAlign improves average classification accuracy by 2.51\% and average F1 score by 2.71\%, outperforming the strongest baseline by 1.45\% in accuracy and 1.69\% in F1 score, while requiring only 12.4\%--53.9\% of the training time of all NTC-specific baselines.

---


### 347. [Scale-Equivariant Generative Forecasting: Weight-Tied Dilated Convolutions, Wavelet Scattering Inputs, and Spectral-Consistency Training for Self-Similar Time Series](https://arxiv.org/abs/2605.17582)

**<font color=#1a73e8>作者：</font>** Andrea Morandi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many natural and engineered time series -- equity returns, climate anomalies, turbulent velocities, neural recordings, packet-level network traffic -- are approximately self-similar: their horizon-$T$ distribution is tied to the horizon-$1$ distribution by one scaling exponent $H$. Standard deep generative sequence models (transformers, dilated TCNs, the WaveNet family) ignore this. Their receptive fields are wide, but kernel parameters live independently at every dilation level, yielding a multi-scale architecture, not a scale-equivariant one. We make three contributions. First, we give a precise definition of discrete scale equivariance for 1D causal networks and prove that dyadic dilation commutes (up to boundary effects) with any dilated-convolution stack whose kernel weights are shared across levels. Tying the kernel shrinks the convolutional parameter budget by an $L$-fold factor (where $L$ is depth) and hard-wires self-similarity in as an inductive bias. Second, we wrap this Scale-Equivariant WaveNet (SE-WaveNet) backbone in three components that carry the same prior: a one-level Daubechies-4 wavelet input, a Hurst-FiLM block exposing the local scaling exponent, and a spectral-consistency training term targeting the $|f|^{-(2H+1)}$ power-law spectrum. The head is a conditional normalising flow, chosen to preserve equivariance. Third, on 30 years of S&P 500 daily log-returns, SE-WaveNet samples reproduce the empirical scaling-collapse diagnostic on the Allan-Variance top-25 universe (median $\mathcal{C}^\star = 0.020$), while a vanilla WaveNet at matched capacity does not ($\geq 0.06$). NLL, KS-calibration, and tail energy distance tie or beat the baseline, with $L\times$ fewer convolutional parameters.

---


### 348. [AgentSteerTTS: A Multi-Agent Closed-Loop Framework for Composite-Instruction Text-to-Speech](https://arxiv.org/abs/2605.17583)

**<font color=#1a73e8>作者：</font>** Bin Kang, Shaoguo Wen, Yang Fan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While existing text-to-speech (TTS) models exhibit high expressiveness, fine-grained control over composite instructions remains challenging due to the structural mismatch between discrete textual intents and continuous acoustic realizations. Inspired by human cognitive decoupling, we introduce AgentSteerTTS, a multi-agent closed-loop framework designed for intent-faithful expressive control of composite instructions. First, in our framework, an adversarial disentanglement agent mitigates speaker-emotion leakage by learning separable identity and emotion-prosody subspaces with leakage-suppressing regularization. Next, a Dual-Stream Anchoring Controller grounds abstract intents using a large-scale acoustic prototype library: a Retrieval Agent selects expressive anchors, while a Synthesis Agent fuses them into continuous control vectors via gated attention. Finally, a Fast-Slow Feedback Agent refines output intensity through latent gradient correction and resolves semantic-acoustic mismatches using high-level perceptual critique. Experiments on a composite-instruction benchmark and public test sets show that AgentSteerTTS yields consistent and significant improvements to the baselines, demonstrating the effectiveness of the proposed method.

---


### 349. [VVitCutLER: Towards Unsupervised Object Detection and Segmentation in Videos](https://arxiv.org/abs/2605.17584)

**<font color=#1a73e8>作者：</font>** Zhijing Lu, Khurram Azeem Hashmi, Didier Stricker 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsupervised pixel-level video understanding remains challenging in real-world scenarios, where motion blur, occlusion, and fast object dynamics often cause temporal drift and flickering this http URL propose VVitCutLER, an unsupervised framework for video object detection and instance segmentation, which improves the quality of pseudo-labels through temporal consistency. Our core contribution is VitCut, a temporarily stable pseudo-label generator that reduces error accumulation during field degradation through cross-frame region consistency. Meanwhile, VitCut uses a distillation decoder to achieve effective instance mask prediction. Then, based on VitCut, VVitCutLER further integrates cross-frame feature aggregation to enhance video-level robustness. Extensive experiments on standard video benchmarks demonstrate that VVitCutLER significantly improves detection and segmentation performance while reducing temporal instability. These results highlight the importance of temporally consistent supervision for robust pixel-level video understanding.

---


### 350. [MSIQ: Moment-based Scale-Invariant Quality Measure for Single Image Super-Resolution](https://arxiv.org/abs/2605.17588)

**<font color=#1a73e8>作者：</font>** Leonid Bedratyuk  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Assessing the quality of single image super-resolution (SISR) results remains an open methodological problem. Common full-reference metrics (PSNR, SSIM, LPIPS) do not explicitly evaluate the preservation of the geometric structure of images, which is critical for the correctness of scale-based reconstruction. In addition, they require the forced alignment of images to the same size (\textit{forced resizing}), which introduces an external interpolation error into the evaluation process.
This paper proposes a diagnostic scale-invariant quality measure, MSIQ (\textit{Moment-based Scale-Invariant Quality}), based on the comparison of normalized central geometric moments of two images. MSIQ enables direct comparison of images with different spatial resolutions without resizing, is mathematically deterministic (\textit{model-free}), and has an analytical form. To provide a theoretical basis for the approach, we introduce a conceptual distinction between the ability of metrics to monotonically track degradation (\textit{tracking ability}) and their geometric selectivity (\textit{geometric specificity}).
The experimental validation confirmed the stability of MSIQ under uniform scaling and, at the same time, revealed the high sensitivity of traditional metrics to the choice of interpolation method. The results show that MSIQ has pronounced geometric selectivity: the proposed measure effectively separates geometric deformations from non-geometric artifacts, in particular JPEG compression, unlike pixel-based and perceptual metrics. It is also shown that the response of MSIQ to structural perturbations remains stable across different classes of SR algorithms, including DNN models with different architectures. The proposed measure is a complementary diagnostic tool for domains where geometric fidelity has priority, in particular medical imaging and remote sensing.

---


> [!TIP]
> 当前位于：**301-350**（第 7/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-619](./part-13.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
