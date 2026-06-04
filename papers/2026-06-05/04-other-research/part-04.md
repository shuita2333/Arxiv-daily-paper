# 📦 其他研究 | 2026年06月05日

> 本类共 **265** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-265](./part-06.md)

---

### 151. [QO-Bench: Diagnosing Query-Operator-Preserving Retrieval over Typed Event Tuples](https://arxiv.org/abs/2606.04646)

**<font color=#1a73e8>作者：</font>** Mengao Zhang, Xiang Yang, Chang Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Many real-world questions over business, legal, and scientific corpora are natural-language versions of database-style queries over records latent in text. Existing retrieval-augmented generation (RAG) systems are optimized primarily for semantic relevance, but retrieving plausible passages does not guarantee correct query execution. We introduce QO-Bench, a diagnostic benchmark for query-operator question answering over typed event tuples. The benchmark covers 22,984 news articles and 614 corporate events across 18 query templates, evaluated on 785 questions. Each gold answer is deterministically computed from typed event tuples and scored by recall, with answers matched to the gold tuples by exact match rather than an LLM judge. This design enables operator-level diagnosis such as joins and intersection. We evaluate RAG, ReAct RAG, GraphRAG, and information-extraction-to-SQL under matched conditions, with a long-context oracle ceiling to isolate retrieval failure. A two-axis framework -- index-time preservation versus query-time execution -- predicts where each paradigm fails, and the results bear it out: systems retrieve relevant text but discard the typed values operators need, and the deployable paradigm ranking inverts across operators, with similarity retrieval leading on filter/project and extraction-to-SQL on intersection and counting. Even given the gold evidence, a long-context oracle stays far from saturated, so operator execution -- not retrieval alone -- is a core bottleneck that a stronger answer model does not remove. QO-Bench reframes the goal from passage relevance to query-operator-preserving retrieval.

---


### 152. [ALINC: Active Learning for Inductive Node Classification via Graph Sampling](https://arxiv.org/abs/2606.04647)

**<font color=#1a73e8>作者：</font>** Pascal Plettenberg, Denis Huseljic, André Alcalde 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Active learning (AL) for node classification typically focuses on selecting the most informative nodes for annotation within one or a few large graphs (e.g., in social network analysis). However, in other domains, such as molecular chemistry or electronic design automation, datasets consist of thousands of independent graphs. In many of these inductive settings, annotating an individual node requires a full-graph analysis, which effectively yields the remaining node labels on-the-fly. Therefore, these scenarios require AL strategies that select entire graphs instead of single nodes, a problem which has not been tackled in the literature so far. Thus, we introduce ALINC, an AL framework for inductive node classification via graph sampling. It bridges the existing methodological gap by elevating node-level utility measures to graph-level selection criteria through various aggregation mechanisms. In an extensive benchmark including ten strategies, three aggregation methods, and four datasets, we identify CoreSet, TypiClust, and BADGE as the top-performing graph sampling strategies. Our detailed analysis further reveals that the choice of the aggregation method is pivotal, as it substantially affects model performance and annotation costs. Finally, we demonstrate the effectiveness of ALINC in two use case studies: site-of-metabolism prediction in molecules and design automation of printed circuit board schematics.

---


### 153. [BiNSGPS: Geometry Problem Solving via Bidirectional Neuro-Symbolic Interaction](https://arxiv.org/abs/2606.04648)

**<font color=#1a73e8>作者：</font>** Qi Wang, Peijie Wang, Fei Yin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Geometry problem solving poses distinct challenges in artificial intelligence. Existing approaches typically fall into two paradigms: symbolic methods, which exhibit limited adaptability, and neural methods, which are prone to hallucinations. Recent neuro-symbolic hybrids predominantly rely on a unidirectional pipeline where neural outputs are fed into solvers without feedback, making system brittle to early-stage errors. To break this unidirectional bottleneck, we propose BiNSGPS, a framework that establishes Bidirectional Neuro-Symbolic Interaction (BiNS) between a MLLM Adviser and a Symbolic Solver. MLLM Adviser actively incorporates feedback from the symbolic solver to dynamically rectify inconsistent formal representations or propose auxiliary hypotheses, resolving symbolic conflicts and facilitating complex deductions.

---


### 154. [Instance-Level Post Hoc Uncertainty Quantification in Object Detection](https://arxiv.org/abs/2606.04656)

**<font color=#1a73e8>作者：</font>** Chongzhe Zhang, Zifan Zeng, Qunli Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object detection is a safety-critical component of autonomous driving. It is essential to quantify the uncertainty in bounding-box predictions for safety assurance. Post hoc uncertainty quantification without retraining aligns with real-world deployment requirements; therefore, we employ the Laplace approximation. Because instance-level uncertainty is needed, linearized inference methods that require multiple backpropagations are not time-efficient, and sampling-based methods are not fully post hoc. We propose Monte-Carlo generalized linearized model (MC-GLM), which provides instance-level and approximately post hoc uncertainty quantification. The number of samples required in the Monte Carlo step is constant and independent of the number of output instances, so it can be parallelized. Experiments on the nuScenes dataset with the CenterPoint detector validate the effectiveness of our method, and the resulting uncertainties exhibit good quality.

---


### 155. [TeleHunt: A Framework and Tool for Efficient Cybercriminal Community Discovery on Telegram](https://arxiv.org/abs/2606.04657)

**<font color=#1a73e8>作者：</font>** Roy Ricaldi, Victor Asanache, Luca Allodi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper presents TeleHunt, a framework and tool for evaluating the effectiveness of different strategies to discover cybercriminal communities on Telegram. TeleHunt employs a set of reference-driven snowballing strategies, integrating message-level classification, contextual filtering, and market-segment labeling. Using open- and dark-web seeds, we systematically evaluate how seed source, pointer type, and exploration strategy influence discovery outcomes in three dimensions: efficiency, accessibility, and rediscovery. Our work provides (i) a modular cybercrime content discovery pipeline, (ii) the first systematic comparison of Telegram discovery strategies with an empirical characterization of market-segment accessibility, and (iii) a labeled dataset of over 172 million messages from 6,022 Telegram communities.

---


### 156. [LifeSide: Benchmarking Agents as Lifelong Digital Companions](https://arxiv.org/abs/2606.04660)

**<font color=#1a73e8>作者：</font>** Yuqian Wu, Zhijie Deng, Wei Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Lifelong digital companions must integrate cross-session cues, continually update their understanding of users, and adapt to shifting privacy boundaries. Existing evaluations fail to capture this, testing memory recall and short-term empathy in isolation. To bridge this gap, we introduce \benchmark, a benchmark centered on multi-session \textit{Memory-Emotion-Environment} loops. By modeling users as persistent worlds with layered profiles and event trajectories, \benchmark uses multi-agent simulation to project environmental dynamics into dialogue, preserving the critical gap between latent thoughts and observable expressions. Evaluating 2,000 personas and 111K tasks across memory tracking, user understanding, privacy control, and emotional companionship, our experiment results reveal a stark reality: even models that saturate current memory benchmarks fail to sustain accurate user understanding and true companionship over long horizons.

---


### 157. [CRAFT: Cost-aware Refinement And Front-aware Tuning of Prompts](https://arxiv.org/abs/2606.04661)

**<font color=#1a73e8>作者：</font>** Shanu Kumar, Shubhanshu Khandelwal, Akhila Yesantarao Venkata 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prompts tuned for accuracy often grow long, raising inference cost on every model call. The best accuracy-cost trade-off depends on the task and the budget, so prompt optimization is a search over the Pareto front of accuracy and prompt-token cost rather than for one prompt. The usual shortcut, collapsing the objectives into a weighted sum, fixes the trade-off weight before search and often recovers only a narrow region of the front, a failure we call scalarization collapse. We present CRAFT (Cost-aware Refinement And Front-aware Tuning), a Pareto-front prompt optimizer that treats target-LLM validation calls as the scarce resource and allocates them to candidates near the optimistic candidate front. Each round, complementary accuracy-oriented and cost-oriented generators propose edits, Pareto-gap acquisition spends the per-round validation budget, and NSGA-II retention keeps a spread-out population. Across six classification and reasoning benchmarks, CRAFT's retained fronts reach both high-accuracy and low-cost regions, while accuracy-only, cost-only, and weighted-sum baselines each concentrate in narrower regions. The accuracy-cost trade-off becomes a post-search choice, not a pre-search weight.

---


### 158. [Why Muon Outperforms Adam: A Curvature Perspective](https://arxiv.org/abs/2606.04662)

**<font color=#1a73e8>作者：</font>** Shuche Wang, Fengzhuo Zhang, Jiaxiang Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon improves training efficiency over Adam in large language-model training by about two times, but the local geometric source of this advantage remains unclear. Our work takes a first step toward demystifying Muon's superiority over Adam from a curvature perspective. First, we apply a second-order Taylor approximation to the training landscape and show that Muon achieves a larger one-step loss decrease than Adam at matched validation loss. The two optimizers have comparable first-order gains, but Muon consistently incurs a smaller second-order curvature penalty. Second, we decompose this curvature penalty into the squared update norm and Normalized Directional Sharpness (NDS). We find that Muon and Adam have comparable update norms, so Muon's smaller curvature penalty is driven by lower NDS, not update scale. Third, we study how training data and model structure shape Muon's NDS advantage. Using Zipf-Probabilistic Context-Free Grammar (PCFG) data with controlled imbalance, we show that data imbalance amplifies Muon's NDS advantage over Adam. A within-/cross-layer decomposition further shows that, in the middle and late stages of training, Muon's lower NDS is mainly sustained by smaller within-layer curvature. Beyond empirical evidence, we analyze stylized quadratic problems with heterogeneous curvature and gradient alignment toward high-curvature modes. We prove that Muon attains a smaller average NDS than GD by balancing update energy across curvature groups; when curvature heterogeneity is sufficiently strong, this also yields lower local quadratic loss after the same number of steps.

---


### 159. [Towards Accurate Model Selection in Deep Unsupervised Domain Adaptation](https://arxiv.org/abs/2606.04665)

**<font color=#1a73e8>作者：</font>** Kaichao You, Ximei Wang, Mingsheng Long 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep unsupervised domain adaptation (Deep UDA) methods successfully leverage rich labeled data in a source domain to boost the performance on related but unlabeled data in a target domain. However, algorithm comparison is cumbersome in Deep UDA due to the absence of accurate and standardized model selection method, posing an obstacle to further advances in the field. Existing model selection methods for Deep UDA are either highly biased, restricted, unstable, or even controversial (requiring labeled target data). To this end, we propose \textit{Deep Embedded Validation} (\textbf{DEV}), which embeds adapted feature representation into the validation procedure to obtain unbiased estimation of the target risk with bounded variance. The variance is further reduced by the technique of control variate. The efficacy of the method has been justified both theoretically and empirically.

---


### 160. [SoK: Post-Quantum Cryptography (PQC) Implementation in Software Systems](https://arxiv.org/abs/2606.04669)

**<font color=#1a73e8>作者：</font>** R.D.N. Shakya, C.P. Wijesiriwardana, S.M. Vidanagamachchi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The transition to Post-Quantum Cryptography (PQC) is essential to protect software systems from emerging quantum-enabled threats. Although standardised PQC algorithms are now available, developers and organisations continue to face significant challenges in integrating them into real-world software systems. While existing studies primarily focus on cryptographic performance and algorithmic security, it provides limited understanding of the broader socio-technological factors that influence successful PQC implementation. This SoK investigates PQC implementation approaches and challenges through the Human, Organisation, and Technology (HOT) dimensions. By systematically synthesising existing approaches across these dimensions, we reveal a notable imbalance in the current body of knowledge, where technological solutions dominate, while human and organisational considerations remain underexplored. Our analysis further shows that PQC implementation challenges are not isolated to individual dimensions; rather, they emerge as interconnected socio-technological constraints that span HOT contexts, collectively shaping implementation outcomes. These findings indicate that PQC implementation extends beyond cryptographic replacement and represents a broader socio-technological transformation requiring coordinated approaches across all HOT dimensions. To address this gap, we propose the PQC-HOT model, a conceptual framework that explains how interactions among HOT dimensions collectively influence PQC implementation in software. The model synthesises the implementation interventions and challenges identified in the SoK into an integrated structure that supports systematic decision-making, planning, and organisational transition strategies. Based on these insights, we outline future research directions and design implications for scalable and sustainable PQC implementation in software systems.

---


### 161. [Learning Long Range Spatio-Temporal Representations over Continuous Time Dynamic Graphs with State Space Models](https://arxiv.org/abs/2606.04672)

**<font color=#1a73e8>作者：</font>** Ayushman Raghuvanshi, Thummaluru Siddartha Readdy, Sundeep Prabhakar Chepuri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous-time dynamic graphs (CTDGs) provide a richer framework to capture fine-grained temporal patterns in evolving relational data. Long-range information propagation is a key challenge while learning representations, wherein it is important to retain and update information over long temporal horizons. Existing approaches restrict models to capture one-hop or local temporal neighborhoods and fail to capture multi-hop or global structural patterns. To mitigate this, we derive a parameter-efficient state-space modeling framework for continuous-time dynamic graphs (CTDG-SSM) from first principles. We first introduce continuous-time Topology-Aware higher order polynomial projection operator (CTT-HiPPO), a novel memory-based reformulation of HiPPO to jointly encode temporal dynamics and graph structure. The solution from CTT-HiPPO is obtained by projecting the classical HiPPO solution through a polynomial of the Laplacian matrix, yielding topology-aware memory updates that admit an equivalent state-space formulation for CTDGs (CTDG-SSM). Then a computationally efficient discrete formulation is obtained using the zero-order hold approach for model implementation.
Across benchmarks on dynamic link prediction, dynamic node classification, and sequence classification, CTDG-SSM achieves state-of-the-art performance. Notably, it achieves large performance gains on datasets that require long range temporal (LRT) and spatial reasoning.

---


### 162. [Test-Time Compute Scaling for ASR with Depth-Conditioned Looped Transformers](https://arxiv.org/abs/2606.04678)

**<font color=#1a73e8>作者：</font>** Yacouba Kaloga, Shashi Kumar, Shakeel A. Sheikh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> End-to-end ASR systems typically use fixed-depth acoustic encoders at inference, making it difficult to trade additional test-time computation for improved recognition without training a larger model. A natural approach is to reuse a shared Transformer block recurrently, but we find that naive looping does not fully exploit additional recurrent compute. We introduce LARM, a depth-conditioned looped Transformer that turns recurrent encoder depth into a controllable test-time compute axis. LARM combines sparse CTC checkpoints, supervision-clock embeddings, FiLM depth conditioning, and delayed soft-posterior feedback. These components structure the loop into recognition checkpoints separated by latent refinement phases and allow shared weights to specialize across recurrent steps. On LibriSpeech, LARM improves WER as the number of inference loops increases and achieves performance competitive with deeper unshared-parameter baselines. Our results show that test-time compute scaling can extend beyond autoregressive language-model reasoning to continuous non-autoregressive speech recognition.

---


### 163. [Real-Time Automatic License Plate Recognition Using YOLOv8, SORT Tracking, and Temporal Data Interpolation](https://arxiv.org/abs/2606.04684)

**<font color=#1a73e8>作者：</font>** Mirza Muhammad Mobeen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The real-time hardships of video processing seriously limit the usage of Automatic License Plate Recognition (ALPR) with application in dynamic traffic monitoring settings. High-fidelity recognition of unconstrained variables, e.g. drastic variations in illumination, acute camera scans, high vehicle speeds, and harsh physical concealment, is a problem that often leads to disjointed tracking paths and poor Optical Character Recognition (OCR) rates. In order to mitigate these weaknesses, the study proposes a 5 stage, end-to-end algorithmic pipeline, encompassing a smooth transition between deep learning based object detection, multi-object tracking which is kinematic in nature, and geometry temporal data interpolation. The suggested architecture takes advantage of a very powerful YOLOv8 nano model to localize the vehicle at the first stage and then Simple Online and Realtime Tracking (SORT) algorithm is used to build spatial-temporal links between frames. Another, more specific typology of YOLOv8 object detectors the license plate area, channeling the sliced array to an EasyOCR chain under the limitations of positional syntax verification. More importantly, an offline interpolation mechanism of temporal bounding box is initiated to recast fragmented paths.

---


### 164. [MeshWeaver: Sparse-Voxel-Guided Surface Weaving for Autoregressive Mesh Generation](https://arxiv.org/abs/2606.04688)

**<font color=#1a73e8>作者：</font>** Jiale Xu, Wang Zhao, Ying Shan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive mesh generation has gained attention by tokenizing meshes into sequences and training models in a language-modeling fashion. However, existing approaches suffer from two fundamental limitations: (i) low tokenization efficiency, which yields long token sequences and prevents scaling to high-poly meshes, and (ii) absence of geometry-aware guidance, as generation is conditioned only on global shape embeddings rather than local surface cues. We introduce MeshWeaver, an autoregressive framework that treats mesh generation as a surface weaving process by directly predicting the next vertex instead of independent coordinates. At its core is a multi-level sparse-voxel encoder that injects geometric context into the generative process in three complementary ways: providing voxel features as vertex representations, guiding token prediction via cross-attention to voxel features, and serving as a structural scaffold that constrains generation around the input surface. Our hierarchical design enables coarse-to-fine vertex prediction in a single decoding step, while tightly coupling the generative model with 3D geometry. Extensive experiments demonstrate that MeshWeaver achieves a state-of-the-art compression ratio of 18%, can generate meshes with up to 16K faces, and significantly improves geometric fidelity over prior approaches.

---


### 165. [SMADE-IE: Sparse Multi-Agent Framework with Evidence-Driven Debate for Zero-Shot Information Extraction](https://arxiv.org/abs/2606.04691)

**<font color=#1a73e8>作者：</font>** Kenfeng Huang, Yi Cai, Xin Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Zero-shot information extraction (IE) with large language models (LLMs) has attracted increasing attention due to its flexibility in adapting to new schemas and domains without task-specific training. Existing approaches mainly rely on monolithic prompting, each-type prompting, or multi-agent debate. However, monolithic prompting often suffers from boundary and type errors, while each-type prompting and multi-agent debate introduce cross-type conflicts, redundant agent interactions, and substantial token overhead. To address these challenges, we propose SMADE-IE, a sparse and evidence-driven multi-agent framework for zero-shot IE. SMADE-IE first employs an Adaptive Mode Selector to dynamically route inputs into either a lightweight Global Extraction Mode or a Type-Centric Extraction Mode, reducing unnecessary type selection and reasoning noise. For conflicting predictions, we further introduce an Evidence-Driven Debate mechanism that structures arguments into Toulmin-style components and performs confidence aggregation through external evidence scoring and Bayesian updates. Experimental results on 9 benchmark datasets across NER, RE, and JERE tasks show that SMADE-IE consistently outperforms existing zero-shot IE baselines while also improving token efficiency through sparse agent selection and early-stopping debate.

---


### 166. [DuDi: Dual-Signal Distillation with Cross-Lingual Verbalizer](https://arxiv.org/abs/2606.04694)

**<font color=#1a73e8>作者：</font>** Patomporn Payoungkhamdee, Tinnakit Udsa, Jian Gang Ngui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Small language models (SLMs) are efficient and scalable, but their multilingual capabilities degrade severely at sub-billion scales, especially for Southeast Asian (SEA) languages. We introduce DuDi, a dual-signal multilingual distillation framework that combines an online sequence-level signal with off-policy and on-policy token-level signals. DuDi further uses a cross-lingual verbalizer to refine teacher feedback and improve teacher-student transferability in multilingual settings. Experiments on SEA-HELM across multiple model families, scales, and teacher-student settings show that DuDi consistently outperforms competitive distillation baselines. Ablations and analyses confirm that sequence-level optimization, token-level supervision, and cross-lingual verbalization provide complementary and transferable learning signals for multilingual SLMs.

---


### 167. [Cone-Compatible Monge Geometry for High-Dimensional Ordered Optimal Transport](https://arxiv.org/abs/2606.04695)

**<font color=#1a73e8>作者：</font>** Lei Luo, Hongliang Zhang, Jian Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-dimensional optimal transport is seldom available in closed form. The one-dimensional case is exceptional because the order of the real line is compatible with convex transport costs, making monotone rearrangement optimal. This paper studies when an analogous Monge structure can be recovered in higher dimensions from a partial order. We introduce a cone-compatible Monge geometry: a closed convex cone (K) induces the order (x\preceq_K y) whenever (y-x\in K), and is compatible with a cost if ordered pairs satisfy a Monge exchange inequality. For squared Mahalanobis costs (c_M(x,y)=(x-y)^\top M(x-y)), we prove a sharp characterization: compatibility holds exactly when (K) is acute under the (M)-inner product, namely (u^\top Mv\ge0) for all (u,v\in K), equivalently (K\subseteq K_M^*). Under this condition, measures supported on cone chains admit a quantile-type closed-form optimal coupling, yielding exact transport under the original ground cost rather than after projection or metric replacement. We distinguish the resulting cone-chain Wasserstein metric on canonically ordered chain distributions from an extended directed cone transport cost on general measures, and develop feasibility, duality, stability, approximation, Gaussian recovery, statistical, and computational results. The theory is complementary to sliced and tree Wasserstein distances: it is not a universal fast surrogate, but a way to obtain interpretable, direction-valid, original-space monotone transport for ordered high-dimensional data.

---


### 168. [Graph-Guided Universum Learning in Generalized Eigenvalue Proximal SVMs for Alzheimer's Disease Classification](https://arxiv.org/abs/2606.04699)

**<font color=#1a73e8>作者：</font>** Yogesh Kumar, Vrushank Ahire, Mudasir Ganaie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Early and accurate detection of Alzheimer's disease (AD) is important for timely intervention and disease management. Generalized Eigenvalue Proximal Support Vector Machine (GEPSVM) and its Universum-based variants have shown promising results for AD classification. However, existing methods treat Universum samples as independent points and do not consider the geometric relationships among them. This paper proposes two graph-guided Universum learning models, namely UG-GEPSVM and IUG-GEPSVM, for AD versus cognitively normal (CN) classification using structural MRI data. In the proposed framework, mild cognitive impairment (MCI) subjects are used as Universum data to provide intermediate information between AD and CN classes. A graph is constructed over the Universum samples using Gaussian similarity, Minimum Spanning Tree connectivity, and multi-hop propagation. From this graph, a Laplacian matrix is derived that captures the geometric structure of the MCI samples. This Laplacian-based regularization is incorporated into the learning process in place of the conventional independent Universum penalty term. UG-GEPSVM integrates this regularization into the generalized eigenvalue formulation, while IUG-GEPSVM extends the numerically stable improved GEPSVM framework using a standard eigenvalue formulation. Experiments on ADNI MRI dataset variants using ICA- and PCA-based features at five different noise levels show that both proposed models consistently outperform existing GEPSVM and Universum-based methods. UG-GEPSVM achieves the highest average AUC of 88.07% and maintains stable performance under increasing noise levels. Statistical tests further confirm the significance of the observed improvements.

---


### 169. [A New Angle on Bones: Robust Pose Estimation in X-Ray and Ultrasound](https://arxiv.org/abs/2606.04700)

**<font color=#1a73e8>作者：</font>** Ron Keuth, Christoph Großbröhmer, Franziska Halm 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Measuring the angle between bone structures is a routine task in medical image analysis and provides a key quantitative parameter for diagnosis and treatment planning. Automated methods can reduce time and cost while improving reproducibility. In this work, we address automatic bone pose estimation using a learning-based point candidate proposal followed by a line model to extract axis parameters. Since conventional line models such as least squares are sensitive to outliers, we incorporate false-positive reduction strategies and robust fitting techniques, such as RANSAC and Hough transforms, to improve robustness. We evaluate our method on three clinically relevant paediatric angle estimation tasks: fracture fragment assessment in radiographs and ultrasound and developmental dysplasia of the hip evaluation in ultrasound using the Graf method. Our approach achieves mean errors of $4.1^\circ$, $5.4^\circ$, and $5.51^\circ$, respectively, not only remaining within the expected clinical observer variability, but also significantly outperforming landmark-based methods. Our code and annotations for fracture angle assessment in radiographs are publicly available on GitHub.

---


### 170. [Benchmarking Living-Screen-Native GUI Agents on Short-Video Platforms](https://arxiv.org/abs/2606.04701)

**<font color=#1a73e8>作者：</font>** Jiashu Yao, Heyan Huang, Daiqing Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> GUI agents today assume a static screen, where the world is frozen between two actions. However, real interfaces such as short-video applications violate this assumption, as their content keeps playing, and a competent user must decide what to watch and for how long. We formalize this task as Living-Screen-Native GUI agents and introduce LivingScreen, the first benchmark instantiating it on short-video platforms, with a faithful browser-based environment, a three-tier task suite, and metrics that jointly score accuracy and information efficiency. Evaluating extensive frontier models, we find that none reaches the human cost-accuracy performance, and that their dominant failure mode is over- and under-observation, pointing to observation control as a missing capability axis for future GUI agents. All data and code will be available at this https URL.

---


### 171. [Enhancing MedSAM with a Lightweight Box Predictor for Medical Image Segmentation](https://arxiv.org/abs/2606.04705)

**<font color=#1a73e8>作者：</font>** Amirhossein Movahedisefat, Amirreza Fateh, Mohammad Reza Mohammadi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic segmentation in medical imaging is a critical yet challenging task due to data scarcity and high variability across modalities. While foundation models like the Segment Anything Model (SAM) show promise, they often struggle with medical images without specific adaptation. Moreover, point prompts, despite being the most natural form of user interaction, provide insufficient spatial context for reliable segmentation, particularly when target structures are irregular or poorly contrasted. In this paper, we propose an enhanced segmentation framework that integrates a lightweight Box Predictor module into the MedSAM architecture. The Box Predictor estimates an approximate bounding box from a single user click using localized image embedding features, providing spatial guidance that reduces the ambiguity of point prompts, while introducing only 1.6M additional parameters and negligible inference overhead. We introduce a two-stage training pipeline where the Box Predictor is trained independently before being integrated into MedSAM. To validate the generalization capability of our method, we conduct extensive evaluations on four diverse datasets (FLARE22, BRISC, BUSI, LungSegDB) spanning distinct imaging modalities, including CT, MRI, and Ultrasound. Our method improves segmentation accuracy and robustness across varied anatomical structures and imaging domains, achieving Dice scores of 0.89 (BUSI), 0.93 (FLARE22), 0.88 (BRISC), and 0.98 (LungSegDB). Code is available at this https URL

---


### 172. [ReConFuse: Reconstruction-Error Guided Semantic Fusion for AI-Generated Video Detection](https://arxiv.org/abs/2606.04706)

**<font color=#1a73e8>作者：</font>** Xiaojing Chen, Xinyu Lu, Changtao Miao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-generated videos are becoming increasingly realistic, raising serious concerns about misinformation, content authenticity, and media trust. Reliable AI-generated video detection is therefore essential for multimedia forensics, yet remains challenging due to the need to capture spatial artifacts, temporal dynamics, and generalize to evolving generative models. In this paper, we explore reconstruction error as a discriminative forensic cue for AI-generated video detection. By reconstructing input videos with a pretrained WF-VAE, we observe that real and generated videos exhibit distinguishable frame-wise reconstruction error patterns, suggesting that reconstruction errors can reveal their distributional discrepancies. However, extending reconstruction-based image detection to videos is non-trivial, since video reconstruction errors are temporally organized across frames and require semantic context for effective interpretation. To address these challenges, we propose ReConFuse, a reconstruction-guided semantic fusion framework for video-level AI-generated video detection. ReConFuse extracts reconstruction error cues from WF-VAE reconstructed videos, aligns them with multi-frame semantic features, and uses a Mamba-based module to model temporal evolution for video-level classification. Experiments across multiple generators and evaluation settings demonstrate the effectiveness and strong generalization ability of ReConFuse.

---


### 173. [Data Efficient Complex Feature Fusion Network For Hyperspectral Image Classification](https://arxiv.org/abs/2606.04710)

**<font color=#1a73e8>作者：</font>** Maitreya Shelare, Atharva Satam, Poonam Sonar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This work presents a data-efficient variant of the Attention-Based Dual-Branch Complex Feature Fusion Network (CFFN) for hyperspectral image classification. The proposed model, termed DE-CFFN, retains the original two-stream structure: the Real-Valued Neural Network (RVNN) processes standard hyperspectral patches, while the Complex-Valued Neural Network (CVNN) handles their Fourier-transformed counterparts. The main contribution of this work lies in the feature extraction process and architectural enhancement. Factor Analysis is used for dimensionality reduction, offering improved latent feature representation over Principal Component Analysis. Additionally, both the RVNN and CVNN streams are structurally modified by successively halving the number of filters in the 3D convolutional layers to reduce complexity. The outputs of both branches are concatenated and passed through a Squeeze and Excitation (SE) block to enhance joint feature representation. Evaluated on the Pavia University and Salinas datasets, DE-CFFN achieves classification performance comparable to CFFN, while significantly reducing model size, memory consumption, and inference latency, making it suitable for real-time hyperspectral imaging applications.

---


### 174. [Selection-Aware Diagnostics for Chain-of-Thought Answer Hijacking](https://arxiv.org/abs/2606.04717)

**<font color=#1a73e8>作者：</font>** Jianwei Tai  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We study a controlled numeric proxy for chain-of-thought (CoT) answer hijacking, motivated by attacks in which benign-looking reasoning steers a harmful final answer. CoT wrappers on GSM8K and MATH-500 flip final answers away from gold labels. Rather than treating activation patching as clean-trace restoration, we ask where hijacked trajectories are fragile and whether recovery depends on a same-problem clean source. Across Qwen2.5-7B and Llama3-8B on GSM8K few-shot, puzzle, and sycophant hijacks, three few-shot/puzzle cells pass confirmatory $K{=}1$ localization after Bonferroni correction. A selection-aware 50/50 band validation preserves held-out in-band minus out-of-band gaps of +32.6, +45.1, and +17.7 points for Qwen-puzzle, Llama3-fewshot, and Llama3-puzzle, while exact $\Lstar$ agreement is much less stable. Qwen-fewshot remains exploratory, and sycophant cells are temporal-diffuse under short patches. A BF16 Qwen-puzzle full-band sweep preserves the band signal ($n{=}30$, spread 0.33 at $K{=}1$, peak layer 20), supporting the conclusion that the band is not only an INT4 artifact. Fixed-hook GSM8K reruns preserve recovery in both primary puzzle cells: Qwen-puzzle recovers 47.0\% at $n{=}100$ (47/100; Wilson 95\% CI [37.5\%, 56.7\%]), while Llama3-puzzle recovers 39.0\% at $n{=}100$ (39/100; [30.0\%, 48.8\%]). Frozen transfer to MATH-500 recovers 26.0\% of qualified cases in the largest fixed-transfer run (13/50; Wilson 95\% CI [15.9\%, 39.6\%]). Source controls change the mechanism interpretation. Paired bootstraps give finite-sample non-separation between clean and random sources in Qwen-fewshot (+3.0 points, 95\% CI [-18.2,+27.3]) and Llama3-puzzle at expanded $n{=}60$ (clean--random -8.3 [-21.7,+5.0]), while Llama3-fewshot is content-mediated (+40.0 [+16.7,+60.0]).

---


### 175. [StrokeTimer: Robust Representation Learning for Ischemic Stroke Onset-Time Estimation from Non-contrast CT](https://arxiv.org/abs/2606.04722)

**<font color=#1a73e8>作者：</font>** Weiru Wang, Susanne G.H. Olthuis, Elizaveta Lavrova 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ischemic stroke is a major global disease. Treatment decisions are highly time-sensitive, as eligibility for reperfusion therapies relies on the interval between stroke onset and intervention. However, the true onset time is often uncertain in clinical practice, necessitating imaging-based assessment of tissue age as a surrogate marker. Early ischemic changes on routinely acquired non-contrast CT (NCCT) are often subtle, and real-world clinical datasets exhibit pronounced onset-time class imbalance and center-scanner-related heterogeneity. In this work, we propose StrokeTimer, a fully automated framework for onset-time estimation in acute ischemic stroke. StrokeTimer integrates self-supervised disentanglement learning with energy-guided contrastive learning to capture subtle ischemic patterns while addressing long-tailed data distributions under acquisition variability. Onset time is categorized into three clinically relevant windows: <4.5 h, 4.5-6 h, and >6 h. Experimental results on a large multi-center NCCT dataset from two national cohorts, MR CLEAN Registry and MR CLEAN LATE, show that StrokeTimer achieves a macro AUC of 0.69 and a macro F1-score of 0.57, improving the strongest baseline by nearly 50% (p < 0.005). In this realistic, challenging setting, representative baseline approaches exhibit near-chance macro performance. Model explanations further highlight subtle gray-white matter blurring and hypodense regions consistent with established radiological biomarkers. These findings demonstrate the potential of StrokeTimer to support treatment decision-making in acute ischemic stroke. Code is available at this https URL.

---


### 176. [Multilingual Long-Form Speech Instruction Following: KIT's Submission to IWSLT 2026](https://arxiv.org/abs/2606.04730)

**<font color=#1a73e8>作者：</font>** Enes Yavuz Ugan, Maike Züfle, Yuka Ko 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With the advent of Large Language Models, single-task and token-based multi-task models have evolved into instruction-based systems that infer task and target language implicitly from natural language prompts. This trend is reflected in IWSLT's Instruction Following Track, which this year introduced new tasks including an unknown surprise task, posing a genuine challenge against overfitting to known tasks. We present KIT's submission to the Long and Short Instruction Following tracks in the unconstrained setting. Our approach combines a general data augmentation pipeline that converts short-form corpora into long-form training data through segment concatenation, LLM-based label generation, and cross-lingual translation, yielding over 1M instances across six tasks and four languages. We further show that likelihood-based re-ranking, while highly effective for ASR, systematically degrades semantic tasks by spuriously selecting candidates generated from segmented audio processing rather than holistic long-form inference, a failure mode resolved by combining likelihood with Minimum Bayes Risk decoding.

---


### 177. [Contrastive Learning and Correlation Clustering for Sequences of Network Telescope Data](https://arxiv.org/abs/2606.04733)

**<font color=#1a73e8>作者：</font>** Jannik Presberger, Alexander Männel, Maynard Koch 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding activities of Internet scanners is challenging; it often requires identifying relationships between sources, a task for which semantic annotations are scarce. This work investigates whether semantically meaningful pairwise relationships between sequences of network flow records can be estimated by contrastive learning, without pretraining and without annotations. To this end, we propose a transformer model that embeds minimally preprocessed sequences of network flow records and train it using contrastive learning. With the similarities obtained from this model, we state a correlation clustering problem and solve it locally. Experimentally, we show: Learned similarities are higher on average for sequences originating from the same source than for sequences originating from different sources, and this property generalizes to unseen sequences of unseen sources. Moreover, correlation clustering yields clusters consistent with scanner labels. The complete source code of the algorithms and for reproducing the experiments is publicly available.

---


### 178. [Trace-Mediated Peak Bias: Bridging Temporal Credit Assignment and Cognitive Heuristics in Deep Reinforcement Learning](https://arxiv.org/abs/2606.04735)

**<font color=#1a73e8>作者：</font>** Viktor Veselý, Aleksandar Todorov, Erwan Escudie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temporal credit assignment is central to both biological and artificial intelligence, yet its interaction with non-linear function approximation is poorly understood. We identify a systematic failure mode in deep reinforcement learning (RL) termed Trace-Mediated Peak Bias (TMPB). At intermediate eligibility trace depths, agents irrationally prefer trajectories with high-magnitude reward ``peaks'' over alternatives with higher cumulative returns. This provides a mechanistic account of the Peak-End Rule: a human memory bias where experiences are judged by their most intense moments rather than integrated utility. We show that TMPB emerges because traces amplify distal Temporal Difference errors into ``gradient shocks'' that fixed-step-size Stochastic Gradient Descent cannot normalize, leading to global overestimation. Conversely, adaptive optimizers mitigate this pathology via second-moment normalization. Our results suggest that human-like saliency distortions may emerge naturally from the mathematical constraints of credit assignment in distributed systems, and that adaptive optimization is a theoretical necessity for rational value estimation.

---


### 179. [Curvature-aware dynamic precision approach for physics-informed neural networks](https://arxiv.org/abs/2606.04736)

**<font color=#1a73e8>作者：</font>** Yingjie Shao, Ioannis N. Athanasiadis, George van Voorn 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) have become a promising framework for simulating partial differential equations (PDEs) by embedding physical laws directly into neural network training. However, recent studies show that PINN optimisation is sensitive to numerical precision. Existing implementations commonly use either single precision (FP32), which is computationally efficient but prone to failure modes, or double precision (FP64), which is robust but substantially expensive. This creates a trade-off between computational efficiency and numerical accuracy. To reduce the computational cost of double-precision training while retaining prediction accuracy, we propose a curvature-aware precision controller that adapts numerical precision during training rather than treating it as a fixed implementation choice. The proposed method reuses curvature information derived from the limited-memory BFGS (L-BFGS) optimiser to construct a precision controller, retaining FP32 when lower precision is sufficient and promoting computation to FP64 when the training dynamics indicate numerical sensitivity or precision-limited stagnation. We evaluate the proposed approach on four canonical PINN failure-mode benchmarks and an irradiance-driven ordinary differential equation example. We further test the proposed approach across different neural network architectures. The method consistently matches or even slightly exceeds full FP64 solution accuracy while reducing training time relative to full double-precision training on all benchmark equations. The obtained results indicate that precision sensitivity in PINN optimisation is phase-dependent, and that selectively applying higher precision only during numerically critical stages can lower computational cost without sacrificing predictive accuracy.

---


### 180. [TIDE: Proactive Multi-Problem Discovery via Template-Guided Iteration](https://arxiv.org/abs/2606.04743)

**<font color=#1a73e8>作者：</font>** Soyeong Jeong, Jinheon Baek, Minki Kang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agents are widely deployed as assistants over documents, tools, and code. However, they typically act only on explicit user requests, which surface only the problems the user has noticed, while many other important problems coexist, hidden in plain sight, within the broader user context, with their total number unknown in advance. We frame this as the task of discovering multiple hidden problems from context, in which coexisting problems should be uncovered, grounded in supporting evidence, and paired with concrete actions. To this end, we introduce TIDE, a template-guided iterative framework with two complementary mechanisms. Specifically, motivated by the observation that single-pass prediction anchors on the most salient cases and yields generic claims, we propose iterative discovery, which surfaces a small batch of candidates per round while conditioning on what has already been found, so subsequent rounds extend coverage; and thought templates, reusable schemas distilled from previously solved cases that specify what contextual signals to attend to and how to connect them, anchoring each prediction in a recognizable problem class. We validate TIDE on two realistic settings, personal workspaces and software repositories, across four model backbones, showing substantial gains over single-shot and parallel multi-agent baselines on task coverage, identification, and resolution.

---


### 181. [Fog of Love: Engineering Virtuous Agent Behavior with Affinity-based Reinforcement Learning in a Game Environment](https://arxiv.org/abs/2606.04750)

**<font color=#1a73e8>作者：</font>** Ajay Vishwanath, Christian Omlin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Instilling virtuous behavior in artificial intelligence has seen increasing interest. One of the techniques proposed is known as affinity-based reinforcement learning, which uses policy regularization on the objective function to incentivize virtuous actions without being fully dependent on the reward function design. Thus far, this technique has been demonstrated to be effective in grid worlds and toy-problem environments with minimal state and action spaces. To expand this research to more sophisticated environments, we introduce a two-player multi-agent environment based on the role-playing board game known as Fog of Love. In this environment, two agents compete to fulfill their individual virtues, while also cooperating to satisfy their relationship. Given the multi-agent nature, this is a complex problem where multi-agent deep deterministic policy gradient agents neither compete nor cooperate successfully. We present evidence that localized affinities enhance agent performance in achieving both competitive and cooperative objectives, resulting from superior overall scores in both domains. This not only results in virtuous choices but also clarifies an agent's teleology and makes its behavior human-level interpretable.

---


### 182. [An Empirical Audit of Input Encoders for Multi-Channel Signal Transformers](https://arxiv.org/abs/2606.04752)

**<font color=#1a73e8>作者：</font>** Ossi Lehtinen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers consuming multi-channel scalar signals must embed $C$ simultaneous values into one $d_{\text{model}}$-dimensional vector per time step. We empirically audit eight input encoders -- spanning a shared-scalar baseline, per-channel linear projections, an orthogonality regulariser, a nonlinear MLP stem, block-partitioned concatenation, channel-independent and channel-as-token architectures, and a projected positional encoding -- on a synthetic benchmark designed to make channel identity informative and on ETTh1 as a real-data check, measured in next-step negative log-likelihood (NLL). The headline is one of practical near-equivalence within a wide "top tier": the standard per-channel linear projection (this http URL(C, $d_{\text{model}}$)) matches every alternative in that tier up to small, statistically real but practically modest, differences. Two encoders lose decisively: the shared-scalar baseline, which collapses for information-theoretic reasons we make explicit, and the channel-independent PatchTST-spirit baseline, which underperforms on both benchmarks and overfits universally on the synthetic one. Paired tests resolve two small gaps: projecting the sinusoidal positional encoding through a learned linear layer edges the rest at small $C$, with a direct geometric probe showing the mechanism is positional-channel orthogonalisation; a nonlinear MLP stem edges them at the largest $C$ we test, with the gap shrinking under more training data. The practical recommendation is to use this http URL(C, $d_{\text{model}}$) by default and reach for something more elaborate only when the task at hand gives a real reason to do so. Code and data to reproduce every experiment in this paper are available at this https URL

---


### 183. [Beyond Structural Symmetries: Linear Mode Connectivity via Neuron Identifiability](https://arxiv.org/abs/2606.04754)

**<font color=#1a73e8>作者：</font>** Vincent Bürgin, Daniel Herbst, Ya-Wei Eileen Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many striking phenomena in deep learning, such as linear mode connectivity and the structured behavior of training dynamics, are closely tied to parameter symmetries: transformations that leave the realized function unchanged. Despite growing attention to parameter symmetries, the exact interplay between parameters, data, and representations remains underexplored. To investigate this, we develop a theoretical framework of effective function classes, i.e., the set of functions a neuron can realize on its input support, and the norm cost of realizing them. We then formalize effective symmetry breaking via neuron identifiability across independent training runs. Our analysis shows that neural networks can admit large families of approximately equivalent solutions even in structurally asymmetric models. We further show that neuron identifiability enables representation merging without prior alignment, and characterize when such merging admits a linear low-loss path. These findings highlight the role of effective function classes in affecting the loss landscape.

---


### 184. [Measuring Model Robustness via Fisher Information: Spectral Bounds, Theoretical Guarantees, and Practical Algorithms](https://arxiv.org/abs/2606.04767)

**<font color=#1a73e8>作者：</font>** Chong Zhang, Xiang Li, Jia Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The robustness of deep neural networks is crucial for safety-critical deployments, yet existing evaluation methods are often attack-dependent and lack interpretability. We propose a principled, attack-agnostic robustness metric based on the spectral norm of the Fisher Information Matrix (FIM), which quantifies the worst-case sensitivity of the model's output distribution to input perturbations. Theoretically, we establish that the FIM equals the variance of the input Jacobian and derive closed-form spectral bounds for common architectures, including VGG, ResNet, DenseNet, and Transformer, providing the first theoretical robustness ranking. To enable scalable evaluation, we develop efficient algorithms, including power iteration and Hutchinson-based estimation, that support both white-box and black-box settings. Extensive experiments across multiple datasets, including CIFAR, ImageNet, and medical images, and across multiple architectures show a strong correlation between our metric and adversarial vulnerability. Our framework serves as an interpretable diagnostic tool that complements attack-based evaluations, offering insights into architectural sensitivity and guiding the design of more robust models. Code is available at: this https URL.

---


### 185. [Coarse-to-fine Hierarchical Architecture with Sequential Mamba for Brain Reconstruction](https://arxiv.org/abs/2606.04772)

**<font color=#1a73e8>作者：</font>** Hoang-Son Vo, Van-Hung Bui, Minh-Huy Mai-Duc 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding the relationship between deep visual representations and the human visual system is a fundamental challenge in computational neuroscience. While modern vision models achieve strong performance in image recognition, their correspondence with the hierarchical organization of the human visual cortex remains an open question. In this study, we propose CHASMBrain, a novel hierarchical two-stage framework for image-to-fMRI encoding. Our architecture leverages a dual-stream Mamba design to explicitly separate and process global semantic tokens and local spatial patches, motivated by the functional organization of the visual cortex. A coarse-to-fine strategy is employed: Stage 1 predicts denoised ROI-level activations, while Stage 2 refines these coarse responses into full voxel-level predictions using a Mamba-VAE. Experiments on the Natural Scenes Dataset (NSD) demonstrate that our method achieves a Pearson correlation of 0.429 and an MSE of 0.261, outperforming all evaluated baselines including ridge regression and DINOv2 linear probes. Beyond predictive performance, causal branch-ablation experiments reveal an asymmetric specialization: the patch stream is specifically locked to early visual cortex (retinotopic regions), while the CLS stream contributes broader semantic context to higher-order areas -- a correspondence that holds causally, not merely correlationally. Cross-subject transfer experiments further show that the learned backbone generalizes across individuals with minimal per-subject adaptation, suggesting the model captures a shared, subject-agnostic visual representation.

---


### 186. [Activation Steering of Video Generation Models via Reduced-Order Linear Optimal Control](https://arxiv.org/abs/2606.04775)

**<font color=#1a73e8>作者：</font>** Jihoon Hong, Alice Chan, Qiyue Dai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Text-to-video (T2V) models trained on large-scale web data can generate undesired content, motivating interventions that reduce harmful outputs without sacrificing visual quality. Activation steering offers an attractive mechanistic alternative to finetuning and prompt filtering, but existing T2V steering methods remain limited, typically applying coarse, non-anticipative interventions that can lead to oversteering and content degradation. To close this gap, we propose Latent Activation Linear-Quadratic Regulator (LA-LQR), a reduced-order optimal control framework for minimally invasive T2V steering. LA-LQR formulates T2V inference as a dynamical system and computes closed-loop feedback interventions that steer activations toward desired feature setpoints while penalizing unnecessary perturbations. To make optimal control feasible for high-dimensional video activations, we project activations onto a low-dimensional, task-relevant subspace derived from contrastive prompt pairs, estimate local linear dynamics in this latent space, and solve a latent LQR problem to obtain timestep- and layer-specific steering signals. We provide theoretical bounds relating latent setpoint tracking to raw activation-space feature control, and empirically validate the fidelity of the reduced latent dynamics. On concept steering and video safety benchmarks, LA-LQR reduces unsafe generations relative to baselines, while preserving prompt fidelity and visual quality.

---


### 187. [UniFair: A unified fair clustering approach based on separation and compactness](https://arxiv.org/abs/2606.04777)

**<font color=#1a73e8>作者：</font>** Antonia Karra, Vasiliki Papanikou, Georgios Vardakas 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clustering is increasingly used to support high-impact decisions, yet standard objectives such as $k$-means can produce clusterings that treat demographic groups unequally. Existing fair clustering methods typically optimize a single notion of fairness and often overlook how clustering costs interact with the geometry of the induced decision boundaries. We propose \textsc{UniFair}, a unified framework that jointly optimizes \emph{separation fairness} and \emph{social fairness}. Separation fairness encourages protected groups to lie farther from the induced decision boundaries, while social fairness reduces disparities in within-cluster distortion by penalizing group-wise clustering costs. We develop gradient-based optimization procedures for separation-fair and unified $k$-means objectives, and extend them to deep clustering by enforcing the same criteria in the latent space of an autoencoder. Experiments on tabular and image datasets show that \textsc{UniFair} reduces both boundary-related and cost-based group disparities with only a modest increase in clustering loss.

---


### 188. [Tree-Based Formalization of Multi-Agent Complementarity in Human-AI Interactions](https://arxiv.org/abs/2606.04779)

**<font color=#1a73e8>作者：</font>** Andrea Ferrario  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Complementarity is the case in which a human--AI interaction (HAI) outperforms the best prediction benchmark available among its members. Although this idea is central in HAI research, formal work on complementarity remains limited. Existing frameworks do not model how agents' predictions compose into workflow-sensitive multi-agent protocols. We close this gap by introducing a tree-based formalization of complementarity in multi-agent HAI. An HAI protocol is represented by an ordered agent-role configuration together with a rooted planar binary tree whose leaves are decorated by prediction vectors. A local binary composition rule is evaluated recursively along the tree, yielding a tree-relative complementarity functional relative to a pointwise-min oracle benchmark. We prove four results. First, selector-based HAIs, including self- or AI-reliance, cannot achieve complementarity regardless of task, loss, or prediction quality. Second, in regression under squared loss, complementarity is equivalent to Euclidean distance minimization from the ground-truth vector; for $N=2$, the optimal linear-pooling weight has a closed form and a residual-correction interpretation. Third, under linear local composition, every protocol tree defines a barycentric coordinate chart on the simplex of leaf weights; Tamari-cover reparameterizations of protocol trees preserve complementarity, and for $N=4$, they satisfy the pentagon identity. Fourth, in binary classification, no internal local composition can achieve complementarity under endpoint-monotone losses, including standard Bregman and many finite Bernoulli $f$-divergence losses; an analogous obstruction holds for multiclass aggregation under cross-entropy. In summary, our framework shows that complementarity is attainable in multi-agent regression, but obstructed in classification under natural conditions on local aggregation and loss functions.

---


### 189. [AIP: A Graph Representation for Learning and Governing Agent Skills](https://arxiv.org/abs/2606.04781)

**<font color=#1a73e8>作者：</font>** Zachary Blumenfeld, Jim Webber  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent Skills today consist largely of free-form prose requiring the agent to read, interpret, and re-derive how to act in every session. This imposes two compounding costs: reduced reliability on implementation-heavy tasks, and difficulty in skill creation and improvement, since editing prose is a fragile process that both humans and agents struggle with, particularly for domain-specific procedural knowledge underrepresented in model training. The Agent Instruction Protocol (AIP) addresses both by modeling a skill as a directed execution graph: discrete steps as nodes backed by deterministic scripts or natural-language descriptions, connected by explicit typed input/output edges, and governed by a schema-validated YAML specification. A compiler meta-skill translates existing human-written skills into this form. The benefits are twofold. First, compiling human-written skills to AIP raised Claude Sonnet's mean task reward from 0.60 to 0.71 and pass rate from 53% to 67% across 27 real agent tasks from SkillsBench - a statistically significant gain (Wilcoxon signed-rank p = 0.011), winning 12 tasks to 2 with 13 ties - often in less wall-clock time. The graph delivers vetted, runnable units to the agent rather than asking it to re-derive code, commands, and tool calls from natural language. Second, on creation and improvement, because each skill is schema-validated, functionally testable, and addressable node-by-node, failures can be diagnosed and repaired precisely. Two authored-skill failures were traced to the script level. After adjusting the AIP spec and recompiling, both recovered with zero regressions (one task going from 0/5 to 5/5), turning skill improvement into a measurable tuning loop rather than a prose rewrite. That same graph structure supports corpus-level governance and skill introspection, and provides a natural action space for reinforcement learning over skills.

---


### 190. [Z-FLoc: Zero-Shot Floorplan Localization via Geometric Primitives](https://arxiv.org/abs/2606.04788)

**<font color=#1a73e8>作者：</font>** Ayumi Umemura, Toshinori Kuwahara, Marc Pollefeys 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual localization -- estimating a camera pose within a pre-existing map -- is a fundamental problem in computer vision.
Floorplans are an attractive map representation: they are readily available for most buildings, compact, and inherently invariant to visual appearance changes.
However, bridging the severe domain gap between camera observations and floorplan geometry remains challenging.
Existing methods address this gap through data-driven learning, yet they require large-scale training data and environment-specific retraining, limiting their practical deployment.
We propose a zero-shot floorplan localization method that generalizes to novel environments without any retraining.
Our key insight is that dominant geometric primitives -- lines and circles -- are ubiquitous in human-made environments and provide appearance-invariant structural constraints.
We extract these primitives from a bird's-eye-view (BEV) projection of monocular 3D reconstructions and match them to the floorplan via dedicated minimal solvers within a robust estimation framework.
Experiments on both simulated and real-world datasets show that our approach outperforms state-of-the-art learning-based methods on unseen environments, while using a single fixed set of hyperparameters across all experiments.
The source code will be made publicly available.

---


### 191. [Crafting Your Evolving Dreams: Concept-Incremental Versatile Customization](https://arxiv.org/abs/2606.04797)

**<font color=#1a73e8>作者：</font>** Jiahua Dong, Wenqi Liang, Hongliu Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Custom diffusion models (CDMs) have garnered significant interest owing to their remarkable capacity for generating personalized concepts. However, the majority of CDMs unrealistically presume that the user's collection of personalized concepts is static and incapable of incremental growth over time. Furthermore, they exhibit significant catastrophic forgetting and concept neglect of previously learned concepts when incrementally learning a sequence of new ones. To resolve the above challenges, we develop a novel Continually Customizable Diffusion Model (CCDM), enabling users to perform concept-incremental versatile customization. Specifically, we design an attribute-decoupled LoRA (AD-LoRA) module and a relevance-guided AD-LoRA aggregation strategy to mitigate catastrophic forgetting. They can preserve concept-specific attributes of each task and leverage beneficial inter-task correlations to enhance the continual learning of new customization tasks. Additionally, to address the challenge of concept neglect, we propose a controllable regional context synthesis strategy that performs multi-concept composition in alignment with user-provided conditions. This strategy enhances the overall consistency in multi-concept synthesis by guaranteeing semantic independence between user-defined regions and their smooth boundary transitions. Experiments show our CCDM exhibits significant improvements over baseline methods.

---


### 192. [Uncertainty-Aware (Un)Supervised Few-Shot User Adaptation for On-Device Personalized Human Activity Recognition](https://arxiv.org/abs/2606.04798)

**<font color=#1a73e8>作者：</font>** Maximilian Burzer, Till Riedel, Michael Beigl 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sensor-based Human Activity Recognition (HAR) models often degrade on unseen users due to domain shifts caused by individual movement patterns and sensor placement. Practical wearable HAR systems therefore require personalization methods that are lightweight, applicable whether calibration data is labeled, unlabeled, or unavailable, and robust under limited calibration. We present a gradient-free framework that repurposes pretrained HAR classifiers as Prototypical Networks using using prior prototypes, which preserve zero-shot performance and regularize adaptation. For labeled calibration, we introduce closed-form Bayesian prototype estimation and extend the same principle to unlabeled calibration. With only 3 seconds of calibration data per activity (one shot), supervised adaptation improves macro-F1 by +2.76 to +33.44 percentage points across four datasets, while unsupervised adaptation improves by +0.56 to +32.13 points. Since adaptation requires only closed-form prototype updates, the framework enables efficient and robust on-device personalization of preexisting HAR classifiers.

---


### 193. [Fast Cubical Persistent Homology on 2D and 3D Images via Union-Find, Pruning, and Lookup Tables](https://arxiv.org/abs/2606.04801)

**<font color=#1a73e8>作者：</font>** Titouan Le Breton, Karol Szustakowski, Marie Piraud  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Flash Cubical, a highly efficient computation of cubical persistence on a V-filtration for 2D and 3D images over $\mathbb{F}_2$. The implementation is built around three core ideas. First, cubical complexes satisfy properties that allow for the computation of persistence of the highest dimension via union-find and duality. Second, pruning of certain edges allows for a fast and efficient implementation of union-find. Third, the use of a lookup table, which exploits the regularity of cubical complexes to pre-compute local information. This avoids the need to compute local information at run time. To the best of our knowledge, this is the most efficient implementation of cubical persistence with a V-filtration, both in terms of time and memory costs. Although the paper focuses on persistence for V-filtration cubical complexes, the underlying ideas generalise naturally to T-filtrations on cubical complexes and suggest promising directions for other complexes.

---


### 194. [The Right Measure for Physics-Constrained Generation: A Co-Area Correction for Posterior-Consistent PDE Inverse Problems](https://arxiv.org/abs/2606.04804)

**<font color=#1a73e8>作者：</font>** Jian Xu, Delu Zeng, John Paisley 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models -- diffusion and flow matching -- are increasingly used to solve partial differential equation (PDE) inverse problems, enforcing the governing physics as a \emph{hard constraint} (via projection or guidance) and reporting the resulting samples as a Bayesian posterior with calibrated uncertainty. We show that this widely adopted recipe samples the wrong distribution. Conditioning a generative prior on a hard PDE constraint is conditioning on a measure-zero manifold -- an operation that is intrinsically ambiguous (the Borel--Kolmogorov paradox) and whose physically correct resolution, the small-residual-noise limit, carries a co-area (Fixman) Jacobian factor $[det(JJ^{\top})]^{-1/2}$ that projection- and guidance-based methods silently omit. We make the bias precise, show that it grows with the heterogeneity of the constraint sensitivity, and validate it on controlled problems against an \emph{i.i.d.} ground-truth arbiter. The omitted factor is not a second-order detail: removing it inflates the posterior error to $20\times$ the sampling-noise floor; minimal-displacement projection (as in PCFM) is biased at $9\times$ the floor; and a naive scalar reweighting does not fix it. We introduce \textbf{CoCoS}, a measure-aware constrained sampler that targets the correct co-area posterior, and show that it matches the gold-standard posterior to within sampling noise. Our results imply that ``satisfying the physics'' is not the same as ``sampling the posterior,'' and give a principled correction for uncertainty-aware scientific inference.

---


### 195. [Dream.exe: Can Video Generation Models Dream Executable Robot Manipulation?](https://arxiv.org/abs/2606.04811)

**<font color=#1a73e8>作者：</font>** Rui Zhao, Kaiming Yang, Jifeng Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation models have made impressive strides in synthesizing visually compelling content, yet their outputs remain confined to the virtual domain. A natural question follows: how well do these models reflect the physical world when their generated videos leave the screen and enter reality? We propose robotic manipulation as a concrete, measurable window onto this question: if a model has truly internalized physical laws, the motion it depicts should translate into executable robot behavior. We introduce this http URL, an evaluation framework that operationalizes this criterion through a video-to-execution pipeline. Given a scene image and a task description, this http URL synthesizes a manipulation video, converts the generated motion into robot trajectories, and executes them in a physics simulator, yielding a grounding signal that purely visual metrics cannot offer. Using this pipeline, we evaluate 8 models spanning frontier closed-source generators, open-source generators, and robot-specific models. Our benchmark covers 101 manually curated manipulation tasks at three levels of physical complexity, measured across visual quality, trajectory fidelity, and execution success. Encouragingly, several models achieve measurable execution success, suggesting that generative priors learned from internet-scale data already encode meaningful physical knowledge. Yet visual quality proves a poor predictor of executability, exposing a dimension of model capability that standard visual evaluations do not capture. this http URL will be open-sourced at this https URL.

---


### 196. [Scenario Generation for Risk-Aware Reinforcement Learning with Probably Approximately Safe Guarantees](https://arxiv.org/abs/2606.04812)

**<font color=#1a73e8>作者：</font>** Mohit Prashant, Arvind Easwaran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Guaranteeing safety is critical to the deployment of reinforcement learning (RL) agents in the real-world, especially as policies learned using deep RL may demonstrate susceptibility to transition perturbations that result in unknown or unsafe behaviour. A method of policy verification is to construct probabilistic barrier-certificates by sampling policy trajectories with respect to safety constraints, thereby demarcating known safe behaviour from unknown behaviour. Obtaining tight upper and lower bounds on the probability of violation of these constraints may be difficult if the policy is susceptible to transition uncertainty or perturbation that places the agent in insufficiently explored states. To address this, we approximate the distribution of the encountered state-space using a variational autoencoder (VAE) and construct upper and lower-bound barrier-certificates using latent characteristics of states to optimize for regions of known, safe behaviour with high confidence. We frame this in our work as a dual optimization problem where the lower-bound barrier-certificate presents a more conservative estimate of the safe region than the upper-bound barrier-certificate. Sampling states that lie within the set difference of the two during training, i.e. the non-robust region, allows us to tighten the upper and lower bounds to provide sharper probabilistic guarantees on safety. Within our study, we describe the guarantees placed and demonstrate the tightness of our bounds experimentally.

---


### 197. [The Usefulness Gap in Proof-of-Useful-Work: An Empirical Study of Pearl's cuPOW Protocol](https://arxiv.org/abs/2606.04819)

**<font color=#1a73e8>作者：</font>** Abhinaba Basu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Pearl, a Layer-1 blockchain with high-profile AI industry endorsements, markets its Proof-of-Useful-Work (PoUW) protocol as simultaneously securing the network and performing AI inference. We present the first systematic empirical measurement of a deployed PoUW system, finding that Pearl's 24 EH/s network -- representing approximately 320,000 GPU-equivalents consuming an estimated 112 MW -- produces zero useful AI computation. Budget GPU rental prices rose 38% and utilization surged from 57% to 94% following the mining software's public release, displacing legitimate research workloads.
Our measurements span five dimensions: (1) network composition analysis of 8,012 workers shows all have inference-capable hardware, yet the dominant mining software contains no inference code; (2) the verification protocol accepts random matrices by design, confirmed by 44 pool-accepted shares from our open-source miner across NVIDIA, AMD, CPU, and Apple Silicon hardware; (3) statistical distribution checks are trivially defeated by adversarial Gaussian sampling; (4) mining is unprofitable at current PRL prices ($0.21) across all GPU tiers (-54% to -72% ROI); and (5) the mining computation is commodity integer arithmetic portable to any hardware platform, offering no vendor lock-in. These findings quantify the verifiability-usefulness tension identified theoretically by Leinweber et al., providing concrete measurements of its magnitude and economic consequences in a deployed system.

---


### 198. [OA-CutMix: Correcting the Label Bias of CutMix](https://arxiv.org/abs/2606.04820)

**<font color=#1a73e8>作者：</font>** Tobias Christian Nauen, Stanislav Frolov, Federico Raue 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> CutMix has become the de facto standard mixing augmentation, yet its label assignment rests on a flawed assumption: The area of the pasted patch faithfully reflects its semantic contribution to the mixed image. In practice, however, patches frequently land on background regions, assigning label credit to classes whose objects are not visible. The mean discrepancy of the CutMix label and the semantic object area is $21.5\%$. In $17\%$ of samples an image contributes zero visible object pixels yet receives nonzero label weight. We propose Object-Aware CutMix (OA-CutMix), which corrects this bias by replacing the area-based CutMix weight with one derived from precomputed segmentation masks, assigning labels in proportion to the visible object area each image contributes to the mix. The image mixing procedure is left entirely unchanged. We evaluate OA-CutMix against 10+ static and dynamic mixing methods across 4 architectures and 6 datasets. OA-CutMix consistently achieves the highest accuracy over all tasks, outperforming even dynamic mixing methods, but at a fraction of the training-time cost. Improvements are largest for small objects, where the label bias from CutMix is greatest. Thus, correcting the label is sufficient to match or exceed the performance of methods modifying the image mixing algorithm.

---


### 199. [Reconciling Causality and Non-Equilibrium Thermodynamics with Hamiltonian Causal Models](https://arxiv.org/abs/2606.04822)

**<font color=#1a73e8>作者：</font>** Dario Rancati, Max Welling, Francesco Locatello  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal modeling of physical temporal phenomena must handle interventions that act along trajectories, nonstationary induced laws, path-dependent effects, and feedback mediated by dynamics, all challenging in standard causal models. We introduce Hamiltonian Causal Models (HCMs), a trajectory-level framework in which observed variables interact with local environments and interventions act as controls of Hamiltonian mechanisms. HCMs separate immutable equations of motion from intervenable mechanisms and define causal effects as discrepancies between interventional path laws. A key motivation for HCMs is their natural interface with non-equilibrium thermodynamics. Entropy production quantifies the irreversibility of a process and is a central causal observable: it is estimable from data and witnesses causal effects along the system's evolution that are invisible to endpoint and cumulative versions of the standard average treatment effect. As in physics, cause and effect are not primitives of the relation between two random variables but arise from the non-invertibility of the thermodynamic arrow. With this, our paper reconciles the language of statistical causal models and non-stationary thermodynamics, offering new tools to describe causality in a wide range of physical systems.

---


### 200. [A French Corpus Annotated for Multiword Expressions with Adverbial Function](https://arxiv.org/abs/2606.04828)

**<font color=#1a73e8>作者：</font>** Eric Laporte, Takuya Nakamura, Stavroula Voyatzi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents a French corpus annotated for multiword expressions (MWEs) with adverbial function. This corpus is designed for investigation on information retrieval and extraction, as well as on deep and shallow syntactic parsing. We delimit which kind of MWEs we annotated, we describe the resources and methods we used for the annotation, and we briefly comment the results. The annotated corpus is available at this http URL under the LGPLLR license.

---


> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-265](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
