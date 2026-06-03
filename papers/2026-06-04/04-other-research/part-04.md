# 📦 其他研究 | 2026年06月04日

> 本类共 **312** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-312](./part-07.md)

---

### 151. [Privilege Risk Evolution for Non-Human Identities: A Temporal Fiber Model for Cloud IAM](https://arxiv.org/abs/2606.03289)

**<font color=#1a73e8>作者：</font>** Christophe Parisel  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cloud permission governance implicitly treats permission equivalence as a static relation. We show that for non-human identities (NHIs), equivalence has two irreducible components: structural equivalence, capturing identical permission profiles at a snapshot via graph fibration, and temporal equivalence, capturing recurring permission states via strongly connected components (SCCs) in a fiber transition graph. We call the equivalence classes under temporal equivalence privilege circuits.
We formalize a three-layer framework: (1) a spatial quotient of the permission graph via fibration, (2) a lineage partition organizing stable transition compartments, (3) windowed SCC analysis as a temporal quotient within lineages.
Empirical evaluation on a large Azure tenant supports the framework. Backtesting demonstrates that early observation of ratchet-type privilege circuits predicts long-term structural stability.

---


### 152. [Message Tuning Outshines Graph Prompt Tuning: A Prismatic Space Perspective](https://arxiv.org/abs/2606.03290)

**<font color=#1a73e8>作者：</font>** Yancheng Chen, Dun Ma, Shuai Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Foundation Models (GFMs), built upon the Pre-training and Adaptation paradigm, have emerged as a research hotspot in graph learning. For GNN-based GFMs, graph prompt tuning has become the prevailing adaptation method for downstream tasks. Although recent methods explain why graph prompt tuning works, how to rigorously measure its adaptation capacity remains an open problem. Addressing this problem is critical for understanding the capability limits of graph prompt tuning and for developing more powerful adaptation methods. In this paper, we propose Prismatic Space Theory (PS-Theory), a novel mathematical framework to quantify the capacity of adaptation methods, while focusing on establishing the upper bound for the adaptation capacity of graph prompt tuning. Building upon the proposed PS-Theory, we further introduce Message Tuning for GFMs (MTG), a lightweight approach that injects a small set of learnable message prototypes into each layer of the GNN backbone to adaptively guide message fusion without updating pre-trained weights. Through our PS-Theory, we prove that the adaptation capacity of MTG can exceed the theoretical upper bound of graph prompt tuning. Extensive experiments demonstrate that MTG consistently outperforms graph prompt baselines across diverse benchmark datasets, providing strong empirical support for our theoretical findings.

---


### 153. [SagaQA: A Multi-hop Reasoning Benchmark for Long-form Narrative Understanding in TV Series](https://arxiv.org/abs/2606.03301)

**<font color=#1a73e8>作者：</font>** Galann Pennec, Zhengyuan Liu, Nicholas Asher 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce SagaQA, a long-form video benchmark for multi-hop reasoning over full-length TV series. Existing video reasoning benchmarks often emphasize local understanding of adjacent frames or clips. SagaQA addresses this gap by requiring high-level comprehension of extended multimodal narratives in entire TV shows. A distinguishing feature of SagaQA is the granularity of its reasoning steps. Our dataset necessitates long-range reasoning hops to connect information across completely different episodes. This requires models to reason over entire events and actions, demanding a deep understanding of the show's narration and progression at a multimodal level. Motivated by recent progress in agentic methods, we further study how different planning strategies handle such complex reasoning. We categorize these approaches into three classes-Parallel, Sequential, and Hybrid planners-and evaluate their ability to generate coherent and complete reasoning plans. Our results on SagaQA suggest that hybrid planners consistently produce higher-quality plans and exhibit stronger capabilities for complex, high-level narrative understanding in TV shows.

---


### 154. [The Reliability Gap in Benchmark Auditing: Distribution Shift and Scale as Failure Modes of Contamination Detection](https://arxiv.org/abs/2606.03305)

**<font color=#1a73e8>作者：</font>** Wojciech Zarzecki, Jan Dubiński, Sebastian Cygert  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Benchmark contamination, where evaluation examples appear in a model's training data, threatens the validity of LLM assessment. Statistical tools for detecting training-data membership exist, but have been validated almost exclusively in controlled academic regimes: large, homogeneous pre-training corpora and transparent, single-stage training pipelines. Whether these methods remain reliable in realistic auditing scenarios remains unclear. We identify two under-studied failure modes: distribution shift, which arises when suspect and validation sets violate the IID assumption, and scale constraints, which arise because benchmarks are orders of magnitude smaller than pre-training corpora. We systematically evaluate three leading paradigms: LLM Dataset Inference, Post-Hoc Dataset Inference, and CoDeC across 27 models from multiple families (including Pythia, OLMo~2, and specialised cultural and medical LLMs) and scales (up to 27B). We then further extend our analysis to frontier industry models. Across 335 evaluations, only 199 yield correct outcomes. LLM Dataset Inference results in false positives under distribution shift, Post-Hoc Dataset Inference is underpowered at benchmark scale, and CoDeC provides only coarse provenance signals that are insufficient to verify individual benchmark splits. Our results reveal a systematic reliability gap between controlled validation and practical benchmark auditing, and show that statistical detection cannot yet replace transparent data provenance. We open-source our benchmark for further research.

---


### 155. [Learning Multi-Scale Hypergraph for High-Order Brain Connectivity Analysis](https://arxiv.org/abs/2606.03310)

**<font color=#1a73e8>作者：</font>** Jaeyoon Sim, Soojin Hwang, Seunghun Baek 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding complex interactions between brain regions is critical for early neurodegenerative disease classification such as Alzheimer's Disease (AD) and Parkinson's Disease (PD). While graph-based models are widely used to analyze brain networks, most existing approaches primarily focus on pairwise interactions between directly connected nodes, limiting their ability to capture higher-order dependencies across multiple regions. Although hypergraph-based methods have been proposed to model higher-order relations, many rely on predefined hyperedges or restrict learning to hyperedge weights, reducing flexibility and limiting their capacity to capture multi-resolution structural patterns. In this regard, we introduce an adaptive multi-scale hyperedge learning framework, i.e., MuHL, which constructs hierarchical node features and dynamically learns high-order interactions through continuous hyperedge construction over multi-resolution graph signals. Extensive experiments on multiple brain network benchmarks demonstrate that MuHL consistently improves disease classification performance across different stages, and further identifies key regions of interest (ROIs) and their group-wise interactions from the learned hyperedges that are associated with disease progression, highlighting its potential as a powerful tool for brain network analysis in neurodegenerative disorders.

---


### 156. [TASE: Truncation-Aware Semantic Embeddings for 3D Scene Understanding and Editing](https://arxiv.org/abs/2606.03314)

**<font color=#1a73e8>作者：</font>** Tim-Felix Faasch, Jochen Kall, Lucas Nunes 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-fidelity semantic 3D scene representations are crucial for numerous applications, including robotics, autonomous driving, and simulation. Beyond this, the ability to edit such representations enables developers to adapt these applications more easily to specific target scenarios. Current approaches provide limited support for controllable editing. We introduce TASE, a method that projects pretrained 2D semantic features into a truncation-aware embedding space to enable flexible 3D scene editing. Our method explicitly optimizes a feature space in which progressively reducing feature channels yields increasingly abstract semantic representations, while retaining more channels preserves fine-grained detail. Additionally, we improve multi-view consistency of the features using a scale- and translation-equivariance loss. The resulting truncation-aware embedding space enables text-driven edits to 3D scenes, providing explicit control over how strongly edits adhere to the original scene content and allowing more substantial modifications than prior methods. Moreover, we propose a finetuning stage for the editing diffusion model to mitigate artifacts caused by geometric changes. Experimental results demonstrate competitive performance in 3D scene editing, substantially outperforming prior methods on edits involving large geometric modifications.

---


### 157. [Validation-Gated Multi-Agent Governance for Online Adaptation of Thermal-Hydraulic Surrogate Models under Operating-Regime Shift](https://arxiv.org/abs/2606.03321)

**<font color=#1a73e8>作者：</font>** Doyeong Lim, Seungyoon Lee, In Cheol Bang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Artificial-intelligence surrogates can support second-by-second thermal-hydraulic forecasting, but models selected and frozen offline may become condition-locked once deployed outside their pretraining envelope. This study develops a guarded continual-adaptation framework for experimental thermal-hydraulic loop data in which role-separated agents - Monitor, Diagnosis, Adaptation, Safety-Auditor, and Orchestrator - diagnose error signatures, prioritize candidate model families, and review promotions, while deterministic champion-challenger gates and background shadow learning retain final authority over model replacement. Seven surrogate families were screened by blocked three-fold cross-validation, and a temporal Fourier neural operator was selected as the initial champion for 60-s-history-to-10-s-trajectory forecasting on two held-out transients, with three seeds per adaptive mode. Static deployment gave a channel-averaged MAE of 7.06 and a 56.8% warning-exceedance ratio; rule-based adaptation reduced MAE to 6.54, whereas shadow refresh alone remained close to Static. The MA-Full mode, in which the role-separated multi-agent council reviews every evaluated stream step, achieved the lowest mean error, 5.72, and 35.8% exceedance, corresponding to a 19.0% improvement over Static. Paired bootstrap intervals against Static excluded zero, although intervals among adaptive modes overlapped and the six paired units limit broad statistical claims. Validated promotions from the neural operator to Transformer and graph neural network indicate that logged, gate-controlled adaptation can support auditable surrogate evolution while deterministic gates retain deployment authority.

---


### 158. [Multi-Modal Graph Neural Network with Transformer-Guided Adaptive Diffusion for Preclinical Alzheimer Classification](https://arxiv.org/abs/2606.03322)

**<font color=#1a73e8>作者：</font>** Jaeyoon Sim, Minjae Lee, Guorong Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The graphical representation of the brain offers critical insights into diagnosing and prognosing neurodegenerative disease via relationships between regions of interest (ROIs). Despite recent emergence of various Graph Neural Networks (GNNs) to effectively capture the relational information, there remain inherent limitations in interpreting the brain networks. Specifically, convolutional approaches ineffectively aggregate information from distant neighborhoods, while attention-based methods exhibit deficiencies in capturing node-centric information, particularly in retaining critical characteristics from pivotal nodes. These shortcomings reveal challenges for identifying disease-specific variation from diverse features from different modalities. In this regard, we propose an integrated framework guiding diffusion process at each node by a downstream transformer where both short- and long-range properties of graphs are aggregated via diffusion-kernel and multi-head attention respectively. We demonstrate the superiority of our model by improving performance of pre-clinical Alzheimer's disease (AD) classification with various modalities. Also, our model adeptly identifies key ROIs that are closely associated with the preclinical stages of AD, marking a significant potential for early diagnosis and prevision of the disease.

---


### 159. [dstack-capsule: Pod-Level Remote Attestation for Confidential Workloads on Kubernetes](https://arxiv.org/abs/2606.03323)

**<font color=#1a73e8>作者：</font>** Yang Yang, Kevin Wang, Yuanhai Luo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rise of LLM-as-a-Service and other confidential cloud workloads demands cryptographic proof that user data is processed in a trusted, untampered environment. Existing solutions, notably Confidential Containers (CoCo), enforce a strict "one Pod per VM" model that attests only the Guest OS stack, leaving container-level identity unverified and incurring prohibitive per-VM resource overhead. We present dstack-capsule, a Kubernetes platform that enables Pod-level remote attestation on Intel TDX by allowing multiple Pods to share a single Confidential VM while each retains independent, hardware-backed proof of identity. Our key insight is a two-layer attestation architecture: static platform measurements are frozen in RTMR[3] via an irreversible privilege fuse, while dynamic Pod identities (pod_uid, pod_spec_hash, workload_id) are embedded in the TDX Quote's report_data field and signed by hardware on every request. dstack-capsule introduces (1) a Pod-level attestation protocol binding Pod spec digests to hardware-signed Quotes; (2) a privilege fuse mechanism that atomically transitions a node from setup mode to secure mode; (3) a multi-layer sandbox spanning storage, runtime, admission, API, and network isolation layers; and (4) a complete open-source implementation based on Kubernetes 1.32, Intel TDX, and Sysbox. We evaluate the security properties, attestation correctness, and performance characteristics of dstack-capsule, demonstrating that it achieves Pod-granularity verification without the resource overhead of per-VM isolation.

---


### 160. [The Violation Situation Pattern: A Knowledge-Graph Pattern for Compliance Violations](https://arxiv.org/abs/2606.03326)

**<font color=#1a73e8>作者：</font>** Nima Kamali Lassem, Fuqi Song, Seyid Amjad Ali  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Compliance pipelines detect violations as transient query results and do not keep the violation itself as a persistent graph object with review state, affected entities, or audit history. The Violation Situation Pattern (VSP) closes this gap. Building on the Situation pattern of Gangemi and Mika, VSP reifies each detected violation as a graph node with a rule identifier, a temporal validity interval, a lifecycle state, and evidence links to the entities involved. Lifecycle transitions are stored as immutable, PROV-O-aligned events, so audit history is a graph traversal. We instantiate VSP in a legal entity and contract lifecycle property graph and operationalize four deontic rules (V1 unauthorized signature, V2 expired mandate, V3 missing confidentiality clause, V4 missing breach-notification clause) through an FCL->Cypher->MERGE pipeline. We check V1 and V2 against BODACC corporate-officer publications, evaluate V4 on 73 GDPRhub enforcement decisions, and run a SHACL cross-formalism check on V3 and V4. The central finding is rule-body independence: extending V4 from clause-presence to deadline checking raises F1 from 0.312 to 0.602, while the pattern's identity, lifecycle, and evidence semantics stay the same. This separates a pattern contribution from a detector contribution, so detection logic can evolve without invalidating accumulated audit history.

---


### 161. [InfoMem: Training Long-Context Memory Agents with Answer-Conditioned Information Gain](https://arxiv.org/abs/2606.03329)

**<font color=#1a73e8>作者：</font>** Tiancheng Han, Yong Li, Wuzhou Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-context tasks require LLMs to identify and preserve answer-relevant information from large contexts. Chunk-wise memory agents address this issue by sequentially reading document chunks, updating a compact memory, and generating the final answer from the accumulated memory. However, existing RL-based chunk-wise agents either rely on sparse final-answer rewards or use lexical intermediate rewards for memory and retrieval actions. These signals supervise task success or local overlap, but do not directly evaluate whether the final memory supports the ground-truth answer. We propose InfoMem, a reward mechanism for training chunk-wise memory agents that evaluates final-memory utility using answer-conditioned information. InfoMem measures how much the final memory increases the model's per-token log-likelihood of the ground-truth answer. To stabilize RL optimization, InfoMem applies this signal only to successful trajectories and normalizes it before reward composition. Under the same GRPO framework and training budget, InfoMem improves long-context memory-agent performance over comparable memory-agent RL baselines. Analyses show that effective final-memory rewards should operate on successful trajectories, be normalized before reward composition, and be conditioned on the answer rather than the query. Our code is available at this https URL.

---


### 162. [Tailoring Strictly Proper Scoring Rules for Downstream Tasks: An Application to Causal Inference](https://arxiv.org/abs/2606.03332)

**<font color=#1a73e8>作者：</font>** Roman Plaud, Alexandre Perez-Lebel, Antoine Saillenfest 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Probabilistic models are typically trained using task-agnostic objectives like log-loss, which can lead to significant errors in downstream estimation. This disconnect is especially critical in Inverse Probability Weighting (IPW) for causal inference, where propensity score errors near $0$ and $1$ often lead to high bias and variance. We propose a principled framework for deriving task-specific strictly proper scoring rules by matching the local curvature of the downstream error metric. We apply this to the Average Treatment Effect (ATE) estimation, deriving a closed-form loss and its corresponding canonical probability mapping that can be readily integrated with any model like a neural network or a gradient boosting algorithm. Extensive evaluations on causal inference benchmarks demonstrate that our tailored objective consistently outperforms standard likelihood-based and covariate-balancing approaches.

---


### 163. [Lingo_Research_Group at SemEval-2026 Task 9: Evaluating Prompt Variants for Polarization Detection](https://arxiv.org/abs/2606.03334)

**<font color=#1a73e8>作者：</font>** Pritam Kadasi, Anuj Tiwari, Mayank Singh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Our submission presented in this paper is for SemEval-2026 Task 9: Multilingual Text Classification Challenge - Polarization Detection and it covers all three subtasks: (1) binary polarization detection, (2) polarization type classification and (3) polarization manifestation identification. We adopt a systematic approach of research on short designed prompts by considering twelve designed prompts that are different in terminology clarity, detail of the definition, guidance of reasoning and in-context examples use. The experiments are conducted using aya-101 and Gemma3-27B, with the latter chosen for the submission at the end of the development through performance considerations. Our system has an average macro level F1-score of 0.762 on Subtask 1, 0.587 on Subtask 2 and 0.444 on Subtask 3 with the average accuracy of 0.819, 0.678 and 0.498, respectively, on the official test set averaged among 22 languages, respectively. With cross-task and cross-lingual analysis, we demonstrate that prompt-based approaches can be used effectively to detect coarse grained polarization but encounter more and more difficulties as far as fine-grained and multi-label sociolinguistic classification is concerned.

---


### 164. [IdEst: Assessing Self-Supervised Learning Representations via Intrinsic Dimension](https://arxiv.org/abs/2606.03338)

**<font color=#1a73e8>作者：</font>** Julie Mordacq, Vicky Kalogeiton, Steve Oudot  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning (SSL) has emerged as a powerful paradigm for learning meaningful representations from unlabeled data. However, the standard protocol for evaluating these representations, linear probing, is computationally expensive, sensitive to hyperparameters, and provides limited insight into the geometric structure of the representation space. In this work, motivated by connections between neural network generalization and intrinsic dimension (ID) we propose IdEst, a method for estimating the ID of SSL representations via the Minimum Spanning Tree dimension estimator ($\mathrm{dim}_\mathrm{MST}$). Across diverse datasets, architectures, and SSL pretraining objectives, we show that IdEst strongly correlates with downstream linear probe performances. Furthermore, we demonstrate that IdEst enables efficient hyperparameter selection, significantly reducing the computational cost compared to supervised alternatives. Our results highlight intrinsic dimensionality as a principled geometric proxy for assessing SSL representations, complementing standard supervised probing protocols.

---


### 165. [Beyond Semantics: Modeling Factual and Affective Perceptual Experiences from Vision-Language Data](https://arxiv.org/abs/2606.03345)

**<font color=#1a73e8>作者：</font>** Youssef Mohamed, Kenneth Ward Church, Mohamed Elhoseiny  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present P-Topics (Perception Topics) modeling, a novel problem for understanding how images are perceived affectively and across cultures. The goal is to (1) discover and model the different perception experiences in a dataset of images and captions, where each experience is defined by an objective factual and a subjective affective aspect, and (2) associate images to their relevant perception experiences. We introduce **PercepT** (**Percep**tion topic **T**ransformer), a two-stage architecture that tackles P-Topics modeling. In the formation stage, percepT discovers *P-Topics* as visual-textual clusters using an unsupervised training objective, and dynamically selects the number of clusters to match the perceptual richness of the dataset. In the mapping stage, it learns *P-Topic mapping functions* via attention pooling to associate images to their respective clusters. On ArtELingo, PercepT achieves a silhouette score of **0.97** compared to **0.37** from the closest baseline reflecting better perceptual clusters. PercepT also achieves an AUC score of **0.94** compared to **0.77** showing better mapping to perceptual clusters. Human evaluation confirms that PercepT captures semantically meaningful perception experiences and significantly outperforms existing methods. Our implementation will be made public.

---


### 166. [AugMask: Training Diffusion Models on Incomplete Tabular Data via Stochastic Augmentation and Masking](https://arxiv.org/abs/2606.03347)

**<font color=#1a73e8>作者：</font>** Jungkyu Kim, Taeyoung Park, Kibok Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Score-based diffusion models have emerged as prominent deep generative models; however, their application to tabular data remains challenging because their backbones assume fully specified inputs, whereas real-world tabular data often contain missing values. We propose AugMask, a plug-and-play training framework that adapts missing-unaware backbones to incomplete data by separating conditioning from supervision. AugMask 1) constructs numeric inputs via conditional stochastic augmentation using lightweight auxiliary models, and 2) applies denoising supervision only to observed coordinates. In effect, augmented missing entries serve as uncertain conditioning context rather than training targets. We connect this training rule to a Rao--Blackwellized objective and show that marginalizing missing entries yields a variance-weighted sensitivity penalty, discouraging over-reliance on uncertain completions. Across diverse datasets and missingness regimes, AugMask enables standard diffusion-based tabular generators to outperform specialized missing-aware baselines.

---


### 167. [SynCred-Bench: Benchmarking Synthetic Credibility in AI-Generated Visual Misinformation](https://arxiv.org/abs/2606.03348)

**<font color=#1a73e8>作者：</font>** Junxiao Yang, Minghao Zhang, Xiaoce Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent generative models can now produce visual artifacts with realistic embedded text and layouts, creating a new misinformation threat: synthetic credibility. We introduce SYNCRED-Bench, a benchmark of 600 AI-generated misinformation images balanced across six credible-form categories and seven fine-grained circulation styles, together with FP450, a real-image negative set for measuring false positives. Extensive evaluation shows that existing systems remain unreliable: under a 5% false-positive-rate constraint, 15 MLLMs achieve only 10.5% true positive rate (TPR), open-source AIGC detectors achieve less than 5%, and commercial APIs reach 57.6%. Human annotators also struggled to identify synthetic credibility, reaching only 63% TPR. These findings establish synthetic credibility as a severe and underexplored visual misinformation challenge, and provide a benchmark for developing detectors that reason beyond superficial credibility cues.

---


### 168. [APIC: Amortized Physics-Informed Calibration using Neural Processes](https://arxiv.org/abs/2606.03355)

**<font color=#1a73e8>作者：</font>** Aishwarya Venkataramanan, Sai Karthikeya Vemuri, Joachim Denzler  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics models are inherently imperfect due to misspecified or missing mechanisms, resulting in systematic discrepancies between model predictions and real-world observations. The Kennedy-O'Hagan (KOH) framework addresses this issue through explicit discrepancy modeling. However, its non-amortized, per-instance formulation limits scalability across families of related systems. We introduce Amortized Physics-Informed Calibration (APIC), a population-level extension of KOH that leverages Neural Processes to perform scalable Bayesian inference across realizations. Our framework employs a two-branch latent architecture to disentangle instance-specific physical parameters from shared, state-dependent structural discrepancies. By integrating differentiable physics into an amortized inference backbone, APIC enables rapid calibration of unseen realizations from sparse observations while quantifying uncertainty. Experiments on the damped spring oscillator, the Lotka-Volterra system, and the advection-diffusion PDE with misspecified physics demonstrate improved parameter recovery and consistent identification of the systemic discrepancy structure compared to other calibration approaches.

---


### 169. [The Unsampled Truth: Psychometrics in SLMs Measure Prompt Artifacts, Not Psychological Constructs](https://arxiv.org/abs/2606.03357)

**<font color=#1a73e8>作者：</font>** Nils Schwager, Christoph Hau, Simon Münker 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When prompting SLMs for psychometric assessments, researchers assume the outputs reflect semantic reasoning. We evaluate this premise across 13 open-weights models (0.6B to 14B parameters) using a prompt variation framework that separates semantic signals from prompt artifacts. By systematically varying personas, instructions, items, and option symbols, we find that artifactual variance frequently overpowers the semantic signal. In these cases, models predominantly reflect prompt compliance rather than simulated psychological traits. While these findings limit SLM utility in psychometrics, our framework provides a diagnostic tool to identify destructive artifacts and isolate semantic understanding for future frontier-model research.

---


### 170. [The Impact of Temporal Granularity on Socio-Demographic Inference from Household Load Profiles](https://arxiv.org/abs/2606.03358)

**<font color=#1a73e8>作者：</font>** Dejan Radovanovic, Maximilian Schirl, Andreas Unterweger 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Smart meter data can reveal sensitive socio-demographic characteristics of households, raising privacy concerns. While this risk has been demonstrated at fixed granularities, the role of temporal resolution in shaping inference performance remains insufficiently explored. This paper addresses this gap by analyzing how load profiles with granularities from 15 minutes to 7 days affect the predictability of eight socio-demographic attributes in a dataset of 1,589 households over one year. We introduce an evaluation framework where classifiers are trained on year-round data but tested on arbitrary weeks, forcing generalization across seasonal and weekly variations. Our results show three main findings. First, while coarsening granularity reduces predictive accuracy, two plateaus emerge: performance is stable between 15 minutes and 1 hour, and again between 1 and 7 days. This reveals opportunities for data minimization without sacrificing utility. Second, interpretable handcrafted and tsfresh features remain competitive with CNN-based autoencoder embeddings, while XGBoost consistently outperforms alternative classifiers. Third, feature importance analysis highlights differences between static and dynamic attributes: dwelling size can be inferred even from coarse data, whereas swimming pool usage requires fine-grained temporal signals. Overall, our study provides new insights into the privacy-utility trade-off in smart metering, showing how temporal resolution, feature extraction, and classifier choice jointly influence socio-demographic inference.

---


### 171. [Mitigating False Credit Propagation: Probabilistic Graphical Reward Aggregation for Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2606.03361)

**<font color=#1a73e8>作者：</font>** Can Lv, Mingju Chen, Heng Chang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rubric-based rewards are increasingly used for open-ended language model post-training, but criterion-level scores are often aggregated as independent utilities. This flat scalarization ignores rubric-specified prerequisite and activation relations among criteria, allowing reward or penalty to be counted even when the condition that licenses it is absent. We call this structural reward-aggregation failure \textbf{False Credit Propagation} (FCP). To address this limitation, we propose \ourname (\textbf{G}raphical \textbf{E}vent \textbf{A}ggregation for \textbf{R}ubric rewards), a probabilistic graphical framework for dependency-aware rubric aggregation. \ourname models each criterion outcome as a latent Bernoulli event in a typed rubric graph, propagates soft suppression from unsupported parent events to their children, and aggregates the resulting event probabilities into a normalized expected signed utility. This yields a linear-time reward computation that can be plugged into standard rubric-based RL pipelines without changing the outer optimization algorithm. Experiments on HealthBench, WritingBench, and PLawBench with two policy backbones show that \ourname consistently improves over flat aggregation and deterministic gating, achieving relative gains of up to 15.5\% over flat aggregation. FCP diagnostics further show that \ourname reduces leakage by 96.5\% relative to flat aggregation while preserving more licensed downstream utility than deterministic gating. Our code is publicly available at this https URL.

---


### 172. [EntSQL: A Benchmark for Grounding Text-to-SQL in Long-Context Enterprise Knowledge](https://arxiv.org/abs/2606.03363)

**<font color=#1a73e8>作者：</font>** Chengxi Liao, Tao Xu, Zulong Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text-to-SQL enables natural language access to databases, and recent LLMs have substantially advanced its capabilities. Existing benchmarks such as Spider, BIRD, and Spider~2.0 evaluate schema generalization, large-scale databases, and realistic workflows, but largely overlook enterprise scenarios where SQL generation depends on private business knowledge, such as internal metrics, reporting conventions, and organizational rules. We introduce EntSQL, an enterprise-oriented Text-to-SQL benchmark for evaluating long-context grounding over proprietary business documents. EntSQL contains 1,066 aligned Chinese-English semantic examples across five business domains, with most examples requiring domain knowledge beyond the question and schema and involving complex SQL structures. On English inputs, the best evaluated system reaches only 15.9\% when long-form documents are provided, highlighting the difficulty of grounding SQL generation in enterprise knowledge.

---


### 173. [Link Prediction or Perdition: the Seeds of Instability in Knowledge Graph Embeddings](https://arxiv.org/abs/2606.03365)

**<font color=#1a73e8>作者：</font>** Guillaume Méroué, Fabien Gandon, Pierre Monnin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Embedding models (KGEMs) constitute the main link prediction approach to complete knowledge graphs. Standard evaluation protocols emphasize rank-based metrics such as MRR or Hits@$K$, but usually overlook the influence of random seeds on result stability. Moreover, these metrics conceal potential instabilities in individual predictions and in the organization of embedding spaces. In this work, we conduct a systematic stability analysis of multiple KGEMs across several datasets. We find that high-performance models actually produce divergent predictions at the triple level and highly variable embedding spaces. By isolating stochastic factors (i.e., initialization, triple ordering, negative sampling, dropout, hardware), we show that each independently induces instability of comparable magnitude. Furthermore, for a given model, hyperparameter configurations with better MRR are not guaranteed to be more stable. Moreover, voting, albeit a known remediation mechanism, only provides a limited enhancement of stability. These findings highlight critical limitations of current benchmarking protocols, and raise concerns about the reliability of KGEMs for knowledge graph completion.

---


### 174. [P\textsuperscript{2}-DPO: Grounding Hallucination in Perceptual Processing via Calibration Direct Preference Optimization](https://arxiv.org/abs/2606.03376)

**<font color=#1a73e8>作者：</font>** Ruipeng Zhang, Zhihao Li, Haozhang Yuan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hallucination has recently garnered significant research attention in Large Vision-Language Models (LVLMs). Direct Preference Optimization (DPO) aims to learn directly from the corrected preferences provided by humans, thereby addressing the hallucination issue. Despite its success, this paradigm has yet to specifically target the perceptual bottleneck in attended regions or address insufficient Visual Robustness against image degradation. Furthermore, existing preference pairs are often vision-agnostic and their inherently off-policy nature limits their effectiveness in guiding model learning. To address these challenges, we propose Perceptual Processing Direct Preference Optimization (P\textsuperscript{2}-DPO), a novel training paradigm in which the model generates and learns from its own preference pairs, thereby directly addressing the identified visual bottlenecks while inherently avoiding the issues of vision-agnostic and off-policy data. It introduces: (1) an on-policy preference pairs construction method targeting Focus-and-Enhance perception and Visual Robustness, and (2) a well-designed Calibration Loss to precisely align visual signals with the causal generation of text. Experimental results demonstrate that with a comparable amount of training data and cost, P\textsuperscript{2}-DPO outperforms strong baselines that rely on costly human feedback on benchmarks. Furthermore, evaluations on Attention Region Fidelity (ARF) and image degradation scenarios validate the effectiveness of P\textsuperscript{2}-DPO in addressing perceptual bottleneck in attended regions and improving Visual Robustness against degraded inputs.

---


### 175. [Intellectual Humility as a Cognitive Filter for AI-Generated Health Misinformation. An Evolutionary Perspective on Epistemic Vigilance](https://arxiv.org/abs/2606.03377)

**<font color=#1a73e8>作者：</font>** Marcin Rządeczka, Maciej Wodziński, Kacper Zacharski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present experimental findings from a study (N=99) examining how intellectual humility (IH), i.e., the metacognitive awareness of epistemic limitations, affects the evaluation of AI-generated health dialogues varying in scientific rigor. Participants were randomly assigned to evaluate one of three dialogues about exercise and mental health: scientifically accurate, moderately pseudoscientific, or strongly pseudoscientific. Results reveal that IH functions as a selective cognitive filter. Individuals with higher humility scores rated pseudoscientific content as significantly less credible, while showing no correlation with credibility assessments of accurate content. Crucially, humility did not predict the ability to identify AI as the source of dialogues, suggesting that epistemic vigilance operates on content quality rather than source attribution. We interpret these findings through an evolutionary lens, proposing that IH represents an ancestral adaptation for navigating informationally uncertain environments. It remains effective at detecting exploitation attempts in AI-generated content, despite humans lacking evolved mechanisms for detecting AI sources. The study contributes to understanding how foundation models might improve or undermine human epistemic defenses, especially in health communication contexts.

---


### 176. [AI Model Extraction Attacks: Bypassing Single-Client Assumptions in Defenses](https://arxiv.org/abs/2606.03381)

**<font color=#1a73e8>作者：</font>** Maxime Schwarzer, Johannes F. Loevenich, Gustavo Sánchez 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Ensuring the protection of Artificial Intelligence (AI) models deployed in military Command and Control (C2) systems and critical infrastructure is essential for maintaining information superiority. Model Extraction Attacks (MEAs) pose a significant threat, as they enable adversaries to replicate proprietary models, compromise protected information, and prepare offline adversarial attacks. However, current defense strategies predominantly rely on the Single Client Assumption (SCA), which is the implicit assumption that attacks originate from isolated identities. This work systematically demonstrates that the SCA is fundamentally invalid in the presence of coordinated threat actors, such as Advanced Persistent Threats (APTs). We introduce a modular, open-source framework called CerberusAI for reproducible model-stealing research, and use it to simulate distributed attack scenarios. Our empirical evaluation shows that well-established defense mechanisms, such as Protecting Against Deep Neural Network Model Stealing Attacks (PRADA), can be bypassed by basic round-robin query distribution strategies, resulting in a significant reduction in detection performance. Furthermore, we demonstrate that even global aggregation approaches can be rendered operationally useless through adaptive traffic mixing. These results highlight the need for a paradigm shift towards stateful, identity-independent defense architectures in the field of model extraction attacks. This paper was originally presented at the International Conference on Military Communication and Information Systems (ICMCIS), organized by the Information Systems Technology (IST) Scientific and Technical Committee, IST-224-RSY - the ICMCIS, held in Bath, United Kingdom, 12-13 May 2026 and won the best paper award.

---


### 177. [Local Guidance, Global Impact: Gaussian-Reshaped Trust Region Unlocks Behavior Transitions](https://arxiv.org/abs/2606.03382)

**<font color=#1a73e8>作者：</font>** Bingxu Liu, Jiashun Liu, Johan Obando-Ceron 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While Proximal Policy Optimization (PPO) demonstrates strong performance in stationary settings, we show that its standard optimization paradigm struggles in continual and non-stationary environments. The failure does not stem from insufficient model capacity or overly restrictive clipping. Instead, PPO performs persistent, directionally inefficient local updates, which indicates a lack of geometry-aware guidance for accumulating meaningful behavioral change and ultimately hindering transitions toward new behavior patterns. Although divergence-based regularization introduces partial geometric awareness, its monotonically increasing penalties implicitly discourage large policy deviations, even when such shifts are necessary for effective adaptation. To address this limitation, we propose Gaussian Trust Region Policy Optimization (GTR), which reshapes the trust region using a Gaussian kernel. The resulting constraint is bounded and non-monotonic, providing strong local stability while progressively relaxing under sustained high-advantage updates. To further improve robustness, we introduce a Mixture Gaussian Anchor that adapts to recent policy trajectories, reducing variance induced by stale references. GTR is architecture-agnostic and achieves strong performance across games, simulated robotic control, open-world exploration, and language model post-training. These results demonstrate that geometry-aware trust-region design can be a promising direction for robust reinforcement learning in complex non-stationary environments. Our code is available at this https URL.

---


### 178. [Operationalizing Cyber Attack Prediction: A Gap-Prioritized Framework with Dataset and Model Selection Guidelines](https://arxiv.org/abs/2606.03386)

**<font color=#1a73e8>作者：</font>** Aminu Muhammad Auwal  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> While AI and machine learning for cyber attack prediction have advanced, a critical gap persists between theoretical research and practical operational deployment. Building on Ankalaki et al. (2025), this paper provides a comprehensive analysis of 150+ benchmark datasets and 200+ studies to identify and prioritize five implementation hurdles: (1) temporal dataset obsolescence, (2) narrow attack scope, (3) real-time model interpretability, (4) inadequate adversarial robustness, and (5) privacy/ethical concerns. We introduce a novel gap-prioritization framework that evaluates these limitations based on detection impact, implementation cost, and remediation time. Our analysis identifies dataset obsolescence and adversarial robustness as the highest-priority gaps, while highlighting model interpretability as the most cost-effective path for resource-constrained environments. To bridge the research-practice divide, we provide a practical implementation roadmap and a dataset quality assessment framework that classifies 45 benchmarks into production-ready, research-only, and unusable categories. This work translates academic findings into actionable decision-support tools for robust, production-oriented AI-driven cyber defense.

---


### 179. [Bastet: A Fine-Grained Expert-Labeled Dataset for DeFi Smart Contract Vulnerability Detection](https://arxiv.org/abs/2606.03387)

**<font color=#1a73e8>作者：</font>** Wan-Hsuan Hsu, Wei-Hsin Wang, Cheng-Yu Liou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Smart contract vulnerabilities in Decentralized Finance (DeFi) protocols resulted in over 1.49 billion USD in confirmed losses in 2024 alone, across 192 incidents [1]. As LLM-based vulnerability detection emerges as a promising approach to address these threats, the quality of evaluation datasets has become a critical bottleneck. Existing datasets suffer from three fundamental problems: they are built on outdated Solidity versions (e.g., v0.4) that no longer reflect modern DeFi contracts [5][6][7]; they rely on automated or LLM-generated annotations that introduce hallucination-driven label noise [9][10]; and they apply coarse single-layer labeling that fails to capture the semantic complexity of real-world business logic vulnerabilities [6][7][11][12]. We present Bastet, an expert-labeled DeFi smart contract vulnerability dataset that addresses all three problems through real-world audit findings (2021-2024), human expert annotation with discussion-based consensus, and a two-layer taxonomy of 46 Tags and 77 Subtags. Bastet comprises 4,402 findings collected from 394 Code4rena competitive audit reports spanning April 2021 to November 2024, of which 849 findings are fully annotated by white-hat security researchers from the DeFiHackLabs community. All annotations are produced through a two-annotator consensus workflow, ensuring label accuracy grounded in real-world vulnerability root causes.

---


### 180. [Flicker-DDPM: Accelerating Denoising Diffusion via 1/f Colored Noise Injection](https://arxiv.org/abs/2606.03393)

**<font color=#1a73e8>作者：</font>** Kexiang Mao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a novel diffusion model, Flicker-DDPM, which incorporates flicker (1/f) noise inspired by self-organized criticality (SOC), a widely observed phenomenon in natural systems. Unlike denoising diffusion probabilistic models (DDPMs), which employ isotropic white noise in the forward process, Flicker-DDPM adopts colored noise with power-law spectra to better match the spectral statistics of natural images, whose power spectra typically follow P(k) proportional to 1/k^{\alpha}. To this end, we develop a colored-noise module based on a spatial correlation kernel, {\sigma}(d) = (d + 1)^{-\eta}, and theoretically establish that adjusting {\eta} controls the spectral exponent {\alpha} of the generated 1/f{\alpha} noise, enabling adaptation to datasets with diverse spectral characteristics. On CIFAR-10, Flicker DDPM matches or surpasses the generation quality of a standard DDPM baseline using 3.33 times fewer sampling steps, with negligible additional computational cost per step. We further develop a frequency-domain linear theory demonstrating that spectrally matched colored noise linearizes the reverse trajectory, theoretically explaining the observed sampling acceleration.

---


### 181. [Causal Evidence of Stack Representations in Modeling Counter Languages Using Transformers](https://arxiv.org/abs/2606.03398)

**<font color=#1a73e8>作者：</font>** Nishit Singh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Formal languages have proven to be effective conduits to understand the inner mechanisms of transformers. Past work has shown that transformers trained on next token prediction over counter languages learn representations consistent with an underlying stack structure. Beyond representational analysis, this paper investigates the causal role of these representations. Linear probes are trained to predict the stack depth at each token from the model's hidden states, and a principal representation direction is extracted from the probe. Ablation of this direction from the model causes sequential accuracy to collapse to near 0%, providing strong empirical evidence that the stack representation is not just learned, but is causally necessary for model performance.

---


### 182. [Towards Characterizing Scientific Image Utility and Upgradability](https://arxiv.org/abs/2606.03401)

**<font color=#1a73e8>作者：</font>** WenZhe Li, Qihang Yan, Liang Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scientific images function as critical evidence in research communication, yet their integrity faces unprecedented threats from AI-generated content that introduces subtle but consequential errors. Existing evaluation paradigms prove inadequate: perceptual quality metrics poorly correlate with scientific validity, while language models lack domain-specific verification capabilities. To address this gap, we propose the \textbf{S}cientific \textbf{I}mage \textbf{U}tility and \textbf{U}pgradability \textbf{A}ssessment (\textbf{SIU$^2$A}) framework, which introduces two complementary dimensions for scientific image evaluation. \textbf{Utility} encompasses \textit{error detection} (identifying scientific inaccuracies) and \textit{correction feasibility} (assessing whether errors can be reliably repaired). \textbf{Upgradability} measures the quality of correction. We categorize scientific image corruption into four fundamental types: Detail Distortion, Incompleteness, False Content, and Entity Confusion. Based on this taxonomy, we construct SIU$^2$A-Benchmark, a dataset with expert annotations for error identification and repair. The framework implements a two-stage evaluation protocol: the \textit{Utility} stage evaluates error detection capability and repair instruction generation, while the \textit{Upgradability} stage assesses whether corrections faithfully restore scientific validity without compromising existing accurate information. Experiments reveal that current multimodal systems exhibit significant limitations in both scientific error assessment and faithful correction, exposing a fundamental gap between visual perception and scientific usability.

---


### 183. [Mamba-Enhanced Implicit Motion Learning for Audio-Driven Portrait Animation](https://arxiv.org/abs/2606.03402)

**<font color=#1a73e8>作者：</font>** Xuan Wei, Jiahui Chen, Kaiheng Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-driven human motion video generation aims to synthesize realistic and temporally coherent human animations from a single static image, with applications in talking-head synthesis, co-speech gesture generation, and dynamic presentations. Moving beyond conventional keypoint-based methods that often struggle to capture subtle motion dynamics, We propose a novel implicit-motion framework for generating realistic and temporally coherent human motion videos from a single static image and audio. Our approach uses a two-stage pipeline that decouples motion prediction from rendering. The first stage integrates appearance priors and hierarchical depth cues into a region-aware attention mechanism to model latent motion features. The second stage employs a Mamba-enhanced diffusion model to directly predict these features from audio and the source image, enabling unsupervised learning of fine-grained motion patterns. This decoupled architecture enhances flexibility and efficiency. Trained on a new 380-hour high-quality dataset, our method outperforms prior work across multiple public benchmarks and our collected data in accuracy, naturalness, and temporal coherence, setting a new state-of-the-art.

---


### 184. [SAMatcher: Co-Visibility Modeling with Segment Anything for Robust Feature Matching](https://arxiv.org/abs/2606.03406)

**<font color=#1a73e8>作者：</font>** Xu Pan, Qiyuan Ma, Mingyue Dong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable correspondence estimation is a fundamental problem in image processing, underpinning applications such as Structure from Motion, visual localization, and image registration. Existing learning-based methods have significantly improved local feature representations, yet most still operate at the pixel or patch level and lack explicit modeling of regions that are jointly visible across views. We propose SAMatcher, a feature matching framework that formulates correspondence estimation through co-visibility modeling. Instead of directly matching local features, SAMatcher first predicts co-visible region masks and bounding boxes as structured priors for correspondence estimation. Built upon the Segment Anything Model (SAM), it introduces a symmetric cross-view interaction mechanism that enables bidirectional feature exchange and cross-view semantic alignment. We further develop a unified supervision scheme that jointly optimizes mask prediction and box localization through mask learning, box regression, and mask-box consistency constraints. Extensive experiments on challenging benchmarks demonstrate substantial improvements over existing matching pipelines, particularly under large viewpoint and scale variations. Our results show that foundation models originally designed for monocular segmentation can be effectively extended to multi-view correspondence reasoning through explicit co-visibility modeling, offering a new perspective on structured representation learning for image matching. Code and project page: this https URL

---


### 185. [Lexicons and grammars for language processing: industrial or handcrafted products?](https://arxiv.org/abs/2606.03412)

**<font color=#1a73e8>作者：</font>** Eric Laporte  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> During the recent years, the use of linguistic data for language processing increased progressively. Such data are now commonly called language resources. Most of the language resources used for this purpose are collections of texts as the Brown Corpus and the Penn Treebank, but electronic lexicons (WordNet, FrameNet, VerbNet, ComLex, Lexicon-Grammar...) and formal grammars (TAG...) developed recently. Most processes of construction of lexicons and grammars are manual, whereas the construction of corpora has always been highly automated. However, more and more specialists of language processing realize that the information content of lexicons and grammars is richer than that of corpora, and hence the former make more elaborate processing possible. The difference in construction time is likely to be connected with the difference in information content: the handcrafting of lexicons and grammars by linguists would make them more informative than automatically generated data. This situation can evolve into two directions: either specialists of language technology get progressively used to handling manually constructed resources, which are more informative and more complex, or the process of construction of lexicons and grammars is automated and industrialized, which is the mainstream perspective. Both evolutions are already in progress, and a tension exists between them. The relation between linguists and computer scientists depends on the future of these evolutions, since the first implies training and hiring numerous linguists, whereas the other depends essentially on solutions elaborated by computer engineers. The aim of this article is to analyse practical examples of the language resources in question, and to discuss about which of the two trends, handcrafting or generating industrially, or a combination of both, can give the best results or is the most realistic.

---


### 186. [MeDxAgent: Multi-Agent Consultation for Interactive Medical Diagnosis](https://arxiv.org/abs/2606.03416)

**<font color=#1a73e8>作者：</font>** Akshat Sanghvi, Naren Akash, Raza Imam 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for health-related decision support. Yet most evaluations treat diagnosis as a single-shot task with complete information provided upfront, often as a multiple-choice selection. This diverges from clinical practice, where diagnosis is interactive and open-ended, involving sequential hypothesis refinement through targeted questioning. We address this gap. We build MeDxBench, a large-scale benchmark of 4,421 clinical cases across 20 specialties. We further propose MeDxAgent, a multi-agent consultation system for interactive diagnosis, and systematically study its prompt-, flow- and agent-level design choices. MeDxAgent achieves a 10.3% accuracy gain over the baseline on MeDxBench, closing 52.3% of the gap to a full-information oracle. We find that specific design choices: collecting demographics first, passing summarized dialogue for diagnosis, and feeding candidate diagnoses for targeted questioning, improve accuracy, mirroring how physicians reason, though their effect emerges fully only in combination. Code and dataset will be released upon publication.

---


### 187. [A unified multi-task framework enables interpretable chest radiograph analysis](https://arxiv.org/abs/2606.03417)

**<font color=#1a73e8>作者：</font>** Lijian Xu, Ziyu Ni, Xinglong Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While multimodal deep learning has advanced medical imaging analysis, existing black-box systems \textcolor{black}{may remain confined to isolated tasks, often overlooking} the trust-sensitive nature of clinical diagnosis as a multi-task process. We propose IMT-CXR (Interpretable Multi-task Transformer for Chest X-ray Analysis), a framework that emulates radiologists' diagnostic workflow through three evidence-driven stages: 1) Disease recognition; 2) Attribute characterization (e.g., size, location, severity quantification); 3) Evidence-integrated report generation with traceable decision pathways. The framework employs a unified transformer architecture optimized via medical-domain instruction tuning, sequentially executing four clinical tasks: multi-label disease classification, lesion localization, anatomical segmentation, and radiology report generation. Experimental validation demonstrates competitive performance on ten CXR benchmarks under direct inference and fine-tuning settings. In a blinded evaluation of 160 historical reports from four medical centers, three radiologists rated 66\% of AI-generated reports as comparable to or surpassing original clinical reports in diagnostic clarity, highlighting the framework's translational potential. By establishing traceable diagnostic pathways from anatomical findings to conclusions, this work bridges the gap between AI technical metrics and clinical utility, advancing trustworthy AI systems in medical imaging.

---


### 188. [PHAF-Personalized Hand Avatars in a Flash](https://arxiv.org/abs/2606.03420)

**<font color=#1a73e8>作者：</font>** Meghana Shankar, Akanxit Upadhyay, Anmol Namdev 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present PHAF-Personalized Hand Avatars in a Flash, a personalized photo-realistic hand avatar which provides high quality multi-view renders from just two images (dorsal and palmar views).Unlike slow optimization-based techniques, PHAF generates fast personalized textures for real-time deployment on edge devices. Our approach combines semantic guided mesh alignment and densified texture extraction to transfer high-frequency details efficiently. A view-based inpainting network refines textures ensuring smooth, continuous appearance. PHAF generalizes to novel viewpoints and leverages a parametric hand model for accurate articulations, making it compatible with standard graphics engines. Experiments show it is comparable to existing methods in visual fidelity while drastically reducing texture generation time by 30 times, enabling practical AR/VR applications.

---


### 189. [FlowGuard: Flow Matching for Identity-Independent Detection of Data-Free Model Stealing Attacks on Energy System Intrusion Detection Systems](https://arxiv.org/abs/2606.03430)

**<font color=#1a73e8>作者：</font>** Maxime Schwarzer, Laurin Holz, Tobias Huerten 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Artificial Intelligence (AI)-based Intrusion Detection Systems (IDS) deployed in energy infrastructure are vulnerable to model theft attacks, which allow adversaries to create evasive traffic offline. Current defences against model extraction rely either on identity-bound query monitoring, which is ineffective against distributed attackers (Sybil), or on prediction poisoning through soft-label perturbation, which is inapplicable to hard-label IDS deployments. Therefore, we propose FlowGuard, an identity-independent defence based on flow matching that classifies incoming queries as out-of-distribution (OOD) prior to IDS processing. This approach exploits the fact that queries generated synthetically for data-free model stealing attacks occupy a lower-dimensional manifold than real network traffic. This results in measurably lower log-likelihoods when using a Continuous Normalizing Flow that has been trained on legitimate data. We evaluate our method against PRADA and FDINet using MAZE and DisGUIDE attacks in single-client and distributed (100-client Sybil) settings. While PRADA's detection rate dropped to 0% when the distribution changed, our defence maintained a stable detection rate across both settings without relying on identity information. We discuss the scope and limitations of the approach, and outline potential applications to data-dependent attacks.

---


### 190. [A Hybrid Approach For Malware Classification Using Secondary Features Fusion](https://arxiv.org/abs/2606.03432)

**<font color=#1a73e8>作者：</font>** Raja Khurram Shahzad, Muhammad Mustaqeem, Haroon Elahi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The number of malware (either variant or novel) is rapidly increasing, making malware detection and mitigation a complex problem. One approach to improving malware mitigation is automatic detection and malware family classification. However, traditional malware detection methods cannot classify detected malware into their respective families, hindering effective malware mitigation. Consequently, this paper proposes a method to automate malware detection and classification of the detected malware into respective malware families. The proposed method uses feature fusion after extracting relevant malware features such as API calls and fixed and variable length n-grams with a customized feature selection method. Moreover, for the predictive model, a voting based approach is proposed for algorithm fusion. For the experimental evaluation of the proposed method, both binary and multi-class classification approaches are applied to the data set provided by Microsoft. Finally, the experimental results are compared with the state of the art. The experimental results indicate the effectiveness and efficiency of the proposed approach with an AUC of 0.989, accuracy of 99.72%, and a log loss of 0.01.

---


### 191. [Signals and Spoils: Speculative Oracle Extractable Value in the Era of Cross-Chain Interoperability](https://arxiv.org/abs/2606.03434)

**<font color=#1a73e8>作者：</font>** Hasret Ozan Sevim, Christof Ferreira Torres  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A new form of Maximal Extractable Value (MEV), termed speculative MEV, has emerged across Layer-2 blockchains. Unlike Ethereum mainnet, many Layer-2 systems lack a public mempool, forcing extraction strategies to become probabilistic: searchers emit multiple identical transactions hoping to capture an opportunity first. This generates substantial transaction spam, increasing fees and wasting block space. We investigate speculative Oracle Extractable Value (OEV), a form of MEV associated with liquidating undercollateralized loans via speculative backrunning of oracle price updates. We propose a methodology for detecting speculative liquidations in the wild and apply it across Arbitrum, Base, and Optimism. On October 10, 2025, we identify 64 speculative liquidators on Aave (57% of all detected liquidators) and 831 successful speculative liquidations (39% of all successful liquidations across the three chains). We further examine whether latency differences in oracle price feed updates across blockchains can be exploited for cross-chain OEV. Specifically, we ask whether a searcher can observe oracle updates on one chain and frontrun liquidation opportunities on another. We systematically analyze Chainlink Decentralized Oracle Network (DON) configurations (deviation thresholds, heartbeat intervals, and submitted price observations) across Arbitrum, Base, Ethereum, and Optimism. Our dataset comprises 63 Chainlink feeds, 12,009 price updates, and over 100,000 oracle observations linked to 2,986 Aave liquidations. We show that independent DONs consume largely identical off-chain price data nearly simultaneously yet publish updates at different times, creating statistically predictable cross-chain exploitation windows. We demonstrate that Chainlink updates on Optimism can predict subsequent updates on Arbitrum and Base, enabling speculative cross-chain OEV extraction.

---


### 192. [FORGE: Multi-Agent Graduated Exploitation and Detection Engineering](https://arxiv.org/abs/2606.03453)

**<font color=#1a73e8>作者：</font>** Farooq Shaikh  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vulnerability disclosure volumes now far exceed organizational assessment capacity, yet three adjacent research communities (proof-of-concept generation, vulnerability prioritization, and detection rule engineering) operate largely in isolation. Existing automated exploit generation systems report binary pass/fail outcomes, discarding partial progress and producing no signal for the other two communities. This paper presents FORGE, a multi-agent system that bridges these three silos through graduated exploitation depth. Five specialized agents (Intel, Generator, Planner, Exploit, and Detector) execute in a fixed pipeline that (1) generates targeted vulnerable applications from CVE metadata, (2) conducts coached, multi-turn exploitation assessed by an LLM-primary oracle on a four-level taxonomy (L0: no evidence through L3: full compromise), and (3) produces Sigma and Snort detection rules grounded in OpenTelemetry exploitation traces. Graduated depth is the bridging mechanism: deeper exploitation yields richer behavioral traces for detection engineering, while depth data across scoring bands provides ground truth for prioritization validation. A tiered knowledge architecture accumulates intelligence across assessments, transferring build and exploitation experience to subsequent CVEs. Evaluation on 603 CVEs from the CVE-GENIE dataset achieves 67.8% end-to-end L1+ exploitation at USD 1.50 per CVE across eight languages and 187 CWE types. Exploitation rates remain near 68% regardless of EPSS or CVSS band, indicating that pattern-level reachability is orthogonal to metadata-based prioritization. Detection rules from L2+ exploitation achieve significantly higher span-normalized grounding than L1-derived rules (p=0.035), and 93.4% of generated Snort rules produce zero false positives against a synthetic benign corpus.

---


### 193. [KVarN: Variance-Normalized KV-Cache Quantization Mitigates Error Accumulation in Reasoning Tasks](https://arxiv.org/abs/2606.03458)

**<font color=#1a73e8>作者：</font>** Lorenz K. Muller, Philippe Bich, Chiara Boretti 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time scaling is a powerful approach to obtain better reasoning in large language models, but it becomes memory-bottlenecked during long-horizon decoding, as the KV-cache grows. KV-cache quantization can help improve this, but current methods are evaluated under prefill-like settings and errors behave differently under autoregressive decoding. We show that in the latter regime, quantization errors accumulate across timesteps, driven primarily by incorrect token scales. We introduce KVarN, a calibration-free KV-cache quantizer that applies a Hadamard rotation followed by a dual-scaling variance normalization across both axes of the K and V matrices. We find that this combination fixes outlying token-scale errors and substantially reduces error accumulation over existing baselines. KVarN establishes a new state-of-theart for KV-cache quantization on generative benchmarks, including MATH500, AIME24 and HumanEval, at 2-bit precision. A vLLM implementation of the KVarN method is available at this https URL

---


### 194. [From 3D Perception to Safety Reasoning: A Graph-Based Framework for Real-Time Underground Mine Monitoring](https://arxiv.org/abs/2606.03460)

**<font color=#1a73e8>作者：</font>** Pasindu Ranasinghe, Simit Raval, Dibyayan Patra 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Underground coal mining requires personnel and heavy equipment to operate within shared, confined, and poorly illuminated spaces where hazards such as equipment proximity violations, structural instabilities, and occluded blind spots are difficult to anticipate. Conventional monitoring systems, including fixed cameras and rule-based proximity alerts, can detect predefined events but lack the 3D scene understanding and contextual memory needed to identify complex or evolving hazards. This paper presents a continuous monitoring framework that converts colourised 3D point clouds into structured and traceable safety reasoning outputs. The framework combines 3D semantic perception, uncertainty-based anomaly detection, rule-based hazard checks, on-device LLM reasoning, and GraphRAG -based memory analysis to identify immediate hazards and interpret longer-term safety patterns. Scene and temporal graphs serve as the explicit knowledge structure, linking perception outputs across reasoning stages. To overcome the scarcity of labeled underground data, real roadway scans, controlled object placement, and high-fidelity longwall simulation were combined to generate diverse hazard scenarios, while self-supervised pretraining improved segmentation from limited annotations. The perception model achieved 92.7% accuracy at 30 FPS with low memory usage. Across 115 hazard scenarios, rule-based checks achieved 57% coverage, increasing to 76% with contextual LLM reasoning and 93% with memory-based reasoning using historical records. Qualitative results show uncertainty-derived anomaly signals support the interpretation of out-of-distribution hazards beyond predefined classes. Overall, graph-based knowledge representation combined with 3D perception and layered safety reasoning provides a practical foundation for intelligent decision support in underground mine monitoring.

---


### 195. [Topology-Aware Gaussian Graph Repair for Robust Graph Neural Networks](https://arxiv.org/abs/2606.03462)

**<font color=#1a73e8>作者：</font>** Anubha Goel, Juho Kanniainen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks have achieved strong performance on graph-structured data, but their effectiveness depends heavily on the quality of the observed graph. In real applications, graph topology is often imperfect: noisy edges may connect unrelated nodes, while missing edges may prevent useful information from being propagated. Existing robust graph learning methods mainly address this problem by removing suspicious edges or by learning a new graph structure during training. However, edge removal alone cannot recover missing connections, and graph structure learning may introduce additional optimization complexity. In this paper, we propose Topology-Aware Gaussian Repair (TAGR), a simple graph repair framework for robust message passing in graph neural networks. Instead of learning a dense adjacency matrix, TAGR constructs a sparse feature-neighborhood graph using an adaptive Gaussian kernel and combines it with a topology-aware residual correction of the observed graph. The Gaussian repair component introduces auxiliary edges between feature-similar nodes, while the residual correction preserves and reweights the original topology according to local feature and structural consistency. The repaired graph can be used directly with standard graph neural networks without changing their architectures. Extensive experiments on benchmark citation networks show that TAGR improves the robustness of GNNs under both noisy-edge and missing-edge settings. The analysis further show that Gaussian feature-neighborhood repair provides the main robustness gain, while topology-aware residual correction improves stability when the observed graph is incomplete. These results suggest that effective graph robustness can be achieved through lightweight sparse graph repair rather than dense graph structure learning.

---


### 196. [DMF: A Deterministic Memory Framework for Conversational AI Agents](https://arxiv.org/abs/2606.03463)

**<font color=#1a73e8>作者：</font>** Matteo Stabile, Enrico Zimuel  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conversational AI agents require memory systems that are both scalable and semantically coherent across long interaction horizons. Existing approaches rely predominantly on large language model (LLM)-based summarisation at write time, which introduces non-determinism, escalating token costs, and opacity in pruning decisions. We present the Deterministic Memory Framework (DMF), a CPU-first approach that replaces generative memory compression with a fully deterministic pipeline grounded in classical NLP analysis, vector geometry, and mathematical scoring. DMF assigns each conversational interaction a Survival Score $\Omega$ computed from deterministic content signals, conversational cues, and structured provenance, combined through a logistic projection. An interaction-count decay law, denoted as $\Omega_{\mathrm{eff}}(\Delta n)$, governs how relevance evolves as new turns arrive, where $\Delta n$ is the number of newer interactions rather than wall-clock time, preserving full determinism. We present the mathematical formulation of DMF, its structured recall pipeline, the pruning decision procedure, and the evaluation protocol. Experiments are conducted on a purpose-built benchmark using the LoCoMo and LongMemEval datasets. We compare DMF against Mem0, a popular memory layer for AI agents. DMF achieves comparable accuracy while using zero tokens to prepare the memory context and 5x to 242x fewer tokens over the entire conversation. These results show that it is possible to eliminate LLM calls from the memory-management loop, reducing token costs to nearly zero and enabling deterministic memory systems for conversational AI agents.

---


### 197. [StepFinder: A Temporal Semantic Framework for Failure Attribution in Multi-Agent Systems](https://arxiv.org/abs/2606.03467)

**<font color=#1a73e8>作者：</font>** Taiyu Zhu, Yifan Wu, Weilin Jin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based multi-agent systems exhibit remarkable collaborative capabilities in complex multi-step tasks. However, these systems are highly sensitive to single-step execution errors that can propagate through agent interactions and lead to cascading failures. To understand the causes of failure and improve system reliability, failure attribution has been introduced as a task that aims to automatically identify the root cause step responsible for a failure. Existing failure attribution methods mainly rely on LLMs to reason over original execution trajectories, which not only incur high inference costs and latency, but also suffer from interference caused by redundant and noisy execution logs, causing LLMs to struggle in accurately identifying the true root cause step. To address this, we propose StepFinder, a lightweight failure attribution framework. We use LLMs solely during the feature construction phase to encode execution logs into temporal semantic sequences. Subsequently, a parameter-efficient combination of temporal modeling and attention modules is applied to capture the sequential evolution and cross-step dependencies of the trajectories. Finally, the step-level error score is refined through multi-scale differences and position bias, enabling precise root cause identification. Experimental results on the Who&When benchmark demonstrate that StepFinder outperforms LLM-based methods in step-level failure attribution while achieving substantially higher inference efficiency, reducing inference time by 79% compared with the fastest LLM-based method, with no text generation overhead. Our code is available at this https URL.

---


### 198. [Mixed-Modality Dual Face-Hair Retrieval](https://arxiv.org/abs/2606.03470)

**<font color=#1a73e8>作者：</font>** Quoc-Anh Bui-Huynh, Mai-Tuyen Lam, Dai-Anh-Tuan Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Dual Face-Hair Retrieval (DFHR), a new mixed-modality dual-reference task in image retrieval where a query consists of a face image specifying identity and a hairstyle reference expressed as either an image or text. Unlike prior retrieval settings, DFHR requires cross-component reasoning between two semantically independent attributes -- identity and hairstyle -- originating from heterogeneous modalities. This formulation demands localized feature disentanglement, cross-modal semantic alignment, and mixed-modality composition within a unified embedding space. We construct DFHR-Bench, the first benchmark for mixed-modality face-hair retrieval, comprising over 180K annotated triplets across dual-image and image-text settings, built via a multi-stage annotation protocol ensuring semantic and identity integrity. We further propose MFHC (Multimodal Face-Hair Combiner), a unified framework that fuses disentangled identity and hairstyle embeddings through token injection and multi-view supervision. DFHR and DFHR-Bench together establish a new paradigm for identity-aware, attribute-controllable visual retrieval across modalities.

---


### 199. [A formal definition and meta-model for a machine theory of mind](https://arxiv.org/abs/2606.03471)

**<font color=#1a73e8>作者：</font>** Fabio Cuzzolin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper proposes, for the first time, a rigorous formal definition of the concept of Machine Theory of Mind, based on principles supported by evidence from cognitive psychology, neuroscience and artificial intelligence, and uses the above as a lens to examine state-of-the-art and current efforts in the field, driving a potential agenda for further research there able to "crack" the problem. It also advances a general holistic meta-model for Machine Theory of Mind, and examines the state of the art when it comes to empirically benchmarking such models.

---


### 200. [PersistGS: Differentiable Physics for Object Permanence in 4D Gaussian Splatting](https://arxiv.org/abs/2606.03479)

**<font color=#1a73e8>作者：</font>** Adrian Ramlal, John S. Zelek  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic 3D Gaussian Splatting (3DGS) methods reconstruct time-varying scenes from synchronized multi-camera video using photometric supervision. When a moving object becomes fully occluded from all training cameras, this supervision vanishes: the Gaussians representing it receive no gradient signal and degrade. Existing approaches to incomplete observations in neural reconstruction rely on learned generative priors that prioritize visual plausibility over physical correctness.
We propose $\textbf{PersistGS}$, a method that restores object permanence during occlusion by coupling differentiable rigid body simulation with 3D Gaussian Splatting. Our approach decomposes the scene into per-object Gaussians and collision meshes, estimates friction and velocity from the observed pre-occlusion trajectory via differentiable simulation, and uses the resulting SE(3) trajectory to position object Gaussians throughout the occlusion period. Because the predicted trajectory satisfies the governing equations of rigid body dynamics, it faithfully captures contact events (bounces, friction-based deceleration, direction changes) that kinematic extrapolation cannot model. We introduce a centroid silhouette loss that isolates positional gradients from appearance noise, yielding 40% lower trajectory error than photometric supervision. We evaluate using cameras withheld from training that observe the object during its occlusion. Experiments on synthetic scenes show that PersistGS outperforms constant velocity extrapolation by +2.46dB PSNR and comes within 0.19dB of a ground-truth trajectory upper bound.

---


> [!TIP]
> 当前位于：**151-200**（第 4/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-312](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
