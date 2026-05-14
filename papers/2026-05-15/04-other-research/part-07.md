# 📦 其他研究 | 2026年05月15日

> 本类共 **328** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-328**（第 7/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-328**

---

### 301. [Coordinating Multiple Conditions for Trajectory-Controlled Human Motion Generation](https://arxiv.org/abs/2605.13729)

**<font color=#1a73e8>作者：</font>** Deli Cai, Haoyang Ma, Changxing Ding  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Trajectory-controlled human motion generation aims to synthesize realistic human motions conditioned on both textual descriptions and spatial trajectories. However, existing methods suffer from two critical limitations: first, the conflict between text and trajectory conditions disrupts the denoising process, resulting in compromised motion quality or inaccurate trajectory following; second, the use of redundant motion representations introduces inconsistencies between motion components, leading to instability during trajectory control. To address these challenges, we propose CMC, a decoupled framework that effectively coordinates text and trajectory conditions through a divide-and-conquer strategy. CMC follows a divide-and-conquer paradigm, comprising two cascaded stages: Trajectory Control and Motion Completion. In the first stage, a diffusion model generates a simplified representation of the controlled joints under trajectory guidance, based on the given trajectories, ensuring accurate and stable trajectory following. In the second stage, a text-conditioned diffusion inpainting model generates full-body motions using the simplified representation from the first stage as partial observations. To mitigate overfitting caused by limited inpainting training data, we further introduce the Selective Inpainting Mechanism (SIM), which alternates between text-to-motion generation and motion inpainting tasks during training. Experiments on HumanML3D and KIT datasets demonstrate that CMC achieves state-of-the-art performance in control accuracy and motion quality, demonstrating its effectiveness in coordinating multimodal conditions and representations.

---


### 302. [Robust and Explainable Bicuspid Aortic Valve Diagnosis Using Stacked Ensembles on Echocardiography](https://arxiv.org/abs/2605.13730)

**<font color=#1a73e8>作者：</font>** Christos Chrysanthos Nikolaidis, Vasileios Sachpekidis, Nikolas Moustakidis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transthoracic echocardiography (TTE) is the first-line imaging modality for diagnosing bicuspid aortic valve (BAV), yet diagnostic performance varies with operator expertise and image quality. We developed an explainable AI model that distinguishes BAV from tricuspid aortic valves (TAV) using routinely acquired parasternal long-axis (PLAX) cine loops. A multi-backbone video ensemble was trained and evaluated using a leakage-aware, stratified outer cross-validation protocol on $N{=}90$ patient studies (48 BAV, 42 TAV). Across fixed outer splits and 10 random seeds, the calibrated stacked ensemble achieved an outer-CV F1-score of $0.907$ and recall of $0.877$. Frame-level Grad-CAM localized salient evidence to the aortic root and leaflet plane, while globally aggregated SHAP values quantified each video backbone's contribution to the stacked prediction, enabling transparent, case-level auditability. These findings indicate that PLAX-based video ensembles can support reliable BAV/TAV classification from routine echocardiographic cine loops and may facilitate earlier detection in non-specialist or resource-limited clinical settings.

---


### 303. [Distinguishing performance gains from learning when using generative AI](https://arxiv.org/abs/2605.13731)

**<font color=#1a73e8>作者：</font>** Lixiang Yan, Samuel Greiff, Jason M. Lodge 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative artificial intelligence (AI) is increasingly being integrated into education, where it can boost learners' performance. However, these uses do not promote the deep cognitive and metacognitive processing that are required for high-quality learning.

---


### 304. [Aligning Network Equivariance with Data Symmetry: A Theoretical Framework and Adaptive Approach for Image Restoration](https://arxiv.org/abs/2605.13744)

**<font color=#1a73e8>作者：</font>** Feiyu Tan, Qi Xie, Zongben Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image restoration is an inherently ill posed inverse problem. Equivariant networks that embed geometric symmetry priors can mitigate this ill posedness and improve performance. However, current understanding of the relationship between network equivariance and data symmetry remains largely heuristic. Particularly for real world data with imperfect symmetry, existing research lacks a systematic theoretical framework to quantify symmetry, select transformation groups, or evaluate model data alignment. To bridge this gap, we conduct an analysis from an optimization perspective and formalize the intrinsic relationship among data symmetry priors, model equivariance, and generalization capability. Specifically, we propose for the first time a quantifiable definition of non strict symmetry at the dataset level (rather than sample level) and use it as a constraint to formulate the restoration inverse problem. We then show that the equivariance for restoration models can be naturally derived from this inverse problems incorporated the proposed symmetry constraints, and that the equivariance error of the optimal restoration operator is strictly bounded by the data symmetry error and the discretization mesh size. Furthermore, by analyzing the network's empirical risk, we demonstrate that aligning equivariance with data symmetry optimizes the bias variance trade off, minimizing the total expected risk. Guided by these insights, we propose a Sample Adaptive Equivariant Network that uses a hypernetwork and transformation learnable equivariant convolutions to dynamically align with each sample's inherent symmetry. Extensive experiments on super resolution, denoising, and deraining validate our theoretical findings and show significant superiority over standard baselines and traditional equivariant models. Our code and supplementary material are available at this https URL.

---


### 305. [Weakly-Supervised Spatiotemporal Anomaly Detection](https://arxiv.org/abs/2605.13746)

**<font color=#1a73e8>作者：</font>** Urvi Gianchandani, Praveen Tirupattur, Mubarak Shah  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we explore a weakly supervised method for anomaly detection. Since annotating videos is time-consuming, we only look at weak video-level labels during training. This means that given a video, we know that it is either normal or contains an anomaly, but no further annotations are used to train the network. Features are extracted from video clips that are either normal or anomalous. These features are used to determine anomaly scores for spatiotemporal regions of the clips based on a classifier and the implementation of a multiple instance ranking loss (MIL). We represent both anomalous and normal video clips as positive and negative bags, respectively, to apply MIL. Furthermore, since anomalies are usually localized to a part of a frame rather than the whole frame, we chose to explore temporal as well as spatial anomaly detection. We show our results on the UCF Crime2Local Dataset, which contains spatiotemporal annotations for a portion of the UCF Crime Dataset.

---


### 306. [Min Generalized Sliced Gromov Wasserstein: A Scalable Path to Gromov Wasserstein](https://arxiv.org/abs/2605.13753)

**<font color=#1a73e8>作者：</font>** Ashkan Shahbazi, Xinran Liu, Ping He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose min Generalized Sliced Gromov--Wasserstein (min-GSGW), a sliced formulation for the Gromov--Wasserstein (GW) problem using expressive generalized slicers. The key idea is to learn coupled nonlinear slicers that assign compatible push-forward values to both input measures, so that monotone coupling in the projected domain lifts to a transport plan evaluated against the GW objective in the original spaces. The resulting plan induces a GW objective value, and min-GSGW minimizes this cost directly in the original spaces. We further show that min-GSGW is rigid-motion invariant, a crucial property for geometric matching and shape analysis tasks. Our contributions are threefold: 1) we introduce generalized slicers into the sliced GW framework, 2) we construct a slicing-based efficient GW transport plan; and 3) we develop an amortized variant that replaces per-instance optimization with a learned slicer for unseen input pairs. We perform experiments on animal mesh matching, horse mesh interpolation, and ShapeNet part transfer. Results show that min-GSGW produces meaningful geometric correspondences and GW objective values at substantially lower computational cost than existing GW solvers.

---


### 307. [Generative Texture Diversification of 3D Pedestrians for Robust Autonomous Driving Perception](https://arxiv.org/abs/2605.13755)

**<font color=#1a73e8>作者：</font>** Arka Bhowmick, Enes Ozeren, Ahmed Abdullah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In recent years, autonomous driving has significantly in creased the demand for high-quality data to train 2D and 3D perception models for safety-critical scenarios. Real world datasets struggle to meet this demand as require ments continuously evolve and large-scale annotated data collection remains costly and time-consuming making syn thetic data a scalable, practical and controllable alterna tive. Pedestrian detection is among the most safety-critical tasks in autonomous driving. In this paper, we propose a simple yet effective method for scaling variability in 3D pedestrian assets for synthetic scene generation. Starting from a single 3D base asset, we generate multiple distinct pedestrian instances by synthesizing diverse facial textures and identity-level appearance variations using StyleGAN2 and automatically mapping them onto 3D meshes. This ap proach enables scalable appearance-level asset diversifica tion without requiring the design of new geometries for each instance. Using the assets, we construct synthetic datasets and study the impact of mixing real and synthetic data for RGB-based object detection. Through complementary ex periments, we analyze geometry-driven distribution shifts in point cloud perception for 3D object detection. Our findings demonstrate that controlled synthetic diversifica tion improves robustness in 2D detection while revealing the sensitivity of 3D perception models to geometric domain gaps. Overall, this work highlights how generative AI en ables scalable, simulation-ready pedestrian diversification through controlled facial texture synthesis, along with the benefits and limitations of cross-domain training strategies in autonomous driving pipelines.

---


### 308. [Fast and effective algorithms for fair clustering at scale](https://arxiv.org/abs/2605.13759)

**<font color=#1a73e8>作者：</font>** Claudio Mantuano, Manuel Kammermann, Philipp Baumann  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clustering is an unsupervised machine learning task that consists of identifying groups of similar objects. It has numerous applications and is increasingly used in fairness-sensitive domains where objects represent individuals, such as customers, employees, or students. We address a fair clustering problem in which objects belong to protected groups. The problem consists of partitioning the objects into a predefined number of clusters while attaining a user-defined target level of fairness, meaning that each protected group is sufficiently represented in each cluster. The objective is to minimize the clustering cost, defined as the sum of squared Euclidean distances between the objects and the centers of their clusters. Since clustering cost and fairness are generally in conflict, managing the trade-off between them is essential in practical applications. Existing methods provide limited control over this trade-off and either fail to scale to large datasets or, when they scale, produce low-quality solutions. We propose a general framework for fair clustering that provides precise control over the cost-fairness trade-off and introduce three heuristics based on it. The first heuristic focuses on solution quality and the flexibility to incorporate additional constraints, the second improves scalability while retaining high solution quality, and the third is designed for maximum scalability, producing solutions for instances with millions of objects in seconds. The proposed heuristics outperform existing approaches in comprehensive numerical experiments on benchmark datasets. The source code of our heuristics and instructions for reproducing the experiments are publicly available on GitHub.

---


### 309. [Toward AI-Driven Digital Twins for Metropolitan Floods: A Conditional Latent Dynamics Network Surrogate of the Shallow Water Equations](https://arxiv.org/abs/2605.13761)

**<font color=#1a73e8>作者：</font>** Phillip Si, Yuan Qiu, Omar Sallam 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI-driven flood digital twins demand fast hydrodynamic surrogates for ensemble forecasting and observation assimilation. Yet even GPU-accelerated two-dimensional shallow water equation (SWE) solvers still require $\sim 55$ minutes per $96$-hour run on a $\sim 4.2$-million-active-cell metropolitan basin (the Des~Plaines River basin at $30\,\mathrm{m}$ resolution), making such workloads prohibitive at native resolution. We present the Conditional Latent Dynamics Network (CLDNet): a low-dimensional latent neural ODE driven by rainfall, paired with a coordinate-based decoder conditioned on static terrain (elevation, slope, Manning roughness) that reconstructs depth and discharge at arbitrary query points. Pointwise decoding decouples memory from grid size and handles irregular watersheds natively, enabling metropolitan-scale training on a single compute node and direct queries at exact gauge coordinates without raster snapping. We evaluate CLDNet on a synthetic $250{,}000$-cell Texas benchmark and on a new Des~Plaines case study of $114$ real-rainfall Stage~IV storms whose reference simulator we validate against United States Geological Survey (USGS) gauges at the April~2013 flood-of-record (Nash--Sutcliffe efficiency $0.57$--$0.94$ on mean-recentered water-surface elevation). CLDNet roughly halves the relative root-mean-squared error of an unconditional baseline, outperforms regular-grid VAE--ConvLSTM and FNO baselines on the Texas benchmark (both presuppose a Cartesian grid and do not apply to the irregular Des~Plaines watershed), reaches a critical success index of $\approx 86\%$ at the $0.5\,\mathrm{m}$ inundation threshold, and produces a full $96$-hour basin-wide forecast in $\sim 29$ seconds -- a $\sim 115\times$ speedup.

---


### 310. [EconAI: Dynamic Persona Evolution and Memory-Aware Agents in Evolving Economic Environments](https://arxiv.org/abs/2605.13762)

**<font color=#1a73e8>作者：</font>** Annie Liu, Zane Cao, Lang Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The integration of large language models (LLMs) in economic simulations has significantly enhanced agent-based modeling, yet existing frameworks struggle to capture the interplay between short-term optimization and long-term strategic planning. Conventional approaches rely on static data-driven predictions, failing to incorporate adaptive behaviors influenced by economic sentiment, market volatility, and individual goals. To address these limitations, we introduce a novel EconAI framework, incorporating economic sentiment indexing (ESI), memory weighting, and dynamic decision-making mechanisms. By quantifying economic belief, adjusting historical data influence, and linking work-consumption behaviors, EconAI achieves a more human-like decision process, where agents adapt their actions based on both market signals and long-term objectives. It is the first LLM-powered simulation system that can simulate the macro/microeconomic environment and interactions in a unified framework. Empirical evaluations show that EconAI improves stability in economic responses, better replicates real-world employment-consumption cycles, and enhances overall decision robustness. This advancement marks a crucial step towards more realistic, adaptive economic agent simulations.

---


### 311. [VectorSmuggle: Steganographic Exfiltration in Embedding Stores and a Cryptographic Provenance Defense](https://arxiv.org/abs/2605.13764)

**<font color=#1a73e8>作者：</font>** Jascha Wanger  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern retrieval-augmented generation (RAG) systems convert sensitive content into high-dimensional embeddings and store them in vector databases that treat the resulting numerical artifacts as opaque. Major vector-store products do not provide native controls for embedding integrity, ingestion-time distributional anomaly detection, or cryptographic provenance attestation. We show this opens a class of steganographic exfiltration attacks: an attacker with write access to the ingestion pipeline can hide payload data inside embeddings using simple post-embedding perturbations (noise injection, rotation, scaling, offset, fragmentation, and combinations thereof) while preserving the surface-level retrieval behavior the RAG system exposes to legitimate users.
We evaluate these techniques across a synthetic-PII corpus on text-embedding-3-large, four locally hosted open embedding models, a cross-corpus replication on BEIR NFCorpus and a Quora subset (over 26,000 chunks combined), seven vector-store configurations, an adaptive-attacker variant of the detector evaluation, and a paraphrased-query retrieval benchmark. Distribution-shifting perturbations are often caught by simple anomaly detectors; small-angle orthogonal rotation defeats distribution-based detection across every (model, corpus) pair tested. A disjoint-Givens rotation encoder gives a closed-form per-vector capacity ceiling of floor(d/2) * b bits, but real embedding manifolds impose a capacity-detectability trade-off, and the retrieval-preserving operating point sits well below it.
We propose VectorPin, a cryptographic provenance protocol that pins each embedding to its source content and producing model via an Ed25519 signature over a canonical byte representation. Any post-embedding modification breaks signature verification. Embedding-level integrity is a deployable, standardizable control that closes this attack class.

---


### 312. [Dense vs Sparse Pretraining at Tiny Scale: Active-Parameter vs Total-Parameter Matching](https://arxiv.org/abs/2605.13769)

**<font color=#1a73e8>作者：</font>** Abdalrahman Wael  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study dense and mixture-of-experts (MoE) transformers in a tiny-scale pretraining regime under a shared LLaMA-style decoder training recipe. The sparse model replaces dense feed-forward blocks with Mixtral-style routed experts. Dense baselines are modestly width-resized to tightly match either active or total parameter budgets, while tokenizer, data, optimizer, schedule, depth, context length, normalization style, and evaluation protocol are held fixed. Our best sparse recipe uses four experts, top-2 routing, Switch-style load balancing, and router z-loss. In a three-seed full-data comparison, the dense active-match model reaches 1.6545 +/- 0.0012 best validation loss, the MoE reaches 1.5788 +/- 0.0020, and the dense total-match model reaches 1.5608 +/- 0.0025. This yields a matched-active gap of 0.0758 +/- 0.0021 in the MoE's favor and a matched-total gap of 0.0180 +/- 0.0020 in the dense model's favor. Across training, the matched-active advantage grows while the matched-total dense advantage narrows sharply. In this sub-25M-parameter regime, MoE therefore improves validation loss under active-parameter matching but does not surpass dense training at equal total stored capacity.

---


### 313. [Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry](https://arxiv.org/abs/2605.13772)

**<font color=#1a73e8>作者：</font>** Tyler Alvarez, Ali Baheri  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models hallucinate during multi-step reasoning, but most existing detectors operate at the trace level: they assign one confidence score to a full output, fail to localize the first error, and often require multiple sampled completions. We frame hallucination instead as a property of the hidden-state trajectory produced during a single forward pass. Correct reasoning moves through a stable manifold of locally coherent transitions; a first error appears as a localized excursion in transport cost away from this manifold. We operationalize this view with a label-conditioned teacher that builds a trace-specific contrastive PCA lens and scores each step with seven geometric transition features, and a deployable BiLSTM student distilled from the teacher that operates on raw hidden states without inference-time labels. We prove that contrastive PCA is the optimal projection for a transport-separation objective between first error and correct states, and that single-pass first error localization holds whenever the first error creates a positive transport margin over preceding correct transitions. On ProcessBench, PRM800K, HaluEval, and TruthfulQA, both models outperform entropy-based, probing-based, and attention-based baselines in-domain; the teacher transfers stably across language models and datasets, while the student collapses under shift, a gap our distillation theory predicts. These results recast step-level hallucination detection as a problem of trajectory dynamics and identify the central obstacle to deployment: preserving the contrastive transport margin under distribution shift.

---


### 314. [Attention Once Is All You Need: Efficient Streaming Inference with Stateful Transformers](https://arxiv.org/abs/2605.13784)

**<font color=#1a73e8>作者：</font>** Victor Norgren  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conventional transformer inference engines are request-driven, paying an O(n) prefill cost on every query. In streaming workloads, where data arrives continuously and queries probe an ever-growing context, this cost is prohibitive. We introduce a data-driven computational model centred on stateful sessions: a persistent KV cache advanced incrementally as new data arrives, so prefill is moved off the critical path and query latency becomes O(|q|), independent of accumulated context size. Building on this, Flash Queries reclaim idle GPU cycles between data arrivals to pre-evaluate registered questions and return cached answers before the user asks, a pattern that is structurally impossible in stateless engines because they discard intermediate state between requests. A multi-tenant continuous-batching scheduler with cell-budget admission and prefix-aware grouped prefill lets dozens of stateful sessions coexist on a single GPU while preserving full quadratic self-attention. On streaming market-data benchmarks the reference implementation achieves up to 5.9x speedup over conventional inference engines (vLLM, SGLang, TensorRT-LLM, this http URL), holding query latency constant as accumulated context grows.

---


### 315. [Interpretable Machine Learning for Antepartum Prediction of Pregnancy-Associated Thrombotic Microangiopathy Using Routine Longitudinal Laboratory Data](https://arxiv.org/abs/2605.13786)

**<font color=#1a73e8>作者：</font>** Chuanchuan Sun, Zhen Yu, Qin Fan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Background: Pregnancy-associated thrombotic microangiopathy (P-TMA) is rare but life-threatening. Early risk prediction before overt clinical presentation remains challenging, as the associated laboratory abnormalities are subtle, multidimensional, and frequently masked by common physiological changes such as gestational thrombocytopenia and pregnancy-related proteinuria, thus overlapping heavily with benign obstetric and renal conditions. This complexity is poorly captured by univariate or rule-based approaches; however, it is addressable by machine learning, which can extract latent, time-dependent risk signatures from longitudinal clinical tests. Methods: This retrospective study included 300 pregnancies comprising 142 P-TMA cases and 158 controls. After exclusion of identifiers and non-informative variables, 146 longitudinal laboratory predictors were retained. Participants were divided into a training cohort (80%) and a held-out test cohort (20%) using stratified sampling. Five algorithms were evaluated: logistic regression, support vector machine with radial basis function kernel, random forest, extra trees, and gradient boosting. The final model was selected by mean cross-validated AUROC, refitted on the full training cohort, and evaluated once in the held-out test cohort. Interpretability analyses examined global feature importance and distributional patterns of leading predictors. Results: Gradient boosting was prespecified by cross-validation in the training cohort. The model achieved an AUROC of 0.872 (95% CI: 0.769-0.952) and an AUPRC of 0.883 (95% CI: 0.780-0.959) in a held-out test cohort, with sensitivity of 0.750 and specificity of 0.812. Conclusions: Longitudinal clinical laboratory tests obtained during routine care contained informative and clinically plausible signals for P-TMA risk. Notably, cystatin C at week 6 showed promise as an early monitoring indicator.

---


### 316. [Force-Aware Neural Tangent Kernels for Scalable and Robust Active Learning of MLIPs](https://arxiv.org/abs/2605.13788)

**<font color=#1a73e8>作者：</font>** Eszter Varga-Umbrich, Zachary Weller-Davies, Paul Duckworth 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Active learning for machine-learning interatomic potentials (MLIPs) must address several challenges to be practical: scaling to large candidate pools, leveraging energy-force supervision, and maintaining robustness when candidate pools are biased relative to the target distribution. In this work, we jointly address these challenges. We first introduce a linearly scaling acquisition framework based on chunked feature-space posterior-variance shortlisting. By avoiding materialisation of the candidate and train set kernels, this approach enables screening of ~200k structures within hours and applies broadly to acquisition strategies that score candidates based on molecular similarity metrics. We then extend the Neural Tangent Kernel (NTK) to a force-aware setting via mixed parameter-coordinate derivatives, yielding a force NTK and a joint energy-force NTK that provide natural similarity metrics for vector-field prediction. We demonstrate the effectiveness of the joint energy-force NTK on the OC20 dataset, where force-aware acquisition is crucial: it achieves the lowest energy and force MAE and RMSE across all metrics and distribution splits. Across T1x, PMechDB, and RGD benchmarks, our force NTK methods remain competitive with established baselines while being significantly more efficient than committee-based approaches. Under a controlled candidate-pool shift case study on T1x, acquisition based on pretrained MLIP embeddings and NTKs remains robust, whereas committee-based methods exhibit higher variance. Overall, these results show that a single pretrained MLIP can enable scalable, force-aware, and distribution-robust active learning for foundation-model fine-tuning.

---


### 317. [ENSEMBITS: an alphabet of protein conformational ensembles](https://arxiv.org/abs/2605.13789)

**<font color=#1a73e8>作者：</font>** Kaiwen Shi, Carlos Oliver  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Protein structure tokenizers (PSTs) are workhorses in protein language modeling, function prediction, and evolutionary analysis. However, existing PSTs only capture local geometry of static structures, and miss the correlated motions and alternative conformational states revealed by protein ensembles. Here we introduce Ensembits, the first tokenizer of protein conformational ensembles. Ensembits address challenges inherent to tokenizing dynamics: deriving informative geometric descriptors across conformations, permutation-invariance encoding of variable-size ensembles, and conquering sparsity in dynamics data. Trained with a Residual VQ-VAE using a frame distillation objective on a large molecular dynamics corpus, Ensembits outperforms all related methods on RMSF prediction, and is the strongest standalone structural tokenizer on an token-conditioned ANOVA test on per-residue motion amplitude. Ensembits further matches or exceeds static tokenizers on EC, GO, binding site/affinity prediction, and zero-shot mutation-effect prediction despite using far less pretraining data. Notably, the distillation objective enables Ensembits to predict dynamics token from one single predicted structure, which alleviates dynamics data sparsity. As the field moves from static structure prediction toward ensemble generation, Ensembits offer the discrete vocabulary needed to bring dynamics into protein language modeling and design.

---


### 318. [Di-BiLPS: Denoising induced Bidirectional Latent-PDE-Solver under Sparse Observations](https://arxiv.org/abs/2605.13790)

**<font color=#1a73e8>作者：</font>** Zhonghao Li, Chaoyu Liu, Qian Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Partial differential equations (PDEs) are fundamental for modeling complex natural and physical phenomena. In many real-world applications, however, observational data are extremely sparse, which severely limits the applicability of both classical numerical solvers and existing neural approaches. While neural methods have shown promising results under moderately sparse observations, their inference efficiency at high resolutions is limited, and their accuracy degrades substantially in the extremely sparse regime. In this work, we propose the Di-BiLPS, a unified neural framework that effectively handle both forward and inverse PDE problems under extremely sparse observations. Di-BiLPS combines a variational autoencoder to compress high-dimensional inputs into a compact latent space, a latent diffusion module to model uncertainty, and contrastive learning to align representations. Operating entirely in this latent space, the framework achieves efficient inference while retaining flexible input-output mapping. In addition, we introduce a PDE-informed denoising algorithm based on a variance-preserving diffusion process, which further improves inference efficiency. Extensive experiments on multiple PDE benchmarks demonstrate that Di-BiLPS consistently achieves SOTA performance under extremely sparse inputs (as low as 3%), while substantially reducing computational cost. Moreover, Di-BiLPS enables zero-shot super-resolution, as it allows predictions over continuous spatial-temporal domains.

---


### 319. [EvoGround: Self-Evolving Video Agents for Video Temporal Grounding](https://arxiv.org/abs/2605.13803)

**<font color=#1a73e8>作者：</font>** Minjoon Jung, Byoung-Tak Zhang, Lorenzo Torresani  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video temporal grounding (VTG) takes an untrimmed video and a natural-language query as input and localizes the temporal moment that best matches the query. Existing methods rely on large, task-specific datasets requiring costly manual annotation. We introduce EvoGround, a framework of two coupled self-evolving agents, a proposer and a solver, that learn temporal grounding from raw videos without any human-labeled data. The proposer generates query--moment pairs from raw videos, while the solver learns to ground them and feeds back signals that improve the proposer in return. Through this self-reinforcing reinforcement-learning loop, the two agents are initialized from the same backbone and mutually improve across iterations. Trained on 2.5K unlabeled videos, EvoGround matches or surpasses fully supervised models across multiple VTG benchmarks, while emerging as a state-of-the-art fine-grained video captioner without manual labels.

---


### 320. [Provable Quantization with Randomized Hadamard Transform](https://arxiv.org/abs/2605.13810)

**<font color=#1a73e8>作者：</font>** Ying Feng, Piotr Indyk, Michael Kapralov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vector quantization via random projection followed by scalar quantization is a fundamental primitive in machine learning, with applications ranging from similarity search to federated learning and KV cache compression. While dense random rotations yield clean theoretical guarantees, they require $\Theta(d^2)$ time. The randomized Hadamard transform $HD$ reduces this cost to $O(d \log d)$, but its discrete structure complicates analysis and leads to weaker or purely empirical compression guarantees.
In this work, we study a variant of this approach: dithered quantization with a single randomized Hadamard transform. Specifically, the quantizer applies $HD$ to the input vector and subtracts a random scalar offset before quantizing, injecting additional randomness at negligible cost. We prove that this approach is unbiased and provides mean squared error bounds that asymptotically match those achievable with truly random rotation matrices. In particular, we prove that a dithered version of TurboQuant achieves mean squared error $\bigl(\pi\sqrt{3}/2 + o(1)\bigr) \cdot 4^{-b}$ at $b$ bits per coordinate, where the $o(1)$ term vanishes uniformly over all unit vectors and all dimensions as the number of quantization levels grows.

---


### 321. [JANUS: Anatomy-Conditioned Gating for Robust CT Triage Under Distribution Shift](https://arxiv.org/abs/2605.13813)

**<font color=#1a73e8>作者：</font>** Lavsen Dahal, Yubraj Bhandari, Geoffrey Rubin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated CT triage requires models that are simultaneously accurate across diverse pathologies and reliable under institutional shift. While Vision Transformers provide strong visual representations, many clinically significant findings are defined by quantitative imaging biomarkers rather than appearance alone. We introduce JANUS, a physiology-guided dual-stream architecture that conditions visual embeddings on macro-radiomic priors via Anatomically Guided Gating. On the MERLIN test set (N=5082), JANUS attains macro-AUROC 0.88 and AUPRC 0.74, outperforming all reproduced baselines. It generalizes to an external dataset N=2000; AUROC 0.87), with the largest gains on findings defined by size and attenuation as well as improved calibration on both datasets. We further quantify prediction suppression using the Physiological Veto Rate (PVR), showing that under domain shift JANUS reduces high-confidence false positives substantially more often than true positives. Together, these results are consistent with physically grounded conditioning that improves both discrimination and reliability in CT triage. Code is made publicly available at github repository this https URL and model weights are at this https URL.

---


### 322. [OmniLiDAR: A Unified Diffusion Framework for Multi-Domain 3D LiDAR Generation](https://arxiv.org/abs/2605.13815)

**<font color=#1a73e8>作者：</font>** Youquan Liu, Weidong Yang, Ao Liang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LiDAR scene generation is increasingly important for scalable simulation and synthetic data creation, especially under diverse sensing conditions that are costly to capture at scale. Typically, diffusion-based LiDAR generators are developed under single-domain settings, requiring separate models for different datasets or sensing conditions and hindering unified, controllable synthesis under heterogeneous distribution shifts. To this end, we present OmniLiDAR, a unified text-conditioned diffusion framework that generates LiDAR scans in a shared range-image representation across eight representative domains spanning three shift types: adverse weather, sensor-configuration changes (e.g., reduced beams), and cross-platform acquisition (vehicle, drone, and quadruped). To enable training a single model over heterogeneous domains without isolating optimization by domain, we introduce a Cross-Domain Training Strategy (CDTS) that mixes domains within each mini-batch and leverages conditioning to steer generation. We further propose Cross-Domain Feature Modeling (CDFM), which captures directional dependencies along azimuth and elevation axes to reflect the anisotropic scanning structure of range images, and Domain-Adaptive Feature Scaling (DAFS) as a lightweight modulation to account for structured domain-dependent feature shifts during denoising. In the absence of a public consolidated benchmark, we construct an 8-domain dataset by combining real-world scans with physically based weather simulation and systematic beam reduction while following official splits. Extensive experiments demonstrate strong generation fidelity and consistent gains in downstream use cases, including generative data augmentation for LiDAR semantic segmentation and 3D object detection, as well as robustness evaluation under corruptions, with consistent benefits in limited-label regimes.

---


### 323. [Uncertainty-Driven Anomaly Detection for Psychotic Relapse Using Smartwatches: Forecasting and Multi-Task Learning Fusion](https://arxiv.org/abs/2605.13816)

**<font color=#1a73e8>作者：</font>** Nikolaos Tsalkitzis, Panagiotis P.Filntisis, Petros Maragos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Digital phenotyping enables continuous passive monitoring of behavior and physiology, offering a promising paradigm for early detection of psychotic relapse. In this work, we develop and systematically study two smartwatch-based frameworks for daily relapse detection. The first forecasts cardiac dynamics and flags deviations between predicted and observed features as indicators of abnormality. The second adopts a multi-task formulation that fuses sleep with motion and cardiac-derived signals, learning time-aware embeddings and predicting measurement timing. Both pipelines use Transformer encoders and output a daily anomaly score, derived from predictive uncertainty estimated via an ensemble of multilayer perceptrons to improve robustness to real-world wearable variability. While each framework independently demonstrates strong predictive power, we show that they capture complementary physiological signatures. Consequently, we propose a late-fusion strategy that synergistically combines the anomaly signals from both architectures into a unified decision score. We benchmark our methodology on the 2nd e-Prevention Grand Challenge dataset, where our fused model achieves a 8% relative improvement over the competition-winning baseline. Our results, supported by extensive ablation studies, suggest that the integration of diverse digital phenotypes, cardiac, motion, and sleep, is essential for the high-fidelity detection of psychotic relapse in real-world settings.

---


### 324. [Reducing cross-sample prediction churn in scientific machine learning](https://arxiv.org/abs/2605.13826)

**<font color=#1a73e8>作者：</font>** Gordan Prastalo, Kevin Maik Jablonka  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific machine learning reports predictive performance. It does not report whether the same prediction would survive a different draw of training data. Across $9$ chemistry benchmarks, two classifiers trained on independent bootstraps of the same training set agree on aggregate accuracy to within $1.3\text{--}4.2$ percentage points but disagree on the class label of $8.0\text{--}21.8\%$ of test molecules. We call this gap \emph{cross-sample prediction churn}. The standard parameter-side techniques (deep ensembles, MC dropout, stochastic weight averaging) do not reduce this gap; two data-side methods do. The first is $K$-bootstrap bagging, which cuts the rate $40\text{--}54\%$ on every dataset at no accuracy cost ($K{\times}$-ERM compute). The second is \emph{twin-bootstrap}, our proposal: two networks trained jointly on independent bootstraps with a sym-KL consistency loss between their predictions, which at matched $2{\times}$-ERM compute reduces churn a further median $45\%$ beyond bagging-$K{=}2$. Cross-sample prediction churn deserves a column alongside predictive performance in scientific-ML benchmark reports, because without it the parameter-side and data-side methods are indistinguishable on the metric they actually differ on.

---


### 325. [Quantifying Sensitivity for Tree Ensembles: A symbolic and compositional approach](https://arxiv.org/abs/2605.13830)

**<font color=#1a73e8>作者：</font>** S. Akshay, Chaitanya Garg, Ashutosh Gupta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Decision tree ensembles (DTE) are a popular model for a wide range of AI classification tasks, used in multiple safety critical domains, and hence verifying properties on these models has been an active topic of study over the last decade. One such verification question is the problem of sensitivity, which asks, given a DTE, whether a small change in subset of features can lead to misclassification of the input. In this work, our focus is to build a quantitative notion of sensitivity, tailored to DTEs, by discretizing the input space of the model and enumerating the regions which are susceptible to sensitivity. We propose a novel algorithmic technique that can perform this computation efficiently, within a certified error and confidence bound. Our approach is based on encoding the problem as an algebraic decision diagram (ADD), and further splitting it into subproblems that can be solved efficiently and make the computation compositional and scalable. We evaluate the performance of our technique over benchmarks of varying size in terms of number of trees and depth, comparing it against the performance of model counters over the same problem encoding. Experimental results show that our tool XCount achieves significant speedup over other approaches and can scale well with the increasing sizes of the ensembles.

---


### 326. [QLAM: A Quantum Long-Attention Memory Approach to Long-Sequence Token Modeling](https://arxiv.org/abs/2605.13833)

**<font color=#1a73e8>作者：</font>** Hoang-Quan Nguyen, Sankalp Pandey, Khoa Luu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modeling long-range dependencies in sequential data remains a central challenge in machine learning. Transformers address this challenge through attention mechanisms, but their quadratic complexity with respect to sequence length limits scalability to long contexts. State-space models (SSMs) provide an efficient alternative with linear-time computation by evolving a latent state through recurrent updates, but their memory is typically formed via additive or linear transitions, which can limit their ability to capture complex global interactions across tokens. In this work, we introduce one of the first studies to leverage the superposition property of quantum systems to enhance state-based sequence modeling. In particular, we propose Quantum Long-Attention Memory (QLAM), a hybrid quantum-classical memory mechanism that can be viewed as a quantum extension of state-space models. Instead of maintaining a classical latent state updated through additive dynamics, QLAM represents the hidden state as a quantum state whose amplitudes encode a superposition of historical information. The state evolves through parameterized quantum circuits conditioned on the input, enabling a non-classical, globally update mechanism. In this way, QLAM preserves the recurrent and linear-time structure of SSMs while fundamentally enriching the memory representation through quantum superposition. Unlike attention mechanisms that explicitly compute pairwise interactions, QLAM implicitly captures global dependencies through the evolution of the quantum state, and retrieves task-relevant information via query-dependent measurements. We evaluate QLAM on sequential variants of standard image classification benchmarks, including sMNIST, sFashion-MNIST, and sCIFAR-10, where images are flattened into token sequences. Across all tasks, QLAM consistently improves over recurrent baselines and transformer-based models.

---


### 327. [Topology-Preserving Neural Operator Learning via Hodge Decomposition](https://arxiv.org/abs/2605.13834)

**<font color=#1a73e8>作者：</font>** Dongzhe Zheng, Tao Zhong, Christine Allen-Blanchette  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we study solution operators of physical field equations on geometric meshes from a function-space perspective. We reveal that Hodge orthogonality fundamentally resolves spectral interference by isolating unlearnable topological degrees of freedom from learnable geometric dynamics, enabling an additive approximation confined to structure-preserving subspaces. Building on Hodge theory and operator splitting, we derive a principled operator-level decomposition. The result is a Hybrid Eulerian-Lagrangian architecture with an algebraic-level inductive bias we call Hodge Spectral Duality (HSD). In our framework, we use discrete differential forms to capture topology-dominated components and an orthogonal auxiliary ambient space to represent complex local dynamics. Our method achieves superior accuracy and efficiency on geometric graphs with enhanced fidelity to physical invariants. Our code is available at this https URL

---


### 328. [R-DMesh: Video-Guided 3D Animation via Rectified Dynamic Mesh Flow](https://arxiv.org/abs/2605.13838)

**<font color=#1a73e8>作者：</font>** Zijie Wu, Lixin Xu, Puhua Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video-guided 3D animation holds immense potential for content creation, offering intuitive and precise control over dynamic assets. However, practical deployment faces a critical yet frequently overlooked hurdle: the pose misalignment dilemma. In real-world scenarios, the initial pose of a user-provided static mesh rarely aligns with the starting frame of a reference video. Naively forcing a mesh to follow a mismatched trajectory inevitably leads to severe geometric distortion or animation failure. To address this, we present Rectified Dynamic Mesh (R-DMesh), a unified framework designed to generate high-fidelity 4D meshes that are ``rectified'' to align with video context. Unlike standard motion transfer approaches, our method introduces a novel VAE that explicitly disentangles the input into a conditional base mesh, relative motion trajectories, and a crucial rectification jump offset. This offset is learned to automatically transform the arbitrary pose of the input mesh to match the video's initial state before animation begins. We process these components via a Triflow Attention mechanism, which leverages vertex-wise geometric features to modulate the three orthogonal flows, ensuring physical consistency and local rigidity during the rectification and animation process. For generation, we employ a Rectified Flow-based Diffusion Transformer conditioned on pre-trained video latents, effectively transferring rich spatio-temporal priors to the 3D domain. To support this task, we construct Video-RDMesh, a large-scale dataset of over 500k dynamic mesh sequences specifically curated to simulate pose misalignment. Extensive experiments demonstrate that R-DMesh not only solves the alignment problem but also enables robust downstream applications, including pose retargeting and holistic 4D generation.

---


> [!TIP]
> 当前位于：**301-328**（第 7/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-328**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
